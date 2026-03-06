---
page_id: wasm__development
locale: en
title: WASM Development Guide
path_segments:
- wasm
- development
source_hash: a286b6d0538a
status: source
permalink: /en/docs/wasm/development/
---

This guide covers writing WASM-compatible multilingual programs and contributing to the WASM backend.

---

## Writing WASM-Compatible Programs

All multilingual programs are automatically compatible with both Python and WASM backends. The backend selection is transparent.

```plaintext
# This program runs on Python or WASM automatically
let matrix_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
let matrix_b = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

# Heavy computation → WASM accelerated when available
let result = matrix_multiply(matrix_a, matrix_b)
print(result)
```

### Patterns for Maximum WASM Benefit

#### 1. Large Data Operations

{{snippet:wasm__development__py01}}

#### 2. Numeric-Intensive Loops

```plaintext
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

{{snippet:wasm__development__py02}}

---

## Backend Selector API

{{snippet:wasm__development__py03}}

### BackendRegistry — Custom Functions

{{snippet:wasm__development__py04}}

---

## Adding WASM Acceleration to a Function

To add WASM acceleration for a new operation:

### Step 1: Implement Python Fallback

{{snippet:wasm__development__py05}}

### Step 2: Add WASM Code Generation

{% raw %}
{{snippet:wasm__development__py06}}
{% endraw %}

### Step 3: Compile to WASM

```bash
# Requires Rust + wasmtime
./build_wasm.sh my_compute

# Output: multilingualprogramming/wasm/my_compute.wasm
```

### Step 4: Add Tests

{{snippet:wasm__development__py07}}

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

{{snippet:wasm__development__py08}}

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
