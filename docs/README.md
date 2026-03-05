# Multilingual Docs Metadata (EN/FR)

This folder contains Markdown-first multilingual documentation metadata and assets.

- `content/`: localized Markdown pages with shared `page_id`.
- `routing/`: localized route manifests keyed by `page_id`.
- `i18n/`: localized UI labels used by documentation surfaces.
- `snippets/`: runnable code variants by snippet ID and language.
- `schemas/`: front matter schema reference.

The production site currently renders from top-level Jekyll pages. Files in this folder are validated by CI and intentionally excluded from Jekyll output.

To scaffold multilingual EN/FR metadata pages from existing section sources, use:

```bash
python scripts/bootstrap_multilingual_docs.py
```

To externalize runnable Python examples into snippet assets (`{{snippet:<id>}}`), use:

```bash
python scripts/externalize_runnable_snippets.py
```
