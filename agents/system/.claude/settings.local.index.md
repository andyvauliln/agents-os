---
about: agent-os/agents/system/.claude/settings.local.json
node: n-10.1.7
basis: f1bbd52f2d8e
written: 2026-10-01T00:52:45Z
by: summary-worker
confirmed: 2026-10-07T19:02:04Z
---
# settings.local.json

## Summary

Personal overrides for Claude Code sessions at the system level, such as another `model` or `env.LOG_LEVEL`. It is git-ignored and never needed for the system agent to run, so nothing may depend on it. Everything shared, including the live-secrets deny rules, belongs in `settings.json`.

## Keep in mind

- When you need a setting to hold for every run or every person, put it in `settings.json`; this file is git-ignored and may not exist.
