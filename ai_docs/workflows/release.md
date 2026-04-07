# Release Workflow

## Use when

- 准备发布版本、生成 release notes 或调整发版流程时。

## Read first

- [release.md](../current/release.md)
- [scripts.md](../current/scripts.md)
- [engineering.md](../standards/engineering.md)

## Implementation sequence

1. 确认版本号更新范围。
2. 跑与发布相关的本地验证。
3. 生成或检查 release notes。
4. 推送 `v*` tag，让 GitHub workflow 接管发布。
5. 如流程或脚本有变动，同步更新文档。

## Update docs/tests

- 发版流程变了更新 `current/release.md` 和 `current/scripts.md`
- 验证入口变了更新 `reference/verification.md`

## Verify

- 运行 full stack 和 docs maintenance 小节：[verification.md](../reference/verification.md)

## Related references

- [tool-entrypoints.md](../reference/tool-entrypoints.md)
- [naming-and-paths.md](../reference/naming-and-paths.md)
