# Multilingual Programming Language Documentation

Documentation website for **multilingual** (v0.4.0), a programming language that supports writing code in 17 human languages with one formal semantic core and Python/WASM backends.

Live site: https://multilingualprogramming.github.io/docs/
Main project: https://github.com/johnsamuelwrites/multilingual

## What is in this repo

This repository contains the Jekyll site source for the documentation portal, including:

- Getting Started guides
- Language Guide (syntax, keywords, control flow, async/generators)
- Reference docs (operators, numerals, builtins, datetime, compatibility)
- WASM backend docs (installation, architecture, performance, troubleshooting)
- Design and architecture documents
- Extension and contribution guides

## Documentation Structure

- `getting-started/`
- `language-guide/`
- `reference/`
- `wasm/`
- `codegen/`
- `design/`
- `extending/`
- `contributing/`
- `_layouts/`, `_includes/`, `assets/`

## Run Locally

Prerequisites:

- Ruby 3.x
- Bundler

Install dependencies:

```bash
bundle install
```

Start the site locally:

```bash
bundle exec jekyll serve
```

Open:

- http://127.0.0.1:4000/docs/

Build static output:

```bash
bundle exec jekyll build
```

## Content and Navigation

- Site configuration and navigation are defined in `_config.yml`.
- Homepage content is in `index.md`.
- Sidebar/navigation rendering uses templates in `_includes/` and `_layouts/`.

## Contributing to Docs

1. Edit or add markdown pages in the relevant section folder.
2. Update `_config.yml` navigation entries when adding new pages.
3. Run `bundle exec jekyll serve` and verify pages render correctly.
4. Submit a pull request.

For language/runtime contribution workflow, see `contributing/` and the [main repository](https://github.com/johnsamuelwrites/multilingual).

## License

Licensed under the terms in `LICENSE`.
