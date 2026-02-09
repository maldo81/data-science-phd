# Non-Negotiables

These constraints apply in every project that adopts this documentation system.

## Security and Data Safety

- Never commit secrets, tokens, private keys, or production credentials.
- Treat `.env`, key files, and credential stores as restricted inputs.
- Review access controls and least-privilege assumptions before automation.

## PHI/PII Handling

- Treat PHI/PII as sensitive by default.
- Do not export, upload, or summarize sensitive records to external tools without explicit approval and de-identification.
- Preserve auditability for any sensitive-data access path.

## Migrations and Data Changes

- Prefer additive, reversible migrations.
- Do not run destructive data operations without an explicit backup + rollback path.
- Validate schema and data changes in non-production first.

## AI Action Boundaries

- AI may suggest, summarize, and prepare.
- AI must not perform irreversible actions silently.
- Human confirmation is required for destructive or high-risk changes.

## Documentation Discipline

- Canonical docs are updated before or alongside implementation.
- Project-specific intent lives in `.project/`.
- Shared conventions live in `.agents/`.
