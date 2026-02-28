---
layout: page
title: "Translation Guidelines"
description: "Rules and standards for translating multilingual keywords and built-in names."
category: "Extending"
permalink: /extending/translation/
prev_page:
  title: "Add a Language"
  url: /extending/
next_page:
  title: "CNL Scope"
  url: /extending/cnl-scope/
---

This document defines the translation quality standards for multilingual keyword and built-in localization.

---

## Core Principles

### 1. Semantic Accuracy First

The translation must accurately convey the semantic meaning of the concept:
- `COND_IF` → a word meaning "if/conditional" in the target language
- `FUNC_DEF` → a word meaning "define/function definition"
- `RETURN` → a word meaning "return/give back"

Do not use literal word-for-word translations if they produce unnatural programming terms. Choose words that a programmer would recognize.

### 2. Prefer Full Words Over Abbreviations

| Prefer | Avoid |
|--------|-------|
| `afficher` (fr, "to show") | `aff` |
| `retourner` (fr, "to return") | `ret` |
| `importer` (fr, "to import") | `imp` |

Exception: if an abbreviation is the established programming convention in the target language (e.g., `def` is universal for function definition).

### 3. Diacritics Policy

**Prefer correct forms with diacritics:**

```json
"FUNC_DEF": { "fr": "déf" }   // preferred over "def"
```

**Allow ASCII aliases when diacritics are hard to type:**

```json
"FUNC_DEF": { "fr": ["déf", "def"] }
```

The first entry is the canonical form. ASCII aliases are additive.

### 4. Uniqueness Requirement

Keywords must be unambiguous within a language:
- No two concepts may share the same keyword in the same language
- Validation enforces this at load time via `KeywordValidator`

### 5. No Spaces in Keywords

Keywords must be identifier-safe:
- Use underscores for multi-word keywords: `de_lire` not `de lire`
- No special characters except underscores
- Must start with a letter or Unicode letter

---

## Language-Specific Guidelines

### European Languages (French, Spanish, German, Italian, etc.)

- Use infinitive verb forms for action keywords (`importer`, `retourner`)
- Use subjunctive or imperative where naturally used in programming contexts
- Keep gender-neutral forms where possible
- Test with native speakers or verified language learners

### Arabic (ar)

- Right-to-left script requires surface normalization rules
- Use Modern Standard Arabic (MSA) terminology
- Prefer technical/programming terminology used in Arab tech communities
- Pay attention to vowel markers (tashkeel) — omit them in keywords

### Hindi (hi) and South Asian Languages

- Use Devanagari script (Hindi), Bengali script (Bengali), Tamil script (Tamil)
- SOV word order requires surface normalization rules for loops/conditions
- Prefer Sanskrit-derived technical terms where they exist

### Chinese Simplified (zh)

- Use simplified characters
- Prefer single characters or short 2-character compounds
- Use established programming terminology from Chinese CS education

### Japanese (ja)

- SOV word order requires surface normalization
- Mix of Kanji, Hiragana, and Katakana is acceptable
- Katakana for technical/foreign-origin terms is common
- Native Japanese verbs for actions (戻る for "return", 表示 for "print")

---

## Collision and Ambiguity Detection

The `KeywordValidator` checks for:

1. **Duplicate keywords** within a language (two concepts with same keyword)
2. **Partial collisions** (keyword A is a prefix of keyword B, causing lexer ambiguity)
3. **Cross-concept confusion** (same keyword used for different semantic concepts)

Run validation:

```bash
python -m multilingualprogramming validate --lang xx
```

Or in Python:

```python
from multilingualprogramming.keyword import KeywordValidator

validator = KeywordValidator()
errors = validator.validate_language("xx")
for error in errors:
    print(error)
```

---

## Cross-Language Safety (False Friends)

When a word exists in multiple languages but with different meanings, ensure it maps to the correct concept in each:

| Word | Language | Correct concept |
|------|----------|----------------|
| `si` | French | `COND_IF` (if) |
| `si` | Spanish | `COND_IF` (if) |
| `se` | Italian | `COND_IF` (if) |
| `se` | Portuguese | `COND_IF` (if) |

In this case, the same surface token in different language modes maps to the same concept — which is safe.

**Dangerous case**: A word in language A that looks identical to a keyword in language B but has a different meaning:

```
"si" in French = "if" (COND_IF)
"si" in music = "B note" (completely different domain)
```

Since languages are mode-switched (one file = one language), this is not a collision issue in practice. But be careful when choosing keywords that could confuse multi-lingual users.

---

## Built-in Aliases

### Rules for Builtin Aliases

1. **Additive only** — Universal English names remain usable in all languages
2. **No semantic change** — Aliases must call exactly the same built-in function
3. **One canonical alias per language** per builtin (multiple OK if diacritics policy applies)
4. **Prefer verb forms** for action builtins (`afficher` for print, `retourner` not applicable to builtins)

### Builtin Translation Table (Key Examples)

| Builtin | French | Spanish | German | Japanese | Arabic | Hindi |
|---------|--------|---------|--------|----------|--------|-------|
| `print` | `afficher` | `imprimir` | `ausgeben` | `表示` | `اطبع` | `छापो` |
| `range` | `intervalle` | `rango` | `bereich` | `範囲` | `مدى` | `परास` |
| `len` | `longueur` | `largo` | `länge` | `長さ` | `طول` | `लंबाई` |
| `sum` | `somme` | `suma` | `summe` | `合計` | `مجموع` | `योग` |
| `input` | `saisie` | `entrada` | `eingabe` | `入力` | `إدخال` | `इनपुट` |

---

## Contributor Checklist

Before submitting a language pack PR:

- [ ] All 51 keyword concepts have translations
- [ ] Keywords are unique within the language (no collisions)
- [ ] Keywords are identifier-safe (letters/underscores only)
- [ ] Diacritics are preferred; ASCII aliases provided where helpful
- [ ] Native speaker review or equivalent (citation in PR description)
- [ ] Technical programming terms verified (not just dictionary translations)
- [ ] Builtin aliases (if provided) are semantically accurate
- [ ] Error messages use same placeholder format as other languages
- [ ] REPL command translations are natural for programmers in that language
- [ ] Surface patterns (if any) tested with real SOV/RTL usage examples
- [ ] All existing 858 tests still pass after changes
- [ ] New tests added for the new language

---

## Resources

- [Adding a New Language](/extending/) — Full onboarding guide
- `multilingualprogramming/resources/usm/keywords.json` — Keyword data file
- `multilingualprogramming/resources/usm/builtins_aliases.json` — Builtin aliases
- `multilingualprogramming/keyword/keyword_validator.py` — Validation logic
