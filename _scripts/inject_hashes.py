#!/usr/bin/env python3
"""
_scripts/inject_hashes.py

Post-processes every HTML file in _site/ to add a data-block-hash attribute
to each <pre> element whose code block has a compiled WASM binary in
assets/wasm/blocks/.

Run this AFTER `bundle exec jekyll build` and AFTER `compile_blocks.py`:

    python _scripts/compile_blocks.py
    bundle exec jekyll build --baseurl /docs
    python _scripts/inject_hashes.py

The JS (main.js) then reads pre.dataset.blockHash directly instead of
re-computing a hash from code.textContent, eliminating the fragile
browser-side hash computation.
"""

import hashlib
import html as html_mod
import re
from pathlib import Path

BLOCKS_DIR = Path('assets/wasm/blocks')
SITE_DIR   = Path('_site')

# Pre-build the set of available hashes for fast lookup.
_available = {p.stem for p in BLOCKS_DIR.glob('*.wasm')}


def _text_content(html_str: str) -> str:
    """Strip HTML tags and decode entities — equivalent to element.textContent."""
    return html_mod.unescape(re.sub(r'<[^>]+>', '', html_str))


def _sha16(text: str) -> str:
    return hashlib.sha256(text.encode('utf-8')).hexdigest()[:16]


# Matches <pre ...><code ...>...</code></pre>.
# Language filtering is intentionally omitted: compile_blocks.py only produced
# WASM for valid blocks, so hash lookup is the only gate needed.
_PRE_RE = re.compile(
    r'(<pre\b)([^>]*)(>)\s*(<code\b[^>]*>)(.*?)</code>\s*</pre>',
    re.DOTALL,
)


def _inject(content: str) -> str:
    def _replace(m: re.Match) -> str:
        pre_tag   = m.group(1)   # '<pre'
        pre_attrs = m.group(2)   # attrs between '<pre' and '>'
        pre_close = m.group(3)   # '>'
        code_open = m.group(4)   # full '<code ...>'
        code_body = m.group(5)   # raw HTML inside <code>

        # Idempotent.
        if 'data-block-hash' in pre_attrs:
            return m.group(0)

        text = _text_content(code_body).strip()
        if not text:
            return m.group(0)

        h = _sha16(text)
        if h not in _available:
            return m.group(0)

        return f'{pre_tag}{pre_attrs} data-block-hash="{h}"{pre_close}{code_open}{code_body}</code></pre>'

    return _PRE_RE.sub(_replace, content)


def main() -> None:
    if not SITE_DIR.exists():
        print(f'ERROR: {SITE_DIR} not found — run `bundle exec jekyll build` first.')
        raise SystemExit(1)
    if not BLOCKS_DIR.exists() or not _available:
        print(f'WARNING: no compiled WASM blocks found in {BLOCKS_DIR}.')

    modified = 0
    for html_file in SITE_DIR.rglob('*.html'):
        original = html_file.read_text(encoding='utf-8')
        updated  = _inject(original)
        if updated != original:
            html_file.write_text(updated, encoding='utf-8')
            modified += 1

    total = sum(1 for _ in SITE_DIR.rglob('*.html'))
    print(f'inject_hashes: {modified}/{total} HTML files updated '
          f'({len(_available)} WASM blocks available).')


if __name__ == '__main__':
    main()
