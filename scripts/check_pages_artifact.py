#!/usr/bin/env python
"""Sanity checks for Jekyll build output before GitHub Pages deployment."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--site-dir", default="_site")
    parser.add_argument("--base-path", default="")
    args = parser.parse_args()

    site_dir = Path(args.site_dir)
    if not site_dir.exists():
        print(f"ERROR: site directory does not exist: {site_dir}")
        return 1

    index_file = site_dir / "index.html"
    page_404 = site_dir / "404.html"
    if not index_file.exists():
        print(f"ERROR: missing required file: {index_file}")
        return 1
    if not page_404.exists():
        print(f"ERROR: missing required file: {page_404}")
        return 1

    if args.base_path and not args.base_path.startswith("/"):
        print(f"ERROR: invalid base path (must start with '/'): {args.base_path!r}")
        return 1

    print(f"Pages artifact sanity checks passed for {site_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
