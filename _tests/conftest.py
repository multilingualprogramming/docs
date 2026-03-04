"""Pytest options for docs code-block compilation tests."""


def pytest_addoption(parser):
    """Register project-local pytest CLI flags."""
    parser.addoption(
        "--block-verbose",
        action="store_true",
        default=False,
        help=(
            "Include failing markdown block id and full block source "
            "in assertion output for code-block tests."
        ),
    )
