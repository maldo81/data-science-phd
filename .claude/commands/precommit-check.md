---
description: Pre-commit checklist for quality and safety
---

Run this checklist before committing:
1. `git status` and `git diff --stat HEAD` reviewed.
2. Relevant tests pass.
3. Migration implications reviewed (if schema/data touched).
4. Translation parity verified (if UI text changed).
5. Skills validated (if skill files changed).
6. No secrets/credentials in staged files.
7. Documentation updates are included.

This command is checklist-only; avoid destructive automation.
