# Project Agent Entrypoint

This file is the cross-tool entrypoint for this repository.

## Working Rules

- Read shared facts before layer-specific guidance.
- Read backend guidance before changing Python package code.
- Read frontend guidance before changing React/Vite code.
- Keep changes minimal, typed, and explicit.

## Execution Style

### Think Before Editing

- State assumptions when they affect the implementation.
- If multiple interpretations exist, surface them instead of choosing silently.
- Prefer clarifying uncertainty before editing files.
- If a simpler approach exists, say so before implementing.
- Push back when warranted instead of mechanically following a weak approach.
- If something is unclear, stop, name the confusion, and ask.

### Simplicity First

- Choose the smallest change that fully solves the task.
- Do not add speculative flexibility, configuration, or abstraction.
- Prefer direct fixes over framework-like restructuring.
- Do not add features beyond what was asked.
- Do not create abstractions for single-use code.
- Do not add error handling for impossible scenarios.
- If a change grows large but could be much smaller, simplify it before shipping.

### Surgical Diffs

- Touch only files and lines that relate to the request.
- Match existing project style and terminology.
- Do not improve adjacent code, comments, or formatting unless required by the task.
- Do not refactor things that are not broken.
- If you notice unrelated dead code, mention it instead of deleting it.
- Remove only the imports, variables, functions, or docs made obsolete by your own change.
- Every changed line should trace directly to the user's request.

### Goal-Driven Verification

- Turn each task into a verifiable outcome.
- For non-trivial work, keep a short plan and verification path in mind before editing.
- Translate vague requests into concrete checks whenever possible.
- Prefer testable targets such as reproducing a bug, proving invalid input fails,
  or confirming behavior before and after a refactor.
- Keep looping until the requested outcome is verified, not just implemented.
