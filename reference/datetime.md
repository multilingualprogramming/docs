---
layout: page
title: "Date & Time"
description: "Multilingual date and time parsing, formatting, and representation."
category: "Reference"
permalink: /reference/datetime/
prev_page:
  title: "Numerals"
  url: /reference/numerals/
---

multilingual provides multilingual date and time classes that parse and format dates using the conventions of 17 supported languages.

---

## MPDate

Multilingual date class with localized parsing and formatting.

```python
from multilingualprogramming import MPDate

# Parse from string with language hint
d1 = MPDate.parse("15 janvier 2024", language="fr")
print(d1.year, d1.month, d1.day)   # 2024 1 15

d2 = MPDate.parse("15 de enero de 2024", language="es")
d3 = MPDate.parse("15 يناير 2024", language="ar")
d4 = MPDate.parse("2024年1月15日", language="ja")
d5 = MPDate.parse("15 जनवरी 2024", language="hi")

# ISO format always works
d6 = MPDate.parse("2024-01-15")     # ISO 8601

# Create from parts
d7 = MPDate(year=2024, month=1, day=15)

# Format for a language
print(d1.format(language="fr"))     # 15 janvier 2024
print(d1.format(language="de"))     # 15. Januar 2024
print(d1.format(language="ar"))     # 15 يناير 2024
print(d1.format(language="ja"))     # 2024年1月15日
print(d1.format(language="zh"))     # 2024年1月15日
print(d1.format(language="hi"))     # 15 जनवरी 2024

# Properties
print(d1.year)                      # 2024
print(d1.month)                     # 1
print(d1.day)                       # 15
print(d1.weekday())                 # 0 (Monday)
print(d1.isoformat())               # "2024-01-15"
```

---

## MPTime

Multilingual time class.

```python
from multilingualprogramming import MPTime

# Create
t1 = MPTime(14, 30, 0)              # 14:30:00
t2 = MPTime(14, 30, 45, 123456)     # 14:30:45.123456

# Format
print(t1.format(language="fr"))     # 14:30:00
print(t1.format(language="ar"))     # ١٤:٣٠:٠٠  (Arabic-Indic digits)
print(t1.format(language="ja"))     # 14時30分00秒

# Properties
print(t1.hour)                      # 14
print(t1.minute)                    # 30
print(t1.second)                    # 0
print(t1.isoformat())               # "14:30:00"
```

---

## MPDatetime

Combined datetime class.

```python
from multilingualprogramming import MPDatetime

# Current datetime
dt = MPDatetime.now()

# Create from parts
dt1 = MPDatetime(year=2024, month=1, day=15, hour=14, minute=30, second=0)

# Parse
dt2 = MPDatetime.parse("15 janvier 2024 14:30:00", language="fr")

# Format
print(dt1.format(language="fr"))    # 15 janvier 2024 à 14:30:00
print(dt1.format(language="de"))    # 15. Januar 2024 um 14:30:00
print(dt1.format(language="ja"))    # 2024年1月15日 14時30分00秒
print(dt1.format(language="ar"))    # 15 يناير 2024 الساعة 14:30:00

# Components
print(dt1.date())                   # MPDate(2024, 1, 15)
print(dt1.time())                   # MPTime(14, 30, 0)
```

---

## Month Names by Language

| Month | en | fr | de | es | ja | ar | hi | zh |
|-------|----|----|----|----|----|----|----|----|
| 1 | January | janvier | Januar | enero | 1月 | يناير | जनवरी | 一月 |
| 2 | February | février | Februar | febrero | 2月 | فبراير | फरवरी | 二月 |
| 3 | March | mars | März | marzo | 3月 | مارس | मार्च | 三月 |
| 4 | April | avril | April | abril | 4月 | أبريل | अप्रैल | 四月 |
| 5 | May | mai | Mai | mayo | 5月 | مايو | मई | 五月 |
| 6 | June | juin | Juni | junio | 6月 | يونيو | जून | 六月 |
| 7 | July | juillet | Juli | julio | 7月 | يوليو | जुलाई | 七月 |
| 8 | August | août | August | agosto | 8月 | أغسطس | अगस्त | 八月 |
| 9 | September | septembre | September | septiembre | 9月 | سبتمبر | सितंबर | 九月 |
| 10 | October | octobre | Oktober | octubre | 10月 | أكتوبر | अक्टूबर | 十月 |
| 11 | November | novembre | November | noviembre | 11月 | نوفمبر | नवंबर | 十一月 |
| 12 | December | décembre | Dezember | diciembre | 12月 | ديسمبر | दिसंबर | 十二月 |

---

## Resource Files

Date/time resources are stored in:

```
multilingualprogramming/resources/datetime/
├── months.json      # Month names in all languages
├── weekdays.json    # Weekday names in all languages
├── eras.json        # Era names (AD/BC, etc.) in all languages
└── formats.json     # Date/time format templates per language
```

---

## Date Literals in Programs

multilingual programs support date literals using dedicated delimiters:

```python
# Date literal syntax (using date delimiters from operators.json)
let today = |2024-01-15|        # ISO date literal
let birthday = |15 janvier 2024|  # Localized date literal (French)
```

---

## Integration with datetime Module

MPDate/MPTime are interoperable with Python's standard `datetime` module:

```python
from multilingualprogramming import MPDate
import datetime

# Convert to Python datetime
mp_date = MPDate.parse("15 janvier 2024", language="fr")
py_date = mp_date.to_python_date()    # datetime.date(2024, 1, 15)

# Convert from Python datetime
py_date = datetime.date(2024, 1, 15)
mp_date = MPDate.from_python_date(py_date)
print(mp_date.format(language="ar"))  # 15 يناير 2024
```
