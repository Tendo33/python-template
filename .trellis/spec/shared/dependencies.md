# Dependencies

Use this when adding or updating dependencies.

## Baseline

| Area | Tooling |
| --- | --- |
| Python runtime | Python 3.10+ |
| Python package manager | `uv` |
| Python quality | `ruff`, `mypy`, `pytest` |
| Python data/config | Pydantic v2, `pydantic-settings` |
| Python logging | `loguru` |
| Frontend package manager | `pnpm` |
| Frontend runtime | React 19, TypeScript strict mode |
| Frontend build | Vite 8 |
| Frontend styling | Tailwind CSS v4, shadcn/ui-style primitives |
| Frontend testing | Vitest, Testing Library, jsdom |

## Rules

- Check existing dependencies before adding a new one.
- Prefer the standard library or existing project helper when it is enough.
- Add FastAPI, SQLAlchemy, Alembic, auth, queue, or scheduler dependencies only
  when the target project has a real requirement.
- Do not expose backend-only secrets through `VITE_*` variables.
- Update docs and verification commands when a dependency changes project
  setup, build, or runtime behavior.

## Search Before Adding

```bash
rg "\"dependency-name\"" pyproject.toml frontend/package.json
rg "from dependency_name|import dependency_name" src tests scripts
rg "dependency-name" frontend/src
```
