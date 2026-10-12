---
about: agent-os/agents/trading/prediction-market/strategy-1-agent/
node: n-21
basis: 42bc22ed809c
written: 2026-10-07T19:03:05Z
by: knowledge-base-agent
confirmed: 2026-10-09T09:57:03Z
---
# strategy-1-agent/

## Summary

The strategy-level agent for strategy 1 in the prediction-market domain: it owns one concrete strategy and all its trading variants, and improves the strategy through them. Its ID is `pm-strategy-1-agent.opus55-test`; the folder keeps the name `strategy-1-agent/`. It has the standard agent folder every level shares.

A daily strategy session runs here with the strategy's own `.claude/`. Its self-improvement sub-agent proposes one change at a time, prepares it as a new test variant that starts once the owner approves a report on it, compares the variants every day in a variant report, by the domain's rules in `trading-metrics.md`, and folds a winning change back into the strategy definition, config and prompt, or retires the variant. History stays in `data/` and `research/`. The strategy reads its variants only through `subagents.link/`; the domain reads the strategy the same way.

Main parts: `.claude/` (manager prompt and the SI sub-agent), `configs/` (jobs and links), `data/` (variant report and history), `docs/` (the strategy definition, proposed), and the variant folders.

The loop's details are proposed. Still open: a real strategy name for the folder, whether it carries the ID suffixes, where the strategy definition lives, and whether the SI sub-agent may retire variants itself.

## Keep in mind

- When you want to try a change to the strategy, create it as a new test variant; never edit a running variant in place.
- When you name a variant, start with this strategy's ID: `pm-strategy-1.[own-name]-v[N].[platform-model]-[test|live]`.
- When you read a variant's files, go through `subagents.link/`; those links are read-only.
