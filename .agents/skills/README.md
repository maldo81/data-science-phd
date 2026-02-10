# Skills (`.agents/skills`)

This folder is the canonical source of skills for the project.

## Required Skill Contract

Each skill folder must include:
- `SKILL.md` with YAML frontmatter containing `name` and `description`

Recommended:
- `agents/openai.yaml` for UI metadata
- `references/` for deep docs
- `scripts/` for deterministic helpers
- `assets/` for reusable output files

## Progressive Disclosure

1. Frontmatter metadata is lightweight and always available.
2. `SKILL.md` body loads only when the skill triggers.
3. `references/` and `scripts/` are loaded/executed only when needed.

## Validation

Run deterministic validation:

```bash
py scripts/qa/validate_skills.py
```

Then run manual routing checks:

```bash
cat scripts/qa/manual_skill_eval.md
```

macOS/Linux: replace `py` with `python3`.

## Sync to Tool-Specific Paths

Canonical -> mirrors:
- `.agents/skills` -> `.claude/skills`
- `.agents/skills` -> `.codex/skills`

Use:

```bash
py scripts/sync-skills.py --dry-run
py scripts/sync-skills.py
```

## Pack Notes

Additional skills may be installed from stable or experimental packs via:

```bash
py .agent-core/scripts/apply_core.py --list-packs
```
