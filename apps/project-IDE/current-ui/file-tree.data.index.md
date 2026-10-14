---
about: agent-os/apps/project-IDE/current-ui/file-tree.data.json
node: n-53.1.2
basis: 09a42999110b
written: 2026-10-07T14:21:32Z
by: knowledge-base-agent
---
# file-tree.data.json

## Summary

Everything the page shows, in one generated file: every item with its notes, status, example, text, How it works, knowledge and tabs, plus the lists of inputs, decisions and docs. `enrich.py` builds it from the tree notes, the drafts, the knowledge and the How it works files, with a new data version each time. It cannot hold a copy of itself, so its File tab shows it exactly as the page loaded it, read-only.

## Keep in mind

- When it is out of date or two copies disagree, rebuild it; never edit or merge it by hand.
