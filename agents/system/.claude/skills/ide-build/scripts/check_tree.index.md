---
about: agent-os/agents/system/.claude/skills/ide-build/scripts/check_tree.py
basis: 8f6ac821c628
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T15:07:13Z
---
# check_tree.py

## What it is

The last check before publishing: the items of the page data must be exactly the files git keeps, the folders that hold them and the top, with each item's path as its id. The local keys files are the only items allowed on top. It prints "tree ok" or what differs.

## Who looks after it

It is written by the owner and project-ide-agent.

## When and how it changes

It changes when the rule for which items the page lists changes.

## Who uses it, and when

It is read by ide-build and project-ide-agent.

## Where it is mentioned

It is described in `agents/system/.claude/skills/ide-build/SKILL.md` and its folder's How it works file `agents/system/.claude/skills/ide-build/scripts/scripts.index.md`.

## Related knowledge

It reads `agents/system/.claude/skills/ide-build/scripts/index_files.py` and `apps/project-IDE/current-ui/file-tree.data.json`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `agents/system/CLAUDE.md` (section "The File Tree page"), `docs/metadata.md`, `agents/system/docs/README.md` (section "The project IDE"), `apps/project-IDE/docs/README.md` (section "How the page is built and checked") and `agents/system/.claude/skills/ide-build/scripts/README.md`.

## Keep in mind

- When it fails, build again; never edit the page data by hand.
