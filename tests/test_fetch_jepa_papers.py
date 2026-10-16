import contextlib
import io
import json
from pathlib import Path
import sys
import tempfile
from types import ModuleType, SimpleNamespace
import unittest
from unittest.mock import patch

import fetch_jepa_papers as fetcher


def note(identifier, status, **fields):
    content = {key: {"value": item} for key, item in fields.items()}
    content["venueid"] = {"value": status}
    return SimpleNamespace(
        id=identifier, content=content, ddate=None, replyto=None,
        invitations=[fetcher.VENUE + "/-/Submission"],
    )


class FakeClient:
    def __init__(self):
        self.active_status = fetcher.VENUE + "/Submission"
        self.calls = []
        self.submission = note(
            "active", self.active_status, title="V-JEPA: vidéo",
            abstract="Predict representations", keywords=["video"], pdf="/pdf/x.pdf",
        )

    def get_group(self, venue):
        return SimpleNamespace(content={
            "submission_name": {"value": "Submission"},
            "submission_venue_id": {"value": self.active_status},
        })

    def get_all_notes(self, **kwargs):
        self.calls.append(kwargs)
        if kwargs["content"]["venueid"] == self.active_status:
            deleted = note("deleted", self.active_status, title="JEPA")
            deleted.ddate = 1
            reply = note("reply", self.active_status, title="JEPA")
            reply.replyto = "active"
            return [
                self.submission, self.submission, deleted, reply,
                note("withdrawn", fetcher.VENUE + "/Withdrawn_Submission", title="JEPA"),
                note("desk", fetcher.VENUE + "/Desk_Rejected_Submission", title="JEPA"),
                note("rejected", fetcher.VENUE + "/Rejected_Submission", title="JEPA"),
            ]
        return [note("accepted", fetcher.VENUE, title="Unrelated paper")]


def openreview_modules(client):
    package = ModuleType("openreview")
    api = ModuleType("openreview.api")
    api.OpenReviewClient = lambda **kwargs: client
    package.api = api
    return {"openreview": package, "openreview.api": api}


class FetchTests(unittest.TestCase):
    def test_each_metadata_field_and_mixed_case_variants(self):
        for field, item in [
            ("title", "I-JEPA"), ("abstract", "uses jEpA2"),
            ("keywords", ["representation", "v-jepa"]),
        ]:
            with self.subTest(field=field):
                paper = fetcher.paper_fields(note("a", "v", **{field: item}))
                self.assertTrue(fetcher.matches_jepa(paper))
        paper = fetcher.paper_fields(note("a", "v", title="Predictive models"))
        self.assertFalse(fetcher.matches_jepa(paper))

    def test_missing_fields_and_string_keywords(self):
        paper = fetcher.paper_fields(note("a", "v", keywords="JEPA"))
        self.assertEqual(paper, {
            "title": "", "abstract": "", "keywords": ["JEPA"], "pdf_url": None,
        })

    def test_pdf_link_uses_note_id(self):
        paper = fetcher.paper_fields(note("abc", "v", pdf="/pdf/attachment.pdf"))
        self.assertEqual(paper["pdf_url"], "https://openreview.net/pdf?id=abc")

    def test_active_status_filter_and_deduplication(self):
        client = FakeClient()
        notes = fetcher.fetch_active_submissions(client, fetcher.VENUE)
        self.assertEqual([item.id for item in notes], ["active", "accepted"])
        self.assertEqual(client.calls, [
            {"invitation": fetcher.VENUE + "/-/Submission",
             "content": {"venueid": client.active_status}},
            {"invitation": fetcher.VENUE + "/-/Submission",
             "content": {"venueid": fetcher.VENUE}},
        ])

    def test_missing_status_configuration_fails(self):
        client = FakeClient()
        client.get_group = lambda venue: SimpleNamespace(content={})
        with self.assertRaisesRegex(RuntimeError, "cannot reliably identify"):
            fetcher.fetch_active_submissions(client, fetcher.VENUE)
        self.assertEqual(client.calls, [])

    def test_successful_export_and_printed_count(self):
        client = FakeClient()
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "jepa_papers.md"
            stdout = io.StringIO()
            with patch.dict(sys.modules, openreview_modules(client)):
                with contextlib.redirect_stdout(stdout):
                    result = fetcher.main(["--output", str(output)])
            self.assertEqual(result, 0)
            papers = json.loads(output.read_text(encoding="utf-8"))
            self.assertEqual(papers, [fetcher.paper_fields(client.submission)])
            self.assertIn("Total JEPA papers found: 1", stdout.getvalue())
            self.assertIn("1. V-JEPA: vidéo", stdout.getvalue())

    def test_network_error_preserves_existing_output(self):
        client = FakeClient()
        def fail(venue):
            raise ConnectionError("network unavailable")
        client.get_group = fail
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "jepa_papers.md"
            output.write_text("previous results", encoding="utf-8")
            with patch.dict(sys.modules, openreview_modules(client)):
                with contextlib.redirect_stderr(io.StringIO()):
                    result = fetcher.main(["--output", str(output)])
            self.assertEqual(result, 1)
            self.assertEqual(output.read_text(encoding="utf-8"), "previous results")

    def test_download_rejects_non_pdf_response(self):
        client = FakeClient()
        client.get_attachment = lambda **kwargs: b"<html>Access denied</html>"
        with tempfile.TemporaryDirectory() as directory:
            with contextlib.redirect_stderr(io.StringIO()):
                failures = fetcher.download_papers(
                    client, [(client.submission, fetcher.paper_fields(client.submission))],
                    directory,
                )
            self.assertEqual(failures, 1)
            self.assertEqual(list(Path(directory).iterdir()), [])

    def test_search_paginates_short_pages_and_filters_status_and_invitation(self):
        client = FakeClient()
        wrong_invitation = note("wrong", client.active_status, title="JEPA")
        wrong_invitation.invitations = [fetcher.VENUE + "/-/Other"]
        withdrawn = note("withdrawn", fetcher.VENUE + "/Withdrawn_Submission", title="JEPA")
        second = note("second", client.active_status, abstract="uses JEPA")
        calls = []

        def search(**kwargs):
            calls.append(kwargs)
            pages = {
                ("title", 0): [client.submission],
                ("title", 1): [wrong_invitation, withdrawn],
                ("abstract", 0): [second, client.submission],
            }
            return pages.get((kwargs["content"], kwargs["offset"]), [])

        client.search_notes = search
        notes = fetcher.search_active_submissions(client, fetcher.VENUE, page_size=100)
        self.assertEqual([item.id for item in notes], ["active", "second"])
        self.assertEqual([(item["content"], item["offset"]) for item in calls], [
            ("title", 0), ("title", 1), ("title", 3),
            ("abstract", 0), ("abstract", 2), ("keywords", 0),
        ])
        self.assertTrue(all(item["source"] == "forum" for item in calls))
        self.assertTrue(all(item["group"] == fetcher.VENUE for item in calls))

    def test_search_repeated_page_fails_instead_of_exporting_partial_results(self):
        client = FakeClient()
        client.search_notes = lambda **kwargs: [client.submission]
        with self.assertRaisesRegex(RuntimeError, "repeated page"):
            fetcher.search_active_submissions(client, fetcher.VENUE)

    def test_search_cli_prints_abstract_without_downloading(self):
        client = FakeClient()
        client.search_notes = lambda **kwargs: (
            [client.submission] if kwargs["offset"] == 0 else []
        )
        client.get_attachment = lambda **kwargs: self.fail("PDF download was not requested")
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "jepa_papers.md"
            stdout = io.StringIO()
            with patch.dict(sys.modules, openreview_modules(client)):
                with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(io.StringIO()):
                    result = fetcher.main([
                        "--mode", "search", "--print-abstracts", "--output", str(output),
                    ])
            self.assertEqual(result, 0)
            self.assertIn("Active search candidates fetched: 1", stdout.getvalue())
            self.assertIn("Abstract: Predict representations", stdout.getvalue())
            self.assertEqual(len(json.loads(output.read_text())), 1)

    def test_challenge_reports_browser_url_and_preserves_output(self):
        client = FakeClient()
        def challenge(**kwargs):
            raise Exception({
                "name": "ChallengeRequiredError", "status": 403,
                "details": {"challengeUrl": "https://openreview.net/challenge?redirect=test",
                            "reqId": "test-request"},
            })
        client.get_all_notes = challenge
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "jepa_papers.md"
            output.write_text("previous results")
            stderr = io.StringIO()
            with patch.dict(sys.modules, openreview_modules(client)):
                with contextlib.redirect_stderr(stderr):
                    result = fetcher.main(["--output", str(output)])
            self.assertEqual(result, 2)
            self.assertIn("https://openreview.net/challenge?redirect=test", stderr.getvalue())
            self.assertIn("test-request", stderr.getvalue())
            self.assertIn("--mode search --print-abstracts", stderr.getvalue())
            self.assertEqual(output.read_text(), "previous results")


if __name__ == "__main__":
    unittest.main()
