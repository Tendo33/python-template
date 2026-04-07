# Naming And Paths Reference

## Purpose

本文件集中维护命名、导入路径、文档路径和兼容策略。其他文档需要引用这些规则时，只链接这里。

## Package and import rules

- 永远从包名导入，不要从 `src` 路径导入
- 正确：`from python_template.config.settings import get_settings`
- 错误：`from src.python_template.config.settings import get_settings`
- 对外稳定导入优先走 `python_template` 包级或稳定子模块

## Path naming rules

- Python 文件与目录使用 `snake_case`
- 前端文件与目录遵循当前 starter 约定
- `ai_docs/` 目录按层命名：`current/`、`standards/`、`workflows/`、`reference/`、`decisions/`

## AI docs layering rules

- `current/` 只写当前真实实现
- `standards/` 只写约束、默认值和工作准则
- `workflows/` 只写任务执行顺序
- `reference/` 只写共享事实
- `decisions/` 只写设计原因

## Legacy document policy

- 旧路径文档保留为兼容入口，不再维护正文
- 旧文档必须明确指向新的 canonical 文档
- 新内容只写进新层级，不回填旧文档

## Adapter file policy

- 当前只维护 `AGENTS.md` 和 `CLAUDE.md` 两个根入口文件
- 入口文件的启用状态由 `ai_adapter_config.json` 声明
- 入口文件只做路由
- 入口文件不维护完整验证命令
- 入口文件不维护长篇设计系统或实现说明
