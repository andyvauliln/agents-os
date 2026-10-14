---
about: agent-os/docs/metadata.md
basis: 672a15c9c9cf
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T15:07:13Z
---
# metadata.md

## What it is

The full logic of the metadata files, in ASD-STE100: which files every file and folder has next to it, how they are named, what each holds, when one goes stale, how the build finds it and how an agent brings it up to date; also how status, owner inputs, decisions and questions work, and the true state of each Details field.

## Who looks after it

The knowledge base agent, together with the `file-index` skill. The two must always say the same thing.

## When and how it changes

It changes when a rule of the metadata changes: a new metadata file, a new Details field, a new naming rule, a change to the build or the page. The change goes into the `file-index` skill and into this doc in the same round.

## Who uses it, and when

The owner reads it to understand the metadata. Every agent reads it before it writes or changes a metadata file; `CLAUDE.md` lists it in the reading order.

## Where it is mentioned

The project README and its ASD-STE100 twin, the project rebuild prompt, `agents/system/CLAUDE.md` and the `file-index` skill.

## Related knowledge

The `file-index` skill holds the same rules as steps for an agent; the project IDE README tells how the page shows the metadata as tabs.

## Keep in mind

- When you change a metadata rule, change this doc and the `file-index` skill in the same round.
- When a part of the metadata logic is built or changes, update its section and the list of parts not built yet.
