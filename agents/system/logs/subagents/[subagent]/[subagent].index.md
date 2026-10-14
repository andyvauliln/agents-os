---
about: agent-os/agents/system/logs/subagents/[subagent]/
basis: 981c7ce4dc3d
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T15:07:13Z
---
# subagents/[subagent]/

## What it is

One log folder per system sub-agent, named after it, such as `news-digest`. Each call is one JSONL line: time, sub-agent, model, number of input files, output path, duration, cost and status. The cost of a shared sub-agent counts to the level that runs it, not to its readers (still open). The format is proposed.

## Who looks after it

It is written by the system helper it is named after, at run time.

## When and how it changes

It changes when a system helper is created; then every call adds a line. It is a name pattern, not a real item: it tells what each item made from it will hold.

## Who uses it, and when

It is read by the system agent; sys-self-improvement-agent; and the owner, on the File Tree page.

## Where it is mentioned

It is described in `agents/system/logs/subagents/` and its folder's How it works file `agents/system/logs/subagents/subagents.index.md`.

## Related knowledge

It is written by `agents/system/.claude/agents/`. It has the same format as `agents/system/data/subagents/[subagent]/`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `docs/metadata.md` and `agents/system/docs/README.md` (section "Logs").

## Keep in mind

- When you log a call's cost, name the field `cost_usd`; the drafts' `usd` does not match the other logs.
