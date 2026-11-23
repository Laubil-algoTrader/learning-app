"""Splice extra topics into a discipline's roadmap.

Topic packs written after the original curriculum (entrance-exam algebra, detailed
mechanics) live in their own modules. Each of their nodes names the existing node it
follows (`insert_after`); positions, levels and the "N." title prefixes are derived
here, so adding a topic never means renumbering the others by hand.
"""

from __future__ import annotations

import re
from typing import Any

_NUMBER_PREFIX = re.compile(r"^\d+\.\s*")


def insert_nodes(nodes: list[dict[str, Any]], extra: list[dict[str, Any]]) -> None:
    """Insert each extra node right after its `insert_after` anchor, in the given order."""
    for source in extra:
        node = dict(source)
        anchor = node.pop("insert_after")
        if any(n["slug"] == node["slug"] for n in nodes):
            raise ValueError(f"duplicate node slug: {node['slug']}")
        idx = next((i for i, n in enumerate(nodes) if n["slug"] == anchor), None)
        if idx is None:
            raise ValueError(f"{node['slug']}: unknown insert_after '{anchor}'")
        # A topic that opens a section belongs to the level of the node it precedes.
        section = node.get("metadata", {}).get("section")
        following = nodes[idx + 1] if idx + 1 < len(nodes) else None
        opens_section = (
            following is not None
            and nodes[idx].get("metadata", {}).get("section") != section
            and following.get("metadata", {}).get("section") == section
        )
        node.setdefault("level", (following if opens_section else nodes[idx])["level"])
        nodes.insert(idx + 1, node)


def renumber(nodes: list[dict[str, Any]]) -> None:
    """Make `order_index` and the "N." title prefix follow the list order."""
    for position, node in enumerate(nodes, start=1):
        node["order_index"] = position
        node["title"] = f"{position}. {_NUMBER_PREFIX.sub('', node['title'])}"
