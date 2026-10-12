---
about: agent-os/agents/system/tests/agents/run-tests.system.link.js
node: n-10.8.1.3
basis: a4f4a0c917bf
written: 2026-10-01T01:00:33Z
by: summary-worker
confirmed: 2026-10-09T10:03:12Z
---
# run-tests.system.link.js

## Summary

A file link to the shared `run-tests` script in `scripts/system/`. Called from here, it presets kind `agents` and this folder's `tests.config.json`, so `node tests/agents/run-tests.system.link.js` runs the system's agent tests, or one with `--id`. It is listed in `system.links.json` and built by relink; it is a link, never a copy, so fixes to `run-tests` reach every level at once.

## Keep in mind

- When you find this link missing or wrong, fix its entry in `system.links.json` and rerun relink; never copy `run-tests` here.
