---
about: agent-os/apps/temp/
basis: 981c7ce4dc3d
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T15:07:13Z
---
# temp/

## What it is

Repositories cloned from GitHub only to study them. Each one gets its own folder: the clone itself in `repo/`, which is never committed, and our vision, README and rebuild prompt for it in `docs/`, only when the owner asks. What the research finds goes into the research folder of the agent that studies it, and the clone is deleted when the research is done. An outside app we decide to use is forked instead and gets its own folder in `apps/`. Nothing is cloned yet.

## Who looks after it

It is written by the agent or session that studies an outside repository and the owner.

## When and how it changes

It changes when a repository is cloned to study it, gets its docs on the owner's request, or is deleted when the research is done. It is empty for now.

## Who uses it, and when

It is read by the agent or session that studies an outside repository and the owner.

## Where it is mentioned

It is described in `apps/docs/README.md`, `apps/docs/rebuild-prompt.md` and its folder's How it works file `apps/apps.index.md`.

## Related knowledge

It is checked by `.gitignore`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `docs/metadata.md`, `apps/docs/README.md`, `docs/README.md` (section "Apps") and `apps/docs/README.md` (section "Research clones").

## Keep in mind

- When you clone here, make sure the ignore file keeps the clone out of git before you commit anything.
