#!/usr/bin/env python
"""Bootstrap EN/FR multilingual metadata pages for Phase A sections."""

from __future__ import annotations

import hashlib
from pathlib import Path

import yaml

SECTIONS = ("getting-started", "language-guide", "reference")

FR_SECTION_SEGMENT = {
    "getting-started": "demarrage",
    "language-guide": "guide-langage",
    "reference": "references",
}

FR_SLUG = {
    "installation": "installation",
    "quick-start": "demarrage-rapide",
    "repl": "repl",
    "all-languages": "toutes-langues",
    "async-generators": "asynchrone-generateurs",
    "control-flow": "controle-flux",
    "french": "francais",
    "functions-classes": "fonctions-classes",
    "keywords": "mots-cles",
    "syntax": "syntaxe",
    "builtins": "fonctions-integrees",
    "compatibility": "compatibilite",
    "datetime": "date-heure",
    "numerals": "numeraux",
    "operators": "operateurs",
}

FR_TITLE = {
    "getting_started": "Demarrage",
    "getting_started__installation": "Installation",
    "getting_started__quick_start": "Demarrage rapide",
    "getting_started__repl": "Guide REPL",
    "language_guide": "Guide du langage",
    "language_guide__all_languages": "Toutes les langues",
    "language_guide__async_generators": "Asynchrone et generateurs",
    "language_guide__control_flow": "Controle de flux",
    "language_guide__french": "Guide francais",
    "language_guide__functions_classes": "Fonctions et classes",
    "language_guide__keywords": "Mots-cles",
    "language_guide__syntax": "Syntaxe",
    "reference": "Reference",
    "reference__builtins": "Fonctions integrees",
    "reference__compatibility": "Compatibilite",
    "reference__datetime": "Date et heure",
    "reference__numerals": "Numeraux",
    "reference__operators": "Operateurs",
}


def parse_front_matter(path: Path) -> tuple[dict, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}, text
    parts = text.split("---\n", 2)
    if len(parts) < 3:
        return {}, text
    front_matter = yaml.safe_load(parts[1]) or {}
    body = parts[2].lstrip("\n")
    return front_matter, body


def page_id_for(section: str, stem: str) -> str:
    section_id = section.replace("-", "_")
    if stem == "index":
        return section_id
    return f"{section_id}__{stem.replace('-', '_')}"


def path_segments_for(locale: str, section: str, stem: str) -> list[str]:
    if locale == "en":
        top = section
        leaf = section if stem == "index" else stem
    else:
        top = FR_SECTION_SEGMENT[section]
        leaf = top if stem == "index" else FR_SLUG.get(stem, stem)
    if stem == "index":
        return [top]
    return [top, leaf]


def build_front_matter(
    locale: str, page_id: str, title_en: str, source_hash: str, path_segments: list[str], status: str
) -> str:
    title = title_en if locale == "en" else FR_TITLE.get(page_id, title_en)
    payload = {
        "page_id": page_id,
        "locale": locale,
        "title": title,
        "path_segments": path_segments,
        "source_hash": source_hash,
        "status": status,
    }
    dumped = yaml.safe_dump(payload, sort_keys=False, allow_unicode=True).strip()
    return f"---\n{dumped}\n---\n\n"


def write_page(target: Path, front_matter: str, body: str, locale: str) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    if locale == "fr":
        banner = (
            "> NOTE: Version francaise en cours de revision. "
            "Le contenu technique ci-dessous reste synchronise avec la source anglaise.\n\n"
        )
        content = front_matter + banner + body
    else:
        content = front_matter + body
    target.write_text(content, encoding="utf-8")


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    content_root = repo_root / "docs" / "content"
    routing_root = repo_root / "docs" / "routing"

    en_routes: dict[str, dict[str, str]] = {}
    fr_routes: dict[str, dict[str, str]] = {}

    for section in SECTIONS:
        for src in sorted((repo_root / section).glob("*.md")):
            source_meta, body = parse_front_matter(src)
            stem = src.stem
            page_id = page_id_for(section, stem)
            source_hash = hashlib.sha1(body.encode("utf-8")).hexdigest()[:12]
            title_en = str(source_meta.get("title") or page_id.replace("_", " ").title())

            en_segments = path_segments_for("en", section, stem)
            fr_segments = path_segments_for("fr", section, stem)

            en_front = build_front_matter("en", page_id, title_en, source_hash, en_segments, "source")
            fr_front = build_front_matter(
                "fr", page_id, title_en, source_hash, fr_segments, "needs_update"
            )

            en_target = content_root / "en" / section / src.name
            fr_name = "index.md" if stem == "index" else f"{fr_segments[-1]}.md"
            fr_target = content_root / "fr" / FR_SECTION_DIR[section] / fr_name

            write_page(en_target, en_front, body, "en")
            write_page(fr_target, fr_front, body, "fr")

            en_routes[page_id] = {"path": f"/en/docs/{'/'.join(en_segments)}"}
            fr_routes[page_id] = {"path": f"/fr/docs/{'/'.join(fr_segments)}"}

    (routing_root / "en.routes.yml").write_text(
        yaml.safe_dump(en_routes, sort_keys=True, allow_unicode=True), encoding="utf-8"
    )
    (routing_root / "fr.routes.yml").write_text(
        yaml.safe_dump(fr_routes, sort_keys=True, allow_unicode=True), encoding="utf-8"
    )

    print("Phase A bootstrap complete for getting-started, language-guide, reference.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
FR_SECTION_DIR = {
    "getting-started": "demarrage",
    "language-guide": "guide-langage",
    "reference": "references",
}
