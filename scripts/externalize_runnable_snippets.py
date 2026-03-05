#!/usr/bin/env python
"""Externalize runnable Python code blocks into snippet assets.

Rewrites EN/FR docs/content pages:
- extracts paired ```python blocks
- writes docs/snippets/<snippet_id>/en.code and fr.code
- replaces inline code blocks with {{snippet:<snippet_id>}}
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

import yaml

PY_BLOCK_RE = re.compile(r"```python\s*\n(.*?)\n```", re.DOTALL)
SNIPPET_TOKEN_TEMPLATE = "{{snippet:%s}}"


@dataclass
class Page:
    path: Path
    page_id: str
    body: str
    front_matter: dict


def parse_front_matter(path: Path) -> Page:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError(f"{path}: missing YAML front matter")
    parts = text.split("---\n", 2)
    if len(parts) < 3:
        raise ValueError(f"{path}: invalid front matter format")
    front_matter = yaml.safe_load(parts[1]) or {}
    if not isinstance(front_matter, dict):
        raise ValueError(f"{path}: front matter must be a mapping")
    page_id = front_matter.get("page_id")
    if not isinstance(page_id, str) or not page_id:
        raise ValueError(f"{path}: missing page_id")
    return Page(path=path, page_id=page_id, body=parts[2], front_matter=front_matter)


def write_page(page: Page) -> None:
    dumped = yaml.safe_dump(page.front_matter, sort_keys=False, allow_unicode=True).strip()
    page.path.write_text(f"---\n{dumped}\n---\n{page.body}", encoding="utf-8")


def extract_python_blocks(body: str) -> list[str]:
    return [m.group(1) for m in PY_BLOCK_RE.finditer(body)]


def replace_python_blocks(body: str, snippet_ids: list[str]) -> str:
    idx = 0

    def repl(_: re.Match[str]) -> str:
        nonlocal idx
        snippet_id = snippet_ids[idx]
        idx += 1
        return SNIPPET_TOKEN_TEMPLATE % snippet_id

    new_body = PY_BLOCK_RE.sub(repl, body)
    if idx != len(snippet_ids):
        raise ValueError("replacement count mismatch")
    return new_body


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    en_root = repo_root / "docs" / "content" / "en"
    fr_root = repo_root / "docs" / "content" / "fr"
    snippets_root = repo_root / "docs" / "snippets"

    en_pages: dict[str, Page] = {}
    fr_pages: dict[str, Page] = {}

    for path in en_root.rglob("*.md"):
        page = parse_front_matter(path)
        en_pages[page.page_id] = page
    for path in fr_root.rglob("*.md"):
        page = parse_front_matter(path)
        fr_pages[page.page_id] = page

    shared_ids = sorted(set(en_pages) & set(fr_pages))
    processed = 0
    skipped = 0
    created_snippets = 0

    for page_id in shared_ids:
        en_page = en_pages[page_id]
        fr_page = fr_pages[page_id]
        en_blocks = extract_python_blocks(en_page.body)
        fr_blocks = extract_python_blocks(fr_page.body)

        if not en_blocks and not fr_blocks:
            continue
        if len(en_blocks) != len(fr_blocks):
            skipped += 1
            print(
                f"SKIP {page_id}: python block count mismatch "
                f"(en={len(en_blocks)}, fr={len(fr_blocks)})"
            )
            continue

        snippet_ids: list[str] = []
        for i, (en_code, fr_code) in enumerate(zip(en_blocks, fr_blocks), start=1):
            snippet_id = f"{page_id}__py{i:02d}"
            snippet_dir = snippets_root / snippet_id
            snippet_dir.mkdir(parents=True, exist_ok=True)
            (snippet_dir / "en.code").write_text(en_code + "\n", encoding="utf-8")
            (snippet_dir / "fr.code").write_text(fr_code + "\n", encoding="utf-8")
            snippet_ids.append(snippet_id)
            created_snippets += 1

        en_page.body = replace_python_blocks(en_page.body, snippet_ids)
        fr_page.body = replace_python_blocks(fr_page.body, snippet_ids)
        write_page(en_page)
        write_page(fr_page)
        processed += 1

    print(f"Processed pages: {processed}")
    print(f"Created/updated snippets: {created_snippets}")
    print(f"Skipped pages: {skipped}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
