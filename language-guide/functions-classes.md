---
layout: page
title: "Functions & Classes"
description: "Defining functions, classes, and using decorators — in all 17 languages."
category: "Language Guide"
permalink: /language-guide/functions-classes/
prev_page:
  title: "Control Flow"
  url: /language-guide/control-flow/
next_page:
  title: "Async & Generators"
  url: /language-guide/async-generators/
---

Functions and classes in multilingual work exactly like Python, with localized keywords for `def`, `class`, `return`, `self`, and related constructs. Identifiers (variable names, function names, class names) are never translated — they remain as-is in the generated Python.

---

## Function Definitions

### Syntax

```text
[DEF] name(params):
    [RETURN] expression
```

### English

```python
def greet(name):
    return f"Hello, {name}!"

print(greet("World"))
```

### French

```python
fonction saluer(nom):
    retourner f"Bonjour, {nom}!"

afficher(saluer("Monde"))
```

### Spanish

```python
función saludar(nombre):
    retornar f"Hola, {nombre}!"

imprimir(saludar("Mundo"))
```

### German

```python
funktion begrüßen(name):
    zurückgeben f"Hallo, {name}!"

ausgeben(begrüßen("Welt"))
```

### Japanese

```python
関数 挨拶(名前):
    戻る f"こんにちは、{名前}！"

表示(挨拶("世界"))
```

### Arabic

```python
دالة تحية(اسم):
    أرجع f"مرحبا، {اسم}!"

اطبع(تحية("العالم"))
```

### Hindi

```python
कार्य अभिवादन(नाम):
    वापस f"नमस्ते, {नाम}!"

छापो(अभिवादन("दुनिया"))
```

### Chinese

```python
函数 问候(名字):
    返回 f"你好, {名字}!"

打印(问候("世界"))
```

---

## Parameter Types

All Python parameter forms are supported across all languages:

```python
def f(
    pos_only_a,
    pos_only_b,
    /,           # positional-only boundary
    regular,
    *args,       # variable positional
    kw_only,     # keyword-only (after *)
    **kwargs     # variable keyword
):
    pass
```

### Default Values

```python
def greet(name, greeting="Hello", times=1):
    for _ in range(times):
        print(f"{greeting}, {name}!")

greet("Alice")                    # Hello, Alice!
greet("Bob", greeting="Hi")      # Hi, Bob!
greet("Carol", times=3)          # Hello, Carol! (×3)
```

### Type Annotations

```python
def add(x: int, y: int) -> int:
    return x + y

def process(items: list, limit: int = 10) -> dict:
    return {i: items[i] for i in range(min(limit, len(items)))}
```

### *args and **kwargs

```python
def variadic(*args, **kwargs):
    print("positional:", args)
    print("keyword:", kwargs)

variadic(1, 2, 3, name="Alice", age=30)
```

### Keyword-Only Arguments

```python
def connect(host, port, *, timeout=30, retries=3):
    print(f"Connecting to {host}:{port}, timeout={timeout}")

connect("localhost", 5432, timeout=60)
```

---

## Return Values

### Single Value

```python
def square(n):
    return n ** 2
```

### Multiple Values (tuple)

```python
def min_max(lst):
    return min(lst), max(lst)

lo, hi = min_max([3, 1, 4, 1, 5, 9, 2, 6])
print(lo, hi)  # 1 9
```

### No Return (None)

```python
def print_banner(text):
    print("=" * 40)
    print(text.center(40))
    print("=" * 40)
    # implicit return None
```

---

## Nested Functions and Closures

```python
def make_counter(start=0):
    let count = start

    def increment(by=1):
        nonlocal count
        count += by
        return count

    return increment

counter = make_counter(10)
print(counter())    # 11
print(counter(5))   # 16
```

---

## Decorators

### Basic Decorator

```python
def log_calls(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Done: {result}")
        return result
    return wrapper

@log_calls
def add(x, y):
    return x + y

add(3, 4)
# Calling add
# Done: 7
```

### Multiple Decorators

Decorators are applied bottom-up:

```python
@decorator_a
@decorator_b
@decorator_c
def my_func():
    pass
# equivalent to: decorator_a(decorator_b(decorator_c(my_func)))
```

### functools.wraps

```python
import functools

def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```

---

## Lambda Functions

```python
let square = lambda x: x ** 2
let add = lambda x, y: x + y
let clamp = lambda val, lo, hi: max(lo, min(hi, val))

print(square(5))       # 25
print(add(3, 4))       # 7
print(clamp(15, 0, 10))  # 10
```

---

## Class Definitions

### Syntax

```text
[CLASS] Name:
    [DEF] __init__(self, params):
        self.attr = value

    [DEF] method(self):
        [RETURN] expression
```

### English

```python
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        return f"{self.name} says {self.sound}"

let dog = Animal("Dog", "woof")
print(dog.speak())  # Dog says woof
```

### French

```python
classe Animal:
    définir __init__(soi, nom, son):
        soi.nom = nom
        soi.son = son

    définir parler(soi):
        retourner f"{soi.nom} dit {soi.son}"

soit chien = Animal("Chien", "ouaf")
afficher(chien.parler())
```

### Japanese

```python
クラス 動物:
    関数 __init__(自分, 名前, 鳴き声):
        自分.名前 = 名前
        自分.鳴き声 = 鳴き声

    関数 話す(自分):
        戻る f"{自分.名前}は{自分.鳴き声}と言います"

変数 犬 = 動物("犬", "ワン")
表示(犬.話す())
```

### Arabic

```python
فئة حيوان:
    دالة __init__(النفس, اسم, صوت):
        النفس.اسم = اسم
        النفس.صوت = صوت

    دالة يتحدث(النفس):
        أرجع f"{النفس.اسم} يقول {النفس.صوت}"

متغير كلب = حيوان("كلب", "هاو")
اطبع(كلب.يتحدث())
```

---

## Inheritance

### Single Inheritance

```python
class Shape:
    def __init__(self, color="black"):
        self.color = color

    def area(self):
        return 0

    def describe(self):
        return f"A {self.color} shape with area {self.area()}"


class Circle(Shape):
    def __init__(self, radius, color="black"):
        super(Circle, self).__init__(color)
        self.radius = radius

    def area(self):
        import math
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height, color="black"):
        super(Rectangle, self).__init__(color)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


let c = Circle(5, "red")
let r = Rectangle(4, 6, "blue")
print(c.describe())   # A red shape with area 78.539...
print(r.describe())   # A blue shape with area 24
```

### Multiple Inheritance

```python
class Flyable:
    def fly(self):
        return "flying"

class Swimmable:
    def swim(self):
        return "swimming"

class Duck(Flyable, Swimmable):
    def quack(self):
        return "quack"

let donald = Duck()
print(donald.fly())    # flying
print(donald.swim())   # swimming
print(donald.quack())  # quack
```

---

## Class Features

### Class and Static Methods

```python
class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1
        self.id = Counter.count

    @classmethod
    def get_count(cls):
        return cls.count

    @staticmethod
    def describe():
        return "I count instances"

    def __repr__(self):
        return f"Counter(id={self.id})"


let a = Counter()
let b = Counter()
print(Counter.get_count())   # 2
print(Counter.describe())    # I count instances
print(a)                     # Counter(id=1)
```

### Properties

```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Below absolute zero!")
        self._celsius = value

    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32


let temp = Temperature(100)
print(temp.celsius)      # 100
print(temp.fahrenheit)   # 212.0
temp.celsius = 0
print(temp.fahrenheit)   # 32.0
```

### Dunder Methods

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __len__(self):
        return 2

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


let v1 = Vector(1, 2)
let v2 = Vector(3, 4)
print(v1 + v2)       # Vector(4, 6)
print(v1 * 3)        # Vector(3, 6)
print(len(v1))       # 2
print(v1 == Vector(1, 2))  # True
```

---

## Dataclasses

```python
from dataclasses import dataclass, field

@dataclass
class Point:
    x: float
    y: float
    label: str = ""

    def distance_from_origin(self):
        return (self.x**2 + self.y**2) ** 0.5


@dataclass
class Polygon:
    vertices: list = field(default_factory=list)

    def add_vertex(self, point):
        self.vertices.append(point)
        return self


let p = Point(3.0, 4.0, "A")
print(p)                           # Point(x=3.0, y=4.0, label='A')
print(p.distance_from_origin())    # 5.0
```

---

## Function Keyword Table

| Concept | en | fr | es | de | ja | ar | hi | zh |
|---------|----|----|----|----|----|----|----|----|
| def | `def` | `fonction` | `función` | `funktion` | `関数` | `دالة` | `कार्य` | `函数` |
| return | `return` | `retourner` | `retornar` | `zurückgeben` | `戻る` | `أرجع` | `वापस` | `返回` |
| class | `class` | `classe` | `clase` | `klasse` | `クラス` | `فئة` | `वर्ग` | `类` |
| self | `self` | `soi` | `yo` | `selbst` | `自分` | `النفس` | `स्वयं` | `自身` |
| super | `super` | `super` | `super` | `super` | `super` | `super` | `super` | `super` |

> `super`, `lambda`, `pass` are universal across all 17 languages.

See [Keywords Reference](/language-guide/keywords/) for all 17 languages.
