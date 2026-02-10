---
name: feature-delivery
description: Plan and deliver features using a structured Plan -> Implement -> Validate loop. Use for medium-to-large changes requiring clarification, design choices, and test strategy.
---

# Feature Delivery

Use this skill when a request requires multi-step implementation decisions.

## Delivery Loop

1. Clarify intent
- goal, success criteria, non-goals
- constraints, dependencies, and risk boundaries

2. Map impact
- affected files and interfaces
- documentation and migration impact
- compatibility considerations

3. Choose implementation slice
- smallest coherent increment
- explicit acceptance checks
- rollback or mitigation path

4. Implement with discipline
- keep edits minimal and scoped
- update docs with behavior changes
- avoid hidden side effects

5. Validate
- run targeted tests/checks
- verify acceptance criteria
- capture follow-up tasks explicitly

## Artifacts

- Use the project PRD in .project/specs/prd.md for project intent.
- For each non-trivial feature, create or update a short design note in .project/specs/.

## References

- Change spec template: `references/change-spec-template.md`
- Test planning checklist: `references/test-planning-checklist.md`
