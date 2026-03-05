---
page_id: language_guide__all_languages
locale: fr
title: Toutes les langues
path_segments:
- guide-langage
- toutes-langues
source_hash: 897bd24154cc
status: translated
---



Cette page fournit des exemples de programmes complets pour les 17 langues supportees, avec variables, controle de flux, fonctions et classes. Chaque exemple est executable tel quel.

Tous les programmes produisent la meme sortie quelle que soit la langue utilisee.

---

## Anglais (`en`) {#english}

{{snippet:language_guide__all_languages__py01}}

**Execution :**
```bash
python -m multilingualprogramming run program.ml --lang en
```

---

## Francais (`fr`) {#french}

{{snippet:language_guide__all_languages__py02}}

**Execution :**
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

## Italian (`it`) {#italian}

{{snippet:language_guide__all_languages__py05}}

---

## Portuguese (`pt`) {#portuguese}

{{snippet:language_guide__all_languages__py06}}

---

## Polish (`pl`) {#polish}

{{snippet:language_guide__all_languages__py07}}

---

## Dutch (`nl`) {#dutch}

{{snippet:language_guide__all_languages__py08}}

---

## Swedish (`sv`) {#swedish}

{{snippet:language_guide__all_languages__py09}}

---

## Danish (`da`) {#danish}

{{snippet:language_guide__all_languages__py10}}

---

## Finnish (`fi`) {#finnish}

{{snippet:language_guide__all_languages__py11}}

---

## Hindi (`hi`) {#hindi}

{{snippet:language_guide__all_languages__py12}}

**Execution :**
```bash
python -m multilingualprogramming run program.ml --lang hi
```

---

## Arabe (`ar`) {#arabic}

{{snippet:language_guide__all_languages__py13}}

**Execution :**
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

## Chinese Simplified (`zh`) {#chinese}

{{snippet:language_guide__all_languages__py16}}

**Execution :**
```bash
python -m multilingualprogramming run program.ml --lang zh
```

---

## Japonais (`ja`) {#japanese}

{{snippet:language_guide__all_languages__py17}}

**Execution :**
```bash
python -m multilingualprogramming run program.ml --lang ja
```

---

## Surface Normalization (SOV/RTL Languages)

Pour des langues comme le japonais, l'arabe, l'hindi, le bengali et le tamoul, l'ordre naturel des mots differe de la grammaire positionnelle par defaut. Le normaliseur de surface reecrit ces formes avant le parsing.

### Japonais — for loop (iterable-first)

Natural form (accepted):
{{snippet:language_guide__all_languages__py18}}

Canonical form (also accepted):
{{snippet:language_guide__all_languages__py19}}

Both compile to the same Core AST.

### Arabe — for loop

Natural form:
{{snippet:language_guide__all_languages__py20}}

### Execution de tous les exemples

```bash
# Validate all 17 languages
python -m multilingualprogramming smoke --all

# Executer le smoke test d'une langue specifique
python -m multilingualprogramming smoke --lang fr
```
