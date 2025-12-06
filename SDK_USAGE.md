# SDK 使用指南 (SDK Usage Guide)

本文档介绍如何将 `python_template` 作为 SDK 使用，以及为什么在测试代码中导入时不需要加 `src` 前缀。

## 1. 如何作为 SDK 使用

### 安装

如果你是在本地开发，推荐使用 "可编辑模式" (Editable Install) 安装：

```bash
# 使用 pip
pip install -e .

# 或者使用 uv (本项目推荐)
uv pip install -e .
```

如果已经发布到 PyPI，则直接安装包名：

```bash
pip install python-template
```

### 导入和使用

安装完成后，你可以直接在任何 Python 脚本中导入 `python_template`，**不需要** 关心它在项目中的具体路径（如 `src`）。

```python
from python_template.utils import read_json

# 使用工具函数
data = read_json("data.json")
print(data)
```

## 2. 为什么测试文件夹导入不需要加 `src`？

你在 `tests` 文件夹中看到的代码：

```python
from python_template.utils import read_json
```

之所以不需要写成 `from src.python_template.utils import ...`，主要有两个原因：

### 原因一：`src` 布局 (Src Layout) 规范

本项目采用了标准的 `src` 布局结构：

```text
python-template/
├── src/
│   └── python_template/  <-- 实际的包在这里
├── tests/
└── pyproject.toml
```

在这种布局下，`src` 目录本身不是包的一部分，它只是一个容器。当你执行 `pip install -e .` 时，Python 的包管理器会将 `src` 目录添加到 Python 的搜索路径（`sys.path`）中，或者通过 `.pth` 文件将 `python_template` 链接到环境中。

因此，Python 解释器在查找包时，会直接在 `src` 下找到 `python_template`，所以你直接 `import python_template` 即可。

### 原因二：Pytest 配置

在 `pyproject.toml` 文件中，我们明确配置了 `pytest` 的 `pythonpath`：

```toml
[tool.pytest.ini_options]
# ...
pythonpath = ["src"]
```

这行配置告诉 `pytest`：在运行测试之前，先把 `src` 目录加入到 `sys.path` 中。这样，测试代码运行时就能像安装了该包一样，直接找到 `python_template` 模块。

## 总结

*   **作为用户**：安装后直接 `import python_template`。
*   **作为开发者**：在 `tests` 中也是直接 `import python_template`，这是由 `src` 布局规范和 `pytest` 配置共同保证的。永远不要在导入语句中包含 `src`（例如 `from src.python_template import ...` 是错误的写法）。
