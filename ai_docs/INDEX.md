# AI Docs Index

## How to use this index

- 按任务场景找文档，不按文件名猜。
- 先看 `current/` 确认当前实现，再看 `standards/` 和 `workflows/`。
- 涉及命令、目录、工具入口时，只引用 `reference/`。

## I want to understand the repository

- 仓库总览：[architecture.md](current/architecture.md)
- 当前项目结构：[project-structure.md](reference/project-structure.md)
- 命名与路径规则：[naming-and-paths.md](reference/naming-and-paths.md)

## I want to change backend code

- 当前 backend 实现：[backend.md](current/backend.md)
- backend 约束：[backend.md](standards/backend.md)
- 推荐执行流程：[add-backend-feature.md](workflows/add-backend-feature.md)

## I want to change frontend code

- 当前 frontend starter：[frontend.md](current/frontend.md)
- frontend 约束：[frontend.md](standards/frontend.md)
- 当前设计系统：[design-system.md](standards/design-system.md)
- 推荐执行流程：[add-frontend-feature.md](workflows/add-frontend-feature.md)

## I want to change full-stack behavior

- 当前系统边界：[architecture.md](current/architecture.md)
- backend 现状：[backend.md](current/backend.md)
- frontend 现状：[frontend.md](current/frontend.md)
- 推荐执行流程：[add-fullstack-feature.md](workflows/add-fullstack-feature.md)

## I want to fix a bug

- 统一 bug 修复流程：[fix-bug.md](workflows/fix-bug.md)
- 验证命令：[verification.md](reference/verification.md)

## I want to review or polish a change

- 工程准则：[engineering.md](standards/engineering.md)
- 文档准则：[documentation.md](standards/documentation.md)
- 评审流程：[review-change.md](workflows/review-change.md)

## I want to release

- 当前发版方式：[release.md](current/release.md)
- 发版流程：[release.md](workflows/release.md)

## I want to update AI adapters

- 工具入口清单：[tool-entrypoints.md](reference/tool-entrypoints.md)
- 工程与文档准则：[engineering.md](standards/engineering.md)
- 设计决策：[adr-002-tool-adapter-strategy.md](decisions/adr-002-tool-adapter-strategy.md)

## I want the design rationale

- 为什么 `ai_docs/` 是唯一详细事实源：[adr-001-ai-docs-source-of-truth.md](decisions/adr-001-ai-docs-source-of-truth.md)
- 为什么 adapter 要保持轻量：[adr-002-tool-adapter-strategy.md](decisions/adr-002-tool-adapter-strategy.md)
