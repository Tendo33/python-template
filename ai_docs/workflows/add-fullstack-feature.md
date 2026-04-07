# Add Full Stack Feature Workflow

## Use when

- 同时改 backend、frontend、文档或 adapter，或者任务跨越多个子系统时。

## Read first

- [architecture.md](../current/architecture.md)
- [backend.md](../current/backend.md)
- [frontend.md](../current/frontend.md)
- [engineering.md](../standards/engineering.md)

## Implementation sequence

1. 先拆出 backend、frontend、文档和 adapter 的影响面。
2. 先确定当前实现边界，不把未来扩展误写成当前状态。
3. backend 与 frontend 的改动分别遵守对应 standards。
4. 如果改了流程、入口、结构或共享事实，同步更新 `ai_docs/`。
5. 完成后跑 full-stack 验证和 AI docs 校验。

## Update docs/tests

- 更新相关 `current/` 和 `standards/` 文档
- 如改动任务路径或入口，再更新 `workflows/`、`tool-entrypoints.md` 和 adapter
- 行为改动分别补 backend / frontend 测试

## Verify

- 运行 full stack 和 docs maintenance 小节：[verification.md](../reference/verification.md)

## Related references

- [project-structure.md](../reference/project-structure.md)
- [tool-entrypoints.md](../reference/tool-entrypoints.md)
