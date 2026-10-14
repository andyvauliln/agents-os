---
about: agent-os/agents/system/docs/how-to/promote-to-live.md
node: n-2.11.4
basis: af6f2dfb89a3
written: 2026-10-07T19:01:11Z
by: knowledge-base-agent
---
# promote-to-live.md

## Summary

The runbook for taking a test agent live with the owner's approval. It checks the criteria (every enabled test passing, `before_promote` tests included, plus any its domain sets), has the agent's parent or a self-improvement helper propose it, waits for the owner to approve in the UI, then creates a new agent ending in `-live`, switches its mode, monitors it and updates the registry. A domain may add steps, such as a funded account. The steps are still proposed.

## Keep in mind

- When an agent goes live, create a new agent ending in `-live` with `parent` set to the test agent; never rename or switch the test agent.
- When you promote, wait for the owner's approval in the UI; no agent, script or sub-agent approves going live.
- When you set up the live agent, run its live jobs `local` only; cloud, desktop and GitHub jobs always stay in test.
