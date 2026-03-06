---
page_id: wasm__performance
locale: en
title: WASM Performance Tuning
path_segments:
- wasm
- performance
source_hash: 5c6b23b59e51
status: source
permalink: /en/docs/wasm/performance/
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

{{snippet:wasm__performance__py01}}

### Profiling with Python's cProfile

{{snippet:wasm__performance__py02}}

---

## Optimization Strategies

### 1. Batch Operations

Instead of calling WASM functions in a loop, batch your data:

{{snippet:wasm__performance__py03}}

### 2. Prefer WASM for Intensive Inner Loops

{{snippet:wasm__performance__py04}}

### 3. Module Preloading

Force WASM module loading at startup to avoid first-call latency:

{{snippet:wasm__performance__py05}}

### 4. NumPy Hybrid Mode

Install with NumPy for the best non-WASM fallback:

```bash
pip install multilingualprogramming[performance]  # includes numpy
```

{{snippet:wasm__performance__py06}}

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

{{snippet:wasm__performance__py07}}

---

## Memory Optimization

### Linear Memory Layout

Default: 64MB (1024 pages × 64KB)

For large matrix operations:

{{snippet:wasm__performance__py08}}

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
   {{snippet:wasm__performance__py09}}python
# At application start
selector.call_function("fibonacci", 1)  # triggers loading + caching
```

### Issue: Memory errors on large operations

{{snippet:wasm__performance__py10}}
