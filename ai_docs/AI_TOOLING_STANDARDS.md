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

## README standard for template-based projects

When a new project is created from this template, treat `README.md` as a product-facing entry page rather than a plain file index.

Required structure:

1. A clear title and one short subtitle that explains what the project is and who it is for.
2. A first-screen action area with quick navigation links or badge-style buttons.
3. A table of contents near the top for fast scanning.
4. A `Quick Start` section with the shortest path from clone to first successful run.
5. A `Use This Template` or equivalent setup section for projects generated from this repository.
6. Screenshot placeholders or real screenshots placed early in the README.
7. A project structure section that helps new contributors orient quickly.
8. Verification commands, release workflow, and links to `ai_docs/`.

Writing rules:

- Write for humans first. Use natural, direct language and avoid inflated or AI-sounding phrasing.
- Prefer short paragraphs, concrete statements, and copyable commands.
- Show the fastest happy path before the full reference material.
- Keep sections skimmable. A reader should understand the project in less than a minute.
- Borrow layout ideas from strong open source READMEs when useful, but do not copy their wording or project framing.
- When screenshots are not ready yet, leave explicit placeholders with recommended filenames so later projects can fill them in quickly.

For any project created from this template, keep this README style unless the user explicitly asks for a different documentation style.

## Backend Baseline

- Python 3.10+
- `uv` for dependency and command execution
- `ruff` for lint + format
- `pytest` for tests
- If API is needed: FastAPI + Pydantic v2 + SQLAlchemy + Alembic
- Backend code must stay concise, readable, and clean. Prefer straightforward designs over clever abstractions, and avoid unnecessary indirection.

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
