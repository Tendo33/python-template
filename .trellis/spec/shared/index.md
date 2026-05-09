# Shared Index

This spec is the primary documentation source for `python-template`.

## Repository Shape

```text
src/<package_name>/      # Python package
tests/                   # Python tests
scripts/                 # Maintenance and release scripts
frontend/                # React + Vite starter
.trellis/spec/           # Trellis development specs and project facts
```

## Source of Truth

- Start with this file and [../guides/index.md](../guides/index.md).
- Use [architecture.md](./architecture.md) for current project scope.
- Use [project-structure.md](./project-structure.md) for current paths.
- Use [naming-and-paths.md](./naming-and-paths.md) for import and naming rules.
- Use [verification.md](./verification.md) for commands.

## Documentation Files

| File | Description | When to Read |
| --- | --- | --- |
| [code-quality.md](./code-quality.md) | Mandatory quality rules | Always |
| [dependencies.md](./dependencies.md) | Stack and dependency constraints | Adding or updating dependencies |
| [architecture.md](./architecture.md) | Current project truth | Understanding scope |
| [project-structure.md](./project-structure.md) | Current repository layout | Adding or moving files |
| [naming-and-paths.md](./naming-and-paths.md) | Import, naming, and root entrypoint rules | Changing paths or docs |
| [scripts.md](./scripts.md) | Maintenance scripts | Updating scripts or template tasks |
| [release.md](./release.md) | Release flow | Preparing releases |
| [project-docs.md](./project-docs.md) | Trellis documentation conventions | Changing docs or project structure |
| [verification.md](./verification.md) | Baseline verification commands | Before completion |

## Core Rules

- No untyped public Python APIs.
- No `Any` in new Python code unless the boundary is genuinely dynamic.
- No frontend `any` in new TypeScript code.
- No secrets in logs or Vite public environment variables.
- Generated frontend build artifacts stay out of git unless the target project
  explicitly stores static output.

## Working Rules

- Do not import Python modules through `src.<package_name>...`.
- Do not document future service, repository, database, or HTTP layers as
  already implemented.
- When adding a new public import surface, update package exports and tests.
- Keep frontend and backend contracts explicit. If the frontend calls a backend
  endpoint, document the request, response, and error shape.
- Do not commit generated frontend build artifacts unless the target project
  explicitly serves checked-in static files.
