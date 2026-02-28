---
layout: page
title: "Built-in Aliases"
description: "All 41 localized built-in aliases across all 17 languages."
category: "Reference"
permalink: /reference/builtins/
prev_page:
  title: "Reference"
  url: /reference/
next_page:
  title: "Operators"
  url: /reference/operators/
---

multilingual provides localized aliases for 41 commonly used Python built-in functions. Universal English names are **always available** in all languages — aliases are additive.

---

## Using Built-in Aliases

```python
# In English — universal name works
print(range(5))
print(len([1, 2, 3]))

# In French — both universal and alias work
afficher(intervalle(5))    # French aliases
print(range(5))            # Universal name — still works in French!

# In Japanese — both work
表示(範囲(5))               # Japanese aliases
print(range(5))            # Universal still works
```

---

## Complete Alias Table

### Core I/O

| Builtin | fr | es | de | ja | ar | hi | zh |
|---------|----|----|----|----|----|----|-----|
| `print` | afficher | imprimir | ausgeben | 表示 | اطبع | छापो | 打印 |
| `input` | saisie | entrada | eingabe | 入力 | إدخال | इनपुट | 输入 |
| `open` | ouvrir | abrir | oeffnen | 開く | افتح | खोलो | 打开 |

### Sequence Operations

| Builtin | fr | es | de | ja | ar | hi | zh |
|---------|----|----|----|----|----|----|-----|
| `range` | intervalle | rango | bereich | 範囲 | مدى | परास | 范围 |
| `len` | longueur | largo | länge | 長さ | طول | लंबाई | 长度 |
| `sum` | somme | suma | summe | 合計 | مجموع | योग | 总和 |
| `sorted` | trie | ordenado | sortiert | ソート済み | مرتب | क्रमबद्ध | 排序 |
| `reversed` | inverse | invertido | umgekehrt | 逆順 | معكوس | उलटा | 反转 |
| `enumerate` | enumerer | enumerar | aufzaehlen | 列挙 | عدِّد | गणना | 枚举 |
| `zip` | combiner | combinar | kombinieren | 組み合わせ | اربط | जोड़ो | 压缩 |
| `map` | appliquer | aplicar | anwenden | マップ | طبِّق | लागू | 映射 |
| `filter` | filtrer | filtrar | filtern | フィルター | رشِّح | फ़िल्टर | 过滤 |

### Math

| Builtin | fr | es | de | ja | ar | hi | zh |
|---------|----|----|----|----|----|----|-----|
| `abs` | valeur\_abs | abs | absolutwert | 絶対値 | قيمة\_مطلقة | परम\_मूल्य | 绝对值 |
| `min` | minimum | minimo | minimum | 最小 | أصغر | न्यूनतम | 最小值 |
| `max` | maximum | maximo | maximum | 最大 | أكبر | अधिकतम | 最大值 |
| `round` | arrondir | redondear | runden | 丸める | أقرب | गोल | 四舍五入 |
| `pow` | puissance | potencia | potenz | べき乗 | أس | घात | 幂 |
| `divmod` | divmod | divmod | divmod | 除算余り | قسمة\_مع\_باقي | भाग\_और\_शेष | 整除 |

### Type Functions

| Builtin | fr | es | de | ja | ar | hi | zh |
|---------|----|----|----|----|----|----|-----|
| `type` | type | tipo | typ | 型 | نوع | प्रकार | 类型 |
| `isinstance` | estinstance | esinstancia | istinstanz | インスタンス確認 | هل\_نوع | उदाहरण\_है | 是实例 |
| `issubclass` | soussclasse | essubclase | istunterklasse | サブクラス確認 | هل\_فئة\_فرعية | उपवर्ग\_है | 是子类 |
| `repr` | repr | repr | repr | 表現 | تمثيل | प्रतिनिधित्व | 表示 |
| `str` | chaine | cadena | zeichenkette | 文字列 | سلسلة | स्ट्रिंग | 字符串 |
| `int` | entier | entero | ganzzahl | 整数 | صحيح | पूर्णांक | 整数 |
| `float` | flottant | flotante | fliesskomma | 浮動小数点 | عشري | दशमलव | 浮点数 |
| `bool` | booleen | booleano | boolesch | ブール | منطقي | बूलियन | 布尔 |

### Collections

| Builtin | fr | es | de | ja | ar | hi | zh |
|---------|----|----|----|----|----|----|-----|
| `list` | liste | lista | liste | リスト | قائمة | सूची | 列表 |
| `dict` | dico | dicc | dict | 辞書 | قاموس | शब्दकोश | 字典 |
| `set` | ensemble | conjunto | menge | 集合 | مجموعة | समुच्चय | 集合 |
| `tuple` | tuple | tupla | tupel | タプル | تيوبل | ट्यूपल | 元组 |
| `frozenset` | ensemble\_gele | conjuntofijo | frozenset | 凍結集合 | مجموعة\_ثابتة | जमाया\_सेट | 冻结集合 |
| `bytes` | octets | bytes | bytes | バイト列 | بايتات | बाइट | 字节 |

### Introspection

| Builtin | fr | es | de | ja | ar | hi | zh |
|---------|----|----|----|----|----|----|-----|
| `dir` | repertoire | directorio | verzeichnis | ディレクトリ | دليل | निर्देशिका | 目录 |
| `hasattr` | aattribut | tieneattr | hatattr | 属性あり | له\_خاصية | विशेषता\_है | 有属性 |
| `getattr` | getattr | obtenerattr | getattr | 属性取得 | احصل\_على\_خاصية | विशेषता\_प | 获取属性 |
| `setattr` | setattr | asignarattr | setattr | 属性設定 | حدد\_خاصية | विशेषता\_स | 设置属性 |
| `delattr` | delattr | eliminarattr | delattr | 属性削除 | احذف\_خاصية | विशेषता\_ह | 删除属性 |
| `callable` | appelable | invocable | aufrufbar | 呼び出し可能 | قابل\_للاستدعاء | कॉल\_योग्य | 可调用 |
| `hash` | hacher | hash | hash | ハッシュ | هاش | हैश | 哈希 |

### Iteration

| Builtin | fr | es | de | ja | ar | hi | zh |
|---------|----|----|----|----|----|----|-----|
| `iter` | iterateur | iterador | iterator | イテレータ | مكرر | पुनरावर्तक | 迭代器 |
| `next` | suivant | siguiente | naechster | 次 | التالي | अगला | 下一个 |
| `any` | quelconque | cualquiera | irgendein | どれか | أي | कोई | 任意 |
| `all` | tous | todos | alle | すべて | كل | सब | 所有 |

### String/Encoding

| Builtin | fr | es | de | ja | ar | hi | zh |
|---------|----|----|----|----|----|----|-----|
| `chr` | chr | chr | chr | 文字 | حرف | वर्ण | 字符 |
| `ord` | ord | ord | ord | 文字コード | رمز\_حرف | कोड | 编码 |
| `format` | formater | formatear | formatieren | フォーマット | تنسيق | प्रारूप | 格式化 |

---

## Checking Available Aliases

```python
from multilingualprogramming.codegen import RuntimeBuiltins

# Get all builtins (including aliases) for a language
builtins = RuntimeBuiltins.for_language("fr")

# Check if alias exists
print("afficher" in builtins)    # True
print("imprimir" in builtins)    # False (Spanish, not French)
print("print" in builtins)       # True (universal)

# List all localized aliases for French
aliases = {k: v.__name__ for k, v in builtins.items()
           if k not in dir(__builtins__)}
print(aliases)
```

---

## REPL: List Aliases

In the REPL, use `:kw` to see all keyword and builtin aliases for the current language:

```
multilingual [fr]> :kw
```

---

## Adding More Aliases

Additional aliases can be added via `multilingualprogramming/resources/usm/builtins_aliases.json`. See [Translation Guidelines](/extending/translation/) for the process.
