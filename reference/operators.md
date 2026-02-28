---
layout: page
title: "Operators Reference"
description: "Complete operator reference for multilingual — arithmetic, comparison, bitwise, and Unicode alternatives."
category: "Reference"
permalink: /reference/operators/
prev_page:
  title: "Built-in Aliases"
  url: /reference/builtins/
next_page:
  title: "Numerals"
  url: /reference/numerals/
---

multilingual supports the full Python operator set plus Unicode alternatives where applicable.

---

## Arithmetic Operators

| Operator | Unicode alt | Meaning | Example |
|----------|-------------|---------|---------|
| `+` | — | Addition | `x + y` |
| `-` | — | Subtraction | `x - y` |
| `*` | `×` | Multiplication | `x * y` |
| `/` | `÷` | True division | `x / y` |
| `//` | — | Floor division | `x // y` |
| `%` | — | Modulo | `x % y` |
| `**` | — | Power | `x ** y` |
| `-` (unary) | — | Negation | `-x` |
| `+` (unary) | — | Positive | `+x` |

---

## Comparison Operators

| Operator | Unicode alt | Meaning | Example |
|----------|-------------|---------|---------|
| `==` | — | Equal | `x == y` |
| `!=` | `≠` | Not equal | `x != y` |
| `<` | — | Less than | `x < y` |
| `>` | — | Greater than | `x > y` |
| `<=` | `≤` | Less or equal | `x <= y` |
| `>=` | `≥` | Greater or equal | `x >= y` |

---

## Assignment Operators

| Operator | Meaning | Example |
|----------|---------|---------|
| `=` | Assignment | `x = 5` |
| `+=` | Add and assign | `x += 3` |
| `-=` | Subtract and assign | `x -= 2` |
| `*=` | Multiply and assign | `x *= 4` |
| `/=` | Divide and assign | `x /= 2` |
| `//=` | Floor-divide and assign | `x //= 3` |
| `%=` | Modulo and assign | `x %= 7` |
| `**=` | Power and assign | `x **= 2` |
| `&=` | Bitwise AND assign | `x &= 0xFF` |
| `\|=` | Bitwise OR assign | `x \|= 0x01` |
| `^=` | Bitwise XOR assign | `x ^= 0x10` |
| `<<=` | Left shift assign | `x <<= 2` |
| `>>=` | Right shift assign | `x >>= 1` |
| `:=` | Walrus (assign + return) | `(n := len(data))` |

---

## Boolean Operators

| Concept | Keyword forms (per language) | Meaning |
|---------|------------------------------|---------|
| `AND` | `and` (en), `et` (fr), `und` (de), `かつ` (ja), `و` (ar) | Logical AND |
| `OR` | `or` (en), `ou` (fr), `oder` (de), `または` (ja), `أو` (ar) | Logical OR |
| `NOT` | `not` (en), `pas` (fr), `nicht` (de), `ではない` (ja), `ليس` (ar) | Logical NOT |

---

## Identity and Membership

| Concept | Keyword | Meaning | Example |
|---------|---------|---------|---------|
| `IS` | `is` | Identity check | `x is None` |
| `IS_NOT` | `is not` | Negative identity | `x is not None` |
| `IN_OP` | `in` | Membership | `x in [1,2,3]` |
| `NOT_IN` | `not in` | Non-membership | `x not in items` |

---

## Bitwise Operators

| Operator | Meaning | Example |
|----------|---------|---------|
| `&` | Bitwise AND | `x & 0xFF` |
| `\|` | Bitwise OR | `x \| 0x01` |
| `^` | Bitwise XOR | `x ^ 0x10` |
| `~` | Bitwise NOT | `~x` |
| `<<` | Left shift | `x << 2` |
| `>>` | Right shift | `x >> 1` |

---

## Delimiters

| Symbol | Unicode alt | Meaning |
|--------|-------------|---------|
| `(` `)` | — | Parentheses |
| `[` `]` | — | Square brackets |
| `{` `}` | — | Curly brackets |
| `:` | — | Block/slice separator |
| `,` | — | Separator |
| `.` | — | Attribute access |
| `...` | `…` | Ellipsis |

---

## Date Literal Delimiters

| Symbol | Meaning | Example |
|--------|---------|---------|
| `\|...\|` | Date literal | `\|2024-01-15\|` |

---

## Operator Localization

Operators are not localized per language (they use the universal symbol set). However, some natural-language alternatives exist for boolean operators:

```python
# All equivalent in English:
x and y
x AND y  # case insensitive in some contexts

# In Japanese, 'かつ' is 'and', 'または' is 'or'
# In Arabic, 'و' is 'and', 'أو' is 'or'
```

Use `:ops` in the REPL to see the current language's operator descriptions:

```
multilingual [fr]> :ops
Operators for French (fr):
  +    addition
  -    soustraction
  *    multiplication
  /    division
  //   division entière
  %    modulo
  **   puissance
  ...
```

---

## Operator Precedence

Follows Python operator precedence (from highest to lowest):

| Level | Operators |
|-------|-----------|
| 1 (highest) | `**` |
| 2 | `+x`, `-x`, `~x` (unary) |
| 3 | `*`, `@`, `/`, `//`, `%` |
| 4 | `+`, `-` |
| 5 | `<<`, `>>` |
| 6 | `&` |
| 7 | `^` |
| 8 | `\|` |
| 9 | `==`, `!=`, `<`, `>`, `<=`, `>=`, `is`, `is not`, `in`, `not in` |
| 10 | `not` |
| 11 | `and` |
| 12 (lowest) | `or` |

Parentheses can always be used to override precedence.
