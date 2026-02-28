---
layout: page
title: "Controlled Language Scope"
description: "Why multilingual uses controlled language subsets and what this means for language design."
category: "Extending"
permalink: /extending/cnl-scope/
prev_page:
  title: "Translation Guidelines"
  url: /extending/translation/
---

multilingual uses **controlled natural language (CNL) subsets**, not unconstrained natural language.

---

## Why Controlled Language?

Natural language introduces:
- **Ambiguity** — the same word can have multiple meanings
- **Morphology** — inflected forms (verb conjugations, plurals, case endings)
- **Cultural variability** — idioms, register, context-dependent meaning
- **Synonymy** — many words for the same concept

To keep compilation **deterministic**, each frontend supports a **constrained surface**. This means:

- Every token maps to exactly one concept
- No disambiguation heuristics at parse time
- No morphological analysis required
- Predictable behavior for every program

---

## What's In Scope

### Concept-Keyword Mappings

Each semantic concept maps to exactly one keyword per language:

```
COND_IF → "if" (en) / "si" (fr) / "wenn" (de) / "もし" (ja) / "إذا" (ar)
```

One keyword per concept per language. No synonyms, no variants (except diacritic aliases).

### Finite Built-in Alias Sets

Localized aliases for a curated set of built-in functions:
- 41 concepts currently localized
- Each maps to exactly one alias per language
- Universal English names always available alongside aliases

### Finite Declarative Surface Normalization Patterns

For SOV/RTL languages, declarative rules handle alternate word orders:
- Rules are finite and enumerable
- Each rule is tested and narrowly scoped
- No open-ended pattern matching

### Deterministic Parse and Execution

Same program in language X always produces same output as same program in language Y.

---

## What's Out of Scope

### Open-Ended Intent Extraction

Not supported:
```
# This is NOT a valid multilingual program
print the sum of all numbers from one to ten
```

multilingual is not a natural language programming system. Programs must use explicit keywords.

### Free-Form Conversational Programming

```
# NOT supported
Add a function that greets users
```

### Full Morphology and Synonym Resolution

```
# In French, all of these would mean the same thing in natural French,
# but only the canonical keyword is accepted:
afficher(x)     # canonical alias — ACCEPTED
montrer(x)      # synonym — NOT accepted as a builtin alias
montrez(x)      # conjugated form — NOT accepted
```

Only the registered keyword form is recognized. This prevents ambiguity.

### Arbitrary Grammar Extensions

Surface normalization patterns must be:
1. Narrowly scoped (minimal pattern footprint)
2. Test-backed (executor tests for each form)
3. Non-overlapping (no ambiguity between rules)
4. Based on actual linguistic usage (native speaker input preferred)

---

## Ambiguity Policy

**Prefer explicit token-level concepts over heuristic interpretation.**

1. Conflicting keyword mappings are **disallowed** by validation/tests
2. Surface patterns are added incrementally with dedicated tests
3. When in doubt, reject the form rather than guess intent

**Example of an ambiguous form (rejected):**

```
# In Spanish, "para" could be:
# - LOOP_FOR ("for" loop)
# - PREP ("for" preposition, e.g., "para ti" = "for you")
```

In multilingual Spanish, `para` is defined as `LOOP_FOR`. If used in a non-loop context where it appears as an argument, the lexer still tokenizes it as `LOOP_FOR`. This is intentional — the controlled subset avoids contexts where `para` would be ambiguous.

---

## Practical Authoring Rule

When onboarding a language:

**Accept only forms that can be specified and tested as stable grammar rules.**

**Reject forms that require:**
- Broad NLP inference
- Context-sensitive disambiguation
- Morphological analysis
- Semantic role labeling

**Test before you accept.** If a surface form requires a special-case rule to parse, add a specific test for it. If the rule is too broad or overlapping, narrow it.

---

## Connection to Related Work

The CNL approach is related to:
- **Controlled Natural Language (CNL)** research — constrained subsets of natural languages with formal semantics
- **Racket #lang** — explicit language selection at module boundary, shared semantic core
- **ALGOL 68** — multiple publication languages mapping to one formal definition

See [Related Work](/design/related-work/) for more context.

---

## Evolution

The CNL scope boundary may evolve:

- **More surface patterns** — expanding the set of accepted natural forms for existing languages
- **More aliases** — additional localized built-in aliases beyond the current 41
- **New language packs** — subject to same CNL rules

What will not change:
- The requirement for deterministic parsing
- The prohibition on open-ended NLP
- The single-keyword-per-concept-per-language rule
