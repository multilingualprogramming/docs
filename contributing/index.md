---
layout: page
title: "Contributing & Development"
description: "Setup, testing, debugging, and contributing to multilingual."
category: "Contributing"
permalink: /contributing/
---

This guide covers contributor setup, the development workflow, testing, and debugging.

---

## Setup

Use a virtual environment and editable install so code changes are picked up immediately without reinstalling.

```bash
python -m venv .venv

# Windows PowerShell
.venv\Scripts\Activate.ps1

# Linux / macOS
source .venv/bin/activate

python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

If your shell doesn't support the extras syntax:

```bash
python -m pip install -e .
python -m pip install pytest pytest-cov pylint
```

---

## CLI During Development

### End-user style

```bash
multilingual repl
multilingual run hello.ml
multilg run hello.ml
```

### Python module style (recommended while developing)

Using module style ensures you're running exactly the Python interpreter and environment under your virtual environment:

```bash
python -m multilingualprogramming repl
python -m multilingualprogramming run hello.ml --lang fr
python -m multilingualprogramming compile hello.ml
python -m multilingualprogramming smoke --all
```

---

## Running Tests

### All tests

```bash
python -m pytest -q
```

### One test file

```bash
python -m pytest -q tests/parser_test.py
```

### Focused subset

```bash
python -m pytest -q tests/parser_test.py -k "async or comprehension"
```

### With output (for debugging)

```bash
python -m pytest -q -s tests/repl_test.py
```

### Coverage report

```bash
python -m pytest --cov=multilingualprogramming --cov-report=term-missing
```

---

## Test Suite Overview

| Suite | File | Description |
|-------|------|-------------|
| Parser | `tests/parser_test.py` | AST construction from all constructs |
| Executor | `tests/executor_test.py` | End-to-end program execution |
| Semantic | `tests/semantic_test.py` | Scope/symbol validation |
| Codegen | `tests/codegen_test.py` | Python code generation |
| Core IR | `tests/core_ir_test.py` | Core IR lowering and structure |
| Frontend equivalence | `tests/frontend_equivalence_test.py` | Cross-language AST equivalence |
| REPL | `tests/repl_test.py` | REPL commands and interaction |
| Numerals | `tests/numeral_test.py` | MPNumeral, UnicodeNumeral, etc. |
| Keywords | `tests/keywords_test.py` | KeywordRegistry lookups |
| Surface | `tests/surface_*.py` | Language-specific surface normalization |
| WASM | `tests/wasm_*.py` | Backend selector and fallbacks |

Total: **858 tests across 78 suites** (as of v0.4.0)

---

## Lint and Quality Checks

```bash
python -m pylint $(git ls-files '*.py')
```

On Windows PowerShell:

```powershell
python -m pylint (git ls-files '*.py')
```

---

## Debugging

### Show generated Python in REPL

```bash
python -m multilingualprogramming repl --show-python
```

### Debug parser/codegen for a specific file

```bash
python -m multilingualprogramming compile examples/surface_for_es.ml --lang es
```

### Python breakpoint

```python
breakpoint()
```

Then run:

```bash
python -m multilingualprogramming run examples/arithmetics_en.ml --lang en
```

---

## Packaging Sanity Check

After modifying `pyproject.toml` entry points, reinstall:

```bash
python -m pip install -e .
```

Verify all entry points:

```bash
multilingual --version
multilg --version
python -m multilingualprogramming --version
```

---

## Project Structure

```
multilingualprogramming/
├── __init__.py              # Public exports
├── lexer/
│   └── lexer.py             # Unicode-aware tokenizer
├── parser/
│   ├── parser.py            # Parser → AST
│   └── ast_nodes.py         # AST node classes
├── core/
│   ├── core_ir.py           # CoreIRProgram dataclass
│   └── lowering.py          # Surface AST → Core IR
├── semantic/
│   └── analyzer.py          # Scope/type checker
├── codegen/
│   ├── python_generator.py  # Python code emitter
│   ├── wasm_generator.py    # WASM code emitter
│   └── runtime_builtins.py  # RuntimeBuiltins
├── runtime/
│   ├── backend_selector.py  # BackendSelector
│   └── python_fallbacks.py  # FALLBACK_REGISTRY
├── resources/
│   └── usm/
│       ├── keywords/        # keywords.json per language
│       ├── builtins_aliases.json
│       └── surface_patterns.json
├── repl/
│   └── repl.py              # Interactive REPL
└── cli/
    └── main.py              # CLI entry point
tests/
examples/
docs/
```

---

## Contributing a New Language

See [Add a Language](/extending/) for the full 8-step onboarding process.

In summary:
1. Add `keywords.json` for your language code
2. Add `error_messages.json`
3. Add `builtins_aliases.json` entries
4. Add `surface_patterns.json` normalization rules if needed
5. Write equivalence tests
6. Run validation commands
7. Submit a pull request

---

## Python Compatibility Roadmap

The project targets full CPython 3.12 compatibility across five stages:

| Stage | Goal |
|-------|------|
| 0 | Baseline freeze and measurement |
| 1 | Syntax coverage parity (parser/lexer) |
| 2 | Semantic and runtime parity |
| 3 | Import/stdlib parity |
| 4 | Ecosystem compatibility |

All compatibility claims must be test-backed. The `docs/reference/compatibility/` page is the source-of-truth status table.

---

## Opening Issues and PRs

- Bug reports: [GitHub Issues](https://github.com/johnsamuelwrites/multilingual/issues)
- Feature requests: [GitHub Discussions](https://github.com/johnsamuelwrites/multilingual/discussions)
- Pull requests: target the `main` branch

Include:
- A minimal reproduction case for bugs
- Test coverage for new features
- Updated documentation for user-facing changes
