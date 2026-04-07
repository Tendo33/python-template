# Start Task Workflow

## Use when

- 开始任何代码、文档、adapter 或脚本任务时。

## Read first

- [engineering.md](../standards/engineering.md)
- [project-structure.md](../reference/project-structure.md)

## Implementation sequence

1. 确认任务目标、作用范围和风险点。
2. 先读对应 `current/` 文档确认当前实现。
3. 再读对应 `standards/` 文档确认约束。
4. 按任务类型进入对应 workflow。
5. 改动完成后回到共享验证入口。

## Update docs/tests

- 行为、结构、脚本、公共导出或 adapter 变了就补文档。
- 新行为和 bugfix 要补测试。

## Verify

- 运行与你任务匹配的小节：[verification.md](../reference/verification.md)

## Related references

- [naming-and-paths.md](../reference/naming-and-paths.md)
- [tool-entrypoints.md](../reference/tool-entrypoints.md)
