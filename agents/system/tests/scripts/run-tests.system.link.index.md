---
about: agent-os/agents/system/tests/scripts/run-tests.system.link.js
basis: 674b4c90b427
written: 2026-10-01T01:00:33Z
by: summary-worker
confirmed: 2026-10-14T15:07:13Z
---
# run-tests.system.link.js

## Summary

A file link to the shared `run-tests` script in `scripts/system/`. Called from here, it presets kind `scripts` and this folder's `tests.config.json`, so `node tests/scripts/run-tests.system.link.js` runs the system's script tests, or one with `--id`. It is listed in `system.links.json` and built by relink; it is a link, never a copy.

## Keep in mind

- When you find this link missing or wrong, fix its entry in `system.links.json` and rerun relink; never copy `run-tests` here.
