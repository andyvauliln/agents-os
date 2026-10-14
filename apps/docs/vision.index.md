---
about: agent-os/apps/docs/vision.md
basis: ed2f5718d050
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T15:07:13Z
---
# vision.md

## What it is

The vision of the apps folder: why the Agent OS has apps, the three kinds (our own apps, research clones, apps we use as a fork), how apps should work for us, the apps today, and what is still open. It is the first thing to read about apps, in plain words for the owner and anyone new.

## Who looks after it

The knowledge base agent, with the `vision-doc` skill and its outline for an app. The owner can also change it on the File Tree page; their edit is folded in at the next sync.

## When and how it changes

It changes when an input changes what apps are for, the rules for outside code, the list of apps, the stage of the project or an open question about apps. The agent finds the sections the input touches, rewrites them so the doc still reads as one story, moves answered questions into place, then brings the README, its ASD-STE100 twin and the rebuild prompt in line, in that order.

## Who uses it, and when

The owner and anyone new read it first to understand apps. Every agent reads it for the big picture before working in `apps/`, and the knowledge base agent reads it before writing the apps README.

## Where it is mentioned

The apps README names it in its first section; the apps rebuild prompt uses its words; the project docs and the system docs point to the apps docs; `docs/file-tree.md` lists it.

## Related knowledge

The apps README describes the same apps exactly, with paths. The project IDE's own vision goes deeper into the IDE. The owner's inputs and decisions in `apps/project-IDE/data/` are behind it.

## Keep in mind

- When you write it, keep paths out of it except in "Going deeper".
- When an app is added or removed, update "The apps today" and the README in the same change.
