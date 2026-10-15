---
about: agent-os/agents/system/.claude/skills/ide-build/scripts/rebuild.py
basis: e96d06cfe13b
written: 2026-10-15T07:10:39Z
by: knowledge-base-agent
---
# rebuild.py

## What it is

The rebuild of the page data for a start of the project IDE. It runs `materialize.py`, builds the data in a scratch folder and compares it with the data next to the page; only when something differs does it build in place with the next data version, so a restart with no change leaves git clean. Then it prints the How it works report and runs the tree check.

## Who looks after it

The project IDE agent, with the owner.

## When and how it changes

It changes when the build steps or the data's comparison change, for example when `enrich.py` gets new options. After a change, the scripts README, the `ide-build` skill and the IDE rebuild prompt are brought in line.

## Who uses it, and when

`start.sh` at the top of the repository, at every start of the IDE. It is not the full build of a round: that one also writes stale How it works files, runs the page check and publishes.

## Where it is mentioned

`agents/system/.claude/skills/ide-build/SKILL.md`, `agents/system/.claude/skills/ide-build/scripts/README.md`, `apps/project-IDE/docs/README.md`, `apps/project-IDE/docs/rebuild-prompt.md`, `apps/project-IDE/server/README.md` and `start.sh`.

## Related knowledge

It runs `materialize.py`, `enrich.py`, `build_map.py` and `check_tree.py` next to it, and writes `apps/project-IDE/current-ui/file-tree.data.json` and `real-files.json`. Like every build script, it uses the Python standard library only.

## Keep in mind

- When it reports stale How it works files, write them with the `file-index` skill; it never writes them itself.
- When the data must be published, run the full `ide-build`; this script never publishes.
