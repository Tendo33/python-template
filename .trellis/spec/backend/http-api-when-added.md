# HTTP API When Added

The baseline Python template does not assume an HTTP API. Use this only after a
target project adds one.

## Rules

- Keep handlers thin.
- Validate input at the HTTP boundary.
- Move real business flow into service-level code only when it improves clarity.
- Keep repository/persistence details out of handlers.
- Keep API routes separate from static frontend fallback rules.
- Use finite error codes for public endpoints.
- Do not return tracebacks or internal config in public responses.

## Contract

For every frontend-consumed endpoint, document:

- HTTP method and path
- Request body or query params
- Success response
- Error response
- Auth or origin assumptions
- Whether the endpoint can be cached

## Verification

Add tests for:

- Valid request
- Invalid request
- Expected error response
- Any frontend/static routing interaction
