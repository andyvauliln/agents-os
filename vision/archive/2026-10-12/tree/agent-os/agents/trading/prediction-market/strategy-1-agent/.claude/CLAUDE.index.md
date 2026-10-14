---
about: agent-os/agents/trading/prediction-market/strategy-1-agent/.claude/CLAUDE.md
node: n-21.1.5
basis: f0f3ed489856
written: 2026-10-07T19:03:05Z
by: knowledge-base-agent
---
# CLAUDE.md

## Summary

The strategy agent's prompt: it makes `pm-strategy-1-agent.opus55-test` the strategy manager, which runs and compares the variants, works with its self-improvement sub-agent [21.1.1.1] and folds a winning change back into the strategy, together with the definition in `docs/` and the config. It is the system's common prompt, plus the domain's trading layer `common/trading-prompt.md`, plus this level's part. Open: whether the shared parts are imported from linked copies or copied in, and whether a fold-back needs the owner.

## Keep in mind

- When you want to try a prompt change, make it a new test variant first; only a tested winner is folded back into this file.
