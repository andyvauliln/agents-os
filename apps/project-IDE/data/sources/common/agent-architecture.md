# Agent OS: Agent architecture (v0.2)

How one agent works inside: what its folder holds, how a run goes, how it uses sub-agents and memory, and how it gets its data. It holds for every level: the system [10], a domain [19] and the levels each domain defines below it (D-022). A domain may add its own layer: for example, the prediction-market domain's `common/trading-agent-architecture.md` covers its strategies [21] and trading variants [23]. How the agents fit together as a system is in architecture.md; triggers, modes, links, logs and the config merge are in shared-mechanics.md.

## Parts of an agent
<!-- k: id=common-agent-parts applies=[2.17.1],[10],[19],[21],[23] sources=D-022,D-024,D-025,D-029,D-030,D-031,D-056 status=decided -->
Every agent is a folder with the same parts (template: file-tree.md [2.7.1]):

| Part | What it does for the agent |
|---|---|
| `.claude/` | Its Claude Code level: `CLAUDE.md` (its prompt), `settings.json` (permissions, hooks, model), its own skills, sub-agents, rules, commands, workflows and sub-agent memory ([2.7.2]). |
| `configs/` | Its own config `[name].config.json`, its jobs `[name].workers.json`, its links `[name].links.json`, plus links to the shared config files it reads. |
| `scripts/` | Its own `*.worker.*` and `*.system.*` scripts and any script kind its domain adds, plus links to shared scripts (relink, run-tests). |
| `logs/`, `data/` | What it wrote (runs, decisions, outputs), plus links to the few shared files it reads. |
| `docs/` | `README.md`, `changes.md`, decisions, notes and any doc its domain adds, plus links to the shared docs it needs. |
| `tests/`, `research/` | Its tests with their configs, and the history of research done for it (placement at the folder root is proposed). |
| `init.sh`, `start.sh` | Setup (install, then relink) and one run. |

A level with children (the system, a domain, and any level below with children) also has `subagents.link/` in each content folder, one folder link per child (D-030). An agent at the lowest level has no children.

## The run loop
<!-- k: id=common-agent-run-loop applies=[2.17.1],[24.5],[23] sources=in-20260929-1452,in-20260929-1455,D-056 status=decided -->
Every run is **read data, analyse, decide, act**. The possible decisions: act on the outside world through its scripts; wait for information or schedule the next run; collect more data or do research (create and run a sub-agent); create, subscribe to, unsubscribe from, configure or schedule workers. A domain may add decisions of its own. An agent is one harness, platform and model; it runs one run at a time, and each run takes all new data since the last one.

### How a run starts
<!-- k: id=common-agent-run-start applies=[2.17.1],[14.1],[41],[27.4],[34],[19.2.1],[21.2.1] sources=D-021,D-029,D-056 status=proposed -->
1. The scheduler [14.1] starts the agent's main-run job (like [27.4]) on its schedule, or when a file in its `on_change` list changes.
2. `run-job`, through `start.sh` [41] and `run-agent` [14.1], merges the config, writes `logs/effective-config.json`, and starts Claude Code headless in the agent's own folder, so it uses its own `.claude/` and its own links (D-021).
3. The agent reads what is new in `data/` and in its data links since the last run.
4. It decides. Outside actions go only through its scripts, which read the mode and check the general stop switch first.
5. It writes one line per run to `logs/runs.jsonl` and a summary to `logs/run-[date].md`.

Domain sessions, and the sessions of the levels a domain defines, run the same way, in their own folders, as `agent` jobs in their workers files (like [19.2.1], [21.2.1]).

## Sub-agents
<!-- k: id=common-agent-subagents applies=[2.17.1],[10.1.1],[19.1.1],[21.1.1],[26] sources=D-008,D-018,D-026,D-030,D-033 status=decided -->
Each level's `.claude/agents/` holds its sub-agents: Claude Code sub-agents with their own context and tools (D-008). Every level has a self-improvement sub-agent scoped to that level ([10.1.1.1], [19.1.1.2], [21.1.1.1]; D-018). The system level also holds the support roles, such as the knowledge agent [10.1.1.2] (D-026, D-033). An agent at the lowest level may have its own sub-agents too (like [26]). No level links another level's `.claude/` (D-030). Every sub-agent is listed in index/subagents.md.

### How sub-agent results reach an agent
<!-- k: id=common-agent-subagent-outputs applies=[2.17.1],[16.3],[35.1] sources=D-020,D-021 status=proposed -->
Higher-level sub-agents do not run inside an agent's session. They run in their own level's session and write outputs, e.g. `data/subagents/news-digest/latest.md` [16.3], which the agent links as a data file (like [35.1]). A parent that needs a child's skill or sub-agent reads it by path.

## Memory
<!-- k: id=common-agent-memory applies=[2.17.1],[10.1.12],[19.1.12],[21.1.12],[24.12],[46.2] sources=D-024,D-025,D-056 status=proposed -->
- A sub-agent with `memory: project` keeps its memory in the level's `.claude/agent-memory/[subagent-name]/MEMORY.md` ([10.1.12], [19.1.12], [21.1.12], [24.12]); `memory: local` uses `agent-memory-local/`, which is git-ignored.
- Memory holds lessons and pointers only (e.g. a research id). Research lives in `research/`, test state in `tests/`, and each agent's own change record in its `docs/changes.md`.
- An agent's own memory and its "previous and next run" info have no home yet.

## How an agent gets data
<!-- k: id=common-agent-data applies=[2.17.1],[35],[35.1],[35.2],[34.1],[27.1],[30.1],[46.1] sources=D-010,D-014,D-020,D-030 status=decided -->
- **Own data:** its own workers write to `data/[producer]/` (like [35.2]).
- **Everything else comes in as individual file links** in its own folders, one per file its logic needs: shared worker outputs [16.2], sub-agent outputs [16.3], the outputs of its domain or of a level above it, or another domain's or agent's outputs (like [35.1], [34.1], [27.1], [30.1], [46.1]; D-020).
- **Links are read-only.** The agent writes only its own real files.
- **A parent reads its children's files** through its `subagents.link/` folders (D-030).
- Producers keep a stable `latest.*` file so links survive rotation (proposed).

## The links file
<!-- k: id=common-agent-links-file applies=[2.17.1],name:*.links.json,name:relink.system.link.js sources=D-031,in-20260930-1153 status=decided -->
Every agent lists the files it links in its own `configs/[name].links.json` ([11.13], [19.2.3], [21.2.3], [27.3]): where each link appears and which file it points at. Only the shared `relink` script [14.1] makes links from these files. After editing its links file, the agent reruns relink (`node scripts/relink.system.link.js`). Format: [11.13] and data-schemas.md; when relink runs: shared-mechanics.md; steps: how-to/add-or-change-link.md.

## Open questions
<!-- k: id=common-agent-open applies=[2.17.1],[24.5],[27],[46],[24],[16.1] sources=derived status=open -->
- Is `CLAUDE.md` composed from common-prompt.md [2.17.3] plus an agent prompt by `@import` or a link, or copied in at creation ([24.5])?
- May an agent edit its own config [27] and docs [46], or only its SI sub-agent and domain agent?
- What does a Cursor-routed agent use instead of `.claude/` ([24])?
- How is "new since the last run" tracked: file times or a cursor in [16.1]?

## Changelog
- v0.2 (2026-10-07): trading parts moved to the prediction-market domain's `common/trading-agent-architecture.md` (D-056, D-058).
- v0.1 (2026-09-30): created from file-tree.md v1.15, vision.md v0.19 and the owner inputs (D-033).
