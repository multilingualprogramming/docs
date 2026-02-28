---
layout: page
title: "WASM Troubleshooting"
description: "Solutions to common WASM backend issues."
category: "WASM Backend"
permalink: /wasm/troubleshooting/
prev_page:
  title: "WASM Development"
  url: /wasm/development/
next_page:
  title: "WASM FAQ"
  url: /wasm/faq/
---

## Quick Diagnostics

```python
from multilingualprogramming.runtime.backend_selector import BackendSelector
import sys, platform

selector = BackendSelector()
print(f"WASM Available: {selector.is_wasm_available()}")
print(f"Current Backend: {selector.backend}")
print(f"Python: {sys.version}")
print(f"Platform: {platform.system()} {platform.machine()}")
```

- `WASM Available: True` → WASM is working ✓
- `WASM Available: False` → See Issue 2 below

---

## Issue 1: ModuleNotFoundError — No module named 'wasmtime'

**Symptom:**
```
ModuleNotFoundError: No module named 'wasmtime'
```

**Cause:** wasmtime runtime not installed.

**Solutions:**

```bash
# Install with WASM support
pip install multilingualprogramming[wasm]

# Or install wasmtime separately
pip install wasmtime

# Or use Python-only mode
pip install multilingualprogramming
```

**Code workaround:**

```python
from multilingualprogramming.runtime.backend_selector import BackendSelector, Backend
selector = BackendSelector(prefer_backend=Backend.PYTHON)
```

---

## Issue 2: WASM Not Available

**Symptom:**
```
selector.is_wasm_available() → False
WASM Available: False
```

**Diagnosis:**

```python
from multilingualprogramming.runtime.backend_selector import BackendSelector
selector = BackendSelector()
print(selector.is_wasm_available())
print(selector.backend)
```

**Possible causes:**

**a) wasmtime not installed:**
```bash
pip install wasmtime>=1.0.0
```

**b) WASM binaries missing:**
```python
import os, multilingualprogramming
wasm_dir = os.path.join(os.path.dirname(multilingualprogramming.__file__), 'wasm')
print(os.listdir(wasm_dir))  # Should contain .wasm files
```
If empty: `pip install --force-reinstall multilingualprogramming[wasm]`

**c) Platform not supported (ARM64, 32-bit):**
```python
# Use Python fallback
selector = BackendSelector(prefer_backend=Backend.PYTHON)
```

**d) WASM module corruption:**
```bash
pip uninstall multilingualprogramming
pip install multilingualprogramming[wasm]
```

---

## Issue 3: Performance Not Improved

**Symptom:** WASM not faster than expected.

**Diagnosis:**

```python
import time
from multilingualprogramming.runtime.backend_selector import BackendSelector, Backend

def benchmark(func_name, *args, n=10):
    sel_py = BackendSelector(prefer_backend=Backend.PYTHON)
    sel_wasm = BackendSelector(prefer_backend=Backend.WASM)

    # Warm up WASM (first call loads module)
    sel_wasm.call_function(func_name, *args)

    # Python timing
    start = time.perf_counter()
    for _ in range(n):
        sel_py.call_function(func_name, *args)
    py_time = (time.perf_counter() - start) / n

    # WASM timing
    start = time.perf_counter()
    for _ in range(n):
        sel_wasm.call_function(func_name, *args)
    wasm_time = (time.perf_counter() - start) / n

    speedup = py_time / wasm_time if wasm_time > 0 else float('inf')
    print(f"Python: {py_time*1000:.2f}ms/call")
    print(f"WASM:   {wasm_time*1000:.2f}ms/call")
    print(f"Speedup: {speedup:.1f}x")

benchmark("fibonacci", 25)
```

**Possible causes:**

**a) Operation too small (< 1ms):**
WASM overhead dominates. Batch operations or use larger inputs.

**b) WASM not actually being used:**
```python
print(BackendSelector().backend)  # Should be "wasm"
```

**c) Operation not WASM-accelerated:**
```python
from multilingualprogramming.runtime.python_fallbacks import FALLBACK_REGISTRY
print("fibonacci" in FALLBACK_REGISTRY)
```

**d) Cold start (first call):**
Pre-warm at startup:
```python
selector.call_function("fibonacci", 1)  # Triggers loading and caching
```

---

## Issue 4: Out of Memory

**Symptom:**
```
RuntimeError: Out of memory
WASM trap: out of bounds memory access
```

**Cause:** Linear memory (default 64MB) exceeded.

**Diagnosis:**

```python
import sys
matrix_size = 10000
matrix = [[1.0] * matrix_size for _ in range(matrix_size)]
size_mb = sys.getsizeof(matrix) / 1024 / 1024
print(f"Matrix: {size_mb:.1f} MB")
# Warning if > 64MB (WASM default)
```

**Solutions:**

```python
# Increase memory allocation
from multilingualprogramming.runtime.backend_selector import BackendConfig
config = BackendConfig(memory_pages=8192)  # 512MB
selector = BackendSelector(config=config)
```

Or use Python fallback for very large data:
```python
selector = BackendSelector(prefer_backend=Backend.PYTHON)
```

---

## Issue 5: Windows ImportError

**Symptom:**
```
ImportError: DLL load failed
```

**Solution:** Install Visual C++ Redistributables, or:
```bash
pip install --upgrade wasmtime
```

---

## Issue 6: WASM Type Error

**Symptom:**
```
TypeError: Invalid argument type for WASM function
```

**Cause:** Argument type mismatch between Python and WASM signatures.

**Common type mappings:**

| Python type | Expected WASM type | Fix |
|-------------|-------------------|-----|
| `float` | `i32` | Convert: `int(value)` |
| `int` | `f64` | Convert: `float(value)` |
| `None` | any | Check for None before calling |

```python
# If you get type errors, check the function signature:
from multilingualprogramming.runtime.python_fallbacks import FALLBACK_REGISTRY
fn = FALLBACK_REGISTRY.get("my_function")
import inspect
print(inspect.signature(fn))
```

---

## Issue 7: WASM Timeout

**Symptom:** Function call hangs or takes very long.

**Solutions:**

```python
# Add timeout
from multilingualprogramming.runtime.backend_selector import BackendConfig
config = BackendConfig(timeout_ms=5000)  # 5 second timeout
selector = BackendSelector(config=config)

try:
    result = selector.call_function("long_operation", *args)
except RuntimeError as e:
    print(f"Timeout: {e}")
    # Fall back to Python
```

---

## Issue 8: Concurrent Access Errors

**Symptom:**
```
RuntimeError: WASM module already instantiated
```

**Cause:** Multiple threads trying to access the same WASM module simultaneously.

**Solution:** Use separate `BackendSelector` instances per thread:

```python
import threading

def worker(data):
    # Each thread gets its own selector
    selector = BackendSelector()
    return selector.call_function("fibonacci", data)

threads = [threading.Thread(target=worker, args=(i,)) for i in range(10)]
```

---

## Diagnostic Script

Run this to generate a complete diagnostic report:

```python
#!/usr/bin/env python3
"""WASM diagnostic script for multilingual."""
import sys
import platform
import importlib

print("=" * 60)
print("multilingual WASM Diagnostic Report")
print("=" * 60)

print(f"\nSystem:")
print(f"  Python: {sys.version}")
print(f"  Platform: {platform.system()} {platform.machine()}")
print(f"  Architecture: {platform.architecture()[0]}")

print(f"\nInstallation:")
try:
    import multilingualprogramming
    print(f"  multilingualprogramming: ✓ {multilingualprogramming.__version__}")
except ImportError as e:
    print(f"  multilingualprogramming: ✗ {e}")

try:
    import wasmtime
    print(f"  wasmtime: ✓")
except ImportError:
    print(f"  wasmtime: ✗ (not installed)")

try:
    import numpy
    print(f"  numpy: ✓ {numpy.__version__}")
except ImportError:
    print(f"  numpy: ✗ (optional)")

print(f"\nWASM Backend:")
try:
    from multilingualprogramming.runtime.backend_selector import BackendSelector
    s = BackendSelector()
    print(f"  Available: {s.is_wasm_available()}")
    print(f"  Backend: {s.backend}")
except Exception as e:
    print(f"  Error: {e}")

print(f"\nFallback Functions:")
try:
    from multilingualprogramming.runtime.python_fallbacks import FALLBACK_REGISTRY
    print(f"  Registered: {len(FALLBACK_REGISTRY)} functions")
    print(f"  Functions: {', '.join(sorted(FALLBACK_REGISTRY.keys())[:10])}...")
except Exception as e:
    print(f"  Error: {e}")

print("\n" + "=" * 60)
```

---

## Getting Help

If none of the above solves your issue:

1. Run the diagnostic script above and copy the output
2. Open an issue at: [GitHub Issues](https://github.com/johnsamuelwrites/multilingual/issues)
3. Include: diagnostic output, error message, minimal reproduction case
