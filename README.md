# Python Template

<div align="center">

一个开箱就能继续做事的 Python 工程模板。<br>
后端、前端、质量检查、发布脚本和 AI 协作文档都已经铺好，适合直接拿来起新项目。

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/downloads/)
[![uv](https://img.shields.io/badge/uv-managed-4B5563?style=for-the-badge)](https://github.com/astral-sh/uv)
[![Ruff](https://img.shields.io/badge/ruff-lint%20%26%20format-111827?style=for-the-badge)](https://github.com/astral-sh/ruff)
[![React](https://img.shields.io/badge/frontend-React%20%2B%20Vite-0F172A?style=for-the-badge)](#frontend)

[![Quick Start](https://img.shields.io/badge/Quick%20Start-5%20minutes-111827?style=for-the-badge)](#quick-start)
[![Use Template](https://img.shields.io/badge/Use%20This%20Template-Get%20Started-2563EB?style=for-the-badge)](#use-this-template)
[![Project Structure](https://img.shields.io/badge/Project%20Structure-Overview-059669?style=for-the-badge)](#project-structure)
[![AI Docs](https://img.shields.io/badge/AI%20Docs-Vibe%20Coding%20Ready-7C3AED?style=for-the-badge)](#ai-docs)

</div>

## 目录

- [为什么用这个模板](#why-this-template)
- [截图预留](#screenshots)
- [quick start](#quick-start)
- [用这个模板创建新项目](#use-this-template)
- [项目结构](#project-structure)
- [后端](#backend)
- [前端](#frontend)
- [维护脚本](#scripts)
- [质量检查](#verification)
- [AI docs](#ai-docs)
- [发布流程](#release)
- [许可证](#license)

## 为什么用这个模板

很多模板的问题不是功能少，而是第一天看着全，第二天就不知道该从哪里下手。这个仓库想解决的是另一件事：把真正会影响启动效率的东西先准备好。

- Python 3.10+、`uv`、`ruff`、`mypy`、`pytest` 已经串起来了。
- React + TypeScript + Vite + Tailwind CSS v4 + shadcn/ui 的前端基线已经放进来了。
- 常用的配置、日志、文件读写、JSON 工具和基础模型约定已经有了。
- `rename_package.py`、`update_version.py`、`setup_pre_commit.py` 这些维护动作已经脚本化。
- `ai_docs/` 不是摆设，里面有面向 AI 协作和 vibe coding 的工程约束，后续项目可以直接继承。

如果你想从一个尽量稳、尽量省事、又不至于过度抽象的模板起步，它就是干这个的。

## Screenshots

这部分按产品 README 的展示方式预留了位置，后续你可以直接替换成真实截图。

### Screenshot 1: 项目首页 / 主界面

> 占位说明：建议替换为项目主界面、控制台首页或关键工作流截图。<br>
> 推荐路径：`docs/assets/readme/screenshot-hero.png`

### Screenshot 2: 后端或 CLI 运行效果

> 占位说明：建议替换为后端服务启动、测试通过、CLI 执行结果等截图。<br>
> 推荐路径：`docs/assets/readme/screenshot-backend.png`

### Screenshot 3: 前端页面或组件展示

> 占位说明：建议替换为前端页面、表单、仪表盘或核心交互截图。<br>
> 推荐路径：`docs/assets/readme/screenshot-frontend.png`

### Screenshot 4: AI 协作文档或开发流程

> 占位说明：建议替换为 `ai_docs/`、CI 检查结果或开发流程图。<br>
> 推荐路径：`docs/assets/readme/screenshot-ai-docs.png`

## Quick Start

第一次启动，按这一段走就够了。

### 1. 克隆项目

```bash
git clone https://github.com/Tendo33/python-template.git
cd python-template
```

### 2. 安装依赖

```bash
uv sync --all-extras
pnpm --prefix frontend install
```

### 3. 初始化环境变量

```bash
cp .env.example .env
```

默认配置已经尽量压到最小：

```env
ENVIRONMENT=development
LOG_LEVEL=INFO
LOG_FILE=logs/app.log
```

### 4. 先跑一遍检查

```bash
uv run pytest
pnpm --prefix frontend test
```

### 5. 启动前端开发环境

```bash
pnpm --prefix frontend dev
```

如果你现在只关心后端能力，到这里已经可以开始工作了。

## Use This Template

这个模板最适合在项目一开始就改名、改版本、改仓库信息，不要拖到后面再补。

### 1. 用模板创建新仓库

如果你是在 GitHub 上使用模板仓库，直接点 `Use this template`。<br>
如果你是本地复制项目，可以这样开始：

```bash
git clone https://github.com/Tendo33/python-template.git my-new-project
cd my-new-project
```

### 2. 第一时间改包名

先预览，再执行：

```bash
python scripts/rename_package.py --dry-run my_new_project
python scripts/rename_package.py my_new_project
```

这个脚本会处理：

- `src/python_template/` 目录重命名
- 常见源码和配置文件中的模板名称替换
- `frontend/package.json` 的项目名
- `frontend/index.html` 的标题

### 3. 更新项目信息

至少把这些地方改掉：

- `pyproject.toml` 里的 `name`、`description`、`authors`、`urls`
- `src/<your_package>/__init__.py` 里的 `__version__`
- `README.md` 里的项目名、截图、示例命令和仓库链接

### 4. 按需更新版本号

```bash
python scripts/update_version.py --dry-run 0.2.0
python scripts/update_version.py 0.2.0
```

### 5. 打开提交前检查

```bash
python scripts/setup_pre_commit.py
```

## Project Structure

```text
python-template/
├── src/python_template/      # Python 包主体
│   ├── config/               # 配置管理
│   ├── contracts/            # 协议与接口约定
│   ├── core/                 # 核心上下文与基础能力
│   ├── models/               # Pydantic 模型
│   ├── observability/        # 日志与可观测性
│   └── utils/                # 文件、JSON、日期、装饰器等通用工具
├── tests/                    # Python 测试
├── scripts/                  # 维护脚本
├── frontend/                 # React + Vite 前端
├── ai_docs/                  # AI / vibe coding 工程规范
├── pyproject.toml
└── README.md
```

## Backend

后端默认栈：

- Python 3.10+
- `uv`
- `ruff`
- `pytest`
- `pydantic-settings`
- `loguru`

模板已经带上这些常用能力：

- 配置读取：`python_template.config.settings`
- 日志初始化：`python_template.observability.log_config`
- 文件与 JSON 工具：`python_template.utils`
- 可复用的模型和工具函数：`models/`、`utils/`、`core/`

示例导入：

```python
from python_template.config.settings import get_settings
from python_template.observability.log_config import get_logger, setup_logging
from python_template.utils import read_json, read_text_file, write_json, write_text_file
```

日志示例：

```python
from python_template.observability.log_config import get_logger, setup_logging

setup_logging(level="INFO", log_file="logs/app.log")
logger = get_logger(__name__)
logger.info("service started")
```

配置示例：

```python
from python_template.config.settings import get_settings

settings = get_settings()
print(settings.environment)
print(settings.log_level)
```

## Frontend

前端默认栈已经固定好：

- `pnpm`
- React
- TypeScript
- Vite
- Tailwind CSS v4
- shadcn/ui
- Vitest + Testing Library

目录约定：

```text
frontend/src/
├── app/            # app shell 和入口页面
├── features/       # 领域模块
├── components/ui/  # shadcn/ui 基础组件
├── hooks/          # 全局 hooks
├── lib/            # 工具与 API 包装
├── styles/         # 全局样式与 tokens
└── test/           # 测试基础设施
```

常用命令：

```bash
pnpm --prefix frontend dev
pnpm --prefix frontend lint
pnpm --prefix frontend typecheck
pnpm --prefix frontend test
pnpm --prefix frontend build
```

## Scripts

这个模板不想让你手工做重复劳动，所以把高频维护动作收成了脚本。

| 脚本 | 用途 |
| :--- | :--- |
| `python scripts/rename_package.py my_new_project` | 批量重命名模板包名 |
| `python scripts/update_version.py 0.2.0` | 同步更新前后端版本号 |
| `python scripts/setup_pre_commit.py` | 安装或更新 pre-commit hooks |
| `python scripts/generate_release_notes.py --tag v0.2.0 --output .github/release-notes.md` | 生成 release notes |
| `uv run python scripts/run_vulture.py --min-confidence 80` | 检查可能未使用的代码 |

更多说明见 [ai_docs/SCRIPTS_GUIDE.md](ai_docs/SCRIPTS_GUIDE.md)。

## Verification

真正能让模板长期可用的，不是起步命令，而是每次修改后的检查约束。

### 后端检查

```bash
uv run ruff check src tests scripts
uv run ruff format --check src tests scripts
uv run mypy src
uv run pytest
```

### 前端检查

```bash
pnpm --prefix frontend lint
pnpm --prefix frontend typecheck
pnpm --prefix frontend test
pnpm --prefix frontend build
```

### 全量检查

```bash
uv run ruff check src tests scripts
uv run ruff format --check src tests scripts
uv run mypy src
uv run pytest
pnpm --prefix frontend lint
pnpm --prefix frontend typecheck
pnpm --prefix frontend test
pnpm --prefix frontend build
```

## AI Docs

`ai_docs/` 是这个模板和普通脚手架最大的区别之一。它不是给人“看看而已”的附属目录，而是给 AI 助手和后续协作者用的项目契约。

建议阅读顺序：

1. `ai_docs/AI_TOOLING_STANDARDS.md`
2. `ai_docs/BACKEND_STANDARDS.md`
3. `ai_docs/FRONTEND_STANDARDS.md`
4. `ai_docs/frontend_design/DESIGN_SYSTEM.md`
5. 其他专题文档，例如 `MODELS_GUIDE.md`、`SETTINGS_GUIDE.md`、`SDK_USAGE.md`

当前包含的文档：

- `ai_docs/AI_TOOLING_STANDARDS.md`：全局 AI 工作流和质量门禁
- `ai_docs/BACKEND_STANDARDS.md`：后端架构与工程约束
- `ai_docs/FRONTEND_STANDARDS.md`：前端栈与实现约束
- `ai_docs/frontend_design/DESIGN_SYSTEM.md`：前端设计系统规范
- `ai_docs/SCRIPTS_GUIDE.md`：脚本使用说明
- `ai_docs/MODELS_GUIDE.md`：Pydantic 模型规范
- `ai_docs/SETTINGS_GUIDE.md`：配置管理指南
- `ai_docs/SDK_USAGE.md`：`src` 布局与导入约定
- `ai_docs/PRE_COMMIT_GUIDE.md`：提交前检查说明

## Release

发布流程已经准备好了，常规做法是：

```bash
python scripts/update_version.py --dry-run 0.3.0
python scripts/update_version.py 0.3.0
uv run pytest
pnpm --prefix frontend test
git add -A
git commit -m "chore: release v0.3.0"
git tag v0.3.0
git push && git push --tags
```

推送 tag 之后，`.github/workflows/release.yml` 会负责后续发布动作。<br>
如果配置了对应的模型环境变量，release notes 也可以自动生成；如果没有，流程会回退到确定性文案，不会卡住发布。

## License

MIT，见 `LICENSE`。
