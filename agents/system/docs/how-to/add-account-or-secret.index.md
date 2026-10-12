---
about: agent-os/agents/system/docs/how-to/add-account-or-secret.md
node: n-2.11.6
basis: c5a219f28bfa
written: 2026-10-07T19:01:11Z
by: knowledge-base-agent
---
# add-account-or-secret.md

## Summary

The runbook for adding or rotating an API key or outside account. The owner creates the key and adds a `KEY=value` line to the test `.env` (a live key goes into the live `.env`, by the owner only), records its metadata in the secrets index, and lists only the key name in the platform config and the agent's `secret_keys`; a test run and `check-links` follow. A domain may keep more about its accounts. The steps are proposed.

## Keep in mind

- When you add a key, put its value only in the `.env` file under `.secrets/`; configs, docs, logs and prompts get the key name only.
- When the key or account is for live use, only the owner adds it and approves it.
- When you rotate a key, keep the same key name, update `rotate_by` and delete the old key at the provider.
