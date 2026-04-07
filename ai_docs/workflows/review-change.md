# Review Change Workflow

## Use when

- 做提交前自检、代码评审、文档评审或 adapter 评审时。

## Read first

- [engineering.md](../standards/engineering.md)
- [documentation.md](../standards/documentation.md)

## Implementation sequence

1. 检查改动是否写进了正确层级。
2. 检查是否重复维护了共享事实。
3. 检查链接是否稳定、路径是否真实存在。
4. 检查测试和验证是否覆盖影响面。
5. 检查 adapter 是否仍然保持轻量。

## Update docs/tests

- 如发现共享事实重复，收敛到 `reference/`
- 如发现旧文档仍在承载正文，改成兼容跳转

## Verify

- 运行 docs maintenance 和与你影响面匹配的小节：[verification.md](../reference/verification.md)

## Related references

- [project-structure.md](../reference/project-structure.md)
- [tool-entrypoints.md](../reference/tool-entrypoints.md)
