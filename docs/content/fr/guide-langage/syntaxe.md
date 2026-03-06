---
page_id: language_guide__syntax
locale: fr
title: Syntaxe
path_segments:
- guide-langage
- syntaxe
source_hash: 1a1df4d35040
status: translated
permalink: /fr/docs/guide-langage/syntaxe/
---

Cette page sert de référence syntaxique pour `multilingual`. Les mots-clés affichés sous la forme `[CONCEPT]` représentent des concepts sémantiques ; remplacez-les par le mot-clé approprié à la langue choisie.

Voir la [Référence des mots-clés]({{ '/fr/docs/guide-langage/mots-cles/' | relative_url }}) pour le mapping complet.

---

## Conventions de syntaxe

- `[LET]` : mot-clé de déclaration de variable (`let`, `soit`, `sei`, etc.)
- `[IF]` : condition
- `[FOR]` : boucle `for`
- `[DEF]` : définition de fonction
- `[CLASS]` : définition de classe
- `[RETURN]` : instruction de retour
- Les identifiants peuvent utiliser Unicode et ne sont pas traduits
- Les chaînes utilisent `"..."`, `'...'`, `"""..."""` ou `f"..."`

---

## Variables et déclarations

### Déclaration de variable

```text
[LET] identifier = expression
[LET] identifier: type = expression
```

Exemples :
{{snippet:language_guide__syntax__py01}}

### Constantes

```text
const IDENTIFIER = expression
```

{{snippet:language_guide__syntax__py02}}

### Affectation chaînée

```text
identifier = identifier = expression
[LET] a = [LET] b = expression
```

{{snippet:language_guide__syntax__py03}}

### Suppression

```text
del identifier
```

### Affectation augmentée

{{snippet:language_guide__syntax__py04}}

---

## Littéraux

### Nombres

{{snippet:language_guide__syntax__py05}}

### Chaînes

{{snippet:language_guide__syntax__py06}}

### Booléens et `None`

{{snippet:language_guide__syntax__py07}}

### Collections

{{snippet:language_guide__syntax__py08}}

---

## Expressions

### Arithmétique

{{snippet:language_guide__syntax__py09}}

### Comparaison

{{snippet:language_guide__syntax__py10}}

### Booléens

{{snippet:language_guide__syntax__py11}}

### Opérateurs bit à bit

{{snippet:language_guide__syntax__py12}}

### Slicing

{{snippet:language_guide__syntax__py13}}

### Opérateur morse

{{snippet:language_guide__syntax__py14}}

### Expression ternaire

```text
value_if_true [IF] condition [ELSE] value_if_false
```

{{snippet:language_guide__syntax__py15}}

### Dépaquetage

{{snippet:language_guide__syntax__py16}}

### Dépaquetage de dictionnaires et d'ensembles

{{snippet:language_guide__syntax__py17}}

### Lambda

```text
lambda params: expression
```

{{snippet:language_guide__syntax__py18}}

---

## Contrôle de flux

### `if` / `elif` / `else`

```text
[IF] condition:
    block
[ELIF] condition:
    block
[ELSE]:
    block
```

### Boucle `for`

```text
[FOR] target [IN] iterable:
    block
[ELSE]:
    block  # exécuté s'il n'y a pas de break
```

Cible tuple :
{{snippet:language_guide__syntax__py19}}

### Boucle `while`

```text
[LOOP_WHILE] condition:
    block
[ELSE]:
    block  # exécuté s'il n'y a pas de break
```

### `match` / `case`

```text
match expression:
    case pattern:
        block
    case pattern [IF] guard:
        block
    case pattern1 | pattern2:
        block
    case pattern [AS] name:
        block
    case _:
        block  # cas par défaut
```

### `break` / `continue` / `pass`

{{snippet:language_guide__syntax__py20}}

---

## Fonctions

### Définition simple

```text
[DEF] name(params):
    block
```

### Avec retour

```text
[DEF] name(params):
    [RETURN] expression
```

### Types de paramètres

{{snippet:language_guide__syntax__py21}}

### Valeurs par défaut

{{snippet:language_guide__syntax__py22}}

### Annotations de type

{{snippet:language_guide__syntax__py23}}

### Générateurs

```text
[DEF] name(params):
    [YIELD] expression
    [YIELD] [FROM] iterable
```

{{snippet:language_guide__syntax__py24}}

### Fonctions asynchrones

```text
[ASYNC] [DEF] name(params):
    [AWAIT] expression
    [ASYNC] [FOR] target [IN] iterable:
        block
    [ASYNC] [WITH] expression [AS] name:
        block
```

{{snippet:language_guide__syntax__py25}}

### Décorateurs

{{snippet:language_guide__syntax__py26}}

---

## Classes

### Classe simple

```text
[CLASS] Name:
    [DEF] __init__(self, params):
        self.attr = value

    [DEF] method(self):
        [RETURN] expression
```

### Héritage

```text
[CLASS] Child(Parent):
    [DEF] __init__(self, params):
        super(Child, self).__init__(params)
```

### Classe avec décorateurs

{{snippet:language_guide__syntax__py27}}

---

## Gestion des exceptions

### `try` / `except` / `else` / `finally`

```text
[TRY]:
    block
[EXCEPT] ExceptionType [AS] name:
    block
[EXCEPT] (Type1, Type2) [AS] name:
    block
[ELSE]:
    block
[FINALLY]:
    block
```

### `raise`

```text
[RAISE] ExceptionType("message")
[RAISE]
[RAISE] ExceptionA [FROM] ExceptionB
```

### `assert`

```text
[ASSERT] condition
[ASSERT] condition, "message"
```

---

## Gestionnaires de contexte

```text
[WITH] expression [AS] name:
    block

[WITH] expr1 [AS] n1, expr2 [AS] n2:
    block
```

{{snippet:language_guide__syntax__py28}}

---

## Compréhensions

### Compréhension de liste

{{snippet:language_guide__syntax__py29}}

### Compréhension de dictionnaire

{{snippet:language_guide__syntax__py30}}

### Compréhension d'ensemble

{{snippet:language_guide__syntax__py31}}

### Expression génératrice

{{snippet:language_guide__syntax__py32}}

---

## Imports

```text
[IMPORT] module
[FROM] module [IMPORT] name
[FROM] module [IMPORT] name [AS] alias
[FROM] module [IMPORT] *
```

{{snippet:language_guide__syntax__py33}}

---

## Portée : `global` et `nonlocal`

```text
[GLOBAL] identifier
[NONLOCAL] identifier
```

{{snippet:language_guide__syntax__py34}}

---

## Valeurs et opérateurs spéciaux

| Expression | Signification |
|-----------|---------------|
| `True` | Booléen vrai |
| `False` | Booléen faux |
| `None` | Valeur nulle |
| `Ellipsis` / `...` | Littéral d'ellipse |
| `NotImplemented` | Marqueur de non-implémentation |
| `is` | Test d'identité |
| `is not` | Négation d'identité |
| `in` | Test d'appartenance |
| `not in` | Négation d'appartenance |

---

## Types d'exceptions pris en charge

{{snippet:language_guide__syntax__py35}}
