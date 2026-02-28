---
layout: page
title: "REPL Guide"
description: "Interactive REPL with language switching, Python preview, and keyword inspection."
category: "Getting Started"
permalink: /getting-started/repl/
prev_page:
  title: "Quick Start"
  url: /getting-started/quick-start/
next_page:
  title: "Language Guide"
  url: /language-guide/
---

The multilingual REPL (Read-Eval-Print Loop) is a language-switching interactive environment for writing and testing programs in any of the 17 supported languages.

---

## Starting the REPL

```bash
# Default (English)
python -m multilingualprogramming repl

# Start in a specific language
python -m multilingualprogramming repl --lang fr
python -m multilingualprogramming repl --lang ja
python -m multilingualprogramming repl --lang ar

# With Python preview (show generated Python alongside output)
python -m multilingualprogramming repl --show-python

# Short command alias
multilg repl --lang de
```

---

## REPL Commands

| Command | Description |
|---------|-------------|
| `:help` | Show all available REPL commands |
| `:language <code>` | Switch active language (e.g., `:language fr`) |
| `:python` | Toggle Python preview mode (show generated Python) |
| `:reset` | Reset interpreter state (clear all variables/functions) |
| `:kw` | List keywords for the current language |
| `:kw XX` | List keywords for language code XX |
| `:ops` | List operators for the current language |
| `:ops XX` | List operators for language code XX |
| `:q` | Quit the REPL |

---

## Example Sessions

### English Session

```
multilingual> let x = 10
multilingual> let y = 25
multilingual> print(x + y)
35
multilingual> def square(n):
...               return n * n
...
multilingual> print(square(7))
49
```

### Language Switching

```
multilingual [en]> :language fr
Switched to: French (fr)
multilingual [fr]> soit a = 5
multilingual [fr]> soit b = 3
multilingual [fr]> afficher(a + b)
8
multilingual [fr]> :language ja
Switched to: Japanese (ja)
multilingual [ja]> 変数 値 = 42
multilingual [ja]> 表示(値)
42
```

### Python Preview Mode

```
multilingual [en]> :python
Python preview: ON
multilingual [en]> let items = [1, 2, 3]
# Python: items = [1, 2, 3]
multilingual [en]> for i in items:
...                    print(i * 2)
# Python:
# for i in items:
#     print(i * 2)
2
4
6
```

### Inspecting Keywords

```
multilingual [fr]> :kw
Keywords for French (fr):
  if          → si
  elif        → sinonsi
  else        → sinon
  for         → pour
  in          → dans
  while       → tantque
  def         → déf
  return      → retourner
  let         → soit
  class       → classe
  ...

multilingual> :kw ar
Keywords for Arabic (ar):
  if      → إذا
  for     → لكل
  while   → بينما
  def     → دالة
  let     → ليكن
  ...
```

---

## Language Codes

| Language | Code | Example keyword |
|----------|------|----------------|
| English | `en` | `if` |
| French | `fr` | `si` |
| Spanish | `es` | `si` |
| German | `de` | `wenn` |
| Italian | `it` | `se` |
| Portuguese | `pt` | `se` |
| Polish | `pl` | `jezeli` |
| Dutch | `nl` | `als` |
| Swedish | `sv` | `om` |
| Danish | `da` | `hvis` |
| Finnish | `fi` | `jos` |
| Hindi | `hi` | `अगर` |
| Arabic | `ar` | `إذا` |
| Bengali | `bn` | `যদি` |
| Tamil | `ta` | `என்றால்` |
| Chinese | `zh` | `如果` |
| Japanese | `ja` | `もし` |

---

## Smoke Tests

Quick validation snippets to verify a language is working correctly.

### Snippet A — Variables and Print

```
<LET> x = 2
<LET> y = 3
<PRINT>(x + y)
```

Replace `<LET>` and `<PRINT>` with the language-specific keywords. Expected output: `5`

### Snippet B — For Loop

```
<LET> total = 0
<FOR> i <IN> <RANGE>(4):
    total = total + i
<PRINT>(total)
```

Expected output: `6`

**English:**

```python
let x = 2
let y = 3
print(x + y)

let total = 0
for i in range(4):
    total = total + i
print(total)
```

**French:**

```python
soit x = 2
soit y = 3
afficher(x + y)

soit total = 0
pour i dans intervalle(4):
    total = total + i
afficher(total)
```

**German:**

```python
sei x = 2
sei y = 3
ausgeben(x + y)

sei total = 0
für i in bereich(4):
    total = total + i
ausgeben(total)
```

**Japanese:**

```python
変数 x = 2
変数 y = 3
表示(x + y)

変数 合計 = 0
毎 i 中 範囲(4):
    合計 = 合計 + i
表示(合計)
```

**Arabic:**

```python
ليكن x = 2
ليكن y = 3
اطبع(x + y)

ليكن المجموع = 0
لكل i في مدى(4):
    المجموع = المجموع + i
اطبع(المجموع)
```

**Hindi:**

```python
मान x = 2
मान y = 3
छापो(x + y)

मान योग = 0
के_लिए i में परास(4):
    योग = योग + i
छापो(योग)
```

---

## REPL Tips

- Multi-line input: continue with `...` for blocks (if, for, def, class)
- Variables and functions defined in one language persist across `:language` switches (identifiers stay, keywords change)
- `:reset` clears all state including variables and function definitions
- Use `:python` to understand what code is actually being run
