---
about: agent-os/agents/trading/prediction-market/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/configs/models.config.link.json
node: p-agent-os-agents-trading-prediction-market-strategy-1-agent-pm-strategy-1.momentum-v1.opus55-test-configs-models.config.link.json
basis: 6948f4b12c1c
written: 2026-10-01T00:55:25Z
by: summary-worker
confirmed: 2026-10-09T10:03:12Z
---
# models.config.link.json

## Summary

A read-only file link to the shared `models.config.json` [11.11], which routes every AI-using agent, sub-agent and worker to a platform and model. This variant's route is `opus-5.5` on Claude Code, matching the `opus55` in its name. A job's own `model` wins; `model: "route"` looks it up there (format proposed). Relink builds the link from the links file [27.3].

## Keep in mind

- When you want this agent on another model, create a new test variant with a new name; a route change is never made in place.
