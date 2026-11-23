"""Authoring tools for topic packs (modules exporting <X>_NODES and <X>_LESSONS).

    python3 tools/topic_tools.py validate <module> <NODES_VAR> <LESSONS_VAR> <domain_slug>
    python3 tools/topic_tools.py dump <module> <NODES_VAR> <LESSONS_VAR> > pack.txt

A pack's nodes carry `insert_after` (the slug they follow); backend/content_merge.py turns
that into positions and "N." title prefixes. `validate` checks the shape the lesson view
and the review cards rely on; `dump` prints the pack as text for a reviewer.
"""

from __future__ import annotations

import importlib
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

CARD_KEYS = {"item_type", "title", "prompt", "answer", "hints", "payload"}


def _first_number(text: str) -> float | None:
    s = text.replace("−", "-")
    s = re.sub(r"(?<=\d) (?=\d{3}\b)", "", s)
    m = re.search(r"-?\d+(?:[.,]\d+)?(?:/\d+)?", s)
    if not m:
        return None
    t = m.group(0).replace(",", ".")
    if "/" in t:
        a, b = t.split("/")
        return float(a) / float(b)
    return float(t)


def _load(module: str, nodes_var: str, lessons_var: str):
    mod = importlib.import_module(module)
    return getattr(mod, nodes_var), getattr(mod, lessons_var)


def validate(module: str, nodes_var: str, lessons_var: str, domain_slug: str) -> int:
    from backend.seed_data import SEED_DOMAINS

    nodes, lessons = _load(module, nodes_var, lessons_var)
    # A discipline that is not in the app yet starts empty: no lab, nodes chained from "__start__".
    domain = next((d for d in SEED_DOMAINS if d["slug"] == domain_slug), {"slug": domain_slug, "nodes": [], "lab_type": None})
    new_slugs = {n["slug"] for n in nodes}
    existing = [n for n in domain["nodes"] if n["slug"] not in new_slugs]
    existing_slugs = {n["slug"] for n in existing} | {"__start__"}
    import os

    existing_slugs |= set(filter(None, os.environ.get("EXTRA_SLUGS", "").split(",")))
    all_titles = {it["title"] for d in SEED_DOMAINS for n in d["nodes"] if n["slug"] not in new_slugs for it in n["items"]}
    lab_tabs = {n["metadata"].get("lab_tab") for n in domain["nodes"]} - {None}
    lab_links = {None} | ({f"{domain['lab_type']}:{t}" for t in lab_tabs} if domain["lab_type"] else set())
    errors: list[str] = []
    seen: set[str] = set()
    for n in nodes:
        s = n.get("slug", "?")
        for key in ("slug", "title", "summary", "prerequisites", "metadata", "items", "insert_after"):
            if key not in n:
                errors.append(f"{s}: falta la clave {key}")
        if s in existing_slugs:
            errors.append(f"{s}: ese slug ya existe en la app")
        if re.match(r"^\d+\.", n.get("title", "")):
            errors.append(f"{s}: el título no lleva número")
        if n.get("insert_after") not in existing_slugs | new_slugs:
            errors.append(f"{s}: insert_after desconocido ({n.get('insert_after')})")
        for p in n.get("prerequisites", []):
            if p not in existing_slugs | new_slugs:
                errors.append(f"{s}: prerrequisito desconocido {p}")
        md = n.get("metadata", {})
        if not md.get("section") or not isinstance(md.get("est_minutes"), int):
            errors.append(f"{s}: metadata necesita section y est_minutes")
        if lab_tabs and md.get("lab_tab") not in lab_tabs:
            errors.append(f"{s}: lab_tab inválido (usá uno de {sorted(lab_tabs)})")
        if s not in lessons:
            errors.append(f"{s}: falta la lección")
        items = n.get("items", [])
        if not 6 <= len(items) <= 10:
            errors.append(f"{s}: {len(items)} tarjetas (deben ser 6 a 10)")
        for i, it in enumerate(items, 1):
            tag = f"{s}#{i}"
            if set(it) != CARD_KEYS:
                errors.append(f"{tag}: claves {sorted(it)}")
                continue
            if it["item_type"] not in ("worked_example", "recall"):
                errors.append(f"{tag}: item_type inválido")
            if it["title"] in seen or it["title"] in all_titles:
                errors.append(f"{tag}: título repetido: {it['title']}")
            seen.add(it["title"])
            if not (1 <= len(it["hints"]) <= 2) or not all(isinstance(h, str) and h.strip() for h in it["hints"]):
                errors.append(f"{tag}: 1 o 2 pistas")
            payload = it["payload"]
            check = payload.get("check")
            if payload.get("lab_link") not in lab_links:
                errors.append(f"{tag}: lab_link inválido {payload.get('lab_link')}")
            if set(payload) - {"check", "lab_link"}:
                errors.append(f"{tag}: payload con claves extra")
            if not check:
                errors.append(f"{tag}: falta check")
                continue
            if check["type"] == "numeric":
                value, tol = check.get("value"), check.get("tolerance", 0)
                if set(check) != {"type", "value", "tolerance", "unit"} or not isinstance(value, (int, float)) or not 0 <= tol <= 0.02:
                    errors.append(f"{tag}: check numérico mal formado (tolerancia relativa, máx. 0.02)")
                else:
                    shown = _first_number(it["answer"])
                    if shown is None or abs(shown - value) > max(abs(value) * tol, 1e-9):
                        errors.append(f"{tag}: la respuesta debe EMPEZAR con el valor {value} (empieza con {shown})")
            elif check["type"] == "choice":
                o = check.get("options", [])
                if len(o) not in (3, 4) or len(set(o)) != len(o) or not isinstance(check.get("correct"), int) or not 0 <= check["correct"] < len(o):
                    errors.append(f"{tag}: opciones mal formadas")
            elif check["type"] == "order":
                if len(check.get("lines", [])) < 3:
                    errors.append(f"{tag}: order con menos de 3 líneas")
            elif check["type"] == "text":
                if not check.get("accept"):
                    errors.append(f"{tag}: text sin accept")
            else:
                errors.append(f"{tag}: tipo de check desconocido")
    for s, lesson in lessons.items():
        if s not in new_slugs:
            errors.append(f"lección huérfana {s}")
        if set(lesson) != {"hook", "concept", "example", "check", "checks", "takeaway_prompt"}:
            errors.append(f"{s}: claves de lección {sorted(lesson)}")
            continue
        if not isinstance(lesson["hook"], dict) or set(lesson["hook"]) != {"question", "intuition"}:
            errors.append(f"{s}: hook debe ser {{question, intuition}}")
        c = lesson["concept"]
        if set(c) != {"points", "real_world", "key_rule", "pitfall"} or not 3 <= len(c["points"]) <= 6 or len(c["real_world"]) != 3:
            errors.append(f"{s}: concept mal formado (3-6 points, 3 real_world)")
        elif any(set(r) != {"title", "detail"} for r in c["real_world"]):
            errors.append(f"{s}: real_world mal formado")
        e = lesson["example"]
        if set(e) != {"title", "steps", "lab_link", "lab_cta"} or not 3 <= len(e["steps"]) <= 6 or e["lab_link"] not in lab_links or bool(e["lab_link"]) != bool(e["lab_cta"]):
            errors.append(f"{s}: example mal formado")
        questions = [lesson["check"]] + list(lesson["checks"])
        if len(questions) != 3:
            errors.append(f"{s}: deben ser 3 preguntas (check + 2 checks)")
        for qi, q in enumerate(questions, 1):
            o = q.get("options", [])
            if (
                len(o) != 3
                or sum(1 for x in o if x.get("ok")) != 1
                or any(set(x) != {"text", "ok", "feedback"} or not x["feedback"].strip() for x in o)
                or len({x["text"] for x in o}) != 3
            ):
                errors.append(f"{s} pregunta {qi}: mal formada")
    print(f"{len(nodes)} nodos, {sum(len(n['items']) for n in nodes)} tarjetas, {len(lessons)} lecciones")
    print("SIN ERRORES" if not errors else "ERRORES:\n" + "\n".join(errors))
    return 1 if errors else 0


def dump(module: str, nodes_var: str, lessons_var: str) -> int:
    nodes, lessons = _load(module, nodes_var, lessons_var)

    def check_text(c: dict) -> str:
        t = c["type"]
        if t == "numeric":
            return f"NUM {c['value']} tol={c['tolerance']} {c['unit']}"
        if t == "choice":
            return "OPC: " + " | ".join(("[OK] " if i == c["correct"] else "") + o for i, o in enumerate(c["options"]))
        if t == "order":
            return "ORDEN: " + " → ".join(c["lines"])
        return json.dumps(c, ensure_ascii=False)

    for n in nodes:
        print("=" * 80)
        print(n["slug"], "—", n["title"], "| after", n["insert_after"], "| prereq", n["prerequisites"], "|", n["metadata"])
        print("Resumen:", n["summary"])
        lesson = lessons[n["slug"]]
        print("GANCHO:", lesson["hook"]["question"], "//", lesson["hook"]["intuition"])
        for p in lesson["concept"]["points"]:
            print(" •", p)
        for r in lesson["concept"]["real_world"]:
            print(" [MR]", r["title"], ":", r["detail"])
        print(" REGLA:", lesson["concept"]["key_rule"])
        print(" ERROR:", lesson["concept"]["pitfall"])
        print(" EJEMPLO:", lesson["example"]["title"], "|", lesson["example"]["lab_link"], lesson["example"]["lab_cta"])
        for i, s in enumerate(lesson["example"]["steps"], 1):
            print(f"   {i}. {s}")
        for q in [lesson["check"]] + lesson["checks"]:
            print(" PREG:", q["question"])
            for o in q["options"]:
                print("    ", "[OK]" if o["ok"] else "[--]", o["text"], "→", o["feedback"])
        print(" CIERRE:", lesson["takeaway_prompt"])
        for i, it in enumerate(n["items"], 1):
            print(f"[#{i}] ({it['item_type']}) {it['title']}\n   P: {it['prompt']}\n   R: {it['answer']}\n   H: {' / '.join(it['hints'])}\n   {check_text(it['payload']['check'])} {it['payload'].get('lab_link', '')}")
    return 0


if __name__ == "__main__":
    if len(sys.argv) == 6 and sys.argv[1] == "validate":
        sys.exit(validate(*sys.argv[2:6]))
    if len(sys.argv) == 5 and sys.argv[1] == "dump":
        sys.exit(dump(*sys.argv[2:5]))
    print(__doc__)
    sys.exit(2)
