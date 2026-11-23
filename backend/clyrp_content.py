"""Comprensión Lectora y Resolución de Problemas (CLyRP), a module of the UNCuyo entrance course.

The topics live in two packs (reading and language; problem solving). Their nodes are chained
with `insert_after` ("__start__" for the first one); this module lays them out in that order,
gives each section its own level and numbers the titles.
"""

from __future__ import annotations

from typing import Any

from backend.clyrp_lectura_content import CLYRP_LECTURA_LESSONS, CLYRP_LECTURA_NODES
from backend.clyrp_problemas_content import CLYRP_PROBLEMAS_LESSONS, CLYRP_PROBLEMAS_NODES
from backend.content_merge import renumber


def _chain(nodes: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Order nodes by their insert_after links, starting from "__start__"."""
    by_anchor = {n["insert_after"]: n for n in nodes}
    ordered: list[dict[str, Any]] = []
    anchor = "__start__"
    while anchor in by_anchor:
        node = dict(by_anchor.pop(anchor))
        node.pop("insert_after")
        ordered.append(node)
        anchor = node["slug"]
    if by_anchor:
        raise ValueError(f"CLyRP nodes not reachable from __start__: {sorted(n['slug'] for n in by_anchor.values())}")
    return ordered


def _build_nodes() -> list[dict[str, Any]]:
    nodes = _chain(CLYRP_LECTURA_NODES + CLYRP_PROBLEMAS_NODES)
    sections: list[str] = []
    for node in nodes:
        section = node["metadata"]["section"]
        if section not in sections:
            sections.append(section)
        node["level"] = sections.index(section) + 1
    renumber(nodes)
    return nodes


CLYRP_DOMAIN: dict[str, Any] = {
    "slug": "comprension-problemas",
    "name": "Comprensión lectora y resolución de problemas",
    "icon": "book",
    "color": "#5b6b3a",
    "domain_type": "conceptual",
    "lab_type": "generic",
    "description": (
        "El tercer módulo del ingreso a Ingeniería de la UNCuyo: leer textos científicos y consignas, "
        "pasar del lenguaje coloquial al simbólico, lógica, tablas y gráficos, y estrategias para resolver "
        "problemas de porcentajes, fracciones, edades y geometría."
    ),
    "config": {
        "tools": [],
        "method_tips": [
            "En las preguntas sobre un texto, justificá cada respuesta con una frase concreta del texto: si no la encontrás, desconfiá de esa opción.",
            "Antes de calcular, escribí qué representa cada letra y qué te piden; al final, verificá el resultado en el enunciado.",
            "En los acertijos de lógica armá siempre la tabla de doble entrada y marcá lo que queda descartado.",
        ],
    },
    "nodes": _build_nodes(),
}

CLYRP_LESSONS: dict[str, dict[str, Any]] = {**CLYRP_LECTURA_LESSONS, **CLYRP_PROBLEMAS_LESSONS}
