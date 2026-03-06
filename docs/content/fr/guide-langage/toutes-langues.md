---
page_id: language_guide__all_languages
locale: fr
title: Toutes les langues
path_segments:
- guide-langage
- toutes-langues
source_hash: 897bd24154cc
status: translated
permalink: /fr/docs/guide-langage/toutes-langues/
---

Cette page fournit des exemples de programmes complets pour les 17 langues prises en charge, avec variables, contrôle de flux, fonctions et classes. Chaque exemple est exécutable tel quel.

Tous les programmes produisent la même sortie quelle que soit la langue utilisée.

---

## Anglais (`en`) {#english}

{{snippet:language_guide__all_languages__py01}}

**Exécution :**
```bash
python -m multilingualprogramming run program.ml --lang en
```

---

## Français (`fr`) {#french}

{{snippet:language_guide__all_languages__py02}}

**Exécution :**
```bash
python -m multilingualprogramming run programme.ml --lang fr
```

---

## Espagnol (`es`) {#spanish}

{{snippet:language_guide__all_languages__py03}}

---

## Allemand (`de`) {#german}

{{snippet:language_guide__all_languages__py04}}

---

## Italien (`it`) {#italian}

{{snippet:language_guide__all_languages__py05}}

---

## Portugais (`pt`) {#portuguese}

{{snippet:language_guide__all_languages__py06}}

---

## Polonais (`pl`) {#polish}

{{snippet:language_guide__all_languages__py07}}

---

## Néerlandais (`nl`) {#dutch}

{{snippet:language_guide__all_languages__py08}}

---

## Suédois (`sv`) {#swedish}

{{snippet:language_guide__all_languages__py09}}

---

## Danois (`da`) {#danish}

{{snippet:language_guide__all_languages__py10}}

---

## Finnois (`fi`) {#finnish}

{{snippet:language_guide__all_languages__py11}}

---

## Hindi (`hi`) {#hindi}

{{snippet:language_guide__all_languages__py12}}

**Exécution :**
```bash
python -m multilingualprogramming run program.ml --lang hi
```

---

## Arabe (`ar`) {#arabic}

{{snippet:language_guide__all_languages__py13}}

**Exécution :**
```bash
python -m multilingualprogramming run program.ml --lang ar
```

---

## Bengali (`bn`) {#bengali}

{{snippet:language_guide__all_languages__py14}}

---

## Tamil (`ta`) {#tamil}

{{snippet:language_guide__all_languages__py15}}

---

## Chinois simplifié (`zh`) {#chinese}

{{snippet:language_guide__all_languages__py16}}

**Exécution :**
```bash
python -m multilingualprogramming run program.ml --lang zh
```

---

## Japonais (`ja`) {#japanese}

{{snippet:language_guide__all_languages__py17}}

**Exécution :**
```bash
python -m multilingualprogramming run program.ml --lang ja
```

---

## Normalisation de surface

Pour des langues comme le japonais, l'arabe, l'hindi, le bengali et le tamoul, l'ordre naturel des mots peut différer de la grammaire positionnelle par défaut. Le normaliseur de surface réécrit ces formes avant le parsing.

### Japonais : boucle `for`

Forme naturelle :
{{snippet:language_guide__all_languages__py18}}

Forme canonique :
{{snippet:language_guide__all_languages__py19}}

Les deux compilent vers le même Core AST.

### Arabe : boucle `for`

Forme naturelle :
{{snippet:language_guide__all_languages__py20}}

### Exécution de tous les exemples

```bash
python -m multilingualprogramming smoke --all
python -m multilingualprogramming smoke --lang fr
```
