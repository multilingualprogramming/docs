---
layout: page
title: "WASM Development Guide"
description: "Guide to developing with and contributing to the multilingual WASM backend."
category: "WASM Backend"
permalink: /wasm/development/
prev_page:
  title: "Performance Tuning"
  url: /wasm/performance/
next_page:
  title: "WASM Troubleshooting"
  url: /wasm/troubleshooting/
---

This guide covers writing WASM-compatible multilingual programs and contributing to the WASM backend.

---

## Writing WASM-Compatible Programs

All multilingual programs are automatically compatible with both Python and WASM backends. The backend selection is transparent.

```python
# This program runs on Python or WASM automatically
let matrix_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
let matrix_b = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

# Heavy computation → WASM accelerated when available
let result = matrix_multiply(matrix_a, matrix_b)
print(result)
```

### Patterns for Maximum WASM Benefit

#### 1. Large Data Operations

```python
# Generate large dataset
let size = 500
let matrix = [[i * size + j for j in range(size)] for i in range(size)]

# WASM accelerates this 100x
let transposed = matrix_transpose(matrix)
```

#### 2. Numeric-Intensive Loops

```python
# Scientific computation — WASM excels here
def monte_carlo_pi(samples):
    let inside = 0
    for i in range(samples):
        let x = random()
        let y = random()
        if x*x + y*y <= 1.0:
            inside += 1
    return 4.0 * inside / samples

# With large samples, WASM gives 100x speedup
let pi_estimate = monte_carlo_pi(1000000)
print(f"π ≈ {pi_estimate:.4f}")
```

#### 3. Cryptographic Operations

```python
import os

let data = os.urandom(1024 * 1024)  # 1MB
let key = b"secret_key"

# XOR cipher — WASM gives 100x speedup on large data
def xor_cipher(data, key):
    return bytes(b ^ key[i % len(key)] for i, b in enumerate(data))

let encrypted = xor_cipher(data, key)
```

---

## Backend Selector API

```python
from multilingualprogramming.runtime.backend_selector import (
    BackendSelector,
    BackendRegistry,
    BackendConfig,
    Backend,
)

# Basic usage
selector = BackendSelector()
result = selector.call_function("fibonacci", 30)
print(result)

# Force Python for debugging
python_selector = BackendSelector(prefer_backend=Backend.PYTHON)
result = python_selector.call_function("fibonacci", 30)

# Check backend per call
print(f"Using: {selector.backend}")
```

### BackendRegistry — Custom Functions

```python
from multilingualprogramming.runtime.backend_selector import BackendRegistry

registry = BackendRegistry()

# Register a Python implementation
def my_add(x: int, y: int) -> int:
    return x + y

registry.register_python("my_add", my_add)

# Register a WASM implementation (path to .wasm binary)
registry.register_wasm("my_add_fast", "./my_add.wasm")

# Call using best available backend
result = registry.call("my_add", 5, 3)
```

---

## Adding WASM Acceleration to a Function

To add WASM acceleration for a new operation:

### Step 1: Implement Python Fallback

```python
# In multilingualprogramming/runtime/python_fallbacks.py

class MyOperations:
    @staticmethod
    def my_compute(x: int, y: int) -> int:
        """Pure Python fallback implementation."""
        result = 0
        for i in range(x):
            result += i * y
        return result

# Register in FALLBACK_REGISTRY
FALLBACK_REGISTRY["my_compute"] = MyOperations.my_compute
```

### Step 2: Add WASM Code Generation

{% raw %}
```python
# In multilingualprogramming/codegen/wasm_generator.py

def generate_my_compute_wasm(self, x_type="i64", y_type="i64") -> str:
    """Generate Rust code for my_compute."""
    return f"""
#[no_mangle]
pub extern "C" fn my_compute(x: {x_type}, y: {y_type}) -> {x_type} {{
    let mut result: {x_type} = 0;
    for i in 0..x {{
        result += i * y;
    }}
    result
}}
"""
```
{% endraw %}

### Step 3: Compile to WASM

```bash
# Requires Rust + wasmtime
./build_wasm.sh my_compute

# Output: multilingualprogramming/wasm/my_compute.wasm
```

### Step 4: Add Tests

```python
# In tests/wasm_corpus_test.py

def test_my_compute_wasm():
    from multilingualprogramming.runtime.backend_selector import BackendSelector, Backend

    # Python result
    py_sel = BackendSelector(prefer_backend=Backend.PYTHON)
    py_result = py_sel.call_function("my_compute", 100, 5)

    # WASM result (if available)
    if BackendSelector().is_wasm_available():
        wasm_sel = BackendSelector(prefer_backend=Backend.WASM)
        wasm_result = wasm_sel.call_function("my_compute", 100, 5)
        assert py_result == wasm_result

    assert py_result == sum(i * 5 for i in range(100))
```

---

## Development Environment

### Setup

```bash
git clone https://github.com/johnsamuelwrites/multilingual.git
cd multilingual

# Development installation (all extras)
pip install -e ".[dev,wasm,performance]"

# Install Rust (for building WASM modules)
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

### Running WASM Tests

```bash
# WASM-specific tests
pytest tests/wasm_corpus_test.py -v
pytest tests/wasm_comprehensive_test.py -v

# All tests including WASM
pytest -q

# With verbose WASM logging
MULTILINGUAL_DEBUG=1 pytest tests/wasm_corpus_test.py -v
```

### Building WASM Binaries from Source

```bash
# Requires Rust + wasm-pack or wasmtime CLI
./build_wasm.sh

# Or manually:
cd multilingualprogramming/wasm/src
cargo build --target wasm32-unknown-unknown --release
cp target/wasm32-unknown-unknown/release/*.wasm ../
```

---

## WASM Module Structure

A WASM module in multilingual typically exports:

```rust
// Required exports
#[no_mangle]
pub extern "C" fn function_name(arg1: i64, arg2: f64) -> i64 { ... }

// Metadata exports
#[no_mangle]
pub extern "C" fn __wasm_metadata_function_count() -> i32 { ... }

#[no_mangle]
pub extern "C" fn __wasm_metadata_version() -> i32 { 1 }

// Memory management (if needed)
#[no_mangle]
pub extern "C" fn __wasm_alloc(size: i32) -> i32 { ... }

#[no_mangle]
pub extern "C" fn __wasm_free(ptr: i32, size: i32) { ... }
```

---

## Testing Equivalence

WASM and Python backends must produce identical results. Test both:

```python
import pytest
from multilingualprogramming.runtime.backend_selector import BackendSelector, Backend

@pytest.fixture
def python_selector():
    return BackendSelector(prefer_backend=Backend.PYTHON)

@pytest.fixture
def wasm_selector():
    selector = BackendSelector(prefer_backend=Backend.WASM)
    if not selector.is_wasm_available():
        pytest.skip("WASM not available")
    return selector

def test_fibonacci_equivalence(python_selector, wasm_selector):
    for n in range(0, 20):
        py_result = python_selector.call_function("fibonacci", n)
        wasm_result = wasm_selector.call_function("fibonacci", n)
        assert py_result == wasm_result, f"Mismatch at n={n}: {py_result} != {wasm_result}"

def test_matrix_multiply_equivalence(python_selector, wasm_selector):
    a = [[1, 2, 3], [4, 5, 6]]
    b = [[7, 8], [9, 10], [11, 12]]
    py_result = python_selector.call_function("matrix_multiply", a, b)
    wasm_result = wasm_selector.call_function("matrix_multiply", a, b)
    assert py_result == wasm_result
```

---

## CI/CD Configuration

```yaml
# .github/workflows/wasm-tests.yml
name: WASM Tests

on: [push, pull_request]

jobs:
  test-wasm:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.12'
      - name: Install with WASM
        run: pip install -e ".[dev,wasm]"
      - name: Run WASM tests
        run: pytest tests/wasm_corpus_test.py tests/wasm_comprehensive_test.py -v
      - name: Run all tests
        run: pytest -q
```
