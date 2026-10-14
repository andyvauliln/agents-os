---
about: agent-os/agents/system/logs/
basis: 91cc6f2cac14
written: 2026-10-07T19:01:11Z
by: knowledge-base-agent
confirmed: 2026-10-14T15:07:13Z
---
# logs/

## Summary

The system's shared logs, sorted by source, and the UI's starting point for every log in the system. `system/` holds the machinery's JSONL log (scheduler, triggers, relink and link checks, loaded or refused keys, errors, AI costs); `services/` one line per test or live action of a shared service; `workers/` the shared workers' logs; `subagents/` one line per sub-agent call with its cost. Through `subagents.link/` the UI goes down to each domain's logs and the levels below. Each agent's own logs stay in its own `logs/`. The content is git-ignored runtime output; log format and retention are still open.

## Keep in mind

- When you write a log, never include a secret value; loggers redact anything `load-secret` resolved.
- When you write a timestamp, use UTC ISO 8601 with `Z`; growing logs are JSONL, one compact object per line.
