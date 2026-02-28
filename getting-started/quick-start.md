---
layout: page
title: "Quick Start"
description: "A 10-minute tour of multilingual features: variables, control flow, functions, classes, and more."
category: "Getting Started"
permalink: /getting-started/quick-start/
prev_page:
  title: "Installation"
  url: /getting-started/installation/
next_page:
  title: "REPL Guide"
  url: /getting-started/repl/
---

This guide walks through the core language features in 10 minutes using English. Every construct shown here is available in all 17 languages — see the [Language Guide](/language-guide/all-languages/) for equivalents.

---

## Variables

Use `let` to declare a variable:

```python
let x = 42
let name = "Alice"
let pi = 3.14159
let active = True
let nothing = None
```

Type annotations are optional:

```python
let count: int = 0
let ratio: float = 0.5
let label: str = "hello"
```

Chained assignment:

```python
let a = let b = let c = 0
```

---

## Arithmetic

Standard arithmetic operators:

```python
let a = 10
let b = 3

print(a + b)    # 13
print(a - b)    # 7
print(a * b)    # 30
print(a / b)    # 3.3333...
print(a // b)   # 3   (floor division)
print(a % b)    # 1   (modulo)
print(a ** b)   # 1000 (power)
```

Augmented assignment:

```python
let x = 10
x += 5    # x = 15
x -= 3    # x = 12
x *= 2    # x = 24
x //= 4   # x = 6
x **= 2   # x = 36
```

---

## Strings and F-Strings

```python
let first = "Hello"
let last = "World"
let greeting = f"{first}, {last}!"
print(greeting)   # Hello, World!

# Format specifiers
let pi = 3.14159
print(f"Pi is {pi:.2f}")   # Pi is 3.14

# Triple-quoted strings
let poem = """
Line one
Line two
Line three
"""
```

---

## Control Flow

### if / elif / else

```python
let score = 85

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("F")
```

### Ternary (inline if)

```python
let x = 10
let label = "even" if x % 2 == 0 else "odd"
print(label)  # even
```

### Walrus Operator

```python
let data = [1, 2, 3, 4, 5]
if (n := len(data)) > 3:
    print(f"Long list: {n} items")
```

---

## Loops

### for loop

```python
for i in range(5):
    print(i)   # 0, 1, 2, 3, 4

# Iterate over a list
let fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# With enumerate
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")
```

### for / else

```python
for i in range(5):
    if i == 3:
        break
else:
    print("Loop completed without break")
```

### while loop

```python
let count = 0
while count < 5:
    print(count)
    count += 1
```

### break and continue

```python
for i in range(10):
    if i % 2 == 0:
        continue   # skip even
    if i > 7:
        break
    print(i)   # 1, 3, 5, 7
```

---

## Data Structures

### Lists

```python
let numbers = [1, 2, 3, 4, 5]
let first = numbers[0]       # 1
let last = numbers[-1]       # 5
let slice_ = numbers[1:3]    # [2, 3]
let reversed_ = numbers[::-1] # [5, 4, 3, 2, 1]
numbers.append(6)
print(len(numbers))          # 6
```

### Tuples

```python
let point = (3, 4)
let x, y = point

# Starred unpacking
let first_, *rest_ = [1, 2, 3, 4, 5]
let a_, *middle_, z_ = [1, 2, 3, 4, 5]
```

### Dictionaries

```python
let person = {"name": "Alice", "age": 30}
print(person["name"])         # Alice
person["city"] = "Paris"

# Dict comprehension
let squares = {n: n**2 for n in range(5)}

# Merging (dict unpacking)
let merged = {**person, **{"country": "France"}}
```

### Sets

```python
let unique = {1, 2, 3, 2, 1}   # {1, 2, 3}
let evens = {x for x in range(10) if x % 2 == 0}
```

---

## Functions

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Alice"))           # Hello, Alice!
print(greet("Bob", "Hi"))       # Hi, Bob!
```

### *args and **kwargs

```python
def sum_all(*numbers):
    return sum(numbers)

def show_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

print(sum_all(1, 2, 3, 4))
show_info(name="Alice", age=30)
```

### Positional-Only and Keyword-Only

```python
def format_data(a, b, /, *, sep=", "):
    return f"{a}{sep}{b}"

print(format_data("x", "y"))         # x, y
print(format_data("x", "y", sep="—"))  # x—y
```

### Type Annotations

```python
def add(x: int, y: int) -> int:
    return x + y

def repeat(s: str, n: int = 1) -> str:
    return s * n
```

### Lambda

```python
let square = lambda x: x ** 2
let numbers_ = [3, 1, 4, 1, 5]
let sorted_ = sorted(numbers_, key=lambda x: -x)
```

---

## Comprehensions

```python
# List comprehension
let squares = [x**2 for x in range(10) if x % 2 == 0]

# Nested comprehension
let matrix = [[i * j for j in range(3)] for i in range(3)]
let flat = [x for row in matrix for x in row]

# Dict comprehension
let word_lengths = {word: len(word) for word in ["apple", "banana"]}

# Set comprehension
let unique_lengths = {len(word) for word in ["hi", "hello", "hey"]}

# Generator expression
let total = sum(x**2 for x in range(100))
```

---

## Classes

```python
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        return f"{self.name} says {self.sound}"

    def __repr__(self):
        return f"Animal({self.name!r})"


class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name, "Woof")

    def fetch(self, item):
        return f"{self.name} fetches the {item}!"


let dog = Dog("Rex")
print(dog.speak())        # Rex says Woof
print(dog.fetch("ball"))  # Rex fetches the ball!
```

---

## Exception Handling

```python
try:
    let result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
except (TypeError, ValueError) as e:
    print(f"Type/Value error: {e}")
else:
    print("No error occurred")
finally:
    print("Always runs")

# raise
def validate_age(age):
    if age < 0:
        raise ValueError(f"Age cannot be negative: {age}")
    return age

# raise ... from (exception chaining)
try:
    int("not a number")
except ValueError as e:
    raise RuntimeError("Conversion failed") from e
```

---

## Context Managers

```python
# File I/O
with open("data.txt", "w", encoding="utf-8") as f:
    f.write("hello")

with open("data.txt", "r", encoding="utf-8") as f:
    let content = f.read()

# Multiple context managers
with open("in.txt") as src, open("out.txt", "w") as dst:
    dst.write(src.read())
```

---

## Generators

```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for num in countdown(5):
    print(num)  # 5, 4, 3, 2, 1

# yield from
def chain(*iterables):
    for it in iterables:
        yield from it

let combined = list(chain([1, 2], [3, 4], [5]))
```

---

## Async / Await

```python
import asyncio

async def fetch_data(url):
    await asyncio.sleep(0.1)  # simulate I/O
    return f"Data from {url}"

async def main():
    let result = await fetch_data("https://example.com")
    print(result)

asyncio.run(main())
```

---

## Pattern Matching

```python
let command = "quit"

match command:
    case "quit":
        print("Quitting...")
    case "help":
        print("Help menu")
    case str(c) if c.startswith("go "):
        print(f"Going to: {c[3:]}")
    case _:
        print(f"Unknown command: {command}")
```

---

## Imports

```python
import math
from math import sqrt, pi
from math import sqrt as root

print(math.factorial(10))
print(root(16))        # 4.0
print(pi)              # 3.14159...
```

---

## Next: All 17 Languages

Every feature above is available in all 17 supported languages.
See [All Languages Reference](/language-guide/all-languages/) for the complete keyword and syntax mapping.
