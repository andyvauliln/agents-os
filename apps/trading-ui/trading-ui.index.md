---
about: agent-os/apps/trading-ui/
basis: 981c7ce4dc3d
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T15:07:13Z
---
# trading-ui/

## What it is

The prediction-market domain's dashboard, meant as a web app where the owner would watch and control the trading agents: each agent in full, its logs, performance and decisions, new variants to approve, live accounts to approve, and agents to stop or delete. It belongs to stage two and is empty: the folder holds only its metadata files. It may never be needed if the project IDE next to it, `apps/project-IDE/`, does the job; the owner decides when stage two starts.

## Who looks after it

It is written by the owner.

## When and how it changes

It changes when the owner starts stage two and the dashboard is designed, or decides it is not needed. It belongs to stage two and is not built yet.

## Who uses it, and when

It is read by the owner.

## Where it is mentioned

It is described in `apps/docs/README.md` and its folder's How it works file `apps/apps.index.md`.

## Related knowledge

It has the same format as `apps/project-IDE/`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `docs/metadata.md`, `apps/docs/README.md`, `docs/README.md` (section "Apps") and `apps/docs/README.md` (section "The prediction-market dashboard").

## Keep in mind

- When an action touches live money, it needs the owner's approval in the UI; nothing else can grant it.
