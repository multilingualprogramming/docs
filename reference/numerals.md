---
layout: page
title: "Numeral Systems"
description: "Multilingual numeral support — Unicode scripts, Roman numerals, complex numbers, fractions."
category: "Reference"
permalink: /reference/numerals/
prev_page:
  title: "Operators"
  url: /reference/operators/
next_page:
  title: "Date & Time"
  url: /reference/datetime/
---

multilingual provides first-class support for numerals in multiple scripts and representations.

---

## MPNumeral

Base multilingual numeral class. Supports arithmetic across numeral scripts.

```python
from multilingualprogramming import MPNumeral

# Create from integer
n1 = MPNumeral(42)

# Create from Arabic-Indic digits
n2 = MPNumeral("٤٢")

# Create from Devanagari digits
n3 = MPNumeral("४२")

# Create from CJK numerals
n4 = MPNumeral("四十二")

# Arithmetic (all return MPNumeral)
result = n1 + n2
result = n1 * MPNumeral(3)
result = n1 - MPNumeral(10)
result = n1 / MPNumeral(6)

# Conversion
print(n1.to_int())              # 42
print(n1.to_arabic_indic())     # ٤٢
print(n1.to_devanagari())       # ४२
print(n1.to_bengali())          # ৪২
print(n1.to_cjk())              # 四十二
print(n1.to_roman())            # XLII
print(n1.to_scientific())       # 4.2e+01
```

---

## UnicodeNumeral

Handles numerals in Unicode scripts.

```python
from multilingualprogramming import UnicodeNumeral

# Arabic-Indic numerals
u1 = UnicodeNumeral("٣٧")
print(u1.to_int())    # 37

# Devanagari numerals (Hindi)
u2 = UnicodeNumeral("३७")
print(u2.to_int())    # 37

# Bengali numerals
u3 = UnicodeNumeral("৩৭")
print(u3.to_int())    # 37

# Tamil numerals
u4 = UnicodeNumeral("௩௭")
print(u4.to_int())    # 37

# CJK digits
u5 = UnicodeNumeral("三七")
print(u5.to_int())    # 37
```

---

## RomanNumeral

```python
from multilingualprogramming import RomanNumeral

# From Roman string
r1 = RomanNumeral("XIV")
print(r1.to_int())      # 14
print(int(r1))          # 14

r2 = RomanNumeral("XLII")
print(r2.to_int())      # 42

# From integer
r3 = RomanNumeral(2024)
print(str(r3))          # MMXXIV

# Arithmetic
r4 = RomanNumeral("X") + RomanNumeral("V")
print(str(r4))          # XV
```

---

## ComplexNumeral

```python
from multilingualprogramming import ComplexNumeral

c1 = ComplexNumeral(3, 4)       # 3 + 4i
print(c1.real)                  # 3
print(c1.imag)                  # 4
print(c1.magnitude())           # 5.0
print(str(c1))                  # 3+4i

c2 = ComplexNumeral.from_string("2+3i")
c3 = c1 + c2
```

---

## FractionNumeral

```python
from multilingualprogramming import FractionNumeral

f1 = FractionNumeral(1, 3)      # 1/3
f2 = FractionNumeral(1, 4)      # 1/4

print(f1.numerator)             # 1
print(f1.denominator)           # 3
print(float(f1))                # 0.3333...

f3 = f1 + f2                    # 1/3 + 1/4 = 7/12
print(f3.numerator)             # 7
print(f3.denominator)           # 12

# Unicode fractions
f4 = FractionNumeral.from_unicode("½")   # 1/2
f5 = FractionNumeral.from_unicode("¾")   # 3/4
```

---

## NumeralConverter

Utility class for converting between numeral systems.

```python
from multilingualprogramming import NumeralConverter

conv = NumeralConverter()

# To various scripts
print(conv.to_arabic_indic(42))     # ٤٢
print(conv.to_devanagari(42))       # ४२
print(conv.to_bengali(42))          # ৪২
print(conv.to_tamil(42))            # ௪௨
print(conv.to_cjk(42))              # 四十二
print(conv.to_roman(42))            # XLII

# From various scripts to integer
print(conv.to_int("٤٢"))            # 42 (Arabic-Indic)
print(conv.to_int("४२"))            # 42 (Devanagari)
print(conv.to_int("XLII"))          # 42 (Roman)
print(conv.to_int("四十二"))         # 42 (CJK)

# Detect script
print(conv.detect_script("٤٢"))     # "arabic_indic"
print(conv.detect_script("四十二"))  # "cjk"
print(conv.detect_script("XIV"))    # "roman"
```

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

## Using Numerals in Programs

Multilingual programs can use any supported numeral literal directly:

```python
# English program with Devanagari numeral
let count = ४२        # equivalent to 42
print(count + 8)     # 50

# French program with Arabic-Indic numeral
soit total = ٣٠ + ١٢
afficher(total)      # 42
```

The lexer recognizes numerals in all supported scripts and normalizes them to the canonical integer/float representation before parsing.
