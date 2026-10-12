---
about: agent-os/agents/system/.claude/settings.json
node: n-10.1.6
basis: 636ae21e1b81
written: 2026-10-07T19:01:11Z
by: knowledge-base-agent
---
# settings.json

## Summary

The committed Claude Code settings for system-level sessions: default model, permissions, environment, hooks, status line and output style. Like every level's settings, it denies reading and editing `.secrets/live/**`, while the test keys stay usable. Proposed: `env.AGENT_OS_ENV` (`test` or `live`) and a `PostToolUse` hook that runs relink after a links file is edited, plus the `on_change` tests. Runs started by `run-job` take their model from the job or [11.11].

## Keep in mind

- When you edit permissions, keep the deny rules `Read(**/.secrets/live/**)` and `Edit(**/.secrets/live/**)`.
- When you set the mode variable, name it `AGENT_OS_ENV`, the name the secrets use; older drafts say `TRADING_OS_ENV` or `TRADING_OS_MODE`.
