---
page_id: wasm
locale: en
title: WASM Backend
path_segments:
- wasm
source_hash: 7a83161027ac
status: source
permalink: /en/docs/wasm/
---

The multilingual WASM backend provides 50–100x performance improvements for compute-intensive operations while maintaining 100% Python compatibility through automatic fallback.

<div class="callout callout-info">
<span class="callout-icon">ℹ️</span>
<div class="callout-content">
<strong>WASM is optional</strong>
<p>All multilingual programs work without WASM. The backend is transparent — the same code runs on both Python and WASM backends. Install WASM for performance, not for compatibility.</p>
</div>
</div>

---

## Key Features

<div class="card-grid">

<div class="card">
<span class="card-icon">⚡</span>
<h3>50–100x Speedup</h3>
<p>Matrix operations, cryptography, scientific computing, image processing up to 100x faster than pure Python.</p>
</div>

<div class="card">
<span class="card-icon">🔄</span>
<h3>Zero Code Changes</h3>
<p>Transparent backend selection. Your multilingual programs run identically on Python and WASM — no API changes needed.</p>
</div>

<div class="card">
<span class="card-icon">🛡️</span>
<h3>Automatic Python Fallback</h3>
<p>If WASM is unavailable (wrong platform, not installed), Python execution kicks in automatically. Never breaks.</p>
</div>

<div class="card">
<span class="card-icon">🌐</span>
<h3>Cross-Platform</h3>
<p>Windows x86_64, Linux x86_64, macOS x86_64, macOS ARM64. Works in Docker, virtual environments, CI/CD.</p>
</div>

<div class="card">
<span class="card-icon">🔧</span>
<h3>WAT Code Generation</h3>
<p>Compiles the Core AST directly to WebAssembly Text (WAT) format. WAT is assembled to binary WASM and executed via wasmtime — no external Rust toolchain required.</p>
</div>

<div class="card">
<span class="card-icon">📦</span>
<h3>25+ Pure Python Fallbacks</h3>
<p>Every WASM-accelerated function has a pure Python fallback implementation. Full coverage, always.</p>
</div>

</div>

---

## Performance Overview

| Operation | Python | WASM | Speedup |
|-----------|--------|------|---------|
| Matrix 1000×1000 multiply | 5.0s | 50ms | **100x** |
| Matrix 100×100 multiply | 50ms | 1ms | **50x** |
| XOR cipher (1MB) | 500ms | 5ms | **100x** |
| Fibonacci(30) | 200ms | 2ms | **100x** |
| JSON parse (10MB) | 200ms | 20ms | **10x** |
| Blur 4K image | 2s | 40ms | **50x** |
| Monte Carlo (1M samples) | 1s | 10ms | **100x** |

---

## Quick Start

### Install with WASM

```bash
pip install multilingualprogramming[wasm]
```

### Verify WASM Availability

{{snippet:wasm__py01}}

### Force a Specific Backend

{{snippet:wasm__py02}}

### Environment Variable Override

```bash
# Force Python backend
export MULTILINGUAL_BACKEND=python

# Force WASM
export MULTILINGUAL_BACKEND=wasm

# Enable verbose logging
export MULTILINGUAL_DEBUG=1
```

---

## WASM Architecture

```
multilingual Source (.ml)
        │
        ▼
  ┌──────────────┐
  │ Lexer/Parser │  (same pipeline for both backends)
  └──────┬───────┘
         │ Core AST
         ▼
  ┌─────────────────┐
  │  WAT Generator  │  → WAT text (module.wat)
  │  (wat_generator.py)  │    ↓
  └─────────────────┘  wabt / wat2wasm
                            ↓
                       .wasm binary
                            │
                 ┌──────────┴──────────┐
                 │                     │
         ┌───────▼──────┐    ┌─────────▼────────┐
         │ WASM Loader  │    │ Backend Selector  │
         │ (loader.py)  │    │ (auto-detect)     │
         └───────┬──────┘    └─────────┬─────────┘
                 │                     │
    ┌────────────┴─────────────────────┘
    │
    ▼
┌──────────────────────────────────┐
│        Execution                 │
│  WASM path: wasmtime runtime     │
│  Python path: pure Python        │
└──────────────────────────────────┘
```

---

## Backend Selection Algorithm

```
1. Check if wasmtime is installed
2. Check if WASM binary (.wasm) exists
3. Check platform compatibility
4. Try to load and instantiate WASM module
5. If any step fails → use Python fallback (transparent)
6. Cache loaded modules for subsequent calls
```

---

## WAT Language Support

The WAT backend supports a rich subset of the multilingual language. Unsupported constructs emit stub comments and fall back to Python.

| Construct | WAT support |
|---|---|
| Variable declaration/assignment | ✓ |
| Arithmetic (+, -, *, /) | ✓ (f64) |
| Augmented assignment (+=, -=, *=, /=, //=, %=) | ✓ |
| Augmented assignment (&=, \|=, ^=, <<=, >>=) | ✓ i32 round-trip |
| Comparisons and boolean logic | ✓ |
| `if` / `elif` / `else` | ✓ |
| `while` loop | ✓ |
| `for` loop | ✓ |
| Function definition and `return` | ✓ |
| `async def` / `await` | ✓ best-effort |
| Class definition (OOP) with fields | ✓ linear-memory object model |
| Inheritance and `super()` | ✓ C3 MRO |
| `match`/`case` (numeric/boolean) | ✓ lowered to WAT blocks |
| `match`/`case` (string/complex) | stub |
| `print` | ✓ host import |
| `abs`, `min`, `max` (n-arg) | ✓ native f64 ops |
| `len` (string literal/var, list, tuple) | ✓ |
| List/tuple literal allocation | ✓ heap bump-allocator |
| List/tuple index read | ✓ |
| `try/except/finally` | ✓ best-effort |
| `with` statement | ✓ best-effort |
| Lambda expressions | ✓ lifted to named WAT functions |
| List/generator comprehension over `range` | ✓ |
| String concatenation, indexing, slicing | not supported |
| `async for` / `async with` | not supported |

---

## Supported Operations

All 17 languages support both Python and WASM backends. The WASM backend accelerates:

- **Matrix operations** — multiply, transpose, determinant, inverse
- **Cryptography** — XOR, AES-like operations, hashing
- **Scientific computing** — Monte Carlo, numerical integration, FFT
- **Image processing** — blur, sharpen, edge detection
- **String operations** — pattern matching, encoding
- **JSON parsing** — large document processing
- **Fibonacci and numeric recursion** — optimized integer arithmetic

---

## Installation Options

| Option | Command | Size | Features |
|--------|---------|------|---------|
| Minimal | `pip install multilingualprogramming` | ~50MB | Python only |
| Recommended | `pip install multilingualprogramming[wasm]` | ~150MB | WASM + Python fallback |
| Performance | `pip install multilingualprogramming[performance]` | ~250MB | WASM + NumPy + Python |

---

## Documentation Pages

{% capture installation_url %}{{ '/en/docs/wasm/installation/' | relative_url }}{% endcapture %}
{% capture architecture_url %}{{ '/en/docs/wasm/architecture/' | relative_url }}{% endcapture %}
{% capture performance_url %}{{ '/en/docs/wasm/performance/' | relative_url }}{% endcapture %}
{% capture development_url %}{{ '/en/docs/wasm/development/' | relative_url }}{% endcapture %}
{% capture troubleshooting_url %}{{ '/en/docs/wasm/troubleshooting/' | relative_url }}{% endcapture %}
{% capture faq_url %}{{ '/en/docs/wasm/faq/' | relative_url }}{% endcapture %}

<div class="card-grid">

<div class="card">
<a href="{{ installation_url | strip }}">
<span class="card-icon">📦</span>
<h3>Installation Guide</h3>
<p>Platform-specific setup, verification, troubleshooting common installation issues.</p>
</a>
</div>

<div class="card">
<a href="{{ architecture_url | strip }}">
<span class="card-icon">🏛️</span>
<h3>Architecture Overview</h3>
<p>WASM infrastructure stack, code generation pipeline, Python–WASM bridge.</p>
</a>
</div>

<div class="card">
<a href="{{ performance_url | strip }}">
<span class="card-icon">📈</span>
<h3>Performance Tuning</h3>
<p>Benchmarking, optimization strategies, profiling, and performance expectations by operation type.</p>
</a>
</div>

<div class="card">
<a href="{{ development_url | strip }}">
<span class="card-icon">🛠️</span>
<h3>WASM Development</h3>
<p>Writing WASM-compatible multilingual code, contributing to the WASM backend.</p>
</a>
</div>

<div class="card">
<a href="{{ troubleshooting_url | strip }}">
<span class="card-icon">🔍</span>
<h3>Troubleshooting</h3>
<p>Common issues, platform-specific workarounds, diagnostic commands.</p>
</a>
</div>

<div class="card">
<a href="{{ faq_url | strip }}">
<span class="card-icon">❓</span>
<h3>FAQ</h3>
<p>Frequently asked questions about WASM support, performance, and compatibility.</p>
</a>
</div>

</div>
