# Settings Guide

项目配置定义在 `src/python_template/config/settings.py`，基于 `pydantic-settings`。

## Quick Start

### 1. 复制环境变量文件

```bash
cp .env.example .env
```

### 2. 在代码中读取配置

```python
from python_template.config.settings import get_settings

settings = get_settings()
print(settings.environment)
print(settings.log_level)
print(settings.get_log_file_path())
```

## 当前基线字段

`Settings` 当前只保留最小运行时配置：

| 字段 | 含义 | 默认值 |
| :--- | :--- | :--- |
| `environment` | 运行环境，支持 `development` / `staging` / `production` | `development` |
| `log_level` | 日志级别 | `INFO` |
| `log_file` | 日志文件路径 | `logs/app.log` |

对应 `.env.example`：

```env
ENVIRONMENT=development
LOG_LEVEL=INFO
LOG_FILE=logs/app.log
```

## 校验规则

- `environment` 只能是 `development`、`staging`、`production`
- `log_level` 会自动转成大写，并限制在：
  - `TRACE`
  - `DEBUG`
  - `INFO`
  - `SUCCESS`
  - `WARNING`
  - `ERROR`
  - `CRITICAL`

## 配置优先级

从高到低：

1. 环境变量
2. `.env`
3. 字段默认值

`Settings` 的 `model_config` 还包含这些行为：

- `env_file=".env"`
- `env_file_encoding="utf-8"`
- `env_nested_delimiter="_"`
- `case_sensitive=False`
- `extra="ignore"`

## 单例与重载

### `get_settings()`

- 使用 `@lru_cache`
- 在一个进程内默认返回同一个 `Settings` 实例

### `reload_settings(env_file=...)`

- 会先清空 `get_settings()` 缓存
- 可用于测试场景下加载临时 `.env`

示例：

```python
from pathlib import Path

from python_template.config.settings import reload_settings

settings = reload_settings(env_file=Path(".env.test"))
```

## 路径辅助方法

### `get_project_root()`

从 `src/<package>/config/settings.py` 反推项目根目录。

### `get_log_file_path()`

- 如果 `log_file` 已经是绝对路径，原样返回
- 如果是相对路径，会拼接到项目根目录下

## 添加新配置字段

1. 在 `Settings` 里新增字段
2. 使用 `Field(...)` 补充默认值、约束和说明
3. 需要时增加 `@field_validator`
4. 在 `.env.example` 里补对应变量
5. 如果文档或 README 中提到相关运行方式，一并更新

示例：

```python
from pydantic import Field

database_url: str = Field(
    default="sqlite:///./app.db",
    description="Database connection URL",
)
```
