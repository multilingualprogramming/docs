---
layout: page
title: "WASM Architecture"
description: "Architecture and design of the multilingual WASM infrastructure."
category: "WASM Backend"
permalink: /wasm/architecture/
prev_page:
  title: "WASM Installation"
  url: /wasm/installation/
next_page:
  title: "Performance Tuning"
  url: /wasm/performance/
---

The WASM infrastructure is designed around three principles: **transparent selection**, **graceful degradation**, and **zero user-code changes**.

---

## High-Level Architecture

```
┌─────────────────────────────────────────────────────────────┐
│              Multilingual Programming Language v0.4          │
└─────────────────────────────────────────────────────────────┘
                              │
                ┌─────────────┴──────────────┐
                │                            │
         ┌──────▼──────┐          ┌──────────▼────────┐
         │ User Code   │          │ Standard Library  │
         │ (.ml files) │          │ (17 languages)    │
         └──────┬──────┘          └──────────┬────────┘
                └─────────────┬──────────────┘
                              │
                         ┌────▼─────┐
                         │  Lexer   │
                         └────┬─────┘
                              │
                         ┌────▼─────┐
                         │  Parser  │
                         └────┬─────┘
                              │
                    ┌─────────▼──────────┐
                    │   Core AST         │
                    └─────────┬──────────┘
                              │
                ┌─────────────┴──────────────┐
                │                            │
         ┌──────▼──────────┐      ┌──────────▼────────┐
         │ Python Code     │      │   WASM Code       │
         │ Generator       │      │   Generator       │
         └──────┬──────────┘      └──────────┬────────┘
                │                            │
                │                    ┌───────▼────────┐
                │                    │ Rust Code      │
                │                    │ (Intermediate) │
                │                    └───────┬────────┘
                │                            │
                │                    ┌───────▼────────┐
                │                    │ Cranelift      │
                │                    │ Compiler       │
                │                    └───────┬────────┘
                │                            │
                │                    ┌───────▼────────┐
                │                    │ WASM Binary    │
                │                    │ (.wasm files)  │
                │                    └───────┬────────┘
                └─────────────┬──────────────┘
                              │
                    ┌─────────▼──────────┐
                    │ Backend Selector   │
                    │ Smart Auto-        │
                    │ Detection          │
                    └─────────┬──────────┘
                              │
                ┌─────────────┴──────────────┐
                │                            │
         ┌──────▼──────────┐      ┌──────────▼────────┐
         │ Python Executor │      │ WASM Loader       │
         │ (+ Fallbacks)   │      │ (+ Type Conv)     │
         └─────────────────┘      └──────────┬────────┘
                                             │
                              ┌──────────────┼──────────────┐
                              │              │              │
                         ┌────▼──┐    ┌─────▼──┐    ┌─────▼──┐
                         │Python │    │WASM   │    │Memory  │
                         │Fallbk │    │Exec   │    │Mgmt    │
                         │(25+   │    │Inst.  │    │(Linear)│
                         │funcs) │    │       │    │        │
                         └───────┘    └───────┘    └────────┘
```

---

## Component 1: WASM Code Generator

**File**: `multilingualprogramming/codegen/wasm_generator.py`

Transforms the Core AST into Rust intermediate code, which is then compiled to WASM by Cranelift.

**Responsibilities:**
- Transform AST → Rust intermediate code
- Generate memory management code
- Optimize for Cranelift backend
- Export function metadata

**Key features:**
- 200+ lines of Rust code generation
- Multi-function support
- 64MB memory allocation
- Panic handlers
- Metadata functions

**Output**: Rust source code → compiled `.wasm` binary

```python
from multilingualprogramming.codegen import WasmGenerator

generator = WasmGenerator()
wasm_bytes = generator.generate_wasm(ast, function_name="fibonacci")
```

---

## Component 2: WASM Bridge (Python ↔ WASM)

**File**: `multilingualprogramming/wasm/loader.py`

Handles loading WASM binaries, type conversion between Python and WASM, and module caching.

```python
from multilingualprogramming.wasm.loader import WasmModule, WasmModuleCache

class WasmModule:
    """Represents a loaded WASM module."""

    @staticmethod
    def load(module_path: str | Path) -> "WasmModule":
        """Load a WASM binary from disk."""
        ...

    def instantiate(self) -> bool:
        """Instantiate the module. Returns True on success."""
        ...

    def call(self, function_name: str, *args) -> Any:
        """Call a WASM function with Python arguments."""
        ...

    def has_function(self, function_name: str) -> bool:
        """Check if the module exports a given function."""
        ...


class WasmModuleCache:
    """Cache loaded modules to avoid repeated loading."""

    def get_or_load(self, module_path: str | Path) -> WasmModule | None:
        """Get from cache or load and cache a module."""
        ...
```

**Type conversion (Python → WASM):**

| Python type | WASM type | Notes |
|-------------|-----------|-------|
| `int` | `i32` / `i64` | Automatic width selection |
| `float` | `f32` / `f64` | Automatic precision selection |
| `list[int]` | linear memory | Serialized to WASM memory |
| `list[float]` | linear memory | Serialized to WASM memory |
| `str` | linear memory | UTF-8 encoded |
| `bool` | `i32` | 0 or 1 |

---

## Component 3: Backend Selector

**File**: `multilingualprogramming/runtime/backend_selector.py`

Intelligently selects between WASM and Python backends, with automatic fallback.

```python
from enum import Enum

class Backend(Enum):
    PYTHON = "python"
    WASM   = "wasm"
    AUTO   = "auto"    # default


class BackendSelector:
    """Intelligent backend selection with automatic fallback."""

    def __init__(self, prefer_backend: Backend = Backend.AUTO):
        self.prefer_backend = prefer_backend
        self.backend = self._detect_backend()

    def is_wasm_available(self) -> bool:
        """True if WASM can be loaded and used."""
        ...

    def call_function(self, function_name: str, *args) -> Any:
        """
        Call a function using the best available backend.
        Automatically falls back to Python if WASM fails.
        """
        ...

    def _detect_backend(self) -> Backend:
        """
        Detection order:
        1. Check if wasmtime installed
        2. Check if WASM binary exists
        3. Check platform compatibility
        4. Try loading WASM module
        5. Fall back to Python on any failure
        """
        ...


class BackendRegistry:
    """Register functions for different backends."""

    def register_python(self, func_name: str, func: Callable) -> None:
        """Register a Python implementation."""
        ...

    def register_wasm(self, func_name: str, wasm_path: str) -> None:
        """Register a WASM implementation."""
        ...
```

---

## Component 4: Python Fallbacks

**File**: `multilingualprogramming/runtime/python_fallbacks.py`

25+ pure Python implementations of WASM-accelerated functions. Used when WASM is unavailable.

```python
from multilingualprogramming.runtime.python_fallbacks import (
    MatrixOperations,
    NumericOperations,
    CryptoOperations,
    ImageOperations,
    FALLBACK_REGISTRY,
)

# Matrix operations
MatrixOperations.multiply(a: list[list], b: list[list]) -> list[list]
MatrixOperations.transpose(m: list[list]) -> list[list]
MatrixOperations.determinant(m: list[list]) -> float

# Numeric operations
NumericOperations.fibonacci(n: int) -> int
NumericOperations.factorial(n: int) -> int
NumericOperations.is_prime(n: int) -> bool
NumericOperations.monte_carlo_pi(samples: int) -> float

# Crypto operations
CryptoOperations.xor_cipher(data: bytes, key: bytes) -> bytes

# Image operations
ImageOperations.blur(pixels: list, width: int, height: int) -> list

# Registry
print(FALLBACK_REGISTRY)  # dict of all registered fallback functions
```

---

## Memory Model

WASM uses **linear memory** — a flat byte array accessible from both WASM and Python.

```
Linear Memory Layout (64 MB default):
┌─────────────────────────────────────────────────┐
│ 0x00000 │ Static data (strings, constants)       │
│ 0x10000 │ Stack (function frames)                │
│ 0x20000 │ Heap (dynamic allocation)              │
│ ...     │                                        │
│ 0x3FFFF │ End of 64 MB                           │
└─────────────────────────────────────────────────┘
```

Python objects are serialized to linear memory before WASM function calls, and deserialized from memory after.

---

## Module Caching

WASM modules are loaded lazily and cached:

```
First call to function X:
  1. Check module cache → miss
  2. Find .wasm file for X
  3. Load binary → instantiate → cache
  4. Call function → return result

Subsequent calls:
  1. Check module cache → hit
  2. Call function directly → return result
```

**Cache overhead**: ~10–50ms on first call, ~0ms after.

---

## WASM Generation Pipeline

For a multilingual function like:

```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

The WASM generator produces Rust intermediate code:

```rust
#[no_mangle]
pub extern "C" fn fibonacci(n: i64) -> i64 {
    if n <= 1 {
        return n;
    }
    fibonacci(n - 1) + fibonacci(n - 2)
}

#[no_mangle]
pub extern "C" fn __wasm_metadata_function_count() -> i32 {
    1
}
```

This is compiled by Cranelift to a `.wasm` binary exported to `multilingualprogramming/wasm/`.

---

## Error Handling

The WASM bridge handles errors at multiple levels:

1. **Load errors** (binary not found, invalid WASM) → fall back to Python
2. **Type errors** (argument doesn't match WASM signature) → raise `TypeError`
3. **Runtime errors** (WASM trap, out-of-bounds memory) → fall back to Python fallback
4. **Timeout** (configurable, default: no timeout) → `RuntimeError`

---

## Extending WASM with New Functions

To add a new WASM-accelerated function:

1. **Implement Python fallback** in `python_fallbacks.py`:

```python
class NewOperations:
    @staticmethod
    def my_operation(x: int, y: int) -> int:
        return x * y  # pure Python implementation
```

2. **Register the fallback**:

```python
FALLBACK_REGISTRY["my_operation"] = NewOperations.my_operation
```

3. **Add WASM code generation** in `wasm_generator.py` for the Rust/Cranelift version.

4. **Add tests** in `tests/wasm_corpus_test.py`.
