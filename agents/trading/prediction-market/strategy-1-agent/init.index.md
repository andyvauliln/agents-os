---
about: agent-os/agents/trading/prediction-market/strategy-1-agent/init.sh
node: n-21.10
basis: b9d1aacbeea2
written: 2026-10-01T00:59:34Z
by: summary-worker
confirmed: 2026-10-07T19:05:50Z
---
# init.sh

## Summary

The strategy agent's re-runnable setup script. It installs the strategy's dependencies, then runs `relink` for this agent: the file links from `strategy-1-agent.links.json` and the strategy's entry in each of the domain's `subagents.link/` folders. It also registers the agent in the index and the UI. After that, links follow the links file by themselves, so a link change needs no new `init.sh` run. Open: whether `create-agent` generates it.
