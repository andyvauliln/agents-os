---
about: agent-os/agents/trading/prediction-market/strategy-1-agent/package.json
node: n-21.8
basis: 695c8a53feee
written: 2026-10-01T01:08:49Z
by: summary-worker
confirmed: 2026-10-07T19:05:50Z
---
# package.json

## Summary

The strategy agent's JS/TS dependencies and npm scripts, part of the standard folder every level has. As proposed, `name` is the agent's name and `start` runs `./start.sh`; `test` runs both kinds of tests through the runner links in `tests/agents/` and `tests/scripts/`, since the strategy's `scripts/` has no run-tests link. `dependencies` lists the libraries its own scripts need, and `init.sh` installs them. Open: dependencies per agent, or shared through one workspace at the root.
