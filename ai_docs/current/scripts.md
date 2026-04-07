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
- `sync_ai_adapters.py`：根据 `ai_adapter_config.json` 生成或清理 AI 入口文件
- `check_ai_docs.py`：校验 `ai_docs/` 与 AI 入口文件是否和配置保持一致

## Rename and versioning

- `rename_package.py` 会处理源码目录、文档、配置、前端文件和 AI adapter 中的模板名称
- `update_version.py` 会更新 `pyproject.toml`、包版本和前端版本号

## Pre-commit and quality hooks

- 仓库使用 `.pre-commit-config.yaml`
- 当前 hook 主要覆盖格式、基础配置检查和 Ruff
- 日常验证命令见 [verification.md](../reference/verification.md)

## Release notes generation

- `generate_release_notes.py` 会收集 tag、changelog 和 commit 信息
- 有 API key 时可调用模型生成摘要
- 没有 API key 时回退到确定性 highlights

## Shared references

- 验证命令见 [verification.md](../reference/verification.md)
- 其它阅读路径请从 `ai_docs/INDEX.md` 进入
