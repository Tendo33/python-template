# Project Structure

## Current Repository Shape

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
│   ├── src/features/             # Reserved feature modules, currently empty
│   ├── src/hooks/                # Reserved hooks directory, currently empty
│   ├── src/lib/                  # Shared frontend utilities
│   ├── src/styles/               # Global styles and tokens
│   └── src/test/                 # Frontend test setup
├── .trellis/spec/                # Trellis specs and project facts
├── .github/workflows/            # CI and release workflows
├── AGENTS.md                     # Cross-tool root entrypoint
├── CLAUDE.md                     # Claude root entrypoint
├── README.md
└── pyproject.toml
```

## Current Frontend Starter

- Current page entry: `frontend/src/app/App.tsx`
- Shared components: `frontend/src/components`
- Current stable frontend utility file: `frontend/src/lib/utils.ts`
- `frontend/src/features` and `frontend/src/hooks` exist but do not yet contain
  business-level code.

## Recommended Future Expansion

If the project grows, extend along existing paths instead of adding unrelated
top-level directories:

- Add frontend feature modules under `frontend/src/features/*`.
- Add shared hooks under `frontend/src/hooks`.
- Add stable shared frontend helpers under `frontend/src/lib`.
- Add backend `api/`, `service/`, `repository/`, and `domain/` only when the
  real project needs those layers.
