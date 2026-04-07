# Fix Bug Workflow

## Use when

- 修复代码缺陷、文档错误、断链、失效规则或 adapter 漂移时。

## Read first

- [engineering.md](../standards/engineering.md)
- 与问题对应的 `current/` 文档
- 与问题对应的 `standards/` 文档

## Implementation sequence

1. 先确认当前真实行为和期望行为。
2. 把修复范围控制在最小安全改动。
3. 如果问题来自文档漂移或 adapter 重复，优先修 canonical source。
4. 同步补回归测试或校验。
5. 跑与影响面相符的验证。

## Update docs/tests

- bug 来自文档不一致时，优先更新 `ai_docs/`
- bug 来自入口漂移时，重新生成 adapter
- 行为 bug 至少补一个回归测试

## Verify

- 运行与你影响面匹配的小节：[verification.md](../reference/verification.md)

## Related references

- [tool-entrypoints.md](../reference/tool-entrypoints.md)
- [naming-and-paths.md](../reference/naming-and-paths.md)
