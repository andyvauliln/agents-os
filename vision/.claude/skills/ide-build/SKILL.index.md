---
about: agent-os/agents/system/.claude/skills/ide-build/SKILL.md
node: n-10.1.2.5.1
basis: 013df59f5f73
written: 2026-10-14T12:00:00Z
by: knowledge-base-agent
confirmed: 2026-10-06T21:10:15Z
---
# SKILL.md

## Summary

The steps that keep the page in step with the disk and rebuild it: read the tree notes; build the page data from every file git keeps, with the next version (`enrich.py`); keep the files on disk in step with their sources, give each new item its empty metadata files, keep a `.gitkeep` in each empty folder and write `docs/file-tree.md` again (`materialize.py`, then enrich again if it made files); check that every How it works file is current and none is left over (`build_map.py`); copy the data next to the page; test it on a desktop and a phone width (`check_page.js`); check that the page tree equals the files in git; publish it at the same link; and tell the owner in plain words what changed. A change the owner made on the page reaches the disk first, through `ide-sync`. The same steps in ASD-STE100 are in `docs/metadata.md`, section 11.
