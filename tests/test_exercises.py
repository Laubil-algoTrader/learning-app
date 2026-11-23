"""Exercises section: content integrity and the attempt log."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from backend import exercise_store
from backend.api import APIError, handle_api_request
from backend.db import Database
from backend.exercises.registry import EXERCISES, EXERCISES_BY_NODE
from backend.seed_data import SEED_DOMAINS


class TestExerciseContent(unittest.TestCase):
    def test_every_exercise_belongs_to_a_seed_topic(self) -> None:
        seed_slugs = {n["slug"] for d in SEED_DOMAINS for n in d["nodes"]}
        self.assertGreater(len(EXERCISES), 0)
        for ex in EXERCISES:
            self.assertIn(ex["node"], seed_slugs, ex["id"])
            self.assertTrue(ex["id"].startswith(ex["node"] + "-"), ex["id"])
            self.assertIn(ex["level"], (1, 2, 3), ex["id"])

    def test_problems_are_gradable_and_explained(self) -> None:
        for ex in EXERCISES:
            if ex["kind"] != "problem":
                continue
            self.assertTrue(1 <= len(ex["parts"]) <= 3, ex["id"])
            self.assertGreaterEqual(len(ex["solution"]), 3, ex["id"])
            self.assertGreaterEqual(len(ex["hints"]), 1, ex["id"])
            for part in ex["parts"]:
                check = part["check"]
                self.assertIn(check["type"], ("numeric", "choice", "text"), ex["id"])
                if check["type"] == "numeric":
                    # Tolerances are relative: anything loose would accept wrong answers. Above 1 %
                    # only for small angles or results that swing with reasonable intermediate rounding.
                    self.assertLessEqual(check["tolerance"], 0.03, ex["id"])
                if check["type"] == "choice":
                    self.assertEqual(len(set(check["options"])), len(check["options"]), ex["id"])
                    self.assertTrue(0 <= check["correct"] < len(check["options"]), ex["id"])

    def test_projects_have_observable_completion_criteria(self) -> None:
        for ex in EXERCISES:
            if ex["kind"] != "project":
                continue
            self.assertGreaterEqual(len(ex["steps"]), 3, ex["id"])
            self.assertGreaterEqual(len(ex["done_when"]), 2, ex["id"])

    def test_topics_list_exercises_from_easy_to_hard(self) -> None:
        for slug, exercises in EXERCISES_BY_NODE.items():
            levels = [e["level"] for e in exercises]
            self.assertEqual(levels, sorted(levels), slug)


class TestExerciseAttempts(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.db = Database(Path(self.tmp.name) / "test.db")
        self.problem = next(e for e in EXERCISES if e["kind"] == "problem")
        seed_domain = next(d for d in SEED_DOMAINS if any(n["slug"] == self.problem["node"] for n in d["nodes"]))
        self.domain_slug = seed_domain["slug"]

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def _status(self, exercise_id: str) -> dict:
        data = exercise_store.domain_exercises(self.db, self.domain_slug)
        return next(e for t in data["topics"] for e in t["exercises"] if e["id"] == exercise_id)["status"]

    def test_overview_only_lists_disciplines_with_exercises(self) -> None:
        domains = exercise_store.overview(self.db)["domains"]
        self.assertIn(self.domain_slug, {d["slug"] for d in domains})
        for d in domains:
            self.assertGreater(d["total"], 0)
            self.assertEqual(d["solved"], 0)

    def test_failed_then_solved_attempts_update_the_status(self) -> None:
        ex = self.problem
        parts = len(ex["parts"])
        self.assertEqual(self._status(ex["id"])["attempts"], 0)

        exercise_store.log_attempt(self.db, ex["id"], {"correct": False, "parts_ok": 0})
        status = self._status(ex["id"])
        self.assertEqual((status["attempts"], status["solved"]), (1, False))

        res = exercise_store.log_attempt(self.db, ex["id"], {"correct": True, "parts_ok": parts, "saw_solution": True})
        self.assertTrue(res["correct"])
        status = self._status(ex["id"])
        self.assertEqual((status["attempts"], status["solved"], status["solved_unaided"]), (2, True, False))

        exercise_store.log_attempt(self.db, ex["id"], {"correct": True, "parts_ok": parts})
        self.assertTrue(self._status(ex["id"])["solved_unaided"])

    def test_an_attempt_missing_parts_is_never_recorded_as_solved(self) -> None:
        ex = next((e for e in EXERCISES if e["kind"] == "problem" and len(e["parts"]) > 1), None)
        if ex is None:
            self.skipTest("no multi-part problem in the packs")
        res = exercise_store.log_attempt(self.db, ex["id"], {"correct": True, "parts_ok": len(ex["parts"]) - 1})
        self.assertFalse(res["correct"])

    def test_topic_is_flagged_after_two_unsolved_exercises(self) -> None:
        slug, exercises = next((s, e) for s, e in EXERCISES_BY_NODE.items() if len(e) >= 2 and e[0]["kind"] == "problem")
        domain_slug = next(d["slug"] for d in SEED_DOMAINS if any(n["slug"] == slug for n in d["nodes"]))
        topic = lambda: next(t for t in exercise_store.domain_exercises(self.db, domain_slug)["topics"] if t["slug"] == slug)
        self.assertFalse(topic()["struggling"])
        for ex in exercises[:2]:
            exercise_store.log_attempt(self.db, ex["id"], {"correct": False, "parts_ok": 0})
        self.assertTrue(topic()["struggling"])

    def test_api_routes(self) -> None:
        status, overview = handle_api_request(self.db, "GET", "/api/exercises")
        self.assertEqual(status, 200)
        self.assertTrue(overview["domains"])

        status, data = handle_api_request(self.db, "GET", f"/api/exercises/{self.domain_slug}")
        self.assertEqual(status, 200)
        self.assertEqual(data["totals"]["solved"], 0)

        body = b'{"correct": true, "parts_ok": %d}' % len(self.problem["parts"])
        status, res = handle_api_request(self.db, "POST", f"/api/exercises/{self.problem['id']}/attempts", body)
        self.assertEqual(status, 201)
        self.assertTrue(res["status"]["solved"])

        with self.assertRaises(APIError) as ctx:
            handle_api_request(self.db, "POST", "/api/exercises/no-existe-1/attempts", b"{}")
        self.assertEqual(ctx.exception.status, 404)

        status, lesson = handle_api_request(self.db, "GET", "/api/nodes/1/lesson")
        self.assertEqual(status, 200)
        self.assertIn("exercise_count", lesson)


if __name__ == "__main__":
    unittest.main()
