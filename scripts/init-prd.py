#!/usr/bin/env python3
"""Create `.project/specs/prd.md` from template if missing (or with --force)."""

from __future__ import annotations

import argparse
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description="Initialize project PRD from template")
    parser.add_argument("--target", default=".", help="Project root")
    parser.add_argument(
        "--template",
        default=".project/specs/templates/prd.template.md",
        help="Template path relative to project root",
    )
    parser.add_argument(
        "--output",
        default=".project/specs/prd.md",
        help="Output path relative to project root",
    )
    parser.add_argument("--force", action="store_true", help="Overwrite existing output")
    args = parser.parse_args()

    root = Path(args.target).resolve()
    template = root / args.template
    output = root / args.output

    if not template.exists():
        raise SystemExit(f"template not found: {template}")

    if output.exists() and not args.force:
        print(f"skipped (exists): {output}")
        return 0

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(template.read_text(encoding="utf-8"), encoding="utf-8")
    print(f"wrote: {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
