# AI Tooling Standards

`ai_docs/` 是这个仓库给 AI 助手、自动化工具和协作者共用的事实源。

开始任何实现或文档任务前，先读本文件，再按主题打开对应专项文档。

## ai_docs 索引

| 文档 | 作用 |
| :--- | :--- |
| `AI_TOOLING_STANDARDS.md` | 全局工作流、事实对齐和质量门禁 |
| `BACKEND_STANDARDS.md` | 后端分层、导入、测试和文档约定 |
| `FRONTEND_STANDARDS.md` | 前端固定栈、starter 现状与扩展约定 |
| `frontend_design/DESIGN_SYSTEM.md` | 当前前端视觉 / 交互系统的唯一说明 |
| `SCRIPTS_GUIDE.md` | 仓库维护脚本与发版脚本说明 |
| `MODELS_GUIDE.md` | Pydantic v2 模型约定 |
| `SETTINGS_GUIDE.md` | `pydantic-settings` 配置管理说明 |
| `SDK_USAGE.md` | `src` 布局下的安装与导入方式 |
| `PRE_COMMIT_GUIDE.md` | Git hooks 与本地质量检查说明 |

## 共享工作流

1. 先确认目标、作用范围和风险点。
2. 在改代码前先核对真实实现，不要靠记忆更新文档。
3. 做最小、可审查的修改。
4. 改完后运行相关验证。
5. 如果行为、目录结构、脚本、导出面或工作流变了，顺手更新文档。

## 文档更新原则

文档过期通常不是因为“没写”，而是因为写了以后没有持续对照代码。这个仓库要求：

- 文档描述的内容必须能映射到真实文件、真实命令、真实导出。
- 如果某个目录或能力还没落地，就明确写成“推荐扩展约定”，不要写成“当前已经存在”。
- `README.md` 负责入口认知，`ai_docs/` 负责工程事实，二者口径必须一致。
- 前端设计文档不能保留大段 `[待定]` 占位来冒充规范；当前 UI 是什么，就写什么。
- 示例代码优先选择仓库当前公开 API，而不是历史路径或计划中的理想路径。

## README 标准

这个仓库是模板型项目，`README.md` 需要长期满足这些要求：

1. 顶部一句话说明项目是什么、适合谁。
2. 首屏有快速导航或 badge。
3. 顶部附近提供目录。
4. `Quick Start` 给出从 clone 到首次成功运行的最短路径。
5. 提供 `Use This Template` 或等价说明。
6. 早期放置截图位或真实截图。
7. 说明当前项目结构，不夸大不存在的目录。
8. 集中列出验证命令、发版流程和 `ai_docs/` 入口。

写作规则：

- 先写人能直接拿来用的信息，再写背景解释。
- 段落短、命令可复制、避免空泛口号。
- “当前实现”与“推荐扩展方向”分开写。
- 如果某部分依赖可选环境变量，明确写出有 / 无配置时的行为差异。

## Backend Baseline

- Python 3.10+
- `uv`
- `ruff`
- `mypy`
- `pytest`
- FastAPI + Pydantic v2 + SQLAlchemy + Alembic 仅在项目确实需要时引入

默认后端验证：

```bash
uv run ruff check src tests scripts
uv run ruff format --check src tests scripts
uv run mypy src
uv run pytest
```

## Frontend Baseline

- `pnpm`
- React + TypeScript + Vite
- Tailwind CSS v4
- shadcn/ui 风格组件模式
- Vitest + Testing Library

默认前端验证：

```bash
pnpm --prefix frontend lint
pnpm --prefix frontend typecheck
pnpm --prefix frontend test
pnpm --prefix frontend build
```

## Definition of Done

一个任务只有在下面条件都满足时才算完成：

- 请求中的行为或文档目标已经落实
- 相关命令已经验证
- 文档、配置、脚本说明与当前实现一致
- 没有继续传播已经过期的目录、导入路径或工作流描述
