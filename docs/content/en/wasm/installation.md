---
page_id: wasm__installation
locale: en
title: WASM Installation
path_segments:
- wasm
- installation
source_hash: c2006bf62d77
status: source
permalink: /en/docs/wasm/installation/
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

{{snippet:wasm__installation__py01}}

### Comprehensive Check

{{snippet:wasm__installation__py02}}

---

## Backend Configuration

### Python API

{{snippet:wasm__installation__py03}}

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

{{snippet:wasm__installation__py04}}

### Performance not improved

1. Verify WASM is available:
   {{snippet:wasm__installation__py05}}bash
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
