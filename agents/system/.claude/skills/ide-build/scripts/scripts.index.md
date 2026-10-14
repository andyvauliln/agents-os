---
about: agent-os/agents/system/.claude/skills/ide-build/scripts/
basis: a8d75d5f1e5f
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T15:07:13Z
---
# scripts/

## What it is

The build scripts, in Python with nothing beyond the standard library, plus one page check in JavaScript. `enrich.py` builds the page data from the files on disk with help from `index_files.py` and `tabs.py`, `materialize.py` gives new items their empty metadata files and writes the plain tree, `build_map.py` finds out-of-date How it works files, and `check_page.js` and `check_tree.py` test the page and its tree before it is published. `README.md` explains how to run them.

## Who looks after it

It is written by the owner and project-ide-agent.

## When and how it changes

It changes when a script is added, split, removed or renamed.

## Who uses it, and when

It is read by ide-build, project-ide-agent and knowledge-base-agent.

## Where it is mentioned

It is described in `agents/system/.claude/skills/ide-build/scripts/README.md` and its folder's How it works file `agents/system/.claude/skills/ide-build/ide-build.index.md`.

## Related knowledge

It is read by `agents/system/.claude/skills/ide-build/SKILL.md`. It writes `apps/project-IDE/current-ui/file-tree.data.json`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `agents/system/CLAUDE.md` (section "The File Tree page"), `docs/metadata.md`, `agents/system/docs/README.md` (section "The project IDE") and `apps/project-IDE/docs/README.md` (section "How the page is built and checked").

## Keep in mind

- When you add code here, give each runnable thing (function, endpoint, script, worker) its own file with one purpose; group related ones in a folder.
