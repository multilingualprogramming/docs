---
layout: page
title: "Frontend Contracts"
description: "How language frontends relate to the shared core — translation function, goals, and validation."
category: "Design"
permalink: /design/frontend-contracts/
prev_page:
  title: "Core Specification"
  url: /design/core-spec/
next_page:
  title: "Surface Normalization"
  url: /design/surface-normalization/
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

```python
from multilingualprogramming.core.lowering import lower_to_core_ir

core = lower_to_core_ir(ast, source_language="fr")
# core.ast — the Program node
# core.source_language — "fr"
# core.core_version — "0.1"
```

---

## Validation Strategy

Frontend contracts are validated through a **test-centric approach**:

### 1. Parser Equivalence Tests

Compare `ASTPrinter` output for equivalent programs in different languages:

```python
# tests/frontend_equivalence_test.py

def get_ast_repr(source: str, language: str) -> str:
    lexer = Lexer(language=language)
    parser = Parser(language=language)
    tokens = lexer.tokenize(source)
    ast = parser.parse(tokens)
    printer = ASTPrinter()
    return printer.print(ast)

def test_let_equivalence():
    en_ast = get_ast_repr("let x = 42", "en")
    fr_ast = get_ast_repr("soit x = 42", "fr")
    ja_ast = get_ast_repr("変数 x = 42", "ja")
    ar_ast = get_ast_repr("ليكن x = 42", "ar")

    assert en_ast == fr_ast == ja_ast == ar_ast
```

### 2. Runtime Equivalence Tests

Compare final program output across language pairs:

```python
def execute_and_capture(source: str, language: str) -> str:
    import io, sys
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()
    ProgramExecutor().execute(source, language=language)
    output = sys.stdout.getvalue()
    sys.stdout = old_stdout
    return output

def test_output_equivalence():
    programs = {
        "en": "let x = 10\nlet y = 20\nprint(x + y)",
        "fr": "soit x = 10\nsoit y = 20\nafficher(x + y)",
        "ja": "変数 x = 10\n変数 y = 20\n表示(x + y)",
        "ar": "ليكن x = 10\nليكن y = 20\naطبع(x + y)",
    }
    outputs = {lang: execute_and_capture(src, lang) for lang, src in programs.items()}
    assert len(set(outputs.values())) == 1  # All outputs identical
```

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
