---
about: agent-os/agents/system/docs/how-to/add-or-run-tests.md
node: n-2.11.7
basis: c3e9d343b49f
written: 2026-10-07T19:01:11Z
by: knowledge-base-agent
---
# add-or-run-tests.md

## Summary

The runbook for adding, enabling or running a test at any level. Pick the level and the kind (`agents` for prompt and sub-agent behaviour, `scripts` for code), write the test file, add an entry to that folder's `tests.config.json`, run it through the runner link there, and read the result written back to the config and to `logs/tests.jsonl`. The owner turns tests on or off in the UI. The steps are still proposed.

## Keep in mind

- When a test fails, set its `next_action` in `tests.config.json` so its owner knows what to do.
- When you write a test, use fixture data in test mode, with no network, no secrets and no live actions.
