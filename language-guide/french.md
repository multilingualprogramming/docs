---
layout: page
title: "Guide de programmation (Français)"
description: "Guide complet de programmation multilingual en français."
category: "Language Guide"
permalink: /language-guide/french/
prev_page:
  title: "All 17 Languages"
  url: /language-guide/all-languages/
---

Ce guide présente la programmation avec `multilingual` en français. Il couvre les capacités du langage, le flux d'exécution, les exemples pratiques, et les points d'extension.

---

## Objectif du projet

`multilingual` permet d'écrire du code dans plusieurs langues humaines, tout en conservant un modèle sémantique unique.

Concrètement :

- vous écrivez des mots-clés dans votre langue (ex. `soit`, `pour`, `dans`, `afficher`) ;
- le compilateur interne les mappe vers des concepts universels ;
- le code est transpilé en Python puis exécuté.

---

## Démarrage rapide

Les fichiers source du langage utilisent l'extension `.ml` (par exemple `bonjour.ml`).

```bash
# Installation
pip install multilingualprogramming

# Lancer le REPL en français
multilingual repl --lang fr

# Afficher aussi le Python généré
multilingual repl --lang fr --show-python

# Exécuter un fichier source
multilingual run bonjour.ml --lang fr
```

Exemple `bonjour.ml` :

```text
afficher("Bonjour le monde")
```

---

## Capacités principales du langage

### Variables et affectation

```text
soit total = 0
soit nom = "Alice"
```

### Conditions

```text
si total > 0:
    afficher("positif")
sinon:
    afficher("nul ou négatif")
```

### Boucles

```text
soit somme = 0
pour i dans intervalle(5):
    somme = somme + i
afficher(somme)
```
Sortie : `10`

### Fonctions

```text
fonction carré(x):
    retourner x * x

afficher(carré(6))
```
Sortie : `36`

### Collections et slicing

```text
soit valeurs = [10, 20, 30, 40]
afficher(valeurs[1:3])
afficher(valeurs[::-1])
```
Sortie : `[20, 30]` puis `[40, 30, 20, 10]`

### Compréhensions

```text
soit carrés = [x * x pour x dans intervalle(6)]
afficher(carrés)
```
Sortie : `[0, 1, 4, 9, 16, 25]`

---

## Classes et objets

```text
classe Compteur:
    fonction __init__(soi, départ):
        soi.valeur = départ

    fonction incrémenter(soi):
        soi.valeur = soi.valeur + 1
        retourner soi.valeur

soit c = Compteur(10)
afficher(c.incrémenter())
```
Sortie : `11`

---

## Imports

```text
importer math
depuis math importer sqrt comme root_fn
afficher(root_fn(16))
```
Sortie : `4.0`

---

## Gestion d'exceptions

```text
essayer:
    soit racine = root_fn(16)
sauf Exception comme erreur:
    soit racine = 0
finalement:
    afficher(racine)
```

---

## Programmation asynchrone

```text
importer asyncio

async_fonction télécharger(url: chaine) -> chaine:
    retourner f"contenu simulé pour {url}"

async_fonction lire(url: chaine) -> chaine:
    retourner attendre télécharger(url)

afficher(asyncio.run(lire("https://exemple.fr")))
```
Sortie : `contenu simulé pour https://exemple.fr`

---

## Opérateur walrus (`:=`)

```text
soit résultat = (n := 10) + 5
afficher(n, résultat)
```
Sortie : `10 15`

---

## Boucle `tant_que`

```text
soit compteur = 0
tant_que compteur < 5:
    compteur = compteur + 1
afficher(compteur)
```
Sortie : `5`

---

## Logique booléenne

```text
soit drapeau_ok = Vrai et non Faux
affirmer drapeau_ok
afficher(drapeau_ok)
```

---

## Dépliage de dictionnaires

```text
soit base = {"langue": "fr", "niveau": "intermédiaire"}
soit extra = {"niveau": "avancé", "thème": "tests"}
soit profil = {**base, **extra}
afficher(profil)
```
Sortie : `{'langue': 'fr', 'niveau': 'avancé', 'thème': 'tests'}`

---

## Alias français des built-ins

Certains built-ins universels ont des alias localisés. Les noms universels Python restent utilisables en parallèle.

| Alias français | Built-in Python |
|----------------|-----------------|
| `afficher` | `print` |
| `intervalle` | `range` |
| `longueur` | `len` |
| `somme` | `sum` |
| `saisie` | `input` |
| `ouvrir` | `open` |
| `trie` | `sorted` |
| `inverse` | `reversed` |
| `énumérer` | `enumerate` |
| `combiner` | `zip` |
| `appliquer` | `map` |
| `filtrer` | `filter` |
| `type` | `type` |
| `liste` | `list` |
| `dico` | `dict` |
| `ensemble` | `set` |
| `tuple` | `tuple` |

Voir la [référence des alias built-in](/reference/builtins/) pour la liste complète.

---

## Commandes REPL

| Commande | Description |
|----------|-------------|
| `:help` | Afficher l'aide |
| `:language fr` | Forcer la langue française |
| `:python` | Activer/désactiver l'affichage du Python généré |
| `:reset` | Vider l'état de la session |
| `:kw fr` | Lister les mots-clés français |
| `:ops fr` | Lister les symboles et opérateurs |
| `:q` | Quitter |

---

## Architecture technique

Le flux est identique pour toutes les langues :

```
Source français (.ml)
      │
      ▼  Lexer (tokenisation Unicode)
Tokens
      │
      ▼  Parser
AST surface
      │
      ▼  lower_to_core_ir()
CoreIRProgram
      │
      ▼  SemanticAnalyzer
AST validé
      │
      ▼  PythonCodeGenerator
Code Python (str)
      │
      ▼  exec() avec RuntimeBuiltins
Résultat
```

Ce design permet d'ajouter des langues sans réécrire parser/codegen.

---

## Exemple complet

```text
soit base = [1, 2, 3, 4, 5]
soit pairs = [x pour x dans base si x % 2 == 0]

fonction moyenne(liste):
    retourner somme(liste) / longueur(liste)

si longueur(pairs) > 0:
    afficher("Pairs:", pairs)
    afficher("Moyenne:", moyenne(pairs))
sinon:
    afficher("Aucune valeur paire")
```

Sortie attendue :
```
Pairs: [2, 4]
Moyenne: 3.0
```

---

## Bonnes pratiques

- Utiliser un seul style lexical par fichier (français ou autre) pour garder le code lisible
- Vérifier les mots-clés disponibles via `:kw fr`
- Activer `--show-python` au débogage pour comprendre la transpilation
- Écrire des tests de bout en bout avec `ProgramExecutor` pour valider la sémantique

---

## API Python

```python
from multilingualprogramming import ProgramExecutor

executor = ProgramExecutor()

# Exécuter du code français
executor.execute("""
soit items = [1, 2, 3]
afficher(somme(items))
""", language="fr")

# Transpiler vers Python sans exécuter
python_code = executor.transpile("""
pour i dans intervalle(5):
    afficher(i)
""", language="fr")
print(python_code)
# for i in range(5):
#     print(i)
```
