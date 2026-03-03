#!/usr/bin/env python3
"""
_tests/test_code_blocks.py

Verify that every executable code block in the docs can be:
  1. Compiled to WAT text via `multilingual build-wasm-bundle`.
  2. Assembled to a binary via `wat2wasm`.
  3. Validated as a well-formed WASM module via `wasm-validate`.
  4. Executed (calling __main()) without trapping, via the wasmtime Python API.

Run locally (requires multilingual, wabt, and optionally wasmtime installed):
    pytest _tests/ -v

Each code block becomes its own parametrized test case, identified by
its source file and zero-based index within that file:

    test_code_blocks.py::test_block[getting-started/quick-start.md::block-2]
"""

import re
import subprocess
from pathlib import Path

import pytest

# ---------------------------------------------------------------------------
# Configuration — must match NON_EXECUTABLE in main.js and compile_blocks.py
# ---------------------------------------------------------------------------

NON_EXECUTABLE = {
    'bash', 'sh', 'shell', 'powershell', 'cmd',
    'yaml', 'toml', 'json', 'plaintext', 'text',
    'output', 'wat', 'rust',
    '',
}

REPO_ROOT = Path(__file__).parent.parent
COMPILE_TIMEOUT = 60   # seconds — build-wasm-bundle per block
ASSEMBLE_TIMEOUT = 30  # seconds — wat2wasm
VALIDATE_TIMEOUT = 10  # seconds — wasm-validate
EXECUTE_TIMEOUT  = 10  # seconds — __main() wall-clock guard


# ---------------------------------------------------------------------------
# Block collection
# ---------------------------------------------------------------------------

def _collect_blocks():
    """
    Yield pytest.param(code, id=...) for every executable fenced code block
    found in the docs markdown files.

    A block is included when its language tag is NOT in NON_EXECUTABLE.
    Unlike compile_blocks.py we do NOT filter on `print(` — we want to test
    every block that the docs present to readers as executable.
    """
    pattern = re.compile(r'^```(\w*)\n(.*?)^```', re.MULTILINE | re.DOTALL)

    md_files = sorted(
        p for p in REPO_ROOT.rglob('*.md')
        if '.jekyll-cache' not in p.parts and 'vendor' not in p.parts
    )

    for md_file in md_files:
        content = md_file.read_text(encoding='utf-8')
        rel     = md_file.relative_to(REPO_ROOT).as_posix()
        for idx, m in enumerate(pattern.finditer(content)):
            lang = m.group(1).lower()
            code = m.group(2).strip()
            if lang in NON_EXECUTABLE or not code:
                continue
            yield pytest.param(code, id=f'{rel}::block-{idx}')


# ---------------------------------------------------------------------------
# Execution helper (wasmtime Python API)
# ---------------------------------------------------------------------------

def _execute_wasm(wasm_path: Path) -> str:
    """
    Instantiate *wasm_path* with the standard multilingual host imports and
    call ``__main()``.  Returns the captured stdout string.

    Raises ``pytest.skip`` if the wasmtime Python package is not installed.
    Raises ``AssertionError`` if ``__main`` traps or is not exported.
    """
    try:
        from wasmtime import Engine, FuncType, Linker, Module, Store, ValType
    except ImportError:
        pytest.skip('wasmtime Python package not installed — skipping execution check')

    engine = Engine()
    store  = Store(engine)
    module = Module(engine, wasm_path.read_bytes())
    linker = Linker(engine)

    buf      = []
    mem_ref  = [None]

    # Host callbacks — mirror the ABI declared in the WAT backend
    def _print_str(ptr, length):
        if mem_ref[0] is not None:
            raw = bytes(mem_ref[0].data(store)[ptr: ptr + length])
            buf.append(raw.decode('utf-8', errors='replace'))

    i32 = ValType.i32()
    f64 = ValType.f64()

    linker.define_func('env', 'print_str',     FuncType([i32, i32], []), _print_str)
    linker.define_func('env', 'print_f64',     FuncType([f64],       []), lambda v: buf.append(str(v)))
    linker.define_func('env', 'print_bool',    FuncType([i32],       []), lambda v: buf.append('True' if v else 'False'))
    linker.define_func('env', 'print_sep',     FuncType([],          []), lambda: buf.append(' '))
    linker.define_func('env', 'print_newline', FuncType([],          []), lambda: buf.append('\n'))

    instance = linker.instantiate(store, module)
    exports  = instance.exports(store)

    assert 'memory' in [e.name for e in module.exports], \
        "WASM module does not export 'memory'"
    assert '__main' in [e.name for e in module.exports], \
        "WASM module does not export '__main'"

    mem_ref[0] = exports['memory']
    exports['__main'](store)

    return ''.join(buf)


# ---------------------------------------------------------------------------
# Test
# ---------------------------------------------------------------------------

@pytest.mark.parametrize('code', _collect_blocks())
def test_block(code, tmp_path):
    """
    Each executable code block in the docs must:
      1. Compile to WAT text without error.
      2. Assemble into a valid WASM binary.
      3. Execute __main() without trapping.
    """
    src_file  = tmp_path / 'block.ml'
    out_dir   = tmp_path / 'out'
    out_dir.mkdir()
    src_file.write_text(code, encoding='utf-8')

    # ── Step 1: Compile to WAT ──────────────────────────────────────────────
    result = subprocess.run(
        ['multilingual', 'build-wasm-bundle', str(src_file), '--out-dir', str(out_dir)],
        capture_output=True, text=True, timeout=COMPILE_TIMEOUT,
    )
    assert result.returncode == 0, (
        f'build-wasm-bundle failed (exit {result.returncode}):\n'
        f'{result.stderr.strip()}'
    )

    wat_file = out_dir / 'module.wat'
    assert wat_file.exists(), (
        'build-wasm-bundle succeeded but produced no module.wat'
    )

    # ── Step 2: Assemble WAT → WASM binary ─────────────────────────────────
    wasm_file = out_dir / 'module.wasm'
    result = subprocess.run(
        ['wat2wasm', str(wat_file), '-o', str(wasm_file)],
        capture_output=True, timeout=ASSEMBLE_TIMEOUT,
    )
    assert result.returncode == 0, (
        f'wat2wasm failed (exit {result.returncode}):\n'
        f'{result.stderr.decode(errors="replace").strip()}'
    )

    # ── Step 3: Validate ────────────────────────────────────────────────────
    result = subprocess.run(
        ['wasm-validate', str(wasm_file)],
        capture_output=True, timeout=VALIDATE_TIMEOUT,
    )
    assert result.returncode == 0, (
        f'wasm-validate rejected the binary:\n'
        f'{result.stderr.decode(errors="replace").strip()}'
    )

    # ── Step 4: Execute (requires wasmtime Python package) ──────────────────
    _execute_wasm(wasm_file)
