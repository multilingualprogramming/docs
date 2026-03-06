---
page_id: reference__builtins
locale: fr
title: Fonctions intégrées
path_segments:
- references
- fonctions-integrees
source_hash: 3b6205ba8915
status: translated
permalink: /fr/docs/references/fonctions-integrees/
---

multilingual fournit des alias localisés pour 41 fonctions intégrées Python courantes. Les noms anglais universels restent **toujours disponibles** dans toutes les langues ; les alias sont simplement ajoutés en complément.

---

## Utilisation des alias de builtins

```plaintext
# In English — universal name works
print(range(5))
print(len([1, 2, 3]))

# In French — both universal and alias work
afficher(intervalle(5))    # French aliases
print(range(5))            # Universal name — still works in French!

# In Japanese — both work
表示(範囲(5))
print(range(5))
```

---

## Table complète des alias

### E/S de base

| Builtin | fr | es | de | ja | ar | hi | zh |
|---------|----|----|----|----|----|----|-----|
| `print` | afficher | imprimir | ausgeben | 表示 | اطبع | छापो | 打印 |
| `input` | saisie | entrada | eingabe | 入力 | إدخال | इनपुट | 输入 |
| `open` | ouvrir | abrir | oeffnen | 開く | افتح | खोलो | 打开 |

### Opérations de séquence

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

### Mathématiques

| Builtin | fr | es | de | ja | ar | hi | zh |
|---------|----|----|----|----|----|----|-----|
| `abs` | valeur_abs | abs | absolutwert | 絶対値 | قيمة_مطلقة | परम_मूल्य | 绝对值 |
| `min` | minimum | minimo | minimum | 最小 | أصغر | न्यूनतम | 最小值 |
| `max` | maximum | maximo | maximum | 最大 | أكبر | अधिकतम | 最大值 |
| `round` | arrondir | redondear | runden | 丸める | أقرب | गोल | 四舍五入 |
| `pow` | puissance | potencia | potenz | べき乗 | أس | घात | 幂 |
| `divmod` | divmod | divmod | divmod | 除算余り | قسمة_مع_باقي | भाग_और_शेष | 整除 |

### Fonctions de type

| Builtin | fr | es | de | ja | ar | hi | zh |
|---------|----|----|----|----|----|----|-----|
| `type` | type | tipo | typ | 型 | نوع | प्रकार | 类型 |
| `isinstance` | estinstance | esinstancia | istinstanz | インスタンス確認 | هل_نوع | उदाहरण_है | 是实例 |
| `issubclass` | sousclasse | essubclase | istunterklasse | サブクラス確認 | هل_فئة_فرعية | उपवर्ग_है | 是子类 |
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
| `frozenset` | ensemble_gele | conjuntofijo | frozenset | 凍結集合 | مجموعة_ثابتة | जमाया_सेट | 冻结集合 |
| `bytes` | octets | bytes | bytes | バイト列 | بايتات | बाइट | 字节 |

### Introspection

| Builtin | fr | es | de | ja | ar | hi | zh |
|---------|----|----|----|----|----|----|-----|
| `dir` | repertoire | directorio | verzeichnis | ディレクトリ | دليل | निर्देशिका | 目录 |
| `hasattr` | aattribut | tieneattr | hatattr | 属性あり | له_خاصية | विशेषता_है | 有属性 |
| `getattr` | getattr | obtenerattr | getattr | 属性取得 | احصل_على_خاصية | विशेषता_प | 获取属性 |
| `setattr` | setattr | asignarattr | setattr | 属性設定 | حدد_خاصية | विशेषता_स | 设置属性 |
| `delattr` | delattr | eliminarattr | delattr | 属性削除 | احذف_خاصية | विशेषता_ह | 删除属性 |
| `callable` | appelable | invocable | aufrufbar | 呼び出し可能 | قابل_للاستدعاء | कॉल_योग्य | 可调用 |
| `hash` | hacher | hash | hash | ハッシュ | هاش | हैश | 哈希 |

### Itération

| Builtin | fr | es | de | ja | ar | hi | zh |
|---------|----|----|----|----|----|----|-----|
| `iter` | iterateur | iterador | iterator | イテレータ | مكرر | पुनरावर्तक | 迭代器 |
| `next` | suivant | siguiente | naechster | 次 | التالي | अगला | 下一个 |
| `any` | quelconque | cualquiera | irgendein | どれか | أي | कोई | 任意 |
| `all` | tous | todos | alle | すべて | كل | सब | 所有 |

### Chaînes et encodage

| Builtin | fr | es | de | ja | ar | hi | zh |
|---------|----|----|----|----|----|----|-----|
| `chr` | chr | chr | chr | 文字 | حرف | वर्ण | 字符 |
| `ord` | ord | ord | ord | 文字コード | رمز_حرف | कोड | 编码 |
| `format` | formater | formatear | formatieren | フォーマット | تنسيق | प्रारूप | 格式化 |

---

## Vérification des alias disponibles

{{snippet:reference__builtins__py01}}

---

## REPL : lister les alias

Dans le REPL, utilisez `:kw` pour voir tous les alias de mots-clés et de builtins de la langue courante :

```
multilingual [fr]> :kw
```

---

## Ajouter plus d'alias

Des alias supplémentaires peuvent être ajoutés via `multilingualprogramming/resources/usm/builtins_aliases.json`. Voir les [directives de traduction](/fr/docs/extension/traduction/) pour la procédure.
