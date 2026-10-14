---
about: agent-os/
basis: 2bc2f979831d
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T15:07:13Z
---
# agent-os/

## What it is

The whole repository of the Agent OS: the owner's system that runs AI agents of any kind, such as trading, social media or management. Trading is the first kind; it lives in `agents/trading/`, whose first domain, prediction-market, waits for stage two. The project is in stage one: finish the project IDE, make every metadata file correct and finish the docs at the project, system, trading and apps levels.

The top holds `docs/`, the project docs for people (vision, README and its ASD-STE100 twin, rebuild prompt, the plain file tree and the metadata logic); `agents/`, with the system level in `agents/system/` (its `CLAUDE.md` is the file AI sessions read first) and trading in `agents/trading/`; `apps/`, with the project IDE (the owner's File Tree page and the project's records), the trading dashboard and research clones; `.secrets/`, the keys store, in git except its `.env` files; `README.md`, the front page, empty for now; `HANDOFF.md`, how a new session picks the work up; and `.gitignore`. The planning folder `vision/` is being removed in this change. Every file and folder has a How it works file and a Details file next to it.

## Who looks after it

It is written by the owner; knowledge-base-agent; and project-ide-agent (ide-sync, ide-build).

## When and how it changes

It changes when a top-level folder or file is added, moved or removed, or the stage or the way of working changes.

## Who uses it, and when

It is read by the owner, every agent, Claude Code started in agents/system/ and an AI rebuilding the repository.

## Where it is mentioned

It is described in `docs/README.md`, `docs/vision.md` and `docs/file-tree.md`.

## Related knowledge

It is built from `docs/rebuild-prompt.md`. It is read by `agents/system/CLAUDE.md`. It links to `README.md`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `docs/metadata.md` and `docs/README.md` (section "How the repository is laid out").

## Keep in mind

- When anything needs a secret, list the key name in `secret_keys` and let `load-secret` load it; never write a value anywhere.
- When you change a file, read its whole context first (the levels above included) and bring everything related in line in the same round.
- When you write about the system as a whole, write in general terms: it runs agents of any kind, and trading is one kind that lives in its own folder.
