---
layout: page
title: "Getting Started"
description: "Install multilingual and write your first program in any of 17 human languages."
category: "Getting Started"
permalink: /getting-started/
next_page:
  title: "Installation"
  url: /getting-started/installation/
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

```python
from multilingualprogramming.runtime.backend_selector import BackendSelector
selector = BackendSelector()
print(f"WASM available: {selector.is_wasm_available()}")
```

---

## Your First Program

### English

Create a file `hello_en.ml`:

```python
let message = "Hello, multilingual world!"
let count = 3

for i in range(count):
    print(f"[{i}] {message}")
```

Run it:

```bash
python -m multilingualprogramming run hello_en.ml --lang en
```

### French

Create `hello_fr.ml`:

```python
soit message = "Bonjour, monde multilingue!"
soit compteur = 3

pour i dans intervalle(compteur):
    afficher(f"[{i}] {message}")
```

Run:

```bash
python -m multilingualprogramming run hello_fr.ml --lang fr
```

### Japanese

Create `hello_ja.ml`:

```python
変数 メッセージ = "こんにちは、多言語の世界！"
変数 カウント = 3

毎 i 中 範囲(カウント):
    表示(f"[{i}] {メッセージ}")
```

Run:

```bash
python -m multilingualprogramming run hello_ja.ml --lang ja
```

### Arabic

Create `hello_ar.ml`:

```python
ليكن رسالة = "مرحبا بالعالم متعدد اللغات!"
ليكن عداد = 3

لكل i في مدى(عداد):
    اطبع(f"[{i}] {رسالة}")
```

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

```python
from multilingualprogramming import (
    ProgramExecutor,
    REPL,
    Lexer,
    Parser,
    SemanticAnalyzer,
    PythonCodeGenerator,
    KeywordRegistry,
    MPNumeral,
    MPDate,
)

# Execute a multilingual program
executor = ProgramExecutor()
executor.execute("""
let greeting = "Hello"
let times = 3
for i in range(times):
    print(f"{greeting} #{i+1}")
""", language="en")

# Inspect keywords for a language
registry = KeywordRegistry()
print(registry.get_keyword("COND_IF", "fr"))   # "si"
print(registry.get_keyword("FUNC_DEF", "ja"))   # "関数"
print(registry.get_keyword("LOOP_FOR", "ar"))   # "لكل"
```

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
