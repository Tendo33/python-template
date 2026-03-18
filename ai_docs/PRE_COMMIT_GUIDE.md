# Pre-commit Guide

Pre-commit runs quality checks automatically during `git commit`.

## Install Hooks

```bash
uv run pre-commit install
```

or use helper script:

```bash
python scripts/setup_pre_commit.py
```

## Common Commands

```bash
uv run pre-commit run --all-files
uv run pre-commit run
uv run pre-commit autoupdate
```

## Hooks in This Project

From `.pre-commit-config.yaml`:

- trailing whitespace / EOF fixes
- YAML/TOML/JSON checks
- merge-conflict and debug statement checks
- Ruff lint (`ruff`) and format (`ruff-format`)

## If a Commit Fails

- If hooks auto-fix files: run `git add -A` and commit again.
- If lint errors remain: fix manually and commit again.
