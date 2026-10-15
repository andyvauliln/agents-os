---
about: agent-os/apps/
basis: 0324cce385ea
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-15T10:41:12Z
---
# apps/

## What it is

Applications and projects: our own apps, the outside apps we use and repositories cloned only to study them. Today it holds `docs/` (the apps vision, README, README twin and rebuild prompt), the owner's project IDE in `project-IDE/` (the File Tree page, its server and this project's records), the prediction-market domain's trading dashboard in `trading-ui/`, empty and waiting for stage two, and `temp/` for research clones. Every app has its own `docs/`. An outside app we use is meant to be forked on GitHub and get its own folder with `docs/` and `repo/`: `main` holds our changes, `upstream` follows the source. None is brought in yet. Still open: whether agents may clone on their own and how a fork sits in the repository.

## Who looks after it

It is written by the owner, knowledge-base-agent and project-ide-agent (ide-sync).

## When and how it changes

It changes when an app is added, updated from its source or removed, or the rules for outside code change.

## Who uses it, and when

It is read by the owner, every agent before working on an app and an AI rebuilding the repository.

## Where it is mentioned

It is described in `apps/docs/README.md`, `apps/docs/vision.md`, `docs/README.md` and its folder's How it works file `agent-os.index.md`.

## Related knowledge

It is built from `apps/docs/rebuild-prompt.md`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `docs/metadata.md`, `apps/docs/README.md` and `docs/README.md` (section "Apps").

## Keep in mind

- When you clone a repository only to study it, put it in `temp/`; never commit the clone.
- When we start using an outside app, fork it first and change only our `main` branch; never change `upstream`.
- When an app is added, updated from its source or removed, update its docs and its row in the apps list in the same change.
