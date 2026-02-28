---
layout: page
title: "Control Flow"
description: "if/elif/else, for, while, match/case, break, continue, and pass — in all 17 languages."
category: "Language Guide"
permalink: /language-guide/control-flow/
prev_page:
  title: "Syntax Reference"
  url: /language-guide/syntax/
next_page:
  title: "Functions & Classes"
  url: /language-guide/functions-classes/
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

```python
let x = 42

if x > 0:
    print("positive")
elif x < 0:
    print("negative")
else:
    print("zero")
```

### French

```python
soit x = 42

si x > 0:
    afficher("positif")
sinon_si x < 0:
    afficher("négatif")
sinon:
    afficher("zéro")
```

### Spanish

```python
sea x = 42

si x > 0:
    imprimir("positivo")
sino_si x < 0:
    imprimir("negativo")
sino:
    imprimir("cero")
```

### German

```python
sei x = 42

wenn x > 0:
    ausgeben("positiv")
sonst_wenn x < 0:
    ausgeben("negativ")
sonst:
    ausgeben("null")
```

### Japanese

```python
変数 x = 42

もし x > 0:
    表示("正")
そうでなければもし x < 0:
    表示("負")
そうでなければ:
    表示("ゼロ")
```

### Arabic

```python
متغير x = 42

إذا x > 0:
    اطبع("موجب")
وإلا_إذا x < 0:
    اطبع("سالب")
وإلا:
    اطبع("صفر")
```

### Hindi

```python
चर x = 42

यदि x > 0:
    छापो("धनात्मक")
अथवा_यदि x < 0:
    छापो("ऋणात्मक")
अन्यथा:
    छापो("शून्य")
```

### Chinese

```python
变量 x = 42

如果 x > 0:
    打印("正数")
否则如果 x < 0:
    打印("负数")
否则:
    打印("零")
```

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

```python
for i in range(5):
    print(i)

# With else
for item in [1, 2, 3]:
    if item == 99:
        break
else:
    print("not found")
```

### French

```python
pour i dans intervalle(5):
    afficher(i)
```

### Spanish

```python
para i en rango(5):
    imprimir(i)
```

### German

```python
für i in bereich(5):
    ausgeben(i)
```

### Japanese

```python
毎 i 中 範囲(5):
    表示(i)
```

### Arabic

```python
لكل i في مدى(5):
    اطبع(i)
```

### Hindi

```python
प्रत्येक i में परास(5):
    छापो(i)
```

### Chinese

```python
对于 i 在 范围(5):
    打印(i)
```

### Tuple Unpacking in For

```python
# English — all languages support tuple targets
let pairs = [(1, "a"), (2, "b"), (3, "c")]

for index, letter in pairs:
    print(f"{index}: {letter}")

# enumerate
for i, val in enumerate(["x", "y", "z"]):
    print(i, val)

# zip
for a, b in zip([1, 2, 3], ["one", "two", "three"]):
    print(a, b)
```

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

```python
let count = 0

while count < 5:
    print(count)
    count += 1
```

### French

```python
soit compteur = 0

tant_que compteur < 5:
    afficher(compteur)
    compteur += 1
```

### Spanish

```python
sea contador = 0

mientras contador < 5:
    imprimir(contador)
    contador += 1
```

### German

```python
sei zaehler = 0

solange zaehler < 5:
    ausgeben(zaehler)
    zaehler += 1
```

### Japanese

```python
変数 カウント = 0

間 カウント < 5:
    表示(カウント)
    カウント += 1
```

### Arabic

```python
متغير عداد = 0

طالما عداد < 5:
    اطبع(عداد)
    عداد += 1
```

### Hindi

```python
चर गिनती = 0

जबकि गिनती < 5:
    छापो(गिनती)
    गिनती += 1
```

### Chinese

```python
变量 计数 = 0

当 计数 < 5:
    打印(计数)
    计数 += 1
```

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

```python
let command = "quit"

match command:
    case "quit":
        print("quitting")
    case "help":
        print("showing help")
    case _:
        print(f"unknown: {command}")
```

### Value Capture

```python
match point:
    case (0, 0):
        print("origin")
    case (x, 0):
        print(f"on x-axis at {x}")
    case (0, y):
        print(f"on y-axis at {y}")
    case (x, y):
        print(f"point at ({x}, {y})")
```

### Guard Conditions

```python
match value:
    case n if n < 0:
        print("negative")
    case n if n == 0:
        print("zero")
    case n:
        print(f"positive: {n}")
```

### OR Patterns

```python
match status:
    case 400 | 401 | 403:
        print("client error")
    case 500 | 502 | 503:
        print("server error")
    case 200:
        print("ok")
```

### AS Pattern

```python
match data:
    case [first, *rest] as full_list:
        print(f"first={first}, full={full_list}")
```

### Class Patterns

```python
from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float

match shape:
    case Point(x=0, y=0):
        print("origin")
    case Point(x=px, y=py):
        print(f"point at {px}, {py}")
```

---

## Break / Continue / Pass

These keywords are universal (not localized) across all languages.

### break — Exit a loop early

```python
for i in range(100):
    if i == 10:
        break
    print(i)
# prints 0 through 9
```

### continue — Skip current iteration

```python
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
# prints 1, 3, 5, 7, 9
```

### pass — No-op placeholder

```python
for item in items:
    pass  # TODO: process item later

def not_implemented_yet():
    pass
```

---

## Nested Loops

```python
# Multiplication table
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i}×{j}={i*j}", end="  ")
    print()
```

French version:

```python
pour i dans intervalle(1, 4):
    pour j dans intervalle(1, 4):
        afficher(f"{i}×{j}={i*j}", fin="  ")
    afficher()
```

---

## Loop-Else Idiom

```python
# Search with for-else
let target = 7
let numbers = [1, 3, 5, 7, 9]

for n in numbers:
    if n == target:
        print(f"Found {target}")
        break
else:
    print(f"{target} not found")

# While-else
let x = 10
while x > 0:
    x -= 3
    if x == 1:
        break
else:
    print("loop finished normally")
```

---

## Walrus Operator in Conditions

```python
import re

let lines = ["hello world", "foo bar", "test 123"]

for line in lines:
    if m := re.search(r"\d+", line):
        print(f"Found number: {m.group()} in '{line}'")
```

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
