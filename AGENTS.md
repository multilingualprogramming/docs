# AGENTS.md

Repository guidance for LLM agents working in `docs/`.

## Scope

- This repository contains the documentation site for the `multilingualprogramming` project.
- The public site is built with Jekyll from the top-level site files (`index.md`, `_layouts/`, `_includes/`, `assets/`, `_config.yml`).
- The structured multilingual source of truth lives under `docs/` and currently supports English (`en`) and French (`fr`).

## Primary Goal

Help users write, explain, or update programs for the `multilingualprogramming` language using the documentation in this repository.

For now, optimize for:

- English code and explanations
- French code and explanations
- EN/FR documentation parity when editing docs assets

## Source Of Truth

When answering language or API questions, prefer these locations in order:

1. `docs/content/en/` and `docs/content/fr/` for authored documentation
2. `docs/snippets/<snippet_id>/en.code` and `docs/snippets/<snippet_id>/fr.code` for runnable examples
3. `docs/routing/*.routes.yml` and `docs/i18n/*/ui.yml` for localized paths and UI labels
4. Top-level Jekyll pages only when you need to understand the published site shell

Do not invent syntax if the docs or snippets already show it.

## Programming Guidance

When a user asks for code in this language:

- Pick the requested locale. If unspecified, default to English unless the user writes in French.
- Keep one lexical style per file. Do not mix French and English keywords in the same example unless the user asks for comparison.
- Prefer examples that match documented syntax from the repo.
- For French examples, use documented forms such as `soit`, `afficher`, `si`, `sinon`, `pour`, `dans`, `fonction`, `retourner`, `classe`, `importer`.
- For English examples, use documented forms such as `let`, `print`, `if`, `else`, `for`, `in`, `function`, `return`, `class`, `import`.
- When helpful, provide parallel EN and FR versions of the same program.

## Docs Editing Rules

If you modify multilingual docs content:

- Keep `page_id` identical across locales.
- Keep `source_hash` synchronized from the English source to the French translation.
- Keep `path_segments` localized per language.
- Ensure every referenced `{{snippet:<id>}}` has both `en.code` and `fr.code`.
- Do not add inline runnable Python blocks inside `docs/content/`; use snippet tokens instead.

## Validation Commands

Run these when your changes touch docs structure, snippets, or CI:

```powershell
python scripts/validate_multilingual_docs.py --strict-freshness
python -m pytest _tests -q
bundle exec jekyll build
python scripts/check_pages_artifact.py --site-dir _site --base-path /docs
```

## CI Files

- `.github/workflows/docs-ci.yml` validates docs metadata, runs tests, and builds the site.
- `.github/workflows/docs-deploy-pages.yml` rebuilds and deploys the site to GitHub Pages after successful CI on `main`.

## Known Constraint

The `_tests/` suite exercises docs examples through the PyPI package `multilingualprogramming`.
Install it with `pip install multilingualprogramming`.
If that package is not installed in the current environment, those tests should be skipped rather than failing at import time.
