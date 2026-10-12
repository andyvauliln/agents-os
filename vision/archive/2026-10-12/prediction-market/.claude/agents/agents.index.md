---
about: agent-os/agents/trading/prediction-market/.claude/agents/
node: n-19.1.1
basis: f4bdd33a7cdb
written: 2026-10-01T00:53:39Z
by: summary-worker
confirmed: 2026-10-09T09:57:03Z
---
# agents/

## Summary

The domain level's Claude Code sub-agents, each with its own context and tools, kept as real files and not linked from anywhere. The one named so far is `pm-self-improvement-agent`, which compares strategies and their variants across the domain and proposes new ones; its file is still a proposal. Other domain sub-agents, such as pre-analysis sub-agents that digest worker data, follow the placeholder pattern. Proposed: each runs as a `subagent` job in the domain's workers file and hands its results over as data files in the domain's `data/`, never inside a trading agent's session.

## Keep in mind

- When you add a sub-agent, give it a unique name checked against the registry and the sub-agent index, and list it in `index/subagents.md`.
- When you need another agent to use a sub-agent's output, have it link the output file; no level links another level's `.claude/`.
