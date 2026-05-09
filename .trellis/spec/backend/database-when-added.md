# Database When Added

The baseline Python template does not include a database. Use this only when the
target project adds persistence.

## Rules

- Choose the simplest persistence layer that supports the feature.
- Do not introduce repository abstractions before there is a persistence
  boundary to hide.
- Keep migrations and schema docs close to the database tooling.
- Validate external input before persistence.
- Do not log connection strings, credentials, or raw sensitive records.

## Boundaries

When persistence exists:

- Handlers should not know storage details.
- Service code may coordinate business flow.
- Repository/data-access code may own database queries.
- Models used for API responses should not be confused with database row types
  unless they are intentionally the same.

## Verification

Add integration tests when behavior depends on real database constraints,
migrations, transactions, or query semantics.
