#!/usr/bin/env python3
"""Download a limited batch of main-paper PDFs from the saved JEPA JSON."""

import argparse
import getpass
import os
from pathlib import Path
import json
import shutil
import subprocess
import sys
from urllib.parse import parse_qs, urlparse

from fetch_jepa_papers import API_URL, ROOT, write_json


def validate_pdf(path):
    if not path.read_bytes().lstrip().startswith(b"%PDF-"):
        raise ValueError("Response is not a PDF")
    if shutil.which("pdfinfo"):
        subprocess.run(["pdfinfo", str(path)], check=True, capture_output=True, timeout=30)
        return "pdfinfo"
    return "PDF header only (pdfinfo is not installed)"


def download_batch(client, papers, directory):
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=True)
    report = []
    for index, paper in enumerate(papers, 1):
        item = {"index": index, "title": paper["title"], "pdf_url": paper.get("pdf_url")}
        temporary = None
        try:
            url = urlparse(paper.get("pdf_url") or "")
            identifiers = parse_qs(url.query).get("id", [])
            if url.hostname != "openreview.net" or len(identifiers) != 1:
                raise ValueError("Expected an OpenReview PDF URL with one note ID")
            identifier = identifiers[0]
            if not identifier or not identifier.isalnum():
                raise ValueError("Invalid OpenReview note ID")
            path = directory / f"{identifier}.pdf"
            if path.exists():
                item.update(status="cached", path=str(path), validation=validate_pdf(path))
            else:
                data = client.get_attachment(id=identifier, field_name="pdf")
                if not isinstance(data, bytes) or not data.lstrip().startswith(b"%PDF-"):
                    raise ValueError("Attachment response is not a PDF")
                temporary = path.with_suffix(".pdf.part")
                temporary.write_bytes(data)
                validation = validate_pdf(temporary)
                temporary.replace(path)
                item.update(status="downloaded", path=str(path), validation=validation)
            print(f"[{index}/{len(papers)}] {item['status']}: {paper['title']}", flush=True)
        except Exception as exc:
            payload = exc.args[0] if exc.args and isinstance(exc.args[0], dict) else {}
            item.update(status="failed", error=str(exc))
            if payload.get("name"):
                item["error_name"] = payload["name"]
            if (payload.get("details") or {}).get("challengeUrl"):
                item["challenge_url"] = payload["details"]["challengeUrl"]
            print(f"[{index}/{len(papers)}] failed: {paper['title']}\n  {exc}",
                  file=sys.stderr, flush=True)
        finally:
            if temporary is not None:
                temporary.unlink(missing_ok=True)
        report.append(item)
        write_json(directory / "download_report.json", report)
    return report


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=ROOT / "jepa_papers.json")
    parser.add_argument("--limit", type=int, default=10)
    parser.add_argument(
        "--login", action="store_true",
        help="prompt for OpenReview credentials; authentication may not clear a browser challenge",
    )
    parser.add_argument("--output-dir", type=Path, default=ROOT / "papers" / "first10")
    args = parser.parse_args(argv)
    if args.limit < 1:
        parser.error("--limit must be positive")

    try:
        from openreview.api import OpenReviewClient
        papers = json.loads(args.input.read_text(encoding="utf-8"))[:args.limit]
        credentials = {}
        token = os.environ.get("OPENREVIEW_TOKEN")
        if args.login:
            username = os.environ.get("OPENREVIEW_USERNAME") or input("OpenReview email/username: ").strip()
            password = os.environ.get("OPENREVIEW_PASSWORD") or getpass.getpass("OpenReview password: ")
            if not username or not password:
                raise ValueError("Both an OpenReview username and password are required")
            credentials.update(username=username, password=password)
        elif token:
            credentials["token"] = token
        # openreview-py also reads optional username/password environment variables.
        client = OpenReviewClient(baseurl=API_URL, **credentials)
        report = download_batch(client, papers, args.output_dir)
    except Exception as exc:
        print(f"Could not start download batch: {exc}", file=sys.stderr)
        return 1

    successes = sum(item["status"] != "failed" for item in report)
    print(f"Readable PDFs available: {successes}/{len(report)}")
    print(f"Report: {args.output_dir / 'download_report.json'}")
    challenged = [item for item in report if item.get("error_name") == "ChallengeRequiredError"]
    if challenged:
        print(
            "OpenReview requires browser challenge verification. Open the first saved "
            "pdf_url or challenge_url in your browser and complete any verification shown. "
            "Browser verification is not automatically shared with this Python session. "
            "You can test account authentication with --login --limit 1; it is not a "
            "confirmed fix for the challenge.", file=sys.stderr,
        )
    return 0 if successes == len(report) else 1


if __name__ == "__main__":
    raise SystemExit(main())
