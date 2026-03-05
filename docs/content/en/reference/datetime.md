---
page_id: reference__datetime
locale: en
title: Date & Time
path_segments:
- reference
- datetime
source_hash: 4e5871b97df0
status: source
---

multilingual provides multilingual date and time classes that parse and format dates using the conventions of 17 supported languages.

---

## MPDate

Multilingual date class with localized parsing and formatting.

{{snippet:reference__datetime__py01}}

---

## MPTime

Multilingual time class.

{{snippet:reference__datetime__py02}}

---

## MPDatetime

Combined datetime class.

{{snippet:reference__datetime__py03}}

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

{{snippet:reference__datetime__py04}}

---

## Integration with datetime Module

MPDate/MPTime are interoperable with Python's standard `datetime` module:

{{snippet:reference__datetime__py05}}
