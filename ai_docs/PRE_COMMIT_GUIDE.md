# Pre-commit Guide

pre-commit 会在 `git commit` 前自动跑一组质量检查，帮助我们在本地尽早发现格式和基础配置问题。

## 安装方式

直接安装：

```bash
uv run pre-commit install
```

或使用仓库脚本：

```bash
python scripts/setup_pre_commit.py
```

## 常用命令

```bash
uv run pre-commit run --all-files
uv run pre-commit run
uv run pre-commit autoupdate
python scripts/setup_pre_commit.py --test
python scripts/setup_pre_commit.py --all
```

## 当前启用的 hooks

来自 `.pre-commit-config.yaml`：

- `trailing-whitespace`
- `end-of-file-fixer`
- `check-yaml`
- `check-toml`
- `check-json`
- `check-added-large-files`
- `check-merge-conflict`
- `debug-statements`
- `ruff --fix`
- `ruff-format`

当前 `mypy` hook 仍然保留为注释状态，没有默认启用。

## 当前排除路径

pre-commit 默认跳过这些目录或产物：

- `venv/`
- `tests/`
- `docs/`
- `build/`
- `dist/`
- `.agent/`
- `.agents/`
- `.claude/`
- `.codex/`
- `.cursor/`
- `.github/`
- `.pytest_cache/`
- `.ruff_cache/`

## 如果提交失败

- 如果 hook 自动改了文件：重新 `git add -A` 再提交
- 如果 Ruff 仍报错：手动修复后重新提交
- 如果只是临时跳过：`git commit --no-verify`

除非非常确定风险可接受，否则不要把 `--no-verify` 当常规流程。
