---
page_id: language_guide__syntax
locale: en
title: Syntax Reference
path_segments:
- language-guide
- syntax
source_hash: 1a1df4d35040
status: source
permalink: /en/docs/language-guide/syntax/
---

This page is the definitive syntax reference for multilingual. Keywords shown in `[CONCEPT]` form refer to semantic concepts — replace them with the appropriate keyword for your chosen language.

See [Keywords Reference](/en/docs/language-guide/keywords/) for the full mapping.

---

## Syntax Conventions

- `[LET]` — variable declaration keyword (`let`, `soit`, `sei`, `変数`, `مان`, ...)
- `[IF]` — conditional (`if`, `si`, `wenn`, `もし`, `إذا`, ...)
- `[FOR]` — for loop keyword
- `[DEF]` — function definition
- `[CLASS]` — class definition
- `[RETURN]` — return statement
- Identifiers are any Unicode sequence (not translated)
- String literals: `"..."`, `'...'`, `"""..."""`, `f"..."`

---

## Variables and Declarations

### Variable Declaration

```text
[LET] identifier = expression
[LET] identifier: type = expression
```

Examples:
{{snippet:language_guide__syntax__py01}}

### Constants

```text
const IDENTIFIER = expression
```

{{snippet:language_guide__syntax__py02}}

### Chained Assignment

```text
identifier = identifier = expression
[LET] a = [LET] b = expression
```

{{snippet:language_guide__syntax__py03}}

### Delete

```text
del identifier
```

### Augmented Assignment

{{snippet:language_guide__syntax__py04}}

---

## Literals

### Numbers

{{snippet:language_guide__syntax__py05}}

### Strings

{{snippet:language_guide__syntax__py06}}

### Booleans and None

{{snippet:language_guide__syntax__py07}}

### Collections

{{snippet:language_guide__syntax__py08}}

---

## Expressions

### Arithmetic

{{snippet:language_guide__syntax__py09}}

### Comparison

{{snippet:language_guide__syntax__py10}}

### Boolean

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

## Control Flow

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

## Functions

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

### Parameter Types

{{snippet:language_guide__syntax__py21}}

### Default Values

{{snippet:language_guide__syntax__py22}}

### Type Annotations

{{snippet:language_guide__syntax__py23}}

### Generators

```text
[DEF] name(params):
    [YIELD] expression
    [YIELD] [FROM] iterable
```

{{snippet:language_guide__syntax__py24}}

### Async Functions

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

## Exception Handling

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

### List Comprehension

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
