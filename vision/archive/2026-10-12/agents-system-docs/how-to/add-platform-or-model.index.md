---
about: agent-os/agents/system/docs/how-to/add-platform-or-model.md
node: n-2.11.3
basis: d92dd278117c
written: 2026-10-07T19:01:11Z
by: knowledge-base-agent
---
# add-platform-or-model.md

## Summary

The runbook for adding a new AI platform or model and routing agents, sub-agents or workers to it. It adds the platform or model to `models.config.json` with its status and key names, puts its keys in the test `.env`, teaches `run-job` the platform's headless command, routes objects to it, runs one job in test mode and lists it in `index/models.md`. The steps are still proposed; which config folder a non-Claude harness uses is open.

## Keep in mind

- When you move an agent to a new model, create a new test version of it; never edit the old one.
- When you add a platform, put only key names or refs in `models.config.json`, never values.
