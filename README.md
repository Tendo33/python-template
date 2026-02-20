# Python Template

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Code style: ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)

一个现代化的 Python 工具库模板，集成了常用的工具函数和最佳实践。

## ⚠️ v0.2.0 Breaking Changes

`python_template.utils` 顶层导出已收敛为稳定核心 API。以下旧导入方式需要迁移到子模块：

- `from python_template.utils import retry_decorator` -> `from python_template.utils.decorator_utils import retry_decorator`
- `from python_template.utils import chunk_list` -> `from python_template.utils.common_utils import chunk_list`
- `from python_template.utils import Context` -> `from python_template.utils.context import Context`
- `from python_template.utils import list_files` -> `from python_template.utils.file_utils import list_files`

保留在顶层 `python_template.utils` 的核心能力：日志、Settings、基础文件读写、基础 JSON 读写、基础日期时间工具。

## 🚀 开发者快速上手

如果你是刚克隆此项目的开发人员，请按照以下顺序初始化项目：

### 1. 环境准备

本项目使用 [uv](https://github.com/astral-sh/uv) 进行包管理。

```bash
# 安装 uv (如果尚未安装)
pip install uv
```

### 2. 安装依赖

```bash
# 同步项目依赖（包含开发工具）
uv sync --all-extras
```

### 3. 项目重命名 (可选)

如果你将此模板用于新项目，请先重命名包名：

```bash
# 将 'python_template' 重命名为你的项目名
python scripts/rename_package.py my_awesome_project
```

### 4. 配置代码检查

安装 git hooks 以确保代码质量：

```bash
# 配置 pre-commit hooks
python scripts/setup_pre_commit.py
```

### 5. 验证环境

运行测试确保一切正常：

```bash
uv run pytest
```

## 🧭 模板使用教程（从 0 到可开发）

如果你后面要把这个仓库当作模板反复使用，建议按下面流程走一遍。

### 第 0 步：准备你的新项目目录

```bash
# 方式 1：直接复制模板
git clone https://github.com/Tendo33/python-template.git my-new-project
cd my-new-project

# 方式 2：你也可以用自己的模板仓库地址
# git clone <your-template-repo> my-new-project
```

### 第 1 步：安装依赖并确认基础环境

```bash
# 安装全部依赖（含开发工具）
uv sync --all-extras

# 验证 Python 工具链
uv run ruff --version
uv run pytest --version
```

### 第 2 步：重命名包名（建议第一时间做）

模板默认包名是 `python_template`。如果不改，后续发布或多项目并行时会很容易混淆。

```bash
# 先预览，确认影响范围
python scripts/rename_package.py my_new_project --dry-run

# 确认后执行（会修改 src 目录、导入路径、文档等）
python scripts/rename_package.py my_new_project
```

执行后建议马上做一次检查：

```bash
uv run ruff check src tests scripts
uv run pytest
```

### 第 3 步：更新项目元信息（发布前必须）

重点改这些位置：

- `pyproject.toml`：`name`、`description`、`authors`、`urls`
- `src/<your_package>/__init__.py`：`__version__`
- `.env.example`：`ENVIRONMENT`、`LOG_LEVEL`、`LOG_FILE`
- `README.md`：项目名、安装方式、示例导入路径

可用脚本统一更新版本号：

```bash
python scripts/update_version.py 0.2.0
```

### 第 4 步：配置运行环境

```bash
# 复制环境变量模板
cp .env.example .env

# 按需修改 .env（至少确认 ENVIRONMENT / LOG_LEVEL）
```

如果你有额外配置，直接在 `src/<your_package>/utils/setting.py` 的 `Settings` 类里新增字段，并同步更新 `.env.example`。

### 第 5 步：启用提交前质量门禁（强烈建议）

```bash
# 安装并启用 pre-commit
python scripts/setup_pre_commit.py
```

这样每次 `git commit` 前都会自动执行格式化与静态检查，能提前挡住大多数低级问题。

### 第 6 步：开始业务开发（推荐最小循环）

每次做完一个小功能，至少跑下面四个命令：

```bash
uv run ruff check src tests scripts
uv run ruff format --check src tests scripts
uv run mypy src
uv run pytest
```

如果都通过，再提交代码。这样你的模板项目会一直保持“可运行、可测试、可发布”的状态。

### 第 7 步：交付前最终检查清单

在准备发布/交付前，建议再跑一次：

```bash
uv run ruff check src tests scripts
uv run ruff format --check src tests scripts
uv run mypy src
uv run pytest
uv run python scripts/run_vulture.py --min-confidence 80
```

### 常见问题（高频）

1. `import python_template` 报错  
   - 先确认执行过 `uv sync --all-extras`，并在项目根目录运行命令。  
2. 重命名后测试失败  
   - 通常是有遗漏导入或缓存，先看 `git diff`，再重新跑 `uv run pytest`。  
3. Ruff 扫到不该扫的目录  
   - 本模板已在 `pyproject.toml` 排除 `.agent/.claude/.codex/.cursor`，如你新增目录可按同样方式加入排除。

---

## ✨ 特性

- 🛠 **丰富的工具集**：包含日期、文件、JSON、装饰器、通用工具等常用模块
- 📝 **强大的日志系统**：基于 [loguru](https://github.com/Delgan/loguru) 的预配置日志管理
- ⚙️ **配置管理**：基于 [pydantic-settings](https://github.com/pydantic/pydantic-settings) 的类型安全配置
- 🔄 **上下文管理**：线程安全的运行时上下文存储
- 🚀 **现代化工具链**：使用 `uv` 进行包管理，`ruff` 进行代码检查和格式化

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

### 2. 配置管理 (Settings)

基于 Pydantic 的类型安全配置管理，支持环境变量和 .env 文件。

```python
from python_template.utils import get_settings

# 获取配置（单例）
settings = get_settings()

# 访问配置项
print(f"Environment: {settings.environment}")
print(f"Log Level: {settings.log_level}")

# 获取项目路径
project_root = settings.get_project_root()
log_path = settings.get_log_file_path()
```

**配置文件设置：**

```bash
# 复制示例文件
cp .env.example .env

# 编辑 .env 文件设置你的配置
ENVIRONMENT=development
LOG_LEVEL=DEBUG
```

**添加自定义配置：**

在 `src/python_template/utils/setting.py` 中添加字段：

```python
class Settings(BaseSettings):
    # ... 现有字段 ...

    # 添加你的配置
    database_url: str = Field(
        default="sqlite:///./app.db",
        description="Database URL"
    )
```

详细说明请查看 [配置指南](doc/SETTINGS_GUIDE.md)

### 3. 装饰器工具 (Decorators)

```python
from python_template.utils.decorator_utils import (
    log_calls,
    retry_decorator,
    timing_decorator,
)

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

#### 异步装饰器 (Async Decorators)

```python
from python_template.utils.decorator_utils import (
    async_timing_decorator,
    async_retry_decorator,
    async_catch_exceptions,
    AsyncContextTimer,
)

# 异步计时装饰器
@async_timing_decorator
async def fetch_data():
    await asyncio.sleep(1)
    return "data"

# 异步重试装饰器
@async_retry_decorator(max_retries=3, delay=1.0)
async def unstable_api_call():
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()

# 异步异常捕获装饰器
@async_catch_exceptions(default_return=None)
async def safe_fetch():
    # ... 可能失败的异步操作
    pass

# 异步上下文计时器
async def process():
    async with AsyncContextTimer("异步数据处理"):
        await heavy_async_operation()
```

### 4. 通用工具 (Common Utils)

```python
from python_template.utils.common_utils import chunk_list, flatten_dict, merge_dicts

# 列表分块
items = [1, 2, 3, 4, 5]
chunks = list(chunk_list(items, 2))  # [[1, 2], [3, 4], [5]]

# 字典展平
nested = {"a": {"b": 1}}
flat = flatten_dict(nested)  # {"a.b": 1}

# 字典合并
d1 = {"a": 1}
d2 = {"b": 2}
merged = merge_dicts(d1, d2)  # {"a": 1, "b": 2}
```

### 5. 文件操作 (File Utils)

```python
from python_template.utils import read_text_file, write_text_file, ensure_directory

# 确保目录存在
ensure_directory("data/output")

# 写入文件 (自动创建父目录)
write_text_file("Hello World", "data/output/test.txt")

# 读取文件
content = read_text_file("data/output/test.txt", default="Default Content")
```

### 6. JSON 处理 (JSON Utils)

```python
from python_template.utils import read_json, write_json

data = {"name": "test", "value": 123}

# 写入 JSON
write_json(data, "config.json", indent=2)

# 读取 JSON
config = read_json("config.json", default={})
```

### 7. 日期时间 (Date Utils)

```python
from datetime import datetime
from python_template.utils import get_timestamp, format_datetime, get_current_time

# 获取当前 ISO 时间戳
ts = get_timestamp()

# 获取当前时间字符串
now = get_current_time()

# 格式化日期
formatted = format_datetime(datetime.now(), format_str="%Y-%m-%d")
```

### 8. 数据模型 (Pydantic Models)

所有数据模型使用 Pydantic BaseModel 进行定义,提供类型验证和序列化功能。

```python
from python_template.models import BaseModel, User, ApiResponse
from pydantic import Field

# 使用预定义模型
user = User(
    id=1,
    username="john_doe",
    email="john@example.com",
    full_name="John Doe"
)

# 序列化
user_dict = user.model_dump()
user_json = user.model_dump_json()

# 创建自定义模型
class Product(BaseModel):
    """产品模型"""
    id: int = Field(..., description="产品ID", ge=1)
    name: str = Field(..., description="产品名称", min_length=1)
    price: float = Field(..., description="价格", gt=0)

# 使用泛型响应模型
response = ApiResponse[Product](
    success=True,
    data=Product(id=1, name="Phone", price=999.99),
    message="Product fetched successfully"
)
```

详细使用说明请查看 [模型使用指南](doc/MODELS_GUIDE.md)

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
│   └── models/             # 数据模型
│       ├── base.py            # BaseModel 与通用 Mixin
│       └── examples.py        # 示例模型 (User/ApiResponse 等)
├── tests/                  # 测试用例
├── scripts/                # 维护脚本
│   ├── rename_package.py      # 重命名包脚本
│   ├── setup_pre_commit.py    # git hooks 配置脚本
│   └── update_version.py      # 版本更新脚本
├── pyproject.toml          # 项目配置
└── README.md               # 说明文档
```

## 🛠 开发指南

### 环境设置

```bash
# 克隆项目
git clone https://github.com/Tendo33/python-template.git
cd python-template

# 安装开发依赖
uv sync --all-extras
```

### 代码质量

本项目使用 `ruff` 进行代码格式化和检查。

```bash
# 格式化代码
uv run ruff format src tests scripts

# 代码检查
uv run ruff check src tests scripts

# 类型检查
uv run mypy src
```

### 运行测试

```bash
# 运行所有测试
uv run pytest
```

## 🛠️ 维护脚本

项目在 `scripts/` 目录下提供了一些实用的维护脚本：

### 1. Git Hooks 配置 (`setup_pre_commit.py`)

用于自动配置 git hooks，确保每次提交时自动运行代码检查和格式化。

```bash
# 安装并配置 hooks
python scripts/setup_pre_commit.py

# 选项：
# --update  更新 hooks 到最新版本
# --test    手动运行 hooks 检查所有文件
# --all     执行安装、更新和测试
```

### 2. 项目重命名 (`rename_package.py`)

如果你想将模板用于新项目，可以使用此脚本一键重命名包名和相关配置。

```bash
# 预览修改 (不实际执行)
python scripts/rename_package.py my_new_project --dry-run

# 执行重命名
python scripts/rename_package.py my_new_project
```

### 3. 版本更新 (`update_version.py`)

统一更新项目中的版本号（包括 pyproject.toml, \_\_init\_\_.py 等）。

```bash
# 更新版本到 0.2.0
python scripts/update_version.py 0.2.0
```

## 📚 文档

- [配置指南](doc/SETTINGS_GUIDE.md) - Pydantic Settings 详细说明
- [模型使用指南](doc/MODELS_GUIDE.md) - Pydantic BaseModel 数据模型使用说明
- [SDK 使用指南](doc/SDK_USAGE.md) - 工具函数使用示例  
- [Pre-commit 指南](doc/PRE_COMMIT_GUIDE.md) - Git hooks 配置


---

### Star History

[![Star History Chart](https://api.star-history.com/svg?repos=Tendo33/python-template&type=Date)](https://star-history.com/#Tendo33/python-template&Date)

### Contributors

<a href="https://github.com/Tendo33/python-template/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=Tendo33/python-template" />
</a>


## 📄 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件。
