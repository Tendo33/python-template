# Current Release

## When to read

- 准备发版、更新 changelog 或调整 release notes 流程时先读这里。

## Current truth

当前仓库通过 `.github/workflows/release.yml` 处理 tag 触发的发布流程。

当前发版链路包括：

- 更新版本号
- 运行本地验证
- 创建并推送 `v*` tag
- 由 GitHub Actions 生成或更新 Release

## Release notes

- release notes 由 `scripts/generate_release_notes.py` 生成
- 脚本会读取 tag、上一个 tag、changelog 和 commits
- 有模型凭据时尝试生成摘要；失败时自动回退

## Shared references

- 验证命令见 [verification.md](../reference/verification.md)
- 其它阅读路径请从 `ai_docs/INDEX.md` 进入
