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
│              Multilingual Programming Language v0.5.1         │
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
                    │  SemanticAnalyzer  │
                    └─────────┬──────────┘
                              │
                ┌─────────────┴──────────────┐
                │                            │
         ┌──────▼──────────┐      ┌──────────▼────────┐
         │ Python Code     │      │  WATCodeGenerator  │
         │ Generator       │      │  (wat_generator.py)│
         └──────┬──────────┘      └──────────┬────────┘
                │                            │
                │                    ┌───────▼────────┐
                │                    │  WAT Text      │
                │                    │  (module.wat)  │
                │                    └───────┬────────┘
                │                            │
                │               ┌────────────┴─────────────┐
                │               │                          │
                │       ┌───────▼────────┐      ┌──────────▼────────┐
                │       │ wasmtime       │      │ WASM Binary       │
                │       │ (server-side)  │      │ (module.wasm)     │
                │       └───────┬────────┘      └──────────┬────────┘
                └───────────────┴──────────────────────────┘
                                          │
                               ┌──────────▼──────────┐
                               │   Runtime Output    │
                               │ (via host callbacks)│
                               └─────────────────────┘
```

---

## Component 1: WATCodeGenerator

**File**: `multilingualprogramming/codegen/wat_generator.py`

Transforms the Core AST directly into WebAssembly Text Format (WAT). This is the primary WASM backend — no Rust intermediate or external compiler is involved.

**Responsibilities:**
- Transform AST nodes → WAT instructions
- Manage linear memory for strings and objects
- Emit host import declarations (`env.print_str`, `env.print_f64`, etc.)
- Generate the `__main` export as the program entry point
- Produce `abi_manifest.json` describing exported functions

**Output files** (via `multilingual build-wasm-bundle`):

| File | Description |
|------|-------------|
| `module.wat` | Human-readable WAT source (educational display) |
| `module.wasm` | Binary WASM compiled from WAT (browser execution) |
| `host_shim.js` | JS stub implementations of host import callbacks |
| `abi_manifest.json` | ABI metadata: exports, types, memory layout |

**Usage:**

```bash
# Build a complete browser bundle from a multilingual source file
multilingual build-wasm-bundle demo.ml --out-dir wasm-out
```

```python
from multilingualprogramming.codegen.wat_generator import WATCodeGenerator

gen = WATCodeGenerator()
wat_text = gen.generate(ast)   # returns WAT source as a string
```

---

## Component 2: Host Import Protocol

WAT modules produced by `WATCodeGenerator` use a **callback-based output protocol** rather than returning values. The runtime (browser or wasmtime) must supply these imports under the `env` namespace:

| Import | Signature | Description |
|--------|-----------|-------------|
| `env.print_str` | `(ptr: i32, len: i32)` | Print a UTF-8 string slice from linear memory |
| `env.print_f64` | `(val: f64)` | Print a floating-point number |
| `env.print_bool` | `(val: i32)` | Print `True` (1) or `False` (0) |
| `env.print_sep` | `()` | Print an argument separator (space) |
| `env.print_newline` | `()` | Print a newline |

**Browser import object example:**

```js
const importObject = {
  env: {
    print_str(ptr, len) {
      output += new TextDecoder().decode(new Uint8Array(memory.buffer, ptr, len));
    },
    print_f64(val)  { output += String(val); },
    print_bool(val) { output += val ? 'True' : 'False'; },
    print_sep()     { output += ' '; },
    print_newline() { output += '\n'; },
  },
};

const { instance } = await WebAssembly.instantiateStreaming(fetch('module.wasm'), importObject);
instance.exports.__main();   // run the program
```

**wasmtime import example** (server-side, via `host_shim.js` or Python bridge):

```python
# The host_shim.js / wasmtime Python bindings handle this automatically.
# Output is collected in a buffer and returned after __main() completes.
```

---

## Component 3: WAT Module Exports

Every WAT bundle produced by `WATCodeGenerator` exports:

```wat
;; Program entry point
(export "__main" (func $__main))

;; Linear memory shared with host
(export "memory" (memory $mem))
```

The `__main` function runs the top-level program statements and calls any user-defined functions as needed. The browser REPL and inline Run buttons all invoke `__main()`.

---

## Component 4: Backend Selector

**File**: `multilingualprogramming/runtime/backend_selector.py`

For server-side use, `BackendSelector` intelligently chooses between wasmtime and Python execution:

```python
from multilingualprogramming.runtime.backend_selector import (
    BackendSelector, Backend
)

# Auto-select (wasmtime if available, else Python)
sel = BackendSelector()
result = sel.call_function("fibonacci", 30)

# Force Python for debugging
sel_py = BackendSelector(prefer_backend=Backend.PYTHON)
```

---

## Memory Model

WAT uses **linear memory** — a flat byte array accessible from both the WASM module and the host.

```
Linear Memory Layout:
┌─────────────────────────────────────────────────┐
│ 0x00000 │ Static data (string constants)         │
│ 0x10000 │ Stack (function frames)                │
│ 0x20000 │ Heap (dynamic allocation)              │
│ ...     │                                        │
└─────────────────────────────────────────────────┘
```

Strings are written to linear memory before `print_str` is called; the host reads them back via `TextDecoder` (browser) or wasmtime's memory view (server).

---

## WASM Generation Pipeline

For a multilingual function like:

```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

`WATCodeGenerator` produces WAT directly:

```wat
(module
  (import "env" "print_f64"  (func $print_f64  (param f64)))
  (import "env" "print_newline" (func $print_newline))

  (func $fibonacci (param $n f64) (result f64)
    local.get $n
    f64.const 1
    f64.le
    if (result f64)
      local.get $n
    else
      local.get $n
      f64.const 1
      f64.sub
      call $fibonacci
      local.get $n
      f64.const 2
      f64.sub
      call $fibonacci
      f64.add
    end
  )

  (func $__main
    f64.const 10
    call $fibonacci
    call $print_f64
    call $print_newline
  )

  (memory (export "memory") 1)
  (export "__main" (func $__main))
)
```

This WAT text is then assembled into a `.wasm` binary (via `wabt`/`wat2wasm`) and served to the browser for execution.

---

## Build Pipeline (CI)

```
demo.ml
  │
  ▼  multilingual build-wasm-bundle demo.ml --out-dir wasm-out
wasm-out/
  ├── module.wat          ← WAT source (human-readable)
  ├── module.wasm         ← binary (browser execution)
  ├── host_shim.js        ← JS host import stubs
  └── abi_manifest.json   ← ABI metadata
  │
  ▼  wasm-validate + wasm2wat (wabt)
  ▼  mv module.* → multilingual.*
assets/wasm/
  ├── multilingual.wat
  ├── multilingual.wasm
  ├── host_shim.js
  └── abi_manifest.json
```

---

## Error Handling

The WASM bridge handles errors at multiple levels:

1. **Load errors** (binary not found, invalid WASM) → fall back to Python
2. **Host import errors** (missing `env.*` function) → `LinkError` at instantiation
3. **Runtime traps** (out-of-bounds memory, stack overflow) → caught and shown as stderr
4. **Timeout** (configurable) → `RuntimeError`

---

## OOP Object Model in WAT (v0.5.0+)

Classes with instance attributes use a **linear-memory bump allocator** for object storage. Stateless classes (no `self.attr` assignments) use `f64.const 0` as the `self` value for backward compatibility.

### Heap Allocator

```wat
(global $__heap_ptr (mut i32) (i32.const HEAP_BASE))
```

- Emitted only when at least one stateful class exists.
- `HEAP_BASE` is computed from string data size, rounded up to 8-byte alignment (minimum 64).
- Each constructor advances `$__heap_ptr` by the object's byte size and returns the pointer as `f64`.

### Field Layout

Fields are stored as `f64` values (8 bytes each) in linear memory. Inherited fields come first:

```
Object memory layout:
┌─────────────────────────────────────────────────┐
│ +0   │ field_0 (f64, 8 bytes)                   │
│ +8   │ field_1 (f64, 8 bytes)                   │
│ ...  │                                           │
└─────────────────────────────────────────────────┘
```

Field store/load pattern:

```wat
;; self.attr = value  (store)
local.get $self
i32.trunc_f64_u
i32.const <field_offset>   ;; field_index * 8
i32.add
<value>
f64.store

;; x = self.attr  (load)
local.get $self
i32.trunc_f64_u
i32.const <field_offset>
i32.add
f64.load
```

### Inheritance

- `_effective_field_layout(cls)`: merges parent fields before own fields recursively.
- `_mro(cls)`: C3 linearization (same algorithm as CPython, cycle-safe).
- Method resolution: if a subclass does not define a method, the parent's WAT function name is used.
- Constructor inheritance: if a class has no `__init__`, the parent's constructor is inherited.
- `super()` calls: `_resolve_super_call(expr)` detects `super().method(...)` and maps to the parent's WAT function.

### Stub Detection

Unsupported WAT constructs emit comment stubs:

```wat
;; unsupported call: len(mylist)
```

Use `has_stub_calls(wat_text)` to detect stubs programmatically:

```python
from multilingualprogramming.codegen.wat_generator import WATCodeGenerator, has_stub_calls

gen = WATCodeGenerator("en")
wat = gen.generate(ast)
if has_stub_calls(wat):
    print("WAT contains unsupported call stubs")
```

---

## Extending WASM with New Functions

To add a new operation to the WAT backend:

1. **Add WAT code generation** in `wat_generator.py` — emit the appropriate WAT instructions for the new AST node type.

2. **Implement Python fallback** in `python_fallbacks.py` for server-side use when wasmtime is unavailable:

```python
class NewOperations:
    @staticmethod
    def my_operation(x: int, y: int) -> int:
        return x * y

FALLBACK_REGISTRY["my_operation"] = NewOperations.my_operation
```

3. **Add tests** in `tests/wasm_corpus_test.py` verifying both backends produce identical results.
