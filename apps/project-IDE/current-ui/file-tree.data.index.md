---
about: agent-os/apps/project-IDE/current-ui/file-tree.data.json
basis: 981c7ce4dc3d
written: 2026-10-14T15:06:23Z
by: project-ide-agent
confirmed: 2026-10-14T15:07:13Z
---
# file-tree.data.json

## Summary

Everything the page shows, in one generated file: every item, with its path as its id, its status, its How it works and Details, its Example, Questions and ASD-STE100 text where those files exist, and its extra tabs, plus the decisions the page shows when one is named. `enrich.py` builds it from the files on disk and the metadata files next to each item, with a new data version each time. The text of each file is in `real-files.json` next to it. It cannot hold a copy of itself, so its File tab shows it exactly as the page loaded it, read-only.

## Keep in mind

- When it is out of date or two copies disagree, rebuild it; never edit or merge it by hand.
