---
about: agent-os/agents/trading/prediction-market/strategy-1-agent/.claude/settings.json
node: n-21.1.6
basis: 636ae21e1b81
written: 2026-10-01T00:53:12Z
by: summary-worker
confirmed: 2026-10-07T19:05:50Z
---
# settings.json

## Summary

The committed Claude Code settings for sessions in the strategy folder: permissions, hooks, env, model, status line and output style. Like every level's, it denies reading and editing `.secrets/live/**`. A `PostToolUse` hook reruns relink when the strategy's links file is edited and runs the `on_change` tests. The key set is still a proposal, and jobs started by `run-job` take their model from the job or the routing config, not from here.

## Keep in mind

- When you edit it, keep the `Read` and `Edit` deny rules for `.secrets/live/**`.
