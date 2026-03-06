---
page_id: language_guide__french
locale: fr
title: Guide français
path_segments:
- guide-langage
- francais
source_hash: 8aaca71d7f2f
status: translated
permalink: /fr/docs/guide-langage/francais/
---

Ce guide présente la programmation avec `multilingual` en français. Il couvre les capacités du langage, le flux d'exécution, des exemples pratiques et les principaux points d'extension.

---

## Objectif du projet

`multilingual` permet d'écrire du code dans plusieurs langues humaines tout en conservant un modèle sémantique unique.

Concrètement :

- vous écrivez les mots-clés dans votre langue, par exemple `soit`, `pour`, `dans`, `afficher`
- le compilateur les mappe vers des concepts universels
- le code est transpilé en Python puis exécuté

---

## Démarrage rapide

Les fichiers source utilisent l'extension `.ml`.

```bash
pip install multilingualprogramming
multilingual repl --lang fr
multilingual repl --lang fr --show-python
multilingual run bonjour.ml --lang fr
```

Exemple `bonjour.ml` :

```text
afficher("Bonjour le monde")
```

---

## Capacités principales

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

### Fonctions

```text
fonction carre(x):
    retourner x * x

afficher(carre(6))
```

### Collections et slicing

```text
soit valeurs = [10, 20, 30, 40]
afficher(valeurs[1:3])
afficher(valeurs[::-1])
```

### Compréhensions

```text
soit carres = [x * x pour x dans intervalle(6)]
afficher(carres)
```

---

## Classes et objets

```text
classe Compteur:
    fonction __init__(soi, depart):
        soi.valeur = depart

    fonction incrementer(soi):
        soi.valeur = soi.valeur + 1
        retourner soi.valeur

soit c = Compteur(10)
afficher(c.incrementer())
```

---

## Imports

```text
importer math
de math importer sqrt comme root_fn
afficher(root_fn(16))
```

---

## Gestion des exceptions

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

async_fonction telecharger(url: chaine) -> chaine:
    retourner f"contenu simulé pour {url}"

async_fonction lire(url: chaine) -> chaine:
    retourner attendre telecharger(url)

afficher(asyncio.run(lire("https://exemple.fr")))
```

---

## Opérateur morse

```text
soit resultat = (n := 10) + 5
afficher(n, resultat)
```

---

## Boucle `tant_que`

```text
soit compteur = 0
tant_que compteur < 5:
    compteur = compteur + 1
afficher(compteur)
```

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
soit extra = {"niveau": "avancé", "theme": "tests"}
soit profil = {**base, **extra}
afficher(profil)
```

---

## Alias français des fonctions intégrées

| Alias français | Nom universel |
|----------------|---------------|
| `afficher` | `print` |
| `intervalle` | `range` |
| `longueur` | `len` |
| `somme` | `sum` |
| `saisie` | `input` |
| `ouvrir` | `open` |
| `trie` | `sorted` |
| `inverse` | `reversed` |
| `enumerer` | `enumerate` |
| `combiner` | `zip` |
| `appliquer` | `map` |
| `filtrer` | `filter` |

Voir la [référence des fonctions intégrées]({{ '/fr/docs/references/fonctions-integrees/' | relative_url }}) pour la liste complète.

---

## Commandes REPL

| Commande | Description |
|----------|-------------|
| `:help` | Afficher l'aide |
| `:language fr` | Forcer la langue française |
| `:python` | Afficher ou masquer le Python généré |
| `:reset` | Réinitialiser la session |
| `:kw fr` | Lister les mots-clés français |
| `:ops fr` | Lister les opérateurs |
| `:q` | Quitter |

---

## Architecture technique

Le flux est identique pour toutes les langues :

```text
Source français (.ml)
      |
      v  Lexer
Tokens
      |
      v  Parser
AST surface
      |
      v  lower_to_core_ir()
CoreIRProgram
      |
      v  SemanticAnalyzer
AST validé
      |
      v  PythonCodeGenerator
Code Python
      |
      v  exec() avec RuntimeBuiltins
Résultat
```

Ce design permet d'ajouter des langues sans réécrire le parseur ni la génération de code.

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

---

## Bonnes pratiques

- utiliser un seul style lexical par fichier
- vérifier les mots-clés disponibles avec `:kw fr`
- activer `--show-python` pour le débogage
- écrire des tests de bout en bout avec `ProgramExecutor`

---

## API Python

{{snippet:language_guide__french__py01}}
