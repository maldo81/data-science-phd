# Validate Changes

Run a focused validation pass after changes.

## 1) Repo status review

```bash
git status
git diff --stat HEAD
```

## 2) Run project tests/checks

```bash
# Replace with your project command set
# examples:
# pytest
# npm test
# make test
# uv run pytest
```

## 3) Migration/schema review (if data model changed)

```bash
# Ensure migrations are reviewed and reversible
# Ensure rollback/backups are defined for high-risk changes
```

## 4) Localization parity (if UI text changed)

```bash
# Run your localization workflow, then verify parity checks
```

## 5) Skills validation (if skills changed)

```bash
py scripts/qa/validate_skills.py
```
