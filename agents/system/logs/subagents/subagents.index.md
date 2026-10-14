---
about: agent-os/agents/system/logs/subagents/
basis: 6f8c6087e8ab
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T19:42:37Z
---
# subagents/

## What it is

The logs of the system's helpers, one folder per helper, one line per call with its cost. The project IDE server is set to log each request sent from the File Tree page in `project-ide-agent/` here. Today it holds only the name pattern `[subagent]/`.

## Who looks after it

It is written by the system's helpers, at run time; and the File Tree page's server, for its requests.

## When and how it changes

It changes when a system helper is added or removed. It is empty for now.

## Who uses it, and when

It is read by the system agent; sys-self-improvement-agent; and the owner, on the File Tree page.

## Where it is mentioned

It is described in `agents/system/docs/README.md` (section "Logs"), `agents/system/logs/` and its folder's How it works file `agents/system/logs/logs.index.md`.

## Related knowledge

It is written by `agents/system/.claude/agents/`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `docs/metadata.md` and `agents/system/docs/README.md` (section "Logs").

## Keep in mind

- When you write a log line, never include a key value.
