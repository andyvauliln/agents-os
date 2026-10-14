# Questions: SKILL.md

## Open questions for the owner

None open.

## The owner's questions

### 2026-10-13: How the tree is kept in step with the disk

> explain me in ads style how de we sync file tree with a disk step by step

The page has no tree of its own. After a change, `enrich.py` reads every file git keeps with its metadata and marks empty files, `materialize.py` gives new items empty metadata files, keeps a `.gitkeep` in empty folders and writes `docs/file-tree.md`, `build_map.py` checks the How it works files, `check_page.js` tests the page, the page tree is compared with git, and the page is published. A change the owner made on the page reaches the disk first through `ide-sync`, after Apply changes.

Docs improved: agents/system/.claude/skills/ide-build/SKILL.index.md, agents/system/.claude/skills/ide-build/SKILL.md.
