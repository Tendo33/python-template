# AI Tooling Standards

This folder is the single source of truth for AI assistants in this repository.

Before starting any implementation task, read `ai_docs/AI_TOOLING_STANDARDS.md` and then open the relevant specialized docs.

## ai_docs Index

| Document | Purpose |
| :--- | :--- |
| `AI_TOOLING_STANDARDS.md` | Global AI workflow and quality gates |
| `BACKEND_STANDARDS.md` | Backend architecture and API rules |
| `FRONTEND_STANDARDS.md` | Frontend stack and implementation conventions |
| `frontend_design/DESIGN_SYSTEM.md` | **Frontend Design System** — 5-layer UI/UX spec (principles → tokens → components → patterns → screens). Read before any frontend UI work. Update before any UI refactor. |
| `SCRIPTS_GUIDE.md` | Maintenance scripts (`rename_package`, `update_version`, etc.) |
| `MODELS_GUIDE.md` | Pydantic model conventions |
| `SETTINGS_GUIDE.md` | Configuration management with pydantic-settings |
| `SDK_USAGE.md` | `src` layout import/use conventions |
| `PRE_COMMIT_GUIDE.md` | Git hook quality checks |

## Shared Workflow

1. Confirm goal and assumptions before coding.
2. Make minimal, reviewable changes.
3. Follow project conventions from `ai_docs/`.
4. Verify before claiming completion.

## Backend Baseline

- Python 3.10+
- `uv` for dependency and command execution
- `ruff` for lint + format
- `pytest` for tests
- If API is needed: FastAPI + Pydantic v2 + SQLAlchemy + Alembic

Backend verification:

```bash
uv run ruff check src tests scripts
uv run ruff format --check src tests scripts
uv run mypy src
uv run pytest
```

See `ai_docs/BACKEND_STANDARDS.md` for details.

## Frontend Baseline

Fixed stack unless user explicitly overrides:

- `pnpm`
- React + TypeScript + Vite
- Tailwind CSS + shadcn/ui

Frontend verification:

```bash
pnpm --prefix frontend lint
pnpm --prefix frontend typecheck
pnpm --prefix frontend test
pnpm --prefix frontend build
```

See `ai_docs/FRONTEND_STANDARDS.md` for details.

## Definition of Done

A task is done only when:

- requested behavior is implemented,
- relevant checks pass,
- edge cases are addressed,
- docs/config are updated if behavior or workflow changed.
