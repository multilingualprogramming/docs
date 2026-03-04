#!/usr/bin/env python3
"""
_scripts/inject_hashes.py

Post-processes every HTML file in _site/ to add a data-block-hash attribute
to each <pre> element whose code block was successfully compiled to WASM.

Uses assets/wasm/blocks/manifest.json (written by compile_blocks.py) to match
compiled blocks to their HTML counterparts by source text, so there is no
fragile independent hash computation on either side.

Run after `bundle exec jekyll build`:

    python _scripts/compile_blocks.py
    bundle exec jekyll build --baseurl /docs
    python _scripts/inject_hashes.py
"""

import html as html_mod
import json
import re
from pathlib import Path

BLOCKS_DIR = Path('assets/wasm/blocks')
MANIFEST   = BLOCKS_DIR / 'manifest.json'
SITE_DIR   = Path('_site')


def _text_content(html_str: str) -> str:
    """Strip HTML tags and decode entities — equivalent to element.textContent."""
    return html_mod.unescape(re.sub(r'<[^>]+>', '', html_str))


# Matches <pre ...><code ...>...</code></pre>.
_PRE_RE = re.compile(
    r'(<pre\b)([^>]*)(>)\s*(<code\b[^>]*>)(.*?)</code>\s*</pre>',
    re.DOTALL,
)


def _inject(content: str, lookup: dict[str, str]) -> str:
    """lookup maps stripped source text → hash16."""
    def _replace(m: re.Match) -> str:
        pre_tag   = m.group(1)
        pre_attrs = m.group(2)
        pre_close = m.group(3)
        code_open = m.group(4)
        code_body = m.group(5)

        if 'data-block-hash' in pre_attrs:
            return m.group(0)   # idempotent

        text = _text_content(code_body).strip()
        if not text:
            return m.group(0)

        h = lookup.get(text)
        if not h:
            return m.group(0)

        return (f'{pre_tag}{pre_attrs} data-block-hash="{h}"{pre_close}'
                f'{code_open}{code_body}</code></pre>')

    return _PRE_RE.sub(_replace, content)


def main() -> None:
    if not SITE_DIR.exists():
        print(f'ERROR: {SITE_DIR} not found — run `bundle exec jekyll build` first.')
        raise SystemExit(1)
    if not MANIFEST.exists():
        print(f'ERROR: {MANIFEST} not found — run `compile_blocks.py` first.')
        raise SystemExit(1)

    # manifest: hash16 → source_text  →  invert to source_text → hash16
    manifest: dict[str, str] = json.loads(MANIFEST.read_text(encoding='utf-8'))
    lookup = {src: h for h, src in manifest.items()}
    print(f'Loaded {len(lookup)} compiled blocks from manifest.')

    modified = 0
    for html_file in SITE_DIR.rglob('*.html'):
        original = html_file.read_text(encoding='utf-8')
        updated  = _inject(original, lookup)
        if updated != original:
            html_file.write_text(updated, encoding='utf-8')
            modified += 1

    total = sum(1 for _ in SITE_DIR.rglob('*.html'))
    print(f'inject_hashes: {modified}/{total} HTML files updated.')


if __name__ == '__main__':
    main()
