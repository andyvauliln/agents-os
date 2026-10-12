---
about: agent-os/docs/file-tree.md
node: n-57.5
written: 2026-10-12T00:00:00Z
by: knowledge-base-agent
---
# file-tree.md

## What it is

A plain list of every path in the repository, one per line, with nothing else on the line: no comments, numbers or other metadata. It gives people and AI a fast, exact map of what exists.

## Who looks after it

The project IDE agent, with the `ide-build` skill: the build writes it. Nobody writes it by hand.

## When and how it changes

Every round, when the page is built: the build lists the paths in the repository and writes the file again, so it always matches the disk and the page.

## Who uses it, and when

Claude Code started in the system folder reads it after the project and system docs, to know what exists. The owner and any agent use it to find a file fast.

## Where it is mentioned

`agents/system/CLAUDE.md` (the reading list), the project README and rebuild prompt, and the `ide-build` skill.

## Related knowledge

It lists the same paths as the File Tree page and as git (`git ls-files --cached --others --exclude-standard`). The tree notes in `vision/docs/file-tree.md` are a different file: the planned tree with one section per item. Adding a little information to each line later is an idea still weighed.

## Keep in mind

- When it looks wrong, fix the build and rebuild; never edit it by hand.
