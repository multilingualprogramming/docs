---
layout: page
title: "Syntax Reference"
description: "Complete syntax reference for every construct supported by multilingual."
category: "Language Guide"
permalink: /language-guide/syntax/
prev_page:
  title: "All 17 Languages"
  url: /language-guide/all-languages/
next_page:
  title: "Control Flow"
  url: /language-guide/control-flow/
---

This page is the definitive syntax reference for multilingual. Keywords shown in `[CONCEPT]` form refer to semantic concepts — replace them with the appropriate keyword for your chosen language.

See [Keywords Reference](/language-guide/keywords/) for the full mapping.

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
```python
let x = 42
let name: str = "Alice"
```

### Constants

```text
const IDENTIFIER = expression
```

```python
const MAX_SIZE = 1000
const PI = 3.14159
```

### Chained Assignment

```text
identifier = identifier = expression
[LET] a = [LET] b = expression
```

```python
let a = let b = let c = 0
x = y = z = 10
```

### Delete

```text
del identifier
```

### Augmented Assignment

```python
x += 5
x -= 3
x *= 2
x /= 4
x //= 3
x %= 7
x **= 2
x &= 0xFF
x |= 0x01
x ^= 0x10
x <<= 2
x >>= 1
```

---

## Literals

### Numbers

```python
let i = 42          # integer
let f = 3.14        # float
let sci = 1.5e10    # scientific notation
let h = 0xFF        # hexadecimal
let o = 0o77        # octal
let b = 0b1010      # binary
let c = 3 + 4j      # complex number
```

### Strings

```python
let s1 = "hello"
let s2 = 'hello'
let s3 = """
multi-line
string
"""
let name = "World"
let f1 = f"Hello, {name}!"
let f2 = f"Pi = {3.14159:.2f}"
let f3 = f"{value!r}"    # repr format
let f4 = f"{value!s}"    # str format
let f5 = f"{value!a}"    # ascii format
```

### Booleans and None

```python
let t = True
let f = False
let n = None
```

### Collections

```python
let lst = [1, 2, 3]             # list
let dct = {"a": 1, "b": 2}     # dict
let st = {1, 2, 3}             # set
let tpl = (1, 2, 3)            # tuple
let empty_list = []
let empty_dict = {}
let empty_set = set()
let empty_tuple = ()
```

---

## Expressions

### Arithmetic

```python
a + b    # addition
a - b    # subtraction
a * b    # multiplication
a / b    # true division
a // b   # floor division
a % b    # modulo
a ** b   # power
-a       # negation
```

### Comparison

```python
a == b    # equal
a != b    # not equal
a < b     # less than
a > b     # greater than
a <= b    # less or equal
a >= b    # greater or equal
a is b    # identity
a is not b
a in b    # membership
a not in b
```

### Boolean

```python
a and b
a or b
not a
```

### Bitwise

```python
a & b    # AND
a | b    # OR
a ^ b    # XOR
~a       # NOT
a << n   # left shift
a >> n   # right shift
```

### Slicing

```python
lst[0]        # index
lst[-1]       # from end
lst[1:3]      # slice
lst[::2]      # step
lst[::-1]     # reverse
lst[1:8:2]    # start:stop:step
```

### Walrus Operator

```python
if (n := len(data)) > 10:
    print(f"Long: {n}")
```

### Ternary Expression

```text
value_if_true [IF] condition [ELSE] value_if_false
```

```python
let label = "even" if x % 2 == 0 else "odd"
```

### Unpacking

```python
let a, b, c = [1, 2, 3]
let first, *rest = [1, 2, 3, 4]
let a_, *mid, last_ = [1, 2, 3, 4, 5]
let x_, y_ = (10, 20)
```

### Dict/Set Unpacking

```python
let merged = {**d1, **d2}
```

### Lambda

```text
lambda params: expression
```

```python
let sq = lambda x: x**2
let add = lambda x, y: x + y
```

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
```python
for i, v in enumerate([10, 20, 30]):
    print(i, v)
```

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

```python
for i in range(10):
    if i == 5:
        break
    if i % 2 == 0:
        continue
    pass    # no-op placeholder
```

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

```python
def f(
    pos_only_a,
    pos_only_b,
    /,          # positional-only boundary
    regular,
    *args,      # variable positional
    kw_only,    # keyword-only
    **kwargs    # variable keyword
):
    pass
```

### Default Values

```python
def greet(name, greeting="Hello", times=1):
    for _ in range(times):
        print(f"{greeting}, {name}")
```

### Type Annotations

```python
def add(x: int, y: int) -> int:
    return x + y

def process(items: list, limit: int = 10) -> dict:
    return {}
```

### Generators

```text
[DEF] name(params):
    [YIELD] expression
    [YIELD] [FROM] iterable
```

```python
def count_up(n):
    for i in range(n):
        yield i

def chain(*iterables):
    for it in iterables:
        yield from it
```

### Async Functions

```text
[ASYNC] [DEF] name(params):
    [AWAIT] expression
    [ASYNC] [FOR] target [IN] iterable:
        block
    [ASYNC] [WITH] expression [AS] name:
        block
```

```python
import asyncio

async def fetch(url):
    await asyncio.sleep(0.1)
    return f"result from {url}"

async def main():
    result = await fetch("https://example.com")
    print(result)

asyncio.run(main())
```

### Decorators

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("before")
        result = func(*args, **kwargs)
        print("after")
        return result
    return wrapper

@my_decorator
def hello():
    print("hello!")

# Multiple decorators (applied bottom-up)
@decorator1
@decorator2
def my_func():
    pass
```

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

```python
class MyClass:
    class_var = 0

    @staticmethod
    def static_method():
        return "static"

    @classmethod
    def class_method(cls):
        return cls.class_var

    def instance_method(self):
        return self

    def __repr__(self):
        return f"MyClass()"
```

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

```python
with open("file.txt", "r") as f:
    content = f.read()

with open("in.txt") as src, open("out.txt", "w") as dst:
    dst.write(src.read())
```

---

## Comprehensions

### List Comprehension

```python
[x**2 for x in range(10)]
[x for x in items if x > 0]
[x for row in matrix for x in row]  # nested
```

### Dict Comprehension

```python
{k: v for k, v in pairs}
{k: v for k, v in d.items() if v > 0}
```

### Set Comprehension

```python
{x**2 for x in range(10)}
{len(w) for w in words if w}
```

### Generator Expression

```python
sum(x**2 for x in range(100))
list(x for x in items if x > 0)
```

---

## Imports

```text
[IMPORT] module
[FROM] module [IMPORT] name
[FROM] module [IMPORT] name [AS] alias
[FROM] module [IMPORT] *
```

```python
import math
from math import sqrt
from math import sqrt as root
from os import *
```

---

## Global and Nonlocal

```text
[GLOBAL] identifier
[NONLOCAL] identifier
```

```python
count = 0

def increment():
    global count
    count += 1

def outer():
    x = 0
    def inner():
        nonlocal x
        x += 1
    inner()
    return x
```

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

```python
BaseException
Exception
ArithmeticError
FloatingPointError
OverflowError
ZeroDivisionError
LookupError
IndexError
KeyError
NameError
UnboundLocalError
TypeError
ValueError
AttributeError
ImportError
ModuleNotFoundError
OSError
FileNotFoundError
FileExistsError
PermissionError
IOError
RuntimeError
RecursionError
NotImplementedError
StopIteration
StopAsyncIteration
GeneratorExit
SystemExit
KeyboardInterrupt
MemoryError
BufferError
EOFError
ConnectionError
TimeoutError
UnicodeError
UnicodeDecodeError
UnicodeEncodeError
SyntaxError
IndentationError
TabError
AssertionError
SystemError
ReferenceError
ExceptionGroup
BaseExceptionGroup
# ... and all Warning subclasses
```
