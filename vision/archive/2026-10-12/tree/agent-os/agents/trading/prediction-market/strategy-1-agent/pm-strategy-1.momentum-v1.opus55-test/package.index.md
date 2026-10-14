---
about: agent-os/agents/trading/prediction-market/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/package.json
node: n-38
basis: 4b6b0b552cc1
written: 2026-10-01T01:03:51Z
by: summary-worker
confirmed: 2026-10-07T19:05:50Z
---
# package.json

## Summary

The agent's JS/TS dependencies and npm scripts; every level has one. `name` is the agent's name, with `private: true` and `type: "module"`. `npm start` runs `./start.sh`, and `npm test` runs `node scripts/run-tests.system.link.js`, which runs both kinds of test. `dependencies` lists only the libraries the agent's own scripts need, and `init.sh` installs them. The fields are proposed. Still open: dependencies per agent, or one shared workspace at the root.
