---
about: agent-os/agents/trading/prediction-market/strategy-1-agent/configs/subagents.link/
node: n-21.2.2
basis: 6913695bb49d
written: 2026-10-01T00:55:34Z
by: summary-worker
confirmed: 2026-10-09T10:03:12Z
---
# subagents.link/

## Summary

The strategy's child links for configs: a real folder with one folder link per trading variant, pointing at that variant's `configs/`. Through it the strategy session and its self-improvement sub-agent read every variant's config, jobs and links files, to compare them and see what a challenger changed. `relink` builds the entries from the folder tree when a variant is created and removes them after a variant is deleted; no links file lists them. The strategy only reads here. Every content folder of the strategy has the same `subagents.link/`.

## Keep in mind

- When you scan the strategy's files, never follow `subagents.link/` recursively; go down one child at a time.
- When you create or delete a variant, let relink update this folder; never add or remove a link by hand.
