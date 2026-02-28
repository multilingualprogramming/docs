---
layout: page
title: "All 17 Languages"
description: "Complete program examples and keyword references for all 17 supported languages."
category: "Language Guide"
permalink: /language-guide/all-languages/
prev_page:
  title: "Keywords"
  url: /language-guide/keywords/
next_page:
  title: "Syntax Reference"
  url: /language-guide/syntax/
---

This page provides complete program examples for all 17 supported languages, demonstrating variables, control flow, functions, and classes. Each example is a complete, runnable program.

All programs produce identical output regardless of language used.

---

## English (`en`) {#english}

```python
import math
from math import sqrt as root_fn

let shared_counter = 3

def bump_global():
    global shared_counter
    shared_counter = shared_counter + 2
    return shared_counter

def make_counter(start):
    let total = start
    def step():
        nonlocal total
        total = total + 1
        return total
    return step

let next_count = make_counter(5)
let first_step = next_count()
let second_step = next_count()

let zipped_pairs = list(zip([1, 2, 3], [4, 5, 6]))
let unique_values = set([1, 1, 2, 3])
let fixed_values = tuple([10, 20, 30])

let first_item, *middle_items, last_item = [1, 2, 3, 4]
let merged_map = {**{"x": 1}, **{"y": 2}}

def format_tag(a, /, *, b):
    return f"{a}-{b:.1f}"

let seed = 0
let walrus_value = (seed := seed + 9)

class CounterBox:
    def __init__(self, start_base):
        self.value = start_base

class CounterBoxChild(CounterBox):
    def __init__(self, start_base):
        super(CounterBoxChild, self).__init__(start_base)
        self.value = self.value + 1

def produce_three():
    for idx in range(3):
        yield idx

let produced_total = sum(produce_three())

try:
    if len(unique_values) > 2:
        raise ValueError("boom")
except ValueError as handled_error:
    let handled = True
finally:
    let root_value = int(root_fn(16))

print(f"counter={bump_global()}, root={root_value}, total={produced_total}")
```

**Run:**
```bash
python -m multilingualprogramming run program.ml --lang en
```

---

## French (`fr`) {#french}

```python
importer math
de math importer sqrt comme root_fn

soit compteur_partage = 3

déf augmenter_global():
    mondial compteur_partage
    compteur_partage = compteur_partage + 2
    retourner compteur_partage

déf creer_compteur(debut):
    soit total = debut
    déf etape():
        nonlocal total
        total = total + 1
        retourner total
    retourner etape

soit prochain_compte = creer_compteur(5)
soit premier_pas = prochain_compte()
soit deuxieme_pas = prochain_compte()

soit paires_combinees = liste(combiner([1, 2, 3], [4, 5, 6]))
soit valeurs_uniques = ensemble([1, 1, 2, 3])
soit valeurs_fixes = tuple([10, 20, 30])

soit premier_elem, *milieu, dernier_elem = [1, 2, 3, 4]
soit carte_fusionnee = {**{"x": 1}, **{"y": 2}}

déf formater_etiquette(a, /, *, b):
    retourner f"{a}-{b:.1f}"

soit graine = 0
soit valeur_walrus = (graine := graine + 9)

classe BoiteCompteur:
    déf __init__(self, base_debut):
        self.valeur = base_debut

classe BoiteCompteurEnfant(BoiteCompteur):
    déf __init__(self, base_debut):
        super(BoiteCompteurEnfant, self).__init__(base_debut)
        self.valeur = self.valeur + 1

déf produire_trois():
    pour idx dans intervalle(3):
        produire idx

soit total_produit = somme(produire_trois())

essayer:
    si longueur(valeurs_uniques) > 2:
        soulever ValueError("boom")
sauf ValueError comme erreur_traitee:
    soit traite = Vrai
finalement:
    soit valeur_racine = int(root_fn(16))

afficher(f"compteur={augmenter_global()}, racine={valeur_racine}, total={total_produit}")
```

**Run:**
```bash
python -m multilingualprogramming run programme.ml --lang fr
```

---

## Spanish (`es`) {#spanish}

```python
importar math
de math importar sqrt como root_fn

sea contador_compartido = 3

def incrementar_global():
    global contador_compartido
    contador_compartido = contador_compartido + 2
    retornar contador_compartido

def crear_contador(inicio):
    sea total = inicio
    def paso():
        nonlocal total
        total = total + 1
        retornar total
    retornar paso

sea proximo_contador = crear_contador(5)
sea primer_paso = proximo_contador()
sea segundo_paso = proximo_contador()

sea pares_combinados = lista(combinar([1, 2, 3], [4, 5, 6]))
sea valores_unicos = conjunto([1, 1, 2, 3])
sea valores_fijos = tupla([10, 20, 30])

sea primer_elem, *medio, ultimo_elem = [1, 2, 3, 4]
sea mapa_fusionado = {**{"x": 1}, **{"y": 2}}

def formatear_etiqueta(a, /, *, b):
    retornar f"{a}-{b:.1f}"

sea semilla = 0
sea valor_walrus = (semilla := semilla + 9)

clase CajaContador:
    def __init__(self, base_inicio):
        self.valor = base_inicio

clase CajaContadorHijo(CajaContador):
    def __init__(self, base_inicio):
        super(CajaContadorHijo, self).__init__(base_inicio)
        self.valor = self.valor + 1

def producir_tres():
    para idx en rango(3):
        producir idx

sea total_producido = suma(producir_tres())

intentar:
    si largo(valores_unicos) > 2:
        lanzar ValueError("boom")
excepto ValueError como error_manejado:
    sea manejado = Verdadero
finalmente:
    sea valor_raiz = int(root_fn(16))

imprimir(f"contador={incrementar_global()}, raiz={valor_raiz}, total={total_producido}")
```

---

## German (`de`) {#german}

```python
importieren math
von math importieren sqrt als root_fn

sei gemeinsamer_zaehler = 3

def erhoehe_global():
    global gemeinsamer_zaehler
    gemeinsamer_zaehler = gemeinsamer_zaehler + 2
    zurueck gemeinsamer_zaehler

def erstelle_zaehler(start):
    sei gesamt = start
    def schritt():
        nichtlokal gesamt
        gesamt = gesamt + 1
        zurueck gesamt
    zurueck schritt

sei naechster_zaehler = erstelle_zaehler(5)
sei erster_schritt = naechster_zaehler()
sei zweiter_schritt = naechster_zaehler()

sei gezippte_paare = liste(kombinieren([1, 2, 3], [4, 5, 6]))
sei eindeutige_werte = menge([1, 1, 2, 3])
sei feste_werte = tupel([10, 20, 30])

sei erstes_elem, *mitte, letztes_elem = [1, 2, 3, 4]
sei zusammengefuehrt = {**{"x": 1}, **{"y": 2}}

def format_tag(a, /, *, b):
    zurueck f"{a}-{b:.1f}"

sei startpunkt = 0
sei walrus_wert = (startpunkt := startpunkt + 9)

klasse ZaehlerBox:
    def __init__(self, start_basis):
        self.wert = start_basis

klasse ZaehlerBoxKind(ZaehlerBox):
    def __init__(self, start_basis):
        super(ZaehlerBoxKind, self).__init__(start_basis)
        self.wert = self.wert + 1

def drei_erzeugen():
    für idx in bereich(3):
        erzeugen idx

sei gesamt_erzeugt = summe(drei_erzeugen())

versuche:
    wenn länge(eindeutige_werte) > 2:
        ausloesen ValueError("boom")
ausser ValueError als behandelter_fehler:
    sei behandelt = Wahr
schliesslich:
    sei wurzel_wert = int(root_fn(16))

ausgeben(f"zaehler={erhoehe_global()}, wurzel={wurzel_wert}, gesamt={gesamt_erzeugt}")
```

---

## Italian (`it`) {#italian}

```python
sia contatore_condiviso = 3

def incrementa_globale():
    globale contatore_condiviso
    contatore_condiviso = contatore_condiviso + 2
    ritorna contatore_condiviso

def crea_contatore(inizio):
    sia totale = inizio
    def passo():
        nonlocale totale
        totale = totale + 1
        ritorna totale
    ritorna passo

sia prossimo_contatore = crea_contatore(5)
sia primo_passo = prossimo_contatore()
sia secondo_passo = prossimo_contatore()

sia coppie_unite = lista(combina([1, 2, 3], [4, 5, 6]))
sia valori_unici = insieme([1, 1, 2, 3])
sia valori_fissi = tupla([10, 20, 30])

sia primo_elem, *mezzo, ultimo_elem = [1, 2, 3, 4]

classe ScatolaContatore:
    def __init__(self, base_inizio):
        self.valore = base_inizio

classe ScatolaContatoreFilglio(ScatolaContatore):
    def __init__(self, base_inizio):
        super(ScatolaContatoreFilglio, self).__init__(base_inizio)
        self.valore = self.valore + 1

def produci_tre():
    per idx in intervallo(3):
        genera idx

sia totale_prodotto = somma(produci_tre())

prova:
    se lunghezza(valori_unici) > 2:
        solleva ValueError("boom")
tranne ValueError come errore_gestito:
    sia gestito = Vero
infine:
    sia valore_radice = int(root_fn(16))

stampa(f"contatore={incrementa_globale()}, radice={valore_radice}, totale={totale_prodotto}")
```

---

## Portuguese (`pt`) {#portuguese}

```python
seja contador_compartilhado = 3

def incrementar_global():
    global contador_compartilhado
    contador_compartilhado = contador_compartilhado + 2
    retornar contador_compartilhado

def criar_contador(inicio):
    seja total = inicio
    def passo():
        nonlocal total
        total = total + 1
        retornar total
    retornar passo

seja proximo_contador = criar_contador(5)
seja primeiro_passo = proximo_contador()
seja segundo_passo = proximo_contador()

seja pares_combinados = lista(combinar([1, 2, 3], [4, 5, 6]))
seja valores_unicos = conjunto([1, 1, 2, 3])
seja valores_fixos = tupla([10, 20, 30])

classe CaixaContador:
    def __init__(self, base_inicio):
        self.valor = base_inicio

classe CaixaContadorFilho(CaixaContador):
    def __init__(self, base_inicio):
        super(CaixaContadorFilho, self).__init__(base_inicio)
        self.valor = self.valor + 1

def produzir_tres():
    para idx em intervalo(3):
        produzir idx

seja total_produzido = soma(produzir_tres())

tentar:
    se largo(valores_unicos) > 2:
        levantar ValueError("boom")
exceto ValueError como erro_tratado:
    seja tratado = Verdadeiro
finalmente:
    seja valor_raiz = int(root_fn(16))

imprimir(f"contador={incrementar_global()}, raiz={valor_raiz}, total={total_produzido}")
```

---

## Polish (`pl`) {#polish}

```python
niech wspolny_licznik = 3

def zwieksz_globalny():
    globalny wspolny_licznik
    wspolny_licznik = wspolny_licznik + 2
    zwroc wspolny_licznik

def stworz_licznik(start):
    niech suma = start
    def krok():
        nielokalny suma
        suma = suma + 1
        zwroc suma
    zwroc krok

niech nastepny_licznik = stworz_licznik(5)
niech pierwszy_krok = nastepny_licznik()
niech drugi_krok = nastepny_licznik()

niech unikalne = zbior([1, 1, 2, 3])

klasa PudelkoLicznika:
    def __init__(self, baza_start):
        self.wartosc = baza_start

klasa PudelkoLicznikaDziecko(PudelkoLicznika):
    def __init__(self, baza_start):
        super(PudelkoLicznikaDziecko, self).__init__(baza_start)
        self.wartosc = self.wartosc + 1

def produkuj_trzy():
    dla idx w zakresie(3):
        wyprodu idx

niech suma_wyprodukowana = sumuj(produkuj_trzy())

sprobuj:
    jezeli dlugosc(unikalne) > 2:
        wrzuc ValueError("boom")
poza ValueError jako obsluzony_blad:
    niech obsluzony = Prawda
wreszcie:
    niech wartosc_pierwiastka = int(root_fn(16))

wypisz(f"licznik={zwieksz_globalny()}, pierwiastek={wartosc_pierwiastka}, suma={suma_wyprodukowana}")
```

---

## Dutch (`nl`) {#dutch}

```python
zij gedeelde_teller = 3

def verhoog_globaal():
    globaal gedeelde_teller
    gedeelde_teller = gedeelde_teller + 2
    retourneer gedeelde_teller

def maak_teller(start):
    zij totaal = start
    def stap():
        nietlocaal totaal
        totaal = totaal + 1
        retourneer totaal
    retourneer stap

zij volgende_teller = maak_teller(5)
zij eerste_stap = volgende_teller()
zij tweede_stap = volgende_teller()

zij unieke_waarden = verzameling([1, 1, 2, 3])

klasse TellerDoos:
    def __init__(self, start_basis):
        self.waarde = start_basis

def produceer_drie():
    voor idx in bereik(3):
        produceer idx

zij totaal_geproduceerd = som(produceer_drie())

probeer:
    als lengte(unieke_waarden) > 2:
        gooi ValueError("boom")
behalve ValueError als behandelde_fout:
    zij behandeld = Waar
uiteindelijk:
    zij wortel_waarde = int(root_fn(16))

druk_af(f"teller={verhoog_globaal()}, wortel={wortel_waarde}, totaal={totaal_geproduceerd}")
```

---

## Swedish (`sv`) {#swedish}

```python
låt delad_rakare = 3

def oka_global():
    global delad_rakare
    delad_rakare = delad_rakare + 2
    returnera delad_rakare

def skapa_rakare(start):
    låt totalt = start
    def steg():
        icklokal totalt
        totalt = totalt + 1
        returnera totalt
    returnera steg

låt nasta_rakare = skapa_rakare(5)
låt forsta_steg = nasta_rakare()
låt andra_steg = nasta_rakare()

låt unika_varden = uppsattning([1, 1, 2, 3])

klass RakareBox:
    def __init__(self, start_bas):
        self.varde = start_bas

def producera_tre():
    for idx i intervall(3):
        producera idx

låt total_producerat = summa(producera_tre())

forsok:
    om langd(unika_varden) > 2:
        hojd ValueError("boom")
utom ValueError som hanterat_fel:
    låt hanterat = Sant
slutligen:
    låt rot_varde = int(root_fn(16))

skriv_ut(f"rakare={oka_global()}, rot={rot_varde}, total={total_producerat}")
```

---

## Danish (`da`) {#danish}

```python
lad delt_taeller = 3

def oeg_global():
    global delt_taeller
    delt_taeller = delt_taeller + 2
    returner delt_taeller

def opret_taeller(start):
    lad total = start
    def trin():
        ikkelokal total
        total = total + 1
        returner total
    returner trin

lad naeste_taeller = opret_taeller(5)
lad foerste_trin = naeste_taeller()
lad andet_trin = naeste_taeller()

lad unikke_vaerdier = saet([1, 1, 2, 3])

klasse TaellerBoks:
    def __init__(self, start_basis):
        self.vaerdi = start_basis

def producere_tre():
    for idx i omrade(3):
        producere idx

lad samlet_produceret = sum(producere_tre())

provedet:
    hvis laengde(unikke_vaerdier) > 2:
        kast ValueError("boom")
undtagen ValueError som behandlet_fejl:
    lad behandlet = Sand
endelig:
    lad rod_vaerdi = int(root_fn(16))

udskriv(f"taeller={oeg_global()}, rod={rod_vaerdi}, total={samlet_produceret}")
```

---

## Finnish (`fi`) {#finnish}

```python
olkoon yhteinen_laskuri = 3

def kasvata_globaali():
    globaali yhteinen_laskuri
    yhteinen_laskuri = yhteinen_laskuri + 2
    palauta yhteinen_laskuri

def luo_laskuri(alku):
    olkoon yhteensa = alku
    def askel():
        eipaik yhteensa
        yhteensa = yhteensa + 1
        palauta yhteensa
    palauta askel

olkoon seuraava_laskuri = luo_laskuri(5)
olkoon ensimmainen_askel = seuraava_laskuri()
olkoon toinen_askel = seuraava_laskuri()

olkoon uniikit_arvot = joukko([1, 1, 2, 3])

luokka LaskuriLaatikko:
    def __init__(self, alku_pohja):
        self.arvo = alku_pohja

def tuota_kolme():
    jokaiselle idx in valimat(3):
        tuota idx

olkoon tuotettu_yhteensa = yhteenlaske(tuota_kolme())

yrita:
    jos pituus(uniikit_arvot) > 2:
        nosta ValueError("boom")
paitsi ValueError kuin kasitelty_virhe:
    olkoon kasitelty = Tosi
viimein:
    olkoon juuriarvo = int(root_fn(16))

tulosta(f"laskuri={kasvata_globaali()}, juuri={juuriarvo}, yhteensa={tuotettu_yhteensa}")
```

---

## Hindi (`hi`) {#hindi}

```python
आयात math
से math आयात sqrt रूपमें root_fn

मान साझा_गणक = 3

परिभाषा बढाएं_वैश्विक():
    वैश्विक साझा_गणक
    साझा_गणक = साझा_गणक + 2
    वापसी साझा_गणक

परिभाषा बनाएं_गणक(शुरुआत):
    मान total = शुरुआत
    परिभाषा कदम():
        अस्थानीय total
        total = total + 1
        वापसी total
    वापसी कदम

मान अगला_गणक = बनाएं_गणक(5)
मान पहला_कदम = अगला_गणक()
मान दूसरा_कदम = अगला_गणक()

मान जिप्पड_जोडी = सूची(जोड़ो([1, 2, 3], [4, 5, 6]))
मान अनन्य_मान = समुच्चय([1, 1, 2, 3])
मान निश्चित_मान = ट्यूपल([10, 20, 30])

मान पहला_वस्तु, *मध्य_वस्तुएं, अंतिम_वस्तु = [1, 2, 3, 4]
मान मर्ज_मैप = {**{"x": 1}, **{"y": 2}}

परिभाषा लेबल_स्वरूप(a, /, *, b):
    वापसी f"{a}-{b:.1f}"

मान बीज = 0
मान वालरस_मूल्य = (बीज := बीज + 9)

वर्ग गणक_डिब्बा:
    परिभाषा __init__(self, आधार_शुरुआत):
        self.मूल्य = आधार_शुरुआत

वर्ग गणक_डिब्बा_बाल(गणक_डिब्बा):
    परिभाषा __init__(self, आधार_शुरुआत):
        सुपर(गणक_डिब्बा_बाल, self).__init__(आधार_शुरुआत)
        self.मूल्य = self.मूल्य + 1

परिभाषा तीन_उत्पन्न():
    के_लिए idx में परास(3):
        उत्पन्न idx

मान उत्पन्न_कुल = योग(तीन_उत्पन्न())

कोशिश:
    अगर लंबाई(अनन्य_मान) > 2:
        उठाओ ValueError("boom")
सिवाय ValueError रूपमें संभाला_त्रुटि:
    मान संभाला = सच
अंत_में:
    मान मूल_मूल्य = int(root_fn(16))

छापो(f"गणक={बढाएं_वैश्विक()}, मूल={मूल_मूल्य}, कुल={उत्पन्न_कुल}")
```

**Run:**
```bash
python -m multilingualprogramming run program.ml --lang hi
```

---

## Arabic (`ar`) {#arabic}

```python
استيراد math
من math استيراد sqrt كـ root_fn

ليكن عداد_مشترك = 3

دالة زيادة_عام():
    عام عداد_مشترك
    عداد_مشترك = عداد_مشترك + 2
    إرجاع عداد_مشترك

دالة إنشاء_عداد(بداية):
    ليكن total = بداية
    دالة خطوة():
        غير_محلي total
        total = total + 1
        إرجاع total
    إرجاع خطوة

ليكن العداد_التالي = إنشاء_عداد(5)
ليكن الخطوة_الأولى = العداد_التالي()
ليكن الخطوة_الثانية = العداد_التالي()

ليكن أزواج_مربوطة = قائمة(اربط([1, 2, 3], [4, 5, 6]))
ليكن قيم_فريدة = مجموعة([1, 1, 2, 3])
ليكن قيم_ثابتة = تيوبل([10, 20, 30])

ليكن العنصر_الأول, *العناصر_الوسطى, العنصر_الأخير = [1, 2, 3, 4]
ليكن الخريطة_المدمجة = {**{"x": 1}, **{"y": 2}}

دالة تنسيق_الوسم(a, /, *, b):
    إرجاع f"{a}-{b:.1f}"

ليكن البذرة = 0
ليكن قيمة_المهمة = (البذرة := البذرة + 9)

صنف صندوق_العداد:
    دالة __init__(self, أساس_البداية):
        self.القيمة = أساس_البداية

صنف صندوق_العداد_الفرعي(صندوق_العداد):
    دالة __init__(self, أساس_البداية):
        فئة_أب(صندوق_العداد_الفرعي, self).__init__(أساس_البداية)
        self.القيمة = self.القيمة + 1

دالة إنتاج_ثلاثة():
    لكل idx في مدى(3):
        اعطِ idx

ليكن مجموع_المُنتج = مجموع(إنتاج_ثلاثة())

حاول:
    إذا طول(قيم_فريدة) > 2:
        أثِر ValueError("boom")
إلا ValueError كـ الخطأ_المعالج:
    ليكن معالج = صحيح
أخيرًا:
    ليكن قيمة_الجذر = int(root_fn(16))

اطبع(f"عداد={زيادة_عام()}, جذر={قيمة_الجذر}, مجموع={مجموع_المُنتج}")
```

**Run:**
```bash
python -m multilingualprogramming run program.ml --lang ar
```

---

## Bengali (`bn`) {#bengali}

```python
ধরি ভাগ_করা_গণক = 3

ফাংশন বৃদ্ধি_বৈশ্বিক():
    বৈশ্বিক ভাগ_করা_গণক
    ভাগ_করা_গণক = ভাগ_করা_গণক + 2
    ফেরত ভাগ_করা_গণক

ফাংশন তৈরি_গণক(শুরু):
    ধরি মোট = শুরু
    ফাংশন ধাপ():
        অ-স্থানীয় মোট
        মোট = মোট + 1
        ফেরত মোট
    ফেরত ধাপ

ধরি পরবর্তী_গণক = তৈরি_গণক(5)
ধরি প্রথম_ধাপ = পরবর্তী_গণক()
ধরি দ্বিতীয়_ধাপ = পরবর্তী_গণক()

ধরি অনন্য_মান = সেট([1, 1, 2, 3])

শ্রেণি গণক_বাক্স:
    ফাংশন __init__(self, ভিত্তি_শুরু):
        self.মান = ভিত্তি_শুরু

শ্রেণি গণক_বাক্স_শিশু(গণক_বাক্স):
    ফাংশন __init__(self, ভিত্তি_শুরু):
        super(গণক_বাক্স_শিশু, self).__init__(ভিত্তি_শুরু)
        self.মান = self.মান + 1

ফাংশন তিন_উৎপন্ন():
    জন্য idx মধ্যে পরিসর(3):
        উৎপন্ন idx

ধরি উৎপাদিত_মোট = যোগফল(তিন_উৎপন্ন())

চেষ্টা:
    যদি দৈর্ঘ্য(অনন্য_মান) > 2:
        উত্থাপন ValueError("boom")
ছাড়া ValueError হিসেবে পরিচালিত_ত্রুটি:
    ধরি পরিচালিত = সত্য
অবশেষে:
    ধরি মূল_মান = int(root_fn(16))

ছাপাও(f"গণক={বৃদ্ধি_বৈশ্বিক()}, মূল={মূল_মান}, মোট={উৎপাদিত_মোট}")
```

---

## Tamil (`ta`) {#tamil}

```python
இருக்கட்டும் பகிர்ந்த_கணக்கி = 3

சார்பு அதிகரி_உலகளாவிய():
    உலகளாவிய பகிர்ந்த_கணக்கி
    பகிர்ந்த_கணக்கி = பகிர்ந்த_கணக்கி + 2
    திரும்பு பகிர்ந்த_கணக்கி

சார்பு உருவாக்கு_கணக்கி(தொடக்கம்):
    இருக்கட்டும் மொத்தம் = தொடக்கம்
    சார்பு படி():
        உள்ளூர்_அல்ல மொத்தம்
        மொத்தம் = மொத்தம் + 1
        திரும்பு மொத்தம்
    திரும்பு படி

இருக்கட்டும் அடுத்த_கணக்கி = உருவாக்கு_கணக்கி(5)
இருக்கட்டும் முதல்_படி = அடுத்த_கணக்கி()
இருக்கட்டும் இரண்டாவது_படி = அடுத்த_கணக்கி()

இருக்கட்டும் தனித்துவ_மதிப்புகள் = தொகுப்பு([1, 1, 2, 3])

வகுப்பு கணக்கி_பெட்டி:
    சார்பு __init__(self, அடிப்படை_தொடக்கம்):
        self.மதிப்பு = அடிப்படை_தொடக்கம்

வகுப்பு கணக்கி_பெட்டி_குழந்தை(கணக்கி_பெட்டி):
    சார்பு __init__(self, அடிப்படை_தொடக்கம்):
        super(கணக்கி_பெட்டி_குழந்தை, self).__init__(அடிப்படை_தொடக்கம்)
        self.மதிப்பு = self.மதிப்பு + 1

சார்பு மூன்று_உற்பத்தி():
    ஒவ்வொரு idx இல் வரம்பு(3):
        உற்பத்தி idx

இருக்கட்டும் உற்பத்தி_மொத்தம் = தொகை(மூன்று_உற்பத்தி())

முயற்சி:
    என்றால் நீளம்(தனித்துவ_மதிப்புகள்) > 2:
        எறி ValueError("boom")
தவிர ValueError ஆக கையாளப்பட்ட_பிழை:
    இருக்கட்டும் கையாளப்பட்டது = உண்மை
இறுதியாக:
    இருக்கட்டும் மூல_மதிப்பு = int(root_fn(16))

அச்சிடு(f"கணக்கி={அதிகரி_உலகளாவிய()}, மூலம்={மூல_மதிப்பு}, மொத்தம்={உற்பத்தி_மொத்தம்}")
```

---

## Chinese Simplified (`zh`) {#chinese}

```python
取込 math
从 math 取込 sqrt 作为 root_fn

令 共享_计数器 = 3

定义 增加_全局():
    全局 共享_计数器
    共享_计数器 = 共享_计数器 + 2
    返回 共享_计数器

定义 创建_计数器(开始):
    令 total = 开始
    定义 步骤():
        非局部 total
        total = total + 1
        返回 total
    返回 步骤

令 下一个_计数器 = 创建_计数器(5)
令 第一步 = 下一个_计数器()
令 第二步 = 下一个_计数器()

令 压缩_对 = 列表(压缩([1, 2, 3], [4, 5, 6]))
令 唯一_值 = 集合([1, 1, 2, 3])
令 固定_值 = 元组([10, 20, 30])

令 第一项, *中间项, 最后项 = [1, 2, 3, 4]
令 合并_映射 = {**{"x": 1}, **{"y": 2}}

定义 格式_标签(a, /, *, b):
    返回 f"{a}-{b:.1f}"

令 种子 = 0
令 海象_值 = (种子 := 种子 + 9)

类 计数器_盒子:
    定义 __init__(self, 起始_基础):
        self.值 = 起始_基础

类 计数器_盒子_子类(计数器_盒子):
    定义 __init__(self, 起始_基础):
        父类(计数器_盒子_子类, self).__init__(起始_基础)
        self.值 = self.值 + 1

定义 产出_三():
    对于 idx 里 范围(3):
        产出 idx

令 产出_总计 = 总和(产出_三())

尝试:
    如果 长度(唯一_值) > 2:
        引发 ValueError("boom")
除了 ValueError 作为 处理的_错误:
    令 处理 = 真
最终:
    令 根_值 = int(root_fn(16))

打印(f"计数器={增加_全局()}, 根={根_值}, 总计={产出_总计}")
```

**Run:**
```bash
python -m multilingualprogramming run program.ml --lang zh
```

---

## Japanese (`ja`) {#japanese}

```python
取込 math
から math 取込 sqrt として root_fn

変数 共有_カウンタ = 3

関数 増加_グローバル():
    大域 共有_カウンタ
    共有_カウンタ = 共有_カウンタ + 2
    戻る 共有_カウンタ

関数 作成_カウンタ(開始):
    変数 total = 開始
    関数 ステップ():
        非局所 total
        total = total + 1
        戻る total
    戻る ステップ

変数 次_カウンタ = 作成_カウンタ(5)
変数 最初_ステップ = 次_カウンタ()
変数 第二_ステップ = 次_カウンタ()

変数 ペア化_項目 = リスト(組み合わせ([1, 2, 3], [4, 5, 6]))
変数 ユニーク_値 = 集合([1, 1, 2, 3])
変数 固定_値 = タプル([10, 20, 30])

変数 最初_項目, *中間_項目, 最後_項目 = [1, 2, 3, 4]
変数 合成_マップ = {**{"x": 1}, **{"y": 2}}

関数 ラベル_フォーマット関数(a, /, *, b):
    戻る f"{a}-{b:.1f}"

変数 シード = 0
変数 ウォルラス_値 = (シード := シード + 9)

クラス カウンタ_ボックス:
    関数 __init__(self, 開始_基底):
        self.値 = 開始_基底

クラス カウンタ_子ボックス(カウンタ_ボックス):
    関数 __init__(self, 開始_基底):
        親クラス(カウンタ_子ボックス, self).__init__(開始_基底)
        self.値 = self.値 + 1

関数 三つ_産出():
    毎 idx 中 範囲(3):
        産出 idx

変数 産出_合計 = 合計(三つ_産出())

試す:
    もし 長さ(ユニーク_値) > 2:
        発生 ValueError("boom")
除いて ValueError として 処理済み_エラー:
    変数 処理済み = 真
最終的に:
    変数 根_値 = int(root_fn(16))

表示(f"カウンタ={増加_グローバル()}, 根={根_値}, 合計={産出_合計}")
```

**Run:**
```bash
python -m multilingualprogramming run program.ml --lang ja
```

---

## Surface Normalization (SOV/RTL Languages)

For languages like Japanese, Arabic, Hindi, Bengali, and Tamil, natural word order differs from the default positional grammar. The surface normalizer rewrites natural forms before parsing.

### Japanese — for loop (iterable-first)

Natural form (accepted):
```python
範囲(6) 内の 各 i に対して:
    表示(i)
```

Canonical form (also accepted):
```python
毎 i 中 範囲(6):
    表示(i)
```

Both compile to the same Core AST.

### Arabic — for loop

Natural form:
```python
لكل i في مدى(4):
    اطبع(i)
```

### Running All Examples

```bash
# Validate all 17 languages
python -m multilingualprogramming smoke --all

# Run specific language smoke test
python -m multilingualprogramming smoke --lang fr
```
