# Manual Skill Eval Checklist

Use this when adding or modifying skills without paid API eval pipelines.

## Goal

Verify that prompts route to the expected skill and that instructions are followed.

## Steps

1. Start a fresh agent session.
2. Run 3-5 prompt variants per changed skill.
3. Confirm the expected skill is loaded.
4. Confirm referenced files are loaded only when needed.
5. Confirm response quality and safety boundaries.

## Prompt Matrix Template

- Skill: `<skill-name>`
  - Prompt A:
  - Prompt B:
  - Prompt C:
  - Expected load behavior:
  - Actual result:

## Pass Criteria

- Triggering prompts load the intended skill.
- Non-triggering prompts do not force irrelevant skill loads.
- No unsafe or irreversible behavior is suggested without confirmation.
