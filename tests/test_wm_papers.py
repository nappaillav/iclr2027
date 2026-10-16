import contextlib
from datetime import datetime, timedelta, timezone
import io
import json
from pathlib import Path
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

import wm_papers as wm


def paper(title, abstract="", keywords=None):
    return {"title": title, "abstract": abstract, "keywords": keywords or [],
            "pdf_url": "https://openreview.net/pdf?id=abc"}


def note(identifier, status, **fields):
    return SimpleNamespace(
        id=identifier, content={"venueid": {"value": status}, **{
            key: {"value": value} for key, value in fields.items()
        }}, ddate=None, replyto=None, invitations=[wm.VENUE + "/-/Submission"],
    )


class WorldModelTests(unittest.TestCase):
    def test_world_model_variants_across_metadata_without_jepa(self):
        for term in ["World Models", "world-model", "WORLD–MODEL", "LeWorldModel",
                     "world modeling", "world modelling"]:
            with self.subTest(term=term):
                self.assertTrue(wm.matches_world_model(paper(term)))
                self.assertTrue(wm.matches_world_model(paper("Paper", abstract=term)))
                self.assertTrue(wm.matches_world_model(paper("Paper", keywords=[term])))
        self.assertFalse(wm.matches_world_model(paper("JEPA for image classification")))

    def test_hierarchy_screening_avoids_generic_nested_calls(self):
        for description in [
            "hierarchical planning", "multi-scale future prediction", "cross-scale learning",
            "nested latent representations", "a latent-pyramid predictor", "subgoals",
            "a high-level planner and a low-level controller",
        ]:
            with self.subTest(description=description):
                self.assertTrue(wm.matches_hierarchy(paper("World Model", description)))
        self.assertFalse(wm.matches_hierarchy(paper("World Model", "nested model calls")))
        self.assertFalse(wm.matches_hierarchy(paper("World Model", "nested polynomial probes")))

    def test_offline_input_exports_hierarchy_without_rewriting_the_source(self):
        hierarchical = paper("Hierarchical World Model", "Details", ["planning"])
        ordinary = paper("World model forecasting")
        unrelated = paper("Hierarchical image classifier")
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "input.json"
            output = Path(directory) / "wm.json"
            hierarchy = Path(directory) / "hierarchy.json"
            source.write_text(json.dumps([hierarchical, ordinary, unrelated]))
            stdout = io.StringIO()
            with patch.object(wm, "create_client", side_effect=AssertionError("No network needed")):
                with contextlib.redirect_stdout(stdout):
                    result = wm.main([
                        "--input", str(source), "--output", str(output),
                        "--hierarchy-output", str(hierarchy),
                    ])
            self.assertEqual(result, 0)
            self.assertFalse(output.exists())
            self.assertEqual(json.loads(hierarchy.read_text()), [hierarchical])
            self.assertEqual(json.loads(source.read_text()), [hierarchical, ordinary, unrelated])
            info = json.loads((Path(directory) / "hierarchy_source.json").read_text())
            self.assertEqual(info["source_kind"], "saved_json")
            self.assertEqual(info["hierarchy_matches"], 1)
            self.assertNotIn(hierarchical["title"], stdout.getvalue())
            self.assertNotIn(hierarchical["abstract"], stdout.getvalue())

    def test_search_unions_queries_paginates_and_excludes_inactive_notes(self):
        active_status = wm.VENUE + "/Submission"
        first = note("first", active_status, title="World model")
        second = note("second", active_status, title="Hierarchical world model")
        withdrawn = note("withdrawn", wm.VENUE + "/Withdrawn_Submission", title="World model")
        calls = []
        def search(**kwargs):
            calls.append(kwargs)
            key = (kwargs["term"], kwargs["offset"])
            return {
                (wm.SEARCH_TERMS[0], 0): [first],
                (wm.SEARCH_TERMS[0], 1): [second, withdrawn],
                (wm.SEARCH_TERMS[1], 0): [first, second],
            }.get(key, [])
        client = SimpleNamespace(
            get_group=lambda venue: SimpleNamespace(content={
                "submission_name": {"value": "Submission"},
                "submission_venue_id": {"value": active_status},
            }), search_notes=search,
        )
        result = wm.search_active_world_models(client, wm.VENUE, request_delay=0)
        self.assertEqual([item.id for item in result], ["second"])
        self.assertEqual({call["term"] for call in calls}, set(wm.SEARCH_TERMS))
        self.assertTrue(all(call["group"] == wm.VENUE for call in calls))
        self.assertTrue(all(call["source"] == "forum" for call in calls))
        self.assertTrue(all(call["content"] == "all" for call in calls))
        self.assertTrue(all(call["limit"] == 1000 for call in calls))

    def test_anonymous_client_ignores_login_environment_and_disables_retries(self):
        from openreview.api import OpenReviewClient
        login_environment = {
            "OPENREVIEW_USERNAME": "test@example.com", "OPENREVIEW_PASSWORD": "test-password",
            "OPENREVIEW_TOKEN": "test-token",
        }
        with patch.dict("os.environ", login_environment):
            with patch.object(OpenReviewClient, "login_user", side_effect=AssertionError("No login")):
                client = wm.create_client()
            self.assertIsNone(client.token)
            self.assertNotIn("Authorization", client.headers)
            self.assertEqual(client.session.get_adapter(wm.API_URL).max_retries.total, 0)
            import os
            self.assertTrue(all(os.environ[key] == value for key, value in login_environment.items()))
            client.session.close()

    def test_checkpoint_resumes_at_failed_offset_without_repeating_previous_page(self):
        active_status = wm.VENUE + "/Submission"
        first = note("first", active_status, title="Hierarchical world model")
        second = note("second", active_status, title="Hierarchical world model")
        client = SimpleNamespace(get_group=lambda venue: SimpleNamespace(content={
            "submission_name": {"value": "Submission"},
            "submission_venue_id": {"value": active_status},
        }))
        def interrupted(**kwargs):
            if kwargs["offset"] == 0:
                return [first]
            raise Exception({"name": "RateLimitError", "status": 429,
                             "details": {"resetTime": "2000-01-01T00:00:00Z"}})
        client.search_notes = interrupted
        with tempfile.TemporaryDirectory() as directory:
            checkpoint = Path(directory) / "checkpoint.json"
            with self.assertRaises(Exception):
                wm.search_active_world_models(client, wm.VENUE, checkpoint_path=checkpoint, request_delay=0)
            saved = json.loads(checkpoint.read_text())
            self.assertEqual(saved["offset"], 1)
            self.assertEqual(saved["matches"][0]["id"], "first")
            calls = []
            def resumed(**kwargs):
                calls.append((kwargs["term"], kwargs["offset"]))
                return [second] if (kwargs["term"], kwargs["offset"]) == (wm.SEARCH_TERMS[0], 1) else []
            client.search_notes = resumed
            with contextlib.redirect_stdout(io.StringIO()):
                result = wm.search_active_world_models(
                    client, wm.VENUE, checkpoint_path=checkpoint, request_delay=0,
                )
            self.assertEqual([item.id for item in result], ["first", "second"])
            self.assertEqual(calls[0], (wm.SEARCH_TERMS[0], 1))
            self.assertTrue(json.loads(checkpoint.read_text())["complete"])

    def test_saved_cooldown_makes_no_requests_even_when_restart_is_requested(self):
        active_status = wm.VENUE + "/Submission"
        client = SimpleNamespace(
            get_group=lambda venue: SimpleNamespace(content={
                "submission_name": {"value": "Submission"},
                "submission_venue_id": {"value": active_status},
            }),
            search_notes=lambda **kwargs: (_ for _ in ()).throw(Exception({
                "name": "RateLimitError", "status": 429, "details": {
                    "resetTime": (datetime.now(timezone.utc) + timedelta(hours=1)).isoformat(),
                },
            })),
        )
        with tempfile.TemporaryDirectory() as directory:
            checkpoint = Path(directory) / "checkpoint.json"
            with self.assertRaises(Exception):
                wm.search_active_world_models(client, wm.VENUE, checkpoint_path=checkpoint, request_delay=0)
            client.get_group = lambda venue: self.fail("Must not fetch group during cooldown")
            client.search_notes = lambda **kwargs: self.fail("Must not retry during cooldown")
            for restart in [False, True]:
                with self.subTest(restart=restart), self.assertRaises(wm.SearchPaused):
                    wm.search_active_world_models(
                        client, wm.VENUE, checkpoint_path=checkpoint, request_delay=0, restart=restart,
                    )

    def test_rate_limit_keeps_partial_matches_and_preserves_completed_export(self):
        active_status = wm.VENUE + "/Submission"
        first = note("first", active_status, title="Hierarchical world model", abstract="Saved abstract")
        def search(**kwargs):
            if kwargs["offset"] == 0:
                return [first]
            raise Exception({"name": "RateLimitError", "status": 429,
                             "details": {"resetTime": "2000-01-01T00:00:00Z"}})
        client = SimpleNamespace(
            get_group=lambda venue: SimpleNamespace(content={
                "submission_name": {"value": "Submission"},
                "submission_venue_id": {"value": active_status},
            }), search_notes=search,
        )
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "wm.json"
            hierarchy = Path(directory) / "hierarchy.json"
            output.write_text("completed export")
            with patch.object(wm, "create_client", return_value=client):
                with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
                    result = wm.main([
                        "--output", str(output), "--hierarchy-output", str(hierarchy),
                        "--request-delay", "0",
                    ])
            self.assertEqual(result, 3)
            self.assertEqual(output.read_text(), "completed export")
            partial = json.loads((Path(directory) / "wm_partial.json").read_text())
            self.assertEqual(partial[0]["abstract"], "Saved abstract")
            self.assertFalse(hierarchy.exists())

    def test_network_failure_preserves_both_existing_exports(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "wm.json"
            hierarchy = Path(directory) / "hierarchy.json"
            output.write_text("previous full export")
            hierarchy.write_text("previous hierarchy export")
            with patch.object(wm, "create_client", side_effect=ConnectionError("network unavailable")):
                with contextlib.redirect_stderr(io.StringIO()):
                    result = wm.main(["--output", str(output), "--hierarchy-output", str(hierarchy)])
            self.assertEqual(result, 1)
            self.assertEqual(output.read_text(), "previous full export")
            self.assertEqual(hierarchy.read_text(), "previous hierarchy export")

    def test_combined_filter_can_match_across_fields_but_requires_both_categories(self):
        self.assertTrue(wm.matches_combined(paper(
            "World model", abstract="Plans with hierarchical subgoals",
        )))
        self.assertTrue(wm.matches_combined(paper(
            "Hierarchical forecasting", keywords=["World Models"],
        )))
        self.assertFalse(wm.matches_combined(paper("World model with a flat planner")))
        self.assertFalse(wm.matches_combined(paper("Hierarchical image classification")))

    def test_legacy_checkpoint_is_backed_up_and_seeds_the_combined_search(self):
        status = wm.VENUE + "/Submission"
        ordinary = note("ordinary", status, title="World model")
        combined = note("combined", status, title="Hierarchical world model")
        old_state = {
            "venue": wm.VENUE, "terms": list(wm.LEGACY_SEARCH_TERMS),
            "invitation": wm.VENUE + "/-/Submission", "statuses": [status, wm.VENUE],
            "query_index": 0, "offset": 10000, "seen_ids": ["ordinary", "combined"],
            "matches": [vars(ordinary), vars(combined)], "complete": False,
            "rate_limit_reset_utc": None,
        }
        calls = []
        def search(**kwargs):
            calls.append(kwargs)
            return []
        client = SimpleNamespace(
            get_group=lambda venue: self.fail("Existing venue metadata should be reused"),
            search_notes=search,
        )
        with tempfile.TemporaryDirectory() as directory:
            checkpoint = Path(directory) / "checkpoint.json"
            checkpoint.write_text(json.dumps(old_state))
            with contextlib.redirect_stdout(io.StringIO()):
                result = wm.search_active_world_models(
                    client, wm.VENUE, checkpoint_path=checkpoint, request_delay=0,
                )
            self.assertEqual([item.id for item in result], ["combined"])
            self.assertEqual(calls[0]["offset"], 0)
            self.assertEqual(calls[0]["term"], wm.SEARCH_TERMS[0])
            backup = checkpoint.with_name("checkpoint_world_models_backup.json")
            self.assertEqual(json.loads(backup.read_text()), old_state)
            saved = json.loads(checkpoint.read_text())
            self.assertEqual(saved["terms"], list(wm.SEARCH_TERMS))
            self.assertTrue(saved["complete"])

    def test_fetch_exports_combined_matches_directly_without_an_offline_step(self):
        status = wm.VENUE + "/Submission"
        notes = [note("plain", status, title="World model"),
                 note("joint", status, title="Hierarchical world model", abstract="Prediction")]
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "hierarchy-wm.json"
            with patch.object(wm, "create_client", return_value=object()):
                with patch.object(wm, "search_active_world_models", return_value=notes):
                    with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
                        result = wm.main(["--output", str(output)])
            self.assertEqual(result, 0)
            records = json.loads(output.read_text())
            self.assertEqual([item["title"] for item in records], ["Hierarchical world model"])
            self.assertEqual(set(records[0]), {"title", "abstract", "keywords", "pdf_url"})


if __name__ == "__main__":
    unittest.main()
