---
about: agent-os/agents/system/.claude/skills/file-index/SKILL.md
node: n-10.1.2.2
basis: c163f8888df3
written: 2026-10-07T09:33:39Z
by: knowledge-base-agent
confirmed: 2026-10-07T19:02:04Z
---
# file-index/SKILL.md

## What it is

The instructions the knowledge base agent follows to write and keep the How it works file of every file and folder: where each file goes and how it is named (after its file without the extension, so `vision.md` has `vision.index.md`), its fixed headings, how long it is, and how to write it in plain words for someone new to the project.

## Who looks after it

The knowledge base agent keeps it up to date. Whatever the owner decides about how How it works should look or read goes into it.

## When and how it changes

When the owner changes how How it works should look or read, or how it is kept. The agent updates the skill, then refreshes the index files the change touches.

## Who uses it, and when

The knowledge base agent, after every input or change, once the docs are updated: it lists the out-of-date index files, deepest first, and rewrites or confirms each one. At every sync it also writes the owner's edits from the File Tree page into the files.

## Where it is mentioned

The knowledge base agent's instructions, the last steps of the skill that files every input, the page sections of the vision and README skills, and the file tree.

## Related knowledge

- The index files themselves, one per file and folder.
- Each doc skill's page section, which says what goes under each heading for that doc.
- The map of knowledge to files, which says what each index file is written from.

## Keep in mind

- When you change the headings or the rules here, refresh every index file they touch, deepest first.
- When an index file is still right, confirm it instead of rewriting it, so its parents do not go out of date for nothing.
