# Agent OS: Add a platform or model (v0.2)

How to add a platform (a coding-agent harness such as Cursor or Codex) or a model, and route agents, sub-agents and jobs to it. Routing lives in [11.11] `models.config.json` (D-011); the current list is in index/models.md.

## Steps
<!-- k: id=howto-add-platform-or-model-steps applies=[2.11.3],[11.11],[2.18.6],[14.1],[11.10] sources=D-011,D-029,in-20260929-1455,in-20260930-0938,D-056 status=proposed -->
1. **Add it to [11.11].** A platform goes under `platforms` with its `status` (`default`, `supported`, `supported-not-connected` or `later`) and the key names it needs. A model goes under `models` with its `platform` and `effort`.
2. **Add its keys** to `.secrets/test/.env` [47.1.1] (see add-account-or-secret.md). Only key names or refs go into [11.11].
3. **For a new platform, teach `run-job` [14.1] to start it:** one headless command template, like Claude Code `claude -p`, Cursor `cursor-agent -p` or Codex `codex exec`. Jobs can then name it in `platform` ([11.10]). Which agent-level config folder a non-Claude harness uses (e.g. `.cursor/`) is still open ([24]).
4. **Set the status.** Only a platform whose status allows use can take routes.
5. **Route objects to it:** add `routes[name]` for one agent, sub-agent or worker, or change `defaults_by_type` for a whole type (`main`, `domain`, `si`, `sub`, `worker`, `support`). A single job can name its own `model` in its workers file instead of `route` (D-029).
6. **A model change makes a new agent version:** moving an agent to a new model means a new test agent (see create-agent.md), never an edit of the old one. The SI sub-agents propose such route changes. Where a domain puts the model in an agent's name, the new name must match the new route (for example, the prediction-market domain's `trading-conventions.md`).
7. **Test run:** run one job on the new route in test mode (e.g. a `manual` job, or the agent tests with `node tests/agents/run-tests.system.link.js`) and read its run log.
8. **List it** in `index/models.md` [2.18.6].

## Checks
<!-- k: id=howto-add-platform-or-model-checks applies=[2.11.3],[11.11],[2.18.6],[14.1],[15.1] sources=D-011,D-029,D-056 status=proposed -->
- Every route in [11.11] names a model whose platform status allows use.
- Where an agent's name carries its platform and model, they match its route (the check in [14.1]).
- The test run succeeded; its log names the platform and model, and its cost shows in [15.1].
- [11.11] holds no key values, only key names or refs.
- `index/models.md` lists the platform or model with its status and who routes to it.

## Changelog
- v0.2 (2026-10-07): the rule that a trading agent's model is part of its name moved to the prediction-market domain's `trading-conventions.md`; a model change makes a new version (D-056, D-058).
- v0.1 (2026-09-30): created from file-tree.md v1.15, vision.md v0.19 and the owner inputs (D-033).
