---
about: agent-os/agents/system/.claude/skills/ide-build/scripts/enrich.py
basis: 76ce11ea0217
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T19:42:37Z
---
# enrich.py

## What it is

Builds the page data from the repository on disk: every file git keeps, the folders that hold them and the local keys files, each with its path as its id. For each item it reads the text into `real-files.json`, its How it works and Details files with the state of the How it works file, its Example, Questions and ASD-STE100 files when they exist, and the extra tabs that come from the kind of file. It also reads the decisions for the page's pop-ups, and stamps the data with the next version.

## Who looks after it

It is written by the owner and project-ide-agent.

## When and how it changes

It changes when the page data, a tab, the empty-file rule or how the files on disk and their metadata are read changes.

## Who uses it, and when

It is read by ide-build.

## Where it is mentioned

It is described in its folder's How it works file `agents/system/.claude/skills/ide-build/scripts/scripts.index.md`.

## Related knowledge

It writes `apps/project-IDE/current-ui/real-files.json` and `apps/project-IDE/current-ui/file-tree.data.json`. It reads `agents/system/.claude/skills/ide-build/scripts/tabs.py`, `agents/system/.claude/skills/ide-build/scripts/index_files.py`, `agents/system/.claude/skills/ide-build/scripts/build_map.py`, `apps/project-IDE/data/overrides.json` and `apps/project-IDE/data/decisions.md`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `agents/system/CLAUDE.md` (section "The File Tree page"), `docs/metadata.md`, `agents/system/docs/README.md` (section "The project IDE"), `apps/project-IDE/docs/README.md` (section "How the page is built and checked") and `agents/system/.claude/skills/ide-build/scripts/README.md`.

## Keep in mind

- When you run it, give the next data version in DATA_VERSION.
