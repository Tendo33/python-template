# Codex Project Instructions

Use this file as the default project contract for Codex.

## Workflow

1. Understand the request and the affected parts of the repository.
2. Read `ai_docs/` before changing code or docs.
3. Make minimal, targeted changes.
4. Run relevant verification commands before claiming completion.
5. If behavior, structure, scripts, or workflows changed, update the docs in the same pass.

## Engineering Rules

- **Read `ai_docs/AI_TOOLING_STANDARDS.md` first.**
- Backend rules: `ai_docs/BACKEND_STANDARDS.md`
- Frontend rules: `ai_docs/FRONTEND_STANDARDS.md`
- Frontend design contract: `ai_docs/frontend_design/DESIGN_SYSTEM.md`
- Scripts guide: `ai_docs/SCRIPTS_GUIDE.md`
- Keep functions small, typed, and testable.
- Backend code should be concise, readable, and direct.
- Handle errors explicitly; avoid silent failure paths.
- Documentation must describe the current implementation, not aspirational structure.

## Tech Stack

### Backend

- Python 3.10+ / `uv` / `ruff` / `mypy` / `pytest`
- FastAPI + Pydantic v2 when API work is needed
- SQLAlchemy + Alembic when persistence is needed

### Frontend

- `pnpm`
- React + TypeScript + Vite
- Tailwind CSS + shadcn/ui

Current frontend starter layout:

- `frontend/src/app` — current app entry
- `frontend/src/components` — shared components
- `frontend/src/components/ui` — UI primitives
- `frontend/src/styles` — global styles and tokens
- `frontend/src/test` — test setup

Recommended expansion layout once the app grows:

- `frontend/src/features/*`
- `frontend/src/lib`
- `frontend/src/hooks`

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
