---
page_id: getting_started__repl
locale: en
title: REPL Guide
path_segments:
- getting-started
- repl
source_hash: 4444b80aad58
status: source
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

# With WAT preview (show generated WebAssembly Text alongside output)
python -m multilingualprogramming repl --show-wat

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
| `:wat` or `:wasm` | Toggle WAT preview mode (show generated WebAssembly Text) |
| `:rust` or `:wasmtime` | Toggle wasmtime execution mode (run via WASM instead of Python) |
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

### WAT Preview Mode

Use `:wat` (or `:wasm`) to toggle display of the compiled WebAssembly Text Format alongside each result:

```
multilingual [en]> :wat
WAT preview: ON
multilingual [en]> let x = 42
; WAT:
; (func $__main
;   f64.const 42
;   local.set $x
; )
multilingual [en]> :wat
WAT preview: OFF
```

Use `:rust` (or `:wasmtime`) to switch execution to the wasmtime backend:

```
multilingual [en]> :wasmtime
Backend: wasmtime (WASM)
multilingual [en]> let x = 42
multilingual [en]> print(x)
42
multilingual [en]> :wasmtime
Backend: Python
```

---

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

{{snippet:getting_started__repl__py01}}

**French:**

{{snippet:getting_started__repl__py02}}

**German:**

{{snippet:getting_started__repl__py03}}

**Japanese:**

{{snippet:getting_started__repl__py04}}

**Arabic:**

{{snippet:getting_started__repl__py05}}

**Hindi:**

{{snippet:getting_started__repl__py06}}

---

## REPL Tips

- Multi-line input: continue with `...` for blocks (if, for, def, class)
- Variables and functions defined in one language persist across `:language` switches (identifiers stay, keywords change)
- `:reset` clears all state including variables and function definitions
- Use `:python` to understand what Python code is being generated
- Use `:wat` to inspect the WebAssembly Text Format compiled from your code
- Use `:wasmtime` to run code through the WASM backend instead of Python
