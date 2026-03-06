---
page_id: codegen__api
locale: en
title: Codegen API Reference
path_segments:
- codegen
- api
source_hash: 66021f3a6bbf
status: source
permalink: /en/docs/codegen/api/
---

This page documents the current `0.5.1` code-generation and execution APIs used by `multilingualprogramming`.

---

## Imports

{{snippet:codegen__api__py01}}

---

## ProgramExecutor

High-level entry point for the full frontend-to-runtime pipeline.

{{snippet:codegen__api__py02}}

### Methods

#### `execute(source, capture_output=True, globals_dict=None) -> ExecutionResult`

Runs lexing, parsing, Core IR lowering, optional semantic analysis, Python generation, and `exec()`.

The returned `ExecutionResult` exposes:
- `output`
- `python_source`
- `errors`
- `success`
- `return_value`

{{snippet:codegen__api__py03}}

#### `transpile(source) -> str`

Generate Python without executing it:

{{snippet:codegen__api__py04}}

#### Multi-Language Transpilation

All frontends lower into the same shared core pipeline:

{{snippet:codegen__api__py05}}

---

## Lexer

The lexer is initialized with source text and an optional language hint.

{{snippet:codegen__api__py06}}

### Methods

#### `tokenize() -> list[Token]`

{{snippet:codegen__api__py07}}

---

## Parser

The parser consumes an existing token stream.

{{snippet:codegen__api__py08}}

### Methods

#### `parse() -> Program`

{{snippet:codegen__api__py09}}

---

## SemanticAnalyzer

Performs scope validation and semantic checks on the shared AST.

As of March 2026, plain assignments such as `x = 1` define the variable if needed, while augmented assignments such as `x += 1` still require the name to exist first.

{{snippet:codegen__api__py10}}

### Methods

#### `analyze(ast: Program) -> list[SemanticError]`

{{snippet:codegen__api__py11}}

---

## ASTPrinter

Pretty-prints AST nodes for debugging.

{{snippet:codegen__api__py12}}

### Methods

#### `print(ast) -> str`

{{snippet:codegen__api__py13}}

---

## PythonCodeGenerator

Transpiles the shared AST or a `CoreIRProgram` to Python source.

{{snippet:codegen__api__py14}}

### Methods

#### `generate(node) -> str`

{{snippet:codegen__api__py15}}

### Full Pipeline Example

{{snippet:codegen__api__py16}}

---

## Core IR and Lowering

### `lower_to_core_ir(ast, source_language, frontend_name="lexer_parser") -> CoreIRProgram`

Converts the parsed program into the forward-only core representation used by the generators.

{{snippet:codegen__api__py17}}

### `CoreIRProgram`

{{snippet:codegen__api__py18}}

---

## RuntimeBuiltins

Provides the runtime namespace for generated Python.

{{snippet:codegen__api__py19}}

### `namespace() -> dict`

Includes:
- universal Python builtins
- localized keyword-backed builtins such as `afficher`
- localized aliases from `builtins_aliases.json` such as `longueur`

{{snippet:codegen__api__py20}}

### `make_exec_globals(language="en", extra=None) -> dict`

Recommended helper when you call `exec()` yourself:

{{snippet:codegen__api__py21}}

---

## WATCodeGenerator

Primary WASM-facing generator. It emits WAT directly from the shared AST or from a `CoreIRProgram`.

{{snippet:codegen__api__py22}}

### Methods

#### `generate(program) -> str`

Compile the full program to a WAT module string:

{{snippet:codegen__api__py23}}

The returned module imports `env.print_str`, `env.print_f64`, `env.print_bool`, `env.print_sep`, and `env.print_newline`, and exports `__main`.

### CLI: `build-wasm-bundle`

```bash
multilingual build-wasm-bundle program.ml --out-dir wasm-out
```

This writes:
- `module.wat`
- `module.wasm`
- `host_shim.js`
- `abi_manifest.json`

---

## WasmCodeGenerator

Legacy Rust-intermediate generator in `multilingualprogramming.codegen.wasm_generator`.

{{snippet:codegen__api__py24}}

### Methods

#### `generate(program) -> str`

Returns Rust intermediate code:

{{snippet:codegen__api__py25}}

### `WasmBuildConfig`

Helper used to keep or build that Rust intermediate:

{{snippet:codegen__api__py26}}

---

## BackendSelector

Runtime selector for Python fallback vs. WASM module execution.

{{snippet:codegen__api__py27}}

### `Backend` Enum

{{snippet:codegen__api__py28}}

### `is_wasm_available() -> bool`

{{snippet:codegen__api__py29}}

### `call_function(name: str, *args, **kwargs) -> Any`

{{snippet:codegen__api__py30}}

### Representation

The selector exposes its effective backend through `repr()`:

{{snippet:codegen__api__py31}}

### `BackendRegistry`

Register Python and WASM implementations for named functions:

{{snippet:codegen__api__py32}}

### Explicit Backend Selection

{{snippet:codegen__api__py33}}

---

## FALLBACK_REGISTRY

Pure-Python fallback implementations used when WASM is unavailable or not selected.

{{snippet:codegen__api__py34}}

---

## REPL

Interactive execution loop with optional Python, WAT, and Rust/Wasmtime previews.

{{snippet:codegen__api__py35}}

### Methods

#### `run() -> None`

{{snippet:codegen__api__py36}}

### REPL Commands

| Command | Description |
|---------|-------------|
| `:help` | Show help |
| `:language <code>` | Switch language |
| `:python` | Toggle generated Python preview |
| `:wat` / `:wasm` | Toggle generated WAT preview |
| `:rust` / `:wasmtime` | Toggle generated Rust/Wasmtime bridge preview |
| `:reset` | Clear state |
| `:kw [lang]` | List keywords |
| `:ops [lang]` | List operators and symbols |
| `:q` | Quit |

---

## KeywordRegistry

Programmatic access to concept-to-keyword and keyword-to-concept mappings.

{{snippet:codegen__api__py37}}

---

## Error Handling

Frontend exceptions live in `multilingualprogramming.exceptions`, while `ProgramExecutor.execute()` usually reports failures through `ExecutionResult.errors`.

{{snippet:codegen__api__py38}}

---

## Complete Reference Example

End-to-end French source execution and transpilation:

{{snippet:codegen__api__py39}}
