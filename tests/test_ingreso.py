"""The UNCuyo entrance-course map points at topics that exist, and its overview adds up."""

from pathlib import Path
import tempfile
import unittest

from backend import ingreso_uncuyo
from backend.db import Database
from backend.exercises.registry import EXERCISES, EXERCISES_BY_NODE
from backend.seed_data import SEED_DOMAINS


class TestIngresoMap(unittest.TestCase):
    def test_every_program_topic_is_in_its_subject(self) -> None:
        slugs_by_domain = {d["slug"]: {n["slug"] for n in d["nodes"]} for d in SEED_DOMAINS}
        for subject in ingreso_uncuyo.SUBJECTS:
            self.assertIn(subject["domain"], slugs_by_domain)
            for unit in subject["units"]:
                for slug in unit["topics"]:
                    self.assertIn(slug, slugs_by_domain[subject["domain"]], f"{subject['key']}: {slug}")
        # A topic belongs to a single unit.
        listed = [s for subject in ingreso_uncuyo.SUBJECTS for u in subject["units"] for s in u["topics"]]
        self.assertEqual(len(listed), len(set(listed)))

    def test_overview_on_a_fresh_database(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            db = Database(Path(tmp) / "test.db")
            data = ingreso_uncuyo.overview(db)
            self.assertEqual([s["key"] for s in data["subjects"]], [s["key"] for s in ingreso_uncuyo.SUBJECTS])
            for subject in data["subjects"]:
                expected = sum(len(u["topics"]) for u in next(s for s in ingreso_uncuyo.SUBJECTS if s["key"] == subject["key"])["units"])
                self.assertEqual(subject["topics_total"], expected)
                self.assertEqual(subject["lessons_done"], 0)
                self.assertEqual(subject["progress_pct"], 0)
                self.assertIsNotNone(subject["next_topic"])

    def test_every_official_exercise_belongs_to_a_program_topic(self) -> None:
        program = ingreso_uncuyo.program_slugs()
        for ex in EXERCISES:
            if ex.get("source"):
                self.assertIn(ex["node"], program, f"{ex['id']} ({ex['source']}) fuera de ingreso_uncuyo")

    def test_every_program_topic_has_exercises(self) -> None:
        for slug in ingreso_uncuyo.program_slugs():
            self.assertTrue(EXERCISES_BY_NODE.get(slug), f"Tema del ingreso sin ejercicios: {slug}")


if __name__ == "__main__":
    unittest.main()
