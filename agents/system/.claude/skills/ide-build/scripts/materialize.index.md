---
about: agent-os/agents/system/.claude/skills/ide-build/scripts/materialize.py
basis: 80b627f8fea2
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T19:42:37Z
---
# materialize.py

## What it is

Keeps the metadata files and the plain tree in step with the files on disk. It gives an empty How it works and Details file to every item that has none, outside stage two and outside the kept-data folder `apps/project-IDE/data/sources/prediction-market/metadata/`, keeps a `.gitkeep` in every empty folder and removes it once the folder holds a file, and writes `docs/file-tree.md`, every path in git without the metadata files. It copies nothing from anywhere.

## Who looks after it

It is written by the owner and project-ide-agent.

## When and how it changes

It changes when the rule for which items get metadata files, the .gitkeep rule or the plain tree changes.

## Who uses it, and when

It is read by ide-build.

## Where it is mentioned

It is described in `agents/system/.claude/skills/ide-build/SKILL.md` and its folder's How it works file `agents/system/.claude/skills/ide-build/scripts/scripts.index.md`.

## Related knowledge

It reads `agents/system/.claude/skills/ide-build/scripts/index_files.py`. It writes `docs/file-tree.md`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `agents/system/CLAUDE.md` (section "The File Tree page"), `docs/metadata.md`, `agents/system/docs/README.md` (section "The project IDE"), `apps/project-IDE/docs/README.md` (section "How the page is built and checked") and `agents/system/.claude/skills/ide-build/scripts/README.md`.

## Keep in mind

- When it makes new files, run `enrich.py` again.
