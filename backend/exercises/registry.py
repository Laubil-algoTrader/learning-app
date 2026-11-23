"""Collects every exercise pack in this package.

A pack is any module here that defines `EXERCISES: list[dict]`; dropping a new file in
the package is all it takes to publish more exercises. Two kinds exist:

- "problem": a multi-step exercise with 1-3 auto-checked parts, progressive hints and a
  full worked solution (maths, physics).
- "project": a hands-on build or practice routine with steps and observable "done when"
  criteria the learner ticks off (electronics, guitar).
"""

from __future__ import annotations

import importlib
import pkgutil
from typing import Any

import backend.exercises as _package

_SKIP = {"registry"}


def _load() -> list[dict[str, Any]]:
    exercises: list[dict[str, Any]] = []
    seen: set[str] = set()
    for info in sorted(pkgutil.iter_modules(_package.__path__), key=lambda m: m.name):
        if info.name in _SKIP or info.name.startswith("_"):
            continue
        module = importlib.import_module(f"{_package.__name__}.{info.name}")
        for exercise in getattr(module, "EXERCISES", []):
            if exercise["id"] in seen:
                raise ValueError(f"duplicate exercise id: {exercise['id']}")
            seen.add(exercise["id"])
            exercises.append(exercise)
    return exercises


EXERCISES: list[dict[str, Any]] = _load()
EXERCISES_BY_ID: dict[str, dict[str, Any]] = {e["id"]: e for e in EXERCISES}
EXERCISES_BY_NODE: dict[str, list[dict[str, Any]]] = {}
for _exercise in EXERCISES:
    EXERCISES_BY_NODE.setdefault(_exercise["node"], []).append(_exercise)
for _node_exercises in EXERCISES_BY_NODE.values():
    _node_exercises.sort(key=lambda e: (e["level"], e["id"]))
