# Tool Entrypoints Reference

## Purpose

本文件集中说明仓库里的 AI 入口文件、adapter 层责任和生成方式。

## Root entrypoints

- `AGENTS.md`
  - 跨工具公共入口
  - 指向 `ai_docs/START_HERE.md`、`ai_docs/INDEX.md` 和 `ai_docs/reference/verification.md`

- `CLAUDE.md`
  - Claude Code 项目入口
  - 指向 `AGENTS.md` 和与任务相符的 workflow

## Adapter layers

- `.agents/rules/*`
  - 面向通用 agent 规则系统的轻量 adapter

- `.agents/skills/*`
  - 面向通用 agent skill 系统的轻量 adapter

- `.cursor/rules/*`
  - 面向 Cursor 的轻量规则入口

- `.cursor/skills/*`
  - 面向 Cursor skill 系统的轻量 adapter

- `.claude/skills/*`
  - Claude skills 的路由入口

- `.codex/skills/*`
  - Codex skills 的路由入口

## Generation policy

- 以上入口和 adapter 由 `scripts/sync_ai_adapters.py` 生成或覆写
- 如果需要调整入口结构，先改 `ai_docs/` 和脚本，再重新生成
- 不要直接手改生成文件中的共享正文

## Validation policy

- `scripts/check_ai_docs.py` 负责检查入口文件是否存在、是否保持轻量、是否链接到正确的 canonical 文档
