---
about: agent-os/agents/trading/prediction-market/start.sh
node: n-19.11
basis: 20358858772e
written: 2026-10-01T00:59:09Z
by: summary-worker
confirmed: 2026-10-07T18:57:42Z
---
# start.sh

## Summary

Starts one domain session in the domain folder, so it loads only the domain's `.claude/` and links and reads its strategies through `subagents.link/`. The scheduler calls it for the domain session job in the domain's workers file (every 4 hours in the example), and the owner can also run it by hand. How it ties into the scheduler is proposed.
