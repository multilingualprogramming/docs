from pathlib import Path

from scripts.check_internal_links import check_site


def write(tmp_path: Path, relative_path: str, content: str) -> None:
    target = tmp_path / relative_path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8")


def test_check_site_accepts_valid_internal_links(tmp_path: Path) -> None:
    write(
        tmp_path,
        "index.html",
        """
        <html><body>
        <a href="/docs/fr/docs/demarrage/">French getting started</a>
        <a href="/docs/fr/docs/guide-langage/toutes-langues/#equivalents">All languages</a>
        </body></html>
        """,
    )
    write(
        tmp_path,
        "fr/docs/demarrage/index.html",
        """
        <html><body>
        <a href="/docs/fr/docs/guide-langage/toutes-langues/#equivalents">Guide</a>
        </body></html>
        """,
    )
    write(
        tmp_path,
        "fr/docs/guide-langage/toutes-langues/index.html",
        """
        <html><body>
        <h1 id="equivalents">Equivalents</h1>
        </body></html>
        """,
    )

    assert check_site(tmp_path, base_path="/docs") == []


def test_check_site_rejects_root_relative_links_without_base_path(tmp_path: Path) -> None:
    write(
        tmp_path,
        "fr/docs/demarrage/demarrage-rapide/index.html",
        """
        <html><body>
        <a href="/fr/docs/guide-langage/toutes-langues/">Broken link</a>
        </body></html>
        """,
    )
    write(
        tmp_path,
        "fr/docs/guide-langage/toutes-langues/index.html",
        "<html><body></body></html>",
    )

    errors = check_site(tmp_path, base_path="/docs")

    assert len(errors) == 1
    assert "bypasses base path /docs" in errors[0]


def test_check_site_rejects_missing_anchor(tmp_path: Path) -> None:
    write(
        tmp_path,
        "fr/docs/demarrage/index.html",
        """
        <html><body>
        <a href="/docs/fr/docs/guide-langage/#missing-anchor">Guide</a>
        </body></html>
        """,
    )
    write(
        tmp_path,
        "fr/docs/guide-langage/index.html",
        """
        <html><body>
        <h1 id="existing-anchor">Guide</h1>
        </body></html>
        """,
    )

    errors = check_site(tmp_path, base_path="/docs")

    assert len(errors) == 1
    assert "missing anchor #missing-anchor" in errors[0]
