---
page_id: contributing
locale: fr
title: Contribution et developpement
path_segments:
- contribution
source_hash: 246c35a74a08
status: translated
permalink: /fr/docs/contribution/
---

Ce guide reflete le flux de developpement actuel en `0.5.1`.

- [Documentation multilingue](/fr/contributing/multilingual-docs/)

---

## Installation de developpement

```bash
python -m venv .venv

# Windows PowerShell
.venv\Scripts\Activate.ps1

# Linux / macOS
source .venv/bin/activate

python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Extras optionnels:

```bash
python -m pip install -e ".[wasm]"
python -m pip install -e ".[dev,wasm]"
```

---

## Commandes utiles

```bash
multilingual repl
multilingual run hello.ml
multilg run hello.ml
python -m multilingualprogramming smoke --all
```

---

## Tests

```bash
python -m pytest -q
python -m pytest --cov=multilingualprogramming tests/ -v
python -m pytest tests/lexer_test.py -v
python -m pytest -m wasm tests/
python -m pytest -k "inheritance" tests/
```

D'apres la reference locale actuelle:
- environ 58 fichiers de tests
- environ 1 797 tests
- 2 tests ignores attendus pour `rustc wasm32`

Fichiers cles:
- `tests/lexer_test.py`
- `tests/parser_test.py`
- `tests/semantic_analyzer_test.py`
- `tests/executor_test.py`
- `tests/wat_generator_test.py`
- `tests/frontend_equivalence_test.py`
- `tests/regression_fixes_test.py`

---

## Linting

```bash
pylint $(git ls-files '*.py')
```

Sous PowerShell:

```powershell
python -m pylint (git ls-files '*.py')
```

---

## Validation rapide

```bash
multilingual smoke --all
multilingual smoke --lang fr
python -m multilingualprogramming --version
```

---

## Debogage du REPL

```bash
python -m multilingualprogramming repl --show-python --show-wat --show-rust
```

{{snippet:contributing__py01}}

---

## Points d'attention

- Les affectations simples definissent maintenant les variables pendant l'analyse semantique.
- Le REPL prend en charge `:wat` / `:wasm` et `:rust` / `:wasmtime`.
- `WATCodeGenerator` est le backend WASM principal; le generateur Rust intermediaire est legacy.
- Si vous ajoutez un concept de mot-cle, mettez aussi a jour `tests/keyword_registry_test.py`.
