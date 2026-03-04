#!/usr/bin/env python3
"""
_tests/test_code_blocks.py

Verify that every executable code block in the docs runs correctly via
ProgramExecutor — the same engine used by the browser REPL and inline
Run buttons (Pyodide client-side).

Run locally (requires multilingualprogramming installed):
    pytest _tests/ -v

Each code block becomes its own parametrized test case, identified by
its source file and zero-based index within that file:

    test_code_blocks.py::test_block[getting-started/quick-start.md::block-2]
"""

import re
from pathlib import Path

import pytest

from multilingualprogramming.codegen.executor import ProgramExecutor

# ---------------------------------------------------------------------------
# Configuration — language tags that are not executable multilingual source.
# Must match NON_EXECUTABLE in main.js.
# ---------------------------------------------------------------------------

NON_EXECUTABLE = {
    'bash', 'sh', 'shell', 'powershell', 'cmd',
    'js', 'javascript', 'markdown', 'dockerfile',
    'yaml', 'toml', 'json', 'plaintext', 'text',
    'output', 'wat', 'rust',
    '',
}

REPO_ROOT = Path(__file__).parent.parent

# Blocks whose first line is a host-Python import/shebang — not standalone
# multilingual programs.
HOST_PY_RE = re.compile(
    r'^\s*(import\s+[\w.]+|from\s+[\w.]+\s+import\s+|#!/usr/bin/env\s+python\d*(?:\.\d+)*)',
    re.MULTILINE,
)

# Orphan API blocks that reference names defined in a prior block in the same
# file (executor, sel, wasm_gen, Lexer, Parser, …).  These are documentation
# code fragments, not standalone programs.
PYTHON_API_RE = re.compile(
    r'executor\.|BackendSelector\(\)|NumeralConverter\(\)|ProgramExecutor\(\)'
    r'|wasm_gen\.|sel\.|Lexer\(language=|Parser\(language='
    r'|SemanticAnalyzer\(|ASTPrinter\(\)|\.generate_rust\('
)


# ---------------------------------------------------------------------------
# Block collection
# ---------------------------------------------------------------------------

def _collect_blocks():
    """
    Yield pytest.param(code, id=...) for every executable fenced code block
    found in the docs markdown files.
    """
    pattern = re.compile(r'^```(\w*)\n(.*?)^```', re.MULTILINE | re.DOTALL)

    md_files = sorted(
        p for p in REPO_ROOT.rglob('*.md')
        if '.jekyll-cache'     not in p.parts
        and 'vendor'           not in p.parts
        and 'multilingual-src' not in p.parts
    )

    for md_file in md_files:
        content = md_file.read_text(encoding='utf-8')
        rel     = md_file.relative_to(REPO_ROOT).as_posix()
        for idx, m in enumerate(pattern.finditer(content)):
            lang = m.group(1).lower()
            code = m.group(2).strip()
            if lang in NON_EXECUTABLE or not code:
                continue
            if HOST_PY_RE.search(code) or PYTHON_API_RE.search(code):
                continue
            if 'print(' not in code:
                continue
            yield pytest.param(code, id=f'{rel}::block-{idx}')


# ---------------------------------------------------------------------------
# Test
# ---------------------------------------------------------------------------

@pytest.mark.parametrize('code', _collect_blocks())
def test_block(code):
    """
    Each executable code block in the docs must execute without errors
    via ProgramExecutor — the same engine used by the browser REPL.
    """
    result = ProgramExecutor(language='en').execute(code)
    assert result.success, (
        f'ProgramExecutor reported failure:\n' +
        '\n'.join(result.errors or ['(no error details)'])
    )
