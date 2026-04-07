# Add Frontend Feature Workflow

## Use when

- 新增或调整 frontend 组件、页面、样式、交互或测试时。

## Read first

- [frontend.md](../current/frontend.md)
- [frontend.md](../standards/frontend.md)
- [design-system.md](../standards/design-system.md)

## Implementation sequence

1. 先确认改动属于 starter 现有范围，还是未来推荐扩展。
2. 复用现有 token、组件模式和主题机制。
3. 如需改视觉或交互系统，先更新设计系统文档。
4. 组件和页面同步考虑响应式、可访问性和测试。
5. 完成后跑 frontend 验证。

## Update docs/tests

- starter 实际能力变了就更新 `current/frontend.md`
- 约束或默认方式变了就更新 `standards/frontend.md`
- 视觉系统变了就更新 `standards/design-system.md`

## Verify

- 运行 frontend 小节：[verification.md](../reference/verification.md)

## Related references

- [project-structure.md](../reference/project-structure.md)
- [tool-entrypoints.md](../reference/tool-entrypoints.md)
