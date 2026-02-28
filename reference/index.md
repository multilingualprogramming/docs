---
layout: page
title: "Language Reference"
description: "Complete API and language reference for multilingualprogramming."
category: "Reference"
permalink: /reference/
next_page:
  title: "Built-in Aliases"
  url: /reference/builtins/
badges:
  - text: "v0.4.0"
    type: default
  - text: "Python 3.12+"
    type: success
---

This is the complete reference for the `multilingualprogramming` package. It covers all public APIs, language features, CLI commands, and the Python compatibility baseline.

---

## Package Overview

```python
from multilingualprogramming import (
    # Execution
    ProgramExecutor,
    REPL,

    # Pipeline components
    Lexer,
    Parser,
    SemanticAnalyzer,
    ASTPrinter,
    PythonCodeGenerator,

    # Keyword registry
    KeywordRegistry,
    KeywordValidator,

    # Numerals
    MPNumeral,
    UnicodeNumeral,
    RomanNumeral,
    ComplexNumeral,
    FractionNumeral,
    NumeralConverter,

    # Date/time
    MPDate,
    MPTime,
    MPDatetime,
)
```

---

## ProgramExecutor

The main high-level API for executing multilingual programs.

```python
from multilingualprogramming import ProgramExecutor

executor = ProgramExecutor()

# Execute source string
executor.execute(source: str, language: str = "en") -> None

# Execute a file
executor.execute_file(path: str, language: str = "en") -> None

# Transpile to Python (return Python source without executing)
python_src = executor.transpile(source: str, language: str = "en") -> str
```

**Examples:**

```python
executor = ProgramExecutor()

# Execute English program
executor.execute("""
let x = 10
let y = 20
print(f"Sum: {x + y}")
""", language="en")

# Execute French program
executor.execute("""
soit x = 10
soit y = 20
afficher(f"Somme: {x + y}")
""", language="fr")

# Execute Japanese program
executor.execute("""
変数 x = 10
変数 y = 20
表示(f"合計: {x + y}")
""", language="ja")

# Transpile to Python
python_code = executor.transpile("""
let items = [1, 2, 3]
for i in items:
    print(i)
""", language="en")
print(python_code)
# items = [1, 2, 3]
# for i in items:
#     print(i)
```

---

## Pipeline Components

### Lexer

```python
from multilingualprogramming import Lexer

lexer = Lexer(language="en")
tokens = lexer.tokenize(source: str) -> list[Token]
```

Each `Token` has:
- `type` — token type concept (e.g., `COND_IF`, `LOOP_FOR`, `IDENTIFIER`, `NUMBER`)
- `value` — raw string value from source
- `line` — line number (1-based)
- `column` — column number (1-based)

```python
lexer = Lexer(language="fr")
tokens = lexer.tokenize("si x > 0:\n    afficher(x)")
for tok in tokens:
    print(f"{tok.type:20} {tok.value!r}")
```

### Parser

```python
from multilingualprogramming import Parser

parser = Parser(language="en")
ast = parser.parse(tokens: list[Token]) -> Program
```

The `Program` AST node contains a list of `Statement` nodes. See `multilingualprogramming/parser/ast_nodes.py` for the full node hierarchy.

```python
from multilingualprogramming import Lexer, Parser, ASTPrinter

lexer = Lexer(language="en")
parser = Parser(language="en")
printer = ASTPrinter()

tokens = lexer.tokenize("let x = 42\nprint(x)")
ast = parser.parse(tokens)
printer.print(ast)
```

### SemanticAnalyzer

```python
from multilingualprogramming import SemanticAnalyzer

analyzer = SemanticAnalyzer(language="en")
analyzer.analyze(ast: Program) -> None  # raises on errors
```

### PythonCodeGenerator

```python
from multilingualprogramming import PythonCodeGenerator

codegen = PythonCodeGenerator()
python_src = codegen.generate(ast: Program) -> str
```

**Full pipeline example:**

```python
from multilingualprogramming import (
    Lexer, Parser, SemanticAnalyzer,
    PythonCodeGenerator, ASTPrinter
)

source = """
let nums = [1, 2, 3, 4, 5]
let total = sum(n**2 for n in nums)
print(total)
"""
language = "en"

lexer = Lexer(language=language)
parser = Parser(language=language)
analyzer = SemanticAnalyzer(language=language)
codegen = PythonCodeGenerator()

tokens = lexer.tokenize(source)
ast = parser.parse(tokens)
analyzer.analyze(ast)
python_code = codegen.generate(ast)
print(python_code)
```

---

## KeywordRegistry

```python
from multilingualprogramming import KeywordRegistry

registry = KeywordRegistry()

# Forward lookup: concept → language keyword
keyword = registry.get_keyword(concept: str, language: str) -> str
# e.g., registry.get_keyword("COND_IF", "fr") → "si"

# Reverse lookup: language keyword → concept
concept = registry.get_concept(keyword: str, language: str) -> str
# e.g., registry.get_concept("si", "fr") → "COND_IF"

# All supported languages
langs = registry.get_supported_languages() -> list[str]
# ["en", "fr", "es", "de", "it", "pt", "pl", "nl", "sv", "da", "fi", "hi", "ar", "bn", "ta", "zh", "ja"]

# All keywords for a language
mapping = registry.get_all_keywords(language: str) -> dict[str, str]

# All concepts
concepts = registry.get_all_concepts() -> list[str]
```

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

```python
from multilingualprogramming import MPNumeral

# Create from various forms
n1 = MPNumeral(42)
n2 = MPNumeral("٤٢")       # Arabic-Indic digits
n3 = MPNumeral("四十二")    # CJK numerals

# Arithmetic
result = n1 + n2             # returns MPNumeral
result = n1 * MPNumeral(3)

# Conversion
print(n1.to_int())           # 42
print(n1.to_arabic_indic())  # ٤٢
print(n1.to_devanagari())    # ४२
print(n1.to_cjk())           # 四十二
```

### RomanNumeral

```python
from multilingualprogramming import RomanNumeral

r = RomanNumeral("XIV")
print(r.to_int())    # 14
print(int(r))        # 14

r2 = RomanNumeral(42)
print(str(r2))       # XLII
```

### UnicodeNumeral

```python
from multilingualprogramming import UnicodeNumeral

u = UnicodeNumeral("٣٧")     # Arabic-Indic
print(u.to_int())             # 37

u2 = UnicodeNumeral("३७")    # Devanagari
print(u2.to_int())            # 37
```

### NumeralConverter

```python
from multilingualprogramming import NumeralConverter

conv = NumeralConverter()
print(conv.to_arabic_indic(42))    # ٤٢
print(conv.to_devanagari(42))      # ४२
print(conv.to_bengali(42))         # ৪২
print(conv.to_cjk(42))             # 四十二
print(conv.to_roman(42))           # XLII
```

---

## Date and Time

```python
from multilingualprogramming import MPDate, MPTime, MPDatetime

# Parse multilingual date strings
d = MPDate.parse("15 janvier 2024", language="fr")
print(d.year, d.month, d.day)    # 2024 1 15

d2 = MPDate.parse("15 يناير 2024", language="ar")

# Format for a language
print(d.format(language="fr"))   # 15 janvier 2024
print(d.format(language="de"))   # 15. Januar 2024

# MPTime
t = MPTime(14, 30, 0)
print(t.format(language="fr"))   # 14:30:00

# MPDatetime
dt = MPDatetime.now()
print(dt.format(language="ja"))  # 2024年1月15日 14:30:00
```

---

## REPL

```python
from multilingualprogramming import REPL

repl = REPL(language="en", show_python=False)
repl.run()   # starts interactive REPL

# Programmatic REPL (non-interactive)
repl = REPL(language="fr")
output = repl.eval_line("soit x = 42")
output = repl.eval_line("afficher(x)")
```

---

## CLI Commands

```bash
# Run a program file
python -m multilingualprogramming run <file.ml> --lang <code>
multilingual run <file.ml> --lang en
multilg run programme.ml --lang fr

# Start REPL
python -m multilingualprogramming repl
python -m multilingualprogramming repl --lang fr
python -m multilingualprogramming repl --show-python

# Validate a language pack
python -m multilingualprogramming smoke --lang fr
python -m multilingualprogramming smoke --all

# Show version
python -m multilingualprogramming --version
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
| Localized built-in aliases (41 concepts) | ✅ |
| Surface normalization (SOV/RTL languages) | ✅ |

**858 tests across 78 test suites** provide the compatibility baseline.
