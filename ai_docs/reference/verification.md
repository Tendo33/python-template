# Verification Reference

## Purpose

本文件是仓库验证命令的唯一详细事实源。其他 AI 文档和根入口文件只链接这里，不重复抄写完整命令。

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

`Full stack` 表示本地完整验证，包含前端测试。

## CI gate

GitHub Actions 当前以 `.github/workflows/ci.yml` 为准，实际门禁运行：

```bash
uv run ruff check src tests scripts
uv run ruff format --check src tests scripts
uv run mypy src
uv run pytest
pnpm --prefix frontend lint
pnpm --prefix frontend typecheck
pnpm --prefix frontend build
```

当前 CI 不运行 `pnpm --prefix frontend test`，所以前端测试仍是本地应主动执行的检查项。

## Docs and links

```powershell
@'
from pathlib import Path
import re
import sys

docs = [*Path("ai_docs").rglob("*.md"), Path("README.md"), Path("AGENTS.md"), Path("CLAUDE.md")]
pattern = re.compile(r"\[[^\]]+\]\(([^)#]+)")
missing = []

for doc in docs:
    text = doc.read_text(encoding="utf-8")
    for rel in pattern.findall(text):
        if "://" in rel or rel.startswith("#"):
            continue
        target = (doc.parent / rel).resolve()
        if not target.exists():
            missing.append(f"{doc}: {rel}")

if missing:
    print("\\n".join(missing))
    sys.exit(1)
'@ | uv run python -
```

## Usage rule

- backend-only 任务跑 `Backend`
- frontend-only 任务跑 `Frontend`
- 同时改前后端、脚本时跑 `Full stack`
- 改 `ai_docs/`、`README.md`、`AGENTS.md` 或 `CLAUDE.md` 时，先跑对应任务的本地验证，再额外跑 `Docs and links`
- 判断自动化门禁时看 `CI gate`，不要把它和 `Full stack` 视为同一组检查
