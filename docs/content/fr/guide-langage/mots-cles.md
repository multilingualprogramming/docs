---
page_id: language_guide__keywords
locale: fr
title: Mots-clés
path_segments:
- guide-langage
- mots-cles
source_hash: 98cc9a927f70
status: translated
permalink: /fr/docs/guide-langage/mots-cles/
---

Tous les mots-clés de `multilingual` se mappent vers des **concepts sémantiques**, et non vers des tokens bruts. Le lexer relie les mots-clés de surface propres à chaque langue à ces concepts ; le parseur et la génération de code opèrent ensuite uniquement sur les concepts.

---

## Système de concepts

Un concept comme `COND_IF` se mappe vers `if` en anglais, `si` en français, `wenn` en allemand, etc. Cette séparation garde le parseur et l'analyseur sémantique indépendants de la langue.

Le registre des mots-clés est stocké dans :
`multilingualprogramming/resources/usm/keywords.json`

---

## Contrôle de flux

| Concept | Anglais | Français |
|---------|---------|-----------|
| `COND_IF` | `if` | `si` |
| `COND_ELIF` | `elif` | `sinon_si` |
| `COND_ELSE` | `else` | `sinon` |
| `LOOP_FOR` | `for` | `pour` |
| `IN` | `in` | `dans` |
| `LOOP_WHILE` | `while` | `tant_que` |
| `BREAK` | `break` | `break` |
| `CONTINUE` | `continue` | `continue` |
| `PASS` | `pass` | `pass` |

---

## Déclaration de variables

| Concept | Anglais | Français |
|---------|---------|-----------|
| `LET` | `let` | `soit` |
| `CONST` | `const` | `constante` |
| `GLOBAL` | `global` | `mondial` |
| `NONLOCAL` | `nonlocal` | `nonlocal` |
| `DEL` | `del` | `supprimer` |
| `ASSERT` | `assert` | `affirmer` |

---

## Fonctions et classes

| Concept | Anglais | Français |
|---------|---------|-----------|
| `FUNC_DEF` | `def` | `fonction` |
| `RETURN` | `return` | `retourner` |
| `CLASS_DEF` | `class` | `classe` |
| `LAMBDA` | `lambda` | `lambda` |
| `YIELD` | `yield` | `produire` |
| `YIELD_FROM` | `yield from` | `produire_de` |

---

## Exceptions et contextes

| Concept | Anglais | Français |
|---------|---------|-----------|
| `TRY` | `try` | `essayer` |
| `EXCEPT` | `except` | `sauf` |
| `FINALLY` | `finally` | `finalement` |
| `RAISE` | `raise` | `soulever` |
| `WITH` | `with` | `avec` |
| `AS` | `as` | `comme` |

---

## Asynchrone et imports

| Concept | Anglais | Français |
|---------|---------|-----------|
| `ASYNC` | `async` | `async` |
| `AWAIT` | `await` | `attendre` |
| `IMPORT` | `import` | `importer` |
| `FROM` | `from` | `de` |

---

## Mots-clés d'import

{{snippet:language_guide__keywords__py01}}

---

## Alias des fonctions intégrées

Les noms anglais universels des fonctions intégrées restent toujours valides. Chaque langue peut ajouter des alias localisés en complément.

| Concept | Anglais | Français |
|---------|---------|-----------|
| `print` | `print` | `afficher` |
| `range` | `range` | `intervalle` |
| `len` | `len` | `longueur` |
| `sum` | `sum` | `somme` |
| `abs` | `abs` | `valeur_abs` |
| `sorted` | `sorted` | `trie` |
| `input` | `input` | `saisie` |
| `open` | `open` | `ouvrir` |

Voir la page [Fonctions intégrées](/fr/docs/references/fonctions-integrees/) pour plus de détails.
