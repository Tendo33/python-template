# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.2.2] - 2026-04-07

### Changed
- Refreshed `README.md`, `ai_docs/`, `AGENTS.md`, and `CLAUDE.md` to match the current repository layout, public APIs, frontend starter, script behavior, and release workflow.
- Replaced the placeholder-heavy frontend design system with a concrete description of the current starter UI, token values, components, and extension rules.

## [0.2.1] - 2026-03-18

### Changed
- Documentation refreshed to match current repository state, including unified `ai_docs/` guidance and script usage docs.
- README updated with frontend setup and verification commands (`pnpm --prefix frontend ...`) and corrected release workflow path.
- `rename_package.py` now covers frontend assets/config and AI-tooling config files when renaming project/package identifiers.
- `update_version.py` now updates backend + frontend version targets and auto-detects package directory under `src/`.
- **Breaking:** refactored module layout by moving `setting/context/protocols/logger_util` out of `utils` into `config/settings`, `core/context`, `contracts/protocols`, and `observability/log_config`; removed legacy import paths.
- Simplified default app configuration: removed `APP_NAME`/`APP_VERSION` and kept only `ENVIRONMENT` (dropped `DEBUG`) from baseline runtime mode env vars.
- Unified retry implementation by reusing `decorator_utils` retry internals from `common_utils`.
- Removed `Settings/get_settings/reload_settings` re-exports from `common_utils` to reduce cross-module coupling.
- Unified JSON write contracts so `write_json` and `async_write_json` both return `bool`.
- Unified current date/time defaults to UTC in `date_utils` (`get_current_date`/`get_current_time`), with `use_utc=False` for local time.

## [0.2.0] - 2026-02-20

### Changed
- **Breaking:** narrowed `python_template.utils` top-level exports to a stable core API surface.
- Moved non-core utility imports to submodule-based usage in tests and documentation.
- Enforced test coverage gate with `--cov-fail-under=80`.
- Removed duplicated dependency declarations by dropping `[dependency-groups]`.
- Tightened sdist exclusions to keep assistant/tooling and local artifacts out of release packages.
- Removed unused CLI placeholder configuration from project metadata.

### Added
- Async decorators support (`async_timing_decorator`, `async_retry_decorator`, `async_catch_exceptions`)

## [0.1.0] - 2026-01-20

### Added
- Initial release of Python Template
- **Utils Module**
  - `logger_util`: Loguru-based logging configuration and management
  - `json_utils`: JSON read/write and serialization utilities
  - `file_utils`: File system operations (sync and async)
  - `decorator_utils`: Common decorators (timing, retry, catch_exceptions, etc.)
  - `date_utils`: Date and time manipulation utilities
  - `common_utils`: General utility functions (list chunking, dict operations, etc.)
  - `setting`: Pydantic Settings-based configuration management
  - `context`: Thread-safe runtime context storage
- **Models Module**
  - Base Pydantic models for data validation
- **Scripts**
  - `rename_package.py`: Package renaming utility
  - `setup_pre_commit.py`: Git hooks configuration
  - `update_version.py`: Version update utility
  - `run_vulture.py`: Dead code detection
- **Documentation**
  - Settings guide
  - Models guide
  - SDK usage guide
  - Pre-commit guide
- **Configuration**
  - `pyproject.toml` with full project metadata
  - Ruff linting and formatting configuration
  - Pytest and coverage configuration
  - Pre-commit hooks configuration

[Unreleased]: https://github.com/Tendo33/python-template/compare/v0.2.2...HEAD
[0.2.2]: https://github.com/Tendo33/python-template/compare/v0.2.1...v0.2.2
[0.2.1]: https://github.com/Tendo33/python-template/compare/v0.2.0...v0.2.1
[0.2.0]: https://github.com/Tendo33/python-template/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/Tendo33/python-template/releases/tag/v0.1.0
