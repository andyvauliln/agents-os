---
about: agent-os/agents/trading/prediction-market/.claude/settings.json
node: n-19.1.6
basis: 636ae21e1b81
written: 2026-10-07T18:56:50Z
by: knowledge-base-agent
---
# settings.json

## Summary

The domain level's shared Claude Code settings, committed to git. Like every level's settings it denies reading and editing `.secrets/live/**`. The other keys are proposed: the default session `model`, `allow` rules for running its scripts, `env` with `AGENT_OS_ENV` (`test` or `live`), a `PostToolUse` hook that runs relink after a links file is edited and runs the `on_change` tests, and `statusLine` and `outputStyle`.

## Keep in mind

- When you edit the deny rules, keep `Read` and `Edit` denied on `**/.secrets/live/**`, and do not deny all of `.secrets/**`: agents may read and update the test keys.
- When you set `model` here, remember it is only the session default; scheduled runs take their model from the job or `models.config.json`.
