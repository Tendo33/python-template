# Current Architecture

## When to read

- 想快速理解仓库现在已经落地了什么时先读这里。
- 想判断某项描述属于“当前实现”还是“后续扩展方向”时先读这里。

## Current truth

这个仓库当前是一个面向 AI 协作的前后端模板，而不是已经内建完整业务系统的脚手架。

它已经提供：

- Python 包基础设施：配置、日志、上下文、协议、模型、工具模块
- React + Vite 前端 starter
- 一组仓库维护脚本和 release 流程
- 根目录 AI 入口文件：`AGENTS.md` 和 `CLAUDE.md`
- 一套精简后的 `ai_docs/` 文档系统

它当前没有内建：

- 完整的 HTTP API / service / repository / domain 分层实现
- 数据库 schema、迁移或持久化层
- 真实业务 full-stack demo
- 多页面前端应用或复杂前端状态架构

## Subsystems

- backend 的真实实现见 [backend.md](backend.md)
- frontend 的真实实现见 [frontend.md](frontend.md)
- scripts 的真实实现见 [scripts.md](scripts.md)
- release 的真实实现见 [release.md](release.md)

## Shared references

- 项目结构见 [project-structure.md](../reference/project-structure.md)
- 命名与路径规则见 [naming-and-paths.md](../reference/naming-and-paths.md)
- 验证命令见 [verification.md](../reference/verification.md)
