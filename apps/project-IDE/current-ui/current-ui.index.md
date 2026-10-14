---
about: agent-os/apps/project-IDE/current-ui/
basis: c22b1a6c0348
written: 2026-10-14T15:06:23Z
by: project-ide-agent
confirmed: 2026-10-14T15:07:13Z
---
# current-ui/

## Summary

The File Tree page as the owner uses it now: `file-tree-explorer.html`, the page itself, `file-tree.data.json`, the one data file it loads, and `real-files.json`, the text of every file, which the page loads the first time a file is opened. The build writes the two data files here from the files on disk. It is published on claude.ai at a fixed link, and the owner's server serves this same folder; the project IDE agent rebuilds the data, checks the page on a desktop and a phone width and publishes it again after every round that changes a file, a folder or a metadata file.
