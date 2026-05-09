# Frontend Directory Structure

Use this when adding frontend files under `frontend/`.

## Baseline Shape

```text
frontend/src/
├── app/          # App entry and page-level composition
├── assets/       # Static starter assets
├── components/   # Shared components and UI primitives
├── features/     # Real feature modules when they exist
├── hooks/        # Shared hooks
├── lib/          # Shared frontend utilities
├── styles/       # Global styles and theme tokens
└── test/         # Test setup
```

## Placement Rules

| New thing | Default location |
| --- | --- |
| App shell or top-level page composition | `frontend/src/app/` |
| Reusable UI primitive | `frontend/src/components/ui/` |
| Shared component | `frontend/src/components/` |
| Feature-specific component | `frontend/src/features/<feature>/` |
| Shared hook | `frontend/src/hooks/` |
| API helper or stable utility | `frontend/src/lib/` |
| Theme tokens/global styles | `frontend/src/styles/` |
| Test setup | `frontend/src/test/` |

Only add to `features/`, `hooks/`, or `lib/` when the project has a real use
case. Do not move starter code into a heavy architecture before product needs
exist.
