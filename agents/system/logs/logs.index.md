---
about: agent-os/agents/system/logs/
basis: 91cc6f2cac14
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T15:07:13Z
---
# logs/

## What it is

The system's shared logs, sorted by source, and the starting point for every log in the system. `system/` is for the machinery's JSONL log (scheduler, relink and link checks, loaded or refused keys, errors, AI costs); `services/` for one line per test or live action of a shared service; `workers/` for the shared workers' logs; `subagents/` for one line per sub-agent call with its cost (the project IDE server logs its requests in `subagents/project-ide-agent/`). Through `subagents.link/` a reader goes down to each domain's logs. Each agent's own logs stay in its own `logs/`. `.gitignore` does not keep runtime logs out of git today; whether it should, the log format and how long logs are kept are open.

## Who looks after it

It is written by the shared scripts (planned), at run time; and relink (planned shared script in agents/system/scripts/system/), for subagents.link/.

## When and how it changes

It changes when a source of shared logs is added or removed, or a domain is added or removed. It is empty for now.

## Who uses it, and when

It is read by the system agent; sys-self-improvement-agent; and the owner, on the File Tree page.

## Where it is mentioned

It is described in `agents/system/docs/README.md` (section "Logs"), `agents/system/docs/rebuild-prompt.md` (section "Logs") and `agents/system/system.index.md`.

## Related knowledge

It is written by `agents/system/scripts/system/`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `docs/metadata.md` and `agents/system/docs/README.md` (section "Logs").

## Keep in mind

- When you write a log, never include a secret value; loggers redact anything `load-secret` resolved.
- When you write a timestamp, use UTC ISO 8601 with `Z`; growing logs are JSONL, one compact object per line.
