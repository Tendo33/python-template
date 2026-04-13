# Current Scripts

## When to read

- 想了解仓库维护脚本和本地质量工具时先读这里。
- 想确认脚本、pre-commit 和 release notes 工具当前行为时读这里。

## Current truth

仓库当前提供这些维护脚本：

- `rename_package.py`：重命名 Python 包名和项目名
- `update_version.py`：同步更新版本号
- `setup_pre_commit.py`：安装、更新或测试 pre-commit hooks
- `run_vulture.py`：扫描可能未使用的 Python 代码
- `generate_release_notes.py`：生成 release notes

## When to use which script

### Rename package and project

- 新建仓库后第一时间改模板名称时用 `rename_package.py`
- 它会重命名 `src/python_template/`，并更新源码、文档、配置和前端文本文件中的模板名称引用
- 还会更新 `frontend/package.json` 的 `name` 和 `frontend/index.html` 的 `<title>`

### Update version

- 准备发版或同步版本号时用 `update_version.py`
- 它会更新 `pyproject.toml`、`src/python_template/__init__.py` 和 `frontend/package.json`

### Initialize pre-commit

- 想安装、更新或验证本地 hooks 时用 `setup_pre_commit.py`
- 仓库使用 `.pre-commit-config.yaml`
- 当前 hook 主要覆盖格式、基础配置检查和 Ruff

### Scan unused Python code

- 想做轻量死代码排查时用 `run_vulture.py`
- 它适合在重构前后做快速扫描，不替代测试和人工判断

### Generate release notes

- 准备 release 文案时用 `generate_release_notes.py`
- 它会收集 tag、changelog 和 commit 信息
- 有 API key 时可调用模型生成摘要
- 没有 API key 时回退到确定性 highlights

## Verification

- 脚本、README 和 `ai_docs` 的相关验证命令见 [verification.md](../reference/verification.md)

## Shared references

- 当前发版流程见 [release.md](release.md)
- 验证命令见 [verification.md](../reference/verification.md)
