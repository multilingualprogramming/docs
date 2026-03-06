---
page_id: language_guide__async_generators
locale: fr
title: Asynchrone et générateurs
path_segments:
- guide-langage
- asynchrone-generateurs
source_hash: ef520f55de2d
status: translated
permalink: /fr/docs/guide-langage/asynchrone-generateurs/
---

Les générateurs et les constructions asynchrones de `multilingual` suivent le modèle Python complet, avec des mots-clés localisés pour `yield`, `async`, `await`, `async for` et `async with`.

---

## Générateurs

### Syntaxe

```text
[DEF] name(params):
    [YIELD] expression
    [YIELD] [FROM] iterable
```

Une fonction qui contient `yield` devient un générateur. Elle produit les valeurs à la demande, sans construire toute la séquence en mémoire.

### Anglais

{{snippet:language_guide__async_generators__py01}}

### Français

{{snippet:language_guide__async_generators__py02}}

### Espagnol

{{snippet:language_guide__async_generators__py03}}

### Allemand

{{snippet:language_guide__async_generators__py04}}

### Japonais

{{snippet:language_guide__async_generators__py05}}

### Arabe

{{snippet:language_guide__async_generators__py06}}

### Hindi

{{snippet:language_guide__async_generators__py07}}

### Chinois

{{snippet:language_guide__async_generators__py08}}

---

## `yield from`

`yield from` délègue la production des valeurs à un autre itérable ou à un autre générateur :

{{snippet:language_guide__async_generators__py09}}

### Générateur récursif

{{snippet:language_guide__async_generators__py10}}

---

## Expressions génératrices

Les expressions génératrices produisent des séquences paresseuses sans définir de fonction dédiée :

{{snippet:language_guide__async_generators__py11}}

---

## Cas d'usage

### Séquences infinies

{{snippet:language_guide__async_generators__py12}}

### Lecture de fichiers en flux

{{snippet:language_guide__async_generators__py13}}

### Pipelines de transformation

{{snippet:language_guide__async_generators__py14}}

---

## Fonctions asynchrones

### Syntaxe

```text
[ASYNC] [DEF] name(params):
    [AWAIT] expression
```

### Anglais

{{snippet:language_guide__async_generators__py15}}

### Français

{{snippet:language_guide__async_generators__py16}}

### Espagnol

{{snippet:language_guide__async_generators__py17}}

### Allemand

{{snippet:language_guide__async_generators__py18}}

### Japonais

{{snippet:language_guide__async_generators__py19}}

### Arabe

{{snippet:language_guide__async_generators__py20}}

---

## Boucles `async for`

Itération sur des itérables asynchrones :

### Syntaxe

```text
[ASYNC] [FOR] target [IN] async_iterable:
    block
```

### Anglais

{{snippet:language_guide__async_generators__py21}}

### Français

{{snippet:language_guide__async_generators__py22}}

---

## `async with` et gestionnaires de contexte

```text
[ASYNC] [WITH] expression [AS] name:
    block
```

{{snippet:language_guide__async_generators__py23}}

---

## Exemple asynchrone complet

{{snippet:language_guide__async_generators__py24}}

---

## Générateurs asynchrones

Une fonction qui combine `async def` et `yield` devient un générateur asynchrone :

{{snippet:language_guide__async_generators__py25}}

---

## Exécution de code asynchrone

{{snippet:language_guide__async_generators__py26}}

---

## Repères de vocabulaire

| Concept | Anglais | Français |
|---------|---------|-----------|
| Définition asynchrone | `async def` | `async_fonction` |
| Attente | `await` | `attendre` |
| Production | `yield` | `produire` |
| Délégation | `yield from` | `produire de` |
| Boucle asynchrone | `async for` | `async_pour` |
| Contexte asynchrone | `async with` | `async_avec` |

Voir la [Référence des mots-clés]({{ '/fr/docs/guide-langage/mots-cles/' | relative_url }}) pour la liste complète des 17 langues.
