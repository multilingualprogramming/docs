---
page_id: language_guide__all_languages
locale: en
title: All 17 Languages
path_segments:
- language-guide
- all-languages
source_hash: 897bd24154cc
status: source
---

This page provides complete program examples for all 17 supported languages, demonstrating variables, control flow, functions, and classes. Each example is a complete, runnable program.

All programs produce identical output regardless of language used.

---

## English (`en`) {#english}

{{snippet:language_guide__all_languages__py01}}

**Run:**
```bash
python -m multilingualprogramming run program.ml --lang en
```

---

## French (`fr`) {#french}

{{snippet:language_guide__all_languages__py02}}

**Run:**
```bash
python -m multilingualprogramming run programme.ml --lang fr
```

---

## Spanish (`es`) {#spanish}

{{snippet:language_guide__all_languages__py03}}

---

## German (`de`) {#german}

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

**Run:**
```bash
python -m multilingualprogramming run program.ml --lang hi
```

---

## Arabic (`ar`) {#arabic}

{{snippet:language_guide__all_languages__py13}}

**Run:**
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

**Run:**
```bash
python -m multilingualprogramming run program.ml --lang zh
```

---

## Japanese (`ja`) {#japanese}

{{snippet:language_guide__all_languages__py17}}

**Run:**
```bash
python -m multilingualprogramming run program.ml --lang ja
```

---

## Surface Normalization (SOV/RTL Languages)

For languages like Japanese, Arabic, Hindi, Bengali, and Tamil, natural word order differs from the default positional grammar. The surface normalizer rewrites natural forms before parsing.

### Japanese — for loop (iterable-first)

Natural form (accepted):
{{snippet:language_guide__all_languages__py18}}

Canonical form (also accepted):
{{snippet:language_guide__all_languages__py19}}

Both compile to the same Core AST.

### Arabic — for loop

Natural form:
{{snippet:language_guide__all_languages__py20}}

### Running All Examples

```bash
# Validate all 17 languages
python -m multilingualprogramming smoke --all

# Run specific language smoke test
python -m multilingualprogramming smoke --lang fr
```
