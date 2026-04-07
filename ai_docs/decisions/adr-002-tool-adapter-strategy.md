# ADR-002: Thin Tool Adapters

## Status

Accepted

## Context

仓库需要兼容多个 AI 工具，而不同工具对入口文件和规则文件的支持方式不同。手工维护多套详细正文会让规则分叉。

## Decision

根入口和工具文件只保留轻量路由职责：

- 指向 `ai_docs/START_HERE.md`
- 指向任务索引和相关 workflow
- 指向共享验证入口

adapter 通过 `scripts/sync_ai_adapters.py` 生成或覆写，校验交给 `scripts/check_ai_docs.py`。

## Consequences

- 工具入口更短、更稳定
- 规则更新先改 canonical docs，再统一生成
- adapter 不再承担详细事实维护
