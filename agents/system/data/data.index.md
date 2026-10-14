---
about: agent-os/agents/system/data/
basis: 999a0282665b
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T19:42:37Z
---
# data/

## What it is

The system's shared data, sorted by source, as JSON and Markdown files with no database. `system/` is for the machinery's state (every job's last and next run, the links index of who reads which file); `workers/` for the shared workers' outputs, each a dated file plus a stable `latest.*` that agents link; `subagents/` for sub-agent digests, built once for many readers. Through `subagents.link/` the system reaches each domain's data and the levels below. Each agent keeps its own data in its own `data/`. Nothing runs yet, so it holds only name patterns. `.gitignore` does not keep runtime data out of git today; whether it should is open, as is how "new since the last run" is tracked.

## Who looks after it

It is written by the shared scripts, workers and helpers (planned), at run time; and relink (planned shared script in agents/system/scripts/system/), for subagents.link/.

## When and how it changes

It changes when a source of shared data is added or removed, or a domain is added or removed. It is empty for now.

## Who uses it, and when

It is read by agents, through file links to latest files; the owner, on the File Tree page; and the system agent.

## Where it is mentioned

It is described in `agents/system/docs/README.md` (section "Workers and data"), `agents/system/docs/rebuild-prompt.md` (section "Workers and data") and `agents/system/system.index.md`.

## Related knowledge

It is written by `agents/system/scripts/`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `docs/metadata.md` and `agents/system/docs/README.md` (section "Workers and data").

## Keep in mind

- When you give an agent shared data, link the `latest.*` file through its links file; never copy it.
- When you add data, put it here only if agents in more than one domain use it; data one agent or one domain uses stays in its own folder.
