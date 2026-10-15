---
about: agent-os/apps/project-IDE/docs/vision.md
basis: eed5a53f0807
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T15:07:13Z
---
# vision.md

## What it is

The project IDE's vision, the first doc to read about it. It says what the IDE is for (the owner's window on a project built with AI, and the full context every AI works from), why it exists, how it should work for the owner, where it stands, the stage one work still open, and the questions only the owner can answer. It names no files except the README at its end.

## Who looks after it

The knowledge base agent writes it with the `vision-doc` skill, using its outline for an app. The owner can also change it on the File Tree page.

## When and how it changes

It changes when an owner input touches what the IDE is for, how it should behave, its plans or an open question about it. The agent finds the sections the input touches, rewrites them so the doc still reads as one story, moves answered questions into their section, and then brings the IDE's README, its ASD-STE100 version and its rebuild prompt in line, in that order.

## Who uses it, and when

The owner and anyone new to the IDE read it first. The project IDE agent and every AI working on the page read it as background. The knowledge base agent reads it before writing the IDE's other docs.

## Where it is mentioned

The IDE's README names it in its first section. The `vision-doc` skill, the system's `CLAUDE.md` reading list (through the IDE docs), and the apps docs point to it; `docs/file-tree.md` lists it.

## Related knowledge

It must agree with the IDE's README (same words in its "In short"), the rebuild prompt, the system's vision on the project IDE, and the apps vision. It rests on the owner's inputs about the File Tree page, the server, deleting, Apply changes, the real tree, the metadata files and stage one.

## Keep in mind

- When you are about to name a folder or a file, stop: that belongs in the README.
- When the owner decides an idea or answers a question here, move it into its section and update the README and rebuild prompt the same round.
- When you describe the page, say what the owner sees and does, never how the code works.
