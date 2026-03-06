---
page_id: reference__numerals
locale: fr
title: Numéraux
path_segments:
- references
- numeraux
source_hash: fbb7f9155632
status: translated
permalink: /fr/docs/references/numeraux/
---

`multilingual` prend en charge nativement les numéraux dans plusieurs écritures et représentations.

---

## `MPNumeral`

Classe de base des numéraux multilingues. Elle permet les opérations arithmétiques entre différentes écritures numériques.

{{snippet:reference__numerals__py01}}

---

## `UnicodeNumeral`

Gère les numéraux dans les écritures Unicode.

{{snippet:reference__numerals__py02}}

---

## `RomanNumeral`

{{snippet:reference__numerals__py03}}

---

## `ComplexNumeral`

{{snippet:reference__numerals__py04}}

---

## `FractionNumeral`

{{snippet:reference__numerals__py05}}

---

## `NumeralConverter`

Classe utilitaire pour convertir entre différents systèmes numériques.

{{snippet:reference__numerals__py06}}

---

## Écritures numériques prises en charge

| Écriture | Exemple | Usage |
|----------|---------|-------|
| Arabe occidental | `42` | Usage universel |
| Arabe oriental | `٤٢` | Arabe |
| Devanagari | `४२` | Hindi |
| Bengali | `৪২` | Bengali |
| Tamil | `௪௨` | Tamil |
| CJK | `四十二` | Chinois, japonais |
| Romain | `XLII` | Usage historique |
| Scientifique | `4.2e+01` | Usage universel |

---

## Utilisation dans les programmes

Les programmes `multilingual` peuvent utiliser directement n'importe quel littéral numérique pris en charge :

{{snippet:reference__numerals__py07}}

{{snippet:reference__numerals__py08}}

Le lexer reconnaît ces écritures et les normalise vers une représentation canonique avant le parsing.
