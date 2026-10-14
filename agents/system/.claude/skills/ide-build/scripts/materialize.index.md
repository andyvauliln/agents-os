---
about: agent-os/agents/system/.claude/skills/ide-build/scripts/materialize.py
basis: 2978a5768482
written: 2026-10-14T15:04:45Z
by: project-ide-agent
confirmed: 2026-10-14T15:07:13Z
---
# materialize.py

## Summary

Keeps the metadata files and the plain tree in step with the files on disk. It gives an empty How it works and Details file to every item that has none, outside stage two, keeps a `.gitkeep` in every empty folder and removes it once the folder holds a file, and writes `docs/file-tree.md`, every path in git without the metadata files. It copies nothing from anywhere.

## Keep in mind

- When it makes new files, run `enrich.py` again.
