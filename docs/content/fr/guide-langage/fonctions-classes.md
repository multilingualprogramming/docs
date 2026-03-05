---
page_id: language_guide__functions_classes
locale: fr
title: Fonctions et classes
path_segments:
- guide-langage
- fonctions-classes
source_hash: b0f5ca5c422c
status: translated
---



Les fonctions et classes dans multilingual fonctionnent comme en Python, avec des mots-cles localises pour `def`, `class`, `return`, `self` et les constructions associees. Les identifiants (variables, fonctions, classes) ne sont jamais traduits - ils restent tels quels dans le Python genere.

---

## Definitions de fonctions

### Syntaxe

```text
[DEF] name(params):
    [RETURN] expression
```

### Anglais

{{snippet:language_guide__functions_classes__py01}}

### Francais

{{snippet:language_guide__functions_classes__py02}}

### Espagnol

{{snippet:language_guide__functions_classes__py03}}

### Allemand

{{snippet:language_guide__functions_classes__py04}}

### Japonais

{{snippet:language_guide__functions_classes__py05}}

### Arabe

{{snippet:language_guide__functions_classes__py06}}

### Hindi

{{snippet:language_guide__functions_classes__py07}}

### Chinese

{{snippet:language_guide__functions_classes__py08}}

---

## Types de parametres

Toutes les formes de parametres Python sont supportees dans toutes les langues :

{{snippet:language_guide__functions_classes__py09}}

### Valeurs par defaut

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

## Fonctions imbriquees et closures

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

## Fonctions lambda

{{snippet:language_guide__functions_classes__py21}}

---

## Class Definitions

### Syntaxe

```text
[CLASS] Name:
    [DEF] __init__(self, params):
        self.attr = value

    [DEF] method(self):
        [RETURN] expression
```

### Anglais

{{snippet:language_guide__functions_classes__py22}}

### Francais

{{snippet:language_guide__functions_classes__py23}}

### Japonais

{{snippet:language_guide__functions_classes__py24}}

### Arabe

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

Voir [Reference des mots-cles](/language-guide/keywords/) pour les 17 langues.
