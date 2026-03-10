---
page_id: codegen__api
locale: fr
title: Référence de l'API de génération de code
path_segments:
- generation-code
- api
source_hash: f5184586a04b
status: translated
permalink: /fr/docs/generation-code/api/
---

Cette page documente l'API actuelle `0.6.0` de transpilation, d'exécution et de génération WAT/WASM.

---

## Imports

{{snippet:codegen__api__py01}}

---

## `ProgramExecutor`

Point d'entrée de haut niveau pour l'ensemble du pipeline.

{{snippet:codegen__api__py02}}

### Méthodes

#### `execute(source, capture_output=True, globals_dict=None) -> ExecutionResult`

Exécute le lexing, le parsing, l'abaissement Core IR, l'analyse sémantique optionnelle, la génération Python, puis `exec()`.

Le résultat expose notamment :
- `output`
- `python_source`
- `errors`
- `success`
- `return_value`

{{snippet:codegen__api__py03}}

#### `transpile(source) -> str`

Génère le Python sans l'exécuter :

{{snippet:codegen__api__py04}}

### Transpilation multilingue

Toutes les variantes linguistiques convergent vers le même pipeline interne :

{{snippet:codegen__api__py05}}

---

## Lexer

Le lexer prend le texte source et, en option, un indice de langue.

{{snippet:codegen__api__py06}}

### Méthodes

#### `tokenize() -> list[Token]`

{{snippet:codegen__api__py07}}

---

## Parser

Le parser consomme un flux de jetons déjà produit.

{{snippet:codegen__api__py08}}

### Méthodes

#### `parse() -> Program`

{{snippet:codegen__api__py09}}

---

## `SemanticAnalyzer`

Valide les portées et les contraintes sémantiques du programme partagé.

Depuis mars 2026, une affectation simple comme `x = 1` définit la variable si nécessaire, tandis qu'une affectation augmentée comme `x += 1` exige toujours une définition préalable.

{{snippet:codegen__api__py10}}

### Méthodes

#### `analyze(ast: Program) -> list[SemanticError]`

{{snippet:codegen__api__py11}}

---

## `ASTPrinter`

Affichage formaté de l'AST pour le débogage.

{{snippet:codegen__api__py12}}

### Méthodes

#### `print(ast) -> str`

{{snippet:codegen__api__py13}}

---

## `PythonCodeGenerator`

Transpile l'AST partagé ou un `CoreIRProgram` en code Python.

{{snippet:codegen__api__py14}}

### Méthodes

#### `generate(node) -> str`

{{snippet:codegen__api__py15}}

### Exemple de pipeline complet

{{snippet:codegen__api__py16}}

---

## Core IR et abaissement

### `lower_to_core_ir(ast, source_language, frontend_name="lexer_parser") -> CoreIRProgram`

Convertit le programme parsé dans la représentation cœur forward-only utilisée par les générateurs.

{{snippet:codegen__api__py17}}

### `CoreIRProgram`

{{snippet:codegen__api__py18}}

---

## `RuntimeBuiltins`

Construit l'espace de noms runtime du Python généré.

{{snippet:codegen__api__py19}}

### `namespace() -> dict`

Inclut :
- les builtins Python universels
- les builtins localisés comme `afficher`
- les alias localisés issus de `builtins_aliases.json` comme `longueur`

{{snippet:codegen__api__py20}}

### `make_exec_globals(language="en", extra=None) -> dict`

Helper recommandé si vous utilisez `exec()` directement :

{{snippet:codegen__api__py21}}

---

## `WATCodeGenerator`

Générateur principal côté WASM. Il produit directement du WAT à partir de l'AST partagé ou d'un `CoreIRProgram`.

En `0.6.0`, le backend WAT couvre l'état actuel du modèle objet à classes stateful, le dispatch dynamique, les accesseurs de propriété, l'abaissement de `with`/`try`/`match`, les littéraux `bytes` et l'abaissement asynchrone best-effort décrit dans le dépôt amont.

{{snippet:codegen__api__py22}}

### Méthodes

#### `generate(program) -> str`

Compile le programme complet en chaîne WAT :

{{snippet:codegen__api__py23}}

Le module généré importe `env.print_str`, `env.print_f64`, `env.print_bool`, `env.print_sep` et `env.print_newline`, puis exporte `__main`.

### CLI : `build-wasm-bundle`

```bash
multilingual build-wasm-bundle programme.ml --out-dir wasm-out
```

Cette commande écrit :
- `module.wat`
- `module.wasm`
- `host_shim.js`
- `abi_manifest.json`

---

## `WasmCodeGenerator`

Ancien générateur basé sur un intermédiaire Rust, dans `multilingualprogramming.codegen.wasm_generator`.

{{snippet:codegen__api__py24}}

### Méthodes

#### `generate(program) -> str`

Retourne le code Rust intermédiaire :

{{snippet:codegen__api__py25}}

### `WasmBuildConfig`

Helper pour conserver ou construire cet intermédiaire :

{{snippet:codegen__api__py26}}

---

## `BackendSelector`

Sélecteur runtime entre le repli Python et l'exécution via module WASM.

{{snippet:codegen__api__py27}}

### Enum `Backend`

{{snippet:codegen__api__py28}}

### `is_wasm_available() -> bool`

{{snippet:codegen__api__py29}}

### `call_function(name: str, *args, **kwargs) -> Any`

{{snippet:codegen__api__py30}}

### Représentation

Le backend effectif apparaît dans `repr()` :

{{snippet:codegen__api__py31}}

### `BackendRegistry`

Permet d'enregistrer des implémentations Python et WASM par nom :

{{snippet:codegen__api__py32}}

### Sélection explicite du backend

{{snippet:codegen__api__py33}}

---

## `FALLBACK_REGISTRY`

Implémentations Python de repli utilisées quand WASM est indisponible ou non sélectionné.

{{snippet:codegen__api__py34}}

---

## REPL

Boucle interactive avec aperçus optionnels du Python généré, du WAT et du pont Rust/Wasmtime.

{{snippet:codegen__api__py35}}

### Méthodes

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
| `:reset` | Réinitialiser l'état |
| `:kw [lang]` | Lister les mots-clés |
| `:ops [lang]` | Lister les opérateurs et symboles |
| `:q` | Quitter |

---

## `KeywordRegistry`

Accès programmatique aux correspondances concept ↔ mot-clé.

{{snippet:codegen__api__py37}}

---

## Gestion des erreurs

Les exceptions frontend vivent dans `multilingualprogramming.exceptions`, tandis que `ProgramExecutor.execute()` renvoie en général les échecs via `ExecutionResult.errors`.

{{snippet:codegen__api__py38}}

---

## Exemple complet de référence

Exécution et transpilation d'une source française de bout en bout :

{{snippet:codegen__api__py39}}
