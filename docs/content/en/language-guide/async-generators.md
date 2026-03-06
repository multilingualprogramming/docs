---
page_id: language_guide__async_generators
locale: en
title: Async & Generators
path_segments:
- language-guide
- async-generators
source_hash: ef520f55de2d
status: source
permalink: /en/docs/language-guide/async-generators/
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

{{snippet:language_guide__async_generators__py01}}

### French

{{snippet:language_guide__async_generators__py02}}

### Spanish

{{snippet:language_guide__async_generators__py03}}

### German

{{snippet:language_guide__async_generators__py04}}

### Japanese

{{snippet:language_guide__async_generators__py05}}

### Arabic

{{snippet:language_guide__async_generators__py06}}

### Hindi

{{snippet:language_guide__async_generators__py07}}

### Chinese

{{snippet:language_guide__async_generators__py08}}

---

## yield from

`yield from` delegates to another iterable or generator:

{{snippet:language_guide__async_generators__py09}}

### Recursive Generator

{{snippet:language_guide__async_generators__py10}}

---

## Generator Expressions

Generator expressions produce lazy sequences without a function definition:

{{snippet:language_guide__async_generators__py11}}

---

## Generator Use Cases

### Infinite Sequences

{{snippet:language_guide__async_generators__py12}}

### File Streaming (Memory Efficient)

{{snippet:language_guide__async_generators__py13}}

### Pipeline Pattern

{{snippet:language_guide__async_generators__py14}}

---

## Async Functions

### Syntax

```text
[ASYNC] [DEF] name(params):
    [AWAIT] expression
```

### English

{{snippet:language_guide__async_generators__py15}}

### French

{{snippet:language_guide__async_generators__py16}}

### Spanish

{{snippet:language_guide__async_generators__py17}}

### German

{{snippet:language_guide__async_generators__py18}}

### Japanese

{{snippet:language_guide__async_generators__py19}}

### Arabic

{{snippet:language_guide__async_generators__py20}}

---

## Async For

Iterating over async iterables:

### Syntax

```text
[ASYNC] [FOR] target [IN] async_iterable:
    block
```

### English

{{snippet:language_guide__async_generators__py21}}

### French

{{snippet:language_guide__async_generators__py22}}

---

## Async With (Context Managers)

```text
[ASYNC] [WITH] expression [AS] name:
    block
```

{{snippet:language_guide__async_generators__py23}}

---

## Complete Async Example

{{snippet:language_guide__async_generators__py24}}

---

## Async Generators

A function that combines `async def` and `yield` is an async generator:

{{snippet:language_guide__async_generators__py25}}

---

## Running Async Code

{{snippet:language_guide__async_generators__py26}}

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

See [Keywords Reference]({{ '/en/docs/language-guide/keywords/' | relative_url }}) for all 17 languages.
