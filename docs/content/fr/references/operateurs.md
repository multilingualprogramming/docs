---
page_id: reference__operators
locale: fr
title: Opérateurs
path_segments:
- references
- operateurs
source_hash: 7ce7e4343a9f
status: translated
permalink: /fr/docs/references/operateurs/
---

`multilingual` prend en charge l'ensemble des opérateurs Python, avec quelques alternatives Unicode lorsque cela est pertinent.

---

## Opérateurs arithmétiques

| Opérateur | Alternative Unicode | Signification | Exemple |
|-----------|---------------------|---------------|---------|
| `+` | — | Addition | `x + y` |
| `-` | — | Soustraction | `x - y` |
| `*` | `×` | Multiplication | `x * y` |
| `/` | `÷` | Division réelle | `x / y` |
| `//` | — | Division entière | `x // y` |
| `%` | — | Modulo | `x % y` |
| `**` | — | Puissance | `x ** y` |

---

## Opérateurs de comparaison

| Opérateur | Alternative Unicode | Signification | Exemple |
|-----------|---------------------|---------------|---------|
| `==` | — | Égalité | `x == y` |
| `!=` | `≠` | Différence | `x != y` |
| `<` | — | Inférieur à | `x < y` |
| `>` | — | Supérieur à | `x > y` |
| `<=` | `≤` | Inférieur ou égal à | `x <= y` |
| `>=` | `≥` | Supérieur ou égal à | `x >= y` |

---

## Opérateurs d'affectation

| Opérateur | Signification | Exemple |
|-----------|---------------|---------|
| `=` | Affectation | `x = 5` |
| `+=` | Ajouter et affecter | `x += 3` |
| `-=` | Soustraire et affecter | `x -= 2` |
| `*=` | Multiplier et affecter | `x *= 4` |
| `/=` | Diviser et affecter | `x /= 2` |
| `//=` | Diviser entière et affecter | `x //= 3` |
| `%=` | Modulo et affecter | `x %= 7` |
| `**=` | Élever à la puissance et affecter | `x **= 2` |
| `:=` | Opérateur morse | `(n := len(data))` |

---

## Opérateurs booléens

| Concept | Formes de mot-clé | Signification |
|---------|-------------------|---------------|
| `AND` | `and`, `et` | ET logique |
| `OR` | `or`, `ou` | OU logique |
| `NOT` | `not`, `pas` | NON logique |

---

## Identité et appartenance

| Concept | Mot-clé | Signification | Exemple |
|---------|---------|---------------|---------|
| `IS` | `is` | Test d'identité | `x is None` |
| `IS_NOT` | `is not` | Négation d'identité | `x is not None` |
| `IN_OP` | `in` | Appartenance | `x in [1, 2, 3]` |
| `NOT_IN` | `not in` | Non-appartenance | `x not in items` |

---

## Opérateurs binaires

| Opérateur | Signification | Exemple |
|-----------|---------------|---------|
| `&` | ET binaire | `x & 0xFF` |
| `\|` | OU binaire | `x \| 0x01` |
| `^` | XOR binaire | `x ^ 0x10` |
| `~` | NON binaire | `~x` |
| `<<` | Décalage à gauche | `x << 2` |
| `>>` | Décalage à droite | `x >> 1` |

---

## Délimiteurs

| Symbole | Signification |
|---------|---------------|
| `(` `)` | Parenthèses |
| `[` `]` | Crochets |
| `{` `}` | Accolades |
| `:` | Séparateur de bloc ou de slice |
| `,` | Séparateur |
| `.` | Accès à un attribut |
| `...` | Ellipse |

---

## Littéraux de date

| Symbole | Signification | Exemple |
|---------|---------------|---------|
| `\|...\|` | Littéral de date | `\|2024-01-15\|` |

---

## Localisation des opérateurs

Les opérateurs symboliques ne sont pas localisés. En revanche, certaines formes textuelles changent selon la langue pour les opérateurs booléens :

{{snippet:reference__operators__py01}}

Utilisez `:ops` dans le REPL pour afficher la description des opérateurs de la langue courante.

---

## Précédence

La précédence suit les règles Python, du plus fort au plus faible :

| Niveau | Opérateurs |
|--------|------------|
| 1 | `**` |
| 2 | `+x`, `-x`, `~x` |
| 3 | `*`, `@`, `/`, `//`, `%` |
| 4 | `+`, `-` |
| 5 | `<<`, `>>` |
| 6 | `&` |
| 7 | `^` |
| 8 | `\|` |
| 9 | `==`, `!=`, `<`, `>`, `<=`, `>=`, `is`, `is not`, `in`, `not in` |
| 10 | `not` |
| 11 | `and` |
| 12 | `or` |

Les parenthèses permettent toujours de forcer l'ordre d'évaluation.
