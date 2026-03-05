#!/usr/bin/env python
"""Validate EN/FR multilingual docs metadata and assets."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path

import yaml

REQUIRED_KEYS = {"page_id", "locale", "title", "path_segments", "source_hash", "status"}
SUPPORTED_LOCALES = ("en", "fr")
SNIPPET_TOKEN_RE = re.compile(r"\{\{\s*snippet:([a-zA-Z0-9_-]+)\s*\}\}")


@dataclass
class DocPage:
    file_path: Path
    page_id: str
    locale: str
    title: str
    path_segments: list[str]
    source_hash: str
    status: str
    body: str

    @property
    def route_path(self) -> str:
        return f"/{self.locale}/docs/" + "/".join(self.path_segments)


def parse_front_matter(path: Path) -> tuple[dict, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError(f"{path}: missing YAML front matter start delimiter")
    parts = text.split("---\n", 2)
    if len(parts) < 3:
        raise ValueError(f"{path}: invalid YAML front matter format")
    raw_yaml = parts[1]
    body = parts[2]
    data = yaml.safe_load(raw_yaml) or {}
    if not isinstance(data, dict):
        raise ValueError(f"{path}: front matter must be a YAML mapping")
    return data, body


def load_routes(repo_root: Path, locale: str) -> dict[str, str]:
    route_file = repo_root / "docs" / "routing" / f"{locale}.routes.yml"
    if not route_file.exists():
        raise ValueError(f"missing route manifest: {route_file}")
    raw = yaml.safe_load(route_file.read_text(encoding="utf-8")) or {}
    if not isinstance(raw, dict):
        raise ValueError(f"{route_file}: manifest must be a mapping")
    routes: dict[str, str] = {}
    for page_id, payload in raw.items():
        if isinstance(payload, dict):
            path_value = payload.get("path")
        else:
            path_value = None
        if not isinstance(page_id, str) or not isinstance(path_value, str):
            raise ValueError(f"{route_file}: entry for {page_id!r} must include string path")
        routes[page_id] = path_value
    return routes


def load_docs(repo_root: Path, locale: str) -> dict[str, DocPage]:
    root = repo_root / "docs" / "content" / locale
    if not root.exists():
        raise ValueError(f"missing locale folder: {root}")
    pages: dict[str, DocPage] = {}
    for path in root.rglob("*.md"):
        metadata, body = parse_front_matter(path)
        missing = REQUIRED_KEYS - metadata.keys()
        if missing:
            raise ValueError(f"{path}: missing required keys: {sorted(missing)}")
        page_id = metadata["page_id"]
        locale_value = metadata["locale"]
        title = metadata["title"]
        path_segments = metadata["path_segments"]
        source_hash = metadata["source_hash"]
        status = metadata["status"]
        if not isinstance(page_id, str) or not page_id:
            raise ValueError(f"{path}: page_id must be a non-empty string")
        if locale_value != locale:
            raise ValueError(f"{path}: locale must be {locale!r}, got {locale_value!r}")
        if not isinstance(title, str) or not title:
            raise ValueError(f"{path}: title must be a non-empty string")
        if not isinstance(path_segments, list) or not path_segments:
            raise ValueError(f"{path}: path_segments must be a non-empty list")
        if not all(isinstance(segment, str) and segment for segment in path_segments):
            raise ValueError(f"{path}: every path_segments entry must be a non-empty string")
        if not isinstance(source_hash, str) or not source_hash:
            raise ValueError(f"{path}: source_hash must be a non-empty string")
        if not isinstance(status, str) or not status:
            raise ValueError(f"{path}: status must be a non-empty string")
        if page_id in pages:
            raise ValueError(f"{path}: duplicate page_id {page_id!r} for locale {locale}")
        pages[page_id] = DocPage(
            file_path=path,
            page_id=page_id,
            locale=locale,
            title=title,
            path_segments=path_segments,
            source_hash=source_hash,
            status=status,
            body=body,
        )
    return pages


def validate_snippets(repo_root: Path, page: DocPage, errors: list[str]) -> None:
    for snippet_id in SNIPPET_TOKEN_RE.findall(page.body):
        snippet_file = repo_root / "docs" / "snippets" / snippet_id / f"{page.locale}.code"
        if not snippet_file.exists():
            errors.append(
                f"{page.file_path}: missing snippet variant for {snippet_id!r} locale {page.locale}"
            )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--strict-freshness", action="store_true")
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parents[1]
    errors: list[str] = []
    warnings: list[str] = []

    pages_by_locale: dict[str, dict[str, DocPage]] = {}
    routes_by_locale: dict[str, dict[str, str]] = {}
    try:
        for locale in SUPPORTED_LOCALES:
            pages_by_locale[locale] = load_docs(repo_root, locale)
            routes_by_locale[locale] = load_routes(repo_root, locale)
    except ValueError as exc:
        print(f"ERROR: {exc}")
        return 1

    en_ids = set(pages_by_locale["en"])
    fr_ids = set(pages_by_locale["fr"])
    missing_in_fr = sorted(en_ids - fr_ids)
    missing_in_en = sorted(fr_ids - en_ids)
    if missing_in_fr:
        errors.append(f"missing French pages for page_id(s): {', '.join(missing_in_fr)}")
    if missing_in_en:
        errors.append(f"missing English pages for page_id(s): {', '.join(missing_in_en)}")

    for locale in SUPPORTED_LOCALES:
        locale_pages = pages_by_locale[locale]
        locale_routes = routes_by_locale[locale]
        route_seen: dict[str, str] = {}
        for page_id, page in locale_pages.items():
            expected_route = page.route_path
            actual_route = locale_routes.get(page_id)
            if actual_route is None:
                errors.append(f"{locale} route manifest missing page_id {page_id!r}")
            elif actual_route != expected_route:
                errors.append(
                    f"{locale} route mismatch for {page_id!r}: expected {expected_route}, got {actual_route}"
                )
            previous = route_seen.get(expected_route)
            if previous:
                errors.append(
                    f"{locale} route collision: {expected_route} used by {previous!r} and {page_id!r}"
                )
            else:
                route_seen[expected_route] = page_id
            validate_snippets(repo_root, page, errors)
        extra_routes = sorted(set(locale_routes) - set(locale_pages))
        for extra in extra_routes:
            errors.append(f"{locale} route manifest has unknown page_id {extra!r}")

    common_ids = sorted(en_ids & fr_ids)
    stale_ids: list[str] = []
    for page_id in common_ids:
        en_hash = pages_by_locale["en"][page_id].source_hash
        fr_hash = pages_by_locale["fr"][page_id].source_hash
        if en_hash != fr_hash:
            stale_ids.append(page_id)
    if stale_ids:
        message = "stale translation hash mismatch for page_id(s): " + ", ".join(stale_ids)
        if args.strict_freshness:
            errors.append(message)
        else:
            warnings.append(message)

    if warnings:
        for warning in warnings:
            print(f"WARNING: {warning}")
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print("Multilingual docs validation passed for locales: en, fr")
    return 0


if __name__ == "__main__":
    sys.exit(main())
