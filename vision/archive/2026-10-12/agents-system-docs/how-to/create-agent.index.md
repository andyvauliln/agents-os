---
about: agent-os/agents/system/docs/how-to/create-agent.md
node: n-2.11.1
basis: f6c4d723428e
written: 2026-10-07T19:01:11Z
by: knowledge-base-agent
---
# create-agent.md

## Summary

The runbook for creating any new agent and plugging it in. It goes from an input to a checked, unique name, scaffolds the standard folder, writes the config, links and jobs files, runs `init.sh` to build the links, sets the route, runs the tests in test mode, registers the agent and starts its first run. A domain may add its own steps, as the prediction-market domain does for a strategy or variant. The steps are still proposed.

## Keep in mind

- When you name a new agent, check the format and that the name is not in the registry, retired names included.
- When you write its config, set `mode: test` and list key names only in `secret_keys`, never values.
- When the domain puts the platform and model in the agent's name, make them match its route in `models.config.json`.
