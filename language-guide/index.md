---
layout: page
title: "Language Guide"
description: "Complete guide to writing programs in multilingual — covering all 17 language frontends and every supported construct."
category: "Language Guide"
permalink: /language-guide/
next_page:
  title: "Syntax Reference"
  url: /language-guide/syntax/
---

The Language Guide covers all 17 supported human languages and the complete set of constructs you can use to write multilingual programs.

---

## How Languages Work

Every supported language is a **frontend** over the same semantic core. The compiler:

1. **Tokenizes** source with Unicode-aware lexer, resolving keywords to semantic concepts
2. **Normalizes** surface forms (handles SOV/RTL word order for Japanese, Arabic, etc.)
3. **Parses** concept tokens into a language-agnostic Core AST
4. **Analyzes** scope, symbols, and structural constraints
5. **Generates** Python or WASM output

The same program — in any language — produces identical behavior.

---

## Language Categories

### European Languages (SVO word order)

| Language | Code | Script |
|----------|------|--------|
| English | `en` | Latin |
| French | `fr` | Latin |
| Spanish | `es` | Latin |
| German | `de` | Latin |
| Italian | `it` | Latin |
| Portuguese | `pt` | Latin |
| Polish | `pl` | Latin |
| Dutch | `nl` | Latin |
| Swedish | `sv` | Latin |
| Danish | `da` | Latin |
| Finnish | `fi` | Latin |

### South Asian Languages

| Language | Code | Script | Word order |
|----------|------|--------|------------|
| Hindi | `hi` | Devanagari | SOV |
| Bengali | `bn` | Bengali | SOV |
| Tamil | `ta` | Tamil | SOV |

### Middle Eastern

| Language | Code | Script | Direction |
|----------|------|--------|-----------|
| Arabic | `ar` | Arabic | RTL |

### East Asian

| Language | Code | Script | Word order |
|----------|------|--------|------------|
| Chinese (Simplified) | `zh` | CJK | SVO |
| Japanese | `ja` | CJK + Kana | SOV |

---

## Sections in this Guide

<div class="card-grid">

<div class="card">
<a href="/language-guide/syntax/">
<span class="card-icon">📐</span>
<h3>Syntax Reference</h3>
<p>Complete syntax for every construct: variables, control flow, functions, classes, async, exceptions, comprehensions.</p>
</a>
</div>

<div class="card">
<a href="/language-guide/keywords/">
<span class="card-icon">🔑</span>
<h3>Keywords</h3>
<p>Full keyword table: all 51 semantic concepts across all 17 languages.</p>
</a>
</div>

<div class="card">
<a href="/language-guide/control-flow/">
<span class="card-icon">🔀</span>
<h3>Control Flow</h3>
<p>if/elif/else, for, while, match/case, break, continue with examples in every language.</p>
</a>
</div>

<div class="card">
<a href="/language-guide/functions-classes/">
<span class="card-icon">🏗️</span>
<h3>Functions & Classes</h3>
<p>def, class, decorators, inheritance, generators, lambdas — with all 17 language forms.</p>
</a>
</div>

<div class="card">
<a href="/language-guide/async-generators/">
<span class="card-icon">⚙️</span>
<h3>Async & Generators</h3>
<p>async def, await, async for, async with, yield, yield from.</p>
</a>
</div>

<div class="card">
<a href="/language-guide/all-languages/">
<span class="card-icon">🌐</span>
<h3>All 17 Languages</h3>
<p>Complete program examples in every supported language with full feature coverage.</p>
</a>
</div>

</div>
