---
page_id: language_guide__control_flow
locale: fr
title: Controle de flux
path_segments:
- guide-langage
- controle-flux
source_hash: 76561f72de89
status: translated
---



Le controle de flux dans multilingual utilise la meme semantique que Python avec des mots-cles localises. Toutes les constructions se comportent de facon identique dans les 17 langues supportees - seuls les mots-cles de surface changent.

---

## Conditionals — if / elif / else

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

### Francais

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

### Chinese

{{snippet:language_guide__control_flow__py08}}

---

## For Loop

### Syntaxe

```text
[FOR] target [IN] iterable:
    block
[ELSE]:
    block   # runs if loop completed without break
```

### Anglais

{{snippet:language_guide__control_flow__py09}}

### Francais

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

### Chinese

{{snippet:language_guide__control_flow__py16}}

### Tuple Unpacking in For

{{snippet:language_guide__control_flow__py17}}

---

## While Loop

### Syntaxe

```text
[LOOP_WHILE] condition:
    block
[ELSE]:
    block   # runs if condition became false (no break)
```

### Anglais

{{snippet:language_guide__control_flow__py18}}

### Francais

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

### Chinese

{{snippet:language_guide__control_flow__py25}}

---

## Match / Case (Pattern Matching)

Pattern matching (Python 3.10+) uses the `match` keyword, which is universal (not localized). Case patterns follow standard Python syntax.

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
        block   # wildcard / default
```

### Literal Patterns

{{snippet:language_guide__control_flow__py26}}

### Value Capture

{{snippet:language_guide__control_flow__py27}}

### Guard Conditions

{{snippet:language_guide__control_flow__py28}}

### OR Patterns

{{snippet:language_guide__control_flow__py29}}

### AS Pattern

{{snippet:language_guide__control_flow__py30}}

### Class Patterns

{{snippet:language_guide__control_flow__py31}}

---

## Break / Continue / Pass

These keywords are universal (not localized) across all languages.

### break — Exit a loop early

{{snippet:language_guide__control_flow__py32}}

### continue — Skip current iteration

{{snippet:language_guide__control_flow__py33}}

### pass — No-op placeholder

{{snippet:language_guide__control_flow__py34}}

---

## Nested Loops

{{snippet:language_guide__control_flow__py35}}

Version francaise :

{{snippet:language_guide__control_flow__py36}}

---

## Loop-Else Idiom

{{snippet:language_guide__control_flow__py37}}

---

## Walrus Operator in Conditions

{{snippet:language_guide__control_flow__py38}}

---

## Table complete des mots-cles de controle de flux

| Concept | en | fr | es | de | ja | ar | hi | zh |
|---------|----|----|----|----|----|----|----|----|
| if | `if` | `si` | `si` | `wenn` | `もし` | `إذا` | `यदि` | `如果` |
| elif | `elif` | `sinon_si` | `sino_si` | `sonst_wenn` | `そうでなければもし` | `وإلا_إذا` | `अथवा_यदि` | `否则如果` |
| else | `else` | `sinon` | `sino` | `sonst` | `そうでなければ` | `وإلا` | `अन्यथा` | `否则` |
| for | `for` | `pour` | `para` | `für` | `毎` | `لكل` | `प्रत्येक` | `对于` |
| in (for) | `in` | `dans` | `en` | `in` | `中` | `في` | `में` | `在` |
| while | `while` | `tant_que` | `mientras` | `solange` | `間` | `طالما` | `जबकि` | `当` |
| break | `break` | `break` | `break` | `break` | `break` | `break` | `break` | `break` |
| continue | `continue` | `continue` | `continue` | `continue` | `continue` | `continue` | `continue` | `continue` |
| pass | `pass` | `pass` | `pass` | `pass` | `pass` | `pass` | `pass` | `pass` |

> `break`, `continue`, and `pass` are universal across all 17 languages.

Voir [Reference des mots-cles](/language-guide/keywords/) pour les 17 langues, y compris italien, portugais, polonais, neerlandais, suedois, danois, finnois, bengali et tamoul.
