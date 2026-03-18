# Codex Project Instructions

Use this file as the default project contract for Codex.

## Workflow

1. Understand request and constraints.
2. Propose concise implementation steps.
3. Implement with minimal, targeted edits.
4. Run verification commands before completion claims.

## Engineering Rules

- Follow `ai_docs/AI_TOOLING_STANDARDS.md`.
- Follow `ai_docs/BACKEND_STANDARDS.md` for backend API/service tasks.
- Prefer Python 3.10+ + uv + ruff + pytest for backend work.
- Keep functions small, typed, and testable.
- Handle errors explicitly; avoid silent failures.

## Tech Stack

### Backend

- Python 3.10+ / uv / ruff / pytest
- FastAPI + Pydantic v2 (when API is needed)
- SQLAlchemy + Alembic (when persistence is needed)

### Frontend

- **pnpm** (package manager)
- React + TypeScript + Vite
- Tailwind CSS + **shadcn/ui** (component library)

Layout convention:

- `frontend/src/app` — app shell and routing
- `frontend/src/features/*` — domain modules
- `frontend/src/components/ui` — shadcn/ui primitives and shared components
- `frontend/src/lib` — utilities and API wrappers

For backend-focused work, use:

```bash
cat .codex/skills/backend-engineering-playbook/SKILL.md
```

## Required Verification

Run what applies to the task:

```bash
# Backend
uv run ruff check src tests scripts
uv run ruff format --check src tests scripts
uv run mypy src
uv run pytest

# Frontend
pnpm --prefix frontend lint
pnpm --prefix frontend typecheck
pnpm --prefix frontend test
pnpm --prefix frontend build
```
