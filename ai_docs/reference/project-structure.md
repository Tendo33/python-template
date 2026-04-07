# Project Structure Reference

## Purpose

本文件是项目结构说明的唯一详细事实源。其他文档需要描述目录时，只做用途说明并链接到这里。

## Current repository shape

```text
python-template/
├── src/python_template/          # Python package
│   ├── config/                   # Settings and configuration loading
│   ├── contracts/                # Protocol interfaces
│   ├── core/                     # Runtime context helpers
│   ├── models/                   # Pydantic base and example models
│   ├── observability/            # Logging setup and helpers
│   └── utils/                    # Stable utility modules
├── tests/                        # Python tests
├── scripts/                      # Maintenance and release scripts
├── frontend/                     # React + Vite starter
│   ├── src/app/                  # Current app entry
│   ├── src/components/           # Shared components and primitives
│   ├── src/styles/               # Global styles and tokens
│   └── src/test/                 # Frontend test setup
├── ai_docs/                      # Shared AI and engineering docs
├── .github/workflows/            # CI and release workflows
├── AGENTS.md                     # Cross-tool root entrypoint
├── CLAUDE.md                     # Claude root entrypoint
├── ai_adapter_config.json        # Generated adapter configuration
├── README.md
└── pyproject.toml
```

## Current frontend starter

- 已存在：`frontend/src/app`
- 已存在：`frontend/src/components`
- 已存在：`frontend/src/components/ui`
- 已存在：`frontend/src/styles`
- 已存在：`frontend/src/test`

## Recommended future expansion

这些目录目前不是当前实现，只是推荐扩展方向：

- `frontend/src/features/*`
- `frontend/src/lib`
- `frontend/src/hooks`
- backend 中按项目需要新增 `api`、`service`、`repository`、`domain`

## Usage rule

- 文档里写“当前已经存在什么”时，只能引用 `Current repository shape`
- 文档里写“未来推荐怎么扩展”时，只能引用 `Recommended future expansion`
