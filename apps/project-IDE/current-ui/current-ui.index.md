---
about: agent-os/apps/project-IDE/current-ui/
node: n-53.1
basis: 866f24a21312
written: 2026-10-14T12:00:00Z
by: knowledge-base-agent
confirmed: 2026-10-09T10:30:32Z
---
# current-ui/

## Summary

The File Tree page as the owner uses it now: `file-tree-explorer.html`, the page itself, and `file-tree.data.json`, the one data file it loads. It is published on claude.ai at a fixed link; the project IDE agent rebuilds the data, checks the page on a desktop and a phone width and publishes it again after every round that changes the tree, a doc or a How it works file. While we plan, the build writes the working page and data in `vision/explorer/`, so `file-tree.data.json` here is an empty placeholder (`{}`) until the build writes here after the move out of `vision/`.
