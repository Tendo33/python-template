# Python Template

一个面向开发者的 Python 项目模板：后端基础设施、前端 starter、质量检查、发版脚本和 AI 协作规范都已经接好，适合直接起新仓库，而不是从空目录重新拼。

<div align="center">

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/downloads/)
[![uv](https://img.shields.io/badge/uv-managed-4B5563?style=for-the-badge)](https://github.com/astral-sh/uv)
[![Ruff](https://img.shields.io/badge/ruff-lint%20%26%20format-111827?style=for-the-badge)](https://github.com/astral-sh/ruff)
[![Frontend](https://img.shields.io/badge/Frontend-React%20%2B%20Vite-0F172A?style=for-the-badge)](#frontend)

[![Quick Start](https://img.shields.io/badge/Quick%20Start-5%20minutes-111827?style=for-the-badge)](#quick-start)
[![Use This Template](https://img.shields.io/badge/Use%20This%20Template-Get%20Started-2563EB?style=for-the-badge)](#use-this-template)
[![Project Structure](https://img.shields.io/badge/Project%20Structure-Overview-059669?style=for-the-badge)](#project-structure)
[![AI Docs](https://img.shields.io/badge/AI%20Docs-Project%20Contract-7C3AED?style=for-the-badge)](#ai-docs)

</div>

## 目录

- [为什么用这个模板](#为什么用这个模板)
- [截图预留](#截图预留)
- [Quick Start](#quick-start)
- [Use This Template](#use-this-template)
- [Project Structure](#project-structure)
- [Backend](#backend)
- [Frontend](#frontend)
- [Scripts](#scripts)
- [Verification](#verification)
- [AI Docs](#ai-docs)
- [Release](#release)
- [License](#license)

## 为什么用这个模板

这个仓库解决的不是“怎么再造一个模板”，而是“怎么把项目第 1 天到第 30 天最容易反复手工做的事情先准备好”。

- 后端基线已经就位：`uv`、`ruff`、`mypy`、`pytest`、`pydantic-settings`、`loguru`
- 前端 starter 已经可运行：React 19 + TypeScript + Vite + Tailwind CSS v4 + shadcn/ui 风格组件
- 常见基础模块已经拆好：配置、日志、上下文、协议、模型、文件 / JSON / 日期工具
- 维护动作脚本化：包名重命名、版本更新、pre-commit 安装、无用代码扫描、release notes 生成
- `ai_docs/` 不是装饰目录，而是给 AI 助手和协作者共用的项目契约

如果你想从一个尽量直接、尽量省心、又不会一上来就堆满过度抽象的仓库起步，这个模板就是为这种场景准备的。

## 截图预留

模板仓库默认保留展示位，后续可以直接替换成真实截图。

### Screenshot 1: 项目首页 / 主界面

推荐路径：`docs/assets/readme/screenshot-hero.png`

### Screenshot 2: 后端或 CLI 运行效果

推荐路径：`docs/assets/readme/screenshot-backend.png`

### Screenshot 3: 前端页面或组件展示

推荐路径：`docs/assets/readme/screenshot-frontend.png`

### Screenshot 4: AI 协作或质量检查流程

推荐路径：`docs/assets/readme/screenshot-ai-docs.png`

## Quick Start

### 1. 克隆仓库

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

当前默认环境变量只有最小基线：

```env
ENVIRONMENT=development
LOG_LEVEL=INFO
LOG_FILE=logs/app.log
```

### 4. 先跑一次检查

```bash
uv run pytest
pnpm --prefix frontend test
```

### 5. 启动前端开发环境

```bash
pnpm --prefix frontend dev
```

如果你现在只想从后端代码开始扩展，到这一步就已经可以动手了。

## Use This Template

建议在项目刚创建时就把名字、版本和仓库信息换掉，不要等后面文件变多了再统一修。

### 1. 基于模板创建新仓库

GitHub 上可以直接点 `Use this template`。如果你是在本地复制：

```bash
git clone https://github.com/Tendo33/python-template.git my-new-project
cd my-new-project
```

### 2. 第一时间改包名

```bash
python scripts/rename_package.py --dry-run my_new_project
python scripts/rename_package.py my_new_project
```

脚本会同时处理：

- `src/python_template/` 目录重命名
- 文档、配置、前端文件、AI 配置中的模板名称替换
- `frontend/package.json` 的 `name`
- `frontend/index.html` 的 `<title>`

### 3. 更新项目元信息

至少检查这些位置：

- `pyproject.toml` 的 `name`、`description`、`authors`、`urls`
- `src/<your_package>/__init__.py` 的 `__version__`
- `README.md` 的项目名、仓库链接、截图和示例命令

### 4. 更新版本号

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
├── src/python_template/          # Python 包主体
│   ├── config/                   # Settings 与配置加载
│   ├── contracts/                # Protocol 接口定义
│   ├── core/                     # Context 等运行时基础设施
│   ├── models/                   # Pydantic 基础模型与示例模型
│   ├── observability/            # loguru 日志配置
│   └── utils/                    # 文件 / JSON / 日期 / 通用工具
├── tests/                        # Python 测试
├── scripts/                      # 仓库维护脚本
├── frontend/                     # React + Vite 前端 starter
│   ├── src/app/                  # 当前页面入口
│   ├── src/components/           # 共享组件与 ui primitives
│   ├── src/styles/               # 全局样式与设计 token
│   └── src/test/                 # 前端测试初始化
├── ai_docs/                      # AI / 协作文档与工程规范
├── .github/workflows/            # CI 与 release workflow
├── pyproject.toml
└── README.md
```

前端目前故意保持为一个很小的 starter。等项目长大后，再按 `ai_docs/reference/project-structure.md` 和 `ai_docs/standards/frontend.md` 里的约定扩展目录。

## Backend

后端默认栈：

- Python 3.10+
- `uv`
- `ruff`
- `mypy`
- `pytest`
- `pydantic-settings`
- `loguru`

当前模板已经内置这些可直接复用的入口：

- 配置：`python_template.config.settings`
- 日志：`python_template.observability.log_config`
- 公共工具：`python_template.utils`
- 上下文：`python_template.core.context`
- 协议接口：`python_template.contracts.protocols`
- Pydantic 模型：`python_template.models`

常见导入方式：

```python
from python_template.config.settings import get_settings
from python_template.observability.log_config import get_logger, setup_logging
from python_template.utils import (
    read_json,
    read_text_file,
    write_json,
    write_text_file,
)
```

日志最小示例：

```python
from python_template.observability.log_config import get_logger, setup_logging

setup_logging(level="INFO", log_file="logs/app.log")
logger = get_logger(__name__)
logger.info("service started")
```

## Frontend

前端固定基线：

- `pnpm`
- React 19
- TypeScript 5
- Vite 8
- Tailwind CSS v4
- shadcn/ui 风格组件模式
- Vitest + Testing Library

当前 starter 的实际文件比较精简：

```text
frontend/src/
├── app/App.tsx                  # 单页入口
├── components/theme-toggle.tsx  # 深浅色切换
├── components/ui/button.tsx     # Button primitive
├── styles/globals.css           # OKLCH token + Tailwind theme bridge
├── test/setup.ts                # Vitest setup
└── main.tsx                     # 前端 bootstrap
```

当前页面包含：

- 吸顶头部
- 品牌标题
- 深浅色切换按钮
- 居中的 hero 文案与 CTA
- 简单页脚

如果要开始新的 UI 设计工作，先按下面流程准备风格输入：

1. 先到 `https://github.com/VoltAgent/awesome-design-md` 选择一个设计风格起点。
2. 如果没有更明确的参考，可以默认使用 Linear 风格。
3. 在项目根目录运行 `npx getdesign@latest add linear.app`，安装对应的 `DESIGN.md`。
4. 然后要求你的 AI assistant 在后续 UI 工作中使用项目根目录的 `DESIGN.md`。

更详细的前端设计流程和约束请看 `ai_docs/standards/design-system.md` 与 `ai_docs/workflows/add-frontend-feature.md`。

常用命令：

```bash
pnpm --prefix frontend dev
pnpm --prefix frontend lint
pnpm --prefix frontend typecheck
pnpm --prefix frontend test
pnpm --prefix frontend build
```

## Scripts

| 脚本 | 用途 |
| :--- | :--- |
| `python scripts/rename_package.py --dry-run my_new_project` | 预览模板重命名结果 |
| `python scripts/rename_package.py my_new_project` | 执行包名与项目名替换 |
| `python scripts/update_version.py 0.2.2` | 同步更新后端 + 前端版本号 |
| `python scripts/setup_pre_commit.py --all` | 安装、更新并测试 pre-commit hooks |
| `python scripts/run_vulture.py --min-confidence 80` | 扫描可能未使用的 Python 代码 |
| `python scripts/generate_release_notes.py --tag v0.2.1 --output .github/release-notes.md` | 生成 release notes |

更多细节见 [ai_docs/current/scripts.md](ai_docs/current/scripts.md)。

## Verification

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

### 本地全量检查

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

更详细的验证入口见 [ai_docs/reference/verification.md](ai_docs/reference/verification.md)。CI 当前会跑 Python 质量检查和前端 `lint` / `typecheck` / `build`；前端测试默认是本地必跑项。

## AI Docs

`ai_docs/` 是模板的重要组成部分。它的职责不是“补充阅读材料”，而是作为仓库给 AI 助手和协作者共用的唯一详细事实源。

建议阅读顺序：

1. `ai_docs/START_HERE.md`
2. `ai_docs/INDEX.md`
3. `ai_docs/current/architecture.md`
4. `ai_docs/reference/verification.md`
5. 按任务进入 `ai_docs/current/*`、`ai_docs/standards/*`、`ai_docs/workflows/*`

如果任务涉及前端 UI：

- 先看 `ai_docs/standards/design-system.md`
- 再看 `ai_docs/workflows/add-frontend-feature.md`
- 如果项目根目录已经有 `DESIGN.md`，把它和上面两份文档一起作为 UI 工作输入

当前文档覆盖：

- `current/`：当前真实实现
- `standards/`：工程准则和默认约束
- `workflows/`：任务执行流程
- `reference/`：共享事实，例如验证命令、目录结构、工具入口
- `decisions/`：设计决策与架构原因

## Release

推荐发版流程：

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

推送 `v*` tag 后，`.github/workflows/release.yml` 会：

1. 校验 tag 格式
2. 运行 `scripts/generate_release_notes.py`
3. 创建或更新 GitHub Release

如果仓库配置了 `OPENAI_API_KEY`，release notes 会尝试调用模型生成摘要；如果没有，脚本会自动回退到确定性文本，不会阻塞发布。

## License

MIT，见 `LICENSE`。
