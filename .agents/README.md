# Shared Operations (`.agents`)

This directory is the shared operations layer for humans and AI agents.

Use it to:
- define reusable operating rules
- keep agent workflows consistent
- host reusable skills
- scaffold a reusable knowledge base

## Document Authority

If documents conflict:
1. `.project/specs/*` defines project-specific intent and requirements.
2. `.agents/*` defines reusable operating conventions.
3. Code implements both and should not silently diverge.

## Start Here

- Root `AGENTS.md`
- Root `CLAUDE.md`
- `.agents/core/non-negotiables.md`
- `.agents/codex/workflow.md`
- `.agents/skills/README.md`
- `.agents/knowledge/README.md`

## Folder Map

- `.agents/core/` - non-negotiable rules shared across projects
- `.agents/codex/` - codex workflow notes
- `.agents/skills/` - canonical reusable skills
- `.agents/knowledge/` - writing/sources/retrieval scaffolding

## Change Discipline

When changing reusable conventions:
1. Update `.agents/*` first.
2. Then update tool glue (`.claude/*`, `.codex/*`) if needed.
3. Then propagate to projects via managed sync.

When changing project direction:
1. Update `.project/specs/*`.
2. Update project implementation after docs are aligned.
