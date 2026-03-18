# Settings Guide

Project settings are defined in `src/python_template/config/settings.py` using `pydantic-settings`.

## Quick Start

1. Copy env file:

```bash
cp .env.example .env
```

2. Use settings in code:

```python
from python_template.config.settings import get_settings

settings = get_settings()
print(settings.environment)
print(settings.log_level)
```

## Current Baseline Fields

From `Settings`:

- `environment` (`development` / `staging` / `production`)
- `log_level` (`TRACE|DEBUG|INFO|SUCCESS|WARNING|ERROR|CRITICAL`)
- `log_file`

From `.env.example`:

```env
ENVIRONMENT=development
LOG_LEVEL=INFO
LOG_FILE=logs/app.log
```

## Add New Settings

1. Add field in `Settings` with `Field(...)`
2. Add key to `.env.example`
3. Add validators if needed (`@field_validator`)

Example:

```python
database_url: str = Field(default="sqlite:///./app.db")
```

## Priority

1. Environment variables
2. `.env` file
3. Default field values
