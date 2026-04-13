# Project Structure Reference

## Purpose

本文件集中说明当前仓库目录结构。其他文档需要引用目录、位置或扩展点时，只链接这里。

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
│   ├── src/app/                  # Current app entry and page test
│   ├── src/assets/               # Static starter assets
│   ├── src/components/           # Shared components and UI primitives
│   ├── src/features/             # Reserved feature modules (currently empty)
│   ├── src/hooks/                # Reserved hooks directory (currently empty)
│   ├── src/lib/                  # Shared frontend utilities
│   ├── src/styles/               # Global styles and tokens
│   └── src/test/                 # Frontend test setup
├── ai_docs/                      # Shared AI and engineering docs
│   ├── current/                  # Current implementation facts
│   ├── standards/                # Working rules and defaults
│   └── reference/                # Shared commands and structure references
├── .github/workflows/            # CI and release workflows
├── AGENTS.md                     # Cross-tool root entrypoint
├── CLAUDE.md                     # Claude root entrypoint
├── README.md
└── pyproject.toml
```

## Current frontend starter

- 当前页面入口在 `frontend/src/app/App.tsx`
- 共享组件位于 `frontend/src/components`
- 当前只有一个稳定的前端通用工具文件：`frontend/src/lib/utils.ts`
- `frontend/src/features` 和 `frontend/src/hooks` 已建目录，但还没有业务级内容

## Recommended future expansion

如果项目继续长大，优先沿着现有目录扩展，而不是平铺新增顶层目录：

- 在 `frontend/src/features/*` 下按业务拆分前端模块
- 在 `frontend/src/hooks` 下沉淀共享 hooks
- 在 `frontend/src/lib` 下放稳定的通用前端工具
- backend 再按真实需要引入 `api`、`service`、`repository`、`domain`

## Usage rule

- 描述当前目录现状时，只引用 `Current repository shape`
- 描述预留扩展方向时，只引用 `Recommended future expansion`
