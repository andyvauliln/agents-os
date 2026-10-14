---
about: agent-os/apps/project-IDE/docs/README.md
basis: 7babe3db53ee
written: 2026-10-12T00:00:00Z
by: knowledge-base-agent
confirmed: 2026-10-14T15:07:13Z
---
# README.md

## What it is

The full manual of the project IDE. It describes every part of the File Tree page and how to use it, the three places the page runs (claude.ai, the owner's server, view only), how the page is built and checked, how the owner's work comes back into the files, the metadata files behind the tabs, how to run the server, who looks after it, where every part lives now and later, and what is still open.

## Who looks after it

The knowledge base agent writes it with the `readme-doc` skill. The owner asked for it to be the complete manual of the IDE, so it is longer than the skill's usual length for an app. The owner can also change it on the page.

## When and how it changes

It changes after every change to a part of the IDE: the page, the build scripts, the sync, the server or its settings, the metadata files, or where a part lives. It is updated after the vision and before its ASD-STE100 version and the rebuild prompt. The agent rewrites the parts the change touches, keeps "Still open in the design" current and checks every docs path.

## Who uses it, and when

The owner reads it to learn or check how the IDE works. The project IDE agent and every AI read it before working on the page, its build, its sync or its server. Claude Code started in the system folder reaches it from the system's `CLAUDE.md`.

## Where it is mentioned

The IDE's vision ends by naming it. The system's `CLAUDE.md` lists it as the IDE docs to read. The system and apps READMEs point to it for the project IDE. `README.asd.md` is its ASD-STE100 copy.

## Related knowledge

It must agree with the IDE's vision and rebuild prompt, the `ide-build` and `ide-sync` skills, the project IDE agent, the server's README, the build scripts' README and the page itself. The page and its scripts are the facts it describes; when they disagree, the code and the notes win and the README is fixed.

## Keep in mind

- When you change the page, a script, the server or a skill of the IDE, update the matching part of this manual the same round, then README.asd.md.
- When you give a path, check it exists; say where it lives while we plan and where it goes later.
- When you write about a key, write its name only, never its value.
