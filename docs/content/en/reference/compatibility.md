---
page_id: reference__compatibility
locale: en
title: Compatibility Matrix
path_segments:
- reference
- compatibility
source_hash: 5266b537e3e5
status: source
permalink: /en/docs/reference/compatibility/
---

This matrix defines the current compatibility baseline for `multilingual`. The source of truth is:

- `examples/complete_features_en.ml` and equivalents in all 17 languages
- `tests/` (1,926 collected tests across 63 test files)

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
| Bytes literals | ✅ | `b"..."`, `B"..."`, triple-quoted `b"""..."""` |
| Raw strings | ✅ | `r"..."`, `R"..."`, triple-quoted `r"""..."""` — no escape processing |
| Raw bytes | ✅ | `rb"..."`, `br"..."` and all case variants |
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
| Localized built-in aliases | ✅ 75 concepts | 75 builtins with aliases in all 16 non-English languages |
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

1,926 collected tests across 63 test files:

| Test area | Files | Description |
|-----------|-------|-------------|
| Numerals and dates | 8 | Multilingual numerals, Unicode, Roman, complex, fractions, datetime |
| Lexer | 2 | Tokenization and lexer behavior |
| Parser | 5 | Expressions, statements, compounds, multilingual, errors |
| Semantic analysis | 6 | Scopes, constants, control flow, definitions, multilingual errors, symbol table |
| Code generation | 4 | Expressions, statements, compounds, multilingual |
| Execution | 4 | Basic, multilingual, transpile, errors |
| Critical features | 8 | Triple-quoted strings, slices, parameters, tuples, comprehensions, decorators, f-strings |
| Language completeness and CLI | 8 | Augmented assignment, membership, ternary, assert, chained assignment, CLI, REPL |
| Advanced language features | 23 | Loop else, yield/raise from, set comprehensions, parameter separators, f-string formatting, match guards/OR/AS, global/nonlocal, builtins, exceptions, surface normalization, extended builtins, alias resolution, starred unpacking, integration, multilingual |
| WAT/WASM backend | 8 | WAT generation, manifest/build orchestration, OOP/inheritance and dispatch in WAT, string/lambda lowering, WASM execution, corpus projects (20) |
| Infrastructure | 10 | Keyword registry, AST nodes, AST printer, error messages, runtime builtins, REPL |

---

## Not Guaranteed

The following are **not** claimed as universally compatible:

- Arbitrary Python projects running unchanged
- Full behavioral parity with all CPython edge cases
- Full third-party package/runtime ecosystem compatibility
- Every advanced metaprogramming/introspection scenario
- WAT `@property` deleter protocol (`@property` getter/setter are lowered; deleter handling is not documented as complete)
- WAT `print` `file=` keyword argument (stdout is the only target in WAT)

---

## Known Fixes

| Version | Fix |
|---------|-----|
| v0.6.0 | **100% Python 3.12 core syntax**: bytes literals (`b"..."`), raw strings (`r"..."`), raw bytes (`rb"..."`) fully supported in lexer, parser, and both code generators |
| v0.6.0 | Localized aliases expanded from 41 → 75: `eval`, `exec`, `compile`, `globals`, `locals`, `vars`, `help`, `memoryview`, `breakpoint`, `aiter`, `anext`, `exit`, `quit`, `copyright`, `credits`, `license` added across all 16 non-English languages |
| v0.6.0 | WAT `@property` getter: `obj.attr` now emits a WAT function call to the getter instead of a raw `f64.load` |
| v0.6.0 | WAT `@staticmethod` / `@classmethod`: detected via decorator; call sites no longer push an implicit `self` |
| v0.6.0 | WAT `print` `sep=` / `end=`: custom separator and terminator interned in the data section and printed via `$print_str`; `sep=""` / `end=""` suppress output |
| v0.6.0 | WAT dynamic dispatch: type tag (class ID) stored 8 bytes before each stateful object; `$__dispatch_method` switch function generated for every overridden method; function parameters of unknown type now dispatch polymorphically at runtime |
| v0.5.1 | Documentation updates |
| v0.5.0 | WAT/WASM OOP object model: class lowering with linear-memory bump allocator, inheritance with C3 MRO, `super()` resolution, WAT execution tests |
| v0.5.0 | SemanticAnalyzer: plain assignments (`x = 5`) now correctly define the variable in scope |
| v0.5.0 | Augmented assignment (`x += 1`) now correctly reports `UNDEFINED_NAME` when the target variable has not been previously defined |

---

## Recommendation

When evaluating compatibility for a real codebase:

1. Start from this matrix
2. Run smoke tests: `multilingual smoke --all`
3. Run focused tests: `multilingual run yourprogram.ml --lang en`
4. Track gaps as concrete syntax/runtime items
