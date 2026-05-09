# Backend Directory Structure

Use this when adding backend files.

## Baseline Shape

```text
src/<package_name>/
├── config/          # Settings and configuration loading
├── contracts/       # Protocol interfaces
├── core/            # Runtime context helpers
├── models/          # Pydantic base and project models
├── observability/   # Logging setup and helpers
└── utils/           # Stable utility modules
tests/
scripts/
```

## Placement Rules

| New thing | Default location |
| --- | --- |
| Settings field or config helper | `src/<package_name>/config/` |
| Pydantic model intended for reuse | `src/<package_name>/models/` |
| Runtime context object/helper | `src/<package_name>/core/` |
| Protocol/interface | `src/<package_name>/contracts/` |
| Logging helper | `src/<package_name>/observability/` |
| General utility with 2+ real users | `src/<package_name>/utils/` |
| Maintenance script | `scripts/` |
| Python test | `tests/` |

## Conditional Directories

Add these only when the project actually needs them:

| Directory | Add when |
| --- | --- |
| `api/` | A real HTTP layer exists |
| `service/` | Business flow no longer fits cleanly in handlers/helpers |
| `repository/` | Persistence exists and needs a boundary |
| `domain/` | Domain rules are complex enough to stand apart |

Do not create empty architecture folders as future signals.
