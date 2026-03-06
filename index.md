---
layout: home
title: "Multilingual Programming Language"
description: "Write programs in English, French, Spanish, Japanese, Arabic, Hindi and more. One formal core. Python and WASM backends."
permalink: /
---

<section class="hero">
  <span class="hero-eyebrow">v0.5.1 &mdash; Now with WASM &amp; OOP</span>
  <h1 class="hero-title">
    Write Code in<br/>
    <span class="gradient-text">Any Human Language</span>
  </h1>
  <p class="hero-description">
    <strong>multilingual</strong> is a programming language with one formal semantic core and multiple natural-language frontends. Write in English, French, Spanish, Japanese, Arabic, Hindi and more &mdash; compile to Python or WASM.
  </p>
  <div class="hero-actions">
    <a href="{{ '/en/docs/getting-started/' | relative_url }}" class="btn btn-primary">Get Started &rarr;</a>
    <a href="{{ '/en/docs/language-guide/' | relative_url }}" class="btn btn-secondary">Language Guide</a>
    <a href="https://github.com/johnsamuelwrites/multilingual" class="btn btn-secondary" target="_blank" rel="noopener">View on GitHub</a>
  </div>
</section>

<div class="stats-strip">
  <div class="stat-item">
    <div class="stat-value">17</div>
    <div class="stat-label">Human Languages</div>
  </div>
  <div class="stat-item">
    <div class="stat-value">1,797</div>
    <div class="stat-label">Test Cases</div>
  </div>
  <div class="stat-item">
    <div class="stat-value">100x</div>
    <div class="stat-label">WASM Speedup</div>
  </div>
  <div class="stat-item">
    <div class="stat-value">41</div>
    <div class="stat-label">Localized Builtins</div>
  </div>
  <div class="stat-item">
    <div class="stat-value">0.5.1</div>
    <div class="stat-label">Current Version</div>
  </div>
</div>

<!-- Code demo -->
<section class="home-section" style="padding-top:3rem" markdown="1">
  <div style="text-align:center; margin-bottom:2rem">
    <span class="section-eyebrow">Same Program, Every Language</span>
    <h2 class="section-title">One Syntax Model, 17 Expressions</h2>
    <p class="section-desc" style="margin: 0 auto 0">Write the same logic in any supported language. The compiler maps it all to the same formal core and Python output.</p>
  </div>

<div class="code-demo">
  <div class="code-demo-header">
    <span class="code-demo-dot dot-red"></span>
    <span class="code-demo-dot dot-yellow"></span>
    <span class="code-demo-dot dot-green"></span>
    <span class="code-demo-title">hello.ml</span>
  </div>
  <div class="code-demo-tabs">
    <button class="code-tab active" data-target="en">English</button>
    <button class="code-tab" data-target="fr">French</button>
    <button class="code-tab" data-target="es">Spanish</button>
    <button class="code-tab" data-target="ja">Japanese</button>
    <button class="code-tab" data-target="ar">Arabic</button>
    <button class="code-tab" data-target="hi">Hindi</button>
  </div>
  <div class="code-demo-body">
    <div class="code-panel" data-lang="en" style="display:block">
{% highlight python %}
let name = "world"
let count = 5

def greet(n):
    for i in range(count):
        print(f"Hello, {n}! iteration {i}")

greet(name)
{% endhighlight %}
</div>
    <div class="code-panel" data-lang="fr" style="display:none">
{% highlight python %}
soit nom = "monde"
soit compteur = 5

déf saluer(n):
    pour i dans intervalle(compteur):
        afficher(f"Bonjour, {n}! iteration {i}")

saluer(nom)
{% endhighlight %}
</div>
    <div class="code-panel" data-lang="es" style="display:none">
{% highlight python %}
sea nombre = "mundo"
sea contador = 5

def saludar(n):
    para i en rango(contador):
        imprimir(f"Hola, {n}! iteracion {i}")

saludar(nombre)
{% endhighlight %}
</div>
    <div class="code-panel" data-lang="ja" style="display:none">
{% highlight python %}
変数 名前 = "世界"
変数 カウント = 5

関数 挨拶(n):
    毎 i 中 範囲(カウント):
        表示(f"こんにちは {n} 繰り返し {i}")

挨拶(名前)
{% endhighlight %}
</div>
    <div class="code-panel" data-lang="ar" style="display:none">
{% highlight python %}
ليكن اسم = "العالم"
ليكن عداد = 5

دالة تحية(n):
    لكل i في مدى(عداد):
        اطبع(f"مرحبا {n} تكرار {i}")

تحية(اسم)
{% endhighlight %}
</div>
    <div class="code-panel" data-lang="hi" style="display:none">
{% highlight python %}
मान नाम = "दुनिया"
मान गिनती = 5

परिभाषा नमस्ते(n):
    के_लिए i में परास(गिनती):
        छापो(f"नमस्ते {n} पुनरावृत्ति {i}")

नमस्ते(नाम)
{% endhighlight %}
</div>
  </div>
</div>

</section>

<!-- Features -->
<section class="home-section" markdown="1">
  <span class="section-eyebrow">Why multilingual?</span>
  <h2 class="section-title">Designed for the World</h2>

<div class="feature-grid">

<div class="feature-card">
<span class="feature-icon">🌐</span>
<div class="feature-title">17 Human Languages</div>
<p class="feature-desc">English, French, Spanish, German, Italian, Portuguese, Polish, Dutch, Swedish, Danish, Finnish, Hindi, Arabic, Bengali, Tamil, Chinese, and Japanese — all as first-class frontends.</p>
</div>

<div class="feature-card">
<span class="feature-icon">⬡</span>
<div class="feature-title">One Formal Core</div>
<p class="feature-desc">All language frontends compile to the same Core AST and CoreIRProgram. Semantics are identical regardless of the surface language used.</p>
</div>

<div class="feature-card">
<span class="feature-icon">⚡</span>
<div class="feature-title">WASM Backend</div>
<p class="feature-desc">Optional WebAssembly backend delivers 50–100x speedups for matrix operations, cryptography, scientific computing, and more — with automatic Python fallback.</p>
</div>

<div class="feature-card">
<span class="feature-icon">🐍</span>
<div class="feature-title">Python Compatible</div>
<p class="feature-desc">Full Python 3.12+ syntax subset: classes, async/await, comprehensions, decorators, f-strings, pattern matching, generators, context managers, and more.</p>
</div>

<div class="feature-card">
<span class="feature-icon">🔧</span>
<div class="feature-title">Data-Driven Extensibility</div>
<p class="feature-desc">Add a new programming language primarily through JSON configuration files — no parser rewrites needed. Keyword mappings, builtins, and surface patterns all via data.</p>
</div>

<div class="feature-card">
<span class="feature-icon">🧪</span>
<div class="feature-title">~1,797 Tests, 58 Files</div>
<p class="feature-desc">Comprehensive test coverage across all 17 languages. Every language frontend is validated end-to-end: lexer → parser → semantic → codegen → execution.</p>
</div>

<div class="feature-card">
<span class="feature-icon">📝</span>
<div class="feature-title">Interactive REPL</div>
<p class="feature-desc">Language-switching REPL with Python preview mode. Switch between all 17 languages mid-session. Inspect generated Python, list keywords and operators.</p>
</div>

<div class="feature-card">
<span class="feature-icon">🔤</span>
<div class="feature-title">Surface Normalization</div>
<p class="feature-desc">SOV and RTL languages (Japanese, Arabic, Hindi, Bengali, Tamil) support natural word order through declarative surface normalization rules.</p>
</div>

<div class="feature-card">
<span class="feature-icon">🔢</span>
<div class="feature-title">Multilingual Numerals</div>
<p class="feature-desc">Support for Unicode numerals, Roman numerals, complex numbers, fractions, and scientific notation across scripts. Use the numeral system of your language.</p>
</div>

</div>
</section>

<!-- Supported Languages -->
<section class="home-section" markdown="1">
  <span class="section-eyebrow">Supported Languages</span>
  <h2 class="section-title">Featured Language Frontends</h2>
  <p class="section-desc">Each language is a full first-class frontend with localized keywords, error messages, builtins, and REPL support.</p>

<div class="lang-grid">
  <a href="{{ '/en/docs/language-guide/all-languages/#english' | relative_url }}" class="lang-pill">
    English <span class="lang-code">en</span>
  </a>
  <a href="{{ '/en/docs/language-guide/all-languages/#french' | relative_url }}" class="lang-pill">
    French <span class="lang-code">fr</span>
  </a>
  <a href="{{ '/en/docs/language-guide/all-languages/#spanish' | relative_url }}" class="lang-pill">
    Spanish <span class="lang-code">es</span>
  </a>
  <a href="{{ '/en/docs/language-guide/all-languages/#japanese' | relative_url }}" class="lang-pill">
    Japanese <span class="lang-code">ja</span>
  </a>
  <a href="{{ '/en/docs/language-guide/all-languages/#arabic' | relative_url }}" class="lang-pill">
    Arabic <span class="lang-code">ar</span>
  </a>
  <a href="{{ '/en/docs/language-guide/all-languages/#hindi' | relative_url }}" class="lang-pill">
    Hindi <span class="lang-code">hi</span>
  </a>
</div>
</section>

<!-- Quick Start -->
<section class="home-section" markdown="1">
  <span class="section-eyebrow">Quick Start</span>
  <h2 class="section-title">Get Running in 60 Seconds</h2>

**Install:**

```bash
# Minimal (Python backend only)
pip install multilingualprogramming

# Recommended (Python + WASM acceleration)
pip install multilingualprogramming[wasm]

# Maximum performance (Python + WASM + NumPy)
pip install multilingualprogramming[performance]
```

**Start the REPL:**

```bash
# Default (English)
python -m multilingualprogramming repl

# French
python -m multilingualprogramming repl --lang fr

# Japanese
python -m multilingualprogramming repl --lang ja

# With Python preview
python -m multilingualprogramming repl --show-python
```

**Run a file:**

```bash
python -m multilingualprogramming run myprogram.ml --lang en
python -m multilingualprogramming run programme.ml --lang fr
```

**Use as a library:**

```python
from multilingualprogramming import ProgramExecutor

executor = ProgramExecutor()
executor.execute("""
let x = 10
let y = 20
print(x + y)
""", language="en")
```

</section>

<!-- Pipeline overview -->
<section class="home-section" markdown="1">
  <span class="section-eyebrow">Architecture</span>
  <h2 class="section-title">Compilation Pipeline</h2>
  <p class="section-desc">Every program, in any language, follows the same forward-only pipeline to Python or WASM output.</p>

```
Surface Language (.ml file)
        │
        ▼
  ┌─────────────┐
  │    Lexer    │  Unicode-aware tokenization, keyword concept resolution
  └──────┬──────┘
         │ Concept tokens (COND_IF, LOOP_FOR, FUNC_DEF...)
         ▼
  ┌─────────────────┐
  │ Surface Normal. │  Optional: rewrite SOV/RTL word order to canonical
  └──────┬──────────┘
         │
         ▼
  ┌─────────────┐
  │   Parser    │  Build language-agnostic Core AST
  └──────┬──────┘
         │
         ▼
  ┌─────────────────┐
  │  Core IR Wrap   │  CoreIRProgram (typed container with metadata)
  └──────┬──────────┘
         │
         ▼
  ┌──────────────────┐
  │ SemanticAnalyzer │  Scope, symbol, structural checks
  └──────┬───────────┘
         │
    ┌────┴────┐
    │         │
    ▼         ▼
┌───────┐ ┌─────────┐
│Python │ │   WAT   │  Code generation targets
│  Gen  │ │   Gen   │
└───┬───┘ └────┬────┘
    │           │
    ▼           ▼
┌───────┐ ┌──────────┐
│Python │ │ wasmtime │
│Runtime│ │ (→ .wasm)│
└───────┘ └──────────┘
```

<div style="margin-top:1.5rem">
  <a href="{{ '/en/docs/design/' | relative_url }}" class="btn btn-secondary">Read Architecture Docs &rarr;</a>
</div>
</section>
