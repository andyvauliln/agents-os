---
name: planned-items-are-real-files
description: Owner rule 2026-10-12: every planned file/folder exists in the repo; materialize.py creates them each build; page tree must equal git
metadata:
  type: project
---
Owner 2026-10-12: "all what was planned should be already real files". vision/tools/materialize.py (run after enrich.py, then enrich again if it made new ones) creates every planned item missing on disk: drafts copied (draft in vision/ stays the source; node field real_file; server writes both), others empty ({} for .json), .gitkeep in empty folders, placeholder names as written, '|' -> '-'. .secrets/ folders, notes and secrets.index.json are in git (D-063, PR #5); .env files are git-ignored, created empty only when missing, never read (page shows them local_only). Merged to main via PR #4 (8f1c25c).

**Why:** the owner pulled main and the disk differed from the page tree.

**How to apply:** every ide-build runs materialize; verify page paths == `git ls-files --cached --others --exclude-standard` ancestors. Related: [[file-tree-explorer-sync]].
