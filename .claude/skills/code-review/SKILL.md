---
name: code-review
description: Perform structured code review focused on regressions, correctness, security, and test gaps. Use after meaningful code changes, before merge, or when asked for a review report.
---

# Code Review

Use this skill when the task is review-first or when change risk is non-trivial.

## Workflow

1. Determine review scope:
- changed files and interfaces
- behavior that could regress
- migrations, auth, and data handling touchpoints

2. Review for high-impact risks first:
- correctness bugs and edge-case failures
- security issues and trust-boundary violations
- data-loss, irreversible actions, or broken migrations
- API contract or schema regressions

3. Review for maintainability second:
- unreadable or overly coupled code
- missing tests for key behavior
- inconsistent conventions that create future risk

4. Report findings with evidence:
- include file paths and line numbers
- describe user/system impact
- suggest concrete fix direction

## Required Output Format

For each finding include:
- severity (`critical`, `high`, `medium`, `low`)
- concise issue statement
- file reference
- rationale and expected impact

If no findings are present, state that explicitly and list residual risks or testing gaps.

## References

- Severity guidance: `references/severity-matrix.md`
- Review checklist: `references/review-checklist.md`
- False-positive filters: `references/false-positive-guards.md`
