---
page_id: reference__operators
locale: fr
title: Operateurs
path_segments:
- references
- operateurs
source_hash: 7ce7e4343a9f
status: translated
---



multilingual prend en charge l'ensemble complet des operateurs Python, avec alternatives Unicode lorsque c'est pertinent.

---

## Arithmetique Operators

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

## Operateurs de comparaison

| Operator | Unicode alt | Meaning | Example |
|----------|-------------|---------|---------|
| `==` | — | Equal | `x == y` |
| `!=` | `≠` | Not equal | `x != y` |
| `<` | — | Less than | `x < y` |
| `>` | — | Greater than | `x > y` |
| `<=` | `≤` | Less or equal | `x <= y` |
| `>=` | `≥` | Greater or equal | `x >= y` |

---

## Operateurs d'affectation

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

## Operateurs booleens

| Concept | Keyword forms (per language) | Meaning |
|---------|------------------------------|---------|
| `AND` | `and` (en), `et` (fr), `und` (de), `かつ` (ja), `و` (ar) | Logical AND |
| `OR` | `or` (en), `ou` (fr), `oder` (de), `または` (ja), `أو` (ar) | Logical OR |
| `NOT` | `not` (en), `pas` (fr), `nicht` (de), `ではない` (ja), `ليس` (ar) | Logical NOT |

---

## Identite et appartenance

| Concept | Keyword | Meaning | Example |
|---------|---------|---------|---------|
| `IS` | `is` | Identity check | `x is None` |
| `IS_NOT` | `is not` | Negative identity | `x is not None` |
| `IN_OP` | `in` | Membership | `x in [1,2,3]` |
| `NOT_IN` | `not in` | Non-membership | `x not in items` |

---

## Operateurs binaires

| Operator | Meaning | Example |
|----------|---------|---------|
| `&` | Bitwise AND | `x & 0xFF` |
| `\|` | Bitwise OR | `x \| 0x01` |
| `^` | Bitwise XOR | `x ^ 0x10` |
| `~` | Bitwise NOT | `~x` |
| `<<` | Left shift | `x << 2` |
| `>>` | Right shift | `x >> 1` |

---

## Delimiteurs

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

## Delimiteurs de litteraux de date

| Symbol | Meaning | Example |
|--------|---------|---------|
| `\|...\|` | Date literal | `\|2024-01-15\|` |

---

## Localisation des operateurs

Les operateurs ne sont pas localises par langue (ils utilisent un jeu de symboles universel). Cependant, certaines alternatives en langue naturelle existent pour les operateurs booleens :

{{snippet:reference__operators__py01}}

Utilisez `:ops` dans le REPL pour voir la description des operateurs de la langue courante :

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

## Precedence des operateurs

Suit la precedence des operateurs Python (du plus eleve au plus faible) :

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

Les parentheses peuvent toujours etre utilisees pour forcer la precedence.
