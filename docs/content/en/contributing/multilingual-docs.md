---
page_id: contributing__multilingual_docs
locale: en
title: Multilingual Documentation Operations
path_segments:
- contributing
- multilingual-docs
source_hash: 4f17f1104cac
status: source
permalink: /en/docs/contributing/multilingual-docs/
---

This repository keeps documentation authoring in Markdown while adding a strict EN/FR metadata layer for routing, snippet parity, and deployment safety.

---

## Goals

- Keep docs easy for humans to edit in plain Markdown.
- Support translated URLs including translated subdirectory segments.
- Ensure `Try it` and `RUN` get explicit language context.
- Block deploy when multilingual docs integrity checks fail.

---

## Directory Blueprint

```text
docs/
  content/
    en/
      getting-started/
      language-guide/
      reference/
    fr/
      demarrage/
      guide-langage/
      references/
  routing/
    en.routes.yml
    fr.routes.yml
  i18n/
    en/ui.yml
    fr/ui.yml
  snippets/
    <snippet_id>/
      en.code
      fr.code
```

Notes:

- `docs/content/*` is the Markdown source for multilingual routing metadata.
- Existing top-level docs pages remain unchanged and continue to build the public site.
- `docs/` is excluded from Jekyll output so metadata files never break Pages rendering.

---

## Front Matter Contract

Each multilingual page must include:

```yaml
---
page_id: getting_started
locale: en
title: Getting Started
path_segments:
  - getting-started
source_hash: 9f2a1c
status: source
---
```

French page uses the same `page_id` and translated `path_segments`:

```yaml
---
page_id: getting_started
locale: fr
title: Prise en main
path_segments:
  - demarrage
source_hash: 9f2a1c
status: translated
---
```

Rules:

- `page_id` is immutable and shared across locales.
- `path_segments` are locale-specific and can translate subdirectory names.
- `source_hash` is copied from the English source version and used for freshness checks.

---

## Routing Contract

- Canonical mapping key: `locale + page_id`.
- Public path source: `path_segments`.
- Route manifests (`docs/routing/*.routes.yml`) must map each `page_id` to its localized path.
- Language switchers must map by `page_id`, never by slug text.

---

## Snippet Contract

- Runnable examples are referenced by token in Markdown: `{{snippet:hello_world}}`.
- For each referenced snippet ID:
  - `docs/snippets/<id>/en.code` must exist.
  - `docs/snippets/<id>/fr.code` must exist.
- Inline runnable Python blocks are disallowed in `docs/content`; CI enforces snippet-token usage.

This prevents drift between localized runnable examples.

---

## CI and Deploy

`docs-ci.yml` validates:

- metadata schema and locale parity
- route uniqueness and route manifest consistency
- snippet parity
- stale translation reporting (`source_hash`)
- Jekyll build + Pages sanity checks

`docs-deploy-pages.yml` runs after successful CI on `main`:

- rebuilds in a clean environment
- performs sanity checks
- deploys with GitHub Pages actions

---

## Contributor Checklist

1. Update English page in `docs/content/en/...`.
2. Copy/update `source_hash`.
3. Update French counterpart in `docs/content/fr/...`.
4. Ensure EN/FR route manifest entries exist.
5. Ensure snippet variants exist for both locales.
6. Run `python scripts/validate_multilingual_docs.py --strict-freshness`.
7. Verify CI checks pass before merge.
