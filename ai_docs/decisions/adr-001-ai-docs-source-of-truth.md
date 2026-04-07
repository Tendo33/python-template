# ADR-001: `ai_docs/` As The Detailed Source Of Truth

## Status

Accepted

## Context

仓库同时服务多家 AI 工具和人类协作者。如果把详细规则散落在 `AGENTS.md`、`CLAUDE.md`、`.cursor/rules`、skill 文件和 README 里，内容会很快漂移。

## Decision

把 `ai_docs/` 定义为唯一详细事实源，并按 `current/`、`standards/`、`workflows/`、`reference/`、`decisions/` 分层组织。

## Consequences

- 详细正文只维护一次
- adapter 文件可以变薄
- 校验脚本可以围绕单一事实源工作
- 旧文档需要退化为兼容跳转
