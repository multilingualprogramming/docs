---
layout: page
title: "Adding a New Language"
description: "Data-driven guide to adding a new language frontend to multilingual."
category: "Extending"
permalink: /extending/
next_page:
  title: "Translation Guidelines"
  url: /extending/translation/
---

multilingual is designed so new programming languages can be added primarily by updating **data files** (JSON), not parser or codegen logic.

Language onboarding follows a controlled-language policy: add deterministic, testable surface forms only. See [CNL Scope](/extending/cnl-scope/).

---

## Overview

To add language `xx`, you need to:

1. Add keyword mappings in `keywords.json`
2. Add parser/semantic error messages in `error_messages.json`
3. Add REPL localization in `commands.json`
4. (Optional) Add operator description localization in `operators.json`
5. (Optional) Add built-in aliases in `builtins_aliases.json`
6. (Optional) Add surface syntax patterns in `surface_patterns.json`
7. Add tests
8. Update documentation

---

## Step 1: Add Keyword Mappings

**File**: `multilingualprogramming/resources/usm/keywords.json`

1. Add the new language code to `"languages"` array
2. For every concept in every category, add a translation for the new language

```json
{
  "languages": ["en", "fr", "es", ..., "xx"],
  "keywords": {
    "control_flow": {
      "COND_IF": {
        "en": "if",
        "fr": "si",
        "xx": "your_if_keyword"
      },
      "COND_ELIF": {
        "en": "elif",
        "fr": "sinonsi",
        "xx": "your_elif_keyword"
      }
    }
  }
}
```

**Requirements:**
- All 51 concepts must have a translation (completeness validation enforced at load time)
- Prefer unique tokens per language to avoid ambiguity
- Keep tokens identifier-safe (letters/underscores, no spaces)
- Avoid keywords that conflict with builtin names in your language

**Why this is enough:**
- `KeywordRegistry` loads this file dynamically
- `Lexer` detects keywords through `KeywordRegistry`
- `Parser` consumes concept tokens — syntax support follows automatically
- `RuntimeBuiltins` maps builtins from concept IDs — execution picks up automatically

---

## Step 2: Add Error Messages

**File**: `multilingualprogramming/resources/parser/error_messages.json`

For each message key under `messages`, add the new language translation. Use the same placeholders as existing translations.

```json
{
  "messages": {
    "unexpected_token": {
      "en": "Unexpected token '{token}' at line {line}",
      "fr": "Jeton inattendu '{token}' à la ligne {line}",
      "xx": "Your translation with {token} and {line} placeholders"
    },
    "undefined_variable": {
      "en": "Variable '{name}' is not defined",
      "fr": "La variable '{name}' n'est pas définie",
      "xx": "Your translation with {name} placeholder"
    }
  }
}
```

**Why:** `ErrorMessageRegistry.format()` reads this file dynamically and the parser/semantic analyzer use it for diagnostics.

---

## Step 3: Add REPL Localization

**File**: `multilingualprogramming/resources/repl/commands.json`

Update:
1. `help_titles` for the new language
2. Message keys (`keywords_title`, `symbols_title`, `unsupported_language`)
3. `commands.<name>.aliases` — command words in the language
4. `commands.<name>.descriptions` — help text

```json
{
  "help_titles": {
    "en": "Available commands:",
    "fr": "Commandes disponibles:",
    "xx": "Your language: Available commands"
  },
  "commands": {
    "language": {
      "aliases": {
        "en": [":language", ":lang"],
        "fr": [":langue"],
        "xx": [":your_alias"]
      },
      "descriptions": {
        "en": "Switch language",
        "fr": "Changer de langue",
        "xx": "Your description"
      }
    }
  }
}
```

---

## Step 4: Operator Localization (Optional)

**File**: `multilingualprogramming/resources/usm/operators.json`

Add the new language under `description` for each operator:

```json
{
  "operators": {
    "+": {
      "description": {
        "en": "Addition",
        "fr": "Addition",
        "xx": "Your language term for addition"
      }
    }
  }
}
```

Used by the REPL `:ops` command. Falls back to English if not provided.

---

## Step 5: Built-in Aliases (Optional)

**File**: `multilingualprogramming/resources/usm/builtins_aliases.json`

Add localized aliases for selected universal builtins:

```json
{
  "builtins": {
    "print": {
      "en": "print",
      "fr": "afficher",
      "xx": "your_print_word"
    },
    "range": {
      "en": "range",
      "fr": "intervalle",
      "xx": "your_range_word"
    },
    "len": {
      "en": "len",
      "fr": "longueur",
      "xx": "your_length_word"
    }
  }
}
```

**41 builtin concepts** have localization support. The universal English name always remains available — aliases are additive.

---

## Step 6: Surface Syntax Patterns (Optional)

**File**: `multilingualprogramming/resources/usm/surface_patterns.json`

Use this when keyword translation alone is insufficient for natural phrasing. Typical use cases:
- Iterable-first `for` headers (SOV languages like Japanese, Hindi)
- Language-specific particles around loop/condition clauses
- RTL languages (Arabic)

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
      "name": "xx_for_iterable_first",
      "language": "xx",
      "normalize_template": "for_iterable_first",
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

**Pattern token kinds:**
- `expr` — capture expression span into a slot
- `identifier` — capture single identifier token
- `keyword` — require a specific concept token
- `delimiter` — require a delimiter token (`:`, etc.)
- `literal` — require a literal token (particles like `内の`, `ضمن`)

**Output kinds** (`normalize_to` or template):
- `keyword` — emit a concept keyword token
- `delimiter` — emit a delimiter token
- `identifier_slot` — emit captured identifier
- `expr_slot` — emit captured expression

---

## Step 7: Add Tests

Minimum recommended tests:

### 1. Keyword Registry Tests

```python
# tests/keyword_registry_test.py
def test_xx_in_supported_languages():
    registry = KeywordRegistry()
    assert "xx" in registry.get_supported_languages()

def test_xx_cond_if():
    registry = KeywordRegistry()
    assert registry.get_keyword("COND_IF", "xx") == "your_if_keyword"
```

### 2. End-to-End Executor Test

```python
# tests/executor_test.py
def test_xx_basic_program():
    executor = ProgramExecutor()
    source = """
your_let_keyword x = 5
your_let_keyword y = 10
your_print_word(x + y)
"""
    output = executor.execute(source, language="xx")
    assert "15" in output
```

### 3. Error Messages Test

```python
# tests/error_messages_test.py
def test_xx_has_all_error_messages():
    registry = ErrorMessageRegistry()
    for key in registry.get_all_message_keys():
        assert "xx" in registry.get_languages_for_message(key)
```

### 4. Runtime Builtins Test

```python
# tests/runtime_builtins_test.py
def test_xx_print_alias():
    builtins = RuntimeBuiltins.for_language("xx")
    assert "your_print_word" in builtins
    assert builtins["your_print_word"] is print
```

### 5. Surface Normalizer Test (if adding patterns)

```python
# tests/surface_normalizer_test.py
def test_xx_surface_config_valid():
    # Ensure config stays schema-valid
    normalizer = SurfaceNormalizer()
    assert normalizer.validate_config()

def test_xx_for_loop_normalized():
    # Test that your surface form normalizes correctly
    ...
```

---

## Step 8: Update Documentation

At minimum:
- `README.md` — add to supported languages list
- `docs/reference.md` — add to supported languages table
- Link this onboarding guide where relevant

---

## Validation Commands

```bash
# Full test suite
python -m pytest -q

# Focused validation for new language
python -m pytest -q \
  tests/keyword_registry_test.py \
  tests/error_messages_test.py \
  tests/executor_test.py \
  tests/repl_test.py

# Surface normalizer (if patterns added)
python -m pytest -q \
  tests/surface_normalizer_test.py \
  tests/parser_test.py \
  tests/executor_test.py

# Language smoke tests
python -m multilingualprogramming smoke --lang xx
python -m multilingualprogramming smoke --all

# Lint
python -m pylint $(git ls-files '*.py')
```

---

## Common Mistakes

- **Missing concepts**: All 51 concepts must have translations. Validation fails at load time for incomplete packs.
- **Ambiguous keywords**: Avoid keywords that are shared with existing languages if they have different meanings.
- **Reserved words**: Don't use keywords that conflict with Python built-in names that are not localized.
- **Surface pattern errors**: Defining both `normalize_to` and `normalize_template` in one rule → `ValueError`
- **Missing slot references**: Capturing a slot in output that was never captured in the pattern → `ValueError`

---

## Checklist Template

Use `docs/templates/language_pack_checklist.md` when opening a PR for a new language pack:

```markdown
## Language Pack: [Language Name] ([code])

- [ ] keywords.json updated (all 51 concepts)
- [ ] error_messages.json updated (all message keys)
- [ ] commands.json updated (REPL commands)
- [ ] operators.json updated (optional)
- [ ] builtins_aliases.json updated (optional)
- [ ] surface_patterns.json updated (optional, with tests)
- [ ] Keyword registry tests passing
- [ ] Executor end-to-end test passing
- [ ] Error messages test passing
- [ ] Runtime builtins test passing
- [ ] Smoke test passing: `multilingual smoke --lang xx`
- [ ] All 858 existing tests still passing
- [ ] README.md updated
- [ ] docs/reference.md updated
```
