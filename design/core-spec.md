---
layout: page
title: "Core Specification"
description: "Formal core specification v0.1 — the boundary between language frontends and code generation."
category: "Design"
permalink: /design/core-spec/
prev_page:
  title: "Architecture"
  url: /design/
next_page:
  title: "Frontend Contracts"
  url: /design/frontend-contracts/
---

The Core Specification defines the formal boundary used by all language frontends. It is the contract that separates frontend concerns (parsing, keyword resolution, surface normalization) from backend concerns (semantic analysis, code generation, execution).

**Version**: 0.1
**File**: `multilingualprogramming/core/ir.py`

---

## Core Object

`CoreIRProgram` is the typed container that wraps the shared Core AST:

```python
from dataclasses import dataclass, field

@dataclass
class CoreIRProgram:
    ast: Program              # required: the Core AST
    source_language: str      # required: e.g., "en", "fr", "ja"
    core_version: str = "0.1" # default: current core version
    frontend_metadata: dict = field(default_factory=dict)  # optional
```

**Fields:**

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `ast` | `Program` | Yes | The parsed Core AST |
| `source_language` | `str` | Yes | ISO language code used to parse the source |
| `core_version` | `str` | No | Core specification version (default: `"0.1"`) |
| `frontend_metadata` | `dict` | No | Frontend-specific metadata (author, file path, etc.) |

---

## Core Grammar (Minimal)

This minimal grammar captures the main contract between frontends and backends. The actual parser supports a richer grammar.

```
Program      ::= Statement*

Statement    ::= LetDecl
               | Assign
               | IfStmt
               | ForStmt
               | WhileStmt
               | MatchStmt
               | FuncDef
               | AsyncFuncDef
               | ClassDef
               | TryStmt
               | WithStmt
               | ReturnStmt
               | YieldStmt
               | ImportStmt
               | ExprStmt
               | GlobalStmt
               | NonlocalStmt
               | DelStmt
               | AssertStmt
               | RaiseStmt
               | BreakStmt
               | ContinueStmt
               | PassStmt

LetDecl      ::= "LET" Identifier [":" TypeAnnotation] "=" Expr
Assign       ::= Target [":" TypeAnnotation] "=" Expr
AugAssign    ::= Target AugOp Expr

IfStmt       ::= "COND_IF" Expr ":" Block
                 ("COND_ELIF" Expr ":" Block)*
                 ("COND_ELSE" ":" Block)?

ForStmt      ::= "LOOP_FOR" Target "IN" Expr ":" Block
                 ("COND_ELSE" ":" Block)?

WhileStmt    ::= "LOOP_WHILE" Expr ":" Block
                 ("COND_ELSE" ":" Block)?

MatchStmt    ::= "MATCH" Expr ":"
                 ("CASE" Pattern ["IF" Expr] ":" Block)+

FuncDef      ::= ["ASYNC"] "FUNC_DEF" Identifier "(" Params ")"
                 ["->"] TypeAnnotation?  ":" Block

ClassDef     ::= "CLASS_DEF" Identifier ["(" Bases ")"] ":" Block

TryStmt      ::= "TRY" ":" Block
                 ("EXCEPT" [ExceptTarget] ":" Block)*
                 ("COND_ELSE" ":" Block)?
                 ("FINALLY" ":" Block)?

WithStmt     ::= ["ASYNC"] "WITH" ContextList ":" Block

Block        ::= INDENT Statement+ DEDENT

Expr         ::= Literal
               | Identifier
               | Call
               | BinaryOp
               | UnaryOp
               | Compare
               | BoolOp
               | Collection
               | Slice
               | FString
               | Lambda
               | Comprehension
               | Await
               | Walrus
               | Ternary
               | Yield
               | YieldFrom
               | Starred

Literal      ::= Integer | Float | String | Boolean | None | Complex

Collection   ::= List | Dict | Set | Tuple
```

---

## Semantic Concept Tokens

Concept tokens are the boundary between frontend keyword resolution and backend parsing.

| Concept Token | Meaning | Example surface forms |
|---------------|---------|----------------------|
| `COND_IF` | Conditional | `if`, `si`, `wenn`, `もし`, `إذا` |
| `COND_ELIF` | Else-if | `elif`, `sinonsi`, `sonstewenn` |
| `COND_ELSE` | Else | `else`, `sinon`, `sonst`, `そうでなければ` |
| `LOOP_FOR` | For loop | `for`, `pour`, `für`, `毎` |
| `IN` | In (loop) | `in`, `dans`, `in`, `中`, `في` |
| `LOOP_WHILE` | While loop | `while`, `tantque`, `solange`, `間` |
| `BREAK` | Break | `break`, `arreter`, `abbrechen` |
| `CONTINUE` | Continue | `continue`, `continuer` |
| `PASS` | Pass | `pass`, `passer` |
| `LET` | Variable declaration | `let`, `soit`, `sei`, `変数`, `مان` |
| `CONST` | Constant | `const`, `constante` |
| `GLOBAL` | Global scope | `global`, `mondial`, `大域` |
| `NONLOCAL` | Nonlocal scope | `nonlocal`, `非局所` |
| `DEL` | Delete | `del`, `supprimer` |
| `ASSERT` | Assert | `assert`, `affirmer` |
| `FUNC_DEF` | Function def | `def`, `déf`, `定义`, `関数`, `دالة`, `परिभाषा` |
| `RETURN` | Return | `return`, `retourner`, `戻る` |
| `CLASS_DEF` | Class def | `class`, `classe`, `クラス`, `صنف`, `वर्ग` |
| `LAMBDA` | Lambda | `lambda`, `ラムダ` |
| `YIELD` | Yield | `yield`, `produire`, `産出` |
| `YIELD_FROM` | Yield from | `yield from`, `より産出` |
| `ASYNC` | Async | `async`, `非同期` |
| `AWAIT` | Await | `await`, `待機` |
| `TRY` | Try | `try`, `essayer`, `試す` |
| `EXCEPT` | Except | `except`, `sauf`, `除いて` |
| `FINALLY` | Finally | `finally`, `finalement`, `最終的に` |
| `RAISE` | Raise | `raise`, `soulever`, `発生` |
| `WITH` | With | `with`, `avec`, `付き` |
| `AS` | As | `as`, `comme`, `として` |
| `IMPORT` | Import | `import`, `importer`, `取込` |
| `FROM` | From | `from`, `de`, `から` |
| `MATCH` | Match | `match` |
| `CASE` | Case | `case` |

---

## Typing / Validation Rules

Current validation enforces:

1. `ast` must be a `Program` node (instance check)
2. `source_language` must be a non-empty string

**Creating a CoreIRProgram:**

```python
from multilingualprogramming.core.ir import CoreIRProgram
from multilingualprogramming.core.lowering import lower_to_core_ir
from multilingualprogramming import Lexer, Parser

# Parse source
lexer = Lexer(language="fr")
parser = Parser(language="fr")

source = "soit x = 42\nafficher(x)"
tokens = lexer.tokenize(source)
ast = parser.parse(tokens)

# Wrap in CoreIRProgram
core = lower_to_core_ir(ast, source_language="fr")

print(core.source_language)  # "fr"
print(core.core_version)     # "0.1"
print(type(core.ast).__name__)  # "Program"
```

---

## Forward-Only Property

The system guarantees this compilation direction:

```
CS_lang → CoreAST → CoreIRProgram → Python/WASM
```

It does **not** guarantee:
- Reconstruction of original source from Core IR
- Lossless round-trip from Core back to any surface language
- Source-level equivalence checking (only semantic equivalence)

This is by design: the project is a forward compilation framework, not a refactoring or source-transformation system.

---

## Core Version History

| Version | Changes |
|---------|---------|
| `0.1` | Initial core specification. Basic statement/expression grammar. |

Planned for `0.2`:
- Statement/expression sort checks
- Typed annotation consistency validation
- Lowering invariants for restricted subsets
