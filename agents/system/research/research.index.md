---
about: agent-os/agents/system/research/
basis: 716989d020ab
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T15:07:13Z
---
# research/

## What it is

The system's research history: what was asked about the system itself, what was found and what was decided. `index.json` has one entry per item with its question, status, results summary, decisions and what it led to; each item has its own folder with a `README.md` and every artifact. The main writer is the system's self-improvement helper, for example on why a new model was added to routing; the owner, domain agents and support agents may write too. Through `subagents.link/` the system reads each domain's research. The field names are proposed.

## Who looks after it

It is written by sys-self-improvement-agent, the main writer; the owner; the other helpers and any agent that starts research; and relink (planned shared script in agents/system/scripts/system/), for subagents.link/.

## When and how it changes

It changes when a research item is started or closed, or a domain is added or removed. It is empty for now.

## Who uses it, and when

It is read by sys-self-improvement-agent, before it starts new research; the system agent; and the owner, on the File Tree page.

## Where it is mentioned

It is described in `agents/system/docs/README.md` (section "Research"), `agents/system/docs/rebuild-prompt.md` (section "Research") and `agents/system/system.index.md`.

## Related knowledge

It has the same format as `agents/trading/researches/`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `docs/metadata.md` and `agents/system/docs/README.md` (section "Research").

## Keep in mind

- When you start research, read `index.json` first so you do not repeat work.
- When your research leads to an owner decision, also record it in the decision log.
