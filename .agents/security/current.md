# Security - Current Baseline

Use this file as the project security baseline summary.

Update this per project with concrete implementation references.

## Minimum Baseline

- Authentication and session controls are defined and documented.
- Authorization model is explicit (role-based and/or attribute-based).
- Secrets are kept out of source control and prompt logs.
- Destructive operations require explicit confirmation.
- Sensitive-data flows are mapped and auditable.

## Verification Checklist

1. Confirm where auth checks happen.
2. Confirm where permission checks happen.
3. Confirm how secrets are injected at runtime.
4. Confirm logging does not leak sensitive data.
5. Confirm backup and rollback expectations for risky changes.
