---
about: agent-os/agents/system/logs/services/[service]/
basis: 981c7ce4dc3d
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T15:07:13Z
---
# services/[service]/

## What it is

One log folder per acting service shared by several domains, named after it. Every action, test or live, is one JSONL line: when, the service, the mode, the agent, the account, the action and its result, `blocked_by_kill_switch` included. A domain's own acting services log in the domain, such as the prediction-market domain's order logs. The format is proposed.

## Who looks after it

It is written by a shared acting service, when one is built.

## When and how it changes

It changes when a shared acting service is created; then every action it takes adds a line. It is a name pattern, not a real item: it tells what each item made from it will hold.

## Who uses it, and when

It is read by the system agent; sys-self-improvement-agent; and the owner, on the File Tree page.

## Where it is mentioned

It is described in `agents/system/docs/README.md` (section "Actions: test and live"), `agents/system/logs/services/` and its folder's How it works file `agents/system/logs/services/services.index.md`.

## Related knowledge

The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `docs/metadata.md`, `agents/system/docs/README.md` (section "Logs") and `agents/system/docs/README.md` (section "Actions: test and live").

## Keep in mind

- When you build an acting service, log every action here, test or live, blocked ones included.
