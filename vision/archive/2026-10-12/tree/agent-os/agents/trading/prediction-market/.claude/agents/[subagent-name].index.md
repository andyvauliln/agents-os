---
about: agent-os/agents/trading/prediction-market/.claude/agents/[subagent-name].md
node: p-agent-os-agents-prediction-market-agents-.claude-agents-subagent-name-.md
basis: 59799bb46a64
written: 2026-10-01T00:53:02Z
by: summary-worker
confirmed: 2026-10-07T18:57:42Z
---
# [subagent-name].md

## Summary

The pattern for one domain-level sub-agent: a Markdown file named after it, with its own context and tools. Proposed names follow `pm-[role]-agent` (no scope at domain level) and must be unique. Proposed frontmatter: `name`, `description`, `tools` and `memory`; the model comes from the routing config, not from the file. Only the self-improvement sub-agent is named so far.

## Keep in mind

- When you add a sub-agent, check its name is free in the registry and the sub-agent index.
- When you choose its model, set it in `models.config.json`, not in this file.
