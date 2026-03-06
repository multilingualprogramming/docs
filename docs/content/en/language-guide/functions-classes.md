---
page_id: language_guide__functions_classes
locale: en
title: Functions & Classes
path_segments:
- language-guide
- functions-classes
source_hash: b0f5ca5c422c
status: source
permalink: /en/docs/language-guide/functions-classes/
---

Functions and classes in multilingual work exactly like Python, with localized keywords for `def`, `class`, `return`, `self`, and related constructs. Identifiers (variable names, function names, class names) are never translated — they remain as-is in the generated Python.

---

## Function Definitions

### Syntax

```text
[DEF] name(params):
    [RETURN] expression
```

### English

{{snippet:language_guide__functions_classes__py01}}

### French

{{snippet:language_guide__functions_classes__py02}}

### Spanish

{{snippet:language_guide__functions_classes__py03}}

### German

{{snippet:language_guide__functions_classes__py04}}

### Japanese

{{snippet:language_guide__functions_classes__py05}}

### Arabic

{{snippet:language_guide__functions_classes__py06}}

### Hindi

{{snippet:language_guide__functions_classes__py07}}

### Chinese

{{snippet:language_guide__functions_classes__py08}}

---

## Parameter Types

All Python parameter forms are supported across all languages:

{{snippet:language_guide__functions_classes__py09}}

### Default Values

{{snippet:language_guide__functions_classes__py10}}

### Type Annotations

{{snippet:language_guide__functions_classes__py11}}

### *args and **kwargs

{{snippet:language_guide__functions_classes__py12}}

### Keyword-Only Arguments

{{snippet:language_guide__functions_classes__py13}}

---

## Return Values

### Single Value

{{snippet:language_guide__functions_classes__py14}}

### Multiple Values (tuple)

{{snippet:language_guide__functions_classes__py15}}

### No Return (None)

{{snippet:language_guide__functions_classes__py16}}

---

## Nested Functions and Closures

{{snippet:language_guide__functions_classes__py17}}

---

## Decorators

### Basic Decorator

{{snippet:language_guide__functions_classes__py18}}

### Multiple Decorators

Decorators are applied bottom-up:

{{snippet:language_guide__functions_classes__py19}}

### functools.wraps

{{snippet:language_guide__functions_classes__py20}}

---

## Lambda Functions

{{snippet:language_guide__functions_classes__py21}}

---

## Class Definitions

### Syntax

```text
[CLASS] Name:
    [DEF] __init__(self, params):
        self.attr = value

    [DEF] method(self):
        [RETURN] expression
```

### English

{{snippet:language_guide__functions_classes__py22}}

### French

{{snippet:language_guide__functions_classes__py23}}

### Japanese

{{snippet:language_guide__functions_classes__py24}}

### Arabic

{{snippet:language_guide__functions_classes__py25}}

---

## Inheritance

### Single Inheritance

{{snippet:language_guide__functions_classes__py26}}

### Multiple Inheritance

{{snippet:language_guide__functions_classes__py27}}

---

## Class Features

### Class and Static Methods

{{snippet:language_guide__functions_classes__py28}}

### Properties

{{snippet:language_guide__functions_classes__py29}}

### Dunder Methods

{{snippet:language_guide__functions_classes__py30}}

---

## Dataclasses

{{snippet:language_guide__functions_classes__py31}}

---

## Function Keyword Table

| Concept | en | fr | es | de | ja | ar | hi | zh |
|---------|----|----|----|----|----|----|----|----|
| def | `def` | `fonction` | `función` | `funktion` | `関数` | `دالة` | `कार्य` | `函数` |
| return | `return` | `retourner` | `retornar` | `zurückgeben` | `戻る` | `أرجع` | `वापस` | `返回` |
| class | `class` | `classe` | `clase` | `klasse` | `クラス` | `فئة` | `वर्ग` | `类` |
| self | `self` | `soi` | `yo` | `selbst` | `自分` | `النفس` | `स्वयं` | `自身` |
| super | `super` | `super` | `super` | `super` | `super` | `super` | `super` | `super` |

> `super`, `lambda`, `pass` are universal across all 17 languages.

See [Keywords Reference]({{ '/en/docs/language-guide/keywords/' | relative_url }}) for all 17 languages.
