#!/usr/bin/env python3
"""Generate a compact context bundle for local LLM workflows."""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / ".agents" / "context" / "context-bundle.md"

REQUIRED_FILES = [
    ROOT / "AGENTS.md",
    ROOT / "CLAUDE.md",
    ROOT / ".agents" / "README.md",
    ROOT / ".agents" / "core" / "non-negotiables.md",
    ROOT / ".agents" / "codex" / "workflow.md",
    ROOT / ".agents" / "skills" / "README.md",
    ROOT / ".agents" / "knowledge" / "README.md",
    ROOT / ".agents" / "knowledge" / "index.md",
    ROOT / ".project" / "README.md",
    ROOT / ".project" / "specs" / "README.md",
    ROOT / ".project" / "specs" / "prd.md",
]

OPTIONAL_FILES = [
    ROOT / ".agents" / "security" / "current.md",
    ROOT / ".agents" / "auth-rbac.md",
]


def append_file(lines: list[str], path: Path) -> None:
    rel = path.relative_to(ROOT)
    if not path.exists():
        lines.append(f"## MISSING: {rel}")
        lines.append("")
        return
    lines.append(f"## {rel}")
    lines.append("")
    lines.append(path.read_text(encoding="utf-8"))
    lines.append("")


def main() -> int:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    now = datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")

    lines: list[str] = []
    lines.append("# Context Bundle")
    lines.append("")
    lines.append("> GENERATED FILE - DO NOT EDIT DIRECTLY")
    lines.append(f"> Generated at: {now}")
    lines.append("")

    for path in REQUIRED_FILES:
        append_file(lines, path)

    for path in OPTIONAL_FILES:
        if path.exists():
            append_file(lines, path)

    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
