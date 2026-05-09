# Python + Vite Fullstack Spec

Use this spec for repositories based on Simon's Python template: a typed Python
package/backend foundation plus a React + Vite frontend. The backend may later
serve the Vite production build as static assets, but the template should not
pretend a full HTTP API or persistence layer exists before the project creates
one.

## Structure

### [Backend](./backend/index.md)

Python package and backend foundation patterns:

- [Package Structure](./backend/python-package.md)
- [Directory Structure](./backend/directory-structure.md)
- [Type Safety](./backend/type-safety.md)
- [Configuration and Logging](./backend/config-logging.md)
- [HTTP API When Added](./backend/http-api-when-added.md)
- [Database When Added](./backend/database-when-added.md)
- [Testing](./backend/testing.md)

### [Frontend](./frontend/index.md)

React + Vite frontend patterns:

- [Directory Structure](./frontend/directory-structure.md)
- [DESIGN.md Workflow](./frontend/design-md.md)
- [Components](./frontend/components.md)
- [Vite Static Mount](./frontend/vite-static-mount.md)
- [Quality](./frontend/quality.md)

### [Shared](./shared/index.md)

Cross-cutting project rules:

- [Code Quality](./shared/code-quality.md)
- [Dependencies](./shared/dependencies.md)
- [Current Architecture](./shared/architecture.md)
- [Project Structure](./shared/project-structure.md)
- [Naming and Paths](./shared/naming-and-paths.md)
- [Scripts](./shared/scripts.md)
- [Release](./shared/release.md)
- [Project Docs](./shared/project-docs.md)
- [Verification](./shared/verification.md)

### [Guides](./guides/index.md)

Thinking and handoff guides:

- [Task Flow](./guides/task-flow.md)
- [Pre-Implementation Checklist](./guides/pre-implementation-checklist.md)
- [Cross-Layer Thinking Guide](./guides/cross-layer-thinking-guide.md)
- [Review Checklist](./guides/review-checklist.md)

### [Common Issues / Pitfalls](./big-question/index.md)

Stack-specific debugging notes:

- [Generated Frontend Assets](./big-question/generated-frontend-assets.md)
- [Static Fallback vs API Routes](./big-question/static-fallback-vs-api-routes.md)
- [Settings Cache In Tests](./big-question/settings-cache-in-tests.md)

## Read Order

1. `shared/index.md`
2. `backend/index.md` before backend work
3. `frontend/index.md` before frontend work
4. `guides/pre-implementation-checklist.md` before non-trivial changes
5. `shared/verification.md` before claiming completion
6. `guides/review-checklist.md` before handoff

## Baseline Stack

- Python 3.10+
- `uv`
- `ruff`
- `mypy`
- `pytest`
- Pydantic v2 and `pydantic-settings`
- `loguru`
- React 19
- TypeScript strict mode
- Vite 8
- Tailwind CSS v4
- shadcn/ui-style primitives
- Vitest + Testing Library + jsdom

## Project Bias

- Keep changes small, typed, and explicit.
- Describe current implementation as current implementation. Put future API,
  service, repository, domain, and static-mount plans in future-expansion
  language unless they already exist.
- Prefer direct code over abstractions that only serve one call site.
- Update project docs when behavior, structure, scripts, adapters, public APIs,
  or verification commands change.
