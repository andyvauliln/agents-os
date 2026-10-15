---
about: agent-os/agents/system/docs/README.md
basis: 17121dfc96f3
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-15T06:43:18Z
---
# README.md

## What it is

The system's README: an exact map of the system domain for people. It describes every part of `agents/system/` and what it shares with every agent, in a fixed order (agents and levels, the system agent and shared files, domains, workers, jobs, links, settings and models, test and live, keys, logs, tests, research, self-improvement, the AI setup, the knowledge base, the project IDE, the server), and ends each part with the path to its docs.

## Who looks after it

The knowledge base agent writes it with the `readme-doc` skill. The owner can also change it on the File Tree page.

## When and how it changes

It changes when a part changes: a folder, an agent, a config, a job, a script, or how parts connect. The agent rewrites that part's section and the overview, then rewrites `README.asd.md` right after and brings the rebuild prompt in line.

## Who uses it, and when

The owner reads it to see how the system is built. `CLAUDE.md` puts it fourth in its reading list, so every Claude reads it before it changes the system. Domain agents read it to learn what they share.

## Where it is mentioned

`agents/system/CLAUDE.md` lists it under Read first; the project's README points to it for the system; the vision's last section points to it; `README.asd.md` names it as its source.

## Related knowledge

Its ASD-STE100 version `README.asd.md` follows it section for section. The vision gives the why; the rebuild prompt gives the same parts as an exact spec. Trading's README (`agents/trading/docs/README.md`) and the IDE's README (`apps/project-IDE/docs/README.md`) cover the levels it points to.

## Keep in mind

- When you change a section here, rewrite the same section in `README.asd.md` in the same round.
- When a part's docs move, fix its "Its docs:" line.
- When you describe a setting that is not decided, mark it proposed or open.
