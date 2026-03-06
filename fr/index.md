---
layout: home
page_id: home
locale: fr
title: "Langage de programmation multilingue"
description: "Ecrivez des programmes en anglais, francais, espagnol, japonais, arabe, hindi et plus encore. Un seul noyau formel. Backends Python et WASM."
permalink: /fr/
---

<section class="hero">
  <span class="hero-eyebrow">v0.5.1 &mdash; Maintenant avec WASM et POO</span>
  <h1 class="hero-title">
    Ecrivez du code en<br/>
    <span class="gradient-text">toute langue humaine</span>
  </h1>
  <p class="hero-description">
    <strong>multilingual</strong> est un langage de programmation avec un noyau semantique formel unique et plusieurs interfaces en langues naturelles. Ecrivez en anglais, francais, espagnol, japonais, arabe, hindi et plus encore &mdash; compilez vers Python ou WASM.
  </p>
  <div class="hero-actions">
    <a href="{{ '/fr/docs/demarrage/' | relative_url }}" class="btn btn-primary">Commencer &rarr;</a>
    <a href="{{ '/fr/docs/guide-langage/' | relative_url }}" class="btn btn-secondary">Guide du langage</a>
    <a href="https://github.com/johnsamuelwrites/multilingual" class="btn btn-secondary" target="_blank" rel="noopener">Voir sur GitHub</a>
  </div>
</section>

<div class="stats-strip">
  <div class="stat-item">
    <div class="stat-value">17</div>
    <div class="stat-label">Langues humaines</div>
  </div>
  <div class="stat-item">
    <div class="stat-value">1,797</div>
    <div class="stat-label">Cas de test</div>
  </div>
  <div class="stat-item">
    <div class="stat-value">100x</div>
    <div class="stat-label">Acceleration WASM</div>
  </div>
  <div class="stat-item">
    <div class="stat-value">41</div>
    <div class="stat-label">Fonctions localisees</div>
  </div>
  <div class="stat-item">
    <div class="stat-value">0.5.1</div>
    <div class="stat-label">Version actuelle</div>
  </div>
</div>

<section class="home-section" style="padding-top:3rem" markdown="1">
  <div style="text-align:center; margin-bottom:2rem">
    <span class="section-eyebrow">Le meme programme, dans chaque langue</span>
    <h2 class="section-title">Un modele syntaxique, 17 expressions</h2>
    <p class="section-desc" style="margin: 0 auto 0">Ecrivez la meme logique dans n'importe quelle langue prise en charge. Le compilateur la projette vers le meme noyau formel et la meme sortie Python.</p>
  </div>

<div class="code-demo">
  <div class="code-demo-header">
    <span class="code-demo-dot dot-red"></span>
    <span class="code-demo-dot dot-yellow"></span>
    <span class="code-demo-dot dot-green"></span>
    <span class="code-demo-title">bonjour.ml</span>
  </div>
  <div class="code-demo-tabs">
    <button class="code-tab active" data-target="en">Anglais</button>
    <button class="code-tab" data-target="fr">Francais</button>
    <button class="code-tab" data-target="es">Espagnol</button>
    <button class="code-tab" data-target="ja">Japonais</button>
    <button class="code-tab" data-target="ar">Arabe</button>
    <button class="code-tab" data-target="hi">Hindi</button>
  </div>
  <div class="code-demo-body">
    <div class="code-panel" data-lang="en" style="display:block">
{% highlight python %}
let name = "world"
let count = 5

def greet(n):
    for i in range(count):
        print(f"Hello, {n}! iteration {i}")

greet(name)
{% endhighlight %}
</div>
    <div class="code-panel" data-lang="fr" style="display:none">
{% highlight python %}
soit nom = "monde"
soit compteur = 5

fonction saluer(n):
    pour i dans intervalle(compteur):
        afficher(f"Bonjour, {n} ! iteration {i}")

saluer(nom)
{% endhighlight %}
</div>
    <div class="code-panel" data-lang="es" style="display:none">
{% highlight python %}
sea nombre = "mundo"
sea contador = 5

def saludar(n):
    para i en rango(contador):
        imprimir(f"Hola, {n}! iteracion {i}")

saludar(nombre)
{% endhighlight %}
</div>
    <div class="code-panel" data-lang="ja" style="display:none">
{% highlight python %}
変数 名前 = "世界"
変数 カウント = 5

関数 挨拶(n):
    毎 i 中 範囲(カウント):
        表示(f"こんにちは {n} 繰り返し {i}")

挨拶(名前)
{% endhighlight %}
</div>
    <div class="code-panel" data-lang="ar" style="display:none">
{% highlight python %}
ليكن اسم = "العالم"
ليكن عداد = 5

دالة تحية(n):
    لكل i في مدى(عداد):
        اطبع(f"مرحبا {n} تكرار {i}")

تحية(اسم)
{% endhighlight %}
</div>
    <div class="code-panel" data-lang="hi" style="display:none">
{% highlight python %}
मान नाम = "दुनिया"
मान गिनती = 5

परिभाषा नमस्ते(n):
    के_लिए i में परास(गिनती):
        छापो(f"नमस्ते {n} पुनरावृत्ति {i}")

नमस्ते(नाम)
{% endhighlight %}
</div>
  </div>
</div>

</section>

<section class="home-section" markdown="1">
  <span class="section-eyebrow">Pourquoi multilingual ?</span>
  <h2 class="section-title">Concu pour le monde entier</h2>

<div class="feature-grid">

<div class="feature-card">
<span class="feature-icon">🌐</span>
<div class="feature-title">17 langues humaines</div>
<p class="feature-desc">Anglais, francais, espagnol, allemand, italien, portugais, polonais, neerlandais, suedois, danois, finnois, hindi, arabe, bengali, tamoul, chinois et japonais, tous comme interfaces de premier rang.</p>
</div>

<div class="feature-card">
<span class="feature-icon">⬡</span>
<div class="feature-title">Un seul noyau formel</div>
<p class="feature-desc">Toutes les interfaces linguistiques compilent vers le meme AST central et le meme CoreIRProgram. La semantique reste identique quelle que soit la langue de surface.</p>
</div>

<div class="feature-card">
<span class="feature-icon">⚡</span>
<div class="feature-title">Backend WASM</div>
<p class="feature-desc">Le backend WebAssembly optionnel apporte des accelerations de 50x a 100x pour les operations matricielles, la cryptographie, le calcul scientifique et plus encore, avec repli automatique sur Python.</p>
</div>

<div class="feature-card">
<span class="feature-icon">🐍</span>
<div class="feature-title">Compatible Python</div>
<p class="feature-desc">Sous-ensemble complet de la syntaxe Python 3.12+ : classes, async/await, comprehensions, decorateurs, f-strings, pattern matching, generateurs, context managers, et plus.</p>
</div>

<div class="feature-card">
<span class="feature-icon">🔧</span>
<div class="feature-title">Extensibilite guidee par les donnees</div>
<p class="feature-desc">Ajoutez une nouvelle langue de programmation principalement via des fichiers de configuration JSON, sans reecrire le parseur. Mots-cles, fonctions integrees et patterns de surface sont decrits comme des donnees.</p>
</div>

<div class="feature-card">
<span class="feature-icon">🧪</span>
<div class="feature-title">~1,797 tests, 58 fichiers</div>
<p class="feature-desc">Couverture de test complete sur les 17 langues. Chaque interface est verifiee de bout en bout : lexer → parser → semantique → generation de code → execution.</p>
</div>

<div class="feature-card">
<span class="feature-icon">📝</span>
<div class="feature-title">REPL interactif</div>
<p class="feature-desc">REPL avec changement de langue et apercu Python. Basculez entre les 17 langues au cours d'une meme session. Inspectez le Python genere, les mots-cles et les operateurs.</p>
</div>

<div class="feature-card">
<span class="feature-icon">🔤</span>
<div class="feature-title">Normalisation de surface</div>
<p class="feature-desc">Les langues SOV et RTL comme le japonais, l'arabe, le hindi, le bengali et le tamoul prennent en charge l'ordre de mots naturel via des regles declaratives.</p>
</div>

<div class="feature-card">
<span class="feature-icon">🔢</span>
<div class="feature-title">Numeraux multilingues</div>
<p class="feature-desc">Prise en charge des numeraux Unicode, des chiffres romains, des nombres complexes, des fractions et de la notation scientifique dans plusieurs systemes d'ecriture.</p>
</div>

</div>
</section>

<section class="home-section" markdown="1">
  <span class="section-eyebrow">Langues prises en charge</span>
  <h2 class="section-title">Interfaces linguistiques mises en avant</h2>
  <p class="section-desc">Chaque langue est une interface complete avec mots-cles localises, messages d'erreur, fonctions integrees et support REPL.</p>

<div class="lang-grid">
  <a href="{{ '/fr/docs/guide-langage/toutes-langues/#english' | relative_url }}" class="lang-pill">
    Anglais <span class="lang-code">en</span>
  </a>
  <a href="{{ '/fr/docs/guide-langage/toutes-langues/#french' | relative_url }}" class="lang-pill">
    Francais <span class="lang-code">fr</span>
  </a>
  <a href="{{ '/fr/docs/guide-langage/toutes-langues/#spanish' | relative_url }}" class="lang-pill">
    Espagnol <span class="lang-code">es</span>
  </a>
  <a href="{{ '/fr/docs/guide-langage/toutes-langues/#japanese' | relative_url }}" class="lang-pill">
    Japonais <span class="lang-code">ja</span>
  </a>
  <a href="{{ '/fr/docs/guide-langage/toutes-langues/#arabic' | relative_url }}" class="lang-pill">
    Arabe <span class="lang-code">ar</span>
  </a>
  <a href="{{ '/fr/docs/guide-langage/toutes-langues/#hindi' | relative_url }}" class="lang-pill">
    Hindi <span class="lang-code">hi</span>
  </a>
</div>
</section>

<section class="home-section" markdown="1">
  <span class="section-eyebrow">Demarrage rapide</span>
  <h2 class="section-title">Lancez-vous en 60 secondes</h2>

**Installation :**

```bash
# Minimal (backend Python seulement)
pip install multilingualprogramming

# Recommande (Python + acceleration WASM)
pip install multilingualprogramming[wasm]

# Performance maximale (Python + WASM + NumPy)
pip install multilingualprogramming[performance]
```

**Lancer le REPL :**

```bash
# Par defaut (anglais)
python -m multilingualprogramming repl

# Francais
python -m multilingualprogramming repl --lang fr

# Japonais
python -m multilingualprogramming repl --lang ja

# Avec apercu Python
python -m multilingualprogramming repl --show-python
```

**Executer un fichier :**

```bash
python -m multilingualprogramming run myprogram.ml --lang en
python -m multilingualprogramming run programme.ml --lang fr
```

**Utiliser comme bibliotheque :**

```python
from multilingualprogramming import ProgramExecutor

executor = ProgramExecutor()
executor.execute("""
soit x = 10
soit y = 20
afficher(x + y)
""", language="fr")
```

</section>

<section class="home-section" markdown="1">
  <span class="section-eyebrow">Architecture</span>
  <h2 class="section-title">Pipeline de compilation</h2>
  <p class="section-desc">Chaque programme, dans n'importe quelle langue, suit le meme pipeline vers une sortie Python ou WASM.</p>

```
Langage de surface (fichier .ml)
        |
        v
  +---------------+
  |     Lexer     |  Tokenisation Unicode, resolution des concepts de mots-cles
  +------+--------+
         | Jetons conceptuels (COND_IF, LOOP_FOR, FUNC_DEF...)
         v
  +-------------------+
  | Normalisation     |  Optionnelle : reecrit l'ordre SOV/RTL vers une forme canonique
  | de surface        |
  +------+------------+
         |
         v
  +---------------+
  |    Parser     |  Construit un AST central independant de la langue
  +------+--------+
         |
         v
  +-------------------+
  |  Enveloppe CoreIR |  CoreIRProgram (conteneur type avec metadonnees)
  +------+------------+
         |
         v
  +-------------------+
  | Analyse semantique|  Portee, symboles, verification structurelle
  +------+------------+
         |
    +----+----+
    |         |
    v         v
+--------+ +---------+
|Python  | |   WAT   |  Cibles de generation de code
|  Gen   | |   Gen   |
+---+----+ +----+----+
    |           |
    v           v
+--------+ +-----------+
|Python  | | wasmtime  |
|Runtime | | (-> .wasm)|
+--------+ +-----------+
```

<div style="margin-top:1.5rem">
  <a href="{{ '/fr/docs/conception/' | relative_url }}" class="btn btn-secondary">Lire la documentation d'architecture &rarr;</a>
</div>
</section>
