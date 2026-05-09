# Claude Code Project Instructions

## Read Order

1. Start at [AGENTS.md](AGENTS.md)
2. Use [.trellis/spec/README.md](.trellis/spec/README.md) for the Trellis spec overview
3. Use [.trellis/spec/shared/index.md](.trellis/spec/shared/index.md) for repository-wide facts
4. Run the relevant section in [.trellis/spec/shared/verification.md](.trellis/spec/shared/verification.md)

## Claude-Specific Notes

- Use [AGENTS.md](AGENTS.md) as the shared project entrypoint.
- Route task-specific work through `.trellis/spec/`.
- Keep this file thin; detailed rules live in `.trellis/spec/`.

## Claude Execution Style

### Think Before Coding

- State assumptions explicitly when they shape the solution.
- If multiple valid interpretations exist, surface the tradeoff instead of guessing.
- If something is unclear, stop and clarify before editing.
- If a simpler approach exists, say so before implementing.
- Push back when warranted instead of following a weak approach blindly.
- Name confusion directly rather than hiding it behind implementation.

### Simplicity First

- Implement the minimum change that solves the requested problem.
- Do not add extra features, configuration, or abstraction that was not requested.
- If a simpler solution exists, prefer it.
- Do not add abstractions for single-use code.
- Do not add speculative flexibility.
- Do not add error handling for impossible scenarios.
- If a large solution could clearly be much smaller, rewrite it before shipping.

### Surgical Changes

- Keep diffs tightly scoped to the task.
- Do not refactor adjacent code, comments, or formatting unless the request requires it.
- Clean up only the fallout caused by your own changes.
- Match existing style even when you would normally choose differently.
- If you notice unrelated dead code, mention it instead of deleting it.
- Remove only imports, variables, functions, or docs that your own changes made obsolete.
- Every changed line should trace directly to the user's request.

### Goal-Driven Execution

- For multi-step tasks, keep a brief plan with a verification step for each major change.
- Prefer tests or direct checks that prove the requested outcome.
- Before declaring success, run the relevant commands in [.trellis/spec/shared/verification.md](.trellis/spec/shared/verification.md).
- Translate vague requests into concrete, verifiable goals before implementing.
- Treat bug fixes as reproduction plus proof of fix.
- Treat refactors as behavior-preserving changes that must verify before and after.
- Keep iterating until the success criteria are verified, not merely approximated.
