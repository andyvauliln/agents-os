---
about: agent-os/agents/system/.claude/agents/
node: n-10.1.1
basis: a4f907fcc084
written: 2026-10-05T13:25:49Z
by: knowledge-base-agent
confirmed: 2026-10-09T09:57:03Z
---
# agents/

## Summary

The system level's helper agents, each with its own instructions and tools. Three are named so far: the self-improvement agent, which keeps improving the system itself and reacts to new models and tools; the knowledge base agent, which keeps everything we know and writes the docs for people; and the project IDE agent, which builds the File Tree page from the repository and brings the owner's notes and edits back into the files. Planned: a workers helper that knows every worker and reuses, extends or creates one when an agent needs data, and a helper that checks the server and sets how many agents may run at once. Each runs on a schedule set in the system's jobs file and hands its results to other agents as data files.

## Keep in mind

- When you need a new system-support role, add it as a helper agent file here, not as a new agent folder.
