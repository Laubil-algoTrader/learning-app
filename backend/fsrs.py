"""Pure-Python implementation of the FSRS-5 spaced repetition scheduler.

Implements the DSR (Difficulty, Stability, Retrievability) model with the
19 default FSRS-5 parameters, short-term (same-day) stability updates,
mean reversion for difficulty, and human-friendly Spanish interval previews.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
import math
from typing import Any

# Official FSRS-5 default 19 parameters (w0..w18)
DEFAULT_WEIGHTS: tuple[float, ...] = (
    0.40255,  # w0: initial stability Again
    1.18385,  # w1: initial stability Hard
    3.17300,  # w2: initial stability Good
    15.69105, # w3: initial stability Easy
    7.19490,  # w4: initial difficulty baseline
    0.53450,  # w5: initial difficulty grade decay
    1.46040,  # w6: difficulty delta weight
    0.00460,  # w7: difficulty mean reversion weight
    1.54575,  # w8: success stability scaling
    0.11920,  # w9: success stability power decay
    1.01925,  # w10: success stability retrievability gain
    1.93950,  # w11: lapse stability scaling
    0.11000,  # w12: lapse difficulty exponent
    0.29605,  # w13: lapse stability exponent
    2.26980,  # w14: lapse retrievability gain
    0.23150,  # w15: hard penalty multiplier
    2.98980,  # w16: easy bonus multiplier
    0.51655,  # w17: short-term stability scale
    0.66210,  # w18: short-term stability offset
)

DECAY = -0.5
FACTOR = 19.0 / 81.0  # Ensures R(t=S, S) == 0.90

RATING_AGAIN = 1
RATING_HARD = 2
RATING_GOOD = 3
RATING_EASY = 4
VALID_RATINGS = (RATING_AGAIN, RATING_HARD, RATING_GOOD, RATING_EASY)

STATE_NEW = "new"
STATE_LEARNING = "learning"
STATE_REVIEW = "review"
STATE_RELEARNING = "relearning"


@dataclass
class CardState:
    state: str = STATE_NEW
    stability: float = 0.0
    difficulty: float = 0.0
    reps: int = 0
    lapses: int = 0
    last_review_at: str | None = None
    due_at: str | None = None


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def parse_iso(ts: str | None) -> datetime | None:
    if not ts:
        return None
    dt = datetime.fromisoformat(ts.replace("Z", "+00:00"))
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt


def to_iso(dt: datetime) -> str:
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc).isoformat(timespec="seconds")


def clamp(val: float, low: float, high: float) -> float:
    return max(low, min(high, val))


def retrievability(elapsed_days: float, stability: float) -> float:
    """Probability of recall R(t, S) in [0, 1]."""
    if stability <= 0:
        return 0.0
    t = max(0.0, elapsed_days)
    return math.pow(1.0 + FACTOR * (t / stability), DECAY)


def initial_stability(rating: int, w: tuple[float, ...] = DEFAULT_WEIGHTS) -> float:
    return max(0.1, w[rating - 1])


def initial_difficulty(rating: int, w: tuple[float, ...] = DEFAULT_WEIGHTS) -> float:
    d0 = w[4] - math.exp(w[5] * (rating - 1)) + 1.0
    return clamp(d0, 1.0, 10.0)


def next_difficulty(
    difficulty: float, rating: int, w: tuple[float, ...] = DEFAULT_WEIGHTS
) -> float:
    delta_d = -w[6] * (rating - 3)
    # Linear damping keeps difficulty smooth near the [1, 10] bounds
    d_prime = difficulty + delta_d * ((10.0 - difficulty) / 9.0)
    d0_easy = initial_difficulty(RATING_EASY, w)
    d_reverted = w[7] * d0_easy + (1.0 - w[7]) * d_prime
    return clamp(d_reverted, 1.0, 10.0)


def short_term_stability(
    stability: float, rating: int, w: tuple[float, ...] = DEFAULT_WEIGHTS
) -> float:
    s_new = stability * math.exp(w[17] * (rating - 3 + w[18]))
    return max(0.1, s_new)


def next_recall_stability(
    difficulty: float,
    stability: float,
    r: float,
    rating: int,
    w: tuple[float, ...] = DEFAULT_WEIGHTS,
) -> float:
    hard_penalty = w[15] if rating == RATING_HARD else 1.0
    easy_bonus = w[16] if rating == RATING_EASY else 1.0
    inc = (
        math.exp(w[8])
        * (11.0 - difficulty)
        * math.pow(max(stability, 0.1), -w[9])
        * (math.exp(w[10] * (1.0 - r)) - 1.0)
        * hard_penalty
        * easy_bonus
    )
    return max(0.1, stability * (1.0 + inc))


def next_forget_stability(
    difficulty: float,
    stability: float,
    r: float,
    w: tuple[float, ...] = DEFAULT_WEIGHTS,
) -> float:
    s_f = (
        w[11]
        * math.pow(difficulty, -w[12])
        * (math.pow(max(stability, 0.1) + 1.0, w[13]) - 1.0)
        * math.exp(w[14] * (1.0 - r))
    )
    # Post-lapse stability should never exceed previous stability
    return clamp(s_f, 0.1, max(0.1, stability))


def next_interval_days(
    stability: float,
    desired_retention: float = 0.90,
    max_interval: float = 3650.0,
) -> float:
    """Compute interval in days where R(t, S) reaches desired_retention."""
    r_target = clamp(desired_retention, 0.70, 0.99)
    raw = (stability / FACTOR) * (math.pow(r_target, 1.0 / DECAY) - 1.0)
    return clamp(raw, 0.0, max_interval)


def schedule_review(
    card: CardState,
    rating: int,
    now: datetime | None = None,
    desired_retention: float = 0.90,
    w: tuple[float, ...] = DEFAULT_WEIGHTS,
) -> dict[str, Any]:
    """Advance an FSRS-5 card state given a rating in {1, 2, 3, 4}."""
    if rating not in VALID_RATINGS:
        raise ValueError(f"Rating inválido: {rating}. Debe ser 1..4.")

    now_dt = now or utc_now()
    last_dt = parse_iso(card.last_review_at)
    elapsed_days = (
        max(0.0, (now_dt - last_dt).total_seconds() / 86400.0) if last_dt else 0.0
    )

    is_first = card.state == STATE_NEW or card.reps == 0 or card.stability <= 0
    if is_first:
        new_s = initial_stability(rating, w)
        new_d = initial_difficulty(rating, w)
        r_now = 1.0
    else:
        r_now = retrievability(elapsed_days, card.stability)
        new_d = next_difficulty(card.difficulty, rating, w)
        if elapsed_days < 1.0:
            # Same-day / short-term update
            new_s = short_term_stability(card.stability, rating, w)
            if rating == RATING_AGAIN:
                new_s = min(new_s, next_forget_stability(new_d, card.stability, r_now, w))
        elif rating == RATING_AGAIN:
            new_s = next_forget_stability(new_d, card.stability, r_now, w)
        else:
            new_s = next_recall_stability(new_d, card.stability, r_now, rating, w)

    new_reps = card.reps + 1
    # A lapse is forgetting something that was already in long-term review.
    # Repeated "Again" presses while the card is still being (re)learned in the
    # same sitting must not inflate the count (that would flag leeches too early).
    is_lapse = (not is_first) and rating == RATING_AGAIN and card.state == STATE_REVIEW
    new_lapses = card.lapses + (1 if is_lapse else 0)

    if rating == RATING_AGAIN:
        new_state = STATE_LEARNING if is_first else STATE_RELEARNING
        # Short relearning step (10 minutes) for immediate error correction
        interval_days = 10.0 / 1440.0
        due_dt = now_dt + timedelta(minutes=10)
    elif is_first and rating == RATING_HARD:
        new_state = STATE_LEARNING
        interval_days = 0.5  # 12 hours
        due_dt = now_dt + timedelta(hours=12)
    else:
        new_state = STATE_REVIEW
        interval_days = max(1.0, round(next_interval_days(new_s, desired_retention)))
        due_dt = now_dt + timedelta(days=interval_days)

    return {
        "state": new_state,
        "stability": round(new_s, 4),
        "difficulty": round(new_d, 4),
        "reps": new_reps,
        "lapses": new_lapses,
        "elapsed_days": round(elapsed_days, 4),
        "retrievability_before": round(r_now, 4),
        "interval_days": round(interval_days, 4),
        "interval_label": format_interval_es(interval_days),
        "last_review_at": to_iso(now_dt),
        "due_at": to_iso(due_dt),
    }


def format_interval_es(days: float) -> str:
    """Human-friendly Spanish interval label."""
    minutes = round(days * 1440)
    if minutes < 60:
        return f"{max(1, minutes)} min"
    hours = round(days * 24)
    if hours < 24:
        return f"{hours} h"
    d_round = round(days)
    if d_round == 1:
        return "1 día"
    if d_round < 30:
        return f"{d_round} días"
    months = round(days / 30.0, 1)
    if months < 12:
        val = int(months) if months.is_integer() else months
        return f"{val} mes" if val == 1 else f"{val} meses"
    years = round(days / 365.0, 1)
    val = int(years) if years.is_integer() else years
    return f"{val} año" if val == 1 else f"{val} años"


def preview_intervals(
    card: CardState,
    now: datetime | None = None,
    desired_retention: float = 0.90,
) -> dict[int, str]:
    now_dt = now or utc_now()
    return {
        rating: schedule_review(card, rating, now_dt, desired_retention)["interval_label"]
        for rating in VALID_RATINGS
    }


def current_retrievability(card: CardState, now: datetime | None = None) -> float | None:
    if card.state == STATE_NEW or card.stability <= 0 or not card.last_review_at:
        return None
    now_dt = now or utc_now()
    last_dt = parse_iso(card.last_review_at)
    if not last_dt:
        return None
    elapsed = max(0.0, (now_dt - last_dt).total_seconds() / 86400.0)
    return round(retrievability(elapsed, card.stability), 4)
