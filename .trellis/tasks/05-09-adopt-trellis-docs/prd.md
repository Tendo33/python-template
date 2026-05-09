# Adopt Trellis Documentation Model

## Goal

Refactor the repository's AI-facing documentation so Trellis becomes the primary
development harness and documentation entrypoint, while preserving the concrete
project facts that currently live in `ai_docs/`.

## What I Already Know

- The user wants to fully embrace Trellis and is open to changing the existing
  documentation structure.
- `.trellis/spec/` is installed from `python-vite-fullstack`.
- The installed spec currently still treats `ai_docs/` as the preferred
  project-doc system.
- Root `AGENTS.md` and `CLAUDE.md` currently route agents through `ai_docs/`.
- `ai_docs/` currently contains 15 markdown files:
  - `START_HERE.md`
  - `INDEX.md`
  - `current/architecture.md`
  - `current/backend.md`
  - `current/frontend.md`
  - `current/release.md`
  - `current/scripts.md`
  - `standards/backend.md`
  - `standards/frontend.md`
  - `standards/design-system.md`
  - `standards/documentation.md`
  - `standards/engineering.md`
  - `reference/project-structure.md`
  - `reference/naming-and-paths.md`
  - `reference/verification.md`
- `.trellis/spec/` already contains matching layers:
  - `backend/`
  - `frontend/`
  - `shared/`
  - `guides/`
  - `big-question/`
- The existing verification commands in `ai_docs/reference/verification.md`
  match the baseline `.trellis/spec/shared/verification.md`, but the `ai_docs`
  version includes CI gate details and a docs/link check.
- The working tree currently has uncommitted Trellis installation files:
  `.agents/`, `.claude/`, `.codex/`, `.trellis/`.

## Assumptions

- Trellis should become the first documentation source for agents.
- Project-specific facts from `ai_docs/current/` and `ai_docs/reference/` should
  not be lost.
- The migration should avoid duplicating the same rule in both `ai_docs/` and
  `.trellis/spec/`.
- Root entrypoints should stay thin.

## Decisions

- Use Approach B: full Trellis migration.
- Remove `ai_docs/` after moving all still-useful project facts into
  `.trellis/spec/`.
- Do not keep an `ai_docs/` compatibility shim.

## Requirements

- Make Trellis the primary AI/development documentation entrypoint.
- Preserve current project facts: architecture, backend/frontend scope, scripts,
  release flow, project structure, naming rules, and verification commands.
- Update root agent entrypoints so they no longer claim `ai_docs/` is the only
  detailed source of truth.
- Resolve contradictions between `.trellis/spec/` and `ai_docs/`.
- Keep changes documentation-focused unless a verification script or path
  changes require small code/script updates.
- Keep the final structure easy for future agents to follow.

## Acceptance Criteria

- [x] `AGENTS.md` points to Trellis first.
- [x] `CLAUDE.md` points to the shared entrypoint and Trellis first.
- [x] `.trellis/spec/` contains or links to all project-specific facts needed
      for backend, frontend, scripts, release, structure, naming, and
      verification.
- [x] Any remaining `ai_docs/` files have a clearly defined reduced role, or the
      directory is removed and all links are updated.
- [x] Markdown links across root docs, `.trellis/spec/`, and any retained docs
      are valid.
- [x] Verification commands for documentation-only changes are documented and
      runnable.

## Definition Of Done

- Relevant markdown link checks pass.
- No root entrypoint tells agents to use `ai_docs/` as the only detailed source
  of truth.
- No important current project fact is lost during migration.
- The final handoff explains the new read order and what happened to `ai_docs/`.

## Out Of Scope

- Changing backend or frontend runtime behavior.
- Rewriting the Trellis marketplace repository.
- Adding new framework dependencies.
- Changing package names or release automation behavior unless required by docs
  link updates.

## Technical Notes

- Current root entrypoints inspected:
  - `AGENTS.md`
  - `CLAUDE.md`
- Current docs inspected:
  - `ai_docs/START_HERE.md`
  - `ai_docs/INDEX.md`
  - `ai_docs/reference/verification.md`
- Trellis spec files inspected:
  - `.trellis/spec/shared/index.md`
  - `.trellis/spec/shared/project-docs.md`
  - `.trellis/spec/shared/verification.md`
  - `.trellis/spec/backend/index.md`
  - `.trellis/spec/frontend/index.md`

## Candidate Approaches

### Approach A: Trellis primary, `ai_docs/` compatibility shim

Keep `ai_docs/START_HERE.md` and `ai_docs/INDEX.md` as short compatibility
redirects to `.trellis/spec/`, then migrate detailed docs into `.trellis/spec/`.

Pros:
- Less disruptive for tools or humans that still open `ai_docs/`.
- Safer if old prompts mention `ai_docs/`.

Cons:
- Leaves an extra directory whose purpose must be remembered.

### Approach B: Full Trellis migration, remove `ai_docs/`

Move project facts into `.trellis/spec/`, update root entrypoints and docs link
checks, then delete `ai_docs/`.

Pros:
- Cleanest mental model.
- No duplicate documentation system.

Cons:
- Bigger diff.
- Any external workflow still referencing `ai_docs/` breaks until updated.

Decision: selected by user.

### Approach C: Hybrid split

Keep `ai_docs/current/` and `ai_docs/reference/`, but move `standards/` into
`.trellis/spec/`.

Pros:
- Conservative and preserves project-fact docs.

Cons:
- Still two documentation systems; likely not what "fully embrace Trellis"
  means.
