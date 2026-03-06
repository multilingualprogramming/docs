---
page_id: design__frontend_contracts
locale: en
title: Frontend Contracts
path_segments:
- design
- frontend-contracts
source_hash: 2a5dd692fb4e
status: source
permalink: /en/docs/design/frontend-contracts/
---

This document specifies how language frontends relate to the shared Core AST and what contracts they must satisfy.

---

## The Translation Function

For each supported language `lang`, define a translation function:

```
T_lang: CS_lang → CoreAST
```

Where:
- `CS_lang` is concrete syntax in that language (source text using localized keywords)
- `CoreAST` is the shared parser AST (`multilingualprogramming/parser/ast_nodes.py`)

---

## Contract Goals

Each frontend must satisfy three goals:

### 1. Compositional Mapping

Syntax constructs map predictably into core nodes. Sub-expressions map independently.

```
T_lang(if E then S) = IfStmt(T_lang(E), T_lang(S))
T_lang(let x = E)  = LetDecl("x", T_lang(E))
T_lang(f(a, b))    = Call(T_lang(f), [T_lang(a), T_lang(b)])
```

No non-local effects: the translation of an expression does not depend on surrounding context (only scope, which is handled by SemanticAnalyzer).

### 2. Conservative Extension

Frontend-specific surface variants normalize into **existing** core constructs, not new semantics.

**Good** (conservative):
```
# Japanese natural for-loop → existing ForStmt core node
範囲(4) 内の 各 i に対して:  →  ForStmt(target="i", iterable=Call("range", [4]))
```

**Not allowed** (breaking):
```
# Would require a new core node
repeat 5 times:  →  RepeatStmt(5, block)  # RepeatStmt doesn't exist in core
```

If a new surface form requires a fundamentally new semantic concept, the core must be extended first (with design discussion and backward-compatibility analysis), not the frontend.

### 3. Semantics-Preserving Embedding

Equivalent constructs in different frontends execute identically after lowering and codegen.

```
T_en("let x = 42")    → LetDecl("x", Number(42))
T_fr("soit x = 42")   → LetDecl("x", Number(42))
T_ja("変数 x = 42")   → LetDecl("x", Number(42))
T_ar("ليكن x = 42")   → LetDecl("x", Number(42))
```

All four produce the **same** `CoreAST` → **same** Python output → **same** execution behavior.

---

## Non-Goals

These are explicitly **not** required of frontends:

- **Round-trip reconstruction**: No requirement to reconstruct original surface form from `CoreAST`
- **Full natural-language understanding**: Frontends parse controlled keyword-based subsets only
- **Morphological analysis**: Keywords are fixed tokens, not inflected forms

---

## Current Mechanisms

### Concept-Keyword Registry

**File**: `resources/usm/keywords.json`

The registry maps semantic concepts to language-specific surface keywords:

```json
{
  "COND_IF": {
    "en": "if",
    "fr": "si",
    "ja": "もし",
    "ar": "إذا"
  }
}
```

The `Lexer` uses `KeywordRegistry` to resolve surface keywords to concept tokens. The `Parser` grammar operates on concept tokens only — it never sees surface keywords.

### Surface Normalization

**File**: `resources/usm/surface_patterns.json`

For SOV and RTL languages, declarative rules normalize alternate word order before parsing:

```
Japanese natural form:  範囲(4) 内の 各 i に対して:
Normalized to concept:  LOOP_FOR i IN range(4):
```

This keeps the parser grammar unified while supporting natural word order in applicable languages.

### Core IR Wrapping

**File**: `multilingualprogramming/core/lowering.py`

After parsing, `lower_to_core_ir` wraps the raw AST in a `CoreIRProgram`:

{{snippet:design__frontend_contracts__py01}}

---

## Validation Strategy

Frontend contracts are validated through a **test-centric approach**:

### 1. Parser Equivalence Tests

Compare `ASTPrinter` output for equivalent programs in different languages:

{{snippet:design__frontend_contracts__py02}}

### 2. Runtime Equivalence Tests

Compare final program output across language pairs:

{{snippet:design__frontend_contracts__py03}}

### 3. Keyword Completeness Checks

Enforce all 51 concepts have translations for every supported language:

```bash
python -m multilingualprogramming smoke --all
python -m pytest tests/keyword_registry_test.py -v
```

---

## Adding a New Frontend

When adding language `xx`:

1. Satisfies completeness: all 51 concepts must be defined in `keywords.json`
2. Satisfies uniqueness: no two concepts share the same surface keyword in `xx`
3. Satisfies compositionality: each concept keyword maps to exactly one concept
4. (If adding surface patterns): patterns are narrow, tested, and non-overlapping

See [Adding a Language](/extending/) for the full checklist.
