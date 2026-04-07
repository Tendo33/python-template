# Current Architecture

## When to read

- 想快速理解仓库现在已经落地了什么时先读这里。
- 想判断某项能力是“当前实现”还是“未来推荐扩展”时先读这里。

## Current truth

这个仓库当前是一个面向 AI 协作的前后端模板，不是已经内建完整业务系统的脚手架。

它已经提供：

- Python 包基础设施：配置、日志、上下文、协议、模型、工具模块
- React + Vite 前端 starter
- 一组维护脚本和 release 流程
- 一套给多家 AI 工具消费的入口文件和规则 adapter
- 一套分层的 `ai_docs/` 文档系统

它当前没有内建：

- 完整的 API / service / repository / domain 目录实现
- 完整业务数据库层
- 真实 full-stack demo 业务流
- 多页面前端应用或复杂状态管理

## Subsystems

- backend、frontend、scripts 和 release 的进一步阅读路径请从 `ai_docs/INDEX.md` 进入。

## Shared references

- 项目结构见 [project-structure.md](../reference/project-structure.md)
- 工具入口见 [tool-entrypoints.md](../reference/tool-entrypoints.md)
- 验证命令见 [verification.md](../reference/verification.md)
