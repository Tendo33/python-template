# Python Template

[![CI](https://github.com/yourusername/python-template/workflows/CI/badge.svg)](https://github.com/yourusername/python-template/actions)
[![codecov](https://codecov.io/gh/yourusername/python-template/branch/main/graph/badge.svg)](https://codecov.io/gh/yourusername/python-template)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Code style: ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)

一个现代化的 Python 工具库模板，集成了常用的工具函数和最佳实践。

## ✨ 特性

- 🛠 **丰富的工具集**：包含日期、文件、JSON、装饰器等常用工具模块
- 📝 **强大的日志系统**：基于 [loguru](https://github.com/Delgan/loguru) 的预配置日志管理
- ⚙️ **配置管理**：基于 [pydantic-settings](https://github.com/pydantic/pydantic-settings) 的类型安全配置
- 🔄 **上下文管理**：线程安全的运行时上下文存储
- 🚀 **现代化工具链**：使用 `uv` 进行包管理，`ruff` 进行代码检查

## 📦 安装

使用 [uv](https://github.com/astral-sh/uv) 安装：

```bash
# 安装依赖
uv sync

# 以开发模式安装
uv pip install -e .
```

## 🚀 快速开始

### 1. 日志工具 (Logger)

```python
from python_template.utils import get_logger, setup_logging

# 配置日志
setup_logging(level="DEBUG", log_file="logs/app.log")

logger = get_logger(__name__)

logger.info("这是一条信息日志")
logger.error("这是一条错误日志")
logger.debug("这是一条调试日志")
```

### 2. 装饰器工具 (Decorators)

```python
from python_template.utils import timing_decorator, retry_decorator, log_calls

# 计时装饰器
@timing_decorator
def heavy_process():
    # ... 耗时操作
    pass

# 重试装饰器
@retry_decorator(max_retries=3, delay=1.0)
def unstable_network_call():
    # ... 可能失败的网络请求
    pass

# 自动日志记录
@log_calls(log_args=True, log_result=True)
def calculate(a, b):
    return a + b
```

### 3. 文件操作 (File Utils)

```python
from python_template.utils import read_text_file, write_text_file, ensure_directory

# 确保目录存在
ensure_directory("data/output")

# 写入文件 (自动创建父目录)
write_text_file("Hello World", "data/output/test.txt")

# 读取文件
content = read_text_file("data/output/test.txt", default="Default Content")
```

### 4. JSON 处理 (JSON Utils)

```python
from python_template.utils import read_json, write_json

data = {"name": "test", "value": 123}

# 写入 JSON
write_json(data, "config.json", indent=2)

# 读取 JSON
config = read_json("config.json", default={})
```

### 5. 日期时间 (Date Utils)

```python
from python_template.utils import get_timestamp, format_datetime, get_current_time

# 获取当前 ISO 时间戳
ts = get_timestamp()

# 获取当前时间字符串
now = get_current_time()

# 格式化日期
formatted = format_datetime(datetime.now(), format_str="%Y-%m-%d")
```

## 📁 项目结构

```
python-template/
├── src/python_template/
│   ├── utils/              # 核心工具包
│   │   ├── common_utils.py    # 通用工具 (列表/字典操作, 验证等)
│   │   ├── date_utils.py      # 日期时间处理
│   │   ├── file_utils.py      # 文件系统操作
│   │   ├── json_utils.py      # JSON 读写与序列化
│   │   ├── decorator_utils.py # 常用装饰器
│   │   ├── logger_util.py     # 日志配置
│   │   ├── setting.py         # 应用配置管理
│   │   └── context.py         # 上下文管理
│   └── models/             # 数据模型 (预留)
├── tests/                  # 测试用例
├── scripts/                # 开发脚本 (lint, format)
├── pyproject.toml          # 项目配置
└── README.md               # 说明文档
```

## 🛠 开发指南

### 环境设置

```bash
# 克隆项目
git clone https://github.com/yourusername/python-template.git
cd python-template

# 安装开发依赖
uv sync --dev
```

### 代码质量

```bash
# 格式化代码
python scripts/format.py

# 代码检查
python scripts/lint.py
```

### 运行测试

```bash
# 运行所有测试
uv run pytest
```

## 📄 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件。
