# Current Architecture

## Current Truth

This repository is an AI-collaboration-oriented Python + frontend template. It
is not a full business application scaffold.

It currently provides:

- Python package infrastructure: configuration, logging, context helpers,
  protocols, models, and utilities.
- React + Vite frontend starter.
- Repository maintenance scripts and release workflow.
- Root AI entrypoints: `AGENTS.md` and `CLAUDE.md`.
- Trellis development specs under `.trellis/spec/`.

It currently does not include:

- A complete HTTP API, service, repository, or domain layer.
- Database schema, migrations, or persistence.
- A real business full-stack demo.
- Multi-page frontend routing or complex frontend state architecture.

## Subsystems

- Python package/backend guidance: [../backend/index.md](../backend/index.md)
- Frontend guidance: [../frontend/index.md](../frontend/index.md)
- Scripts: [scripts.md](./scripts.md)
- Release: [release.md](./release.md)

## Shared References

- Project structure: [project-structure.md](./project-structure.md)
- Naming and paths: [naming-and-paths.md](./naming-and-paths.md)
- Verification: [verification.md](./verification.md)
