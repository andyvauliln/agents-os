---
about: agent-os/agents/system/scripts/
basis: e9185fe0cced
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T15:09:25Z
---
# scripts/

## What it is

The shared scripts every agent uses, in JS/TS or Python, sorted by kind twice: by sub-folder and by the suffix `[name].[kind].[ext]`. The two general kinds are `system/`, the machinery (create-agent, run-agent, the scheduler and run-job, relink and check-links, load-secret, run-tests, notifier), and `workers/`, the data collectors shared by several domains. A domain keeps its own scripts and kinds, such as the prediction-market domain's `decisions/`, and the system reads them through `subagents.link/`. Agents use a shared script through a file link, so an improvement reaches every agent at once. System-support agents write here; domain and self-improvement agents propose.

## Who looks after it

It is written by the system's helpers; sys-self-improvement-agent (proposes changes); and relink (planned shared script in agents/system/scripts/system/), for subagents.link/.

## When and how it changes

It changes when a shared script is added, moved or removed, or a domain is added or removed. It is empty for now.

## Who uses it, and when

It is read by every agent, through file links to single scripts; the scheduler and run-job (planned); and the owner, on the File Tree page.

## Where it is mentioned

It is described in `agents/system/docs/README.md` (section "Workers and data"), `agents/system/docs/README.md` (section "Jobs and the scheduler") and `agents/system/system.index.md`.

## Related knowledge

It is tested by `agents/system/tests/scripts/`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `docs/metadata.md`, `agents/system/docs/README.md` (section "Workers and data") and `agents/system/docs/README.md` (section "Jobs and the scheduler").

## Keep in mind

- When you name a script, use `[name].[kind].[ext]` and put it in the sub-folder of its kind.
- When a second agent needs an agent-local script, move it to the shared `scripts/` of the nearest level both agents share (here when they are in different domains) and give each a file link; never copy it.
- When you add code here, give each runnable thing (function, endpoint, script, worker) its own file with one purpose; group related ones in a folder.
