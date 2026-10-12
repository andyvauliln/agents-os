---
about: agent-os/agents/trading/prediction-market/strategy-1-agent/.claude/agents/
node: n-21.1.1
basis: 3d67b0da8e21
written: 2026-10-01T10:43:38Z
by: knowledge-base-agent
confirmed: 2026-10-09T09:57:03Z
---
# agents/

## Summary

The strategy level's Claude Code sub-agents, each with its own context and tools, kept as real files that no other level links. The one named so far is the self-improvement sub-agent [21.1.1.1]: it runs the strategy loop, preparing new test variants that start once the owner approves a report on each, comparing them and folding a winner back into the strategy. Other strategy sub-agents, such as pre-analysis ones, come later from the placeholder; they would write their results to the strategy's own `data/`, where agents link them as data files. Each sub-agent runs as a `subagent` job in the strategy's workers file (proposed).

## Keep in mind

- When you add a sub-agent, give it a `subagent` job in the strategy's workers file and list it in the sub-agent index [2.18.3].
