---
about: agent-os/agents/system/docs/
node: n-2
basis: 47793c6459f8
written: 2026-10-07T19:01:11Z
by: knowledge-base-agent
confirmed: 2026-10-09T19:51:44Z
---
# docs/

## Summary

The system's docs, for people and for every agent. The three main docs come first: the vision, read first; the README, every part of the system with the path to its docs; and the rebuild prompt, the spec an AI rebuilds the system from. Beside them, the inputs vision lists every requirement from the owner's own messages by scope, with only the newest form of each, in Simplified Technical English. Next to them are the topic notes agents read while they work: overview, architecture, conventions, safety, data schemas, flows, metrics, glossary, roadmap and feature map, the runbooks in `how-to/`, the common knowledge in `common/` and the lists in `index/`. Each domain adds its own notes in its own `docs/`, such as the prediction-market domain's `trading-` notes, reached through `subagents.link/`. The project's records live in `apps/project-IDE/data/`.

## Keep in mind

- When anything changes (an owner message, an answer, a file), run it through the knowledge base agent so every doc stays current.
- When a lower level's docs change, check the docs above it, up to the system's, in the order vision, README, rebuild prompt.
