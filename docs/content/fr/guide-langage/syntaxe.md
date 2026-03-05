---
page_id: language_guide__syntax
locale: fr
title: Syntaxe
path_segments:
- guide-langage
- syntaxe
source_hash: 1a1df4d35040
status: translated
---



Cette page est la reference syntaxique definitive pour multilingual. Les mots-cles affiches sous forme `[CONCEPT]` representent des concepts semantiques - remplacez-les par le mot-cle approprie pour la langue choisie.

Voir [Reference des mots-cles](/language-guide/keywords/) pour le mapping complet.

---

## Conventions de syntaxe

- `[LET]` — variable declaration keyword (`let`, `soit`, `sei`, `変数`, `مان`, ...)
- `[IF]` — conditional (`if`, `si`, `wenn`, `もし`, `إذا`, ...)
- `[FOR]` — for loop keyword
- `[DEF]` — function definition
- `[CLASS]` — class definition
- `[RETURN]` — return statement
- Identifiers are any Unicode sequence (not translated)
- String literals: `"..."`, `'...'`, `"""..."""`, `f"..."`

---

## Variables et declarations

### Declaration de variable

```text
[LET] identifier = expression
[LET] identifier: type = expression
```

Exemples :
{{snippet:language_guide__syntax__py01}}

### Constantes

```text
const IDENTIFIER = expression
```

{{snippet:language_guide__syntax__py02}}

### Affectation chainee

```text
identifier = identifier = expression
[LET] a = [LET] b = expression
```

{{snippet:language_guide__syntax__py03}}

### Suppression

```text
del identifier
```

### Affectation augmentee

{{snippet:language_guide__syntax__py04}}

---

## Literaux

### Nombres

{{snippet:language_guide__syntax__py05}}

### Chaines

{{snippet:language_guide__syntax__py06}}

### Booleens et None

{{snippet:language_guide__syntax__py07}}

### Collections

{{snippet:language_guide__syntax__py08}}

---

## Expressions

### Arithmetique

{{snippet:language_guide__syntax__py09}}

### Comparaison

{{snippet:language_guide__syntax__py10}}

### Booleen

{{snippet:language_guide__syntax__py11}}

### Bitwise

{{snippet:language_guide__syntax__py12}}

### Slicing

{{snippet:language_guide__syntax__py13}}

### Walrus Operator

{{snippet:language_guide__syntax__py14}}

### Ternary Expression

```text
value_if_true [IF] condition [ELSE] value_if_false
```

{{snippet:language_guide__syntax__py15}}

### Unpacking

{{snippet:language_guide__syntax__py16}}

### Dict/Set Unpacking

{{snippet:language_guide__syntax__py17}}

### Lambda

```text
lambda params: expression
```

{{snippet:language_guide__syntax__py18}}

---

## Controle de flux

### if / elif / else

```text
[IF] condition:
    block
[ELIF] condition:
    block
[ELSE]:
    block
```

### for loop

```text
[FOR] target [IN] iterable:
    block
[ELSE]:
    block  # runs if no break
```

Tuple target:
{{snippet:language_guide__syntax__py19}}

### while loop

```text
[LOOP_WHILE] condition:
    block
[ELSE]:
    block  # runs if no break
```

### match / case

```text
match expression:
    case pattern:
        block
    case pattern [IF] guard:
        block
    case pattern1 | pattern2:
        block
    case pattern [AS] name:
        block
    case _:
        block  # default/wildcard
```

### break / continue / pass

{{snippet:language_guide__syntax__py20}}

---

## Fonctions

### Basic Definition

```text
[DEF] name(params):
    block
```

### With Return

```text
[DEF] name(params):
    [RETURN] expression
```

### Types de parametres

{{snippet:language_guide__syntax__py21}}

### Valeurs par defaut

{{snippet:language_guide__syntax__py22}}

### Type Annotations

{{snippet:language_guide__syntax__py23}}

### Generateurs

```text
[DEF] name(params):
    [YIELD] expression
    [YIELD] [FROM] iterable
```

{{snippet:language_guide__syntax__py24}}

### Fonctions asynchrones

```text
[ASYNC] [DEF] name(params):
    [AWAIT] expression
    [ASYNC] [FOR] target [IN] iterable:
        block
    [ASYNC] [WITH] expression [AS] name:
        block
```

{{snippet:language_guide__syntax__py25}}

### Decorators

{{snippet:language_guide__syntax__py26}}

---

## Classes

### Basic Class

```text
[CLASS] Name:
    [DEF] __init__(self, params):
        self.attr = value

    [DEF] method(self):
        [RETURN] expression
```

### Inheritance

```text
[CLASS] Child(Parent):
    [DEF] __init__(self, params):
        super(Child, self).__init__(params)
```

### Class with Decorators

{{snippet:language_guide__syntax__py27}}

---

## Gestion des exceptions

### try / except / else / finally

```text
[TRY]:
    block
[EXCEPT] ExceptionType [AS] name:
    block
[EXCEPT] (Type1, Type2) [AS] name:
    block
[ELSE]:
    block  # runs if no exception
[FINALLY]:
    block  # always runs
```

### raise

```text
[RAISE] ExceptionType("message")
[RAISE]                          # re-raise current exception
[RAISE] ExceptionA [FROM] ExceptionB  # chaining
```

### assert

```text
[ASSERT] condition
[ASSERT] condition, "message"
```

---

## Context Managers

```text
[WITH] expression [AS] name:
    block

[WITH] expr1 [AS] n1, expr2 [AS] n2:
    block
```

{{snippet:language_guide__syntax__py28}}

---

## Comprehensions

### Comprehension de liste

{{snippet:language_guide__syntax__py29}}

### Dict Comprehension

{{snippet:language_guide__syntax__py30}}

### Set Comprehension

{{snippet:language_guide__syntax__py31}}

### Generator Expression

{{snippet:language_guide__syntax__py32}}

---

## Imports

```text
[IMPORT] module
[FROM] module [IMPORT] name
[FROM] module [IMPORT] name [AS] alias
[FROM] module [IMPORT] *
```

{{snippet:language_guide__syntax__py33}}

---

## Global and Nonlocal

```text
[GLOBAL] identifier
[NONLOCAL] identifier
```

{{snippet:language_guide__syntax__py34}}

---

## Special Values and Operators

| Expression | Meaning |
|-----------|---------|
| `True` | Boolean true |
| `False` | Boolean false |
| `None` | Null value |
| `Ellipsis` / `...` | Ellipsis literal |
| `NotImplemented` | Not-implemented sentinel |
| `is` | Identity check |
| `is not` | Negative identity |
| `in` | Membership check |
| `not in` | Negative membership |

---

## Supported Exception Types (45+)

{{snippet:language_guide__syntax__py35}}
