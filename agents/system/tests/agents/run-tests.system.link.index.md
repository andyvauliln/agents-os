---
about: agent-os/agents/system/tests/agents/run-tests.system.link.js
basis: 674b4c90b427
written: 2026-10-14T12:00:00Z
by: knowledge-base-agent
confirmed: 2026-10-14T15:07:13Z
---
# run-tests.system.link.js

## Summary

A file link to the shared `run-tests` script in `scripts/system/`. Called from here, it presets kind `agents` and this folder's `tests.config.json`, so `node tests/agents/run-tests.system.link.js` runs the system's agent tests, or one with `--id`. It is listed in `system.links.json` and built by relink; it is a link, never a copy, so fixes to `run-tests` reach every level at once. The shared script and this link are planned and still empty, so no agent test can run yet.

## Keep in mind

- When you find this link missing or wrong, fix its entry in `system.links.json` and rerun relink; never copy `run-tests` here.
