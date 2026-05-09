# Project Docs

Trellis is the primary project-doc system for this repository.

## Expected Layout

```text
.trellis/spec/
├── README.md
├── backend/
├── frontend/
├── shared/
├── guides/
└── big-question/
```

## Documentation Rules

- `shared/` stores repository-wide facts, verification commands, structure,
  naming, scripts, release flow, and documentation rules.
- `backend/` stores Python package/backend guidance.
- `frontend/` stores React + Vite frontend guidance.
- `guides/` stores task flow and thinking guides.
- `big-question/` stores recurring pitfalls and debugging notes.
- Root files such as `AGENTS.md` and `CLAUDE.md` should link into
  `.trellis/spec/` instead of duplicating the full text.
- If behavior, structure, scripts, adapters, public APIs, or verification
  commands change, update the related docs in the same change.
- Do not keep a parallel detailed docs tree outside `.trellis/spec/`.

## Tone

Prefer short operational docs over tutorial prose. Agents should be able to find
the right file, understand the boundary, and run the correct check quickly.
