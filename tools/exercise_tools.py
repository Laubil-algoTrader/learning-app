"""Authoring tools for exercise packs (backend/exercises/*.py).

    python3 tools/exercise_tools.py validate <module> [slug,slug,...]
    python3 tools/exercise_tools.py dump <module> > pack.txt

`validate` checks structure and the conventions the app relies on (relative tolerances,
answers that start with the expected value, well-formed choices). With a topic list it
also checks that exactly those topics are covered. `dump` prints a pack as plain text
for a human (or a reviewer) to read and re-solve.
"""

from __future__ import annotations

import importlib
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

PROBLEM_KEYS = {"id", "node", "kind", "level", "title", "statement", "parts", "hints", "solution"}
PROJECT_KEYS = {"id", "node", "kind", "level", "title", "statement", "materials", "steps", "done_when", "hints", "lab_link", "minutes"}
OPTIONAL_KEYS = {"source"}
LAB_LINKS = {
    None, "guitar:metronome", "guitar:tuner", "guitar:chords", "guitar:fretboard", "guitar:ear",
    "electronics:ohm", "electronics:pinout", "electronics:debug", "electronics:projects",
}


def _first_number(text: str) -> float | None:
    s = text.replace("−", "-")
    s = re.sub(r"(?<=\d) (?=\d{3}\b)", "", s)
    sup = str.maketrans("⁰¹²³⁴⁵⁶⁷⁸⁹⁻", "0123456789-")
    sci = re.match(r"\s*(-?\d+(?:[.,]\d+)?)\s*[×x·.]\s*10(?:\^(-?\d+)|([⁻⁰¹²³⁴⁵⁶⁷⁸⁹]+))", s)
    if sci:  # scientific notation such as 3,3×10⁴ or 1,23.10^4
        exp = sci.group(2) or sci.group(3).translate(sup)
        return float(sci.group(1).replace(",", ".")) * 10 ** int(exp)
    m = re.search(r"-?\d+(?:[.,]\d+)?(?:/\d+)?", s)
    if not m:
        return None
    t = m.group(0).replace(",", ".")
    if "/" in t:
        a, b = t.split("/")
        return float(a) / float(b)
    return float(t)


def _strings(value, lo: int, hi: int) -> bool:
    return isinstance(value, list) and lo <= len(value) <= hi and all(isinstance(x, str) and x.strip() for x in value)


def validate(module: str, wanted: list[str]) -> int:
    from backend.seed_data import SEED_DOMAINS

    node_domain = {n["slug"]: d["slug"] for d in SEED_DOMAINS for n in d["nodes"]}
    # Topics written in parallel and not wired into the app yet can be declared here.
    import os

    for slug in filter(None, os.environ.get("EXTRA_SLUGS", "").split(",")):
        node_domain.setdefault(slug.strip(), "(nuevo)")
    exercises = importlib.import_module(module).EXERCISES
    errors: list[str] = []
    ids: set[str] = set()
    per_node: dict[str, list[dict]] = {}
    for ex in exercises:
        i = ex.get("id", "?")
        if not re.fullmatch(r"[a-z0-9-]+", str(i)) or i in ids:
            errors.append(f"{i}: id inválido o repetido")
        ids.add(i)
        node = ex.get("node")
        if node not in node_domain:
            errors.append(f"{i}: tema desconocido {node}")
            continue
        if not str(i).startswith(node + "-"):
            errors.append(f"{i}: el id debe empezar con '{node}-'")
        per_node.setdefault(node, []).append(ex)
        if ex.get("level") not in (1, 2, 3):
            errors.append(f"{i}: level debe ser 1, 2 o 3")
        for key in ("title", "statement"):
            if not isinstance(ex.get(key), str) or not ex[key].strip():
                errors.append(f"{i}: falta {key}")
        if "source" in ex and (not isinstance(ex["source"], str) or not ex["source"].strip()):
            errors.append(f"{i}: source debe ser un texto")
        kind = ex.get("kind")
        if kind == "problem":
            if set(ex) - OPTIONAL_KEYS != PROBLEM_KEYS:
                errors.append(f"{i}: claves {sorted(ex)}")
            if not _strings(ex.get("hints"), 1, 3):
                errors.append(f"{i}: 1 a 3 pistas")
            if not _strings(ex.get("solution"), 3, 8):
                errors.append(f"{i}: la resolución lleva 3 a 8 pasos")
            parts = ex.get("parts") or []
            if not 1 <= len(parts) <= 3:
                errors.append(f"{i}: 1 a 3 incisos")
            for pi, part in enumerate(parts, 1):
                tag = f"{i} inciso {pi}"
                if set(part) != {"prompt", "check", "answer"} or not part["prompt"].strip() or not part["answer"].strip():
                    errors.append(f"{tag}: claves/valores")
                    continue
                check = part["check"]
                if check.get("type") == "numeric":
                    if set(check) != {"type", "value", "tolerance", "unit"}:
                        errors.append(f"{tag}: check numérico mal formado")
                        continue
                    value, tol = check["value"], check["tolerance"]
                    if not isinstance(value, (int, float)) or not 0 <= tol <= 0.03:
                        errors.append(f"{tag}: valor o tolerancia (relativa, máx. 0.03; más de 0.01 solo para ángulos chicos o valores sensibles al redondeo)")
                        continue
                    shown = _first_number(part["answer"])
                    if shown is None or abs(shown - value) > max(abs(value) * tol, 1e-9):
                        errors.append(f"{tag}: 'answer' debe EMPEZAR con el valor {value} (empieza con {shown})")
                elif check.get("type") == "choice":
                    options = check.get("options", [])
                    if (
                        set(check) != {"type", "options", "correct"}
                        or len(options) not in (3, 4)
                        or len(set(options)) != len(options)
                        or not isinstance(check["correct"], int)
                        or not 0 <= check["correct"] < len(options)
                    ):
                        errors.append(f"{tag}: opciones mal formadas")
                elif check.get("type") == "text":
                    if set(check) != {"type", "accept"} or not _strings(check["accept"], 1, 8):
                        errors.append(f"{tag}: text mal formado")
                    elif any(re.search(r"\d\s+\d+/\d+", a) for a in check["accept"]):
                        errors.append(f"{tag}: no pongas números mixtos en accept (el corrector ya los convierte)")
                else:
                    errors.append(f"{tag}: tipo de check inválido")
        elif kind == "project":
            if set(ex) - OPTIONAL_KEYS != PROJECT_KEYS:
                errors.append(f"{i}: claves {sorted(ex)}")
            if not (
                _strings(ex.get("materials"), 1, 10)
                and _strings(ex.get("steps"), 3, 9)
                and _strings(ex.get("done_when"), 2, 5)
                and _strings(ex.get("hints"), 1, 3)
            ):
                errors.append(f"{i}: listas (materials 1-10, steps 3-9, done_when 2-5, hints 1-3)")
            link = ex.get("lab_link")
            if link not in LAB_LINKS and not re.fullmatch(r"(guitar|electronics):[a-z0-9_-]+(:[a-z0-9_-]+)*", str(link)):
                errors.append(f"{i}: lab_link inválido")
            if not isinstance(ex.get("minutes"), int) or not 5 <= ex["minutes"] <= 180:
                errors.append(f"{i}: minutes")
        else:
            errors.append(f"{i}: kind debe ser problem o project")
    for slug in wanted:
        if slug not in per_node:
            errors.append(f"falta el tema {slug}")
    for node, items in per_node.items():
        if wanted and node not in wanted:
            errors.append(f"tema no pedido: {node}")
        print(f"  {node}: {len(items)} (niveles {sorted(x.get('level') for x in items)})")
    print(f"{len(exercises)} ejercicios en {len(per_node)} temas")
    print("SIN ERRORES" if not errors else "ERRORES:\n" + "\n".join(errors))
    return 1 if errors else 0


def dump(module: str) -> int:
    exercises = importlib.import_module(module).EXERCISES

    def check_text(c: dict) -> str:
        if c["type"] == "numeric":
            return f"NUM {c['value']} tol={c['tolerance']} [{c['unit']}]"
        if c["type"] == "choice":
            return "OPC: " + " | ".join(("[OK] " if i == c["correct"] else "") + o for i, o in enumerate(c["options"]))
        return "TEXTO " + repr(c["accept"])

    node = None
    for e in exercises:
        if e["node"] != node:
            node = e["node"]
            print("=" * 90)
            print("TEMA", node)
        print(f"\n[{e['id']}] nivel {e['level']} — {e['title']}" + (f"  (fuente: {e['source']})" if e.get("source") else ""))
        print("  ENUNCIADO:", e["statement"].replace("\n", " ⏎ "))
        if e["kind"] == "problem":
            for p in e["parts"]:
                print("  INCISO:", p["prompt"])
                print("     →", check_text(p["check"]), "| respuesta mostrada:", p["answer"])
            for i, h in enumerate(e["hints"], 1):
                print(f"  PISTA {i}:", h)
            for i, s in enumerate(e["solution"], 1):
                print(f"  PASO {i}:", s)
        else:
            print("  MATERIALES:", " · ".join(e["materials"]), "|", e["minutes"], "min | lab:", e["lab_link"])
            for i, s in enumerate(e["steps"], 1):
                print(f"  PASO {i}:", s)
            for c in e["done_when"]:
                print("  HECHO CUANDO:", c)
            for h in e["hints"]:
                print("  CONSEJO:", h)
    return 0


if __name__ == "__main__":
    if len(sys.argv) >= 3 and sys.argv[1] == "validate":
        sys.exit(validate(sys.argv[2], sys.argv[3].split(",") if len(sys.argv) > 3 else []))
    if len(sys.argv) == 3 and sys.argv[1] == "dump":
        sys.exit(dump(sys.argv[2]))
    print(__doc__)
    sys.exit(2)
