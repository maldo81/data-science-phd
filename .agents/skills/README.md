# Skills (`.agents/skills`)

This folder is the canonical source of skills for this project.

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
python scripts/qa/validate_skills.py
```

## Sync to Tool-Specific Paths

Canonical -> mirrors:
- `.agents/skills` -> `.claude/skills`
- `.agents/skills` -> `.codex/skills`

Use:

```bash
python scripts/sync-skills.py --dry-run
python scripts/sync-skills.py
```
