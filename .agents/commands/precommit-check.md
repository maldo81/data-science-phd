# Precommit Check

Run this checklist before committing:

1. `git status` and `git diff --stat HEAD` reviewed.
2. Relevant tests/checks completed for changed surfaces.
3. Migration implications reviewed if schema/data changed.
4. Translation parity reviewed if UI copy changed.
5. Skill validation executed if skills changed.
6. No secrets/credentials are staged.
7. Project specs and shared docs were updated when needed.
