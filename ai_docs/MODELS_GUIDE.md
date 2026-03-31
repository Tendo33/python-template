# Models Guide

这个仓库的模型约定基于 Pydantic v2，模型文件位于 `src/python_template/models/`。

## 当前结构

```text
src/python_template/models/
├── base.py        # BaseModel, TimestampMixin
├── examples.py    # User, ApiResponse, PaginatedResponse, ConfigModel
└── __init__.py    # 公共导出面
```

## 当前公共导出

```python
from python_template.models import (
    ApiResponse,
    BaseModel,
    ConfigModel,
    PaginatedResponse,
    TimestampMixin,
    User,
)
```

## 核心规则

1. 新模型优先放在 `src/python_template/models/` 下
2. 优先继承项目自己的 `BaseModel`
3. 使用 Pydantic v2 API：
   - `model_config`
   - `model_dump()`
   - `model_dump_json()`
   - `model_validate()`
   - `model_validate_json()`
4. 对外可用的模型要在 `src/python_template/models/__init__.py` 中导出

## `BaseModel`

项目基础模型定义在 `base.py`，当前默认行为：

- `populate_by_name=True`
- `validate_assignment=True`
- `extra="ignore"`
- 提供 `model_dump_json_safe()`，直接输出 JSON-safe dict

示例：

```python
from python_template.models import BaseModel


class Payload(BaseModel):
    ok: bool
```

## `TimestampMixin`

`TimestampMixin` 默认提供 UTC 时间戳：

- `created_at`
- `updated_at`

适合给需要审计字段的模型复用。

## 示例模型

当前模板附带这些示例模型：

- `User`
- `ApiResponse[T]`
- `PaginatedResponse[T]`
- `ConfigModel`

它们主要用于演示：

- 字段约束
- `@field_validator`
- 泛型响应模型
- 基础配置模型写法

## 字段和校验建议

- 所有字段都写明确类型
- 需要约束时使用 `Field(...)`
- 单字段校验用 `@field_validator`
- 跨字段校验用 `@model_validator`
- 可变默认值用 `default_factory`

## 扩展建议

当项目进入业务开发阶段：

- 示例模型可以保留作为参考
- 新的业务模型建议按领域拆成独立文件
- 如果某类模型已成为公开 API，记得更新 `__init__.py` 和相关文档
