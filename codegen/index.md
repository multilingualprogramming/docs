---
layout: page
title: "Python Code Generation"
description: "How multilingual generates Python code from the Core AST, and how to use the codegen API."
category: "Code Generation"
permalink: /codegen/
next_page:
  title: "API Reference"
  url: /codegen/api/
---

The Python code generator (`PythonCodeGenerator`) is the primary backend for multilingual. It takes a `CoreIRProgram` and emits executable Python source code.

---

## Pipeline Position

```
Source Language (.ml)
      │
      ▼  [Lexer + Parser + SurfaceNormalizer]
Core AST
      │
      ▼  [SemanticAnalyzer]
Validated CoreIRProgram
      │
      ▼  [PythonCodeGenerator]
Python Source Code (str)
      │
      ▼  [ProgramExecutor / exec()]
Runtime Output
```

---

## Quick Start

### Transpile to Python

```python
from multilingualprogramming import ProgramExecutor

executor = ProgramExecutor()

# Transpile without executing
python_code = executor.transpile("""
let items = [1, 2, 3, 4, 5]
let squares = [x**2 for x in items]
print(squares)
""", language="en")

print(python_code)
# Output:
# items = [1, 2, 3, 4, 5]
# squares = [x ** 2 for x in items]
# print(squares)
```

### Execute Directly

```python
executor.execute("""
let items = [1, 2, 3, 4, 5]
let squares = [x**2 for x in items]
print(squares)
""", language="en")
# Prints: [1, 4, 9, 16, 25]
```

### Multi-Language Examples

The same Python output is generated regardless of source language:

```python
# English source
executor.transpile("let x = 42\nprint(x)", language="en")
# → "x = 42\nprint(x)"

# French source — identical output
executor.transpile("soit x = 42\nafficher(x)", language="fr")
# → "x = 42\nprint(x)"

# Japanese source — identical output
executor.transpile("変数 x = 42\n表示(x)", language="ja")
# → "x = 42\nprint(x)"
```

---

## Code Generation Rules

### Variables

| multilingual | Generated Python |
|-------------|-----------------|
| `let x = 42` | `x = 42` |
| `let x: int = 42` | `x: int = 42` |
| `const PI = 3.14` | `PI = 3.14` |

### Functions

| multilingual | Generated Python |
|-------------|-----------------|
| `def f(x):` | `def f(x):` |
| `def f(x: int) -> str:` | `def f(x: int) -> str:` |
| `def f(a, /, *, b):` | `def f(a, /, *, b):` |
| `async def f(x):` | `async def f(x):` |

### Control Flow

| multilingual | Generated Python |
|-------------|-----------------|
| `if x > 0:` | `if x > 0:` |
| `elif x < 0:` | `elif x < 0:` |
| `else:` | `else:` |
| `for i in range(5):` | `for i in range(5):` |
| `while x > 0:` | `while x > 0:` |

### Classes

| multilingual | Generated Python |
|-------------|-----------------|
| `class Foo:` | `class Foo:` |
| `class Bar(Foo):` | `class Bar(Foo):` |

### Expressions

| multilingual | Generated Python |
|-------------|-----------------|
| `f"Hello {name}"` | `f"Hello {name}"` |
| `x if cond else y` | `x if cond else y` |
| `[x for x in items]` | `[x for x in items]` |
| `{k: v for k, v in d.items()}` | `{k: v for k, v in d.items()}` |
| `lambda x: x**2` | `lambda x: x**2` |
| `(x := 10)` | `(x := 10)` |

### Imports

Localized import keywords generate standard Python imports:

| multilingual (any language) | Generated Python |
|-----------------------------|-----------------|
| `import math` | `import math` |
| `from math import sqrt` | `from math import sqrt` |
| `from math import sqrt as root` | `from math import sqrt as root` |

### Built-in Aliases

Localized built-in names are resolved to their Python equivalents at code generation:

| multilingual (French) | Generated Python |
|----------------------|-----------------|
| `afficher(x)` | `print(x)` |
| `intervalle(10)` | `range(10)` |
| `longueur(lst)` | `len(lst)` |

---

## Using the Generator Directly

```python
from multilingualprogramming import (
    Lexer, Parser, SemanticAnalyzer,
    PythonCodeGenerator
)
from multilingualprogramming.core.lowering import lower_to_core_ir

source = """
let nums = [1, 2, 3]
let total = sum(n**2 for n in nums)
print(f"Sum of squares: {total}")
"""
language = "en"

# Pipeline
lexer = Lexer(language=language)
parser = Parser(language=language)
analyzer = SemanticAnalyzer(language=language)
codegen = PythonCodeGenerator()

tokens = lexer.tokenize(source)
ast = parser.parse(tokens)
core = lower_to_core_ir(ast, source_language=language)
analyzer.analyze(core.ast)
python_code = codegen.generate(core.ast)

print(python_code)
# Output:
# nums = [1, 2, 3]
# total = sum(n ** 2 for n in nums)
# print(f"Sum of squares: {total}")
```

---

## Runtime Builtins

The Python executor injects a runtime namespace with all multilingual builtins:

```python
from multilingualprogramming.codegen import RuntimeBuiltins

# Get namespace for a language
builtins = RuntimeBuiltins.for_language("fr")

# Contains:
# - All Python built-in functions
# - Localized aliases for all 41 concepts
# - e.g., "afficher" → print, "intervalle" → range, "longueur" → len
```

When the generated Python code is executed, it runs in a namespace that includes both the universal Python names and the localized aliases. This means both `print` and `afficher` work in a French program.

---

## Code Generation Configuration

```python
from multilingualprogramming.codegen import PythonCodeGenerator

# Default settings
codegen = PythonCodeGenerator(
    indent_spaces=4,          # indentation width
    emit_type_annotations=True,  # preserve type annotations in output
    normalize_whitespace=True,    # normalize spacing
)

python_src = codegen.generate(ast)
```

---

## WASM Code Generation

The WASM code generator follows the same interface:

```python
from multilingualprogramming.codegen import WasmGenerator

wasm_gen = WasmGenerator()
wasm_bytes = wasm_gen.generate_wasm(ast, function_name="my_func")

# Or: get the Rust intermediate code
rust_code = wasm_gen.generate_rust(ast, function_name="my_func")
```

See [WASM Architecture](/wasm/architecture/) for details.

---

## Example: Complete Transpilation

Full end-to-end transpile from Japanese to Python:

**Input** (Japanese, `program.ml`):

```python
取込 math

変数 数値 = [1, 2, 3, 4, 5]

関数 計算(リスト):
    変数 合計 = 0
    毎 n 中 リスト:
        合計 = 合計 + n * n
    戻る 合計

変数 結果 = 計算(数値)
表示(f"二乗和: {結果}")
```

**Generated Python:**

```python
import math

数値 = [1, 2, 3, 4, 5]

def 計算(リスト):
    合計 = 0
    for n in リスト:
        合計 = 合計 + n * n
    return 合計

結果 = 計算(数値)
print(f"二乗和: {結果}")
```

**Notes:**
- Keywords translated: `取込` → `import`, `変数` → variable declaration, `関数` → `def`, `毎/中` → `for/in`, `戻る` → `return`, `表示` → `print`
- Identifiers preserved: `数値`, `計算`, `リスト`, `合計`, `結果` (Japanese identifiers remain as-is)
- Output: `二乗和: 55`
