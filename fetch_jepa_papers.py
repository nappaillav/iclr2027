#!/usr/bin/env python3
"""Fetch active JEPA submissions from OpenReview API v2.

The default output is a JSON array, despite the requested .md extension.
"""

import argparse
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
from urllib.parse import quote


VENUE = "ICLR.cc/2027/Conference"
API_URL = "https://api2.openreview.net"
ROOT = Path(__file__).resolve().parent


def value(content, key, default=None):
    """Unwrap an API v2 content field; tolerate absent fields."""
    field = content.get(key, default)
    return field.get("value", default) if isinstance(field, dict) else field


def paper_fields(note):
    content = note.content or {}
    keywords = value(content, "keywords", []) or []
    if isinstance(keywords, str):
        keywords = [keywords]
    return {
        "title": value(content, "title", "") or "",
        "abstract": value(content, "abstract", "") or "",
        "keywords": keywords,
        "pdf_url": (
            f"https://openreview.net/pdf?id={quote(note.id, safe='')}"
            if value(content, "pdf") else None
        ),
    }


def matches_jepa(paper):
    """Substring matching includes I-JEPA, V-JEPA, and JEPA variants."""
    fields = [paper["title"], paper["abstract"], *paper["keywords"]]
    return any("jepa" in str(field).casefold() for field in fields)


def venue_configuration(client, venue):
    group = client.get_group(venue)
    content = group.content or {}
    submission_name = value(content, "submission_name")
    submission_status = value(content, "submission_venue_id")
    if not submission_name or not submission_status:
        raise RuntimeError(
            "Venue configuration lacks submission_name or submission_venue_id; "
            "cannot reliably identify active submissions."
        )

    return f"{venue}/-/{submission_name}", list(dict.fromkeys([submission_status, venue]))


def is_active(note, statuses):
    return (
        not getattr(note, "ddate", None)
        and not getattr(note, "replyto", None)
        and value(note.content or {}, "venueid") in statuses
    )


def fetch_active_submissions(client, venue):
    """Use configured venue IDs, since invitation alone includes withdrawals."""
    invitation, statuses = venue_configuration(client, venue)
    active = {}
    for status in statuses:
        notes = client.get_all_notes(
            invitation=invitation, content={"venueid": status}
        )
        for note in notes:
            if is_active(note, [status]):
                active[note.id] = note
    return list(active.values())


def search_active_submissions(client, venue, page_size=100):
    """Retrieve indexed JEPA candidates; this is not a scan of every paper."""
    invitation, statuses = venue_configuration(client, venue)
    active = {}
    for field in ("title", "abstract", "keywords"):
        offset = 0
        seen = set()
        while True:
            notes = client.search_notes(
                term="jepa", content=field, group=venue, source="forum",
                limit=page_size, offset=offset,
            )
            if not notes:
                break
            identifiers = {note.id for note in notes}
            if not identifiers - seen:
                raise RuntimeError("Search returned a repeated page; export may be incomplete.")
            seen.update(identifiers)
            for note in notes:
                if is_active(note, statuses) and invitation in (note.invitations or []):
                    active[note.id] = note
            # Advance by the actual page length, including any server-side cap.
            offset += len(notes)
    return list(active.values())


def report_fetch_error(exc):
    payload = exc.args[0] if exc.args and isinstance(exc.args[0], dict) else {}
    if payload.get("name") == "ChallengeRequiredError":
        print(
            "OpenReview requires browser challenge verification (HTTP 403). "
            "This blocks metadata retrieval as well as PDFs.", file=sys.stderr,
        )
        details = payload.get("details") or {}
        if details.get("challengeUrl"):
            print(f"Open this challenge URL in your browser:\n{details['challengeUrl']}",
                  file=sys.stderr)
        if details.get("reqId"):
            print(f"OpenReview request ID: {details['reqId']}", file=sys.stderr)
        print(
            "You can try the documented search API with --mode search --print-abstracts. "
            "It may also require verification. Browser verification does not automatically "
            "transfer the browser session to Python. If API requests remain blocked, "
            "contact OpenReview support with the request ID.", file=sys.stderr,
        )
        return 2
    print(f"Fetch/export failed: {exc}", file=sys.stderr)
    return 1


def write_json(output, papers):
    """Replace output atomically after a successful fetch."""
    output = Path(output)
    output.parent.mkdir(parents=True, exist_ok=True)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w", encoding="utf-8", dir=output.parent, delete=False
        ) as stream:
            temporary = Path(stream.name)
            json.dump(papers, stream, ensure_ascii=False, indent=2)
            stream.write("\n")
        temporary.replace(output)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


def download_papers(client, matches, directory):
    """Download main submission PDFs, with optional local text extraction."""
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=True)
    failures = 0
    for note, paper in matches:
        if paper["pdf_url"] is None:
            print(f"No accessible PDF field: {paper['title']}", file=sys.stderr)
            failures += 1
            continue
        # Keep filenames safe even if an unexpected ID is returned.
        filename = quote(note.id, safe="")
        pdf_path = directory / f"{filename}.pdf"
        try:
            data = client.get_attachment(id=note.id, field_name="pdf")
            if not isinstance(data, bytes) or not data.lstrip().startswith(b"%PDF-"):
                raise ValueError("OpenReview attachment is not a PDF")
            pdf_path.write_bytes(data)
            print(f"Downloaded: {pdf_path}")
            if shutil.which("pdftotext"):
                subprocess.run(
                    ["pdftotext", "-layout", str(pdf_path),
                     str(directory / f"{filename}.txt")],
                    check=True, capture_output=True,
                )
        except Exception as exc:
            print(
                f"PDF download/text extraction failed for {paper['title']}: {exc}",
                file=sys.stderr,
            )
            failures += 1
    return failures


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--venue", default=VENUE)
    parser.add_argument("--output", type=Path, default=ROOT / "jepa_papers.md")
    parser.add_argument(
        "--mode", choices=("all", "search"), default="all",
        help="all: scan every active submission; search: retrieve indexed JEPA candidates",
    )
    parser.add_argument(
        "--print-abstracts", action="store_true",
        help="print matching abstracts and keywords; no PDFs are needed",
    )
    parser.add_argument("--download-pdfs", action="store_true")
    parser.add_argument("--pdf-dir", type=Path, default=ROOT / "papers")
    args = parser.parse_args(argv)

    try:
        from openreview.api import OpenReviewClient
    except ImportError:
        print(
            "Missing openreview-py. Install with:\n"
            f"  {ROOT / '.venv/bin/python'} -m pip install -r {ROOT / 'requirements.txt'}",
            file=sys.stderr,
        )
        return 1

    # Public submissions need no login. Credentials are optional and never saved.
    credentials = {}
    token = os.environ.get("OPENREVIEW_TOKEN")
    username = os.environ.get("OPENREVIEW_USERNAME")
    password = os.environ.get("OPENREVIEW_PASSWORD")
    if token:
        credentials["token"] = token
    elif username or password:
        if not (username and password):
            print("Set both OPENREVIEW_USERNAME and OPENREVIEW_PASSWORD.", file=sys.stderr)
            return 1
        credentials.update(username=username, password=password)

    try:
        client = OpenReviewClient(baseurl=API_URL, **credentials)
        if args.mode == "search":
            print(
                "Using OpenReview's search index. Results may miss unindexed papers or "
                "variants that a full substring scan would match.", file=sys.stderr,
            )
            submissions = search_active_submissions(client, args.venue)
        else:
            submissions = fetch_active_submissions(client, args.venue)
        matches = []
        for note in submissions:
            paper = paper_fields(note)
            if matches_jepa(paper):
                matches.append((note, paper))
        matches.sort(key=lambda pair: (pair[1]["title"].casefold(), pair[0].id))
        write_json(args.output, [paper for _, paper in matches])
    except Exception as exc:
        exit_code = report_fetch_error(exc)
        print("No new results were written; any existing output was preserved.", file=sys.stderr)
        return exit_code

    label = "Active search candidates fetched" if args.mode == "search" else "Active submissions fetched"
    print(f"{label}: {len(submissions)}")
    print(f"Total JEPA papers found: {len(matches)}")
    for index, (_, paper) in enumerate(matches, start=1):
        print(f"{index}. {paper['title']}")
        if args.print_abstracts:
            print(f"   Keywords: {', '.join(str(item) for item in paper['keywords'])}")
            print(f"   Abstract: {paper['abstract'] or '(not available)'}\n")
    print(f"Saved JSON to: {args.output}")
    if not submissions:
        print(
            "No active papers returned by this retrieval method. This does not establish "
            "that the venue has no matching submissions; indexing or access may be limited.",
            file=sys.stderr,
        )
    if args.download_pdfs:
        return 1 if download_papers(client, matches, args.pdf_dir) else 0
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
