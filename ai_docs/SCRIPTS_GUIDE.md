# Scripts Guide

仓库维护脚本位于 `scripts/` 目录，默认都可以直接用 `python scripts/<name>.py ...` 调用。

## `rename_package.py`

把模板项目从 `python_template` / `python-template` 重命名为新的包名与项目名。

### 行为

- 校验新包名是否是合法 Python 标识符
- 将 `src/python_template/` 重命名为 `src/<new_package>/`
- 扫描并替换文档、配置、前端文件、AI 配置中的旧名字
- 更新 `frontend/package.json` 的 `name`
- 更新 `frontend/index.html` 的 `<title>`

### 扫描范围

脚本会处理这些后缀或文件名中的文本替换：

- `.py`, `.toml`, `.cfg`, `.ini`
- `.md`, `.rst`, `.txt`
- `.ts`, `.tsx`, `.js`, `.jsx`, `.json`, `.css`, `.html`
- `.yaml`, `.yml`, `.mdc`
- `Makefile`, `Dockerfile`, `.gitignore`, `.env.example`, `.cursorrules`, `components.json`

会跳过常见产物目录，例如 `.git/`、`.venv/`、`node_modules/`、`dist/`、`logs/`、`htmlcov/`。

### 常用命令

```bash
# 预览
python scripts/rename_package.py --dry-run my_new_project

# 执行（交互确认）
python scripts/rename_package.py my_new_project

# 执行并跳过确认
python scripts/rename_package.py -y my_new_project
```

### 执行后建议

```bash
git diff
uv run pytest
pnpm --prefix frontend test
```

## `update_version.py`

同步更新仓库中的版本号。

### 更新目标

- `pyproject.toml`
- `src/<detected_package>/__init__.py`
- `frontend/package.json`（如果存在）

### 规则

- 版本号必须符合 `MAJOR.MINOR.PATCH`
- 会自动探测 `src/` 下唯一的包目录
- `--dry-run` 只预览，不落盘

### 常用命令

```bash
python scripts/update_version.py --dry-run 0.2.2
python scripts/update_version.py 0.2.2
```

## `setup_pre_commit.py`

安装、更新或测试 pre-commit hooks。

### 支持的模式

```bash
# 默认：安装 hooks
python scripts/setup_pre_commit.py

# 更新 hook 版本
python scripts/setup_pre_commit.py --update

# 在全仓测试 hooks
python scripts/setup_pre_commit.py --test

# 安装 + 更新 + 测试
python scripts/setup_pre_commit.py --all
```

额外参数：

```bash
python scripts/setup_pre_commit.py --project-root /path/to/repo
```

脚本会先检查 `pre-commit` 是否可用；如果未安装，会提示使用 `pip install pre-commit` 或 `uv add --dev pre-commit`。

## `run_vulture.py`

运行 Vulture 扫描可能未使用的 Python 代码。

### 默认行为

- 默认扫描 `src/`
- 默认最小置信度是 `60`
- 支持按大小排序

### 常用命令

```bash
python scripts/run_vulture.py
python scripts/run_vulture.py --min-confidence 80
python scripts/run_vulture.py --sort-by-size
python scripts/run_vulture.py src/python_template tests
```

## `generate_release_notes.py`

为指定 git tag 生成 Markdown release notes。

### 输入

- `--tag`：必填，例如 `v0.2.1`
- `--output`：必填，输出 Markdown 文件路径

### 可选参数

- `--repo-root`：仓库根目录，默认当前目录
- `--max-commits`：最多纳入多少条 commit，默认 `200`
- `--model`：摘要模型，默认读 `RELEASE_NOTES_MODEL`，否则回退 `gpt-4o-mini`
- `--model-timeout`：模型请求超时，默认 `30`

### 数据来源

脚本会组合以下信息：

- 当前 tag
- 上一个 tag
- `CHANGELOG.md` 中对应版本段落
- release 区间内的 commit 列表

### 模型调用与回退

如果设置了 `OPENAI_API_KEY`，脚本会尝试调用兼容 OpenAI Chat Completions 的端点生成摘要：

- `OPENAI_API_KEY`
- `RELEASE_NOTES_MODEL`（可选）
- `OPENAI_BASE_URL`（可选，默认 `https://api.openai.com/v1/chat/completions`）

如果没有 API key，或者模型请求失败，脚本会自动回退到确定性 highlights，不会中断发版。

### 常用命令

```bash
python scripts/generate_release_notes.py \
  --tag v0.2.1 \
  --output .github/release-notes.md
```

## 推荐发版流程

```bash
python scripts/update_version.py --dry-run 0.2.2
python scripts/update_version.py 0.2.2
uv run pytest
pnpm --prefix frontend test
git add -A
git commit -m "chore: release v0.2.2"
git tag v0.2.2
git push origin main
git push origin v0.2.2
```

推送 `v*` tag 后，`.github/workflows/release.yml` 会自动生成 release notes 并创建或更新 GitHub Release。
