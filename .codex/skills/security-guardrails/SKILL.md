---
name: security-guardrails
description: Apply secure-by-default checks when changes touch authentication, authorization, secrets, untrusted input, or sensitive data flows.
---

# Security Guardrails

Use this skill whenever code or docs affect security posture.

## Security Review Steps

1. Identify trust boundaries
- user input, external APIs, file uploads, background jobs
- admin-only versus user-level actions

2. Validate controls
- authentication and authorization checks
- least-privilege access paths
- explicit confirmation for destructive actions

3. Check common vulnerability classes
- command injection
- SQL/ORM misuse
- XSS and unsafe HTML rendering
- insecure deserialization
- secret leakage in code/logs

4. Confirm data protections
- sensitive data minimization
- retention and logging discipline
- environment/config separation for secrets

## Output

Report only concrete findings with evidence and practical remediation.

## References

- Threat checklist: `references/threat-checklist.md`
- Sensitive data handling baseline: `references/sensitive-data.md`
- Common coding pitfalls: `references/common-pitfalls.md`
