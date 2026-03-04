#!/usr/bin/env python3
"""
_scripts/compile_blocks.py

Compile every executable code block found in the docs markdown files into its
own WASM binary, stored under assets/wasm/blocks/<hash16>.wasm.

The hash is the first 16 hex characters of the SHA-256 digest of the
(UTF-8, whitespace-stripped) code block content — the same value computed
by the browser at runtime via SubtleCrypto, so the JS can locate the right
binary without any extra build-time HTML annotation.

A block is compiled only when:
  - Its language tag is NOT in NON_EXECUTABLE.
  - Its content contains at least one `print(` call (so it produces output).
  - `multilingual build-wasm-bundle` exits successfully within TIMEOUT seconds.

Blocks that fail to compile are silently skipped; the browser falls back to
the pre-compiled demo binary for those blocks.

Usage (called from CI after `multilingual` and `wabt` are installed):
    python _scripts/compile_blocks.py
"""

import hashlib
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
TIMEOUT    = 60   # seconds per block compilation

HOST_PY_RE = re.compile(
    r'^\s*(import\s+[\w.]+|from\s+[\w.]+\s+import\s+|#!/usr/bin/env\s+python\d*(?:\.\d+)*)',
    re.MULTILINE,
)
PYTHON_API_RE = re.compile(
    r'executor\.|BackendSelector\(\)|NumeralConverter\(\)|ProgramExecutor\(\)'
    r'|wasm_gen\.|sel\.|Lexer\(language=|Parser\(language='
    r'|SemanticAnalyzer\(|ASTPrinter\(\)|\.generate_rust\('
)
WASM_UNSUPPORTED_RE = re.compile(
    r'\byield\b'                        # generators / yield from
    r'|^\s*match\s+\S'                 # structural pattern matching
    r'|:='                              # walrus operator
    r'|^\s*@\w'                         # function / class decorators
    r'|\blambda\b'                      # lambda expressions
    r'|\*\*\w+'                         # **kwargs double-star arg
    r'|(?:,|\()\s*\*[a-zA-Z]'          # *args single-star arg
    r'|(?:,|\()\s*\*\s*,'              # keyword-only * separator  (def f(a, *, b))
    r'|(?:,|\()\s*/\s*[,)]'            # positional-only / sep    (def f(a, b, /))
    r'|\bnonlocal\b'                    # nonlocal (closure)
    r'|\basync\s+(?:def|for|with)\b'   # async / await constructs
    r'|\bcontinue\b'                    # continue (WATCodeGenerator hangs)
    r'|\belif\b',                       # elif (WATCodeGenerator does not yet support)
    re.MULTILINE,
)


def sha16(code: str) -> str:
    """First 16 hex chars of SHA-256(code), matching the browser SubtleCrypto hash."""
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
            r = subprocess.run(
                ['multilingual', 'build-wasm-bundle', str(src), '--out-dir', str(out)],
                check=True, timeout=TIMEOUT, capture_output=True, text=True,
            )
        except subprocess.CalledProcessError as e:
            print(f'build-wasm-bundle failed:\n{e.stderr.strip()}', file=sys.stderr)
            return False
        except subprocess.TimeoutExpired:
            print('timeout', file=sys.stderr)
            return False

        wat_file = out / 'module.wat'
        if not wat_file.exists():
            print('no module.wat produced', file=sys.stderr)
            return False

        try:
            subprocess.run(
                ['wat2wasm', str(wat_file), '-o', str(wasm_path)],
                check=True, timeout=30, capture_output=True,
            )
        except Exception as e:
            print(f'wat2wasm failed: {e}', file=sys.stderr)
            wasm_path.unlink(missing_ok=True)
            return False

        print('ok')
        return True


def main():
    BLOCKS_DIR.mkdir(parents=True, exist_ok=True)

    # Match fenced code blocks: ```lang\n...\n```
    pattern = re.compile(r'^```(\w*)\n(.*?)^```', re.MULTILINE | re.DOTALL)

    md_files = sorted(
        p for p in Path('.').rglob('*.md')
        if '.jekyll-cache'   not in p.parts
        and 'vendor'         not in p.parts
        and 'multilingual-src' not in p.parts  # CI checkout lives inside docs root
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
            if lang == 'python' and (
                HOST_PY_RE.search(code)
                or PYTHON_API_RE.search(code)
                or WASM_UNSUPPORTED_RE.search(code)
            ):
                skipped += 1
                continue
            if 'print(' not in code:
                skipped += 1
                continue

            hash16 = sha16(code)
            wasm_path = BLOCKS_DIR / f'{hash16}.wasm'

            print(f'  [{hash16}] {md_file.name} ... ', end='', flush=True)

            if wasm_path.exists():
                print('cached')
                cached += 1
                compiled += 1
                continue

            ok = compile_block(code, hash16)
            if ok:
                compiled += 1
            else:
                skipped += 1

    print(
        f'\nDone: {compiled} compiled ({cached} from cache), '
        f'{skipped} skipped, {total} total blocks examined.'
    )


if __name__ == '__main__':
    main()
