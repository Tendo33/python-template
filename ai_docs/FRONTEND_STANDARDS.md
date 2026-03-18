# Frontend Development Standards

This document defines the frontend baseline for this project.

> **Design System**: Before writing any UI code, read `ai_docs/frontend_design/DESIGN_SYSTEM.md`.
> It defines the 5-layer design hierarchy (Principles → Tokens → Components → Patterns → Screens).
> To refactor or redesign UI, **update the Design System document first**, then implement.

## Fixed Stack

| Layer | Choice |
| :--- | :--- |
| Package manager | `pnpm` |
| Framework | React |
| Language | TypeScript (`strict`) |
| Bundler | Vite |
| Styling | Tailwind CSS v4 |
| Component library | shadcn/ui |

> Do not change this stack unless the user explicitly asks.

## Current Project Setup

- Alias: `@` -> `frontend/src` (configured in `vite.config.ts` and tsconfig)
- Global styles: `frontend/src/styles/globals.css`
- shadcn component registry: `frontend/components.json`
- Test stack: Vitest + Testing Library + jsdom

## Directory Convention

```text
frontend/src/
├── app/            # app shell, routing, providers
├── features/       # domain modules
├── components/ui/  # shadcn/ui + shared UI primitives
├── hooks/          # global hooks
├── lib/            # utilities / API clients
├── styles/         # global styles and theme tokens
└── test/           # shared test setup
```

## shadcn/ui Rules

- Use shadcn/ui as the base for shared visual components.
- Prefer component composition over ad-hoc duplicated markup.
- Add components via:

```bash
pnpm --prefix frontend dlx shadcn@latest add <component>
```

## TypeScript and Styling

- Keep `strict` mode enabled.
- Avoid `any`; use `unknown` + narrowing if dynamic.
- Use `cn()` from `frontend/src/lib/utils.ts` for class merging.
- Keep theme tokens in CSS variables (globals.css), not inline style objects.

## Testing and Quality

- Unit/component tests with Vitest + Testing Library
- Co-locate tests (`*.test.tsx`) near implementation when practical
- Prefer `userEvent` over `fireEvent` for interactions

Required checks:

```bash
pnpm --prefix frontend lint
pnpm --prefix frontend typecheck
pnpm --prefix frontend test
pnpm --prefix frontend build
```
