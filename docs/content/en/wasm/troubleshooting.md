---
page_id: wasm__troubleshooting
locale: en
title: WASM Troubleshooting
path_segments:
- wasm
- troubleshooting
source_hash: 51e65aa3dd68
status: source
permalink: /en/docs/wasm/troubleshooting/
---

## Quick Diagnostics

{{snippet:wasm__troubleshooting__py01}}

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

{{snippet:wasm__troubleshooting__py02}}

---

## Issue 2: WASM Not Available

**Symptom:**
```
selector.is_wasm_available() → False
WASM Available: False
```

**Diagnosis:**

{{snippet:wasm__troubleshooting__py03}}

**Possible causes:**

**a) wasmtime not installed:**
```bash
pip install wasmtime>=1.0.0
```

**b) WASM binaries missing:**
{{snippet:wasm__troubleshooting__py04}}
If empty: `pip install --force-reinstall multilingualprogramming[wasm]`

**c) Platform not supported (ARM64, 32-bit):**
{{snippet:wasm__troubleshooting__py05}}

**d) WASM module corruption:**
```bash
pip uninstall multilingualprogramming
pip install multilingualprogramming[wasm]
```

---

## Issue 3: Performance Not Improved

**Symptom:** WASM not faster than expected.

**Diagnosis:**

{{snippet:wasm__troubleshooting__py06}}

**Possible causes:**

**a) Operation too small (< 1ms):**
WASM overhead dominates. Batch operations or use larger inputs.

**b) WASM not actually being used:**
{{snippet:wasm__troubleshooting__py07}}

**c) Operation not WASM-accelerated:**
{{snippet:wasm__troubleshooting__py08}}

**d) Cold start (first call):**
Pre-warm at startup:
{{snippet:wasm__troubleshooting__py09}}

---

## Issue 4: Out of Memory

**Symptom:**
```
RuntimeError: Out of memory
WASM trap: out of bounds memory access
```

**Cause:** Linear memory (default 64MB) exceeded.

**Diagnosis:**

{{snippet:wasm__troubleshooting__py10}}

**Solutions:**

{{snippet:wasm__troubleshooting__py11}}

Or use Python fallback for very large data:
{{snippet:wasm__troubleshooting__py12}}

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

{{snippet:wasm__troubleshooting__py13}}

---

## Issue 7: WASM Timeout

**Symptom:** Function call hangs or takes very long.

**Solutions:**

{{snippet:wasm__troubleshooting__py14}}

---

## Issue 8: Concurrent Access Errors

**Symptom:**
```
RuntimeError: WASM module already instantiated
```

**Cause:** Multiple threads trying to access the same WASM module simultaneously.

**Solution:** Use separate `BackendSelector` instances per thread:

{{snippet:wasm__troubleshooting__py15}}

---

## Diagnostic Script

Run this to generate a complete diagnostic report:

{{snippet:wasm__troubleshooting__py16}}

---

## Getting Help

If none of the above solves your issue:

1. Run the diagnostic script above and copy the output
2. Open an issue at: [GitHub Issues](https://github.com/johnsamuelwrites/multilingual/issues)
3. Include: diagnostic output, error message, minimal reproduction case
