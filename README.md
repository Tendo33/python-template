# Python Template

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Code style: ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)

一个面向 Python 3.10+ 的现代化工具库模板：
- `uv` 管理依赖
- `ruff` 负责 lint/format
- `mypy` 类型检查
- `pytest` 测试与覆盖率

## v0.2.0 Breaking Changes

`python_template.utils` 顶层导出已收敛为稳定核心 API。

旧写法需要迁移到子模块：
- `from python_template.utils import retry_decorator` -> `from python_template.utils.decorator_utils import retry_decorator`
- `from python_template.utils import chunk_list` -> `from python_template.utils.common_utils import chunk_list`
- `from python_template.utils import Context` -> `from python_template.utils.context import Context`
- `from python_template.utils import list_files` -> `from python_template.utils.file_utils import list_files`

## 快速开始

### 1) 安装依赖

```bash
uv sync --all-extras
```

### 2) 初始化环境变量

```bash
cp .env.example .env
```

默认配置最小化：

```env
ENVIRONMENT=development
LOG_LEVEL=INFO
LOG_FILE=logs/app.log
```

### 3) 运行质量检查

```bash
uv run ruff check src tests scripts
uv run ruff format --check src tests scripts
uv run mypy src
uv run pytest
```

## 导入约定

### 顶层稳定 API（推荐）

```python
from python_template.utils import (
    get_logger,
    setup_logging,
    get_settings,
    read_json,
    write_json,
    read_text_file,
    write_text_file,
    get_timestamp,
)
```

### 高级能力请从子模块导入

```python
from python_template.utils.decorator_utils import retry_decorator
from python_template.utils.common_utils import chunk_list
from python_template.utils.context import Context
```

## 常用示例

### 日志

```python
from python_template.utils import get_logger, setup_logging

setup_logging(level="INFO", log_file="logs/app.log")
logger = get_logger(__name__)
logger.info("service started")
```

### 配置

```python
from python_template.utils import get_settings

settings = get_settings()
print(settings.environment)
print(settings.log_level)
```

### 文件与 JSON

```python
from python_template.utils import read_json, write_json, read_text_file, write_text_file

write_text_file("hello", "data/hello.txt")
content = read_text_file("data/hello.txt")

write_json({"ok": True}, "data/config.json")
config = read_json("data/config.json", default={})
```

## 项目结构

```text
python-template/
├── src/python_template/
│   ├── models/
│   └── utils/
├── tests/
├── scripts/
├── doc/
├── pyproject.toml
└── README.md
```

## 维护脚本

- `python scripts/rename_package.py my_new_project`
- `python scripts/setup_pre_commit.py`
- `python scripts/update_version.py 0.2.0`
- `uv run python scripts/run_vulture.py --min-confidence 80`

## 文档

- `doc/SETTINGS_GUIDE.md`
- `doc/MODELS_GUIDE.md`
- `doc/SDK_USAGE.md`
- `doc/PRE_COMMIT_GUIDE.md`
- `doc/AI_TOOLING_STANDARDS.md`
- `doc/BACKEND_STANDARDS.md`

## 许可证

MIT，见 `LICENSE`。
