---
page_id: reference
locale: fr
title: Référence technique
path_segments:
- references
source_hash: 7daaacafc108
status: translated
permalink: /fr/docs/references/
---

Cette section rassemble la référence technique de `multilingualprogramming` : API publiques, pipeline de compilation, commandes CLI et base de compatibilité Python.

---

## Vue d'ensemble du package

{{snippet:reference__py01}}

---

## `ProgramExecutor`

API de haut niveau pour exécuter des programmes `multilingual`.

{{snippet:reference__py02}}

**Exemples :**

{{snippet:reference__py03}}

---

## Composants du pipeline

### Lexer

{{snippet:reference__py04}}

Chaque `Token` contient :
- `type` : concept de token, par exemple `COND_IF`, `LOOP_FOR`, `IDENTIFIER` ou `NUMBER`
- `value` : valeur textuelle lue dans la source
- `line` : numéro de ligne, à partir de 1
- `column` : numéro de colonne, à partir de 1

{{snippet:reference__py05}}

### Parser

{{snippet:reference__py06}}

Le nœud AST `Program` contient une liste de nœuds `Statement`. Voir `multilingualprogramming/parser/ast_nodes.py` pour la hiérarchie complète.

{{snippet:reference__py07}}

### Analyse sémantique

{{snippet:reference__py08}}

### Génération de code Python

{{snippet:reference__py09}}

**Exemple complet de pipeline :**

{{snippet:reference__py10}}

---

## `KeywordRegistry`

{{snippet:reference__py11}}

**Catégories de concepts :**

| Catégorie | Exemples |
|-----------|----------|
| Contrôle de flux | `COND_IF`, `COND_ELIF`, `COND_ELSE`, `LOOP_FOR`, `LOOP_WHILE` |
| Déclarations | `LET`, `CONST`, `GLOBAL`, `NONLOCAL`, `DEL`, `ASSERT` |
| Fonctions | `FUNC_DEF`, `RETURN`, `LAMBDA`, `YIELD`, `YIELD_FROM`, `ASYNC`, `AWAIT` |
| Classes | `CLASS_DEF` |
| Opérateurs | `AND`, `OR`, `NOT`, `IS`, `IS_NOT`, `IN_OP`, `NOT_IN` |
| Exceptions et contexte | `TRY`, `EXCEPT`, `ELSE`, `FINALLY`, `RAISE`, `WITH`, `AS` |
| Spéciaux | `IMPORT`, `FROM`, `MATCH`, `CASE` |

---

## Système de numéraux

### `MPNumeral`

{{snippet:reference__py12}}

### `RomanNumeral`

{{snippet:reference__py13}}

### `UnicodeNumeral`

{{snippet:reference__py14}}

### `NumeralConverter`

{{snippet:reference__py15}}

---

## Date et heure

{{snippet:reference__py16}}

---

## REPL

{{snippet:reference__py17}}

---

## Commandes CLI

```bash
# Exécuter un programme
multilingual run <file.ml> --lang en
multilingual run programme.ml --lang fr

# Démarrer le REPL
multilingual repl
multilingual repl --lang fr --show-python --show-wat

# Transpiler vers Python
multilingual compile hello.ml --lang en

# Construire un bundle WASM
multilingual build-wasm-bundle hello.ml --lang en --out-dir ./dist

# Valider un pack de langue
multilingual smoke --lang fr
multilingual smoke --all

# Vérifier l'encodage du code généré
multilingual encoding-check-generated hello.ml --lang en

# Afficher la version
multilingual --version
```

---

## Base de compatibilité Python

**Sous-ensemble Python 3.12+ pris en charge :**

| Fonctionnalité | Statut |
|----------------|--------|
| Déclarations de variables et annotations | ✅ |
| Opérateurs arithmétiques, bit à bit et comparaisons | ✅ |
| Affectations augmentées | ✅ |
| Affectations chaînées | ✅ |
| Dépaquetage étoilé | ✅ |
| Listes, dictionnaires, ensembles et tuples | ✅ |
| F-strings et spécificateurs de format | ✅ |
| `if` / `elif` / `else` | ✅ |
| Boucles `while` / `for` avec `else` | ✅ |
| `break` / `continue` / `pass` | ✅ |
| `match` / `case` avec gardes | ✅ |
| Fonctions avec tous les types de paramètres | ✅ |
| Générateurs et `yield from` | ✅ |
| `async def` / `await` / `async for` / `async with` | ✅ |
| Classes, héritage et `super()` | ✅ |
| `try` / `except` / `else` / `finally` | ✅ |
| `raise` / `raise ... from` | ✅ |
| Gestionnaires de contexte | ✅ |
| Compréhensions et expressions génératrices | ✅ |
| `global` / `nonlocal` / `del` | ✅ |
| `import` / `from ... import` / `as` / `*` | ✅ |
| Alias localisés des fonctions intégrées | ✅ |
| Normalisation de surface pour les langues SOV / RTL | ✅ |

Cette base de compatibilité est couverte par environ 1 797 tests répartis sur 58 fichiers.

---

## Historique des versions

| Version | Points marquants |
|---------|------------------|
| `0.5.1` | Mise à jour de la documentation |
| `0.5.0` | Modèle objet WAT/WASM, héritage avec MRO C3, support de `super()`, correctifs d'analyse sémantique |
| `0.4.0` | Génération WAT/WASM, playground navigateur, backend WASM avec replis Python |
| `0.3.0` | Jalons initiaux du projet |
