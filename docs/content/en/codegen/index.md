---
page_id: codegen
locale: en
title: Python Code Generation
path_segments:
- codegen
source_hash: 5929fb8cc4b6
status: source
permalink: /en/docs/codegen/
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

{{snippet:codegen__py01}}

### Execute Directly

{{snippet:codegen__py02}}

### Multi-Language Examples

The same Python output is generated regardless of source language:

{{snippet:codegen__py03}}

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

{{snippet:codegen__py04}}

---

## Runtime Builtins

The Python executor injects a runtime namespace with all multilingual builtins:

{{snippet:codegen__py05}}

When the generated Python code is executed, it runs in a namespace that includes both the universal Python names and the localized aliases. This means both `print` and `afficher` work in a French program.

---

## Code Generation Configuration

{{snippet:codegen__py06}}

---

## WASM Code Generation

The primary WASM backend is `WATCodeGenerator`, which compiles the Core AST directly to WebAssembly Text Format (WAT). No Rust toolchain or external compiler is required.

{{snippet:codegen__py07}}

From the command line, `build-wasm-bundle` runs the full pipeline (WAT → binary → artifacts):

```bash
multilingual build-wasm-bundle program.ml --out-dir wasm-out
# Produces: module.wat, module.wasm, host_shim.js, abi_manifest.json
```

The generated WAT module exports `__main` and uses host-import callbacks (`env.print_str`, `env.print_f64`, etc.) for output — it does not return values.

See [WASM Architecture]({{ '/en/docs/wasm/architecture/' | relative_url }}) for the full pipeline and host import protocol.

---

## Example: Complete Transpilation

Full end-to-end transpile from Japanese to Python:

**Input** (Japanese, `program.ml`):

{{snippet:codegen__py08}}

**Generated Python:**

{{snippet:codegen__py09}}

**Notes:**
- Keywords translated: `取込` → `import`, `変数` → variable declaration, `関数` → `def`, `毎/中` → `for/in`, `戻る` → `return`, `表示` → `print`
- Identifiers preserved: `数値`, `計算`, `リスト`, `合計`, `結果` (Japanese identifiers remain as-is)
- Output: `二乗和: 55`
