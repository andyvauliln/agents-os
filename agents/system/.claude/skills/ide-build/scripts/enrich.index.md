---
about: agent-os/agents/system/.claude/skills/ide-build/scripts/enrich.py
basis: 4deebc7826e5
written: 2026-10-14T15:04:45Z
by: project-ide-agent
confirmed: 2026-10-14T15:07:13Z
---
# enrich.py

## Summary

Builds the page data from the repository on disk: every file git keeps, the folders that hold them and the local keys files, each with its path as its id. For each item it reads the text into `real-files.json`, its How it works and Details files with the state of the How it works file, its Example, Questions and ASD-STE100 files when they exist, and the extra tabs that come from the kind of file. It also reads the decisions for the page's pop-ups, and stamps the data with the next version.

## Keep in mind

- When you run it, give the next data version in DATA_VERSION.
