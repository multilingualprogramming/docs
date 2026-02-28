---
layout: page
title: "WASM Performance Tuning"
description: "Benchmarking, optimization strategies, and profiling for the WASM backend."
category: "WASM Backend"
permalink: /wasm/performance/
prev_page:
  title: "WASM Architecture"
  url: /wasm/architecture/
next_page:
  title: "WASM Development"
  url: /wasm/development/
---

This guide covers benchmarking, profiling, and optimization strategies for the WASM backend.

---

## Performance Overview

### Expected Speedups by Operation

| Operation | Python Time | WASM Time | Speedup |
|-----------|-------------|-----------|---------|
| Matrix 1000×1000 multiply | 5.0s | 50ms | **100x** |
| Matrix 100×100 multiply | 50ms | 1ms | **50x** |
| XOR cipher (1MB) | 500ms | 5ms | **100x** |
| Fibonacci(30) | 200ms | 2ms | **100x** |
| JSON parse (10MB) | 200ms | 20ms | **10x** |
| Blur 4K image | 2s | 40ms | **50x** |
| Monte Carlo (1M samples) | 1s | 10ms | **100x** |

### When WASM Helps Most

**High speedup (50–100x):**
- Matrix operations (n > 100)
- Cryptographic operations on large data
- Scientific computing (Monte Carlo, numerical integration)
- Large-scale data processing

**Moderate speedup (10x):**
- JSON parsing of large documents
- Image processing
- String operations on large strings

**Minimal speedup (<5x):**
- Operations under 1ms (overhead exceeds savings)
- Small arrays/matrices (n < 10)
- Simple arithmetic on scalars

---

## Benchmarking Your Code

### Built-in Benchmark

```python
import time
from multilingualprogramming.runtime.backend_selector import BackendSelector, Backend

def benchmark(operation_name: str, *args, n_runs: int = 100):
    """Compare WASM vs Python performance."""

    # Python backend
    python_selector = BackendSelector(prefer_backend=Backend.PYTHON)
    python_times = []
    for _ in range(n_runs):
        start = time.perf_counter()
        python_selector.call_function(operation_name, *args)
        python_times.append(time.perf_counter() - start)
    python_avg = sum(python_times) / n_runs

    # WASM backend
    if BackendSelector().is_wasm_available():
        wasm_selector = BackendSelector(prefer_backend=Backend.WASM)
        wasm_times = []
        for _ in range(n_runs):
            start = time.perf_counter()
            wasm_selector.call_function(operation_name, *args)
            wasm_times.append(time.perf_counter() - start)
        wasm_avg = sum(wasm_times) / n_runs
        speedup = python_avg / wasm_avg
        print(f"{operation_name}:")
        print(f"  Python: {python_avg*1000:.2f}ms")
        print(f"  WASM:   {wasm_avg*1000:.2f}ms")
        print(f"  Speedup: {speedup:.1f}x")
    else:
        print(f"{operation_name}: WASM not available (Python: {python_avg*1000:.2f}ms)")

# Run benchmarks
benchmark("fibonacci", 30, n_runs=1000)
benchmark("matrix_multiply",
          [[1]*100 for _ in range(100)],
          [[2]*100 for _ in range(100)],
          n_runs=10)
```

### Profiling with Python's cProfile

```python
import cProfile
from multilingualprogramming import ProgramExecutor

code = """
let nums = [i for i in range(1000)]
let total = sum(n**2 for n in nums)
print(total)
"""

with cProfile.Profile() as prof:
    ProgramExecutor().execute(code, language="en")

prof.print_stats(sort="cumulative", limit=20)
```

---

## Optimization Strategies

### 1. Batch Operations

Instead of calling WASM functions in a loop, batch your data:

```python
# Slow: individual calls
results = []
for n in range(1, 100):
    results.append(selector.call_function("fibonacci", n))

# Fast: batch when possible (WASM works best on large data)
import numpy as np
data = np.arange(1, 100, dtype=np.int64)
# Use numpy operations directly for best performance
results = [fib(n) for n in data]  # still fast with WASM
```

### 2. Prefer WASM for Intensive Inner Loops

```python
# Computation-heavy inner loop → WASM shines
from multilingualprogramming.runtime.python_fallbacks import MatrixOperations

# Instead of nested Python loops:
result = MatrixOperations.multiply(large_matrix_a, large_matrix_b)

# Rather than:
result = [[sum(a[i][k]*b[k][j] for k in range(n)) for j in range(m)] for i in range(n)]
```

### 3. Module Preloading

Force WASM module loading at startup to avoid first-call latency:

```python
from multilingualprogramming.runtime.backend_selector import BackendSelector

# Preload at application startup
selector = BackendSelector()
if selector.is_wasm_available():
    # Warm up: triggers module loading
    selector.call_function("fibonacci", 1)
    selector.call_function("matrix_multiply", [[1]], [[1]])
    print("WASM modules preloaded")
```

### 4. NumPy Hybrid Mode

Install with NumPy for the best non-WASM fallback:

```bash
pip install multilingualprogramming[performance]  # includes numpy
```

```python
# NumPy fallback is 5-10x faster than pure Python for matrix ops
import numpy as np
from multilingualprogramming.runtime.python_fallbacks import MatrixOperations

# With numpy installed, MatrixOperations automatically uses numpy
# when WASM is not available
result = MatrixOperations.multiply(a, b)  # numpy path if WASM unavailable
```

---

## Performance by Backend

### Auto-Detection Flow

```
BackendSelector(prefer_backend=Backend.AUTO)
    │
    ├── wasmtime installed? ──No──► Python backend
    │         │
    │         Yes
    │         │
    ├── .wasm file exists? ──No──► Python backend
    │         │
    │         Yes
    │         │
    ├── Platform compatible? ──No──► Python backend
    │         │
    │         Yes
    │         │
    ├── Module loads ok? ──No──► Python backend
    │         │
    │         Yes
    │         │
    └── WASM backend ✓
```

### Backend Comparison Table

| Aspect | Python | Python+NumPy | WASM |
|--------|--------|-------------|------|
| Install size | 50MB | 150MB | 150MB |
| Matrix 100x100 | 50ms | 5ms | 1ms |
| Matrix 1000x1000 | 5s | 500ms | 50ms |
| First-call overhead | 0ms | 0ms | 10-50ms |
| Subsequent calls | — | — | ~0ms (cached) |
| Platform support | All | All | x86_64/ARM64 |
| Memory usage | Low | Medium | Medium |

---

## Configuration Options

### pyproject.toml WASM Settings

```toml
[tool.multilingual.wasm]
backend = "auto"          # "auto" | "python" | "wasm"
cranelift = true          # Use Cranelift compiler
vectorization = true      # Enable SIMD vectorization
simd = true               # Enable SIMD instructions
parallel = true           # Enable parallel execution
cache = true              # Cache WASM modules
memory_pages = 1024       # Linear memory (64MB default)
timeout_ms = 0            # 0 = no timeout
```

### Runtime Configuration

```python
from multilingualprogramming.runtime.backend_selector import BackendConfig

config = BackendConfig(
    prefer_backend=Backend.AUTO,
    cranelift=True,
    vectorization=True,
    simd=True,
    cache=True,
    memory_pages=1024,
)
selector = BackendSelector(config=config)
```

---

## Memory Optimization

### Linear Memory Layout

Default: 64MB (1024 pages × 64KB)

For large matrix operations:

```python
# For matrices > 512MB, increase memory pages
config = BackendConfig(memory_pages=8192)  # 512MB
selector = BackendSelector(config=config)
```

### Memory Usage Patterns

| Operation | Memory peak | Notes |
|-----------|-------------|-------|
| fibonacci(30) | ~1KB | Stack only |
| Matrix 100×100 | ~160KB | Input + output |
| Matrix 1000×1000 | ~16MB | Input + output |
| XOR cipher (10MB) | ~20MB | Input + output |
| Image 4K | ~50MB | 3 channels × 4K × 4K |

---

## Troubleshooting Performance

### Issue: WASM not faster than expected

1. Check if WASM is actually being used:
   ```python
   print(BackendSelector().backend)  # should be "wasm"
   ```

2. Check operation size (must be > 1ms for WASM to win):
   ```python
   import time
   start = time.perf_counter()
   result = your_operation()
   print(f"Time: {(time.perf_counter()-start)*1000:.2f}ms")
   ```

3. Verify module caching is working (second call should be faster):
   ```python
   for i in range(5):
       start = time.perf_counter()
       selector.call_function("fibonacci", 30)
       print(f"Call {i}: {(time.perf_counter()-start)*1000:.2f}ms")
   ```

### Issue: High first-call latency

Module loading takes 10-50ms. Pre-warm at startup:

```python
# At application start
selector.call_function("fibonacci", 1)  # triggers loading + caching
```

### Issue: Memory errors on large operations

```python
# Increase linear memory
config = BackendConfig(memory_pages=8192)
selector = BackendSelector(config=config)
```
