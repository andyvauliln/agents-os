---
about: agent-os/agents/system/configs/models.config.json
node: n-11.11
basis: 310133be8241
written: 2026-10-07T19:01:11Z
by: knowledge-base-agent
---
# models.config.json

## What it is

The file that says which AI platform, model and effort every agent, helper and AI-using job uses, and which platforms can be used at all. Claude Code with Opus 5.5 is the default; Sonnet 5.5, Cursor's Composer 2.5 and OpenRouter are supported; Codex and Kimi come later.

## Who looks after it

The system's support helpers write it. The self-improvement helpers propose changes.

## When and how it changes

When a platform or model is added or changes status, or when an agent should use another model. Moving an agent to a new model means a new test version of that agent.

## Who uses it, and when

The scripts that start every run, to pick the model; the list of models and the dashboard, to show which model each agent uses.

## Where it is mentioned

Every jobs file (a job can name its own model or take it from here), the list of models, and the names of agents in a domain that puts the model in the name, as the prediction-market domain does.

## Related knowledge

- Where a domain puts an agent's platform and model in its name, they must match what this file says.
- Still open: the default effort, the default model for helpers, and a few model types not listed yet.

## Keep in mind

- When you change an agent's model, create a new test version instead of changing the running one.
