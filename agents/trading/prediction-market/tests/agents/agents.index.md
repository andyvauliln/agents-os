---
about: agent-os/agents/trading/prediction-market/tests/agents/
node: n-19.12.1
basis: 294cd0d2ab1c
written: 2026-10-01T00:58:18Z
by: summary-worker
confirmed: 2026-10-07T18:57:42Z
---
# agents/

## Summary

The domain's agent tests: checks of how the domain owner's prompt and the domain sub-agents behave. It holds `tests.config.json` (every test with on or off, schedule, owner and last result), one `[test-id].test.md` scenario per test, and `run-tests.system.link.js`, the runner link that runs this folder's tests and writes the results back. Each test runs Claude Code headless in a temporary copy of the domain folder, in test mode with no secrets, graded by script checks first. The fields and test format are proposed.

## Keep in mind

- When you add a test of code, put it in `tests/scripts/`, not here.
