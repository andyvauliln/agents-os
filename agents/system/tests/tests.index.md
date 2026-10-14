---
about: agent-os/agents/system/tests/
basis: ab867c5da786
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T15:09:25Z
---
# tests/

## What it is

The system's tests, so every change to the system's prompt, sub-agents or scripts can be checked before and after it runs. `agents/` tests LLM behaviour: the system prompt and its sub-agents, run headless in a temporary copy of the folder, in test mode with no secrets. `scripts/` tests the system's scripts, the shared ones, with node or pytest on fixtures. Each has a `tests.config.json`, where the owner switches tests on or off and `run-tests` writes results, plus a runner link to `run-tests`; results also go to `logs/tests.jsonl`. Through `subagents.link/` the system sees each domain's tests. Every level has this layout; placing it at the folder root rather than in `.claude/` is proposed. Open: whether a failing test blocks runs or only promotion.

## Who looks after it

It is written by the system agent; sys-self-improvement-agent, which adds tests for what it changes; the owner; and relink (planned shared script in agents/system/scripts/system/), for subagents.link/.

## When and how it changes

It changes when a kind of test is added or removed, or a domain is added or removed. It is empty for now.

## Who uses it, and when

It is read by run-tests (planned shared script); the owner, on the File Tree page; and the system agent.

## Where it is mentioned

It is described in `agents/system/docs/README.md` (section "Tests"), `agents/system/docs/rebuild-prompt.md` (section "Tests") and `agents/system/system.index.md`.

## Related knowledge

It reads `agents/system/scripts/` and `agents/system/CLAUDE.md`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `docs/metadata.md` and `agents/system/docs/README.md` (section "Tests").

## Keep in mind

- When you add a test, put prompt and sub-agent tests in `agents/` and code tests in `scripts/`, each with an entry in that folder's `tests.config.json`.
