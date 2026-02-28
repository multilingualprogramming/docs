---
layout: home
title: "Multilingual Programming Language"
description: "Write programs in 17 human languages. One formal core. Python and WASM backends."
permalink: /
---

<section class="hero">
  <span class="hero-eyebrow">v0.4.0 &mdash; Now with WASM &mdash; 17 Languages</span>
  <h1 class="hero-title">
    Write Code in<br/>
    <span class="gradient-text">Any Human Language</span>
  </h1>
  <p class="hero-description">
    <strong>multilingual</strong> is a programming language with one formal semantic core and 17 natural-language frontends. Write in English, French, Japanese, Arabic, Hindi, or 12 more &mdash; compile to Python or WASM.
  </p>
  <div class="hero-actions">
    <a href="/getting-started/" class="btn btn-primary">Get Started &rarr;</a>
    <a href="/language-guide/" class="btn btn-secondary">Language Guide</a>
    <a href="https://github.com/johnsamuelwrites/multilingual" class="btn btn-secondary" target="_blank" rel="noopener">View on GitHub</a>
  </div>
</section>

<div class="stats-strip">
  <div class="stat-item">
    <div class="stat-value">17</div>
    <div class="stat-label">Human Languages</div>
  </div>
  <div class="stat-item">
    <div class="stat-value">858</div>
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
    <div class="stat-value">0.4.0</div>
    <div class="stat-label">Current Version</div>
  </div>
</div>

<!-- Code demo -->
<section class="home-section" style="padding-top:3rem">
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
    <button class="code-tab" data-target="ja">Japanese</button>
    <button class="code-tab" data-target="ar">Arabic</button>
    <button class="code-tab" data-target="hi">Hindi</button>
    <button class="code-tab" data-target="zh">Chinese</button>
  </div>
  <div class="code-demo-body">
    <div class="code-panel" data-lang="en" style="display:block">

```python
let name = "world"
let count = 5

def greet(n):
    for i in range(count):
        print(f"Hello, {n}! iteration {i}")

greet(name)
```

</div>
    <div class="code-panel" data-lang="fr" style="display:none">

```python
soit nom = "monde"
soit compteur = 5

déf saluer(n):
    pour i dans intervalle(compteur):
        afficher(f"Bonjour, {n}! itération {i}")

saluer(nom)
```

</div>
    <div class="code-panel" data-lang="ja" style="display:none">

```python
変数 名前 = "世界"
変数 カウント = 5

関数 挨拶(n):
    毎 i 中 範囲(カウント):
        表示(f"こんにちは、{n}！ 繰り返し {i}")

挨拶(名前)
```

</div>
    <div class="code-panel" data-lang="ar" style="display:none">

```python
ليكن اسم = "العالم"
ليكن عداد = 5

دالة تحية(n):
    لكل i في مدى(عداد):
        اطبع(f"مرحبا، {n}! تكرار {i}")

تحية(اسم)
```

</div>
    <div class="code-panel" data-lang="hi" style="display:none">

```python
मान नाम = "दुनिया"
मान गिनती = 5

परिभाषा नमस्ते(n):
    के_लिए i में परास(गिनती):
        छापो(f"नमस्ते, {n}! पुनरावृत्ति {i}")

नमस्ते(नाम)
```

</div>
    <div class="code-panel" data-lang="zh" style="display:none">

```python
令 名字 = "世界"
令 计数 = 5

定义 问候(n):
    对于 i 里 范围(计数):
        打印(f"你好，{n}！迭代 {i}")

问候(名字)
```

</div>
  </div>
</div>

</section>

<!-- Features -->
<section class="home-section">
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
<div class="feature-title">858 Tests, 78 Suites</div>
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
<section class="home-section">
  <span class="section-eyebrow">Supported Languages</span>
  <h2 class="section-title">17 Language Frontends</h2>
  <p class="section-desc">Every language is a full first-class frontend with localized keywords, error messages, builtins, and REPL support.</p>

<div class="lang-grid">
  <a href="/language-guide/all-languages/#english" class="lang-pill">
    <span>🇬🇧</span> English <span class="lang-code">en</span>
  </a>
  <a href="/language-guide/all-languages/#french" class="lang-pill">
    <span>🇫🇷</span> French <span class="lang-code">fr</span>
  </a>
  <a href="/language-guide/all-languages/#spanish" class="lang-pill">
    <span>🇪🇸</span> Spanish <span class="lang-code">es</span>
  </a>
  <a href="/language-guide/all-languages/#german" class="lang-pill">
    <span>🇩🇪</span> German <span class="lang-code">de</span>
  </a>
  <a href="/language-guide/all-languages/#italian" class="lang-pill">
    <span>🇮🇹</span> Italian <span class="lang-code">it</span>
  </a>
  <a href="/language-guide/all-languages/#portuguese" class="lang-pill">
    <span>🇵🇹</span> Portuguese <span class="lang-code">pt</span>
  </a>
  <a href="/language-guide/all-languages/#polish" class="lang-pill">
    <span>🇵🇱</span> Polish <span class="lang-code">pl</span>
  </a>
  <a href="/language-guide/all-languages/#dutch" class="lang-pill">
    <span>🇳🇱</span> Dutch <span class="lang-code">nl</span>
  </a>
  <a href="/language-guide/all-languages/#swedish" class="lang-pill">
    <span>🇸🇪</span> Swedish <span class="lang-code">sv</span>
  </a>
  <a href="/language-guide/all-languages/#danish" class="lang-pill">
    <span>🇩🇰</span> Danish <span class="lang-code">da</span>
  </a>
  <a href="/language-guide/all-languages/#finnish" class="lang-pill">
    <span>🇫🇮</span> Finnish <span class="lang-code">fi</span>
  </a>
  <a href="/language-guide/all-languages/#hindi" class="lang-pill">
    <span>🇮🇳</span> Hindi <span class="lang-code">hi</span>
  </a>
  <a href="/language-guide/all-languages/#arabic" class="lang-pill">
    <span>🇸🇦</span> Arabic <span class="lang-code">ar</span>
  </a>
  <a href="/language-guide/all-languages/#bengali" class="lang-pill">
    <span>🇧🇩</span> Bengali <span class="lang-code">bn</span>
  </a>
  <a href="/language-guide/all-languages/#tamil" class="lang-pill">
    <span>🇮🇳</span> Tamil <span class="lang-code">ta</span>
  </a>
  <a href="/language-guide/all-languages/#chinese" class="lang-pill">
    <span>🇨🇳</span> Chinese <span class="lang-code">zh</span>
  </a>
  <a href="/language-guide/all-languages/#japanese" class="lang-pill">
    <span>🇯🇵</span> Japanese <span class="lang-code">ja</span>
  </a>
</div>
</section>

<!-- Quick Start -->
<section class="home-section">
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
<section class="home-section">
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
┌───────┐ ┌──────┐
│Python │ │ WASM │  Code generation targets
│  Gen  │ │  Gen │
└───┬───┘ └──┬───┘
    │         │
    ▼         ▼
┌───────┐ ┌──────────┐
│Python │ │ Cranelift│
│Runtime│ │ Compiler │
└───────┘ └──────────┘
```

<div style="margin-top:1.5rem">
  <a href="/design/" class="btn btn-secondary">Read Architecture Docs &rarr;</a>
</div>
</section>
