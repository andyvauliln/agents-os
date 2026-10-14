---
about: agent-os/agents/system/docs/rebuild-prompt.md
basis: 55de3b7ee67a
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T19:42:37Z
---
# rebuild-prompt.md

## What it is

The prompt an AI coding agent follows to build the system domain, `agents/system/`, from nothing. It gives the task and the limits, the system in brief, the ground rules, the exact tree, the conventions, every part with its formats, scripts and check, the build order, the acceptance checks and the list of things not to build. It builds only `agents/system/` and points to the prompts below it.

## Who looks after it

The knowledge base agent writes it with the `rebuild-prompt-doc` skill. The owner can also change it on the File Tree page.

## When and how it changes

It changes when a name, a format, the tree, a script's behaviour, the build order or a check changes, and when an open point is settled. The agent edits the part it touches and the matching checks, after the vision, the README and its ASD-STE100 version are in line.

## Who uses it, and when

An AI rebuilding the system reads it top to bottom and follows it. The owner reads it to check what "the same system" means. The project's rebuild prompt sends the builder here after it builds the root.

## Where it is mentioned

The project's rebuild prompt (`docs/rebuild-prompt.md`) lists it among the child prompts; the system's README names it among the system's docs; `CLAUDE.md` names its skill in the table of docs.

## Related knowledge

The level above is `docs/rebuild-prompt.md` (root, keys, docs, apps); the level below is `agents/trading/docs/rebuild-prompt.md`; the IDE's own build is `apps/project-IDE/docs/rebuild-prompt.md`. Its facts come from the system's README.

## Keep in mind

- When you add a part, add its check and, if needed, a build-order step.
- When a point is still open, list it under "Do not build"; never settle it here.
- When you give an example config, mark choices the owner has not made as defaults.
- When you mention keys, write key names only.
