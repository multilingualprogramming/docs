---
layout: page
title: "Codegen API Reference"
description: "Complete API reference for PythonCodeGenerator, WasmGenerator, RuntimeBuiltins, and the full compilation pipeline."
category: "Code Generation"
permalink: /codegen/api/
prev_page:
  title: "Python Code Generation"
  url: /codegen/
---

This page is the complete API reference for the multilingual code generation subsystem.

---

## Imports

```python
from multilingualprogramming import (
    Lexer,
    Parser,
    SemanticAnalyzer,
    ASTPrinter,
    PythonCodeGenerator,
    ProgramExecutor,
    REPL,
)

from multilingualprogramming.codegen import (
    PythonCodeGenerator,
    WasmGenerator,
    RuntimeBuiltins,
)

from multilingualprogramming.core.lowering import lower_to_core_ir
from multilingualprogramming.runtime.backend_selector import (
    BackendSelector,
    Backend,
    BackendConfig,
    BackendRegistry,
)
from multilingualprogramming.runtime.python_fallbacks import FALLBACK_REGISTRY
```

---

## ProgramExecutor

High-level API for executing or transpiling multilingual programs.

```python
class ProgramExecutor:
    def __init__(self)
```

### Methods

#### `execute(source, language="en", **kwargs) -> None`

Execute a multilingual program end-to-end:

1. Lex → tokenize source
2. Parse → build AST
3. Semantic analysis → validate
4. Code generation → emit Python
5. Execute Python in runtime namespace

```python
from multilingualprogramming import ProgramExecutor

executor = ProgramExecutor()

executor.execute("""
let nums = [1, 2, 3, 4, 5]
let total = sum(nums)
print(f"Total: {total}")
""", language="en")
# Prints: Total: 15
```

#### `transpile(source, language="en") -> str`

Return generated Python source without executing:

```python
python_code = executor.transpile("""
let x = 42
print(x)
""", language="en")

print(python_code)
# x = 42
# print(x)
```

#### Multi-Language Transpilation

All languages produce identical Python output:

```python
# English
executor.transpile("let x = 42\nprint(x)", language="en")
# → "x = 42\nprint(x)"

# French
executor.transpile("soit x = 42\nafficher(x)", language="fr")
# → "x = 42\nprint(x)"

# Japanese
executor.transpile("変数 x = 42\n表示(x)", language="ja")
# → "x = 42\nprint(x)"

# Arabic
executor.transpile("متغير x = 42\nاطبع(x)", language="ar")
# → "x = 42\nprint(x)"

# Chinese
executor.transpile("变量 x = 42\n打印(x)", language="zh")
# → "x = 42\nprint(x)"
```

---

## Lexer

Tokenizes multilingual source code.

```python
class Lexer:
    def __init__(self, language: str = "en")
```

### Methods

#### `tokenize(source: str) -> list[Token]`

```python
from multilingualprogramming import Lexer

lexer = Lexer(language="fr")
tokens = lexer.tokenize("soit x = 42\nafficher(x)")

for tok in tokens:
    print(tok)
# Token(type=KEYWORD, value='soit', ...)
# Token(type=IDENT, value='x', ...)
# Token(type=OP, value='=', ...)
# Token(type=INT, value=42, ...)
# ...
```

---

## Parser

Builds the Abstract Syntax Tree from tokens.

```python
class Parser:
    def __init__(self, language: str = "en")
```

### Methods

#### `parse(tokens) -> ASTNode`

```python
from multilingualprogramming import Parser

parser = Parser(language="fr")
ast = parser.parse(tokens)
```

---

## SemanticAnalyzer

Performs scope analysis, type checking, and semantic validation.

```python
class SemanticAnalyzer:
    def __init__(self, language: str = "en")
```

### Methods

#### `analyze(ast: ASTNode) -> None`

Raises `SemanticError` with localized messages if the AST is invalid.

```python
from multilingualprogramming import SemanticAnalyzer

analyzer = SemanticAnalyzer(language="fr")
analyzer.analyze(core.ast)
```

---

## ASTPrinter

Pretty-prints the AST for debugging.

```python
class ASTPrinter:
    def __init__(self)
```

### Methods

#### `print(ast: ASTNode) -> str`

```python
from multilingualprogramming import ASTPrinter

printer = ASTPrinter()
print(printer.print(ast))
```

---

## PythonCodeGenerator

Emits Python source code from a validated Core IR AST.

```python
class PythonCodeGenerator:
    def __init__(
        self,
        indent_spaces: int = 4,
        emit_type_annotations: bool = True,
        normalize_whitespace: bool = True,
    )
```

### Constructor Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `indent_spaces` | `int` | `4` | Number of spaces per indentation level |
| `emit_type_annotations` | `bool` | `True` | Preserve type annotations in output |
| `normalize_whitespace` | `bool` | `True` | Normalize spacing around operators |

### Methods

#### `generate(ast: ASTNode) -> str`

Generate Python source code from the given AST.

```python
from multilingualprogramming.codegen import PythonCodeGenerator

codegen = PythonCodeGenerator(indent_spaces=4)
python_source = codegen.generate(ast)
print(python_source)
```

### Full Pipeline Example

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

# Step 1: Lex
lexer = Lexer(language=language)
tokens = lexer.tokenize(source)

# Step 2: Parse
parser = Parser(language=language)
ast = parser.parse(tokens)

# Step 3: Lower to Core IR
core = lower_to_core_ir(ast, source_language=language)

# Step 4: Semantic analysis
analyzer = SemanticAnalyzer(language=language)
analyzer.analyze(core.ast)

# Step 5: Generate Python
codegen = PythonCodeGenerator()
python_code = codegen.generate(core.ast)

print(python_code)
# nums = [1, 2, 3]
# total = sum(n ** 2 for n in nums)
# print(f"Sum of squares: {total}")
```

---

## Core IR and Lowering

### `lower_to_core_ir(ast, source_language) -> CoreIRProgram`

Converts a surface AST to the language-neutral Core IR.

```python
from multilingualprogramming.core.lowering import lower_to_core_ir

core = lower_to_core_ir(ast, source_language="fr")
print(core.source_language)   # "fr"
print(core.core_version)      # "1.0"
print(core.ast)               # CoreAST root node
```

### `CoreIRProgram`

```python
@dataclass
class CoreIRProgram:
    ast: ASTNode          # the shared Core AST
    source_language: str  # original language code ("fr", "ja", etc.)
    core_version: str     # semantic version of this core format
    metadata: dict        # optional extra metadata
```

---

## RuntimeBuiltins

Provides the runtime namespace that includes Python built-ins plus all localized aliases.

```python
class RuntimeBuiltins:
    @staticmethod
    def for_language(language: str) -> dict
```

### `for_language(language) -> dict`

Returns a namespace dictionary suitable for `exec()` that includes:
- All Python built-in functions (universal names always available)
- Localized aliases for the specified language

```python
from multilingualprogramming.codegen import RuntimeBuiltins

# French namespace
fr_builtins = RuntimeBuiltins.for_language("fr")

# Universal names always present
print("print" in fr_builtins)     # True
print("range" in fr_builtins)     # True

# Localized aliases added
print("afficher" in fr_builtins)  # True  (print)
print("intervalle" in fr_builtins) # True  (range)
print("longueur" in fr_builtins)  # True  (len)

# Other language's aliases NOT present
print("imprimir" in fr_builtins)  # False (Spanish)

# Full alias list
aliases = {k: v.__name__ for k, v in fr_builtins.items()
           if k not in dir(__builtins__)}
print(aliases)
```

### Executing Code with RuntimeBuiltins

```python
from multilingualprogramming.codegen import RuntimeBuiltins, PythonCodeGenerator
from multilingualprogramming import Lexer, Parser, SemanticAnalyzer
from multilingualprogramming.core.lowering import lower_to_core_ir

source = "afficher(intervalle(5))"
language = "fr"

# Build pipeline
lexer = Lexer(language=language)
parser = Parser(language=language)
analyzer = SemanticAnalyzer(language=language)
codegen = PythonCodeGenerator()

tokens = lexer.tokenize(source)
ast = parser.parse(tokens)
core = lower_to_core_ir(ast, source_language=language)
analyzer.analyze(core.ast)
python_code = codegen.generate(core.ast)

# Execute with runtime builtins
namespace = RuntimeBuiltins.for_language(language)
exec(python_code, namespace)
# Prints: range(0, 5)
```

---

## WasmGenerator

Generates WebAssembly bytecode from a Core IR AST (requires the WASM optional dependency).

```python
class WasmGenerator:
    def __init__(self)
```

### Methods

#### `generate_wasm(ast, function_name: str) -> bytes`

Compile a function from the AST to WASM bytecode:

```python
from multilingualprogramming.codegen import WasmGenerator

wasm_gen = WasmGenerator()
wasm_bytes = wasm_gen.generate_wasm(ast, function_name="fibonacci")

# Write to file
with open("fibonacci.wasm", "wb") as f:
    f.write(wasm_bytes)
```

#### `generate_rust(ast, function_name: str) -> str`

Get the Rust intermediate representation (before WASM compilation):

```python
rust_code = wasm_gen.generate_rust(ast, function_name="fibonacci")
print(rust_code)
```

See [WASM Architecture](/wasm/architecture/) for details on the compilation chain.

---

## BackendSelector

Runtime-level selector that dispatches function calls to either the WASM or Python backend.

```python
class BackendSelector:
    def __init__(
        self,
        prefer_backend: Backend = None,
        config: BackendConfig = None,
    )
```

### `Backend` Enum

```python
from multilingualprogramming.runtime.backend_selector import Backend

Backend.WASM    # Use WebAssembly backend
Backend.PYTHON  # Use Python fallback
Backend.AUTO    # Auto-select (WASM if available, else Python)
```

### Methods

#### `is_wasm_available() -> bool`

```python
from multilingualprogramming.runtime.backend_selector import BackendSelector

sel = BackendSelector()
print(sel.is_wasm_available())   # True / False
```

#### `call_function(name: str, *args) -> Any`

Call a named function using the selected backend:

```python
result = sel.call_function("fibonacci", 30)
print(result)  # 832040
```

#### `backend` property

```python
print(sel.backend)   # "wasm" or "python"
```

### BackendConfig

```python
from multilingualprogramming.runtime.backend_selector import BackendConfig

config = BackendConfig(
    memory_pages=1024,    # WASM linear memory in 64KB pages (default: 1024 = 64MB)
    timeout_ms=5000,      # Max execution time in milliseconds
)
sel = BackendSelector(config=config)
```

### Explicit Backend Selection

```python
from multilingualprogramming.runtime.backend_selector import BackendSelector, Backend

# Force Python fallback
sel_py = BackendSelector(prefer_backend=Backend.PYTHON)

# Force WASM (raises if unavailable)
sel_wasm = BackendSelector(prefer_backend=Backend.WASM)

# Auto (default behavior)
sel_auto = BackendSelector()
```

---

## FALLBACK_REGISTRY

The Python fallback registry maps function names to their Python implementations.

```python
from multilingualprogramming.runtime.python_fallbacks import FALLBACK_REGISTRY

# List all registered functions
print(f"Registered: {len(FALLBACK_REGISTRY)} functions")
print(sorted(FALLBACK_REGISTRY.keys()))

# Check if a function is registered
print("fibonacci" in FALLBACK_REGISTRY)   # True / False

# Get the Python implementation
fn = FALLBACK_REGISTRY.get("fibonacci")
import inspect
print(inspect.signature(fn))
```

---

## REPL

Interactive REPL for multilingual programs.

```python
class REPL:
    def __init__(self, language: str = "en", show_python: bool = False)
```

### Constructor Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `language` | `str` | `"en"` | Starting language |
| `show_python` | `bool` | `False` | Show generated Python after each input |

### Methods

#### `run() -> None`

Start the interactive REPL loop. Exit with `:q` or Ctrl+D.

```python
from multilingualprogramming import REPL

repl = REPL(language="fr", show_python=True)
repl.run()
```

### REPL Commands

| Command | Description |
|---------|-------------|
| `:help` | Show help |
| `:language <code>` | Switch language (e.g. `:language ja`) |
| `:python` | Toggle Python preview mode |
| `:reset` | Clear variable state |
| `:kw [XX]` | Show keywords for current or specified language |
| `:ops [XX]` | Show operators for current or specified language |
| `:q` | Quit |

### CLI Launch

```bash
# Default language (English)
python -m multilingualprogramming repl

# Start in French
python -m multilingualprogramming repl --lang fr

# Show generated Python
python -m multilingualprogramming repl --show-python

# Both flags
python -m multilingualprogramming repl --lang ja --show-python
```

---

## KeywordRegistry

Look up keywords and concept mappings programmatically.

```python
from multilingualprogramming import KeywordRegistry

registry = KeywordRegistry()

# Get keyword for a concept in a language
keyword = registry.get_keyword("COND_IF", "fr")
print(keyword)   # "si"

# Reverse: concept from keyword
concept = registry.get_concept("si", "fr")
print(concept)   # "COND_IF"

# All supported languages
languages = registry.supported_languages()
print(languages)   # ["en", "fr", "es", "de", ...]

# All keywords for a language
keywords = registry.keywords_for_language("ja")
print(keywords)    # {"COND_IF": "もし", "LOOP_FOR": "毎", ...}
```

---

## Error Handling

```python
from multilingualprogramming.errors import (
    MultilingualSyntaxError,
    MultilingualSemanticError,
    MultilingualRuntimeError,
)

try:
    executor.execute(source, language="fr")
except MultilingualSyntaxError as e:
    print(f"Syntax error (line {e.lineno}): {e.message}")
except MultilingualSemanticError as e:
    print(f"Semantic error: {e.message}")
except MultilingualRuntimeError as e:
    print(f"Runtime error: {e.message}")
```

Error messages are localized to the source language — French programs show errors in French, Japanese programs show errors in Japanese.

---

## Complete Reference Example

End-to-end: French source → Python code → execute with builtins:

```python
from multilingualprogramming import (
    Lexer, Parser, SemanticAnalyzer,
    PythonCodeGenerator, ProgramExecutor
)
from multilingualprogramming.codegen import RuntimeBuiltins
from multilingualprogramming.core.lowering import lower_to_core_ir

FRENCH_SOURCE = """
from math import sqrt

fonction hypotenuse(a, b):
    retourner sqrt(a**2 + b**2)

pour n dans intervalle(1, 6):
    afficher(f"hypoténuse({n}, {n+1}) = {hypotenuse(n, n+1):.4f}")
"""

# Method 1: High-level
executor = ProgramExecutor()
executor.execute(FRENCH_SOURCE, language="fr")

# Method 2: Inspect generated Python
python_code = executor.transpile(FRENCH_SOURCE, language="fr")
print(python_code)
# from math import sqrt
#
# def hypotenuse(a, b):
#     return sqrt(a ** 2 + b ** 2)
#
# for n in range(1, 6):
#     print(f"hypoténuse({n}, {n+1}) = {hypotenuse(n, n+1):.4f}")
```
