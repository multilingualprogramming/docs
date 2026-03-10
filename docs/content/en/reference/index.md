---
page_id: reference
locale: en
title: Language Reference
path_segments:
- reference
source_hash: "130731172631"
status: source
permalink: /en/docs/reference/
---

This is the complete reference for the `multilingualprogramming` package. It covers all public APIs, language features, CLI commands, and the Python compatibility baseline.

---

## Package Overview

{{snippet:reference__py01}}

---

## ProgramExecutor

The main high-level API for executing multilingual programs.

{{snippet:reference__py02}}

**Examples:**

{{snippet:reference__py03}}

---

## Pipeline Components

### Lexer

{{snippet:reference__py04}}

Each `Token` has:
- `type` — token type concept (e.g., `COND_IF`, `LOOP_FOR`, `IDENTIFIER`, `NUMBER`)
- `value` — raw string value from source
- `line` — line number (1-based)
- `column` — column number (1-based)

{{snippet:reference__py05}}

### Parser

{{snippet:reference__py06}}

The `Program` AST node contains a list of `Statement` nodes. See `multilingualprogramming/parser/ast_nodes.py` for the full node hierarchy.

{{snippet:reference__py07}}

### SemanticAnalyzer

{{snippet:reference__py08}}

### PythonCodeGenerator

{{snippet:reference__py09}}

**Full pipeline example:**

{{snippet:reference__py10}}

---

## KeywordRegistry

{{snippet:reference__py11}}

**Concept IDs (51 total, 7 categories):**

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

## Numeral System

### MPNumeral

{{snippet:reference__py12}}

### RomanNumeral

{{snippet:reference__py13}}

### UnicodeNumeral

{{snippet:reference__py14}}

### NumeralConverter

{{snippet:reference__py15}}

---

## Date and Time

{{snippet:reference__py16}}

---

## REPL

{{snippet:reference__py17}}

---

## CLI Commands

```bash
# Run a program file
multilingual run <file.ml> --lang en
multilg run programme.ml --lang fr

# Start REPL
multilingual repl
multilingual repl --lang fr --show-python --show-wat

# Transpile to Python (print output, no execution)
multilingual compile hello.ml --lang en

# Build WASM bundle
multilingual build-wasm-bundle hello.ml --lang en --out-dir ./dist

# Validate a language pack
multilingual smoke --lang fr
multilingual smoke --all

# Check generated output encoding
multilingual encoding-check-generated hello.ml --lang en

# Show version
multilingual --version
```

---

## Python Compatibility Baseline

**Supported Python 3.12+ feature subset:**

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
| Localized built-in aliases (75 concepts) | ✅ |
| Surface normalization (SOV/RTL languages) | ✅ |

**1,926 collected tests across 63 test files** provide the compatibility baseline.

---

## Version History

| Version | Highlights |
|---------|-----------|
| `0.6.0` | WAT/WASM stateful object model, dynamic dispatch, `@property` accessors, `with`/`try`/`match` lowering, bytes literals in WAT, expanded localized builtin aliases |
| `0.5.1` | Documentation updates |
| `0.5.0` | WAT/WASM OOP object model; class lowering with linear-memory bump allocator; inheritance with C3 MRO; `super()` resolution; WAT execution tests; SemanticAnalyzer plain-assignment fix |
| `0.4.0` | WAT/WASM code generation; browser playground; WASM backend with 25+ Python fallbacks; 20 corpus projects |
| `0.3.0` | Earlier milestone |
