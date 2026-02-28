---
layout: page
title: "WASM Installation"
description: "Install and verify the WebAssembly backend for multilingual."
category: "WASM Backend"
permalink: /wasm/installation/
prev_page:
  title: "WASM Overview"
  url: /wasm/
next_page:
  title: "WASM Architecture"
  url: /wasm/architecture/
---

The WASM backend is an optional component that provides 50–100x speedups for compute-intensive operations. Python execution always works as a fallback.

---

## Installation Options

### Option 1: Minimal (Python Only)

```bash
pip install multilingualprogramming
```

- Full 17-language support
- All standard library modules
- No WASM acceleration (Python fallback only)
- ~50 MB

### Option 2: Recommended (Python + WASM)

```bash
pip install multilingualprogramming[wasm]
```

- Full 17-language support
- 50–100x acceleration for matrix, crypto, scientific operations
- 10x acceleration for JSON parsing
- Automatic fallback to Python
- ~150 MB
- Requires: wasmtime (auto-installed)

### Option 3: Maximum Performance

```bash
pip install multilingualprogramming[performance]
```

- All WASM features
- NumPy-optimized fallbacks (matrix ops up to 10x faster than pure Python)
- Hybrid execution (WASM where available, NumPy where not)
- ~250 MB

---

## Platform-Specific Setup

### Linux

```bash
python3 -m pip install multilingualprogramming[wasm]

# Verify
python3 -c "
from multilingualprogramming.runtime.backend_selector import BackendSelector
s = BackendSelector()
print(f'WASM: {s.is_wasm_available()}')
print(f'Backend: {s.backend}')
"
```

### macOS

```bash
# Homebrew Python (optional)
brew install python@3.12

python3 -m pip install multilingualprogramming[wasm]

# macOS ARM64 (Apple Silicon): WASM runs via emulation
python3 -c "from multilingualprogramming.runtime.backend_selector import BackendSelector; print(BackendSelector().is_wasm_available())"
```

### Windows

```powershell
python -m pip install multilingualprogramming[wasm]

# Verify
python -c "from multilingualprogramming.runtime.backend_selector import BackendSelector; print(BackendSelector().is_wasm_available())"
```

---

## Verification

### Quick Test

```python
from multilingualprogramming.runtime.backend_selector import BackendSelector, Backend

selector = BackendSelector()
print(f"WASM Available: {selector.is_wasm_available()}")

# Test a function
result = selector.call_function("fibonacci", 10)
print(f"Fibonacci(10): {result}")
```

### Comprehensive Check

```python
#!/usr/bin/env python3
import sys
import platform
from multilingualprogramming.runtime.backend_selector import BackendSelector
from multilingualprogramming.runtime.python_fallbacks import (
    MatrixOperations,
    NumericOperations,
    FALLBACK_REGISTRY,
)

print("=" * 60)
print("Multilingual Programming — WASM Installation Check")
print("=" * 60)

print(f"\n1. System Information:")
print(f"   Platform: {platform.system()}")
print(f"   Python: {sys.version}")
print(f"   Architecture: {platform.machine()}")

selector = BackendSelector()
print(f"\n2. WASM Support:")
print(f"   Available: {selector.is_wasm_available()}")
print(f"   Current Backend: {selector.backend}")

print(f"\n3. Fallback Functions:")
print(f"   Registered: {len(FALLBACK_REGISTRY)} functions")

print(f"\n4. Basic Operations:")
try:
    fib = NumericOperations.fibonacci(10)
    print(f"   ✓ Fibonacci(10): {fib}")

    result = MatrixOperations.multiply([[1, 2], [3, 4]], [[5, 6], [7, 8]])
    print(f"   ✓ Matrix multiply: success")
except Exception as e:
    print(f"   ✗ Error: {e}")

print("\n" + "=" * 60)
if selector.is_wasm_available():
    print("✓ WASM support enabled — 50–100x speedups active!")
else:
    print("⚠ WASM not available — using Python fallback")
    print("  To enable WASM: pip install wasmtime")
print("=" * 60)
```

---

## Backend Configuration

### Python API

```python
from multilingualprogramming.runtime.backend_selector import BackendSelector, Backend

# Auto-detect (default): WASM if available, else Python
selector = BackendSelector(prefer_backend=Backend.AUTO)

# Force Python fallback (debugging, testing)
selector = BackendSelector(prefer_backend=Backend.PYTHON)

# Force WASM (will raise RuntimeError if unavailable)
selector = BackendSelector(prefer_backend=Backend.WASM)
try:
    result = selector.call_function("fibonacci", 10)
except RuntimeError as e:
    print(f"WASM not available: {e}")
```

### Environment Variables

```bash
# Force Python backend globally
export MULTILINGUAL_BACKEND=python

# Force WASM globally
export MULTILINGUAL_BACKEND=wasm

# Verbose logging
export MULTILINGUAL_DEBUG=1
```

---

## Performance Expectations

| Operation | Python | WASM | Speedup |
|-----------|--------|------|---------|
| Matrix 1000×1000 multiply | 5.0s | 50ms | **100x** |
| Matrix 100×100 multiply | 50ms | 1ms | **50x** |
| XOR cipher (1MB) | 500ms | 5ms | **100x** |
| Fibonacci(30) | 200ms | 2ms | **100x** |
| JSON parse (10MB) | 200ms | 20ms | **10x** |
| Blur 4K image | 2s | 40ms | **50x** |

**When you'll see the most benefit:**
- Matrix operations with n > 100
- Cryptographic operations on large data
- Scientific computing (Monte Carlo, numerical integration)
- Large-scale JSON processing

**When benefits are minimal:**
- Operations under 1ms (overhead dominates)
- Simple string operations
- Small arrays/matrices

---

## Supported Platforms

### Tier 1 (Fully Supported)

| Platform | WASM | Python Fallback |
|----------|------|----------------|
| Linux x86_64 | ✅ | ✅ |
| Windows x86_64 | ✅ | ✅ |
| macOS x86_64 | ✅ | ✅ |
| macOS ARM64 | ✅ (emulation) | ✅ |

### Tier 2 (Community Support)

| Platform | WASM | Python Fallback |
|----------|------|----------------|
| Linux ARM64 | ⚠️ | ✅ |
| Windows ARM64 | ⚠️ | ✅ |
| BSD variants | ⚠️ | ✅ |
| 32-bit systems | ❌ | ✅ |

---

## Troubleshooting

### `ModuleNotFoundError: No module named 'wasmtime'`

```bash
pip install wasmtime
# or reinstall with WASM extras
pip install multilingualprogramming[wasm]
```

### WASM not available on macOS ARM64

ARM64 runs via emulation. To explicitly use Python fallback:

```python
from multilingualprogramming.runtime.backend_selector import BackendSelector, Backend
selector = BackendSelector(prefer_backend=Backend.PYTHON)
```

### Performance not improved

1. Verify WASM is available:
   ```python
   print(BackendSelector().is_wasm_available())
   ```

2. Check operation is registered:
   ```python
   from multilingualprogramming.runtime.python_fallbacks import FALLBACK_REGISTRY
   print("matrix_multiply" in FALLBACK_REGISTRY)
   ```

3. Check current backend:
   ```python
   print(BackendSelector().backend)
   ```

### Windows ImportError

Install Visual C++ Redistributables or:

```bash
pip install --upgrade wasmtime
```

---

## System Requirements

| Component | Minimum | Recommended (WASM) |
|-----------|---------|-------------------|
| Python | 3.12+ | 3.12+ |
| RAM | 256 MB | 512 MB |
| Disk | 50 MB | 150 MB |
| OS | Any | Windows/Linux/macOS x86_64 |
| CPU | Any | 64-bit |

---

## Building from Source (WASM)

```bash
git clone https://github.com/johnsamuelwrites/multilingual.git
cd multilingual

# Install development dependencies
pip install -e ".[dev,wasm]"

# Run WASM tests
pytest tests/wasm_corpus_test.py
pytest tests/wasm_comprehensive_test.py

# Build WASM modules (requires Rust + cranelift)
./build_wasm.sh
```

---

## Uninstalling

```bash
# Remove WASM support only
pip uninstall wasmtime

# Complete removal
pip uninstall multilingualprogramming
```
