---
about: agent-os/agents/trading/prediction-market/.claude/agents/pm-self-improvement-agent.md
node: n-19.1.1.2
basis: e18b808eb560
written: 2026-10-07T18:56:50Z
by: knowledge-base-agent
confirmed: 2026-10-09T09:57:03Z
---
# pm-self-improvement-agent.md

## Summary

The domain's self-improvement sub-agent: it compares strategies and their variants across the prediction-market domain, proposes new strategies or variants, and spots domain-wide issues. Proposed: it runs nightly as the `domain-self-improvement` job, reads every strategy through the domain's `subagents.link/` folders (each strategy's daily variant report included), keeps lessons in `agent-memory/pm-self-improvement-agent/MEMORY.md`, and writes research to `research/` and logs to `logs/`. Its template is the shared one with the trading lines in `docs/common/strategy-si-templates.md`.

## Keep in mind

- When you want to try a change, make it a new test variant; never edit a running agent, touch live agents or raise risk caps.
- When you compare strategies, use returns over the same period and test against test; backtests feed research but never decide.
- When you write its memory, store lessons and research item ids, never the research itself.
