# Generated Frontend Assets

## Problem

The frontend works locally, but deployed or backend-served pages show stale UI,
missing assets, or mismatched hashed filenames.

## Common Wrong Fixes

- Commit `frontend/dist/` without a documented reason.
- Point the backend at `frontend/src/`.
- Rebuild frontend manually and forget to update the deploy process.

## Root Cause

Vite production output is generated. The backend can serve it, but the source of
truth remains the frontend source plus the build command.

## Solution

- Keep `frontend/dist/` out of git unless the project explicitly documents
  checked-in static output.
- Make deployment or container build run `pnpm --prefix frontend build`.
- Keep backend static path configurable or clearly documented.
- Test that the backend serves the built asset directory when static serving is
  part of the app.

## Prevention Checklist

- [ ] Frontend build command is in verification.
- [ ] Static output is ignored or intentionally documented.
- [ ] Backend static path is documented.
- [ ] Deploy docs mention frontend build order.
