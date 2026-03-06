---
page_id: reference__compatibility
locale: fr
title: Compatibilité
path_segments:
- references
- compatibilite
source_hash: 5200c7a76a88
status: translated
permalink: /fr/docs/references/compatibilite/
---

Cette matrice décrit l'état actuel de compatibilité de `multilingual`. La source de vérité repose sur :

- `examples/complete_features_en.ml` et ses équivalents dans les 17 langues
- `tests/` (environ 1 797 tests répartis sur 58 fichiers de test)

**Runtime cible** : CPython 3.12.x

---

## Périmètre

`multilingual` prend en charge un large sous-ensemble de la syntaxe et du runtime alignés sur Python 3.12. Il ne s'agit **pas** d'une compatibilité totale avec tous les projets Python existants ni avec tous les écosystèmes tiers. Il s'agit d'un cadre de compilation vers l'avant : langage de surface -> Core AST -> Python.

---

## Langues prises en charge

17 langues naturelles avec mots-clés et messages d'erreur localisés :

| Langue | Code | Mot-clé `if` |
|----------|------|-------------|
| Anglais | `en` | `if` |
| Français | `fr` | `si` |
| Espagnol | `es` | `si` |
| Allemand | `de` | `wenn` |
| Italien | `it` | `se` |
| Portugais | `pt` | `se` |
| Polonais | `pl` | `jezeli` |
| Néerlandais | `nl` | `als` |
| Suédois | `sv` | `om` |
| Danois | `da` | `hvis` |
| Finnois | `fi` | `jos` |
| Hindi | `hi` | `अगर` |
| Arabe | `ar` | `إذا` |
| Bengali | `bn` | `যদি` |
| Tamoul | `ta` | `என்றால்` |
| Chinois | `zh` | `如果` |
| Japonais | `ja` | `もし` |

---

## Constructions cœur

| Domaine | Statut | Notes |
|------|--------|-------|
| Imports | ✅ | `import math`, `from math import sqrt as root_fn` |
| Imports génériques | ✅ | `from os import *` |
| Déclarations de variables | ✅ | `let x = 0`, `const PI = 3.14` |
| Annotations de type | ✅ | `let x: int = 0`, `def f(x: int) -> str:` |
| Arithmétique et expressions | ✅ | `+`, `-`, `*`, `/`, `//`, `%`, `**`, opérateurs binaires |
| Affectation augmentée | ✅ | `+=`, `-=`, `*=`, `/=`, `**=`, `//=`, `%=`, `&=`, `\|=`, `^=`, `<<=`, `>>=` |
| Affectation chaînée | ✅ | `a = b = c = 0` |
| Dépaquetage étoilé | ✅ | `a, *rest = [1, 2, 3]`, `first, *mid, last = items` |

---

## Structures de données

| Domaine | Statut | Notes |
|------|--------|-------|
| Listes | ✅ | littéraux, itération, indexation, tranches |
| Dictionnaires | ✅ | littéraux, compréhensions, dépaquetage (`**d`) |
| Ensembles | ✅ | littéraux, compréhensions |
| Tuples | ✅ | littéraux, dépaquetage |
| Chaînes | ✅ | guillemets simples, doubles, triples, f-strings |
| Spécificateurs de format f-string | ✅ | `f"{x:.2f}"`, `f"{x!r}"`, `f"{x!s}"`, `f"{x!a}"` |
| Littéraux hexadécimaux, octaux et binaires | ✅ | `0xFF`, `0o77`, `0b1010` |
| Notation scientifique | ✅ | `1.5e10` |

---

## Contrôle de flux

| Domaine | Statut | Notes |
|------|--------|-------|
| `if` / `elif` / `else` | ✅ | chaînes conditionnelles complètes |
| Boucles `while` | ✅ | `while condition:` |
| `while` / `else` | ✅ | bloc `else` lorsque la boucle se termine sans `break` |
| Boucles `for` | ✅ | `for item in items:`, cibles avec dépaquetage de tuple |
| `for` / `else` | ✅ | bloc `else` lorsque la boucle se termine sans `break` |
| `break` / `continue` | ✅ | contrôle de boucle |
| `pass` | ✅ | instruction vide |
| `match` / `case` | ✅ | filtrage structurel de motifs |
| Gardes `case` | ✅ | `case n if n > 0:` |
| Motifs `case` avec OU | ✅ | `case 1 \| 2 \| 3:` |
| Liaisons `case ... as` | ✅ | `case pattern as name:` |
| `case _` (par défaut) | ✅ | motif générique / cas par défaut |
| Expressions ternaires | ✅ | `x if cond else y` |

---

## Fonctions et classes

| Domaine | Statut | Notes |
|------|--------|-------|
| Définitions de fonctions | ✅ | `def f(x):`, avec valeurs par défaut, `*args`, `**kwargs` |
| Paramètres positionnels uniquement | ✅ | `def f(a, b, /, c):` |
| Paramètres nommés uniquement | ✅ | `def f(a, *, b):` |
| Annotations de retour | ✅ | `def f() -> int:` |
| Décorateurs | ✅ | `@decorator` sur fonctions et classes |
| Expressions lambda | ✅ | `lambda x: x + 1` |
| `yield` / `yield from` | ✅ | fonctions génératrices et délégation |
| `async def` / `await` | ✅ | fonctions asynchrones, `async for`, `async with` |
| Définitions de classes | ✅ | héritage, méthodes, attributs |
| Opérateur morse | ✅ | `(x := expr)` |

---

## Gestion des erreurs

| Domaine | Statut | Notes |
|------|--------|-------|
| `try` / `except` / `else` / `finally` | ✅ | gestion complète des exceptions |
| `raise` | ✅ | `raise`, `raise ValueError("msg")` |
| `raise` ... `from` | ✅ | chaînage d'exceptions |
| `assert` | ✅ | `assert expr`, `assert expr, msg` |

---

## Portée et variables

| Domaine | Statut | Notes |
|------|--------|-------|
| `global` | ✅ | déclare la portée globale |
| `nonlocal` | ✅ | déclare la portée englobante |
| `del` | ✅ | `del variable` |

---

## Compréhensions et générateurs

| Domaine | Statut | Notes |
|------|--------|-------|
| Compréhensions de listes | ✅ | `[x for x in items if cond]`, imbriquées |
| Compréhensions de dictionnaires | ✅ | `{k: v for k, v in items}` |
| Compréhensions d'ensembles | ✅ | `{x for x in items if cond}`, imbriquées |
| Expressions génératrices | ✅ | `(x for x in items)` |

---

## Gestionnaires de contexte

| Domaine | Statut | Notes |
|------|--------|-------|
| Instruction `with` | ✅ | `with open(f) as h:` |
| Contextes multiples | ✅ | `with A() as a, B() as b:` |
| `async with` | ✅ | gestionnaires de contexte asynchrones |

---

## Couverture des builtins

| Domaine | Statut | Notes |
|---------------|--------|-------|
| Mots-clés Python (3.12) | ✅ Complète | 51 identifiants de concepts, 7 catégories |
| Fonctions built-in universelles | ✅ 70+ disponibles | `len`, `range`, `abs`, `pow`, `divmod`, `complex`, `format`, `ascii`, `compile`, `eval`, `exec`, `globals`, `locals`, `issubclass`, `delattr`, `slice`, `aiter`, `anext`, etc. |
| Types d'exceptions | ✅ 45+ | `BaseException`, `ValueError`, `TypeError`, `KeyError`, `ModuleNotFoundError`, `ExceptionGroup`, `BaseExceptionGroup`, tous les warnings, etc. |
| Valeurs spéciales | ✅ | `True`, `False`, `None`, `Ellipsis`, `NotImplemented` |
| Alias built-in localisés | ✅ 41 concepts | 41 builtins avec alias dans les 16 langues non anglaises |
| Noms built-in Python canoniques | ✅ | Toujours utilisables dans toutes les langues |

---

## Normalisation de syntaxe de surface

Les langues SOV et RTL peuvent utiliser un ordre de mots naturel. Le normaliseur de surface réécrit les tokens dans un ordre canonique avant le parsing.

| Instruction | Langues avec normalisation | Exemple |
|-----------|------------------------------|---------|
| Boucle `for` | `ja`, `ar`, `es`, `pt`, `hi`, `bn`, `ta` | Iterable-first |
| Boucle `while` | `ja`, `ar`, `hi`, `bn`, `ta` | Condition-first |
| Instruction `if` | `ja`, `ar`, `hi`, `bn`, `ta` | Condition-first |
| Instruction `with` | `ja`, `ar`, `hi`, `bn`, `ta` | Expression-first |

---

## Couverture de tests

Environ 1 797 tests répartis sur 58 fichiers de test :

| Domaine | Fichiers | Description |
|-----------|-------|-------------|
| Numéraux et dates | 8 | Numéraux multilingues, Unicode, chiffres romains, complexes, fractions, date / heure |
| Lexer | 2 | Tokenisation et comportement du lexer |
| Parser | 5 | Expressions, instructions, structures composées, multilingue, erreurs |
| Analyse sémantique | 6 | Portées, constantes, contrôle de flux, définitions, erreurs multilingues, table des symboles |
| Génération de code | 4 | Expressions, instructions, structures composées, multilingue |
| Exécution | 4 | Basique, multilingue, transpilation, erreurs |
| Fonctionnalités critiques | 8 | Chaînes triple-quoted, slices, paramètres, tuples, compréhensions, décorateurs, f-strings |
| Couverture du langage et CLI | 8 | Affectation augmentée, appartenance, ternaire, assert, affectation chaînée, CLI, REPL |
| Fonctionnalités avancées | 23 | `loop else`, `yield from`, `raise from`, compréhensions d'ensembles, séparateurs de paramètres, formatage f-string, gardes `match`, `global`, `nonlocal`, builtins, exceptions, normalisation de surface, alias, dépaquetage étoilé, intégration |
| Backend WAT / WASM | 5 | Génération WAT, POO / héritage en WAT, exécution WASM, projets corpus |
| Infrastructure | 10 | Registre des mots-clés, nœuds AST, AST printer, messages d'erreur, builtins runtime, REPL |

---

## Non garanti

Les points suivants **ne sont pas** annoncés comme universellement compatibles :

- Tous les projets Python inchangés
- Une parité comportementale complète avec tous les cas limites de CPython
- Une compatibilité complète avec tous les écosystèmes tiers
- Tous les scénarios avancés de métaprogrammation / introspection
- Des alias localisés pour l'intégralité des builtins CPython
- Le dépaquetage étoilé dans certains contextes d'expressions très imbriqués
- Certaines chaînes complexes de décorateurs avec arguments

---

## Correctifs connus (v0.5.x)

| Version | Correctif |
|---------|-----|
| v0.5.1 | Mises à jour de documentation |
| v0.5.0 | Modèle objet POO WAT / WASM : abaissement des classes avec allocateur linéaire, héritage avec MRO C3, résolution de `super()`, tests d'exécution WAT |
| v0.5.0 | `SemanticAnalyzer` gère correctement les affectations simples (`x = 5`) dans la portée |
| v0.5.0 | L'affectation augmentée (`x += 1`) signale correctement `UNDEFINED_NAME` si la variable n'a pas été définie auparavant |

---

## Recommandation

Pour évaluer la compatibilité sur un vrai code :

1. Partir de cette matrice
2. Exécuter les smoke tests : `multilingual smoke --all`
3. Exécuter des tests ciblés : `multilingual run yourprogram.ml --lang en`
4. Suivre les écarts comme des éléments concrets de syntaxe ou de runtime
