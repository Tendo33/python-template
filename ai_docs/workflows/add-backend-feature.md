# Add Backend Feature Workflow

## Use when

- 新增或调整 backend 逻辑、配置、模型、工具模块或脚本时。

## Read first

- [backend.md](../current/backend.md)
- [backend.md](../standards/backend.md)
- [naming-and-paths.md](../reference/naming-and-paths.md)

## Implementation sequence

1. 先确认需求落在当前模板已有模块，还是需要新增清晰边界。
2. 优先复用稳定公共导入面和已有模块。
3. 保持函数短小、类型清晰、错误处理显式。
4. 如果新增模型、配置或导出面，同步更新相关文档。
5. 完成后补测试并跑 backend 验证。

## Update docs/tests

- 模型、配置、公共导入面变了就更新 `current/backend.md`
- 行为约束变了就更新 `standards/backend.md`
- bugfix 至少补一个回归测试

## Verify

- 运行 backend 小节：[verification.md](../reference/verification.md)

## Related references

- [project-structure.md](../reference/project-structure.md)
- [tool-entrypoints.md](../reference/tool-entrypoints.md)
