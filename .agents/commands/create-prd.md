# Create PRD

Create or refresh project PRD content.

Default output path:
- `.project/specs/prd.md`

## Deterministic Bootstrap (recommended)

If PRD file is missing, create it from template first:

```bash
py scripts/init-prd.py --target .
```

Then refine content for this project.

## Required sections

- summary
- problem statement
- goals and non-goals
- scope and requirements
- risks and mitigations
- validation plan
- rollout notes

If context is missing, ask clarifying questions first.
