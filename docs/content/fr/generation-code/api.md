---
page_id: codegen__api
locale: fr
title: Reference de l'API de generation de code
path_segments:
- generation-code
- api
source_hash: 66021f3a6bbf
status: translated
permalink: /fr/docs/generation-code/api/
---

Cette page documente l'API actuelle `0.5.1` de transpilation, d'execution et de generation WAT/WASM.

---

## Imports

{{snippet:codegen__api__py01}}

---

## ProgramExecutor

Point d'entree haut niveau pour tout le pipeline.

{{snippet:codegen__api__py02}}

### Methodes

#### `execute(source, capture_output=True, globals_dict=None) -> ExecutionResult`

Execute le lexing, le parsing, l'abaissement Core IR, l'analyse semantique optionnelle, la generation Python, puis `exec()`.

Le resultat expose:
- `output`
- `python_source`
- `errors`
- `success`
- `return_value`

{{snippet:codegen__api__py03}}

#### `transpile(source) -> str`

Genere le Python sans l'executer:

{{snippet:codegen__api__py04}}

#### Transpilation multilingue

Toutes les variantes linguistiques convergent vers le meme pipeline interne:

{{snippet:codegen__api__py05}}

---

## Lexer

Le lexer prend le texte source et, en option, un indice de langue.

{{snippet:codegen__api__py06}}

### Methodes

#### `tokenize() -> list[Token]`

{{snippet:codegen__api__py07}}

---

## Parser

Le parser consomme un flux de jetons deja produit.

{{snippet:codegen__api__py08}}

### Methodes

#### `parse() -> Program`

{{snippet:codegen__api__py09}}

---

## SemanticAnalyzer

Valide les portees et les contraintes semantiques du programme partage.

Depuis mars 2026, une affectation simple comme `x = 1` definit la variable si necessaire, tandis qu'une affectation augmentee comme `x += 1` exige toujours une definition prealable.

{{snippet:codegen__api__py10}}

### Methodes

#### `analyze(ast: Program) -> list[SemanticError]`

{{snippet:codegen__api__py11}}

---

## ASTPrinter

Affichage formate de l'AST pour le debogage.

{{snippet:codegen__api__py12}}

### Methodes

#### `print(ast) -> str`

{{snippet:codegen__api__py13}}

---

## PythonCodeGenerator

Transpile l'AST partage ou un `CoreIRProgram` en code Python.

{{snippet:codegen__api__py14}}

### Methodes

#### `generate(node) -> str`

{{snippet:codegen__api__py15}}

### Exemple de pipeline complet

{{snippet:codegen__api__py16}}

---

## Core IR et abaissement

### `lower_to_core_ir(ast, source_language, frontend_name="lexer_parser") -> CoreIRProgram`

Convertit le programme parse dans la representation coeur forward-only utilisee par les generateurs.

{{snippet:codegen__api__py17}}

### `CoreIRProgram`

{{snippet:codegen__api__py18}}

---

## RuntimeBuiltins

Construit l'espace de noms runtime du Python genere.

{{snippet:codegen__api__py19}}

### `namespace() -> dict`

Inclut:
- les builtins Python universels
- les builtins localises comme `afficher`
- les alias localises issus de `builtins_aliases.json` comme `longueur`

{{snippet:codegen__api__py20}}

### `make_exec_globals(language="en", extra=None) -> dict`

Helper recommande si vous utilisez `exec()` directement:

{{snippet:codegen__api__py21}}

---

## WATCodeGenerator

Generateur principal cote WASM. Il produit directement du WAT a partir de l'AST partage ou d'un `CoreIRProgram`.

{{snippet:codegen__api__py22}}

### Methodes

#### `generate(program) -> str`

Compile le programme complet en chaine WAT:

{{snippet:codegen__api__py23}}

Le module genere importe `env.print_str`, `env.print_f64`, `env.print_bool`, `env.print_sep` et `env.print_newline`, puis exporte `__main`.

### CLI: `build-wasm-bundle`

```bash
multilingual build-wasm-bundle programme.ml --out-dir wasm-out
```

Cette commande ecrit:
- `module.wat`
- `module.wasm`
- `host_shim.js`
- `abi_manifest.json`

---

## WasmCodeGenerator

Ancien generateur base sur un intermediaire Rust, dans `multilingualprogramming.codegen.wasm_generator`.

{{snippet:codegen__api__py24}}

### Methodes

#### `generate(program) -> str`

Retourne le code Rust intermediaire:

{{snippet:codegen__api__py25}}

### `WasmBuildConfig`

Helper pour conserver ou construire cet intermediaire:

{{snippet:codegen__api__py26}}

---

## BackendSelector

Selecteur runtime entre le repli Python et l'execution via module WASM.

{{snippet:codegen__api__py27}}

### Enum `Backend`

{{snippet:codegen__api__py28}}

### `is_wasm_available() -> bool`

{{snippet:codegen__api__py29}}

### `call_function(name: str, *args, **kwargs) -> Any`

{{snippet:codegen__api__py30}}

### Representation

Le backend effectif apparait dans `repr()`:

{{snippet:codegen__api__py31}}

### `BackendRegistry`

Permet d'enregistrer des implementations Python et WASM par nom:

{{snippet:codegen__api__py32}}

### Selection explicite du backend

{{snippet:codegen__api__py33}}

---

## FALLBACK_REGISTRY

Implementations Python de repli utilisees quand WASM est indisponible ou non selectionne.

{{snippet:codegen__api__py34}}

---

## REPL

Boucle interactive avec apercus optionnels du Python genere, du WAT et du pont Rust/Wasmtime.

{{snippet:codegen__api__py35}}

### Methodes

#### `run() -> None`

{{snippet:codegen__api__py36}}

### Commandes REPL

| Commande | Description |
|---------|-------------|
| `:help` | Afficher l'aide |
| `:language <code>` | Changer de langue |
| `:python` | Basculer l'aperçu Python |
| `:wat` / `:wasm` | Basculer l'aperçu WAT |
| `:rust` / `:wasmtime` | Basculer l'aperçu Rust/Wasmtime |
| `:reset` | Reinitialiser l'etat |
| `:kw [lang]` | Lister les mots-cles |
| `:ops [lang]` | Lister les operateurs et symboles |
| `:q` | Quitter |

---

## KeywordRegistry

Acces programmatique aux correspondances concept ↔ mot-cle.

{{snippet:codegen__api__py37}}

---

## Gestion des erreurs

Les exceptions frontend vivent dans `multilingualprogramming.exceptions`, tandis que `ProgramExecutor.execute()` renvoie en general les echecs via `ExecutionResult.errors`.

{{snippet:codegen__api__py38}}

---

## Exemple complet de reference

Execution et transpilation d'une source francaise de bout en bout:

{{snippet:codegen__api__py39}}
