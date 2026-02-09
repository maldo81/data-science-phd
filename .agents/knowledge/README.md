# Knowledge Base

This folder is the scaffold for long-lived knowledge that should be reusable across sessions and (optionally) across projects.

## Purpose

Use this space to store:
- writing style guidance
- important reference documents
- research notes
- curated knowledge for retrieval
- decisions and rationale over time

## Structure

- `inbox/` - raw captures, unreviewed notes, quick dumps
- `curated/` - vetted evergreen knowledge
- `research/` - active research notes and findings
- `writing/` - authored drafts and communication patterns
- `style/` - writing voice/style guides and examples
- `sources/` - key documents and source indexes
- `retrieval/` - scaffold for vector-db/RAG metadata and ingestion plans
- `decision-log/` - dated decisions and why they were made

## Governance

1. Capture quickly in `inbox/`.
2. Curate regularly into `curated/` with clear titles and dates.
3. Keep source links/provenance in each curated note.
4. Move stale/duplicative notes out of active folders.

## Retrieval Layer (Scaffold Only)

`retrieval/` is intentionally scaffold-only right now. Use it later to define:
- embedding model choices
- chunking strategy
- metadata schema
- ingestion runbooks
- evaluation criteria for retrieval quality
