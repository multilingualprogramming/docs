---
page_id: contributing
locale: en
title: Contributing & Development
path_segments:
- contributing
source_hash: 48a6c71c7442
status: source
permalink: /en/docs/contributing/
---

This guide reflects the current `0.6.0` development workflow.

---

## Setup

Use a virtual environment and an editable install:

```bash
python -m venv .venv

# Windows PowerShell
.venv\Scripts\Activate.ps1

# Linux / macOS
source .venv/bin/activate

python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Optional extras:

```bash
python -m pip install -e ".[wasm]"
python -m pip install -e ".[dev,wasm]"
```

---

## Running the CLI During Development

```bash
multilingual repl
multilingual run hello.ml
multilg run hello.ml
```

Module form is still the safest during development:

```bash
python -m multilingualprogramming repl
python -m multilingualprogramming run hello.ml --lang fr
python -m multilingualprogramming compile hello.ml
python -m multilingualprogramming smoke --all
```

---

## Testing

### Full suite

```bash
python -m pytest -q
```

### Coverage

```bash
python -m pytest --cov=multilingualprogramming tests/ -v
```

### One file

```bash
python -m pytest tests/lexer_test.py -v
```

### Markers

```bash
python -m pytest -m "not slow" tests/
python -m pytest -m wasm tests/
python -m pytest -m correctness tests/
python -m pytest -m corpus tests/
```

### Pattern filtering

```bash
python -m pytest -k "inheritance" tests/
```

---

## Test Suite Overview

According to the current upstream repository state:
- 63 test files
- 1,926 collected tests

Key files:
- `tests/lexer_test.py`
- `tests/parser_test.py`
- `tests/semantic_analyzer_test.py`
- `tests/executor_test.py`
- `tests/wat_generator_test.py`
- `tests/complete_features_wat_test.py`
- `tests/complete_features_wasm_execution_test.py`
- `tests/frontend_equivalence_test.py`
- `tests/regression_fixes_test.py`
- `tests/wat_oop_dispatch_test.py`
- `tests/wat_generator_manifest_test.py`
- `tests/wat_generator_string_lambda_test.py`

---

## Linting

```bash
pylint $(git ls-files '*.py')
```

On PowerShell:

```powershell
python -m pylint (git ls-files '*.py')
```

---

## Fast Validation Commands

```bash
multilingual smoke --all
multilingual smoke --lang fr
python -m multilingualprogramming --version
```

---

## REPL Debugging

```bash
python -m multilingualprogramming repl --show-python --show-wat --show-rust
```

{{snippet:contributing__py01}}

---

## Current Project Structure

Important paths in the current tree:
- `multilingualprogramming/codegen/executor.py`
- `multilingualprogramming/codegen/python_generator.py`
- `multilingualprogramming/codegen/wat_generator.py`
- `multilingualprogramming/codegen/wasm_generator.py`
- `multilingualprogramming/codegen/runtime_builtins.py`
- `multilingualprogramming/codegen/repl.py`
- `multilingualprogramming/runtime/backend_selector.py`
- `multilingualprogramming/resources/usm/`
- `tests/`
- `examples/`

---

## Notes for Contributors

- Plain assignments now define variables during semantic analysis; keep this behavior covered by tests.
- REPL supports `:wat` / `:wasm` and `:rust` / `:wasmtime`.
- WAT support is the primary WASM-facing backend; the Rust-intermediate generator is legacy.
- If you add keyword concepts, update the concept-count assertion in `tests/keyword_registry_test.py`.
