---
layout: page
title: "Keywords Reference"
description: "Complete keyword mapping: all 51 semantic concepts across all 17 languages."
category: "Language Guide"
permalink: /language-guide/keywords/
prev_page:
  title: "Language Guide"
  url: /language-guide/
next_page:
  title: "All 17 Languages"
  url: /language-guide/all-languages/
---

All keywords in multilingual map to **semantic concepts** — not raw tokens. The lexer resolves language-specific surface keywords to concepts; the parser and codegen operate on concepts only.

---

## Concept System

A concept like `COND_IF` maps to `if` in English, `si` in French, `wenn` in German, `もし` in Japanese, etc. This keeps the parser and semantic analyzer language-agnostic.

The keyword registry is stored in:
`multilingualprogramming/resources/usm/keywords.json`

---

## Control Flow Keywords

| Concept | en | fr | es | de | it | pt | pl | nl | sv | da | fi | hi | ar | bn | ta | zh | ja |
|---------|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
| `COND_IF` | if | si | si | wenn | se | se | jezeli | als | om | hvis | jos | अगर | إذا | যদি | என்றால் | 如果 | もし |
| `COND_ELIF` | elif | sinonsi | sinosino | sonstewenn | altrimenti | senaoif | inaczej | alsdan | annarsif | ellervis | muttajos | वरना | وإلا\_إذا | নইলে\_যদি | இல்லையென்றால் | 否则如果 | そうでなければ\_もし |
| `COND_ELSE` | else | sinon | sino | sonst | altrimenti | senao | inaczej | anders | annars | ellers | muuten | वरना | وإلا | নইলে | இல்லையென்றால் | 否则 | そうでなければ |
| `LOOP_FOR` | for | pour | para | für | per | para | dla | voor | for | for | jokaiselle | के\_लिए | لكل | জন্য | ஒவ்வொரு | 对于 | 毎 |
| `IN` | in | dans | en | in | in | em | w | in | i | i | in | में | في | মধ্যে | இல் | 里 | 中 |
| `LOOP_WHILE` | while | tantque | mientras | solange | mentre | enquanto | dopoki | zolang | medans | imens | kunnes | जबतक | بينما | যতক্ষণ | வரை | 当 | 間 |
| `BREAK` | break | arreter | romper | abbrechen | interrompi | parar | przerwij | stoppen | bryt | stop | lopeta | रोको | توقف | থামো | நிறுத்து | 中断 | 中断 |
| `CONTINUE` | continue | continuer | continuar | fortfahren | continua | continuar | kontynuuj | doorgaan | fortsatt | fortsaet | jatka | जारी | استمر | চালিয়ে\_যাও | தொடர் | 继续 | 継続 |
| `PASS` | pass | passer | pasar | uebergehen | passa | passar | pominac | overslaan | passera | skip | ohita | छोड़ो | تجاوز | এড়িয়ে\_যাও | தவிர் | 通过 | パス |

---

## Variable Declaration

| Concept | en | fr | es | de | it | pt | pl | nl | sv | da | fi | hi | ar | bn | ta | zh | ja |
|---------|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
| `LET` | let | soit | sea | sei | sia | seja | niech | zij | låt | lad | olkoon | मान | ليكن | ধরি | இருக்கட்டும் | 令 | 変数 |
| `CONST` | const | constante | constante | konstante | costante | constante | stala | constante | konstant | konstant | vakio | स्थिरांक | ثابت | ধ্রুবক | மாறிலி | 常量 | 定数 |
| `GLOBAL` | global | mondial | global | global | globale | global | globalny | globaal | global | global | globaali | वैश्विक | عام | বৈশ্বিক | உலகளாவிய | 全局 | 大域 |
| `NONLOCAL` | nonlocal | nonlocal | nolocal | nichtlokal | nonlocale | naolocal | nielokalny | nietlocaal | icklokal | ikkelokal | eipaik | अस्थानीय | غير\_محلي | অ-স্থানীয় | உள்ளூர்\_அல்ல | 非局部 | 非局所 |
| `DEL` | del | supprimer | borrar | loeschen | cancella | apagar | usun | verwijder | radera | slet | poista | हटाओ | احذف | মুছ | நீக்கு | 删除 | 削除 |
| `ASSERT` | assert | affirmer | afirmar | versichern | verifica | verificar | sprawdz | bevestig | bekrafta | bekraeft | vahvista | सुनिश्चित | تأكد | নিশ্চিত | உறுதிப்படுத்து | 断言 | 断言 |

---

## Function and Class

| Concept | en | fr | es | de | it | pt | pl | nl | sv | da | fi | hi | ar | bn | ta | zh | ja |
|---------|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
| `FUNC_DEF` | def | déf | def | def | def | def | def | def | def | def | def | परिभाषा | دالة | ফাংশন | சார்பு | 定义 | 関数 |
| `RETURN` | return | retourner | retornar | zurueck | ritorna | retornar | zwroc | retourneer | returnera | returner | palauta | वापसी | إرجاع | ফেরত | திரும்பு | 返回 | 戻る |
| `CLASS_DEF` | class | classe | clase | klasse | classe | classe | klasa | klasse | klass | klasse | luokka | वर्ग | صنف | শ্রেণি | வகுப்பு | 类 | クラス |
| `LAMBDA` | lambda | lambda | lambda | lambda | lambda | lambda | lambda | lambda | lambda | lambda | lambda | लैम्बडा | لامدا | ল্যাম্বডা | லாம்டா | 匿名 | ラムダ |
| `YIELD` | yield | produire | producir | erzeugen | genera | produzir | wyprodu | produceer | producera | producere | tuota | उत्पन्न | اعطِ | উৎপন্ন | உற்பத்தி | 产出 | 産出 |
| `YIELD_FROM` | yield from | produire\_de | producir\_de | erzeugen\_von | genera\_da | produzir\_de | wyprodu\_z | produceer\_van | producera\_fran | producere\_fra | tuota\_kohteesta | उत्पन्न\_से | اعطِ\_من | উৎপন্ন\_থেকে | உற்பத்தி\_இருந்து | 从产出 | より産出 |

---

## Exception Handling

| Concept | en | fr | es | de | it | pt | pl | nl | sv | da | fi | hi | ar | bn | ta | zh | ja |
|---------|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
| `TRY` | try | essayer | intentar | versuche | prova | tentar | sprobuj | probeer | forsok | provedet | yrita | कोशिश | حاول | চেষ্টা | முயற்சி | 尝试 | 試す |
| `EXCEPT` | except | sauf | excepto | ausser | tranne | exceto | poza | behalve | utom | undtagen | paitsi | सिवाय | إلا | ছাড়া | தவிர | 除了 | 除いて |
| `FINALLY` | finally | finalement | finalmente | schliesslich | infine | finalmente | wreszcie | uiteindelijk | slutligen | endelig | viimein | अंत\_में | أخيرًا | অবশেষে | இறுதியாக | 最终 | 最終的に |
| `RAISE` | raise | soulever | lanzar | ausloesen | solleva | levantar | wrzuc | gooi | hojd | kast | nosta | उठाओ | أثِر | উত্থাপন | எறி | 引发 | 発生 |
| `WITH` | with | avec | con | mit | con | com | z | met | med | med | kanssa | साथ | مع | সাথে | உடன் | 用 | 付き |
| `AS` | as | comme | como | als | come | como | jako | als | som | som | kuin | रूपमें | كـ | হিসেবে | ஆக | 作为 | として |

---

## Async and Scope

| Concept | en | fr | es | de | it | pt | pl | nl | sv | da | fi | hi | ar | bn | ta | zh | ja |
|---------|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
| `ASYNC` | async | async | asinc | async | asinc | async | async | async | async | async | async | असिंक्रोनस | غير\_متزامن | অ্যাসিঙ্ক | ஒத்திசைவற்ற | 异步 | 非同期 |
| `AWAIT` | await | attendre | esperar | warten | attendi | esperar | czekaj | wacht | vanta | vent | odota | प्रतीक्षा | انتظر | অপেক্ষা | காத்திரு | 等待 | 待機 |
| `IMPORT` | import | importer | importar | importieren | importa | importar | importuj | importeer | importera | importere | tuo | आयात | استيراد | আমদানি | இறக்குமதி | 取込 | 取込 |
| `FROM` | from | de | de | von | da | de | z | van | fran | fra | kohteesta | से | من | থেকে | இருந்து | 从 | から |

---

## Import Keywords (Python API)

```python
from multilingualprogramming.keyword import KeywordRegistry

registry = KeywordRegistry()

# Concept → language keyword
print(registry.get_keyword("COND_IF", "fr"))   # si
print(registry.get_keyword("FUNC_DEF", "ja"))   # 関数
print(registry.get_keyword("LOOP_FOR", "ar"))   # لكل
print(registry.get_keyword("LET", "hi"))         # मान
print(registry.get_keyword("CLASS_DEF", "zh"))  # 类

# Language keyword → concept (reverse lookup)
print(registry.get_concept("si", "fr"))          # COND_IF
print(registry.get_concept("関数", "ja"))         # FUNC_DEF

# All supported languages
print(registry.get_supported_languages())
# ['en', 'fr', 'es', 'de', 'it', 'pt', 'pl', 'nl', 'sv', 'da', 'fi', 'hi', 'ar', 'bn', 'ta', 'zh', 'ja']

# All keywords for a language
keywords = registry.get_all_keywords("fr")
for concept, keyword in keywords.items():
    print(f"  {concept}: {keyword}")
```

---

## Builtin Aliases

Universal English builtin names always work. Additionally, each language has localized aliases:

| Concept | en | fr | es | de | ja | ar | hi | zh |
|---------|----|----|----|----|----|----|----|----|
| `print` | print | afficher | imprimir | ausgeben | 表示 | اطبع | छापो | 打印 |
| `range` | range | intervalle | rango | bereich | 範囲 | مدى | परास | 范围 |
| `len` | len | longueur | largo | länge | 長さ | طول | लंबाई | 长度 |
| `sum` | sum | somme | suma | summe | 合計 | مجموع | योग | 总和 |
| `abs` | abs | valeur\_abs | abs | absolutwert | 絶対値 | قيمة\_مطلقة | परम\_मूल्य | 绝对值 |
| `min` | min | minimum | minimo | minimum | 最小 | أصغر | न्यूनतम | 最小值 |
| `max` | max | maximum | maximo | maximum | 最大 | أكبر | अधिकतम | 最大值 |
| `sorted` | sorted | trie | ordenado | sortiert | ソート済み | مرتب | क्रमबद्ध | 排序 |
| `reversed` | reversed | inverse | invertido | umgekehrt | 逆順 | معكوس | उलटा | 反转 |
| `enumerate` | enumerate | enumerer | enumerar | aufzaehlen | 列挙 | عدِّد | गणना | 枚举 |
| `map` | map | appliquer | aplicar | anwenden | マップ | طبِّق | लागू | 映射 |
| `filter` | filter | filtrer | filtrar | filtern | フィルター | رشِّح | फ़िल्टर | 过滤 |
| `zip` | zip | combiner | combinar | kombinieren | 組み合わせ | اربط | जोड़ो | 压缩 |
| `list` | list | liste | lista | liste | リスト | قائمة | सूची | 列表 |
| `dict` | dict | dico | dicc | dict | 辞書 | قاموس | शब्दकोश | 字典 |
| `set` | set | ensemble | conjunto | menge | 集合 | مجموعة | समुच्चय | 集合 |
| `tuple` | tuple | tuple | tupla | tupel | タプル | تيوبل | ट्यूपल | 元组 |
| `type` | type | type | tipo | typ | 型 | نوع | प्रकार | 类型 |
| `isinstance` | isinstance | estinstance | esinstancia | istinstanz | インスタンス確認 | هل\_نوع | उदाहरण\_है | 是实例 |
| `input` | input | saisie | entrada | eingabe | 入力 | إدخال | इनपुट | 输入 |
| `open` | open | ouvrir | abrir | oeffnen | 開く | افتح | खोलो | 打开 |
| `round` | round | arrondir | redondear | runden | 丸める | أقرب | गोल | 四舍五入 |

> **Note**: Universal canonical names (e.g., `print`, `range`) always work in all languages. Aliases are additive — you can use either form.
