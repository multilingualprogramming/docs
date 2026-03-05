---
page_id: language_guide__control_flow
locale: en
title: Control Flow
path_segments:
- language-guide
- control-flow
source_hash: 76561f72de89
status: source
---

Control flow in multilingual uses the same Python semantics with localized keywords. All constructs work identically across all 17 supported languages — only the surface keywords differ.

---

## Conditionals — if / elif / else

### Syntax

```text
[IF] condition:
    block
[ELIF] condition:
    block
[ELSE]:
    block
```

### English

{{snippet:language_guide__control_flow__py01}}

### French

{{snippet:language_guide__control_flow__py02}}

### Spanish

{{snippet:language_guide__control_flow__py03}}

### German

{{snippet:language_guide__control_flow__py04}}

### Japanese

{{snippet:language_guide__control_flow__py05}}

### Arabic

{{snippet:language_guide__control_flow__py06}}

### Hindi

{{snippet:language_guide__control_flow__py07}}

### Chinese

{{snippet:language_guide__control_flow__py08}}

---

## For Loop

### Syntax

```text
[FOR] target [IN] iterable:
    block
[ELSE]:
    block   # runs if loop completed without break
```

### English

{{snippet:language_guide__control_flow__py09}}

### French

{{snippet:language_guide__control_flow__py10}}

### Spanish

{{snippet:language_guide__control_flow__py11}}

### German

{{snippet:language_guide__control_flow__py12}}

### Japanese

{{snippet:language_guide__control_flow__py13}}

### Arabic

{{snippet:language_guide__control_flow__py14}}

### Hindi

{{snippet:language_guide__control_flow__py15}}

### Chinese

{{snippet:language_guide__control_flow__py16}}

### Tuple Unpacking in For

{{snippet:language_guide__control_flow__py17}}

---

## While Loop

### Syntax

```text
[LOOP_WHILE] condition:
    block
[ELSE]:
    block   # runs if condition became false (no break)
```

### English

{{snippet:language_guide__control_flow__py18}}

### French

{{snippet:language_guide__control_flow__py19}}

### Spanish

{{snippet:language_guide__control_flow__py20}}

### German

{{snippet:language_guide__control_flow__py21}}

### Japanese

{{snippet:language_guide__control_flow__py22}}

### Arabic

{{snippet:language_guide__control_flow__py23}}

### Hindi

{{snippet:language_guide__control_flow__py24}}

### Chinese

{{snippet:language_guide__control_flow__py25}}

---

## Match / Case (Pattern Matching)

Pattern matching (Python 3.10+) uses the `match` keyword, which is universal (not localized). Case patterns follow standard Python syntax.

### Syntax

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

French version:

{{snippet:language_guide__control_flow__py36}}

---

## Loop-Else Idiom

{{snippet:language_guide__control_flow__py37}}

---

## Walrus Operator in Conditions

{{snippet:language_guide__control_flow__py38}}

---

## Complete Control Flow Keyword Table

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

See [Keywords Reference](/language-guide/keywords/) for all 17 languages including Italian, Portuguese, Polish, Dutch, Swedish, Danish, Finnish, Bengali, and Tamil.
