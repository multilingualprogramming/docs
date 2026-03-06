---
page_id: getting_started
locale: fr
title: Démarrage
path_segments:
- demarrage
source_hash: 9b9c8ca97172
status: translated
permalink: /fr/docs/demarrage/
---

## Qu'est-ce que `multilingual` ?

**multilingual** est un langage de programmation qui permet d'écrire des programmes avec des mots-clés issus de 17 langues humaines. Tous les frontends linguistiques compilent vers le même Core AST formel, puis vers Python ou WebAssembly.

Vous écrivez dans la langue de votre choix. Le compilateur produit ensuite un comportement identique, quelle que soit la langue utilisée.

**Principes clés :**

- **Un seul cœur sémantique** : les 17 langues se mappent au même Core AST
- **Compilation uniquement en avant** : `Langage de surface -> Core AST -> Python/WASM`
- **Mots-clés pilotés par concepts** : `COND_IF` se mappe vers `if`, `si`, `wenn`, `moshi`, etc.
- **Extensibilité guidée par les données** : les langues sont ajoutées via JSON, sans réécriture de grammaire
- **Runtime compatible Python** : sous-ensemble de Python 3.12+ avec accélération WASM optionnelle

---

## Prérequis

- **Python 3.12+**
- `pip`
- Optionnel : `wasmtime` pour le backend WASM

---

## Installation

### Minimal

```bash
pip install multilingualprogramming
```

### Recommandé

```bash
pip install multilingualprogramming[wasm]
```

### Performance maximale

```bash
pip install multilingualprogramming[performance]
```

---

## Vérifier l'installation

```bash
python -c "import multilingualprogramming; print('OK')"
```

Vérifier la disponibilité WASM :

{{snippet:getting_started__py01}}

---

## Votre premier programme

### Anglais

{{snippet:getting_started__py02}}

```bash
python -m multilingualprogramming run hello_en.ml --lang en
```

### Français

{{snippet:getting_started__py03}}

```bash
python -m multilingualprogramming run hello_fr.ml --lang fr
```

### Japonais

{{snippet:getting_started__py04}}

```bash
python -m multilingualprogramming run hello_ja.ml --lang ja
```

### Arabe

{{snippet:getting_started__py05}}

```bash
python -m multilingualprogramming run hello_ar.ml --lang ar
```

---

## Démarrer le REPL

```bash
python -m multilingualprogramming repl
python -m multilingualprogramming repl --lang fr
python -m multilingualprogramming repl --show-python
```

### Commandes REPL

| Commande | Description |
|---------|-------------|
| `:help` | Afficher les commandes |
| `:language <code>` | Changer de langue |
| `:python` | Activer ou désactiver l'aperçu Python |
| `:reset` | Réinitialiser l'état de l'interpréteur |
| `:kw [XX]` | Lister les mots-clés |
| `:ops [XX]` | Lister les opérateurs |
| `:q` | Quitter |

---

## Référence CLI

```bash
multilingual run <file.ml> --lang <code>
multilingual repl [--lang <code>] [--show-python]
multilingual smoke --lang <code>
multilingual smoke --all
multilingual --version
```

---

## Utilisation comme bibliothèque Python

{{snippet:getting_started__py06}}

---

## Étapes suivantes

{% capture next_installation_url %}{% include localized-url.html page_id='getting_started__installation' fallback_url='/fr/docs/demarrage/installation/' locale=page.locale %}{% endcapture %}
{% capture next_quick_start_url %}{% include localized-url.html page_id='getting_started__quick_start' fallback_url='/fr/docs/demarrage/demarrage-rapide/' locale=page.locale %}{% endcapture %}
{% capture next_language_guide_url %}{% include localized-url.html page_id='language_guide' fallback_url='/fr/docs/guide-langage/' locale=page.locale %}{% endcapture %}
{% capture next_wasm_url %}{% include localized-url.html page_id='wasm' fallback_url='/fr/docs/wasm/' locale=page.locale %}{% endcapture %}

<div class="card-grid">

<div class="card">
<a href="{{ next_installation_url | strip }}">
<span class="card-icon">📦</span>
<h3>Détails d'installation</h3>
<p>Configuration par plateforme, prérequis WASM et environnements virtuels.</p>
</a>
</div>

<div class="card">
<a href="{{ next_quick_start_url | strip }}">
<span class="card-icon">🚀</span>
<h3>Exemples de démarrage rapide</h3>
<p>Tour d'horizon des principales fonctionnalités du langage.</p>
</a>
</div>

<div class="card">
<a href="{{ next_language_guide_url | strip }}">
<span class="card-icon">📖</span>
<h3>Guide du langage</h3>
<p>Référence syntaxique complète pour les 17 langues.</p>
</a>
</div>

<div class="card">
<a href="{{ next_wasm_url | strip }}">
<span class="card-icon">⚡</span>
<h3>Backend WASM</h3>
<p>Accélération WebAssembly et stratégies de repli.</p>
</a>
</div>

</div>
