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

Le guide du langage couvre les 17 langues humaines supportées et l'ensemble des constructions disponibles pour écrire des programmes multilingual.

---

## Fonctionnement des langues

Chaque langue prise en charge constitue un **frontend** vers le même cœur sémantique. Le compilateur :

1. **Tokenise** la source avec un lexer Unicode et relie les mots-clés aux concepts sémantiques
2. **Normalise** les formes de surface (gère l'ordre SOV / RTL pour le japonais, l'arabe, etc.)
3. **Parse** les tokens de concepts vers un Core AST indépendant de la langue
4. **Analyse** les portées, symboles et contraintes structurelles
5. **Génère** du code Python ou WASM

Un même programme, dans n'importe quelle langue, produit un comportement identique.

---

## Catégories de langues

### Langues européennes (ordre SVO)

| Langue | Code | Écriture |
|----------|------|--------|
| Anglais | `en` | Latin |
| Français | `fr` | Latin |
| Espagnol | `es` | Latin |
| Allemand | `de` | Latin |
| Italien | `it` | Latin |
| Portugais | `pt` | Latin |
| Polonais | `pl` | Latin |
| Néerlandais | `nl` | Latin |
| Suédois | `sv` | Latin |
| Danois | `da` | Latin |
| Finnois | `fi` | Latin |

### Langues d'Asie du Sud

| Langue | Code | Écriture | Ordre des mots |
|----------|------|--------|------------|
| Hindi | `hi` | Devanagari | SOV |
| Bengali | `bn` | Bengali | SOV |
| Tamoul | `ta` | Tamil | SOV |

### Moyen-Orient

| Langue | Code | Écriture | Direction |
|----------|------|--------|-----------|
| Arabe | `ar` | Arabe | RTL |

### Asie de l'Est

| Langue | Code | Écriture | Ordre des mots |
|----------|------|--------|------------|
| Chinois (simplifié) | `zh` | CJK | SVO |
| Japonais | `ja` | CJK + Kana | SOV |

---

## Sections de ce guide

<div class="card-grid">

<div class="card">
<a href="/fr/docs/guide-langage/syntaxe/">
<span class="card-icon">📐</span>
<h3>Référence de syntaxe</h3>
<p>Syntaxe complète pour les variables, le contrôle de flux, les fonctions, les classes, l'async, les exceptions et les compréhensions.</p>
</a>
</div>

<div class="card">
<a href="/fr/docs/guide-langage/mots-cles/">
<span class="card-icon">🔑</span>
<h3>Mots-clés</h3>
<p>Table complète des mots-clés : 51 concepts sémantiques sur 17 langues.</p>
</a>
</div>

<div class="card">
<a href="/fr/docs/guide-langage/controle-flux/">
<span class="card-icon">🔀</span>
<h3>Contrôle de flux</h3>
<p>`if` / `elif` / `else`, `for`, `while`, `match/case`, `break`, `continue`, avec exemples dans chaque langue.</p>
</a>
</div>

<div class="card">
<a href="/fr/docs/guide-langage/fonctions-classes/">
<span class="card-icon">🏗️</span>
<h3>Fonctions et classes</h3>
<p>`def`, `class`, décorateurs, héritage, générateurs et lambdas, dans leurs 17 formes linguistiques.</p>
</a>
</div>

<div class="card">
<a href="/fr/docs/guide-langage/asynchrone-generateurs/">
<span class="card-icon">⚙️</span>
<h3>Async et générateurs</h3>
<p>`async def`, `await`, `async for`, `async with`, `yield` et `yield from`.</p>
</a>
</div>

<div class="card">
<a href="/fr/docs/guide-langage/toutes-langues/">
<span class="card-icon">🌐</span>
<h3>Les 17 langues</h3>
<p>Exemples complets de programmes dans chaque langue supportée avec couverture fonctionnelle complète.</p>
</a>
</div>

</div>
