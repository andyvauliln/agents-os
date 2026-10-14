---
about: agent-os/agents/system/
basis: cf844f3ab4b1
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T15:09:25Z
---
# system/

## What it is

The system level of the Agent OS: the system agent and the home of everything every agent shares, whatever its domain. Like every level it has the standard agent folder; its agent, the system manager, oversees the domains, the system's health and its development, and answers the owner's questions about the whole system. `CLAUDE.md` here is the file Claude Code reads first.

Its folders hold what holds for any agent: `configs/` the global settings (test or live, the live list, the general stop switch, jobs, links) and model routing; `scripts/` the shared machinery (create-agent, the scheduler, relink, load-secret, run-tests) and collectors shared by several domains, all still planned; `logs/` and `data/` the shared logs and outputs; `tests/` and `research/`; `docs/` the system's vision, README, README twin and rebuild prompt. Its `.claude/` holds the settings, the skills and the helpers: self-improvement, the knowledge base agent and the project IDE agent.

Agents are meant to use shared files through read-only file links, never copies, and the system reaches each domain through `subagents.link/`, one level at a time. Trading lives in `agents/trading/`, not here.

## Who looks after it

It is written by the owner; knowledge-base-agent; project-ide-agent; and relink (planned shared script in agents/system/scripts/system/), for the child links.

## When and how it changes

It changes when a shared part is added, moved or removed, or a domain is added or removed and its child links change.

## Who uses it, and when

It is read by the owner; every Claude Code session started in agents/system/; the system agent; every agent, through file links to the shared files; and `agents/system/.claude/skills/ide-build/scripts/enrich.py`.

## Where it is mentioned

It is described in `agents/system/docs/README.md`, `agents/system/docs/vision.md`, `agents/system/docs/rebuild-prompt.md`, `agents/system/CLAUDE.md` and `agents/agents.index.md`.

## Related knowledge

It links to `agents/trading/prediction-market/`. It reads `.secrets/`. The rules that apply to it come from `docs/vision.md`, `docs/README.md` (section "The system"), `docs/metadata.md` and `agents/system/CLAUDE.md` (section "Rules").

## Keep in mind

- When agents of different domains need the same agent-local thing, move it into the matching shared folder here and give each a file link; what one domain needs stays in that domain.
- When a rule or setting holds only for one domain, put it in that domain, not here.
- When an owner input or a system change comes in, run it through the knowledge base agent so the docs and the metadata files stay current.
