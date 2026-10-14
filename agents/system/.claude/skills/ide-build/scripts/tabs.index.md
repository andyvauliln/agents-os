---
about: agent-os/agents/system/.claude/skills/ide-build/scripts/tabs.py
basis: 2e94d3274769
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T15:07:13Z
---
# tabs.py

## What it is

The field guides and extra tabs for the page, chosen by the item's path or kind: for a settings file, each key with its values, an example and what it means; for an agent, its overview, jobs and links; for a keys file, the key names, never values.

## Who looks after it

It is written by the owner and project-ide-agent.

## When and how it changes

It changes when a field guide or an extra tab of the page changes, or a settings file gains a key.

## Who uses it, and when

It is read by `agents/system/.claude/skills/ide-build/scripts/enrich.py`.

## Where it is mentioned

It is described in its folder's How it works file `agents/system/.claude/skills/ide-build/scripts/scripts.index.md`.

## Related knowledge

It is read by `agents/system/.claude/skills/ide-build/scripts/enrich.py`. It links to `agents/system/configs/models.config.json`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `agents/system/CLAUDE.md` (section "The File Tree page"), `docs/metadata.md`, `agents/system/docs/README.md` (section "The project IDE"), `apps/project-IDE/docs/README.md` (section "How the page is built and checked") and `agents/system/.claude/skills/ide-build/scripts/README.md`.

## Keep in mind

- When the file set is built, split this file into one file per job; today it does several.
