# Vite Static Mount

Use this when the Python backend serves the built frontend.

## Build Boundary

- Source lives in `frontend/src`.
- Production assets are produced by `pnpm --prefix frontend build`.
- The backend should serve the generated output as static files.
- Do not make Python import frontend source files.
- Do not make frontend code depend on backend internals.

## Routing

- API routes must win before static fallback.
- Static asset paths should be served directly.
- Client-side app routes may fall back to `index.html`.
- Unknown API routes should return API errors, not the frontend shell.

## Configuration

- Keep frontend runtime API base configuration explicit.
- Prefer relative API paths when frontend and backend share the same origin.
- Use environment variables for deploy-specific values.
- Do not expose backend-only secrets through Vite public variables.

## Verification

For static mount changes, run both frontend build and the backend test that
proves static serving or fallback behavior.
