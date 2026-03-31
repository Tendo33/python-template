# Backend Development Standards

本文档定义这个模板仓库的后端默认工程规则。

## 默认栈

- Python 3.10+
- `uv`
- `ruff`
- `mypy`
- `pytest`
- Pydantic v2
- `pydantic-settings`
- `loguru`

如果项目需要 HTTP API，再引入 FastAPI。
如果项目需要持久化，再引入 SQLAlchemy + Alembic。

## 当前模板提供的后端基础

当前 `src/python_template/` 已经拆出这些模块：

- `config/`：`Settings`、`get_settings()`、`reload_settings()`
- `observability/`：`setup_logging()`、`get_logger()`、JSON logging、便捷日志函数
- `utils/`：公开的稳定工具导出面
- `core/`：`Context`、`ContextManager` 与上下文作用域 helpers
- `contracts/`：常用 `Protocol`
- `models/`：Pydantic 基础模型与示例模型

写文档或示例时，应优先引用这些真实模块，不要再使用旧的 `utils.setting`、`utils.logger_util` 等历史路径。

## 可读性优先

- 优先直接、清楚的实现，而不是炫技式抽象。
- 函数短小，职责单一。
- 避免深层嵌套和过早抽象。
- 命名要能让业务流和数据流一眼看懂。

## 分层建议

这个模板本身还没有 API / service / repository 目录，但后续项目推荐遵循清晰边界：

- `api`：路由、请求 / 响应模型、鉴权
- `service`：用例编排、业务流程
- `repository`：数据库或外部存储访问
- `domain`：纯业务规则和领域类型

规则：

- handler 保持轻薄
- SQL / session 细节不要泄漏到 service 层
- service 层要能脱离 HTTP 启动流程被测试
- 任何抽象如果不能让代码更清晰，就不要引入

## 导入与公共 API

优先使用这些稳定导入：

```python
from python_template.config.settings import get_settings
from python_template.observability.log_config import get_logger, setup_logging
from python_template.utils import read_json, read_text_file, write_json, write_text_file
from python_template.models import ApiResponse, User
from python_template.core import Context
```

规则：

- 不要从 `src.python_template...` 导入
- 公开 API 走包级或稳定子模块
- 实验性 / 高阶工具可以走具体子模块，但文档里要说清楚原因

## 配置与安全

- 使用 `pydantic-settings`
- secrets 只从环境变量或受控配置源读取
- 不提交真实密钥
- 日志中不打印 token、密码或敏感个人数据
- 外部输入必须校验和清洗

## 数据与事务

- 写路径要有明确事务边界
- 持久化前先做输入校验
- 有 schema 变更时用迁移，不手改线上表结构
- repository 方法保持窄而清晰

## 测试策略

- 单元测试覆盖纯逻辑和边界情况
- 集成测试覆盖真实 I/O、数据库或 API 流程
- 每个 bugfix 至少补一个回归测试
- 文档示例优先使用已经被测试覆盖的公共 API

## Backend README 约定

顶层 README 中的后端部分应满足：

- 安装和验证命令离 `Quick Start` 足够近
- 给一个短小可运行的导入示例，而不是罗列所有模块
- 解释“模板已经提供什么能力”，而不只是贴目录树
- 如果当前仓库还没有 API 层，不要把 FastAPI 写成“已经存在”

## 后端完成标准

- 请求中的行为已实现
- 相关测试通过
- lint / format / type check 通过
- 涉及行为变化时同步更新 README / `ai_docs/`
