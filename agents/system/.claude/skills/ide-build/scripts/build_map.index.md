---
about: agent-os/agents/system/.claude/skills/ide-build/scripts/build_map.py
basis: d6a82265636f
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T19:42:37Z
---
# build_map.py

## What it is

Keeps the How it works files honest. For each item it makes a basis from the item's own content and, for a folder, the names and How it works texts of what is inside, and compares it with the basis in the file: fresh, stale, missing or empty. It lists the stale ones from the deepest up, shows what one is written from, writes or confirms them, and lists metadata files whose item is gone; the copies in the kept-data folder are data, not orphans.

## Who looks after it

It is written by the owner, project-ide-agent and knowledge-base-agent.

## When and how it changes

It changes when the rule for a fresh How it works file changes, or an option is added.

## Who uses it, and when

It is read by ide-build, file-index and `agents/system/.claude/skills/ide-build/scripts/enrich.py`.

## Where it is mentioned

It is described in its folder's How it works file `agents/system/.claude/skills/ide-build/scripts/scripts.index.md`.

## Related knowledge

It reads `agents/system/.claude/skills/ide-build/scripts/index_files.py`. It is read by `agents/system/.claude/skills/file-index/SKILL.md`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `agents/system/CLAUDE.md` (section "The File Tree page"), `docs/metadata.md`, `agents/system/docs/README.md` (section "The project IDE"), `apps/project-IDE/docs/README.md` (section "How the page is built and checked") and `agents/system/.claude/skills/ide-build/scripts/README.md`.

## Keep in mind

- When the tree or a file changes, run it until nothing is missing or stale and nothing is left over.
