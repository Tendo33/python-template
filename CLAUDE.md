# Claude Code Project Instructions

Use this file as the default project contract for Claude Code.

## Workflow

1. Confirm scope and assumptions.
2. Read `ai_docs/` before changing code or docs.
3. Implement the smallest safe change set.
4. Verify results with project commands.
5. Update docs whenever behavior, workflows, scripts, or public APIs change.

## Engineering Rules

- **Read `ai_docs/AI_TOOLING_STANDARDS.md` first.**
- Backend rules: `ai_docs/BACKEND_STANDARDS.md`
- Frontend rules: `ai_docs/FRONTEND_STANDARDS.md`
- Frontend design contract: `ai_docs/frontend_design/DESIGN_SYSTEM.md`
- Scripts guide: `ai_docs/SCRIPTS_GUIDE.md`
- Keep code typed, readable, and modular.
- Backend code should stay concise and easy to scan.
- Preserve existing project conventions unless asked to change them.
- Documentation should reflect current reality, not planned structure.

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

- `frontend/src/app`
- `frontend/src/components`
- `frontend/src/components/ui`
- `frontend/src/styles`
- `frontend/src/test`

Recommended expansion layout once the app grows:

- `frontend/src/features/*`
- `frontend/src/lib`
- `frontend/src/hooks`

For backend-focused work, use:

```bash
cat .claude/skills/backend-engineering-playbook/SKILL.md
```

## Required Verification

Run relevant checks before completion:

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
