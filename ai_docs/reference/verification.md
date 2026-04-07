# Verification Reference

## Purpose

本文件是仓库验证命令的唯一详细事实源。其他 AI 文档和 adapter 只链接这里，不重复抄写命令。

## Backend

```bash
uv run ruff check src tests scripts
uv run ruff format --check src tests scripts
uv run mypy src
uv run pytest
```

## Frontend

```bash
pnpm --prefix frontend lint
pnpm --prefix frontend typecheck
pnpm --prefix frontend test
pnpm --prefix frontend build
```

## Full stack

```bash
uv run ruff check src tests scripts
uv run ruff format --check src tests scripts
uv run mypy src
uv run pytest
pnpm --prefix frontend lint
pnpm --prefix frontend typecheck
pnpm --prefix frontend test
pnpm --prefix frontend build
```

## Docs and adapter maintenance

```bash
uv run python scripts/check_ai_docs.py
uv run python scripts/sync_ai_adapters.py --check
```

## Usage rule

- backend-only 任务跑 `Backend`
- frontend-only 任务跑 `Frontend`
- 同时改前后端、文档系统、adapter、脚本时跑 `Full stack`
- 改 `ai_docs/` 或 adapter 时额外跑 `Docs and adapter maintenance`
