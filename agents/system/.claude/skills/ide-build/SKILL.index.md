---
about: agent-os/agents/system/.claude/skills/ide-build/SKILL.md
basis: d5fff2f3cc0b
written: 2026-10-15T07:11:30Z
by: knowledge-base-agent
confirmed: 2026-10-15T11:08:51Z
---
# SKILL.md

## What it is

The steps that keep the page in step with the disk and rebuild it, all from the files themselves: give each new item its empty metadata files, keep a `.gitkeep` in each empty folder and write `docs/file-tree.md` again (`materialize.py`); check that every How it works file is current and none is left over (`build_map.py`); build the page data from every file git keeps and its metadata files, with the next version (`enrich.py`); check that the page tree equals the files in git (`check_tree.py`); test the page on a desktop and a phone width (`check_page.js`); publish it at the same link; and tell the owner in plain words what changed. Its scripts table also names `rebuild.py`, the lighter rebuild that `start.sh` runs at each start of the IDE. A change the owner made on the page reaches the disk first, through `ide-sync`. The same steps in ASD-STE100 are in `docs/metadata.md`, section 11.

## Who looks after it

It is written by the owner, project-ide-agent and knowledge-base-agent.

## When and how it changes

It changes when a build step, script, check or the way the page is published changes.

## Who uses it, and when

It is read by project-ide-agent and ide-sync (its last step).

## Where it is mentioned

It is described in `apps/project-IDE/docs/README.md` and its folder's How it works file `agents/system/.claude/skills/ide-build/ide-build.index.md`.

## Related knowledge

It reads `agents/system/.claude/skills/ide-build/scripts/`. It writes `apps/project-IDE/current-ui/file-tree.data.json` and `docs/file-tree.md`. It is read by `agents/system/.claude/skills/ide-sync/SKILL.md`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `agents/system/CLAUDE.md` (section "The File Tree page"), `docs/metadata.md`, `agents/system/docs/README.md` (section "The project IDE") and `apps/project-IDE/docs/README.md` (section "How the page is built and checked").

## Keep in mind


