#!/usr/bin/env python3
"""Deterministic validation for skill folder structure and metadata."""

from __future__ import annotations

from pathlib import Path
import sys
import re

ROOT = Path(__file__).resolve().parents[2]
SKILLS_ROOT = ROOT / ".agents" / "skills"

FRONTMATTER_NAME = re.compile(r"^name:\s*([a-z0-9-]+)\s*$")
FRONTMATTER_DESC = re.compile(r"^description:\s*(.+)$")


def parse_frontmatter(text: str) -> tuple[str | None, str | None, list[str]]:
    errors: list[str] = []
    if not text.startswith("---\n"):
        return None, None, ["missing YAML frontmatter opening '---'"]
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None, None, ["invalid YAML frontmatter block"]

    block = parts[1].strip().splitlines()
    name = None
    desc = None
    for line in block:
        n = FRONTMATTER_NAME.match(line.strip())
        d = FRONTMATTER_DESC.match(line.strip())
        if n:
            name = n.group(1)
        if d:
            desc = d.group(1).strip()

    if not name:
        errors.append("missing required frontmatter field: name")
    if not desc:
        errors.append("missing required frontmatter field: description")
    return name, desc, errors


def validate_skill(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        return ["missing SKILL.md"]

    content = skill_md.read_text(encoding="utf-8")
    name, _desc, parse_errors = parse_frontmatter(content)
    errors.extend(parse_errors)

    if name and name != skill_dir.name:
        errors.append(f"frontmatter name '{name}' must match folder '{skill_dir.name}'")

    # Ensure references listed in markdown code spans exist if they look like file paths
    for match in re.findall(r"`([^`]+)`", content):
        candidate = skill_dir / match
        if "/" in match and not match.startswith("http") and match.endswith((".md", ".py", ".sh", ".yaml", ".json")):
            if not candidate.exists():
                errors.append(f"referenced file not found: {match}")

    return errors


def main() -> int:
    if not SKILLS_ROOT.exists():
        print(f"ERROR: skills root missing: {SKILLS_ROOT}")
        return 1

    failures = 0
    names_seen: set[str] = set()

    for skill_dir in sorted([p for p in SKILLS_ROOT.iterdir() if p.is_dir()]):
        issues = validate_skill(skill_dir)
        if skill_dir.name in names_seen:
            issues.append("duplicate skill folder name")
        names_seen.add(skill_dir.name)

        if issues:
            failures += 1
            print(f"FAIL {skill_dir.name}")
            for issue in issues:
                print(f"  - {issue}")
        else:
            print(f"PASS {skill_dir.name}")

    if failures:
        print(f"\nSkill validation failed: {failures} skill(s) with issues")
        return 1

    print("\nSkill validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
