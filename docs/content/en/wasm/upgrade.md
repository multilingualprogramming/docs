---
page_id: wasm__upgrade
locale: en
title: Upgrading to v0.4 (WASM)
path_segments:
- wasm
- upgrade
source_hash: 050d2a528acc
status: source
permalink: /en/docs/wasm/upgrade/
---

## Overview

Upgrading from v0.3 to v0.4 is safe and simple:

- 100% backward compatible
- No code changes required
- Automatic 50–100x speedups via WASM
- Python fallback always available

---

## Quick Migration

### Step 1: Upgrade Package

```bash
pip install --upgrade multilingualprogramming
# or with WASM support (recommended)
pip install --upgrade "multilingualprogramming[wasm]"
```

### Step 2: No Code Changes!

Your existing v0.3 code works without modification.

### Step 3: (Optional) Verify WASM

{{snippet:wasm__upgrade__py01}}

---

## What's New in v0.4

### 1. WASM Backend

- 50–100x performance improvement for compute-heavy operations
- Transparent, automatic backend selection
- Python fallback always available when WASM is not

### 2. Smart Backend Selector

- Auto-detects WASM availability at startup
- Graceful fallback routing
- Manual override available if needed

### 3. Python Fallback Implementations

- 25+ functions with Python fallbacks
- 100% compatible outputs with WASM equivalents
- Optional NumPy optimization

### 4. Comprehensive Testing

- 33+ new test methods
- Correctness validation across backends
- Performance benchmarking

---

## Compatibility Matrix

| Feature | v0.3 | v0.4 | Notes |
|---------|------|------|-------|
| Core language | ✅ | ✅ | Identical |
| 17 languages | ✅ | ✅ | All supported |
| Python generation | ✅ | ✅ | Identical output |
| Standard library | ✅ | ✅ | Enhanced |
| Code syntax | ✅ | ✅ | No changes |
| Tests | ✅ | ✅+ | 33+ new tests |
| Performance | baseline | 50–100x | WASM acceleration |
| WASM support | ❌ | ✅ | **NEW** |

---

## Installation Options

| Variant | Command | Notes |
|---------|---------|-------|
| Python only (v0.3 style) | `pip install multilingualprogramming` | Same as v0.3 |
| With WASM | `pip install "multilingualprogramming[wasm]"` | **Recommended** |
| With NumPy | `pip install "multilingualprogramming[performance]"` | Maximum speed |

---

## Code Examples

### v0.3 Code — Works Unchanged in v0.4

{{snippet:wasm__upgrade__py02}}

### Optional: Explicit Backend Control (New in v0.4)

{{snippet:wasm__upgrade__py03}}

---

## Testing After Upgrade

Existing tests work without changes:

```bash
# Run your full test suite
pytest tests/

# Verify WASM availability
python -c "
from multilingualprogramming.runtime.backend_selector import BackendSelector
s = BackendSelector()
print('WASM available:', s.is_wasm_available())
print('Backend:', s.backend)
"
```

New v0.4 test patterns available:

{{snippet:wasm__upgrade__py04}}

---

## Breaking Changes

**None.** v0.4 is fully backward compatible.

- All v0.3 code runs unchanged
- All v0.3 APIs still supported
- No deprecations introduced

---

## New Python Requirements

Both v0.3 and v0.4 require Python 3.12+. No change.

### New Optional Dependencies

| Extra | Packages Added |
|-------|----------------|
| `[wasm]` | `wasmtime >= 1.0.0` |
| `[performance]` | `wasmtime >= 1.0.0`, `numpy >= 1.20.0` |

---

## Rollback

If you need to revert:

```bash
pip install "multilingualprogramming==0.3.0"
```

Your code works without changes after rollback.

---

## Upgrade Checklist

- [ ] Run `pip install --upgrade "multilingualprogramming[wasm]"`
- [ ] Run `pytest tests/` — confirm all passing
- [ ] Verify WASM: run the diagnostic snippet above
- [ ] Review [WASM Troubleshooting](/wasm/troubleshooting/) if any issues
- [ ] Benchmark critical paths to confirm speedups

---

## Troubleshooting

### "I don't see speedups"

WASM may not be installed or the operation may be too small for WASM overhead to pay off. See [WASM Troubleshooting](/wasm/troubleshooting/).

### "Code broken after upgrade"

This shouldn't happen. Please [open a GitHub issue](https://github.com/johnsamuelwrites/multilingual/issues) with a minimal reproduction case.

### "Can't install wasmtime"

Platform-specific issue. See [WASM Installation](/wasm/installation/) for platform requirements and workarounds.
