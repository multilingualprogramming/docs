#!/usr/bin/env python
"""Validate internal links in the built Jekyll site."""

from __future__ import annotations

import argparse
import posixpath
import sys
from dataclasses import dataclass, field
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlsplit


SKIP_SCHEMES = {"http", "https", "mailto", "tel", "javascript", "data"}


@dataclass
class BuiltPage:
    html_file: Path
    url: str
    anchors: set[str] = field(default_factory=set)
    links: list[str] = field(default_factory=list)


class HtmlLinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.anchors: set[str] = set()
        self.links: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr_map = dict(attrs)
        element_id = attr_map.get("id")
        if element_id:
            self.anchors.add(element_id)

        if tag == "a":
            anchor_name = attr_map.get("name")
            if anchor_name:
                self.anchors.add(anchor_name)

        if tag in {"a", "area"}:
            href = attr_map.get("href")
            if href:
                self.links.append(href)


def build_public_url(html_file: Path, site_dir: Path) -> str:
    rel = html_file.relative_to(site_dir).as_posix()
    if rel == "index.html":
        return "/"
    if rel.endswith("/index.html"):
        return "/" + rel[: -len("index.html")]
    return "/" + rel


def alias_paths(url: str) -> set[str]:
    aliases = {url}
    if url.endswith("/"):
        aliases.add(url + "index.html")
        if url != "/":
            aliases.add(url.rstrip("/"))
    elif url.endswith("/index.html"):
        aliases.add(url[: -len("index.html")])
        aliases.add(url[: -len("/index.html")] or "/")
    elif url.endswith(".html"):
        aliases.add(url[: -len(".html")] or "/")
    else:
        aliases.add(url + "/")
        aliases.add(url + ".html")
        aliases.add(url + "/index.html")
    return aliases


def collect_site_pages(site_dir: Path) -> tuple[dict[str, BuiltPage], dict[str, BuiltPage]]:
    canonical_pages: dict[str, BuiltPage] = {}
    alias_index: dict[str, BuiltPage] = {}

    for html_file in site_dir.rglob("*.html"):
        parser = HtmlLinkParser()
        parser.feed(html_file.read_text(encoding="utf-8"))
        page = BuiltPage(
            html_file=html_file,
            url=build_public_url(html_file, site_dir),
            anchors=parser.anchors,
            links=parser.links,
        )
        canonical_pages[page.url] = page
        for alias in alias_paths(page.url):
            alias_index[alias] = page

    return canonical_pages, alias_index


def resolve_site_path(raw_path: str, *, current_url: str, base_path: str) -> tuple[str | None, str | None]:
    if raw_path.startswith("#"):
        return current_url, None

    absolute_url = urljoin(f"https://example.test{current_url}", raw_path)
    parsed = urlsplit(absolute_url)
    if parsed.scheme and parsed.scheme not in {"https", "http"}:
        return None, None

    path = parsed.path or "/"
    if base_path:
        if path == base_path:
            return "/", None
        if path.startswith(base_path + "/"):
            trimmed = path[len(base_path) :]
            return trimmed or "/", None
        if path.startswith("/"):
            return None, f"root-relative URL bypasses base path {base_path}: {raw_path}"

    normalized = posixpath.normpath(path)
    if not normalized.startswith("/"):
        normalized = "/" + normalized
    if path.endswith("/") and not normalized.endswith("/"):
        normalized += "/"
    return normalized, None


def check_site(site_dir: Path, *, base_path: str) -> list[str]:
    canonical_pages, alias_index = collect_site_pages(site_dir)
    errors: list[str] = []

    for page in canonical_pages.values():
        for href in page.links:
            parsed = urlsplit(href)
            if parsed.scheme in SKIP_SCHEMES or parsed.netloc:
                continue

            target_path, error = resolve_site_path(href, current_url=page.url, base_path=base_path)
            if error:
                errors.append(f"{page.url} -> {href}: {error}")
                continue
            if target_path is None:
                continue

            target_page = alias_index.get(target_path)
            if target_page is None:
                errors.append(f"{page.url} -> {href}: missing target page {target_path}")
                continue

            fragment = parsed.fragment
            if fragment and fragment not in target_page.anchors:
                errors.append(
                    f"{page.url} -> {href}: missing anchor #{fragment} in {target_page.url}"
                )

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--site-dir", default="_site")
    parser.add_argument("--base-path", default="")
    args = parser.parse_args()

    site_dir = Path(args.site_dir)
    if not site_dir.exists():
        print(f"ERROR: site directory does not exist: {site_dir}")
        return 1

    if args.base_path and not args.base_path.startswith("/"):
        print(f"ERROR: invalid base path (must start with '/'): {args.base_path!r}")
        return 1

    errors = check_site(site_dir, base_path=args.base_path)
    if errors:
        print("ERROR: broken internal links found:")
        for error in errors[:100]:
            print(f" - {error}")
        if len(errors) > 100:
            print(f" - ... and {len(errors) - 100} more")
        return 1

    print(f"Internal link checks passed for {site_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
