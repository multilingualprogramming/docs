---
layout: page
title: "Standard Library Localization"
description: "How multilingual handles localization of built-in functions and library symbols."
category: "Design"
permalink: /design/stdlib-localization/
prev_page:
  title: "Surface Normalization"
  url: /design/surface-normalization/
next_page:
  title: "Related Work"
  url: /design/related-work/
---

This document explains how multilingual handles localization beyond core syntax keywords — specifically for Python built-in functions, standard library symbols, and the policies governing how aliases interact with canonical names.

---

## The Problem

Localizing syntax keywords (like `if`, `for`, `def`) is straightforward compared to localizing library symbols such as `print`, `range`, `len`, and module APIs.

Library-level localization raises deeper questions:
- Should `print` be renamed `afficher` in French programs?
- Should `math.sqrt` become `mathématiques.racine_carrée`?
- What happens when localized names collide across languages?

---

## Scope Layers

multilingual distinguishes three layers of localization:

| Layer | Examples | Approach |
|-------|---------|----------|
| **Language keywords** | `if`, `for`, `def`, `return` | Full localization via concept mapping |
| **Core built-ins** | `print`, `range`, `len`, `sum` | Localized **aliases** (additive only) |
| **Library APIs** | `math.sqrt`, `os.path.join` | Canonical Python names retained |

---

## Current Behavior

### Keywords — Fully Localized

Grammar-level keywords are mapped via the Universal Semantic Model (USM). Every supported language has its own surface form for `COND_IF`, `LOOP_FOR`, `FUNC_DEF`, and all 51 semantic concepts.

```python
# English
if x > 0:
    print(x)

# French (fully localized keywords)
si x > 0:
    afficher(x)

# Japanese (fully localized)
もし x > 0:
    表示(x)
```

### Built-in Aliases — Additive

Selected built-in functions support localized **aliases**. The canonical English name is always available; aliases are additive:

```python
# English universal name — works in any language
print(range(5))
len([1, 2, 3])
sum([1, 2, 3])

# French aliases — also work
afficher(intervalle(5))
longueur([1, 2, 3])
somme([1, 2, 3])

# Both work in the same French program!
soit items = [1, 2, 3]
afficher(longueur(items))   # French alias
print(len(items))           # Universal name — still valid
```

### Library APIs — Canonical Only

Python standard library module/member names are **not** localized:

```python
import math
print(math.sqrt(16))    # Canonical — works in all languages

# math.racine_carrée is NOT supported
# math.квадратный_корень is NOT supported
```

This applies to:
- `math`, `os`, `sys`, `re`, `json`, `datetime`, etc.
- All third-party packages
- All `from module import name` imports

---

## Compatibility Policy

The governing rule is: **canonical Python names are the interoperability baseline**.

1. **Localized aliases are additive** — they never remove or shadow canonical names
2. **If a conflict exists, the canonical name wins** for deterministic behavior
3. **Universal English names always work** in every language mode

This policy preserves:
- Compatibility with Python ecosystem documentation and tutorials
- Ability to mix multilingual authoring with standard Python API usage
- Predictable behavior when copying code between language modes

---

## The 41 Built-in Aliases

These are the built-ins that currently have localized aliases across the 17 supported languages:

### Core I/O
`print`, `input`, `open`

### Sequence Operations
`range`, `len`, `sum`, `sorted`, `reversed`, `enumerate`, `zip`, `map`, `filter`

### Math
`abs`, `min`, `max`, `round`, `pow`, `divmod`

### Type Functions
`type`, `isinstance`, `issubclass`, `repr`, `str`, `int`, `float`, `bool`

### Collections
`list`, `dict`, `set`, `tuple`, `frozenset`, `bytes`

### Introspection
`dir`, `hasattr`, `getattr`, `setattr`, `delattr`, `callable`, `hash`

### Iteration
`iter`, `next`, `any`, `all`

### String/Encoding
`chr`, `ord`, `format`

See [Built-in Aliases Reference](/reference/builtins/) for the complete table across all languages.

---

## Adding Built-in Aliases

Aliases are defined in:

```
multilingualprogramming/resources/usm/builtins_aliases.json
```

Structure:

```json
{
  "print": {
    "fr": "afficher",
    "es": "imprimir",
    "de": "ausgeben",
    "ja": "表示",
    "ar": "اطبع",
    "hi": "छापो",
    "zh": "打印"
  },
  "range": {
    "fr": "intervalle",
    "es": "rango",
    ...
  }
}
```

Guidelines for adding new aliases:
- Must be complete and unambiguous in the target language
- Must not conflict with existing Python keywords or other aliases in the same language
- Must pass collision detection (see [Translation Guidelines](/extending/translation/))
- Should use full natural words, not abbreviations

---

## Open Questions

The following policy decisions are still under discussion:

1. **Opt-in stdlib wrappers**: Should there be opt-in localized wrappers for selected stdlib modules (e.g., a `mathématiques` module wrapping `math` in French)?

2. **Alias collision resolution**: When the same localized word could map to multiple concepts across languages (e.g., `tipo` in Spanish could refer to both `type` and a user-defined function), how should collisions be resolved?

3. **Error message presentation**: Should runtime errors display the canonical Python name, the localized alias, or both?

4. **Module-level localization**: Is there value in allowing `import mathématiques` as an alias for `import math` in French mode?

These questions are tracked in the [GitHub Issues](https://github.com/johnsamuelwrites/multilingual/issues) for community discussion.

---

## Design Rationale

The current approach — full keyword localization + additive built-in aliases + canonical library names — reflects three priorities:

**1. Python ecosystem compatibility**

Keeping library names canonical means multilingual programs can interoperate with any Python documentation, tutorial, or Stack Overflow answer without translation friction. A French developer learning from a Python tutorial can use `math.sqrt()` directly.

**2. Reduced ambiguity**

Additive aliases avoid the risk of a localized name shadowing something meaningful. If `somme` (French for `sum`) is defined as a variable by the user, both `somme` (the variable) and `sum` (the built-in) remain accessible.

**3. Deterministic behavior**

When canonical names always win in conflicts, behavior is predictable across all language modes. A program that works correctly in English mode will produce the same results in French mode — the test suite validates this guarantee (858 tests across 78 suites).
