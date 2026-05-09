# Naming And Paths

## Package And Import Rules

- Import from the package name, never from `src`.
- Correct: `from python_template.config.settings import get_settings`
- Incorrect: `from src.python_template.config.settings import get_settings`
- Stable public imports should prefer `python_template` package-level exports or
  stable submodules.

## Path Naming Rules

- Python files and directories use `snake_case`.
- Frontend files and directories follow the current starter conventions.
- Trellis specs live under `.trellis/spec/`.

## Root Entrypoint Policy

- Root entrypoints are `AGENTS.md` and `CLAUDE.md`.
- Root entrypoints must stay thin and link into `.trellis/spec/`.
- Root entrypoints must only link to files that exist.
