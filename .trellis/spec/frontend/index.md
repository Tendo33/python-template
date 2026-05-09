# Frontend Index

Read this before frontend work in a Python + Vite fullstack repository.

## Baseline

The frontend is a React + TypeScript + Vite app under `frontend/`.

Common structure:

```text
frontend/src/
├── app/
├── assets/
├── components/
├── features/
├── hooks/
├── lib/
├── styles/
└── test/
```

## Current Truth

The current frontend is a lightweight single-page starter, not a complete
business frontend.

Already implemented:

- React + TypeScript + Vite runtime chain.
- Tailwind CSS v4 tokens and theme bridge.
- `Button` primitive based on `class-variance-authority`.
- Light/dark theme toggle.
- Simple landing page.
- Vitest + Testing Library baseline.

Current page scope:

- Sticky header.
- Brand title.
- Theme toggle button.
- Hero copy and CTA.
- Simple footer.

Current structure:

- `frontend/src/app`: page entry and current page test.
- `frontend/src/components`: shared components and UI primitives.
- `frontend/src/styles`: global styles and tokens.
- `frontend/src/test`: test setup.
- `frontend/src/lib/utils.ts`: current stable frontend utility.
- `frontend/src/features` and `frontend/src/hooks`: reserved, currently no
  business-level implementation.

Not present yet:

- Complex routing.
- Data-fetching layer or state management architecture.
- Multi-page app structure.
- Real feature modules.

## Rules

- Read the project root `DESIGN.md` before any UI work.
- If no `DESIGN.md` exists and the task changes visual design, choose a suitable
  design-md starting point before coding.
- Use `pnpm`.
- Keep TypeScript strict.
- Do not use `any` by default.
- Use semantic design tokens instead of hard-coded color values.
- Prefer shadcn/ui-style primitives for reusable UI atoms.
- Add shared utilities to `frontend/src/lib` only after a second real use case
  appears.
- Keep the starter light until the project has real product flows.

## More Specific Guides

- `directory-structure.md`
- `design-md.md`
- `vite-static-mount.md`
- `components.md`
- `quality.md`
