---
page_id: contributing
locale: fr
title: Contribution et développement
path_segments:
- contribution
source_hash: 48a6c71c7442
status: translated
permalink: /fr/docs/contribution/
---

Ce guide reflète le flux de développement actuel en `0.6.0`.

- [Documentation multilingue]({{ '/fr/docs/contribution/documentation-multilingue/' | relative_url }})

---

## Installation de développement

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

D'après l'état actuel du dépôt amont :
- 63 fichiers de tests
- 1 926 tests collectés

Fichiers clés :
- `tests/lexer_test.py`
- `tests/parser_test.py`
- `tests/semantic_analyzer_test.py`
- `tests/executor_test.py`
- `tests/wat_generator_test.py`
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

- Les affectations simples définissent maintenant les variables pendant l'analyse sémantique.
- Le REPL prend en charge `:wat` / `:wasm` et `:rust` / `:wasmtime`.
- `WATCodeGenerator` est le backend WASM principal ; le générateur Rust intermédiaire est hérité de l'ancien flux.
- Si vous ajoutez un concept de mot-clé, mettez aussi à jour `tests/keyword_registry_test.py`.
