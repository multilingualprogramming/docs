#!/usr/bin/env python3
"""
_scripts/compile_blocks.py

Compile every executable code block found in the docs markdown files into its
own WASM binary, stored under assets/wasm/blocks/<hash16>.wasm.

Blocks are attempted for compilation when:
  - Their language tag is NOT in NON_EXECUTABLE.
  - Their content contains at least one `print(` call (so they produce output).

Compilation failures are silently skipped (the block simply won't get a Run
button).  After the run, assets/wasm/blocks/manifest.json is written so that
_scripts/inject_hashes.py can match compiled blocks to their HTML counterparts
by source text rather than by independently recomputing a hash.

Usage (called from CI after `multilingual` and `wabt` are installed):
    python _scripts/compile_blocks.py
"""

import hashlib
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

# Languages that never receive a Run button (matches NON_EXECUTABLE in main.js)
NON_EXECUTABLE = {
    'bash', 'sh', 'shell', 'powershell', 'cmd',
    'js', 'javascript', 'markdown', 'dockerfile',
    'yaml', 'toml', 'json', 'plaintext', 'text', 'output', 'wat', 'rust',
    '',
}

BLOCKS_DIR = Path('assets/wasm/blocks')
MANIFEST   = BLOCKS_DIR / 'manifest.json'
TIMEOUT    = 60   # seconds per block compilation


def sha16(code: str) -> str:
    return hashlib.sha256(code.encode('utf-8')).hexdigest()[:16]


def compile_block(code: str, hash16: str) -> bool:
    """Compile `code` to WASM. Returns True on success, False on failure."""
    wasm_path = BLOCKS_DIR / f'{hash16}.wasm'
    if wasm_path.exists():
        print('cached')
        return True

    with tempfile.TemporaryDirectory() as tmp:
        src = Path(tmp) / 'block.ml'
        out = Path(tmp) / 'out'
        out.mkdir()
        src.write_text(code, encoding='utf-8')

        try:
            subprocess.run(
                ['multilingual', 'build-wasm-bundle', str(src), '--out-dir', str(out)],
                check=True, timeout=TIMEOUT, capture_output=True, text=True,
            )
        except subprocess.CalledProcessError as e:
            print(f'skip ({e.stderr.strip()[:80]})', file=sys.stderr)
            return False
        except subprocess.TimeoutExpired:
            print('skip (timeout)', file=sys.stderr)
            return False

        wat_file = out / 'module.wat'
        if not wat_file.exists():
            print('skip (no module.wat)', file=sys.stderr)
            return False

        try:
            subprocess.run(
                ['wat2wasm', str(wat_file), '-o', str(wasm_path)],
                check=True, timeout=30, capture_output=True,
            )
        except Exception as e:
            print(f'skip (wat2wasm: {e})', file=sys.stderr)
            wasm_path.unlink(missing_ok=True)
            return False

        print('ok')
        return True


def main():
    BLOCKS_DIR.mkdir(parents=True, exist_ok=True)

    # Load existing manifest so cached entries are preserved.
    manifest: dict[str, str] = {}
    if MANIFEST.exists():
        manifest = json.loads(MANIFEST.read_text(encoding='utf-8'))

    pattern = re.compile(r'^```(\w*)\n(.*?)^```', re.MULTILINE | re.DOTALL)

    md_files = sorted(
        p for p in Path('.').rglob('*.md')
        if '.jekyll-cache'    not in p.parts
        and 'vendor'          not in p.parts
        and 'multilingual-src' not in p.parts
    )

    total = compiled = skipped = cached = 0

    for md_file in md_files:
        content = md_file.read_text(encoding='utf-8')
        for m in pattern.finditer(content):
            lang = m.group(1).lower()
            code = m.group(2).strip()
            total += 1

            if lang in NON_EXECUTABLE:
                skipped += 1
                continue
            if 'print(' not in code:
                skipped += 1
                continue

            h = sha16(code)
            print(f'  [{h}] {md_file.name} ... ', end='', flush=True)

            ok = compile_block(code, h)
            if ok:
                compiled += 1
                manifest[h] = code   # record source text for inject_hashes.py
                if (BLOCKS_DIR / f'{h}.wasm').exists() and h in manifest:
                    cached += (1 if 'cached' in str(ok) else 0)
            else:
                skipped += 1

    MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=2),
                        encoding='utf-8')
    print(f'\nDone: {compiled} compiled, {skipped} skipped, {total} total.')
    print(f'Manifest written to {MANIFEST} ({len(manifest)} entries).')


if __name__ == '__main__':
    main()
