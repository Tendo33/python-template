# AI Docs Start Here

## When to read

- 第一次进入这个仓库时先读这里。
- 当你不确定某个任务该看哪份文档时，先回到这里。

## What this folder is

`ai_docs/` 是这个仓库给 AI 助手、自动化工具和协作者共用的唯一详细事实源。

规则：

- 共享事实只在 `ai_docs/` 维护一次。
- 任务入口文件只做路由，不重复维护完整正文。
- 当前实现、工程准则、任务流程、共享参考、设计决策分别落在不同层。

## Fast path by task

- 想快速理解仓库：先读 [INDEX.md](INDEX.md)，再读 [architecture.md](current/architecture.md)。
- 想做 backend 改动：先读 [backend.md](current/backend.md)，再到 [INDEX.md](INDEX.md) 选择 backend workflow。
- 想做 frontend 改动：先读 [frontend.md](current/frontend.md)，再到 [INDEX.md](INDEX.md) 选择 frontend workflow。
- 想做 full-stack 改动：先读 [architecture.md](current/architecture.md)，再到 [INDEX.md](INDEX.md) 选择 full-stack workflow。
- 想修 bug：先到 [INDEX.md](INDEX.md) 选择 bugfix workflow。
- 想发版：先读 [release.md](current/release.md)，再到 [INDEX.md](INDEX.md) 选择 release workflow。
- 想更新 AI 入口文件或规则：先读 [tool-entrypoints.md](reference/tool-entrypoints.md)，再到 [INDEX.md](INDEX.md) 找 adapter 入口。

## Shared references

- 验证命令唯一来源：[verification.md](reference/verification.md)
- 项目结构唯一来源：[project-structure.md](reference/project-structure.md)
- 命名与路径约定唯一来源：[naming-and-paths.md](reference/naming-and-paths.md)
- 工具入口与适配层说明唯一来源：[tool-entrypoints.md](reference/tool-entrypoints.md)

## Notes on legacy docs

- 旧路径文档仍保留为兼容入口，但正文已经迁到新结构。
- 如果看到旧文档，请按文档里的跳转说明进入新路径，不要继续在旧文档上扩写。
