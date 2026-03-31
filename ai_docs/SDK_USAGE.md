# SDK Usage Guide

这个项目使用标准的 `src` 布局。

## 本地安装

推荐：

```bash
uv pip install -e .
```

也可以使用：

```bash
pip install -e .
```

测试时，`uv run ...` 也会自动在当前环境下解析本项目依赖。

## 导入规则

永远从包名导入，不要从 `src` 目录路径导入。

正确示例：

```python
from python_template.utils import read_json
from python_template.config.settings import get_settings
from python_template.observability.log_config import setup_logging
```

错误示例：

```python
from src.python_template.utils import read_json
```

## 当前推荐的公共导入面

### 配置

```python
from python_template.config.settings import Settings, get_settings, reload_settings
```

### 日志

```python
from python_template.observability.log_config import (
    configure_json_logging,
    get_logger,
    setup_logging,
)
```

### 稳定工具

```python
from python_template.utils import (
    read_json,
    read_text_file,
    write_json,
    write_text_file,
)
```

### 模型

```python
from python_template.models import ApiResponse, BaseModel, ConfigModel, User
```

### 运行时上下文

```python
from python_template.core import Context, ContextManager
```

## 深层模块导入规则

可以导入具体子模块，但要满足下面至少一条：

- 需要高级能力，包级导出面没有暴露
- 文档要解释为什么要走子模块
- 这是仓库内部实现代码，不是给外部使用者看的示例

例如：

```python
from python_template.utils.decorator_utils import retry_decorator
from python_template.utils.common_utils import chunk_list
```

## 为什么测试里直接能导入包名

`pyproject.toml` 中的 pytest 配置包含：

```toml
[tool.pytest.ini_options]
pythonpath = ["src"]
```

这只影响 Python 的导入解析，不会改变你读写文件时的相对路径基准。

## 路径处理建议

文件 I/O 使用 `pathlib.Path`，并明确基于项目根目录或调用方传入路径构造，不要假设 `pythonpath` 会影响文件系统路径。
