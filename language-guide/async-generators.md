---
layout: page
title: "Async & Generators"
description: "async/await, async for, async with, generators, and yield — in all 17 languages."
category: "Language Guide"
permalink: /language-guide/async-generators/
prev_page:
  title: "Functions & Classes"
  url: /language-guide/functions-classes/
next_page:
  title: "All 17 Languages"
  url: /language-guide/all-languages/
---

Generators and async constructs in multilingual support the full Python model with localized keywords for `yield`, `async`, `await`, `async for`, and `async with`.

---

## Generators

### Syntax

```text
[DEF] name(params):
    [YIELD] expression
    [YIELD] [FROM] iterable
```

A function containing `yield` becomes a generator — it can produce a sequence of values lazily without building them all in memory.

### English

```python
def count_up(n):
    let i = 0
    while i < n:
        yield i
        i += 1

for val in count_up(5):
    print(val)
# 0, 1, 2, 3, 4
```

### French

```python
fonction compter(n):
    soit i = 0
    tant_que i < n:
        produire i
        i += 1

pour valeur dans compter(5):
    afficher(valeur)
```

### Spanish

```python
función contar(n):
    sea i = 0
    mientras i < n:
        producir i
        i += 1

para valor en contar(5):
    imprimir(valor)
```

### German

```python
funktion zaehlen(n):
    sei i = 0
    solange i < n:
        ergeben i
        i += 1

für wert in zaehlen(5):
    ausgeben(wert)
```

### Japanese

```python
関数 カウント(n):
    変数 i = 0
    間 i < n:
        産出 i
        i += 1

毎 値 中 カウント(5):
    表示(値)
```

### Arabic

```python
دالة عدّ(ن):
    متغير ي = 0
    طالما ي < ن:
        أنتج ي
        ي += 1

لكل قيمة في عدّ(5):
    اطبع(قيمة)
```

### Hindi

```python
कार्य गिनती(n):
    चर i = 0
    जबकि i < n:
        उत्पन्न i
        i += 1

प्रत्येक मूल्य में गिनती(5):
    छापो(मूल्य)
```

### Chinese

```python
函数 计数(n):
    变量 i = 0
    当 i < n:
        产出 i
        i += 1

对于 值 在 计数(5):
    打印(值)
```

---

## yield from

`yield from` delegates to another iterable or generator:

```python
def chain(*iterables):
    for it in iterables:
        yield from it

for item in chain([1, 2], [3, 4], [5]):
    print(item)
# 1, 2, 3, 4, 5
```

### Recursive Generator

```python
def flatten(nested):
    for item in nested:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item

let data = [1, [2, [3, 4]], [5, 6]]
print(list(flatten(data)))  # [1, 2, 3, 4, 5, 6]
```

---

## Generator Expressions

Generator expressions produce lazy sequences without a function definition:

```python
# Generator expression (lazy)
let squares_gen = (x**2 for x in range(10))

# vs list comprehension (eager)
let squares_list = [x**2 for x in range(10)]

# Useful in function calls — avoids building a list
print(sum(x**2 for x in range(100)))      # 328350
print(max(len(w) for w in ["hello", "world", "!"]))  # 5
```

---

## Generator Use Cases

### Infinite Sequences

```python
def fibonacci():
    let a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Take first 10 fibonacci numbers
import itertools
let fibs = list(itertools.islice(fibonacci(), 10))
print(fibs)  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

### File Streaming (Memory Efficient)

```python
def read_chunks(filename, chunk_size=1024):
    with open(filename, "rb") as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            yield chunk

for chunk in read_chunks("large_file.bin"):
    process(chunk)
```

### Pipeline Pattern

```python
def integers_from(n):
    while True:
        yield n
        n += 1

def take(n, gen):
    for _ in range(n):
        yield next(gen)

def squares(gen):
    for x in gen:
        yield x ** 2

# Compose pipelines
let result = list(take(5, squares(integers_from(1))))
print(result)  # [1, 4, 9, 16, 25]
```

---

## Async Functions

### Syntax

```text
[ASYNC] [DEF] name(params):
    [AWAIT] expression
```

### English

```python
import asyncio

async def fetch_data(url):
    await asyncio.sleep(0.1)   # simulate network delay
    return f"data from {url}"

async def main():
    result = await fetch_data("https://example.com")
    print(result)

asyncio.run(main())
```

### French

```python
import asyncio

async_fonction récupérer(url):
    attendre asyncio.sleep(0.1)
    retourner f"données de {url}"

async_fonction principale():
    résultat = attendre récupérer("https://exemple.com")
    afficher(résultat)

asyncio.run(principale())
```

### Spanish

```python
import asyncio

función_async obtener(url):
    esperar asyncio.sleep(0.1)
    retornar f"datos de {url}"

función_async principal():
    resultado = esperar obtener("https://ejemplo.com")
    imprimir(resultado)

asyncio.run(principal())
```

### German

```python
import asyncio

async_funktion abrufen(url):
    erwarten asyncio.sleep(0.1)
    zurückgeben f"Daten von {url}"

async_funktion hauptprogramm():
    ergebnis = erwarten abrufen("https://beispiel.com")
    ausgeben(ergebnis)

asyncio.run(hauptprogramm())
```

### Japanese

```python
import asyncio

非同期関数 取得(url):
    待つ asyncio.sleep(0.1)
    戻る f"{url}からのデータ"

非同期関数 メイン():
    結果 = 待つ 取得("https://example.com")
    表示(結果)

asyncio.run(メイン())
```

### Arabic

```python
import asyncio

دالة_غير_متزامنة جلب(رابط):
    انتظر asyncio.sleep(0.1)
    أرجع f"بيانات من {رابط}"

دالة_غير_متزامنة رئيسي():
    نتيجة = انتظر جلب("https://example.com")
    اطبع(نتيجة)

asyncio.run(رئيسي())
```

---

## Async For

Iterating over async iterables:

### Syntax

```text
[ASYNC] [FOR] target [IN] async_iterable:
    block
```

### English

```python
import asyncio

class AsyncCounter:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.current >= self.limit:
            raise StopAsyncIteration
        await asyncio.sleep(0)
        self.current += 1
        return self.current


async def main():
    async for n in AsyncCounter(5):
        print(n)

asyncio.run(main())
# 1, 2, 3, 4, 5
```

### French

```python
import asyncio

async_classe CompteurAsync:
    définir __init__(soi, limite):
        soi.limite = limite
        soi.actuel = 0

    définir __aiter__(soi):
        retourner soi

    async_définir __anext__(soi):
        si soi.actuel >= soi.limite:
            lever StopAsyncIteration
        attendre asyncio.sleep(0)
        soi.actuel += 1
        retourner soi.actuel

async_fonction principale():
    async_pour n dans CompteurAsync(5):
        afficher(n)

asyncio.run(principale())
```

---

## Async With (Context Managers)

```text
[ASYNC] [WITH] expression [AS] name:
    block
```

```python
import asyncio

class AsyncResource:
    async def __aenter__(self):
        print("acquiring resource")
        await asyncio.sleep(0)
        return self

    async def __aexit__(self, exc_type, exc, tb):
        print("releasing resource")
        await asyncio.sleep(0)
        return False

    async def use(self):
        return "resource data"


async def main():
    async with AsyncResource() as res:
        data = await res.use()
        print(data)

asyncio.run(main())
```

---

## Complete Async Example

```python
import asyncio

async def fetch(session, url):
    """Simulates an async HTTP request."""
    await asyncio.sleep(0.05)  # simulate latency
    return {"url": url, "status": 200, "data": f"content of {url}"}

async def fetch_all(urls):
    """Fetch multiple URLs concurrently."""
    tasks = [fetch(None, url) for url in urls]
    results = await asyncio.gather(*tasks)
    return results

async def process_stream(data_source):
    """Process an async iterator."""
    let total = 0
    async for item in data_source:
        total += item
    return total

async def main():
    let urls = [
        "https://example.com/page1",
        "https://example.com/page2",
        "https://example.com/page3",
    ]

    print("Fetching concurrently...")
    let results = await fetch_all(urls)
    for r in results:
        print(f"  {r['url']}: {r['status']}")

asyncio.run(main())
```

---

## Async Generators

A function that combines `async def` and `yield` is an async generator:

```python
import asyncio

async def async_range(n, delay=0.01):
    for i in range(n):
        await asyncio.sleep(delay)
        yield i

async def main():
    async for val in async_range(5):
        print(val)

asyncio.run(main())
# 0, 1, 2, 3, 4 (with delays)
```

---

## Running Async Code

```python
import asyncio

# Method 1: asyncio.run() — standard for Python 3.7+
asyncio.run(main())

# Method 2: event loop (lower level)
loop = asyncio.get_event_loop()
loop.run_until_complete(main())

# Method 3: gather — run multiple coroutines concurrently
async def main():
    results = await asyncio.gather(
        coroutine_1(),
        coroutine_2(),
        coroutine_3(),
    )
    return results
```

---

## Async / Generator Keyword Table

| Concept | en | fr | es | de | ja | ar | hi | zh |
|---------|----|----|----|----|----|----|----|----|
| async def | `async def` | `async_fonction` | `función_async` | `async_funktion` | `非同期関数` | `دالة_غير_متزامنة` | `असंकालिक_कार्य` | `异步函数` |
| await | `await` | `attendre` | `esperar` | `erwarten` | `待つ` | `انتظر` | `प्रतीक्षा` | `等待` |
| yield | `yield` | `produire` | `producir` | `ergeben` | `産出` | `أنتج` | `उत्पन्न` | `产出` |
| yield from | `yield from` | `produire de` | `producir de` | `ergeben von` | `産出から` | `أنتج من` | `उत्पन्न से` | `从产出` |
| async for | `async for` | `async_pour` | `para_async` | `async_für` | `非同期毎` | `غير_متزامن_لكل` | `असंकालिक_प्रत्येक` | `异步对于` |
| async with | `async with` | `async_avec` | `async_con` | `async_mit` | `非同期と共に` | `غير_متزامن_مع` | `असंकालिक_साथ` | `异步以` |

See [Keywords Reference](/language-guide/keywords/) for all 17 languages.
