---
about: agent-os/agents/system/tests/subagents.link/
basis: 8f7e5ed7a7e2
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T19:42:37Z
---
# subagents.link/

## What it is

The system's view of its domains' tests: one folder link per domain, each pointing at that domain's `tests/`. The system, the UI and self-improvement helpers read the domains' test configs and results through it, going down one `subagents.link/` at a time. Relink builds and removes these links from the folder tree; they are read-only and listed in no links file.

## Who looks after it

It is written by relink (planned shared script in agents/system/scripts/system/), from the folder tree.

## When and how it changes

It changes when a domain is added or removed; relink then adds or removes its link. It is empty for now.

## Who uses it, and when

It is read by the system agent; the owner, on the File Tree page; and sys-self-improvement-agent.

## Where it is mentioned

It is described in `agents/system/tests/`, `agents/system/docs/README.md` (section "How a level reaches its children") and its folder's How it works file `agents/system/tests/tests.index.md`.

## Related knowledge

It links to `agents/trading/prediction-market/tests/`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `docs/metadata.md` and `agents/system/docs/README.md` (section "How a level reaches its children").

## Keep in mind

- When you need to change a domain's test, change it in the domain's own `tests/`; these links are read-only.
