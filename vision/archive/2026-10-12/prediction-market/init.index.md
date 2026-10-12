---
about: agent-os/agents/trading/prediction-market/init.sh
node: n-19.10
basis: b9d1aacbeea2
written: 2026-10-01T00:59:16Z
by: summary-worker
confirmed: 2026-10-07T18:57:42Z
---
# init.sh

## Summary

The domain's setup script, safe to run again: it installs the domain's dependencies, then runs relink for the domain only, which builds the file links in its links file and its entry in each of the system's `subagents.link/` folders, and registers the domain in the index and the UI. Unlike the system's `init.sh`, it installs no git hooks. After setup, relink keeps the links in line with the links file without re-running this script. Still open: whether `create-agent` generates it.

## Keep in mind

- When you change the domain's links, edit its links file and let relink run; there is no need to re-run this script.
