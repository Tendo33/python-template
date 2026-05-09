# Verification

This file is the repository's verification command source of truth.

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

## Full Stack

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

`Full Stack` means local complete verification, including frontend tests.

## CI Gate

GitHub Actions currently use `.github/workflows/ci.yml`. The effective gate is:

```bash
uv run ruff check src tests scripts
uv run ruff format --check src tests scripts
uv run mypy src
uv run pytest
pnpm --prefix frontend lint
pnpm --prefix frontend typecheck
pnpm --prefix frontend build
```

CI does not currently run `pnpm --prefix frontend test`, so frontend tests remain
a local required check.

## Package Build

```bash
uv build --out-dir /tmp/python-template-build --clear
tar -tf /tmp/python-template-build/python_template-*.tar.gz \
  | rg '(^|/)(node_modules|dist|\.next|\.vite|\.trellis|\.agents|\.claude|\.codex|ai_docs)(/|$)' \
  && exit 1 || true
python3 -m zipfile -l /tmp/python-template-build/python_template-*-py3-none-any.whl
```

The wheel should contain only the Python package and package metadata. The
sdist may contain template source files, but it must not contain installed
frontend dependencies, build output, Trellis runtime state, platform adapter
directories, or removed documentation trees.

## Docs And Links

```bash
uv run python - <<'PY'
from pathlib import Path
import re
import sys

docs = [
    *Path(".trellis/spec").rglob("*.md"),
    Path("README.md"),
    Path("AGENTS.md"),
    Path("CLAUDE.md"),
]
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
    print("\n".join(missing))
    sys.exit(1)
PY
```

## Rule

- Backend-only changes run backend checks.
- Frontend-only changes run frontend checks.
- Cross-boundary, scripts, or template-documentation changes run full stack.
- Docs-only changes run `Docs And Links`.
- Release-preparation changes run `Full Stack`, `Docs And Links`, and
  `Package Build`.
- Changes to `.trellis/spec/`, `README.md`, `AGENTS.md`, or `CLAUDE.md` must run
  `Docs And Links` in addition to any task-specific checks.
- Use `CI Gate` when judging automated gate behavior; do not treat it as the
  same thing as `Full Stack`.
