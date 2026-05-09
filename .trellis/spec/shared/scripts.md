# Scripts

## Current Scripts

The repository provides these maintenance scripts:

- `rename_package.py`: rename the Python package and project name.
- `update_version.py`: synchronize version numbers.
- `setup_pre_commit.py`: install, update, or test pre-commit hooks.
- `run_vulture.py`: scan for potentially unused Python code.
- `generate_release_notes.py`: generate release notes.

## When To Use Which Script

### Rename Package And Project

Use `scripts/rename_package.py` immediately after creating a new repository from
the template.

It renames `src/python_template/` and updates source, docs, config, and frontend
text references. It also updates `frontend/package.json` `name` and
`frontend/index.html` `<title>`.

### Update Version

Use `scripts/update_version.py` before release or when synchronizing versions.

It updates:

- `pyproject.toml`
- `src/python_template/__init__.py`
- `frontend/package.json`

### Initialize Pre-Commit

Use `scripts/setup_pre_commit.py` to install, update, or validate hooks.

The repository uses `.pre-commit-config.yaml`; current hooks cover formatting,
basic config checks, and Ruff.

### Scan Unused Python Code

Use `scripts/run_vulture.py` for a lightweight dead-code scan before or after
refactors. It does not replace tests or human review.

### Generate Release Notes

Use `scripts/generate_release_notes.py` for release text. It reads tags,
changelog, and commits. With a model API key it can generate a summary; without
one it falls back to deterministic highlights.

## Verification

Use [verification.md](./verification.md) for task-specific and docs checks.
