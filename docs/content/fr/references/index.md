---
page_id: reference
locale: fr
title: Reference technique
path_segments:
- references
source_hash: 7daaacafc108
status: translated
permalink: /fr/docs/references/
---



Voici la reference complete du package `multilingualprogramming`. Elle couvre les APIs publiques, les fonctionnalites du langage, les commandes CLI et la base de compatibilite Python.

---

## Vue d'ensemble du package

{{snippet:reference__py01}}

---

## ProgramExecutor

API principale de haut niveau pour executer des programmes multilingual.

{{snippet:reference__py02}}

**Exemples :**

{{snippet:reference__py03}}

---

## Composants du pipeline

### Lexer

{{snippet:reference__py04}}

Chaque `Token` contient :
- `type` — token type concept (e.g., `COND_IF`, `LOOP_FOR`, `IDENTIFIER`, `NUMBER`)
- `value` — raw string value from source
- `line` — line number (1-based)
- `column` — column number (1-based)

{{snippet:reference__py05}}

### Parser

{{snippet:reference__py06}}

Le noeud AST `Program` contient une liste de noeuds `Statement`. Voir `multilingualprogramming/parser/ast_nodes.py` pour la hierarchie complete.

{{snippet:reference__py07}}

### SemanticAnalyzer

{{snippet:reference__py08}}

### PythonCodeGenerator

{{snippet:reference__py09}}

**Exemple complet de pipeline :**

{{snippet:reference__py10}}

---

## KeywordRegistry

{{snippet:reference__py11}}

**IDs de concepts (51 au total, 7 categories) :**

| Category | Concepts |
|----------|---------|
| `control_flow` | `COND_IF`, `COND_ELIF`, `COND_ELSE`, `LOOP_FOR`, `IN`, `LOOP_WHILE`, `BREAK`, `CONTINUE`, `PASS` |
| `variable_declaration` | `LET`, `CONST`, `GLOBAL`, `NONLOCAL`, `DEL`, `ASSERT` |
| `function` | `FUNC_DEF`, `RETURN`, `LAMBDA`, `YIELD`, `YIELD_FROM`, `ASYNC`, `AWAIT` |
| `class` | `CLASS_DEF` |
| `operators` | `AND`, `OR`, `NOT`, `IS`, `IS_NOT`, `IN_OP`, `NOT_IN` |
| `exception_handling` | `TRY`, `EXCEPT`, `ELSE`, `FINALLY`, `RAISE`, `WITH`, `AS` |
| `special` | `IMPORT`, `FROM`, `MATCH`, `CASE` |

---

## Systeme de numeraux

### MPNumeral

{{snippet:reference__py12}}

### RomanNumeral

{{snippet:reference__py13}}

### UnicodeNumeral

{{snippet:reference__py14}}

### NumeralConverter

{{snippet:reference__py15}}

---

## Date et heure

{{snippet:reference__py16}}

---

## REPL

{{snippet:reference__py17}}

---

## Commandes CLI

```bash
# Executer un fichier programme
multilingual run <file.ml> --lang en
multilg run programme.ml --lang fr

# Demarrer le REPL
multilingual repl
multilingual repl --lang fr --show-python --show-wat

# Transpiler vers Python (affichage sans execution)
multilingual compile hello.ml --lang en

# Construire un bundle WASM
multilingual build-wasm-bundle hello.ml --lang en --out-dir ./dist

# Valider un pack de langue
multilingual smoke --lang fr
multilingual smoke --all

# Verifier l'encodage de la sortie generee
multilingual encoding-check-generated hello.ml --lang en

# Afficher la version
multilingual --version
```

---

## Base de compatibilite Python

**Sous-ensemble de fonctionnalites Python 3.12+ supporte :**

| Feature | Status |
|---------|--------|
| Variable declarations + type annotations | ✅ |
| Arithmetic, bitwise, comparison operators | ✅ |
| Augmented assignment (`+=`, `-=`, etc.) | ✅ |
| Chained assignment | ✅ |
| Starred unpacking | ✅ |
| Lists, dicts, sets, tuples | ✅ |
| F-strings with format specs (`:.2f`, `!r`, `!s`, `!a`) | ✅ |
| `if` / `elif` / `else` | ✅ |
| `while` / `for` loops with `else` | ✅ |
| `break` / `continue` / `pass` | ✅ |
| `match` / `case` with guards, OR, AS | ✅ |
| Ternary expressions | ✅ |
| Functions with all param types | ✅ |
| Positional-only (`/`) and keyword-only (`*`) params | ✅ |
| `*args` and `**kwargs` | ✅ |
| Decorators on functions and classes | ✅ |
| Lambda expressions | ✅ |
| `yield` / `yield from` | ✅ |
| `async def` / `await` / `async for` / `async with` | ✅ |
| Class definitions and inheritance | ✅ |
| `super()` | ✅ |
| `try` / `except` / `else` / `finally` | ✅ |
| `raise` / `raise ... from` | ✅ |
| `assert` | ✅ |
| `with` / multiple contexts | ✅ |
| List, dict, set comprehensions | ✅ |
| Generator expressions | ✅ |
| Nested comprehensions | ✅ |
| `global` / `nonlocal` | ✅ |
| `del` | ✅ |
| Walrus operator `:=` | ✅ |
| Slices | ✅ |
| `import` / `from ... import` / `as` / `*` | ✅ |
| Wildcard import | ✅ |
| 70+ built-in functions | ✅ |
| 45+ exception types | ✅ |
| Localized built-in aliases (41 concepts) | ✅ |
| Surface normalization (SOV/RTL languages) | ✅ |

**~1 797 tests sur 58 fichiers de tests** definissent la base de compatibilite.

---

## Historique des versions

| Version | Highlights |
|---------|-----------|
| `0.5.1` | Documentation updates |
| `0.5.0` | WAT/WASM OOP object model; class lowering with linear-memory bump allocator; inheritance with C3 MRO; `super()` resolution; WAT execution tests; SemanticAnalyzer plain-assignment fix |
| `0.4.0` | WAT/WASM code generation; browser playground; WASM backend with 25+ Python fallbacks; 20 corpus projects |
| `0.3.0` | Earlier milestone |
