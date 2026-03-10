---
page_id: wasm__architecture
locale: fr
title: Architecture WASM
path_segments:
- wasm
- architecture
source_hash: 8daba5db70bd
status: translated
permalink: /fr/docs/wasm/architecture/
---

Le pipeline WASM actuel (`0.6.0`) suit la chaîne : source multilingue -> AST cœur -> génération WAT -> module WASM -> exécution via runtime.

Le backend Python reste disponible comme repli automatique.

{{snippet:wasm__architecture__py01}}

{{snippet:wasm__architecture__py02}}

{{snippet:wasm__architecture__py03}}

{{snippet:wasm__architecture__py04}}

{{snippet:wasm__architecture__py05}}

{{snippet:wasm__architecture__py06}}
