---
layout: page
title: "Design & Architecture"
description: "Architecture overview of multilingual — layered model, compilation pipeline, and design principles."
category: "Design"
permalink: /design/
next_page:
  title: "Core Specification"
  url: /design/core-spec/
---

This document explains how multilingual works at a design level. It is intended for contributors, language-onboarding authors, and curious users.

---

## Design Goals

1. **One formal core** — All language frontends compile to the same Core AST and `CoreIRProgram`
2. **Forward-only compilation** — `CS_lang → CoreAST → CoreIRProgram → Python/WASM`
3. **Concept-driven keywords** — Localization maps to semantic concepts, not raw tokens
4. **Data-driven extensibility** — Languages added via JSON, not grammar rewrites
5. **Conservative extension** — Language-specific variants normalize to existing core concepts
6. **Deterministic parsing** — Controlled language scope prevents ambiguity

---

## Layered Model

The implementation is structured as four explicit layers:

```
Layer 1: Concrete Surface Syntax (CS_lang)
         Language-specific source text
         "let x = 42"  /  "soit x = 42"  /  "変数 x = 42"
              │
              ▼
Layer 2: Shared Core AST
         Language-agnostic parser output (ast_nodes.py)
         Program([LetDecl("x", Number(42))])
              │
              ▼
Layer 3: Typed Core IR Container
         CoreIRProgram (core/ir.py)
         { ast: Program, source_language: "en", core_version: "0.1" }
              │
              ▼
Layer 4: Target Code Generation
         Python source / WASM binary
         x = 42
```

This makes boundary questions explicit:
- **Parsing**: maps `CS_lang` → Core AST
- **Code generation**: consumes `CoreIRProgram`, not raw source text

---

## Compilation Pipeline

```
Source File (.ml)
      │  language="fr"
      ▼
┌──────────────────┐
│  KeywordRegistry │  Load JSON keyword mappings
│  (resources/)    │  concept "COND_IF" → "si" (fr)
└──────┬───────────┘
       │
       ▼
┌──────────────────┐
│     Lexer        │  Tokenize Unicode source
│  (lexer.py)      │  Resolve surface keywords → concept tokens
│                  │  "si" → COND_IF concept token
└──────┬───────────┘
       │  token stream (concept tokens)
       ▼
┌──────────────────┐
│ SurfaceNormal.   │  Optional: rewrite SOV/RTL word order
│ (surface_norm.)  │  "範囲(4) 内の 各 i に対して:" → "毎 i 中 範囲(4):"
└──────┬───────────┘
       │  normalized token stream
       ▼
┌──────────────────┐
│     Parser       │  Build language-agnostic Core AST
│  (parser.py)     │  grammar operates on concept tokens only
└──────┬───────────┘
       │  Core AST (Program node)
       ▼
┌──────────────────┐
│  lower_to_core   │  Wrap AST in typed CoreIRProgram
│  (core/lowering) │  { ast, source_language, core_version }
└──────┬───────────┘
       │  CoreIRProgram
       ▼
┌──────────────────┐
│ SemanticAnalyzer │  Check scopes, symbols, structural constraints
│ (semantic_anal.) │  Multilingual error messages
└──────┬───────────┘
       │  validated CoreIRProgram
       ▼
    ┌──┴──┐
    │     │
    ▼     ▼
┌───────┐ ┌────────┐
│Python │ │  WASM  │  Code generation targets
│Code   │ │  Code  │
│Gen.   │ │  Gen.  │
└───┬───┘ └───┬────┘
    │         │
    ▼         ▼
┌───────┐ ┌──────────────┐
│Python │ │  Cranelift   │
│Runtime│ │  Compiler    │
│(exec) │ │  → .wasm     │
└───────┘ └──────────────┘
```

---

## Keyword Localization Model

Localization is **concept-driven**, not grammar-driven.

### Universal Semantic Model (USM)

```json
{
  "keywords": {
    "control_flow": {
      "COND_IF": {
        "en": "if",
        "fr": "si",
        "de": "wenn",
        "ja": "もし",
        "ar": "إذا",
        "hi": "अगर",
        "zh": "如果"
      },
      "LOOP_FOR": {
        "en": "for",
        "fr": "pour",
        "de": "für",
        "ja": "毎",
        "ar": "لكل",
        "hi": "के_लिए",
        "zh": "对于"
      }
    }
  }
}
```

**Why this works:**

1. `keywords.json` lists all 17 languages per concept
2. `KeywordRegistry` loads this file dynamically
3. `Lexer` resolves concrete keywords to concepts via `KeywordRegistry`
4. `Parser` operates on concepts — grammar logic is shared across all languages
5. `PythonCodeGenerator` emits Python concepts — code generation is language-agnostic

Adding a new language requires only updating `keywords.json` (and related JSON files). No parser rewrites.

---

## Identifier Interoperability

Identifiers are **Unicode-aware** and are **not translated**.

- Keywords are localized (concept-mapped)
- User-defined names stay exactly as written
- Mixed scripts are allowed (Latin + Devanagari + CJK in one file)

**Rule of thumb:**
- Semantic keywords → normalized to concepts
- Identifiers → remain exact user symbols

A French-keyword file can call a function named in English (or any script), as long as names match. There is no automatic translation of identifiers.

---

## Frontend Contract

Each language frontend is a translation function:

```
T_lang: CS_lang → CoreAST
```

**Goals:**
1. **Compositional** — sub-expressions map independently
2. **Conservative extension** — language forms normalize to existing core constructs
3. **Semantics-preserving** — same program in different languages → identical behavior

**Forward-only property:**

The system guarantees:

```
CS_lang → CoreAST → CoreIRProgram → Python
```

It does **not** guarantee lossless round-tripping from core back to original surface source.

---

## Surface Normalization

Some languages have natural word order that differs from the positional grammar shared by all frontends. The surface normalizer handles this transparently.

### Mechanism

```
Lexer output (concept tokens)
        │
        ▼ Surface Normalizer reads tokens
┌──────────────────────────────────────────┐
│  Match token-level surface patterns      │
│  Capture slots (target, iterable, ...)   │
│  Rewrite to canonical concept order      │
└──────────────────────────────────────────┘
        │ canonical token stream
        ▼
    Parser (unchanged)
```

### Example: Japanese for loop

Natural Japanese form (iterable-first, SOV order):
```python
範囲(6) 内の 各 i に対して:
    表示(i)
```

Canonical multilingual form:
```python
毎 i 中 範囲(6):
    表示(i)
```

Both are accepted. The surface normalizer rewrites the first to the second before parsing.

### Surface Pattern Configuration

Patterns are defined in `resources/usm/surface_patterns.json`:

```json
{
  "templates": {
    "for_iterable_first": [
      { "kind": "keyword", "concept": "LOOP_FOR" },
      { "kind": "identifier_slot", "slot": "target" },
      { "kind": "keyword", "concept": "IN" },
      { "kind": "expr_slot", "slot": "iterable" },
      { "kind": "delimiter", "value": ":" }
    ]
  },
  "patterns": [
    {
      "name": "ja_for_iterable_first",
      "language": "ja",
      "normalize_template": "for_iterable_first",
      "pattern": [
        { "kind": "expr", "slot": "iterable" },
        { "kind": "literal", "value": "内の" },
        { "kind": "literal", "value": "各" },
        { "kind": "identifier", "slot": "target" },
        { "kind": "literal", "value": "に対して" },
        { "kind": "delimiter", "value": ":" }
      ]
    }
  ]
}
```

Current pilot rules: iterable-first `for` loops for Japanese, Arabic, Spanish, Portuguese, Hindi, Bengali, Tamil.

---

## Core IR

```python
# multilingualprogramming/core/ir.py

@dataclass
class CoreIRProgram:
    ast: Program              # The parsed AST
    source_language: str      # e.g., "fr", "ja", "ar"
    core_version: str = "0.1"
    frontend_metadata: dict = field(default_factory=dict)
```

**Validation rules** (`CoreIRProgram`):
1. `ast` must be a `Program` node
2. `source_language` must be a non-empty string

**Planned extensions:**
- Statement/expression sort checks
- Typed annotation consistency checks
- Lowering invariants for restricted subsets

---

## Runtime Builtins

`RuntimeBuiltins` injects localized aliases into the execution namespace:

```python
# Execution namespace includes:
{
    # Universal names (always available)
    "print": print,
    "range": range,
    "len": len,
    # ...

    # Localized aliases (per language)
    "afficher": print,          # fr
    "intervalle": range,        # fr
    "longueur": len,            # fr
    # ...
}
```

Aliases are **additive** — canonical names are never removed. Both `print` and `afficher` work in a French program.

---

## Design Decisions

### Why not full natural language?

Natural language introduces ambiguity, morphology, and cultural variability. Deterministic compilation requires controlled subsets (CNL-style). The project explicitly does not promise full NLP or conversational programming.

### Why not per-language grammars?

Separate grammars per language would fragment the parser, make semantic analysis harder, and break cross-language equivalence. The concept-driven model keeps the parser unified while allowing diverse surface syntax.

### Why Python as the target?

Python is widely understood, has rich ecosystem support, and provides an executable runtime compatible with most existing tooling. WASM is an additional target for performance-critical paths.

### Why data-driven (JSON) keyword mappings?

JSON-based keyword files allow community contributors to add new languages without modifying Python source code. Validation is enforced at load time, keeping the main codebase stable.

---

## File Map

| File | Purpose |
|------|---------|
| `multilingualprogramming/resources/usm/keywords.json` | Keyword concept → language mappings |
| `multilingualprogramming/resources/usm/builtins_aliases.json` | Builtin aliases per language |
| `multilingualprogramming/resources/usm/operators.json` | Operator mappings |
| `multilingualprogramming/resources/usm/surface_patterns.json` | Surface normalization rules |
| `multilingualprogramming/resources/parser/error_messages.json` | Localized error messages |
| `multilingualprogramming/resources/repl/commands.json` | REPL command localization |
| `multilingualprogramming/lexer/lexer.py` | Unicode tokenizer |
| `multilingualprogramming/parser/parser.py` | Core grammar parser |
| `multilingualprogramming/parser/ast_nodes.py` | AST node classes |
| `multilingualprogramming/parser/surface_normalizer.py` | Surface normalization engine |
| `multilingualprogramming/parser/semantic_analyzer.py` | Scope and symbol checks |
| `multilingualprogramming/core/ir.py` | CoreIRProgram definition |
| `multilingualprogramming/core/lowering.py` | AST → Core IR lowering |
| `multilingualprogramming/codegen/python_generator.py` | Python code generation |
| `multilingualprogramming/codegen/wasm_generator.py` | WASM code generation |
| `multilingualprogramming/runtime/backend_selector.py` | WASM/Python backend selection |
| `multilingualprogramming/runtime/python_fallbacks.py` | Pure Python WASM fallbacks |
