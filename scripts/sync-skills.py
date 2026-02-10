#!/usr/bin/env python3
"""One-way sync of canonical skills from .agents/skills to tool-specific folders."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / ".agents" / "skills"
TARGETS = {
    "claude": ROOT / ".claude" / "skills",
    "codex": ROOT / ".codex" / "skills",
}


def sync_skill(skill_dir: Path, target_root: Path, dry_run: bool) -> None:
    target_dir = target_root / skill_dir.name
    if dry_run:
        print(f"[dry-run] sync {skill_dir} -> {target_dir}")
        return
    if target_dir.exists():
        shutil.rmtree(target_dir)
    target_root.mkdir(parents=True, exist_ok=True)
    shutil.copytree(skill_dir, target_dir)
    print(f"synced {skill_dir.name} -> {target_root}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Sync skills from .agents/skills")
    parser.add_argument("--dry-run", action="store_true", help="Show actions without writing")
    parser.add_argument("--skill", help="Sync only one skill folder name")
    parser.add_argument(
        "--target",
        choices=["claude", "codex", "all"],
        default="all",
        help="Sync destination",
    )
    args = parser.parse_args()

    if not SOURCE.exists():
        raise SystemExit(f"missing source directory: {SOURCE}")

    skills = sorted([p for p in SOURCE.iterdir() if p.is_dir()])
    if args.skill:
        skills = [p for p in skills if p.name == args.skill]
        if not skills:
            raise SystemExit(f"skill not found: {args.skill}")

    selected_targets = TARGETS.items() if args.target == "all" else [(args.target, TARGETS[args.target])]

    for _, target in selected_targets:
        for skill in skills:
            sync_skill(skill, target, args.dry_run)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
