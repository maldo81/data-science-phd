# Skill Validation Policy

Default policy avoids extra API billing while maintaining quality.

## Required (always)

- Deterministic validation script:

```bash
py scripts/qa/validate_skills.py
```

macOS/Linux: replace `py` with `python3`.

This checks:
- frontmatter presence (`name`, `description`)
- folder/skill naming consistency
- referenced file existence

## Manual (recommended)

Use `scripts/qa/manual_skill_eval.md` for prompt-routing verification after changing skills.

## Optional automated evals

`scripts/qa/evals/run_skill_evals.py` is opt-in only.

- If no provider API key is configured, it exits as SKIPPED.
- Enable only when you intentionally accept separate API spend.
