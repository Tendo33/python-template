# Naming And Paths Reference

## Purpose

本文件集中维护命名、导入路径、文档路径和根入口文件规则。其他文档需要引用这些规则时，只链接这里。

## Package and import rules

- 永远从包名导入，不要从 `src` 路径导入
- 正确：`from python_template.config.settings import get_settings`
- 错误：`from src.python_template.config.settings import get_settings`
- 对外稳定导入优先走 `python_template` 包级或稳定子模块

## Path naming rules

- Python 文件与目录使用 `snake_case`
- 前端文件与目录遵循当前 starter 约定
- `ai_docs/` 使用 `current/`、`standards/`、`reference/`

## AI docs layering rules

- `current/` 只写当前真实实现
- `standards/` 只写约束、默认值和工作准则
- `reference/` 只写共享事实

## Root entrypoint policy

- 根入口文件为 `AGENTS.md` 和 `CLAUDE.md`
- 根入口文件里的链接必须指向真实存在的文档
