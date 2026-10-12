---
about: agent-os/agents/trading/prediction-market/package.json
node: n-19.8
basis: 695c8a53feee
written: 2026-10-01T01:08:49Z
by: summary-worker
confirmed: 2026-10-07T18:57:42Z
---
# package.json

## Summary

The domain's JS/TS manifest: the libraries its own scripts need, and the npm scripts `start` (runs `start.sh`) and `test`. The domain's `scripts/` has no run-tests link, so `test` runs the runner links in `tests/agents/` and then `tests/scripts/`. Proposed fields: `name` is the domain agent's name, `private: true` and `type: "module"`. `init.sh` installs from it. Still open: dependencies per agent, or shared through a workspace at the root.
