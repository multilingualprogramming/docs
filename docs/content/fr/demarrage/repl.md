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

> Le REPL multilingual (Read-Eval-Print Loop) est un environnement interactif avec changement de langue pour ecrire et tester des programmes dans l'une des 17 langues supportees.

---

## Demarrage du REPL

```bash
# Defaut (anglais)
python -m multilingualprogramming repl

# Demarrer dans une langue specifique
python -m multilingualprogramming repl --lang fr
python -m multilingualprogramming repl --lang ja
python -m multilingualprogramming repl --lang ar

# Avec apercu Python (afficher le Python genere avec la sortie)
python -m multilingualprogramming repl --show-python

# Avec apercu WAT (afficher le texte WebAssembly genere avec la sortie)
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
| `:python` | Activer/desactiver l'apercu Python (afficher le Python genere) |
| ` :wat` ou `:wasm` | Activer/desactiver l'apercu WAT (afficher le texte WebAssembly genere) |
| ` :rust` ou `:wasmtime` | Activer/desactiver le mode d'execution wasmtime (WASM au lieu de Python) |
| `:reset` | Reinitialiser l'etat de l'interpreteur (vider variables/fonctions) |
| `:kw` | Lister les mots-cles de la langue courante |
| `:kw XX` | Lister les mots-cles pour le code langue XX |
| `:ops` | Lister les operateurs de la langue courante |
| `:ops XX` | Lister les operateurs pour le code langue XX |
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

### Mode apercu Python

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

### Mode apercu WAT

Utilisez `:wat` (ou `:wasm`) pour activer/desactiver l'affichage du format texte WebAssembly compile avec chaque resultat :

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

Utilisez `:rust` (ou `:wasmtime`) pour basculer l'execution vers le backend wasmtime :

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

### Inspection des mots-cles

```
multilingual [fr]> :kw
Keywords for French (fr):
  if          → si
  elif        → sinonsi
  else        → sinon
  for         → pour
  in          → dans
  while       → tantque
  def         → déf
  return      → retourner
  let         → soit
  class       → classe
  ...

multilingual> :kw ar
Keywords for Arabic (ar):
  if      → إذا
  for     → لكل
  while   → بينما
  def     → دالة
  let     → ليكن
  ...
```

---

## Codes de langue

| Langue | Code | Mot-cle exemple |
|----------|------|----------------|
| Anglais | `en` | `if` |
| Francais | `fr` | `si` |
| Espagnol | `es` | `si` |
| Allemand | `de` | `wenn` |
| Italien | `it` | `se` |
| Portugais | `pt` | `se` |
| Polonais | `pl` | `jezeli` |
| Neerlandais | `nl` | `als` |
| Suedois | `sv` | `om` |
| Danois | `da` | `hvis` |
| Finnois | `fi` | `jos` |
| Hindi | `hi` | `अगर` |
| Arabic | `ar` | `إذا` |
| Bengali | `bn` | `যদি` |
| Tamil | `ta` | `என்றால்` |
| Chinois | `zh` | `如果` |
| Japonais | `ja` | `もし` |

---

## Smoke tests

Petits extraits de validation pour verifier qu'une langue fonctionne correctement.

### Snippet A — Variables and Print

```
<LET> x = 2
<LET> y = 3
<PRINT>(x + y)
```

Remplacez `<LET>` et `<PRINT>` par les mots-cles specifiques a la langue. Sortie attendue : `5`

### Snippet B — For Loop

```
<LET> total = 0
<FOR> i <IN> <RANGE>(4):
    total = total + i
<PRINT>(total)
```

Sortie attendue : `6`

**Anglais :**

{{snippet:getting_started__repl__py01}}

**Francais :**

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

- Saisie multi-ligne : continuez avec `...` pour les blocs (if, for, def, class)
- Les variables et fonctions definies dans une langue persistent apres `:language` (les identifiants restent, les mots-cles changent)
- `:reset` efface tout l'etat, y compris variables et definitions de fonctions
- Utilisez `:python` pour comprendre le code Python genere
- Utilisez `:wat` pour inspecter le format texte WebAssembly compile depuis votre code
- Utilisez `:wasmtime` pour executer via le backend WASM au lieu de Python
