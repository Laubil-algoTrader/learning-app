"""Unit tests for the pure-Python FSRS-5 scheduler."""

from datetime import datetime, timedelta, timezone
import unittest

from backend import fsrs


class TestFSRS5(unittest.TestCase):
    def setUp(self) -> None:
        self.now = datetime(2026, 11, 20, 12, 0, 0, tzinfo=timezone.utc)

    def test_retrievability_identity_points(self) -> None:
        self.assertAlmostEqual(fsrs.retrievability(0.0, 10.0), 1.0, places=6)
        # By definition of FSRS-5, R(t=S, S) == 0.90
        self.assertAlmostEqual(fsrs.retrievability(10.0, 10.0), 0.90, places=5)
        self.assertLess(fsrs.retrievability(20.0, 10.0), 0.90)

    def test_initial_ratings_monotonic_stability_and_difficulty_bounds(self) -> None:
        card = fsrs.CardState()
        results = {
            r: fsrs.schedule_review(card, r, now=self.now)
            for r in fsrs.VALID_RATINGS
        }
        # Stability increases monotonically with rating
        self.assertLess(results[1]["stability"], results[2]["stability"])
        self.assertLess(results[2]["stability"], results[3]["stability"])
        self.assertLess(results[3]["stability"], results[4]["stability"])
        # Difficulty stays bounded in [1, 10] and decreases with higher rating
        for r in fsrs.VALID_RATINGS:
            self.assertGreaterEqual(results[r]["difficulty"], 1.0)
            self.assertLessEqual(results[r]["difficulty"], 10.0)
        self.assertGreater(results[1]["difficulty"], results[4]["difficulty"])
        # Again schedules a 10-minute relearning step
        self.assertEqual(results[1]["state"], fsrs.STATE_LEARNING)
        self.assertEqual(results[1]["interval_label"], "10 min")

    def test_subsequent_recall_grows_stability_and_lapse_reduces_it(self) -> None:
        card = fsrs.CardState()
        first = fsrs.schedule_review(card, fsrs.RATING_GOOD, now=self.now)
        reviewed_card = fsrs.CardState(
            state=first["state"],
            stability=first["stability"],
            difficulty=first["difficulty"],
            reps=first["reps"],
            lapses=first["lapses"],
            last_review_at=first["last_review_at"],
            due_at=first["due_at"],
        )
        later = self.now + timedelta(days=3)
        good_next = fsrs.schedule_review(reviewed_card, fsrs.RATING_GOOD, now=later)
        easy_next = fsrs.schedule_review(reviewed_card, fsrs.RATING_EASY, now=later)
        lapse_next = fsrs.schedule_review(reviewed_card, fsrs.RATING_AGAIN, now=later)

        self.assertGreater(good_next["stability"], reviewed_card.stability)
        self.assertGreater(easy_next["stability"], good_next["stability"])
        self.assertLessEqual(lapse_next["stability"], reviewed_card.stability)
        self.assertEqual(lapse_next["lapses"], 1)
        self.assertEqual(lapse_next["state"], fsrs.STATE_RELEARNING)

    def test_same_day_short_term_update(self) -> None:
        card = fsrs.CardState()
        first = fsrs.schedule_review(card, fsrs.RATING_AGAIN, now=self.now)
        c2 = fsrs.CardState(
            state=first["state"],
            stability=first["stability"],
            difficulty=first["difficulty"],
            reps=first["reps"],
            lapses=first["lapses"],
            last_review_at=first["last_review_at"],
            due_at=first["due_at"],
        )
        ten_min_later = self.now + timedelta(minutes=10)
        second = fsrs.schedule_review(c2, fsrs.RATING_GOOD, now=ten_min_later)
        self.assertGreater(second["stability"], c2.stability)
        self.assertEqual(second["reps"], 2)

    def test_preview_intervals_and_invalid_rating(self) -> None:
        previews = fsrs.preview_intervals(fsrs.CardState(), now=self.now)
        self.assertEqual(set(previews.keys()), {1, 2, 3, 4})
        for val in previews.values():
            self.assertIsInstance(val, str)
            self.assertTrue(len(val) > 0)
        with self.assertRaises(ValueError):
            fsrs.schedule_review(fsrs.CardState(), 5, now=self.now)


if __name__ == "__main__":
    unittest.main()
