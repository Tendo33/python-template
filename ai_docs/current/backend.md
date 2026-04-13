# Current Backend

## When to read

- 要改 backend 代码前先读这里。
- 需要了解当前 backend 真实实现、公共导入面和配置基线时读这里。

## Current truth

当前 backend 是一个轻量模板基础层，核心包位于 `src/python_template/`。

已经落地的模块：

- `config`：`Settings`、`get_settings()`、`reload_settings()`
- `observability`：`setup_logging()`、`get_logger()` 等日志入口
- `core`：上下文对象与作用域 helpers
- `contracts`：常用 `Protocol`
- `models`：Pydantic 基础模型与示例模型
- `utils`：文件、JSON、日期、装饰器和通用工具

## Settings and configuration

- 当前配置定义在 `python_template.config.settings`
- 基线字段只有 `environment`、`log_level`、`log_file`
- 配置基于 `pydantic-settings`
- `get_settings()` 使用缓存单例
- `reload_settings()` 允许测试场景重载配置

## Models and public exports

- 当前模型位于 `python_template.models`
- 对外公共导出在 `python_template.models.__init__`
- 当前公开导出包括 `BaseModel`、`TimestampMixin`、`User`、`ApiResponse`、`PaginatedResponse`、`ConfigModel`

## Public imports and SDK usage

当前推荐的稳定导入面：

- `python_template.config.settings`
- `python_template.observability.log_config`
- `python_template.utils`
- `python_template.models`
- `python_template.core`

不要从 `src.python_template...` 导入。更细的路径规范见 [naming-and-paths.md](../reference/naming-and-paths.md)。

## What is not here yet

- 当前还没有内建 HTTP API 层
- 当前还没有内建持久化层
- 当前还没有按业务领域拆开的 service / repository / domain 结构

这些属于后续项目扩展方向，具体做法以 standards 文档和当前代码现状为准。

## Shared references

- backend 约束见 [backend.md](../standards/backend.md)
- 项目结构见 [project-structure.md](../reference/project-structure.md)
- 验证命令见 [verification.md](../reference/verification.md)
