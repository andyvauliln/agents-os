# Questions: SKILL.md

## Open questions for the owner

None open.

## The owner's questions

### 2026-10-13: How does the tree stay the same as the disk?

> explain me in ads style how de we sync file tree with a disk step by step

The page has no tree of its own. After a change, the build does these steps:

1. `enrich.py` reads each file that git keeps, with its metadata. It marks the empty files.
2. `materialize.py` gives empty metadata files to new items. It keeps a `.gitkeep` in empty folders. It writes `docs/file-tree.md`.
3. `build_map.py` checks the How it works files.
4. `check_page.js` tests the page.
5. The build compares the page tree with git.
6. The build publishes the page.

The owner can make a change on the page. That change goes to the disk first through `ide-sync`, after Apply changes.

Docs improved: agents/system/.claude/skills/ide-build/SKILL.index.md, agents/system/.claude/skills/ide-build/SKILL.md.
