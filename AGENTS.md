# python-template

Python 项目的脚手架模板，不是业务仓库。Python `>=3.10`，后端包 + Vite 前端。

模板改动会外溢到已经从这里派生的项目，改结构、改默认依赖、改脚本前先想清楚影响。

## 结构

- `src/python_template/`：包代码，按 `config/`、`contracts/`、`core/`、`models/`、`observability/`、`utils/` 分层。
- `frontend/`：Vite + TypeScript，包管理用 pnpm。
- `tests/`：`test_public_api.py`、`test_settings.py`、`test_context_scope.py`，以及 `agent_contracts/`、`template_flow/` 两组模板自身行为的用例（测试模板产物的形状，不要随意删）。
- `scripts/`：`rename_package.py`（派生时改包名）、`update_version.py`、`generate_release_notes.py`、`run_vulture.py`、`setup_pre_commit.py`。
- `VERSION` 与 `CHANGELOG.md` 要和脚本改法保持一致。

## 命令

```bash
uv sync
uv run pytest
uv run ruff check .
pnpm --prefix frontend install
pnpm --prefix frontend run dev
pnpm --prefix frontend run lint
pnpm --prefix frontend run typecheck
pnpm --prefix frontend run test
pnpm --prefix frontend run build
```

## 改模板时的规矩

- 优先让模板可派生：占位名要能被 `scripts/rename_package.py` 全部替换干净。
- 改了 `AGENTS.md` 的结构，同步检查从本模板派生的仓库是否也要更新。
- 不往模板里塞具体业务逻辑或密钥。
