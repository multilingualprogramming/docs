---
layout: page
title: "Related Work"
description: "How multilingual relates to prior work in programming language design, multi-frontend compilers, and controlled natural language."
category: "Design"
permalink: /design/related-work/
prev_page:
  title: "Surface Normalization"
  url: /design/surface-normalization/
---

multilingual is positioned at the intersection of:

- Multi-frontend compilation into a shared core
- Syntax extensibility and macro-style surface design
- Controlled natural-language-inspired frontend design

It does not claim novelty for the general idea of many languages mapping to one core. The contribution is a **coordinated multilingual frontend family** with grammar-sensitive normalization targeting one formal core.

---

## 1. Multi-Frontend Core and IR Work

Established systems already map multiple source languages to shared internal representations:
- **LLVM IR ecosystem** — many source languages (C, C++, Rust, Swift) → LLVM IR → native code
- **GCC internals** — GIMPLE/RTL intermediate representations
- **Core calculi** — lambda calculus, System F in language theory

**Alignment with multilingual:**
- Many-to-one mapping from surface language to shared core
- Separation of frontend concerns from backend/codegen

**Difference in focus:**
- multilingual coordinates multiple **natural-language-inspired** frontend variants within one family, rather than unrelated general-purpose languages

---

## 2. Syntactic Extensibility and Macro Ecosystems

Work on pluggable syntax and macro systems demonstrates that one semantic core can support many surface forms:

- **Racket `#lang`** — selects a language that controls module parsing at both reader and expander levels; supports packaging/installing new languages
- **Macro-centric language extension** — Lisp-style macro systems, syntax-skin approaches
- **SweetJS** — syntactic macros for JavaScript

In Racket specifically, `#lang` is a strong precedent for architecture where language identity is explicit at the module boundary while implementation is shared.

**Alignment with multilingual:**
- Core-first architecture
- Syntactic variation layered on stable semantics

**Difference in focus:**
- multilingual emphasizes multilingual human-language frontends and data-driven onboarding, not a general macro metaprogramming framework
- Localization is the primary motivation, not syntactic extension for its own sake

---

## 3. Controlled Language, NLP Boundaries, and Logic

Community feedback correctly highlights that once syntax approaches natural language, the hard problems shift from classic parsing to linguistic ambiguity, morphology, and intent extraction.

**Related work:**
- **ACE (Attempto Controlled English)** — formal CNL with logical semantics
- **Attempto** — controlled English → first-order logic
- **Common Logic** — ISO standard for sharing and transporting logic
- **Gellish** — formal language for industry knowledge

**multilingual's stance:**
- Explicitly controlled subsets per language (CNL-style)
- Declarative and test-backed normalization rules
- Deterministic parsing and forward compilation
- No claim of full natural-language understanding

---

## 4. Non-English Programming Languages

Several projects have explored non-English programming languages:

- **Hedy** — gradual programming language for education, supports Dutch, Arabic, Portuguese, and others. Focused on beginners.
- **ALGOL 68** — designed with publication forms in multiple languages (English, Russian, German, French). One of the earliest multilingual language specifications.
- **Rouille** — Rust syntax in French (source transformation)
- **Arabic-script Python variants** — various research prototypes
- **Non-English-based programming languages** (Wikipedia list) — historical survey

**Alignment with multilingual:**
- Same motivation: programming language accessibility across language communities
- Non-English keywords as first-class language features

**Difference in focus:**
- multilingual targets a **shared formal core** with 17 concurrent frontends
- Not a single-language alternative, but a unified framework for many
- Not beginner-only (targets Python-like subset)

---

## 5. Education and Accessibility

- **Scratch** — visual, multilingual interface; keyword localization via interface
- **Snap!** — blocks-based, multilingual
- **Processing** — has been adapted for non-English teaching contexts

multilingual differs in targeting a **text-based** programming model with a **formal core**, not a visual/blocks interface.

---

## Boundary Clarification

multilingual's architecture explicitly draws the boundary at:

```
Parsing/frontends:        CS_lang → CoreAST
Core typing boundary:     CoreAST → CoreIRProgram
Codegen/runtime:          CoreIRProgram → Python → execution
```

The project deliberately does **not** promise:
- Lossless round-trip from core to original surface syntax
- Full natural-language understanding
- Semantic equivalence claims beyond what tests cover

---

## Community Discussion

- [Reddit: multilingual — a programming language with one formal core](https://www.reddit.com/r/ProgrammingLanguages/comments/1r860hw/multilingual_a_programming_language_with_one/)
- [Reddit r/Compilers: How far can you decouple a programming language's surface syntax from its semantic core?](https://www.reddit.com/r/Compilers/comments/1r9q6rt/how_far_can_you_decouple_a_programming_languages/)

---

## References

| Project | URL |
|---------|-----|
| Hedy | [hedy.org](https://www.hedy.org/) |
| ALGOL 68 | [Wikipedia](https://en.wikipedia.org/wiki/ALGOL_68) |
| Non-English programming languages | [Wikipedia](https://en.wikipedia.org/wiki/Non-English-based_programming_languages) |
| Rouille | [github.com/bnjbvr/rouille](https://github.com/bnjbvr/rouille) |
| Racket `#lang` guide | [docs.racket-lang.org](https://docs.racket-lang.org/guide/hash-languages.html) |
| multilingual GitHub | [github.com/johnsamuelwrites/multilingual](https://github.com/johnsamuelwrites/multilingual) |
