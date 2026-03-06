---
page_id: wasm__faq
locale: en
title: WASM FAQ
path_segments:
- wasm
- faq
source_hash: ef56e9bd0602
status: source
permalink: /en/docs/wasm/faq/
---

## Quick Answers

**Q: Will WASM work for me?**
Yes! Python fallback always works. WASM gives 50–100x speedup if available.

**Q: What Python versions are supported?**
Python 3.12+ (full features). Check with `python --version`.

**Q: How do I install WASM support?**
`pip install multilingualprogramming[wasm]` — includes wasmtime runtime.

**Q: Is there a performance penalty if WASM is unavailable?**
No. Python fallback is automatic and transparent. No overhead for the WASM check after the first call.

**Q: Will my code break if I add WASM?**
No. WASM is purely optional. Existing code works identically. WASM improves speed, not behavior.

---

## Installation & Setup

### Which installation should I choose?

| Scenario | Command | Notes |
|----------|---------|-------|
| Testing/learning | `pip install multilingualprogramming` | Python only, 50MB |
| Development/production | `pip install multilingualprogramming[wasm]` | WASM + Python, 150MB |
| Max performance | `pip install multilingualprogramming[performance]` | + NumPy, 250MB |

### Do I need to compile anything?

No. WASM binaries are pre-compiled and included in the wheel package.

### How do I verify installation?

{{snippet:wasm__faq__py01}}

### Can I use multilingual in a virtual environment?

Yes. Works with venv, conda, poetry, and all virtual environment managers.

```bash
python -m venv myenv
source myenv/bin/activate   # Linux/macOS
myenv\Scripts\activate      # Windows
pip install multilingualprogramming[wasm]
```

---

## Performance & Speed

### How much faster is WASM?

Depends on the operation:
- Matrix operations: **100x faster**
- Cryptography: **100x faster**
- Image processing: **50x faster**
- JSON parsing: **10x faster**
- Scientific computing: **100x faster**

### Why isn't operation X faster?

Common reasons:
1. Operation is too small (< 1ms) — overhead dominates
2. WASM is not available — using Python fallback
3. Operation is not optimized for WASM yet

### Do I need to change my code for WASM performance?

No. Backend selection is automatic:
- WASM used if available (fast path)
- Python fallback if not (safe path)
- Same code, automatic benefits

### What's the WASM module load overhead?

~10–50ms on first call, then ~0ms (cached for the session).

---

## Compatibility & Platforms

### What platforms are supported?

| Platform | WASM | Python Fallback |
|----------|------|----------------|
| Windows x86_64 | ✅ | ✅ |
| Linux x86_64 | ✅ | ✅ |
| macOS x86_64 | ✅ | ✅ |
| macOS ARM64 | ✅ (emulation) | ✅ |
| Linux ARM64 | ⚠️ Community | ✅ |
| 32-bit systems | ❌ | ✅ |

### Will it work on Raspberry Pi?

Python fallback works. WASM is not available (ARM architecture). All functionality is preserved via Python fallback.

### Does it work with Docker/Kubernetes?

Yes. Same Python 3.12+ requirements.

```dockerfile
FROM python:3.12
RUN pip install multilingualprogramming[wasm]
```

### Can I use it in a web application?

- ✅ Backend (server-side): works great
- ❌ Browser (client-side): future feature

### Does WASM support all 17 languages?

Yes! All 17 languages generate both Python and WASM output. The WASM backend is language-agnostic — it operates on the Core AST, which is the same for all languages.

---

## Features & Capabilities

### Can I use multilingual with NumPy?

Yes, in both fallback and your code:

{{snippet:wasm__faq__py02}}

### What functions are WASM-accelerated?

- Matrix operations (multiply, transpose, determinant)
- Fibonacci, factorial, prime checking
- XOR cipher, hash functions
- Monte Carlo simulations
- Image blur, edge detection
- JSON parsing
- String pattern matching

### Can I add my own WASM functions?

Yes. See the [WASM Architecture](/wasm/architecture/) guide for details on extending the WASM backend.

### How does WASM interact with the 17 language frontends?

WASM acceleration happens at the **backend** level, after parsing. All 17 languages generate identical Core AST → identical WASM output. The frontend language used has no effect on WASM performance.

---

## Debugging

### How do I check if WASM is actually being used?

{{snippet:wasm__faq__py03}}

### How do I force Python execution for debugging?

{{snippet:wasm__faq__py04}}

### How do I enable verbose WASM logging?

```bash
export MULTILINGUAL_DEBUG=1
python -m multilingualprogramming run myprogram.ml --lang en
```

---

## Future Plans

### Will WASM work in browsers?

Browser-side WASM execution is a planned future feature. Currently, WASM runs server-side via wasmtime.

### Will more functions be WASM-accelerated?

Yes. The WASM backend is being extended with more operations in each release.

### Will WASM work on ARM64 natively?

Improved ARM64 support (without emulation) is on the roadmap.

---

## Getting Help

- 🐛 [GitHub Issues](https://github.com/johnsamuelwrites/multilingual/issues)
- 💬 [GitHub Discussions](https://github.com/johnsamuelwrites/multilingual/discussions)
- 📧 Email: johnsamuelwrites@gmail.com

**When reporting issues, include:**

{{snippet:wasm__faq__py05}}
