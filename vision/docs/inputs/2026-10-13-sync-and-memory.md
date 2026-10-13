# Input 2026-10-13: how the tree syncs with the disk, and why the memory notes

- From: the owner, in the thread "Interactive file tree UI"
- Date: 2026-10-13

## Words
~~~text
explain me in ads style how de we sync file tree with a disk step by step, and explain me why we need all of this this new files in a memory folder, and how we ll use it
~~~

## Answer
~~~text
Answered in ASD-STE100. The page has no tree of its own: after a change (on disk, or on the page and written by ide-sync after Apply changes), enrich.py reads every file git keeps with its metadata and marks empty files, materialize.py gives new files empty metadata, keeps .gitkeep and writes docs/file-tree.md, build_map.py checks the How it works files, check_page.js tests the page, the page tree is compared with git, then publish, commit and push. The memory notes tell a new session the lasting rules, wishes and decisions; they must be in git (apps/project-IDE/data/memory/) because Claude Code on the owner's server cannot read the project memory; CLAUDE.md points to MEMORY.md. Proposed: keep only the about 6 notes that are still rules (stage-one, human-docs-style, knowledge-intake-every-input, planned-items-are-real-files, file-tree-explorer-sync, agent-os-trading-domain) and fold the history notes into decisions and the changelog. Waiting for the owner's yes or no.
~~~

## Processed into
- apps/project-IDE/data/plans/2026-10-13-leave-vision.md (memory step, proposed)
