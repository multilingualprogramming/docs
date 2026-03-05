---
page_id: reference__numerals
locale: fr
title: Numeraux
path_segments:
- references
- numeraux
source_hash: fbb7f9155632
status: translated
permalink: /fr/docs/references/numeraux/
---



multilingual provides first-class support for numerals in multiple scripts and representations.

---

## MPNumeral

Base multilingual numeral class. Supports arithmetic across numeral scripts.

{{snippet:reference__numerals__py01}}

---

## UnicodeNumeral

Handles numerals in Unicode scripts.

{{snippet:reference__numerals__py02}}

---

## RomanNumeral

{{snippet:reference__numerals__py03}}

---

## ComplexNumeral

{{snippet:reference__numerals__py04}}

---

## FractionNumeral

{{snippet:reference__numerals__py05}}

---

## NumeralConverter

Utility class for converting between numeral systems.

{{snippet:reference__numerals__py06}}

---

## Supported Numeral Scripts

| Script | Example | Language use |
|--------|---------|-------------|
| Arabic (0-9) | `42` | Universal |
| Arabic-Indic | `٤٢` | Arabic |
| Devanagari | `४२` | Hindi, Sanskrit |
| Bengali | `৪২` | Bengali |
| Tamil | `௪௨` | Tamil |
| CJK | `四十二` | Chinese, Japanese |
| Roman | `XLII` | Latin, historical |
| Scientific | `4.2e+01` | Universal |

---

## Utilisation des numeraux dans les programmes

Multilingual programs can use any supported numeral literal directly:

{{snippet:reference__numerals__py07}}

{{snippet:reference__numerals__py08}}

Le lexer reconnait les numeraux dans toutes les ecritures supportees et les normalise vers la representation canonique entier/flottant avant le parsing.
