# Agent OS: Self-improvement templates (v0.2)

Templates for the self-improvement (SI) sub-agents: one shared base, then what changes at the system [10.1.1.1] and domain [19.1.1.2] level (D-018). A domain adds templates for the levels it defines: for example, the prediction-market domain's `common/strategy-si-templates.md` holds its strategy template [21.1.1.1] with the variant loop the owner asked for in D-032. What SI may never do is in safety.md; the SI wheel as a flow is in flows.md.

## What every SI sub-agent does
<!-- k: id=common-si-purpose applies=[2.17.4],name:*self-improvement-agent.md sources=D-018,in-20260929-1452,in-20260929-1455,in-20260929-1630,D-056 status=decided -->
Every `.claude/` level has one SI sub-agent, scoped to that level (D-018). It is long-lived, with memory, and runs from time to time. It takes in the latest logs, data and research, news from outside (such as a new model or harness) and the owner's comments; it runs research when needed. Its goal: make what it owns fast, cheap, efficient, simple, understandable and better at its goal; fix bugs and issues; test. It may change anything (config, prompt, code, model or platform), but always through a new test agent, never by editing a running one. Its behaviour is specific to what it improves, but built from these shared templates.

## Base template
<!-- k: id=common-si-base-template applies=[2.17.4],name:*self-improvement-agent.md,[10.1.12],[19.1.12],[21.1.12] sources=D-018,D-024,D-025,D-029,D-056 status=proposed -->
Each SI sub-agent file `.claude/agents/[level-id]-self-improvement-agent.md` starts from this. It runs as a `subagent` job in its level's workers file (nightly by default); its model comes from its job or [11.11] (`si` type).

```markdown
---
name: <level-id>-self-improvement-agent
description: Improves <scope>. Reads logs, data, research and owner comments; opens research; proposes or creates new test versions; adds tests.
tools: Read, Grep, Glob, Bash, Write
memory: project
---
You improve <scope>. Goal: fast, cheap, efficient, simple, understandable, better at <goal>. Fix bugs. Test.
1. Read your MEMORY.md and research/index.json so you do not repeat work.
2. Read what changed since your last run: logs, data and docs of what you own
   (your children through subagents.link/), owner comments in docs/notes.md, outside news.
3. Pick at most <n> ideas. For each, open a research item (planned, then running).
4. If a change is worth trying, make it a new TEST agent (a new version) with create-agent,
   add tests for what changed, and link the new agent in the item's `related`.
5. Close each item with results_summary and decisions (done or abandoned).
6. Write lessons and item ids, not the research itself, to MEMORY.md.
Code you write: one job per file, with its tests.
Never: touch live agents, loosen a limit, read .secrets/live/, or delete another agent's files.
```

## System level
<!-- k: id=common-si-system applies=[2.17.4],[10.1.1.1],[10.9],[11.10],[11.11] sources=D-018,D-026,in-20260929-1455 status=proposed -->
- **Owns:** the system itself: shared scripts [14], shared configs [11], routing [11.11] and the shared docs [2].
- **Reads:** system logs [15.1] (errors, costs), the domains through the system's `subagents.link/` folders, owner comments, and news of new models and harnesses.
- **Writes:** research items in [10.9]; route changes proposed as new test versions; proposals for shared files, marked "pending owner" in decisions.md.
- **Memory:** [10.1.12] `sys-self-improvement-agent/MEMORY.md`. **Job:** a nightly `subagent` job in [11.10].

## Domain level
<!-- k: id=common-si-domain applies=[2.17.4],[19.1.1.2],[19.13],[19.1.12],[19.2.1] sources=D-018,D-022,D-024,D-056 status=proposed -->
- **Owns:** the domain and the agents below it.
- **Reads:** every agent below it through the domain's `subagents.link/` folders (like [19.4.1], [19.5.1], [19.6.1]), domain-wide data, owner comments.
- **Writes:** comparisons across the domain, proposals for new agents, domain-wide issues; research in the domain's `research/` (like [19.13]).
- **Memory:** the domain's `.claude/agent-memory/[level-id]-self-improvement-agent/MEMORY.md` (like [19.1.12]). **Job:** a nightly `subagent` job in the domain's workers file (like [19.2.1]).

## Changelog
- v0.2 (2026-10-07): trading parts moved to the prediction-market domain's `common/strategy-si-templates.md` (D-056, D-058): `common-si-strategy`, `common-si-variant-loop`, `common-si-loop-steps` and `common-si-open` moved there; the domain template keeps its general shape here.
- v0.1 (2026-09-30): created from file-tree.md v1.15, vision.md v0.19 and the owner inputs (D-033). Includes the D-032 strategy loop.
