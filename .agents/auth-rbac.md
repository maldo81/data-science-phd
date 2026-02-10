# Auth and RBAC Baseline

This document captures reusable RBAC expectations.

## Core Principles

- Separate identity (authentication) from permission decisions (authorization).
- Enforce least privilege by default.
- Keep role definitions explicit and reviewable.
- Require server-side checks even if UI hides actions.

## Recommended Model

1. Define user or actor categories.
2. Define roles or capabilities with explicit boundaries.
3. Map sensitive actions to required capabilities.
4. Add audit trails for privileged actions.
5. Document escalation and admin scopes.

## Project-Specific Additions

Each project should add:
- role matrix
- route/resource protection map
- provisioning/deprovisioning workflow
- emergency access policy
