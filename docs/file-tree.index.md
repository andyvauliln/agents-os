---
about: agent-os/docs/file-tree.md
basis: 981c7ce4dc3d
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T15:07:13Z
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

It lists the same paths as the File Tree page and as git (`git ls-files --cached --others --exclude-standard`). Adding a little information to each line later is an idea still weighed.

## Keep in mind

- When it looks wrong, fix the build and rebuild; never edit it by hand.
