---
layout: page
title: "Surface Normalization"
description: "How multilingual handles SOV and RTL word order through declarative surface normalization rules."
category: "Design"
permalink: /design/surface-normalization/
prev_page:
  title: "Frontend Contracts"
  url: /design/frontend-contracts/
next_page:
  title: "Related Work"
  url: /design/related-work/
---

Surface normalization allows SOV (Subject-Object-Verb) and RTL (Right-to-Left) languages to use natural word order without forking the parser grammar.

---

## The Core Tension

multilingual uses:
- One shared parser grammar
- Concept-level keyword mapping
- Localized surface forms for those concepts

This optimizes for implementation consistency and cross-language semantic equivalence. However, a shared positional grammar **favors SVO word order** (English, French, etc.) over SOV languages (Japanese, Hindi, Arabic) where natural phrasing differs.

**Without normalization** (unnatural Japanese):
```python
毎 i 中 範囲(6):   # works but unnatural
    表示(i)
```

**With normalization** (natural Japanese):
```python
範囲(6) 内の 各 i に対して:   # natural SOV form, also accepted
    表示(i)
```

Both are accepted. Surface normalization rewrites the natural form to the canonical one before parsing.

---

## Mechanism

```
Lexer output (concept tokens)
        │
        ▼ SurfaceNormalizer reads token stream
┌──────────────────────────────────────────────────┐
│  1. Match token-level surface pattern             │
│  2. Capture named slots (target, iterable, ...)  │
│  3. Rewrite to canonical concept order            │
└──────────────────────────────────────────────────┘
        │ normalized token stream (canonical order)
        ▼
    Parser (unchanged grammar)
```

**Key properties:**
- Surface normalization runs **after** lexing, on concept tokens — not raw text
- It does **not** re-lex; it operates on the lexer's output
- The parser grammar is unchanged — normalization produces tokens the parser already understands

---

## Configuration

**File**: `multilingualprogramming/resources/usm/surface_patterns.json`

Two top-level sections:
- `templates` — reusable canonical rewrites
- `patterns` — language-scoped matching rules

### Pattern Structure

```json
{
  "name": "rule_name",
  "language": "ja",
  "normalize_template": "template_name",   // OR normalize_to
  "pattern": [
    { "kind": "expr", "slot": "iterable" },
    { "kind": "literal", "value": "内の" },
    { "kind": "literal", "value": "各" },
    { "kind": "identifier", "slot": "target" },
    { "kind": "literal", "value": "に対して" },
    { "kind": "delimiter", "value": ":" }
  ]
}
```

### Template Structure

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
  }
}
```

### Pattern Token Kinds

| Kind | Matches | Captures |
|------|---------|---------|
| `expr` | Any expression span | Into named slot |
| `identifier` | Single identifier token | Into named slot |
| `keyword` | Specific concept token | (required, not captured) |
| `delimiter` | Delimiter token (`:`, etc.) | (required, not captured) |
| `literal` | Literal token value (particles) | (required, not captured) |

### Output Token Kinds

| Kind | Emits |
|------|-------|
| `keyword` | Concept keyword token for the target language |
| `delimiter` | Delimiter token |
| `identifier_slot` | Captured identifier slot value |
| `expr_slot` | Captured expression slot tokens |

---

## Current Rules

### Japanese (`ja`) — Iterable-First For Loop

**Natural form:**
```python
範囲(6) 内の 各 i に対して:
    表示(i)
```

**Rule:** Matches `[iterable] 内の 各 [target] に対して :`

**Output:** `毎 [target] 中 [iterable] :` (canonical Japanese for loop)

**Parsed as:** `ForStmt(target="i", iterable=Call("range",[6]))`

---

### Arabic (`ar`) — Iterable-First For Loop

**Natural form:**
```python
لكل i في مدى(4):
    اطبع(i)
```

Arabic's natural form happens to already match the canonical pattern (`FOR target IN iterable:`), so minimal normalization is needed.

---

### Spanish (`es`) and Portuguese (`pt`) — Optional Iterable-First

**Natural form** (Spanish):
```python
para cada i en rango(4):
    imprimir(i)
```

**Canonical form** (also accepted):
```python
para i en rango(4):
    imprimir(i)
```

---

### Hindi (`hi`), Bengali (`bn`), Tamil (`ta`) — SOV Forms

These languages have SOV word order. Surface patterns handle:
- Iterable-first for loops
- Condition-first if statements

```python
# Hindi natural for loop
परास(4) में के_लिए i:   # iterable-first (SOV)
    छापो(i)

# Canonical (also accepted)
के_लिए i में परास(4):
    छापो(i)
```

---

## Authoring New Rules

### Workflow

1. Write 2–3 real source examples from native speakers
2. Tokenize with lexer tests to confirm particles tokenize as expected
3. Add the narrowest possible `pattern` for those forms
4. Rewrite via template or inline output to canonical concept order
5. Add parser + executor tests before adding more variants
6. Repeat with additional rules if needed

### Example: Adding a New Rule

```json
{
  "patterns": [
    {
      "name": "xx_for_natural",
      "language": "xx",
      "normalize_to": [
        { "kind": "keyword", "concept": "LOOP_FOR" },
        { "kind": "identifier_slot", "slot": "target" },
        { "kind": "keyword", "concept": "IN" },
        { "kind": "expr_slot", "slot": "iterable" },
        { "kind": "delimiter", "value": ":" }
      ],
      "pattern": [
        { "kind": "expr", "slot": "iterable" },
        { "kind": "literal", "value": "particle_a" },
        { "kind": "identifier", "slot": "target" },
        { "kind": "literal", "value": "particle_b" },
        { "kind": "delimiter", "value": ":" }
      ]
    }
  ]
}
```

### Validation Rules (enforced at load time)

- Rule must have exactly one of `normalize_to` or `normalize_template`
- All slots referenced in output must be captured in `pattern`
- `language` must be a supported language code
- No overlapping patterns for the same language and statement type

### Common Mistakes

| Mistake | Effect |
|---------|--------|
| `normalize_to` + `normalize_template` in same rule | `ValueError` at load |
| Output slot not in pattern | `ValueError` at load |
| Overly broad `expr` that matches multiple lines | Incorrect normalization |
| Missing `delimiter` in pattern | Failed match |

---

## Debugging Surface Normalization

If a surface form doesn't parse:

1. **Confirm lexer tokenization first:**
   ```python
   lexer = Lexer(language="ja")
   tokens = lexer.tokenize("範囲(4) 内の 各 i に対して:")
   for tok in tokens:
       print(f"{tok.type:20} {tok.value!r}")
   ```

2. **Add a parser unit test** for just the failing statement

3. **Check slot names** match exactly between pattern and output (`target` vs `iterator`)

4. **Verify template name** exists and is spelled exactly

5. **Ensure normalized sequence** is compatible with parser grammar

---

## Limitations

- Surface normalization applies to statement-level constructs only (for, while, if, with)
- Expression-level word order is not normalized (follows canonical order)
- Rules must be manually authored — no automatic inference from language data
- Full morphological variation (inflected particles) is not yet supported
