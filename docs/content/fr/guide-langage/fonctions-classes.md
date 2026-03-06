---
page_id: language_guide__functions_classes
locale: fr
title: Fonctions et classes
path_segments:
- guide-langage
- fonctions-classes
source_hash: b0f5ca5c422c
status: translated
permalink: /fr/docs/guide-langage/fonctions-classes/
---

Les fonctions et les classes de `multilingual` fonctionnent comme en Python, avec des mots-clés localisés pour `def`, `class`, `return`, `self` et les constructions associées. Les identifiants ne sont jamais traduits : ils sont conservés tels quels dans le Python généré.

---

## Définitions de fonctions

### Syntaxe

```text
[DEF] name(params):
    [RETURN] expression
```

### Anglais

{{snippet:language_guide__functions_classes__py01}}

### Français

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

### Chinois

{{snippet:language_guide__functions_classes__py08}}

---

## Types de paramètres

Toutes les formes de paramètres Python sont prises en charge :

{{snippet:language_guide__functions_classes__py09}}

### Valeurs par défaut

{{snippet:language_guide__functions_classes__py10}}

### Annotations de type

{{snippet:language_guide__functions_classes__py11}}

### `*args` et `**kwargs`

{{snippet:language_guide__functions_classes__py12}}

### Arguments uniquement nommés

{{snippet:language_guide__functions_classes__py13}}

---

## Valeurs de retour

### Valeur simple

{{snippet:language_guide__functions_classes__py14}}

### Valeurs multiples

{{snippet:language_guide__functions_classes__py15}}

### Sans retour explicite

{{snippet:language_guide__functions_classes__py16}}

---

## Fonctions imbriquées et fermetures

{{snippet:language_guide__functions_classes__py17}}

---

## Décorateurs

### Décorateur simple

{{snippet:language_guide__functions_classes__py18}}

### Décorateurs multiples

Les décorateurs sont appliqués du bas vers le haut :

{{snippet:language_guide__functions_classes__py19}}

### `functools.wraps`

{{snippet:language_guide__functions_classes__py20}}

---

## Fonctions lambda

{{snippet:language_guide__functions_classes__py21}}

---

## Définitions de classes

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

### Français

{{snippet:language_guide__functions_classes__py23}}

### Japonais

{{snippet:language_guide__functions_classes__py24}}

### Arabe

{{snippet:language_guide__functions_classes__py25}}

---

## Héritage

### Héritage simple

{{snippet:language_guide__functions_classes__py26}}

### Héritage multiple

{{snippet:language_guide__functions_classes__py27}}

---

## Fonctionnalités de classe

### Méthodes de classe et méthodes statiques

{{snippet:language_guide__functions_classes__py28}}

### Propriétés

{{snippet:language_guide__functions_classes__py29}}

### Méthodes spéciales

{{snippet:language_guide__functions_classes__py30}}

---

## `dataclasses`

{{snippet:language_guide__functions_classes__py31}}

---

## Repères de vocabulaire

| Concept | Anglais | Français |
|---------|---------|-----------|
| Définition de fonction | `def` | `fonction` |
| Retour | `return` | `retourner` |
| Définition de classe | `class` | `classe` |
| Référence à l'instance | `self` | `soi` |
| Appel au parent | `super` | `super` |

`super`, `lambda` et `pass` restent universels dans toutes les langues.

Voir la [Référence des mots-clés]({{ '/fr/docs/guide-langage/mots-cles/' | relative_url }}) pour la liste complète des 17 langues.
