---
page_id: getting_started
locale: en
title: Getting Started
path_segments:
- getting-started
source_hash: 9b9c8ca97172
status: source
---

## What is multilingual?

**multilingual** is a programming language framework that lets you write programs using keywords from 17 different human languages. All language frontends compile to the same formal Core AST, then to Python or WebAssembly.

You write in your preferred language. The compiler produces identical behavior regardless of which language you used.

**Key principles:**

- **One semantic core** — All 17 languages map to the same Core AST
- **Forward-only compilation** — `Surface Language → Core AST → Python/WASM`
- **Concept-driven keywords** — `COND_IF` maps to `if` / `si` / `wenn` / `もし` etc.
- **Data-driven extensibility** — Languages added via JSON, not grammar rewrites
- **Python-compatible runtime** — Python 3.12+ syntax subset, WASM acceleration

---

## Prerequisites

- **Python 3.12+** (required)
- pip (comes with Python)
- Optional: wasmtime (for WASM backend, 50–100x speedup)

---

## Installation

### Minimal (Python backend)

```bash
pip install multilingualprogramming
```

Includes full 17-language support with Python execution. No WASM acceleration.

### Recommended (Python + WASM)

```bash
pip install multilingualprogramming[wasm]
```

Adds optional WebAssembly acceleration with automatic Python fallback.

### Maximum Performance

```bash
pip install multilingualprogramming[performance]
```

Adds NumPy for optimized numeric fallbacks alongside WASM.

---

## Verify Installation

```bash
python -c "import multilingualprogramming; print('OK')"
```

Check WASM availability:

{{snippet:getting_started__py01}}

---

## Your First Program

### English

Create a file `hello_en.ml`:

{{snippet:getting_started__py02}}

Run it:

```bash
python -m multilingualprogramming run hello_en.ml --lang en
```

### French

Create `hello_fr.ml`:

{{snippet:getting_started__py03}}

Run:

```bash
python -m multilingualprogramming run hello_fr.ml --lang fr
```

### Japanese

Create `hello_ja.ml`:

{{snippet:getting_started__py04}}

Run:

```bash
python -m multilingualprogramming run hello_ja.ml --lang ja
```

### Arabic

Create `hello_ar.ml`:

{{snippet:getting_started__py05}}

Run:

```bash
python -m multilingualprogramming run hello_ar.ml --lang ar
```

---

## Start the Interactive REPL

The REPL lets you type programs interactively with language switching:

```bash
# Default language (English)
python -m multilingualprogramming repl

# Start in French
python -m multilingualprogramming repl --lang fr

# Show generated Python alongside output
python -m multilingualprogramming repl --show-python
```

### REPL Commands

| Command | Description |
|---------|-------------|
| `:help` | Show all REPL commands |
| `:language <code>` | Switch language (e.g., `:language fr`) |
| `:python` | Toggle Python preview mode |
| `:reset` | Reset interpreter state |
| `:kw [XX]` | List keywords for current or specified language |
| `:ops [XX]` | List operators |
| `:q` | Quit |

**Example REPL session:**

```
> let x = 10
> let y = 20
> print(x + y)
30
> :language fr
Switched to: French (fr)
> soit z = x + y
> afficher(z)
30
> :q
```

---

## CLI Reference

The CLI is available as both `multilingual` and `multilg`:

```bash
# Run a program file
multilingual run <file.ml> --lang <code>

# Start REPL
multilingual repl [--lang <code>] [--show-python]

# Smoke test a language
multilingual smoke --lang <code>
multilingual smoke --all

# Show version
multilingual --version
```

---

## Use as a Python Library

{{snippet:getting_started__py06}}

---

## Next Steps

<div class="card-grid">

<div class="card">
<a href="/getting-started/installation/">
<span class="card-icon">📦</span>
<h3>Installation Details</h3>
<p>Platform-specific setup, WASM requirements, virtual environments.</p>
</a>
</div>

<div class="card">
<a href="/getting-started/quick-start/">
<span class="card-icon">🚀</span>
<h3>Quick Start Examples</h3>
<p>10-minute tour of the main language features.</p>
</a>
</div>

<div class="card">
<a href="/language-guide/">
<span class="card-icon">📖</span>
<h3>Language Guide</h3>
<p>Complete syntax reference for all 17 languages.</p>
</a>
</div>

<div class="card">
<a href="/wasm/">
<span class="card-icon">⚡</span>
<h3>WASM Backend</h3>
<p>50–100x performance with WebAssembly.</p>
</a>
</div>

</div>
