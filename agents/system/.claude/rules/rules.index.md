---
about: agent-os/agents/system/.claude/rules/
node: n-10.1.8
basis: 2543709588ab
written: 2026-10-01T00:52:45Z
by: summary-worker
confirmed: 2026-10-07T19:02:04Z
---
# rules/

## Summary

The system level's topic rules: instructions that apply only when certain files are in play. Each rule is a Markdown file, one topic per file, with a `paths:` frontmatter of globs so it loads only when matching files are read; subfolders are allowed. It is part of the standard `.claude/` every level has and holds only the generic placeholder for now; concrete rules come later.
