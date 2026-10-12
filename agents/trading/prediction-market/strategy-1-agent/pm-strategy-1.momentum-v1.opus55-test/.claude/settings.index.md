---
about: agent-os/agents/trading/prediction-market/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/.claude/settings.json
node: n-24.6
basis: 636ae21e1b81
written: 2026-10-07T19:03:05Z
by: knowledge-base-agent
---
# settings.json

## Summary

The variant's committed Claude Code settings: permissions, hooks, env, default model, status line and output style. Like every level's, it denies reading and editing `.secrets/live/**`, while `test/.env` stays readable. The rest is proposed: `env.AGENT_OS_ENV` set to `test`, and a `PostToolUse` hook that runs relink after a `configs/*.links.json` edit and then the `on_change` tests. Runs started by the scheduler take their model from the job or `models.config.json`, not from here.

## Keep in mind

- When you edit this file, keep the `Read` and `Edit` deny rules for `**/.secrets/live/**`.
- When you add a personal setting (your model, a log level), put it in `settings.local.json` [24.7]; this file is committed and shared.
