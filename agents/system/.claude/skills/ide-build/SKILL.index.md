---
about: agent-os/agents/system/.claude/skills/ide-build/SKILL.md
basis: 28bb24b393d5
written: 2026-10-14T15:06:11Z
by: project-ide-agent
confirmed: 2026-10-14T15:07:13Z
---
# SKILL.md

## Summary

The steps that keep the page in step with the disk and rebuild it, all from the files themselves: give each new item its empty metadata files, keep a `.gitkeep` in each empty folder and write `docs/file-tree.md` again (`materialize.py`); check that every How it works file is current and none is left over (`build_map.py`); build the page data from every file git keeps and its metadata files, with the next version (`enrich.py`); check that the page tree equals the files in git (`check_tree.py`); test the page on a desktop and a phone width (`check_page.js`); publish it at the same link; and tell the owner in plain words what changed. A change the owner made on the page reaches the disk first, through `ide-sync`. The same steps in ASD-STE100 are in `docs/metadata.md`, section 11.
