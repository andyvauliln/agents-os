---
about: agent-os/agents/trading/prediction-market/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/.claude/agents/
node: n-26
basis: 41af2b1d49c8
written: 2026-10-01T00:53:20Z
by: summary-worker
confirmed: 2026-10-09T09:57:03Z
---
# agents/

## Summary

The trading agent's own Claude Code sub-agents, each with its own context and tools, which it may call during a run, for example for research; what they write stays in its own `data/`. They are real files, added later, and linked from nowhere. Unlike the system, domain and strategy levels, a variant has no self-improvement sub-agent: its strategy's SI sub-agent makes new test variants of it instead. Higher-level sub-agents, such as the news digest, never run in this session; their outputs reach the agent as linked data files. Only a placeholder exists so far.

## Keep in mind

- When you add a sub-agent, check its name is free in the registry and the sub-agent index, and list it in `index/subagents.md`.
- When you choose a sub-agent's model, route it in `models.config.json`, not in its file.
