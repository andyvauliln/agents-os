---
about: agent-os/apps/project-IDE/docs/
node: n-53.4
basis: 6dc578c86afb
written: 2026-10-12T00:00:00Z
by: knowledge-base-agent
confirmed: 2026-10-12T15:40:56Z
---
# docs/

## What it is

The project IDE's own docs, as every app in `apps/` has them. `vision.md` says what the IDE is for and why; `README.md` is the full manual of the IDE: every part of the page and how to use it, its three modes, the build and checks, the sync, the metadata files, the server and where everything lives; `README.asd.md` is that manual in ASD-STE100; `rebuild-prompt.md` tells an AI how to build the IDE again exactly. Each doc has its How it works and Details files, an example of its structure and its open questions next to it.

## Who looks after it

The knowledge base agent writes the four docs with the `vision-doc`, `readme-doc`, `readme-asd-doc` and `rebuild-prompt-doc` skills, using their outlines for an app. The project IDE agent tells it when a part of the IDE changed. The owner can change any of them on the page.

## When and how it changes

When an owner input or a change touches the IDE: its purpose, the page, the build, the sync, the server or where its parts live. The docs are updated in the order vision, README, README.asd, rebuild prompt, then their metadata.

## Who uses it, and when

The owner, to understand and check the IDE. Every AI before it works on the page, its build, its sync or its server; Claude Code started in the system folder reaches the README from the system's `CLAUDE.md`.

## Where it is mentioned

The system's `CLAUDE.md` (the IDE docs to read), the apps docs and the system README (the project IDE part), the tree notes, and the IDE folder's own How it works.

## Related knowledge

The docs must agree with each other, with the page and its scripts, the `ide-build` and `ide-sync` skills, the project IDE agent and the server's README. Stage one work still open is the same in all four: a view for every kind of file, correct metadata on every item, and tabs that show only metadata files that exist.

## Keep in mind

- When you change these docs, go in the order vision, README, README.asd, rebuild prompt, then their metadata.
- When a part of the IDE changes, update the README and its ASD-STE100 version the same round.
