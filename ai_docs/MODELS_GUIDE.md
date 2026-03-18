# Models Guide

Rules for Pydantic models in this repository.

## Core Rules

1. Model classes must live under `src/python_template/models/`.
2. Prefer the project `BaseModel` from `python_template.models.base`.
3. Use Pydantic v2 APIs (`model_config`, `model_dump`, `model_validate`).
4. Export public models via `src/python_template/models/__init__.py`.

## Current Structure

```text
src/python_template/models/
├── base.py        # BaseModel, TimestampMixin
├── examples.py    # User, ApiResponse, PaginatedResponse, ConfigModel
└── __init__.py    # public exports
```

## Field and Validation Conventions

- Use explicit type hints for all fields
- Use `Field(...)` for constraints and descriptions
- Use `@field_validator` for single-field checks
- Use `@model_validator` for cross-field checks
- Use `default_factory` for mutable defaults

## Serialization / Validation APIs

- `model.model_dump()`
- `model.model_dump_json()`
- `Model.model_validate(data)`
- `Model.model_validate_json(raw_json)`

Avoid old v1-style `.dict()` / `.json()` / `class Config`.
