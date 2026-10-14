---
about: agent-os/apps/project-IDE/current-ui/real-files.json
basis: 981c7ce4dc3d
written: 2026-10-14T15:06:23Z
by: project-ide-agent
confirmed: 2026-10-14T15:07:13Z
---
# real-files.json

## Summary

The text of every file on the page, one entry per item, keyed by its path. `enrich.py` writes it next to the page data in every build; the page loads it the first time a file is opened, so the page itself stays small, and on the owner's server the same texts are read fresh from disk. A keys file, a file over 200 KB, a file that is not text and the two built data files are not in it.

## Keep in mind

- When it is out of date, rebuild it; never edit it by hand.
