---
name: planned-items-are-real-files
description: Superseded 2026-10-13 (D-065): no planned logic; the page tree is the files on disk; empty files marked + 'empty' filter
metadata:
  type: project
---
**2026-10-13 (D-065), replaces the rule below:** owner: remove all planned logic. enrich.py leaves out items not on disk and marks `empty` files (0 bytes or only {}/[]; not vision/, .gitkeep, .env); materialize.py creates nothing from the plan (only drafts over real files, metadata next to items, empty metadata for found items, .gitkeep, docs/file-tree.md). Page: 'planned' switch replaced by an 'empty' filter. To add a file, create it on disk.

History: Owner 2026-10-12: "all what was planned should be already real files". vision/tools/materialize.py (run after enrich.py, then enrich again if it made new ones) creates every planned item missing on disk: drafts copied (draft in vision/ stays the source; node field real_file; server writes both), others empty ({} for .json), .gitkeep in empty folders, placeholder names as written, '|' -> '-'. .secrets/ folders, notes and secrets.index.json are in git (D-063, PR #5); .env files are git-ignored, created empty only when missing, never read (page shows them local_only). Merged to main via PR #4 (8f1c25c).

**Why:** the owner pulled main and the disk differed from the page tree.

**How to apply:** every ide-build runs materialize; verify page paths == `git ls-files --cached --others --exclude-standard` ancestors. Related: [[file-tree-explorer-sync]].
