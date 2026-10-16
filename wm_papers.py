#!/usr/bin/env python3
"""Fetch abstracts matching world-model AND hierarchy terms anonymously.

Outputs use title, abstract, keywords, and pdf_url. Search progress is checkpointed.
"""

import argparse
from contextlib import contextmanager
from datetime import datetime, timezone
import getpass
import json
import os
from pathlib import Path
import re
import sys
import time
from types import SimpleNamespace

from fetch_jepa_papers import (
    API_URL, ROOT, VENUE, fetch_active_submissions, is_active, paper_fields,
    report_fetch_error, venue_configuration, write_json,
)

LEGACY_SEARCH_TERMS = (
    "world model", "worldmodel", "world modeling", "world modelling",
)
SEARCH_TERMS = (
    "hierarchy", "hierarchical", "multiscale", "multi-scale", "subgoal",
    "subgoals", "nested", "pyramid", "matryoshka",
)
WORLD_MODEL_PATTERN = re.compile(r"world[\s_\-\u2010-\u2015]*(?:models?|modell?ing)\b", re.I)
HIERARCHY_PATTERN = re.compile(
    r"\bhierarch\w*\b"
    r"|\b(?:multi|cross)[\s_\-\u2010-\u2015]*scale\b"
    r"|\bmulti[\s_\-\u2010-\u2015]*resolution\b"
    r"|\bcoarse[\s\-\u2010-\u2015]+to[\s\-\u2010-\u2015]+fine\b"
    r"|\bmatryoshka\b"
    r"|\bsub[\s\-\u2010-\u2015]*goals?\b"
    r"|\b(?:latent|state)[\s\-]+pyramid\b"
    r"|\bnested[\s\-]+(?:latent[\s\-]+)?"
    r"(?:representations?|embeddings?|networks?|dropout)\b"
    r"|\btemporal[\s\-]+abstractions?\b",
    re.I,
)


def metadata_text(paper):
    keywords = paper.get("keywords") or []
    if isinstance(keywords, str):
        keywords = [keywords]
    return "\n".join(str(item) for item in [
        paper.get("title") or "", paper.get("abstract") or "", *keywords,
    ])


def matches_world_model(paper):
    return bool(WORLD_MODEL_PATTERN.search(metadata_text(paper)))


def matches_hierarchy(paper):
    text = metadata_text(paper)
    return bool(
        HIERARCHY_PATTERN.search(text)
        or (
            re.search(r"\bhigh[\s\-]+level\b", text, re.I)
            and re.search(r"\blow[\s\-]+level\b", text, re.I)
        )
    )


def select_papers(papers):
    world_models = [paper for paper in papers if matches_world_model(paper)]
    hierarchy = [paper for paper in world_models if matches_hierarchy(paper)]
    return world_models, hierarchy


def matches_combined(paper):
    return matches_world_model(paper) and matches_hierarchy(paper)


class SearchPaused(RuntimeError):
    """A saved server cooldown is still active; make no additional requests."""


def error_payload(exc):
    return exc.args[0] if exc.args and isinstance(exc.args[0], dict) else {}


def is_rate_limit(exc):
    error = error_payload(exc)
    return error.get("status") == 429 or error.get("name") == "RateLimitError"


def check_cooldown(state):
    reset_time = state.get("rate_limit_reset_utc")
    if reset_time:
        reset = datetime.fromisoformat(reset_time.replace("Z", "+00:00"))
        if datetime.now(timezone.utc) < reset:
            raise SearchPaused(f"OpenReview cooldown lasts until {reset_time}. Resume after that time.")


def search_active_world_models(
    client, venue, page_size=1000, checkpoint_path=None, request_delay=1.0, restart=False,
):
    """Retrieve hierarchy candidates and require BOTH categories in metadata."""
    checkpoint_path = Path(checkpoint_path) if checkpoint_path else None
    if checkpoint_path and checkpoint_path.exists() and restart:
        previous = json.loads(checkpoint_path.read_text(encoding="utf-8"))
        if previous.get("venue") == venue:
            check_cooldown(previous)
    if checkpoint_path and checkpoint_path.exists() and not restart:
        state = json.loads(checkpoint_path.read_text(encoding="utf-8"))
        if state.get("venue") != venue:
            raise ValueError("Checkpoint belongs to a different search; use --restart or another --checkpoint")
        check_cooldown(state)
        if state.get("terms") == list(LEGACY_SEARCH_TERMS):
            backup = checkpoint_path.with_name(f"{checkpoint_path.stem}_world_models_backup.json")
            if backup.exists():
                stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%f")
                backup = backup.with_name(f"{backup.stem}_{stamp}.json")
            write_json(backup, state)
            retained = [item for item in state["matches"]
                        if matches_combined(paper_fields(SimpleNamespace(**item)))]
            state = {
                "venue": venue, "terms": list(SEARCH_TERMS),
                "invitation": state["invitation"], "statuses": state["statuses"],
                "query_index": 0, "offset": 0, "seen_ids": [], "matches": retained,
                "complete": False, "rate_limit_reset_utc": None,
            }
            write_json(checkpoint_path, state)
            print(f"Retained {len(retained)} combined matches; original cache preserved in {backup}.")
        elif state.get("terms") != list(SEARCH_TERMS):
            raise ValueError("Checkpoint belongs to a different search; use --restart or another --checkpoint")
        invitation, statuses = state["invitation"], state["statuses"]
        active = {item["id"]: SimpleNamespace(**item) for item in state["matches"]}
        if state.get("complete"):
            print("Using completed search checkpoint. Use --restart to refresh metadata.")
            return list(active.values())
        print(f"Resuming query {state['query_index'] + 1}, offset {state['offset']}.")
    else:
        invitation, statuses = venue_configuration(client, venue)
        state = {
            "venue": venue, "terms": list(SEARCH_TERMS), "invitation": invitation,
            "statuses": statuses, "query_index": 0, "offset": 0, "seen_ids": [],
            "matches": [], "complete": False, "rate_limit_reset_utc": None,
        }
        active = {}
        if checkpoint_path:
            write_json(checkpoint_path, state)

    def save():
        state["matches"] = [vars(item) for item in active.values()]
        if checkpoint_path:
            write_json(checkpoint_path, state)

    first_request = True
    while state["query_index"] < len(SEARCH_TERMS):
        term = SEARCH_TERMS[state["query_index"]]
        seen = set(state["seen_ids"])
        if not first_request and request_delay:
            time.sleep(request_delay)
        first_request = False
        try:
            notes = client.search_notes(
                term=term, content="all", group=venue, source="forum",
                limit=page_size, offset=state["offset"],
            )
        except Exception as exc:
            if is_rate_limit(exc):
                state["rate_limit_reset_utc"] = (error_payload(exc).get("details") or {}).get("resetTime")
            save()
            raise
        if not notes:
            state.update(query_index=state["query_index"] + 1, offset=0, seen_ids=[])
            save()
            continue
        identifiers = {note.id for note in notes}
        if not identifiers - seen:
            raise RuntimeError("Search returned a repeated page; export may be incomplete.")
        seen.update(identifiers)
        for note in notes:
            if (is_active(note, statuses) and invitation in (note.invitations or [])
                    and matches_combined(paper_fields(note))):
                # Save only the metadata needed for our four-field export.
                content = {key: note.content[key] for key in (
                    "title", "abstract", "keywords", "pdf", "venueid",
                ) if key in note.content}
                active[note.id] = SimpleNamespace(
                    id=note.id, content=content, ddate=None, replyto=None,
                    invitations=[invitation],
                )
        state["offset"] += len(notes)
        state["seen_ids"] = sorted(seen)
        state["rate_limit_reset_utc"] = None
        save()
    state["complete"] = True
    save()
    return list(active.values())


@contextmanager
def anonymous_environment():
    """The SDK implicitly reads login environment variables during construction."""
    names = ("OPENREVIEW_USERNAME", "OPENREVIEW_PASSWORD", "OPENREVIEW_TOKEN")
    previous = {name: os.environ.pop(name) for name in names if name in os.environ}
    try:
        yield
    finally:
        os.environ.update(previous)


def create_client(login=False):
    from openreview.api import OpenReviewClient
    from requests.adapters import HTTPAdapter
    if login:
        username = os.environ.get("OPENREVIEW_USERNAME") or input("OpenReview email/username: ").strip()
        password = os.environ.get("OPENREVIEW_PASSWORD") or getpass.getpass("OpenReview password: ")
        if not username or not password:
            raise ValueError("Both an OpenReview username and password are required")
        client = OpenReviewClient(baseurl=API_URL, username=username, password=password)
    else:
        with anonymous_environment():
            client = OpenReviewClient(baseurl=API_URL)
    # Surface 429 immediately instead of letting the SDK retry or sleep for an hour.
    client.session.mount(API_URL, HTTPAdapter(max_retries=0))
    return client


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--venue", default=VENUE)
    parser.add_argument("--mode", choices=("all", "search"), default="search",
                        help="all: scan all visible active notes; search: indexed candidates")
    parser.add_argument("--login", action="store_true", help="prompt for credentials once")
    parser.add_argument("--input", type=Path, help="process saved JSON without network access")
    parser.add_argument("--output", type=Path, default=ROOT / "hierarchy-wm.json")
    parser.add_argument("--hierarchy-output", type=Path, default=ROOT / "hierarchy-wm.json")
    parser.add_argument("--print-abstracts", action="store_true")
    parser.add_argument("--checkpoint", type=Path, help="search progress file; derived from --output by default")
    parser.add_argument("--restart", action="store_true", help="start a fresh search after any server cooldown")
    parser.add_argument("--page-size", type=int, default=1000)
    parser.add_argument("--request-delay", type=float, default=1.0, help="seconds between search requests")
    args = parser.parse_args(argv)
    if not 1 <= args.page_size <= 1000 or args.request_delay < 0:
        parser.error("--page-size must be 1..1000 and --request-delay must be nonnegative")
    report_output = args.hierarchy_output if args.input else args.output
    report_path = report_output.with_name(f"{report_output.stem}_source.json")
    checkpoint_path = args.checkpoint or args.output.with_name(f"{args.output.stem}_checkpoint.json")
    # Reuse metadata from the previous broad search instead of throwing it away.
    legacy_checkpoint = ROOT / "wm_papers_checkpoint.json"
    if (not args.input and not args.checkpoint and not checkpoint_path.exists()
            and args.output == ROOT / "hierarchy-wm.json" and legacy_checkpoint.exists()):
        checkpoint_path = legacy_checkpoint
    partial_path = args.output.with_name(f"{args.output.stem}_partial.json")
    target_path = args.hierarchy_output if args.input else args.output
    if target_path.resolve() == report_path.resolve():
        parser.error("Output and source report paths must be different")
    if args.input and args.input.resolve() in {args.hierarchy_output.resolve(), report_path.resolve()}:
        parser.error("Hierarchy output must not overwrite the input JSON")
    if not args.input and len({p.resolve() for p in (
        target_path, report_path, checkpoint_path, partial_path,
    )}) != 4:
        parser.error("Checkpoint, partial, and export paths must be distinct")

    written = []
    try:
        if args.input:
            papers = json.loads(args.input.read_text(encoding="utf-8"))
            if not isinstance(papers, list) or any(
                not isinstance(paper, dict)
                or set(paper) != {"title", "abstract", "keywords", "pdf_url"}
                for paper in papers
            ):
                raise ValueError("Input must be an array of title, abstract, keywords, and pdf_url records")
            source_kind = "saved_json"
            print(f"Processing saved JSON: {args.input}. Coverage is limited to this input.")
        else:
            client = create_client(args.login)
            if args.mode == "search":
                print("Using indexed candidates; this may miss papers absent from the search index.",
                      file=sys.stderr)
                notes = search_active_world_models(
                    client, args.venue, page_size=args.page_size,
                    checkpoint_path=checkpoint_path, request_delay=args.request_delay,
                    restart=args.restart,
                )
                source_kind = "indexed_search"
            else:
                notes = fetch_active_submissions(client, args.venue)
                source_kind = "all_visible_active_submissions"
            papers = [paper_fields(note) for note in notes]
            papers.sort(key=lambda paper: (paper["title"].casefold(), paper["pdf_url"] or ""))

        world_models, hierarchy = select_papers(papers)
        info = {
            "created_at_utc": datetime.now(timezone.utc).isoformat(),
            "source_kind": source_kind,
            "input_file": str(args.input.resolve()) if args.input else None,
            "venue": args.venue if not args.input else None,
            "records_examined": len(papers),
            "world_model_matches": len(world_models),
            "hierarchy_matches": len(hierarchy),
            "hierarchy_output": str(target_path),
            "selection_rule": "world-model terminology AND hierarchy-related terminology",
            "hierarchy_selection": "Broad metadata keyword screening; not main-paper review",
            "search_terms": list(SEARCH_TERMS) if source_kind == "indexed_search" else None,
        }
        exports = [(target_path, hierarchy)]
        for path, data in [*exports, (report_path, info)]:
            write_json(path, data)
            written.append(str(path))
    except Exception as exc:
        if is_rate_limit(exc) or isinstance(exc, SearchPaused):
            error = error_payload(exc)
            print(error.get("message") or str(exc), file=sys.stderr)
            reset = (error.get("details") or {}).get("resetTime")
            if reset:
                print(f"Server quota resets at {reset} (UTC).", file=sys.stderr)
            if checkpoint_path.exists():
                state = json.loads(checkpoint_path.read_text(encoding="utf-8"))
                if state.get("venue") == args.venue and not state.get("complete"):
                    partial = [paper_fields(SimpleNamespace(**item)) for item in state["matches"]]
                    partial = [paper for paper in partial if matches_combined(paper)]
                    write_json(partial_path, partial)
                    print(f"Saved {len(partial)} partial matches to {partial_path}.", file=sys.stderr)
                print(f"Progress: {checkpoint_path}", file=sys.stderr)
            print("Completed exports were preserved. Run the same command after cooldown to resume.",
                  file=sys.stderr)
            return 3
        result = report_fetch_error(exc)
        if written:
            print(f"Export incomplete; already written: {', '.join(written)}", file=sys.stderr)
        else:
            print("No new results were written; existing outputs were preserved.", file=sys.stderr)
        return result

    print(f"Records examined: {len(papers)}")
    print(f"World-model + hierarchy matches: {len(hierarchy)} -> {target_path}")
    print(f"Source and counts: {report_path}")
    if args.print_abstracts:
        for index, paper in enumerate(hierarchy, 1):
            print(f"{index}. {paper['title']}")
            print(f"   Abstract: {paper['abstract'] or '(not available)'}\n")
    if hierarchy:
        print(
            "Download all hierarchy candidates with:\n"
            f"  .venv/bin/python download_jepa_papers.py --login --input {target_path} "
            f"--limit {len(hierarchy)} --output-dir papers/wm_hierarchy"
        )
    else:
        print("No hierarchy candidates matched this input.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
