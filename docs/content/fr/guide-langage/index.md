---
page_id: language_guide
locale: fr
title: Guide du langage
path_segments:
- guide-langage
source_hash: f82e154d80f9
status: translated
permalink: /fr/docs/guide-langage/
---



Le guide du langage couvre les 17 langues humaines supportees et l'ensemble des constructions disponibles pour ecrire des programmes multilingual.

---

## Fonctionnement des langues

Chaque langue supportee est un **frontend** sur le meme coeur semantique. Le compilateur :

1. **Tokenise** la source avec un lexer Unicode et relie les mots-cles aux concepts semantiques
2. **Normalise** les formes de surface (gere l'ordre SOV/RTL pour le japonais, l'arabe, etc.)
3. **Parse** les tokens de concepts vers un Core AST independant de la langue
4. **Analyse** les portees, symboles et contraintes structurelles
5. **Genere** du code Python ou WASM

Un meme programme - dans n'importe quelle langue - produit un comportement identique.

---

## Categories de langues

### Langues europeennes (ordre SVO)

| Langue | Code | Ecriture |
|----------|------|--------|
| Anglais | `en` | Latin |
| Francais | `fr` | Latin |
| Espagnol | `es` | Latin |
| Allemand | `de` | Latin |
| Italien | `it` | Latin |
| Portugais | `pt` | Latin |
| Polonais | `pl` | Latin |
| Neerlandais | `nl` | Latin |
| Suedois | `sv` | Latin |
| Danois | `da` | Latin |
| Finnois | `fi` | Latin |

### Langues d'Asie du Sud

| Langue | Code | Ecriture | Word order |
|----------|------|--------|------------|
| Hindi | `hi` | Devanagari | SOV |
| Bengali | `bn` | Bengali | SOV |
| Tamil | `ta` | Tamil | SOV |

### Moyen-Orient

| Langue | Code | Ecriture | Direction |
|----------|------|--------|-----------|
| Arabe | `ar` | Arabe | RTL |

### Asie de l'Est

| Langue | Code | Ecriture | Word order |
|----------|------|--------|------------|
| Chinois (simplifie) | `zh` | CJK | SVO |
| Japonais | `ja` | CJK + Kana | SOV |

---

## Sections de ce guide

<div class="card-grid">

<div class="card">
<a href="/fr/docs/guide-langage/syntaxe/">
<span class="card-icon">📐</span>
<h3>Reference de syntaxe</h3>
<p>Syntaxe complete pour toutes les constructions : variables, controle de flux, fonctions, classes, async, exceptions, comprehensions.</p>
</a>
</div>

<div class="card">
<a href="/fr/docs/guide-langage/mots-cles/">
<span class="card-icon">🔑</span>
<h3>Mots-cles</h3>
<p>Table complete des mots-cles : 51 concepts semantiques sur 17 langues.</p>
</a>
</div>

<div class="card">
<a href="/fr/docs/guide-langage/controle-flux/">
<span class="card-icon">🔀</span>
<h3>Controle de flux</h3>
<p>if/elif/else, for, while, match/case, break, continue avec exemples dans chaque langue.</p>
</a>
</div>

<div class="card">
<a href="/fr/docs/guide-langage/fonctions-classes/">
<span class="card-icon">🏗️</span>
<h3>Fonctions et classes</h3>
<p>def, class, decorators, inheritance, generators, lambdas — with all 17 language forms.</p>
</a>
</div>

<div class="card">
<a href="/fr/docs/guide-langage/asynchrone-generateurs/">
<span class="card-icon">⚙️</span>
<h3>Async et generateurs</h3>
<p>async def, await, async for, async with, yield, yield from.</p>
</a>
</div>

<div class="card">
<a href="/fr/docs/guide-langage/toutes-langues/">
<span class="card-icon">🌐</span>
<h3>Les 17 langues</h3>
<p>Exemples complets de programmes dans chaque langue supportee avec couverture fonctionnelle complete.</p>
</a>
</div>

</div>
