---
about: agent-os/agents/system/package.json
node: n-10.4
basis: 917ffe481ade
written: 2026-10-01T01:01:42Z
by: summary-worker
confirmed: 2026-10-12T15:40:56Z
---
# package.json

## Summary

The system level's JS/TS dependencies and npm scripts. Here the dependencies are the libraries the shared scripts need. Proposed fields: `name` (the agent's name), `private: true`, `type: "module"`, `scripts.start` running `./start.sh`, and `scripts.test` running both test kinds through `run-tests`. `init.sh` installs it. Still open: dependencies per agent, or shared through a workspace at the repo root.
