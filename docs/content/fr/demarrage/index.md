---
page_id: getting_started
locale: fr
title: Demarrage
path_segments:
- demarrage
source_hash: 9b9c8ca97172
status: translated
permalink: /fr/docs/demarrage/
---

## Qu'est-ce que multilingual ?

**multilingual** est un langage de programmation qui vous permet d'ecrire des programmes avec des mots-cles de 17 langues humaines differentes. Tous les frontends de langue compilent vers le meme Core AST formel, puis vers Python ou WebAssembly.

Vous ecrivez dans la langue de votre choix. Le compilateur produit un comportement identique quelle que soit la langue utilisee.

**Principes clefs :**

- **Un seul coeur semantique** - Les 17 langues se mappent au meme Core AST
- **Compilation uniquement en avant** - `Langage de surface -> Core AST -> Python/WASM`
- **Mots-cles pilotes par concepts** - `COND_IF` se mappe vers `if` / `si` / `wenn` / `moshi` etc.
- **Extensibilite guidee par les donnees** - Langues ajoutees via JSON, sans reecriture de grammaire
- **Runtime compatible Python** - Sous-ensemble de syntaxe Python 3.12+, acceleration WASM

---

## Prerequis

- **Python 3.12+** (requis)
- pip (fourni avec Python)
- Optionnel : wasmtime (backend WASM, acceleration 50-100x)

---

## Installation

### Minimal (backend Python)

```bash
pip install multilingualprogramming
```

Inclut la prise en charge complete des 17 langues avec execution Python. Sans acceleration WASM.

### Recommande (Python + WASM)

```bash
pip install multilingualprogramming[wasm]
```

Ajoute une acceleration WebAssembly optionnelle avec repli automatique vers Python.

### Performance maximale

```bash
pip install multilingualprogramming[performance]
```

Ajoute NumPy pour des replis numeriques optimises avec WASM.

---

## Verifier l'installation

```bash
python -c "import multilingualprogramming; print('OK')"
```

Verifier la disponibilite WASM :

{{snippet:getting_started__py01}}

---

## Votre premier programme

### Anglais

Creez un fichier `hello_en.ml` :

{{snippet:getting_started__py02}}

Execution :

```bash
python -m multilingualprogramming run hello_en.ml --lang en
```

### Francais

Creez `hello_fr.ml` :

{{snippet:getting_started__py03}}

Execution :

```bash
python -m multilingualprogramming run hello_fr.ml --lang fr
```

### Japonais

Creez `hello_ja.ml` :

{{snippet:getting_started__py04}}

Execution :

```bash
python -m multilingualprogramming run hello_ja.ml --lang ja
```

### Arabe

Creez `hello_ar.ml` :

{{snippet:getting_started__py05}}

Execution :

```bash
python -m multilingualprogramming run hello_ar.ml --lang ar
```

---

## Demarrer le REPL interactif

Le REPL permet de saisir des programmes de facon interactive et de changer de langue :

```bash
# Langue par defaut (anglais)
python -m multilingualprogramming repl

# Demarrer en francais
python -m multilingualprogramming repl --lang fr

# Afficher le Python genere avec la sortie
python -m multilingualprogramming repl --show-python
```

### Commandes REPL

| Commande | Description |
|---------|-------------|
| `:help` | Afficher toutes les commandes REPL |
| `:language <code>` | Changer de langue (ex. `:language fr`) |
| `:python` | Activer/desactiver l'apercu Python |
| `:reset` | Reinitialiser l'etat de l'interpreteur |
| `:kw [XX]` | Lister les mots-cles de la langue courante ou demandee |
| `:ops [XX]` | Lister les operateurs |
| `:q` | Quitter |

**Exemple de session REPL :**

```
> let x = 10
> let y = 20
> print(x + y)
30
> :language fr
Switched to: French (fr)
> soit z = x + y
> afficher(z)
30
> :q
```

---

## Reference CLI

La CLI est disponible via `multilingual` et `multilg` :

```bash
# Executer un fichier programme
multilingual run <file.ml> --lang <code>

# Demarrer le REPL
multilingual repl [--lang <code>] [--show-python]

# Smoke test a language
multilingual smoke --lang <code>
multilingual smoke --all

# Afficher la version
multilingual --version
```

---

## Utilisation comme bibliotheque Python

{{snippet:getting_started__py06}}

---

## Etapes suivantes

<div class="card-grid">

<div class="card">
<a href="/fr/docs/demarrage/installation/">
<span class="card-icon">📦</span>
<h3>Details d'installation</h3>
<p>Configuration par plateforme, prerequis WASM, environnements virtuels.</p>
</a>
</div>

<div class="card">
<a href="/fr/docs/demarrage/demarrage-rapide/">
<span class="card-icon">🚀</span>
<h3>Exemples de demarrage rapide</h3>
<p>Tour en 10 minutes des principales fonctionnalites du langage.</p>
</a>
</div>

<div class="card">
<a href="/fr/docs/guide-langage/">
<span class="card-icon">📖</span>
<h3>Guide du langage</h3>
<p>Reference syntaxique complete pour les 17 langues.</p>
</a>
</div>

<div class="card">
<a href="/wasm/">
<span class="card-icon">⚡</span>
<h3>Backend WASM</h3>
<p>50–100x performance with WebAssembly.</p>
</a>
</div>

</div>
