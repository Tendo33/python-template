# Backend Standards

## When to read

- backend 任务开始前必读。
- 新增配置、模型、服务边界或对外导入面时回到这里。

## Default stack

- Python 3.10+
- `uv`
- `ruff`
- `mypy`
- `pytest`
- Pydantic v2
- `pydantic-settings`
- `loguru`

只有在项目确实需要时，再引入 FastAPI、SQLAlchemy、Alembic。

## Design rules

- handler 保持轻薄
- 业务流程尽量落在 service 层
- 存储细节不要泄漏到更高层
- 任何抽象如果不能让代码更清晰，就不要引入
- 优先直接、易扫描的实现

## Public API and import rules

- 对外稳定导入优先走包级或稳定子模块
- 示例和文档只引用当前存在的真实模块
- 不从 `src.python_template...` 导入

## Configuration and safety

- 配置统一走 `pydantic-settings`
- secrets 只从环境变量或受控配置源读取
- 日志不打印 token、密码或敏感个人数据
- 外部输入必须校验

## Model conventions

- 新模型优先放在 `python_template.models`
- 对外可用模型应进入公共导出面
- 使用 Pydantic v2 API，不继续扩写 v1 风格示例

## Testing rules

- 新行为补测试
- bugfix 至少补一个回归测试
- 纯逻辑优先单元测试
- 真实 I/O 或脚本行为按需要补集成测试

## Shared references

- 当前 backend 现状见 [backend.md](../current/backend.md)
- 命名与路径见 [naming-and-paths.md](../reference/naming-and-paths.md)
- 验证命令见 [verification.md](../reference/verification.md)
