---
page_id: language_guide__async_generators
locale: fr
title: Asynchrone et generateurs
path_segments:
- guide-langage
- asynchrone-generateurs
source_hash: ef520f55de2d
status: translated
permalink: /fr/docs/guide-langage/asynchrone-generateurs/
---



Les generateurs et constructions async dans multilingual prennent en charge le modele Python complet avec mots-cles localises pour `yield`, `async`, `await`, `async for` et `async with`.

---

## Generateurs

### Syntaxe

```text
[DEF] name(params):
    [YIELD] expression
    [YIELD] [FROM] iterable
```

A function containing `yield` becomes a generator — it can produce a sequence of values lazily without building them all in memory.

### Anglais

{{snippet:language_guide__async_generators__py01}}

### Francais

{{snippet:language_guide__async_generators__py02}}

### Espagnol

{{snippet:language_guide__async_generators__py03}}

### Allemand

{{snippet:language_guide__async_generators__py04}}

### Japonais

{{snippet:language_guide__async_generators__py05}}

### Arabe

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

## Fonctions asynchrones

### Syntaxe

```text
[ASYNC] [DEF] name(params):
    [AWAIT] expression
```

### Anglais

{{snippet:language_guide__async_generators__py15}}

### Francais

{{snippet:language_guide__async_generators__py16}}

### Espagnol

{{snippet:language_guide__async_generators__py17}}

### Allemand

{{snippet:language_guide__async_generators__py18}}

### Japonais

{{snippet:language_guide__async_generators__py19}}

### Arabe

{{snippet:language_guide__async_generators__py20}}

---

## Boucles async for

Iterating over async iterables:

### Syntaxe

```text
[ASYNC] [FOR] target [IN] async_iterable:
    block
```

### Anglais

{{snippet:language_guide__async_generators__py21}}

### Francais

{{snippet:language_guide__async_generators__py22}}

---

## Async with (gestionnaires de contexte)

```text
[ASYNC] [WITH] expression [AS] name:
    block
```

{{snippet:language_guide__async_generators__py23}}

---

## Exemple async complet

{{snippet:language_guide__async_generators__py24}}

---

## Generateurs asynchrones

A function that combines `async def` and `yield` is an async generator:

{{snippet:language_guide__async_generators__py25}}

---

## Execution de code async

{{snippet:language_guide__async_generators__py26}}

---

## Table des mots-cles async/generateur

| Concept | en | fr | es | de | ja | ar | hi | zh |
|---------|----|----|----|----|----|----|----|----|
| async def | `async def` | `async_fonction` | `función_async` | `async_funktion` | `非同期関数` | `دالة_غير_متزامنة` | `असंकालिक_कार्य` | `异步函数` |
| await | `await` | `attendre` | `esperar` | `erwarten` | `待つ` | `انتظر` | `प्रतीक्षा` | `等待` |
| yield | `yield` | `produire` | `producir` | `ergeben` | `産出` | `أنتج` | `उत्पन्न` | `产出` |
| yield from | `yield from` | `produire de` | `producir de` | `ergeben von` | `産出から` | `أنتج من` | `उत्पन्न से` | `从产出` |
| async for | `async for` | `async_pour` | `para_async` | `async_für` | `非同期毎` | `غير_متزامن_لكل` | `असंकालिक_प्रत्येक` | `异步对于` |
| async with | `async with` | `async_avec` | `async_con` | `async_mit` | `非同期と共に` | `غير_متزامن_مع` | `असंकालिक_साथ` | `异步以` |

Voir [Reference des mots-cles](/fr/docs/guide-langage/mots-cles/) pour les 17 langues.
