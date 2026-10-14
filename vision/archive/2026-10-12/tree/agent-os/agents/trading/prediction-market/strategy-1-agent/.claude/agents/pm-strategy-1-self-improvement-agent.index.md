---
about: agent-os/agents/trading/prediction-market/strategy-1-agent/.claude/agents/pm-strategy-1-self-improvement-agent.md
node: n-21.1.1.1
basis: 46d7e215a462
written: 2026-10-01T10:43:25Z
by: knowledge-base-agent
confirmed: 2026-10-09T09:57:03Z
---
# pm-strategy-1-self-improvement-agent.md

## Summary

The strategy's self-improvement sub-agent, `pm-strategy-1-self-improvement-agent`, which runs the strategy loop. It reads the variants' logs, data, docs and tests through the strategy's `subagents.link/` folders, plus research, news and owner comments; opens a research item per idea; prepares a new test variant with `create-agent` and adds tests; the variant may change anything, and it starts only after the owner has read a report on it and approved it. Winners are folded back into the strategy. Its nightly job and memory place are proposals. Open: may it retire losing variants itself?

## Keep in mind

- When you try a change, make it a new test variant with its own name and `parent`; never edit a running variant, touch live agents, raise risk caps or read `.secrets/live/`.
- When you test a challenger, change one thing against the champion and compare only on the same window and capital.
- When you write memory, keep lessons and research item ids there, not the research itself.
- When you prepare a new variant, write a short report for the owner; it does not start until they approve it.
