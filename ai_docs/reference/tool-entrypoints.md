# Tool Entrypoints Reference

## Purpose

本文件集中说明仓库里的 AI 入口文件和生成方式。

## Root entrypoints

- `AGENTS.md`
  - 跨工具公共入口
  - 指向 `ai_docs/START_HERE.md`、`ai_docs/INDEX.md` 和 `ai_docs/reference/verification.md`

- `CLAUDE.md`
  - Claude Code 项目入口
  - 指向 `AGENTS.md` 和与任务相符的 workflow

## Current scope

- 当前仓库只维护根入口文件：`AGENTS.md` 和 `CLAUDE.md`
- 不再维护额外的 tool-specific rules 或 skill adapter 目录
- `ai_adapter_config.json` 是生成目标的显式配置入口

## Generation policy

- 以上入口由 `scripts/sync_ai_adapters.py` 生成或覆写
- 生成哪些入口文件由 `ai_adapter_config.json` 控制
- 如果配置关闭了某类已生成入口，可运行 `scripts/sync_ai_adapters.py --prune` 清理旧文件
- 如果需要调整入口结构，先改 `ai_docs/` 和脚本，再重新生成
- 不要直接手改生成文件中的共享正文

## Validation policy

- `scripts/check_ai_docs.py` 复用生成脚本的目标集检查入口文件是否存在、是否保持轻量、是否链接到正确的 canonical 文档
