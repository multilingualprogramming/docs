---
layout: page
title: "Compatibility Matrix"
description: "Python 3.12 compatibility baseline for multilingual — 858 tests, 78 suites, 17 languages."
category: "Reference"
permalink: /reference/compatibility/
prev_page:
  title: "Reference"
  url: /reference/
---

This matrix defines the current compatibility baseline for `multilingual`. The source of truth is:

- `examples/complete_features_en.ml` and equivalents in all 17 languages
- `tests/` (858 tests across 78 test suites)

**Target runtime**: CPython 3.12.x

---

## Scope Statement

`multilingual` supports a broad Python 3.12-aligned syntax and runtime subset. It is **not** full drop-in compatibility for every existing Python project or third-party ecosystem. It is a forward-compilation framework: surface language → Core AST → Python.

---

## Supported Languages

17 natural languages with localized keywords and error messages:

| Language | Code | `if` keyword |
|----------|------|-------------|
| English | `en` | `if` |
| French | `fr` | `si` |
| Spanish | `es` | `si` |
| German | `de` | `wenn` |
| Italian | `it` | `se` |
| Portuguese | `pt` | `se` |
| Polish | `pl` | `jezeli` |
| Dutch | `nl` | `als` |
| Swedish | `sv` | `om` |
| Danish | `da` | `hvis` |
| Finnish | `fi` | `jos` |
| Hindi | `hi` | `अगर` |
| Arabic | `ar` | `إذا` |
| Bengali | `bn` | `যদি` |
| Tamil | `ta` | `என்றால்` |
| Chinese | `zh` | `如果` |
| Japanese | `ja` | `もし` |

---

## Core Constructs

| Area | Status | Notes |
|------|--------|-------|
| Imports | ✅ | `import math`, `from math import sqrt as root_fn` |
| Wildcard imports | ✅ | `from os import *` |
| Variable declarations | ✅ | `let x = 0`, `const PI = 3.14` |
| Type annotations | ✅ | `let x: int = 0`, `def f(x: int) -> str:` |
| Arithmetic and expressions | ✅ | `+`, `-`, `*`, `/`, `//`, `%`, `**`, bitwise ops |
| Augmented assignment | ✅ | `+=`, `-=`, `*=`, `/=`, `**=`, `//=`, `%=`, `&=`, `\|=`, `^=`, `<<=`, `>>=` |
| Chained assignment | ✅ | `a = b = c = 0` |
| Starred unpacking | ✅ | `a, *rest = [1, 2, 3]`, `first, *mid, last = items` |

---

## Data Structures

| Area | Status | Notes |
|------|--------|-------|
| Lists | ✅ | literals, iteration, indexing, slicing |
| Dictionaries | ✅ | literals, comprehensions, unpacking (`**d`) |
| Sets | ✅ | literals, comprehensions |
| Tuples | ✅ | literals, unpacking |
| Strings | ✅ | single/double/triple quotes, f-strings |
| F-string format specs | ✅ | `f"{x:.2f}"`, `f"{x!r}"`, `f"{x!s}"`, `f"{x!a}"` |
| Hex/octal/binary literals | ✅ | `0xFF`, `0o77`, `0b1010` |
| Scientific notation | ✅ | `1.5e10` |

---

## Control Flow

| Area | Status | Notes |
|------|--------|-------|
| `if` / `elif` / `else` | ✅ | full conditional chains |
| `while` loops | ✅ | `while condition:` |
| `while` / `else` | ✅ | else block when loop completes without `break` |
| `for` loops | ✅ | `for item in items:`, tuple unpacking targets |
| `for` / `else` | ✅ | else block when loop completes without `break` |
| `break` / `continue` | ✅ | loop control |
| `pass` | ✅ | no-op placeholder |
| `match` / `case` | ✅ | structural pattern matching |
| `case` guard clauses | ✅ | `case n if n > 0:` |
| `case` OR patterns | ✅ | `case 1 \| 2 \| 3:` |
| `case` AS bindings | ✅ | `case pattern as name:` |
| `case _` (default) | ✅ | wildcard/default case |
| Ternary expressions | ✅ | `x if cond else y` |

---

## Functions and Classes

| Area | Status | Notes |
|------|--------|-------|
| Function definitions | ✅ | `def f(x):`, with defaults, `*args`, `**kwargs` |
| Positional-only params | ✅ | `def f(a, b, /, c):` |
| Keyword-only params | ✅ | `def f(a, *, b):` |
| Return annotations | ✅ | `def f() -> int:` |
| Decorators | ✅ | `@decorator` on functions and classes |
| Lambda expressions | ✅ | `lambda x: x + 1` |
| `yield` / `yield from` | ✅ | generator functions and delegation |
| `async def` / `await` | ✅ | async functions, `async for`, `async with` |
| Class definitions | ✅ | inheritance, methods, attributes |
| Walrus operator | ✅ | `(x := expr)` |

---

## Error Handling

| Area | Status | Notes |
|------|--------|-------|
| `try` / `except` / `else` / `finally` | ✅ | full exception handling |
| `raise` | ✅ | bare `raise`, `raise ValueError("msg")` |
| `raise` ... `from` | ✅ | exception chaining: `raise X from Y` |
| `assert` | ✅ | `assert expr`, `assert expr, msg` |

---

## Scope and Variables

| Area | Status | Notes |
|------|--------|-------|
| `global` | ✅ | declares global scope |
| `nonlocal` | ✅ | declares enclosing scope |
| `del` | ✅ | `del variable` |

---

## Comprehensions and Generators

| Area | Status | Notes |
|------|--------|-------|
| List comprehensions | ✅ | `[x for x in items if cond]`, nested |
| Dict comprehensions | ✅ | `{k: v for k, v in items}` |
| Set comprehensions | ✅ | `{x for x in items if cond}`, nested |
| Generator expressions | ✅ | `(x for x in items)` |

---

## Context Managers

| Area | Status | Notes |
|------|--------|-------|
| `with` statement | ✅ | `with open(f) as h:` |
| Multiple contexts | ✅ | `with A() as a, B() as b:` |
| `async with` | ✅ | async context managers |

---

## Built-in Coverage

| Coverage area | Status | Notes |
|---------------|--------|-------|
| Python keywords (3.12) | ✅ Complete | 51 concept IDs, 7 categories |
| Universal built-in functions | ✅ 70+ available | `len`, `range`, `abs`, `pow`, `divmod`, `complex`, `format`, `ascii`, `compile`, `eval`, `exec`, `globals`, `locals`, `issubclass`, `delattr`, `slice`, `aiter`, `anext`, and more |
| Exception types | ✅ 45+ | `BaseException`, `ValueError`, `TypeError`, `KeyError`, `ModuleNotFoundError`, `ExceptionGroup`, `BaseExceptionGroup`, all warnings, and more |
| Special values | ✅ | `True`, `False`, `None`, `Ellipsis`, `NotImplemented` |
| Localized built-in aliases | ✅ 41 concepts | 41 builtins with aliases in all 16 non-English languages |
| Canonical Python built-in names | ✅ | Always usable in all languages |

---

## Surface Syntax Normalization

SOV and RTL languages can use natural word order. The surface normalizer rewrites tokens to canonical order before parsing.

| Statement | Languages with normalization | Example |
|-----------|------------------------------|---------|
| `for` loop | `ja`, `ar`, `es`, `pt`, `hi`, `bn`, `ta` | Iterable-first: `範囲(6) 内の 各 i に対して:` |
| `while` loop | `ja`, `ar`, `hi`, `bn`, `ta` | Condition-first |
| `if` statement | `ja`, `ar`, `hi`, `bn`, `ta` | Condition-first |
| `with` statement | `ja`, `ar`, `hi`, `bn`, `ta` | Expression-first |

---

## Test Coverage

858 tests across 78 test suites:

| Test area | Suites | Description |
|-----------|--------|-------------|
| Numerals and dates | 8 | Multilingual numerals, Unicode, Roman, complex, fractions, datetime |
| Lexer | 2 | Tokenization and lexer behavior |
| Parser | 5 | Expressions, statements, compounds, multilingual, errors |
| Semantic analysis | 6 | Scopes, constants, control flow, definitions, multilingual errors, symbol table |
| Code generation | 4 | Expressions, statements, compounds, multilingual |
| Execution | 4 | Basic, multilingual, transpile, errors |
| Critical features | 8 | Triple-quoted strings, slices, parameters, tuples, comprehensions, decorators, f-strings |
| Language completeness and CLI | 8 | Augmented assignment, membership, ternary, assert, chained assignment, CLI, REPL |
| Advanced language features | 23 | Loop else, yield/raise from, set comprehensions, parameter separators, f-string formatting, match guards/OR/AS, global/nonlocal, builtins, exceptions, surface normalization, extended builtins, alias resolution, starred unpacking, integration, multilingual |
| Infrastructure | 10 | Keyword registry, AST nodes, AST printer, error messages, runtime builtins, REPL |

---

## Not Guaranteed

The following are **not** claimed as universally compatible:

- Arbitrary Python projects running unchanged
- Full behavioral parity with all CPython edge cases
- Full third-party package/runtime ecosystem compatibility
- Every advanced metaprogramming/introspection scenario
- Complete localization aliases for all CPython built-in functions (41 of 70+ have aliases)
- Starred unpacking in deeply nested expression contexts
- Complex decorator chains with arguments

---

## Recommendation

When evaluating compatibility for a real codebase:

1. Start from this matrix
2. Run smoke tests: `python -m multilingualprogramming smoke --all`
3. Run focused tests: `python -m multilingualprogramming run yourprogram.ml --lang en`
4. Track gaps as concrete syntax/runtime items
