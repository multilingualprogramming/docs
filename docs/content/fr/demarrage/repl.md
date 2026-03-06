---
page_id: getting_started__repl
locale: fr
title: Guide REPL
path_segments:
- demarrage
- repl
source_hash: 4444b80aad58
status: translated
permalink: /fr/docs/demarrage/repl/
---

> Le REPL multilingual (Read-Eval-Print Loop) est un environnement interactif avec changement de langue pour écrire et tester des programmes dans l'une des 17 langues supportées.

---

## Démarrage du REPL

```bash
# Défaut (anglais)
python -m multilingualprogramming repl

# Démarrer dans une langue spécifique
python -m multilingualprogramming repl --lang fr
python -m multilingualprogramming repl --lang ja
python -m multilingualprogramming repl --lang ar

# Avec aperçu Python
python -m multilingualprogramming repl --show-python

# Avec aperçu WAT
python -m multilingualprogramming repl --show-wat

# Alias de commande court
multilg repl --lang de
```

---

## Commandes REPL

| Commande | Description |
|---------|-------------|
| `:help` | Afficher toutes les commandes REPL disponibles |
| `:language <code>` | Changer la langue active (ex. `:language fr`) |
| `:python` | Activer / désactiver l'aperçu Python |
| `:wat` ou `:wasm` | Activer / désactiver l'aperçu WAT |
| `:rust` ou `:wasmtime` | Activer / désactiver le mode d'exécution wasmtime |
| `:reset` | Réinitialiser l'état de l'interpréteur |
| `:kw` | Lister les mots-clés de la langue courante |
| `:kw XX` | Lister les mots-clés pour le code langue XX |
| `:ops` | Lister les opérateurs de la langue courante |
| `:ops XX` | Lister les opérateurs pour le code langue XX |
| `:q` | Quitter le REPL |

---

## Exemples de sessions

### Session anglaise

```
multilingual> let x = 10
multilingual> let y = 25
multilingual> print(x + y)
35
multilingual> def square(n):
...               return n * n
...
multilingual> print(square(7))
49
```

### Changement de langue

```
multilingual [en]> :language fr
Switched to: French (fr)
multilingual [fr]> soit a = 5
multilingual [fr]> soit b = 3
multilingual [fr]> afficher(a + b)
8
multilingual [fr]> :language ja
Switched to: Japanese (ja)
multilingual [ja]> 変数 値 = 42
multilingual [ja]> 表示(値)
42
```

### Mode aperçu Python

```
multilingual [en]> :python
Python preview: ON
multilingual [en]> let items = [1, 2, 3]
# Python: items = [1, 2, 3]
multilingual [en]> for i in items:
...                    print(i * 2)
# Python:
# for i in items:
#     print(i * 2)
2
4
6
```

### Mode aperçu WAT

Utilisez `:wat` (ou `:wasm`) pour activer / désactiver l'affichage du format texte WebAssembly compilé avec chaque résultat :

```
multilingual [en]> :wat
WAT preview: ON
multilingual [en]> let x = 42
; WAT:
; (func $__main
;   f64.const 42
;   local.set $x
; )
multilingual [en]> :wat
WAT preview: OFF
```

Utilisez `:rust` (ou `:wasmtime`) pour basculer l'exécution vers le backend wasmtime :

```
multilingual [en]> :wasmtime
Backend: wasmtime (WASM)
multilingual [en]> let x = 42
multilingual [en]> print(x)
42
multilingual [en]> :wasmtime
Backend: Python
```

---

### Inspection des mots-clés

```
multilingual [fr]> :kw
Keywords for French (fr):
  if          -> si
  elif        -> sinonsi
  else        -> sinon
  for         -> pour
  in          -> dans
  while       -> tantque
  def         -> déf
  return      -> retourner
  let         -> soit
  class       -> classe
  ...
```

---

## Codes de langue

| Langue | Code | Mot-clé exemple |
|----------|------|----------------|
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

## Smoke tests

Petits extraits de validation pour vérifier qu'une langue fonctionne correctement.

### Snippet A - Variables et affichage

```
<LET> x = 2
<LET> y = 3
<PRINT>(x + y)
```

Remplacez `<LET>` et `<PRINT>` par les mots-clés spécifiques à la langue. Sortie attendue : `5`

### Snippet B - Boucle `for`

```
<LET> total = 0
<FOR> i <IN> <RANGE>(4):
    total = total + i
<PRINT>(total)
```

Sortie attendue : `6`

**Anglais :**

{{snippet:getting_started__repl__py01}}

**Français :**

{{snippet:getting_started__repl__py02}}

**Allemand :**

{{snippet:getting_started__repl__py03}}

**Japonais :**

{{snippet:getting_started__repl__py04}}

**Arabe :**

{{snippet:getting_started__repl__py05}}

**Hindi :**

{{snippet:getting_started__repl__py06}}

---

## Conseils REPL

- Saisie multi-ligne : continuez avec `...` pour les blocs (`if`, `for`, `def`, `class`)
- Les variables et fonctions définies dans une langue persistent après `:language`
- `:reset` efface tout l'état, y compris les variables et les définitions de fonctions
- Utilisez `:python` pour comprendre le code Python généré
- Utilisez `:wat` pour inspecter le format texte WebAssembly compilé depuis votre code
- Utilisez `:wasmtime` pour exécuter via le backend WASM au lieu de Python
