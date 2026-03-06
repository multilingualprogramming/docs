---
page_id: language_guide__control_flow
locale: fr
title: Contrôle de flux
path_segments:
- guide-langage
- controle-flux
source_hash: 76561f72de89
status: translated
permalink: /fr/docs/guide-langage/controle-flux/
---

Le contrôle de flux de `multilingual` reprend la sémantique de Python avec des mots-clés localisés. Les constructions se comportent de la même façon dans les 17 langues prises en charge ; seuls les mots-clés de surface changent.

---

## Conditions : `if` / `elif` / `else`

### Syntaxe

```text
[IF] condition:
    block
[ELIF] condition:
    block
[ELSE]:
    block
```

### Anglais

{{snippet:language_guide__control_flow__py01}}

### Français

{{snippet:language_guide__control_flow__py02}}

### Espagnol

{{snippet:language_guide__control_flow__py03}}

### Allemand

{{snippet:language_guide__control_flow__py04}}

### Japonais

{{snippet:language_guide__control_flow__py05}}

### Arabe

{{snippet:language_guide__control_flow__py06}}

### Hindi

{{snippet:language_guide__control_flow__py07}}

### Chinois

{{snippet:language_guide__control_flow__py08}}

---

## Boucle `for`

### Syntaxe

```text
[FOR] target [IN] iterable:
    block
[ELSE]:
    block   # exécuté si la boucle se termine sans break
```

### Anglais

{{snippet:language_guide__control_flow__py09}}

### Français

{{snippet:language_guide__control_flow__py10}}

### Espagnol

{{snippet:language_guide__control_flow__py11}}

### Allemand

{{snippet:language_guide__control_flow__py12}}

### Japonais

{{snippet:language_guide__control_flow__py13}}

### Arabe

{{snippet:language_guide__control_flow__py14}}

### Hindi

{{snippet:language_guide__control_flow__py15}}

### Chinois

{{snippet:language_guide__control_flow__py16}}

### Dépaquetage de tuples

{{snippet:language_guide__control_flow__py17}}

---

## Boucle `while`

### Syntaxe

```text
[LOOP_WHILE] condition:
    block
[ELSE]:
    block   # exécuté si la condition devient fausse sans break
```

### Anglais

{{snippet:language_guide__control_flow__py18}}

### Français

{{snippet:language_guide__control_flow__py19}}

### Espagnol

{{snippet:language_guide__control_flow__py20}}

### Allemand

{{snippet:language_guide__control_flow__py21}}

### Japonais

{{snippet:language_guide__control_flow__py22}}

### Arabe

{{snippet:language_guide__control_flow__py23}}

### Hindi

{{snippet:language_guide__control_flow__py24}}

### Chinois

{{snippet:language_guide__control_flow__py25}}

---

## `match` / `case`

Le filtrage par motifs de Python 3.10+ utilise le mot-clé universel `match`, non localisé. Les motifs gardent la syntaxe standard de Python.

### Syntaxe

```text
match expression:
    case pattern:
        block
    case pattern [IF] guard:
        block
    case pattern1 | pattern2:
        block
    case (x, y):
        block
    case {"key": value}:
        block
    case ClassName(attr=value):
        block
    case _:
        block   # joker / cas par défaut
```

### Motifs littéraux

{{snippet:language_guide__control_flow__py26}}

### Capture de valeurs

{{snippet:language_guide__control_flow__py27}}

### Conditions de garde

{{snippet:language_guide__control_flow__py28}}

### Motifs alternatifs

{{snippet:language_guide__control_flow__py29}}

### Motif `as`

{{snippet:language_guide__control_flow__py30}}

### Motifs de classes

{{snippet:language_guide__control_flow__py31}}

---

## `break` / `continue` / `pass`

Ces mots-clés sont universels et ne sont pas localisés.

### `break` : sortir d'une boucle

{{snippet:language_guide__control_flow__py32}}

### `continue` : passer à l'itération suivante

{{snippet:language_guide__control_flow__py33}}

### `pass` : instruction vide

{{snippet:language_guide__control_flow__py34}}

---

## Boucles imbriquées

{{snippet:language_guide__control_flow__py35}}

Version française :

{{snippet:language_guide__control_flow__py36}}

---

## Idiome `loop-else`

{{snippet:language_guide__control_flow__py37}}

---

## Opérateur morse dans les conditions

{{snippet:language_guide__control_flow__py38}}

---

## Repères de vocabulaire

| Concept | Anglais | Français |
|---------|---------|-----------|
| Condition | `if` | `si` |
| Sinon si | `elif` | `sinon_si` |
| Sinon | `else` | `sinon` |
| Boucle | `for` | `pour` |
| Appartenance dans une boucle | `in` | `dans` |
| Tant que | `while` | `tant_que` |

Voir la [Référence des mots-clés](/fr/docs/guide-langage/mots-cles/) pour la liste complète des 17 langues.
