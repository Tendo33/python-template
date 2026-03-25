# Backend Development Standards

This document defines the default backend engineering rules for this template.

## Default Stack

- Python 3.10+
- FastAPI (when HTTP API is needed)
- Pydantic v2
- SQLAlchemy + Alembic (when persistence is needed)
- `uv` + `ruff` + `pytest`

## Readability First

Backend code should be concise, easy to understand, and cleanly structured.

- Prefer simple, direct solutions over clever abstractions.
- Keep functions focused and easy to scan.
- Avoid unnecessary indirection, deep nesting, and speculative generalization.
- Name things by intent so the business flow is obvious from the code.

## Layered Architecture

Use clear boundaries:

- `api`: routes, request/response schema, auth guards
- `service`: business use cases, orchestration
- `repository`: DB/storage access
- `domain`: pure business rules and types

Rules:

- Keep handlers thin.
- Do not mix SQL/session details into service logic.
- Keep service logic testable without HTTP/bootstrap.
- Keep each layer easy to follow; if a helper or abstraction does not improve clarity, do not introduce it.

## API Conventions

- Use versioned prefix (e.g. `/api/v1`)
- Define request/response with Pydantic models
- Return structured error payloads with stable error codes
- Support pagination/filter/sort for list endpoints

## Configuration and Security

- Use `pydantic-settings`
- Read secrets from env vars only
- Do not commit real secrets
- Avoid logging tokens/passwords/PII
- Validate and sanitize external input

## Data and Transactions

- Define explicit transaction boundaries for write paths
- Validate input before persistence
- Use migrations for schema changes
- Keep repository methods narrow and purpose-driven

## Testing Strategy

- Unit tests: domain/service logic and edge cases
- Integration tests: repository and API flow checks
- Add regression test for each bug fix

## Done Criteria (Backend)

- behavior implemented as requested
- relevant tests pass
- lint/format checks pass
- docs/migrations updated when needed

Recommended checks:

```bash
uv run ruff check src tests scripts
uv run ruff format --check src tests scripts
uv run mypy src
uv run pytest
```
