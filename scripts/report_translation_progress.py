#!/usr/bin/env python
"""Report EN/FR translation progress for docs/content."""

from __future__ import annotations

from collections import Counter
from pathlib import Path

import yaml


def parse_front_matter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}
    parts = text.split("---\n", 2)
    if len(parts) < 3:
        return {}
    data = yaml.safe_load(parts[1]) or {}
    return data if isinstance(data, dict) else {}


def main() -> int:
    root = Path(__file__).resolve().parents[1] / "docs" / "content" / "fr"
    files = sorted(root.rglob("*.md"))
    statuses = Counter()
    rows: list[tuple[str, str, str]] = []
    for path in files:
        meta = parse_front_matter(path)
        page_id = str(meta.get("page_id", ""))
        status = str(meta.get("status", "missing"))
        statuses[status] += 1
        rows.append((page_id, status, str(path.relative_to(root))))

    total = len(files)
    translated = statuses.get("translated", 0)
    print(f"Total FR pages: {total}")
    print(f"Translated: {translated}")
    print(f"Needs update: {statuses.get('needs_update', 0)}")
    print(f"Source-marked: {statuses.get('source', 0)}")
    print()
    for page_id, status, rel in rows:
        print(f"{status:12} {page_id:40} {rel}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
