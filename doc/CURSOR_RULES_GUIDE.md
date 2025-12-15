# Cursor Rules 使用指南

本项目包含一套完整的 Cursor AI 编码规则，帮助 AI 助手更好地理解项目规范并生成符合最佳实践的代码。

## 📁 文件结构

```
python-template/
├── .cursorrules                    # 主规则文件（Cursor 自动加载）
└── python-template-cursorrules/    # 详细规则文档（参考资料）
    ├── README.md                           # 规则概述
    ├── .cursorrules                        # 规则备份
    ├── python-general-coding-style.mdc     # 通用编码风格
    ├── python-utility-structure.mdc        # 项目结构规范
    ├── python-configuration-management.mdc # 配置管理
    ├── python-logging-practices.mdc        # 日志记录
    ├── python-error-handling.mdc           # 错误处理
    ├── python-testing-practices.mdc        # 测试规范
    ├── python-tooling-standards.mdc        # 工具链标准
    ├── python-performance-optimization.mdc # 性能优化
    └── python-decorator-patterns.mdc       # 装饰器模式
```

## 🚀 如何使用

### 1. 自动应用（推荐）

Cursor IDE 会自动读取项目根目录的 `.cursorrules` 文件，无需手动配置。

**验证是否生效：**
- 在 Cursor 中打开项目
- 使用 AI 助手编写代码时，它会自动遵循 `.cursorrules` 中定义的规范
- 例如：让 AI 创建一个新的工具函数，它会自动添加类型提示、docstring、错误处理等

### 2. 引用详细规则

当需要特定领域的详细指导时，可以在 AI 对话中引用规则文档：

```
@python-template-cursorrules/python-logging-practices.mdc
帮我实现一个结构化日志记录功能
```

或者：

```
参考 python-testing-practices.mdc 的规范，帮我为 date_utils.py 编写测试
```

### 3. 查看规则内容

**查看主规则：**
```bash
cat .cursorrules
```

**查看特定领域规则：**
```bash
cat python-template-cursorrules/python-configuration-management.mdc
```

## 📋 规则分类

### 核心规则

| 规则文件 | 适用场景 | 关键要点 |
|---------|---------|---------|
| `python-general-coding-style.mdc` | 所有 Python 代码 | 函数式编程、命名规范、类型提示 |
| `python-utility-structure.mdc` | 工具函数组织 | 模块化设计、文件结构、依赖管理 |

### 专项规则

| 规则文件 | 适用场景 | 关键要点 |
|---------|---------|---------|
| `python-configuration-management.mdc` | 配置管理 | Pydantic Settings、环境变量、.env 文件 |
| `python-logging-practices.mdc` | 日志记录 | loguru 配置、结构化日志、日志分级 |
| `python-error-handling.mdc` | 错误处理 | 自定义异常、错误传播、重试逻辑 |
| `python-testing-practices.mdc` | 单元测试 | pytest 规范、测试组织、覆盖率 |
| `python-tooling-standards.mdc` | 工具链使用 | uv、ruff、pre-commit 配置 |
| `python-performance-optimization.mdc` | 性能优化 | 缓存、懒加载、异步操作 |
| `python-decorator-patterns.mdc` | 装饰器开发 | timing、retry、logging 装饰器 |

## 💡 使用示例

### 示例 1：创建新的工具函数

**提示词：**
```
按照项目规范，创建一个新的工具函数用于解析 YAML 配置文件
```

**AI 会自动遵循：**
- ✅ 使用类型提示
- ✅ 添加 Google 风格 docstring
- ✅ 实现错误处理
- ✅ 返回 Optional 类型处理异常情况
- ✅ 使用 loguru 记录日志

### 示例 2：重构现有代码

**提示词：**
```
@python-template-cursorrules/python-performance-optimization.mdc
优化 file_utils.py 中的文件读取性能
```

**AI 会参考规则进行：**
- ✅ 添加 @lru_cache 缓存
- ✅ 使用 pathlib.Path
- ✅ 考虑异步 I/O
- ✅ 实现懒加载

### 示例 3：编写测试

**提示词：**
```
参考 python-testing-practices.mdc，为 date_utils.py 生成完整的测试套件
```

**AI 会生成：**
- ✅ AAA 模式的测试函数
- ✅ 参数化测试
- ✅ 边缘案例测试
- ✅ pytest fixtures
- ✅ 错误场景测试

## 🔧 维护和更新

### 更新规则

1. **修改主规则：**
   ```bash
   # 编辑主规则文件
   code .cursorrules
   ```

2. **同步到备份：**
   ```bash
   # 将更新同步到规则文档目录
   cp .cursorrules python-template-cursorrules/.cursorrules
   ```

3. **更新详细规则：**
   ```bash
   # 编辑特定领域规则
   code python-template-cursorrules/python-logging-practices.mdc
   ```

### 验证规则

**测试规则是否生效：**

1. 在 Cursor 中打开 AI 对话
2. 输入简单的代码生成请求
3. 检查生成的代码是否符合规范

**示例验证命令：**
```
创建一个简单的函数用于计算两个数的和
```

期望输出应包含：类型提示、docstring、类型安全的参数检查。

## 📚 最佳实践

### ✅ 推荐做法

1. **定期审查规则**：随着项目演进，定期更新规则文档
2. **引用特定规则**：处理特定领域问题时，明确引用对应的 .mdc 文件
3. **保持一致性**：确保 `.cursorrules` 与详细规则文档同步
4. **团队共享**：将规则文档纳入 Git，确保团队成员使用相同规范

### ❌ 避免事项

1. **不要删除 `.cursorrules`**：这是 Cursor 自动加载的核心文件
2. **不要过度复杂**：保持规则简洁明了，避免过长的规则文件
3. **不要矛盾规则**：确保不同规则文件之间不存在冲突
4. **不要忽略更新**：工具链升级时（如 Pydantic v3），及时更新规则

## 🎯 快速参考

**常用命令：**

```bash
# 查看所有规则文件
ls -la python-template-cursorrules/

# 搜索特定规则
grep -r "loguru" python-template-cursorrules/

# 统计规则行数
wc -l python-template-cursorrules/*.mdc
```

**在 Cursor 中使用：**

```
# 通用提示
@.cursorrules 按照项目规范创建...

# 引用特定规则
@python-template-cursorrules/python-testing-practices.mdc 帮我编写测试...

# 多规则引用
参考 python-error-handling.mdc 和 python-logging-practices.mdc，
实现一个带日志的错误处理装饰器
```

## 🔗 相关文档

- [配置指南](./SETTINGS_GUIDE.md) - Pydantic Settings 详细说明
- [SDK 使用指南](./SDK_USAGE.md) - 工具函数使用示例
- [Pre-commit 指南](./PRE_COMMIT_GUIDE.md) - Git hooks 配置

## 🤝 贡献

如果发现规则需要改进或补充：

1. 修改对应的 `.mdc` 文件
2. 更新 `.cursorrules` 主文件（如需要）
3. 在此文档中记录变更
4. 提交 Pull Request

---

**提示**: 充分利用这些规则，让 AI 助手成为你最得力的编程伙伴！🚀
