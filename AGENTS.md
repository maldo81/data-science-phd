# AI Working Agreement

This repository uses a layered documentation model:
- shared operations and reusable conventions in `.agents/`
- project-specific intent and specs in `.project/`
- tool-specific glue in `.claude/` and `.codex/`

If implementation conflicts with upstream docs, the docs win until they are explicitly updated.

## Required Reading Order

1. `.agents/README.md`
2. `.agents/core/non-negotiables.md`
3. `.agents/codex/workflow.md`
4. `.project/README.md`
5. `.project/specs/README.md`
6. `.project/specs/prd.md`

Never reason from code alone.

## Non-Negotiables

- Documentation-first, not code-first.
- Human confirmation for destructive or irreversible actions.
- No secrets in code, commits, or prompts.
- Keep changes testable, reversible, and auditable.

Detailed rules:
- `.agents/core/non-negotiables.md`
- `.agents/security/current.md` (if installed)
- `.agents/auth-rbac.md` (if installed)

## Operational Rules

- Follow PIV: Plan -> Implement -> Validate -> Iterate.
- Update `.project/specs/prd.md` when scope/sequence changes.
- Update `.project/specs/*` when conceptual boundaries change.
- Keep shared conventions in `.agents/*` and project intent in `.project/*`.

## Skills and Knowledge

- Canonical skills live in `.agents/skills/`.
- Project knowledge scaffold lives in `.agents/knowledge/`:
  - writing style: `.agents/knowledge/style/`
  - important documents: `.agents/knowledge/sources/`
  - retrieval/vector-db scaffold: `.agents/knowledge/retrieval/`

Invoke skills in Codex with `$skill-name`.
