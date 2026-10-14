# Agent OS: Glossary (v0.2)

One meaning per term, so the owner, the agents and the UI use the same words. Terms are in alphabetical order, one to three sentences each, with a pointer to the doc that holds the detail. Numbers [n] are the objects in file-tree.md. The trading terms (strategy, variant, champion and challenger, decision script and more) are in the prediction-market domain's `trading-glossary.md` [19.6.12].

## Terms

### Agent
<!-- k: id=term-agent applies=[4] sources=in-20260929-1452,in-20260929-1455,D-022 status=decided -->
Something that decides and acts with an LLM and has its own standard agent folder: the system and domain level agents, and every agent at the levels each domain defines. Every agent has a globally unique name. Sub-agents are a different thing: they live in a level's `.claude/agents/`.

### Agent folder (standard)
<!-- k: id=term-agent-folder applies=[2.7] sources=D-022,D-025 status=decided -->
The identical folder every agent has at every level: `.claude/`, `configs/`, `scripts/`, `logs/`, `data/`, `docs/`, `tests/`, `research/`, `package.json`, `requirements.txt`, `init.sh`, `start.sh`. Layout: conventions.md `conv-standard-folder`; why: architecture.md `arch-standard-folder`.

### check-links
<!-- k: id=term-check-links applies=[14.1] sources=D-023,D-030,D-031 status=proposed -->
The shared script [14.1] that checks every link: broken links, cycles, symlinks without `.link`, any `.claude` link, and any link into `.secrets/`. `relink` runs it after every change.

### Child link (subagents.link/)
<!-- k: id=term-child-link applies=name:subagents.link sources=D-030 status=decided -->
A folder link from a level to one direct child's folder of the same kind, e.g. `docs/subagents.link/[domain-name]/` in the system. Every content folder of a level with children has them; they are the only folder links. Detail: architecture.md `arch-child-links`.

### Claude folder (.claude/)
<!-- k: id=term-claude-folder applies=name:.claude sources=D-024,D-030 status=decided -->
The standard Claude Code folder every level has: its prompt `CLAUDE.md`, settings, rules, skills, commands, sub-agents, workflows, output styles and sub-agent memory. No level links another level's `.claude/` for now (D-030).

### CLAUDE.md
<!-- k: id=term-claude-md applies=name:CLAUDE.md sources=D-022,D-024 status=decided -->
The prompt of a level, inside its `.claude/`: the system manager [10.1.5], a domain owner such as [19.1.5], or the prompt of a level a domain defines.

### Config
<!-- k: id=term-config applies=name:configs sources=D-006,D-014,D-029,D-031 status=decided -->
A JSON file that sets how something behaves. There are two kinds of config, the global system config and each agent's own config, plus the routing file and each agent's jobs file and links file. Detail: architecture.md `arch-configs`.

### Config merge order
<!-- k: id=term-config-merge applies=[11.1],[27.2] sources=D-006,D-014,D-056 status=proposed -->
How configs combine, lowest to highest: the global system config, then the agent's own config, then the owner's overrides from the UI. A lower layer may only tighten a limit. Detail: common/shared-mechanics.md `common-mech-config-merge`.

### Data
<!-- k: id=term-data applies=name:data sources=D-005,D-010,D-014 status=decided -->
Everything workers, sub-agents and agents produce, as JSON, JSONL and Markdown files for now, with no database (D-005). Shared data sits in the system's `data/` [16] by source; each agent's own data sits in its own `data/`.

### Docs pattern
<!-- k: id=term-docs-pattern applies=name:docs sources=D-017,D-030 status=decided -->
Docs work like the other content folders: the shared docs are real files in `agents/system/docs/` [2], each agent has its own real `docs/` with links to the shared docs it needs, and each level reaches its children's docs through `docs/subagents.link/`.

### Domain
<!-- k: id=term-domain applies=path:agents/* sources=D-013,in-20260929-1452,D-056 status=decided -->
One area of work, such as prediction markets [19], and its folder under `agents/` (a trading domain sits inside `agents/trading/`, D-059). The system [10] is a domain too.

### Domain owner (main domain agent)
<!-- k: id=term-domain-owner applies=[19.1.5] sources=in-20260929-1455,D-022,D-056 status=decided -->
The role that owns a whole domain: its agents, its health, the owner's questions and comments. It is the domain's own prompt [19.1.5], not a separate sub-agent (D-022).

### File link
<!-- k: id=term-file-link applies=name:*.link.* sources=D-020,D-031 status=decided -->
A symlink to one file an agent's logic needs, named `[name].link.[ext]` inside its own content folders, e.g. `data/[worker-name].link.json` [35.1]. It is listed in the agent's links file and read-only for the agent.

### How it works summary
<!-- k: id=term-how-it-works applies=[10.1.2.2] sources=D-033,in-20260930-1533 status=decided -->
The plain-language summary of one file or folder: what it is, how it works, who writes and reads it, what is still open. Each one is a Markdown file of its own, `[name].index.md`, next to the file or inside the folder. The knowledge agent writes them bottom up, children first, and rewrites a summary when anything under it changes; the File Tree page shows it as the main view.

### Important file
<!-- k: id=term-important-file applies=name:*.workers.json,[11.1] sources=in-20260929-1455,D-029 status=decided -->
A file whose change should cancel an agent's current run and start a new one with the new information; other changes wait for the next run. Each agent declares its important files as the `on_change` list of its main-run job (proposed field).

### Index
<!-- k: id=term-index applies=[2.18] sources=in-20260929-1520,D-012,D-033 status=decided -->
The docs folder `index/` [2.18]: one list per kind of thing (agents, workers, sub-agents, services, apps, models, links), plus the knowledge map and the summaries. The agents list [2.18.1] is the registry of every name ever used.

### Input
<!-- k: id=term-input applies=[2.10] sources=D-033,in-20260930-1533,in-20260930-1841 status=decided -->
Anything the owner says about the system, in any channel, and the answer they get to a question. Each is stored word for word in `inputs/` [2.10] with an id `in-YYYYMMDD-HHMM` before its knowledge is filed.

### Job
<!-- k: id=term-job applies=name:*.workers.json sources=D-029,in-20260930-0938 status=decided -->
One thing an agent runs, listed in its workers file: a plain script, or an AI run (the agent's main run, a sub-agent, a skill, a workflow, a command), with on/off, schedule, where it runs, platform and model. Fields: data-schemas.md `schema-workers-job-fields`.

### Knowledge agent
<!-- k: id=term-knowledge-agent applies=[10.1.1.2] sources=D-033 status=decided -->
`sys-knowledge-agent` [10.1.1.2], the system sub-agent that files every owner input and every system change into the docs, keeps the knowledge map and rewrites the How it works summaries. Its skills are `knowledge-intake` [10.1.2.1] and `file-index` [10.1.2.2].

### Knowledge entry
<!-- k: id=term-knowledge-entry applies=[2.1] sources=D-033 status=proposed -->
One tagged section of a topic doc: a heading followed by `<!-- k: id=... applies=... sources=... status=... -->`. `applies` names the files and folders it is for. Format: docs/README.md.

### Knowledge map
<!-- k: id=term-knowledge-map applies=[2.18.8] sources=D-033,in-20260930-1533 status=decided -->
`index/knowledge-map.json` [2.18.8]: which knowledge applies to which file or folder, many to many, built by `build-map` from the knowledge entries and the tree. The knowledge agent uses it to find everything a change touches.

### Level agent
<!-- k: id=term-level-agent applies=[10],[19] sources=D-022 status=decided -->
One of the managing agents: the system agent [10], a domain agent [19], or a managing agent at a level a domain defines. Each has the standard folder and sits above the next level. Detail: architecture.md `arch-levels`.

### Link (.link)
<!-- k: id=term-link applies=[2.7] sources=D-001,D-002,D-030 status=decided -->
A symlink. Every symlinked file or folder has `.link` in its name, or sits directly inside a `.link` folder such as `subagents.link/` (D-002, amended by D-030); a path without either is a real file. The two kinds are file links and child links.

### Links file
<!-- k: id=term-links-file applies=name:*.links.json sources=D-031,in-20260930-1153 status=decided -->
An agent's `configs/[name].links.json`: every file link it wants, where each appears and which file it points at. `relink` builds the links from it. Format: data-schemas.md `schema-links-file`.

### load-secret
<!-- k: id=term-load-secret applies=[14.1],[47.1.1],[47.2.1] sources=D-023,D-027 status=decided -->
The shared loader [14.1] that puts only the keys a job or config lists in `secret_keys` into the running script's process, at run time. Values never reach logs or an LLM. Rules: safety.md.

### Main agent
<!-- k: id=term-main-agent applies=[23] sources=in-20260929-1455,D-056 status=decided -->
The owner's word for an agent that runs and decides, in test or live mode: one harness, platform and model, one run at a time. For example, in the prediction-market domain, a trading variant [23].

### Main run
<!-- k: id=term-main-run applies=name:*.workers.json,[41] sources=D-029 status=decided -->
An agent's own recurring run, the `agent` job in its workers file (e.g. every 15 minutes). The scheduler starts it through `start.sh`, and a change to an important file restarts it.

### Mode (test / live)
<!-- k: id=term-mode applies=[11.1] sources=in-20260929-1455,D-056 status=decided -->
Whether a service that acts does it for real (live) or not (test). Every acting service reads its mode from config, and the mode is the last part of an agent's name. The default is test; only the owner approves live.

### Model
<!-- k: id=term-model applies=[11.11] sources=D-011,in-20260929-1455 status=decided -->
The LLM an AI-using object runs with, such as Opus 5.5, Sonnet 5.5 or Composer 2.5, with its default effort. Models are listed and routed in `models.config.json` [11.11].

### Number ([n])
<!-- k: id=term-number applies=[2.13] sources=derived status=proposed -->
The number of an object in file-tree.md, e.g. [27.3]. Numbers are never reused; a moved or retired object keeps a stub under its old number.

### on_change
<!-- k: id=term-on-change applies=name:*.workers.json sources=D-029 status=proposed -->
A job field: the files whose change starts the job. On a main run it cancels the current run and starts a new one.

### Placeholder
<!-- k: id=term-placeholder applies=[2.13] sources=in-20260929-2025 status=decided -->
A name in `[brackets]` in the tree, e.g. `[agent-name]/` or `[skill-name]/SKILL.md`: a slot for real files that come later. Placeholders show the structure before the concrete logic exists.

### Platform
<!-- k: id=term-platform applies=[11.11] sources=D-011,in-20260929-1455 status=decided -->
The harness that runs an AI job: Claude Code (default), Cursor, OpenRouter (not connected yet), and later Codex and Kimi. Each has a status in `models.config.json` [11.11].

### relink
<!-- k: id=term-relink applies=[14.1],name:relink.system.link.js sources=D-031,in-20260930-1153 status=decided -->
The shared script [14.1] that builds every link from the links files plus the child links and removes links nobody lists. It runs when a links file changes, at review time and when an agent edits its own links file. Detail: architecture.md `arch-relink`.

### Research item
<!-- k: id=term-research-item applies=name:research sources=D-025,in-20260929-2036 status=decided -->
One investigation at a level, with an id like `r-0001`: its question, status, who ran it, results and decisions in `research/index.json`, and its artifacts in `research/[research-id]-[slug]/`.

### Route
<!-- k: id=term-route applies=[11.11] sources=D-011,in-20260929-1455 status=decided -->
"Object X uses this platform and model": the entry in `models.config.json` [11.11] for an agent, sub-agent or worker, or its type default. A job may name its own model instead.

### Run
<!-- k: id=term-run applies=[34],[41] sources=in-20260929-1452,in-20260929-1455 status=decided -->
One pass of an agent through read data, analyse, decide, act. It takes all new data since the last run; an agent runs one run at a time.

### Run-state
<!-- k: id=term-run-state applies=[16.1] sources=D-029,derived status=open -->
The live state of jobs and runs, kept outside the jobs files: `scheduler-state.json` in [16.1] (proposed). Whether a `run-state.json` with per-agent read cursors is needed depends on how "new since the last run" is tracked (open).

### Scheduler
<!-- k: id=term-scheduler applies=[14.1],[10.7] sources=D-029 status=proposed -->
The one central process [14.1] that runs every job in every workers file, watches `on_change` files and keeps the job state. The system's `start.sh` [10.7] starts it.

### Secret key (secret_keys)
<!-- k: id=term-secret-keys applies=[47.1.1],[47.2.1],[47.3] sources=D-027 status=decided -->
A `KEY=value` line in `.secrets/test/.env` or `.secrets/live/.env`, named with a provider or account prefix, e.g. `[PROVIDER]_[ACCOUNT]_[WHAT]`. Configs and jobs list only key names, in `secret_keys`.

### Secrets store
<!-- k: id=term-secrets-store applies=[47] sources=D-023,D-027 status=decided -->
`.secrets/` [47]: the only place keys live, with `test/.env`, `live/.env` and a metadata index, outside `agents/` (location proposed). Nothing links into it.

### Self-improvement (SI) sub-agent
<!-- k: id=term-si-subagent applies=[10.1.1.1],[19.1.1.2],[21.1.1.1] sources=D-018,D-032 status=decided -->
The sub-agent at each level that improves that level: system [10.1.1.1], domain [19.1.1.2], and the levels a domain defines, e.g. [21.1.1.1]. It reads logs, data, research and owner comments and makes changes as new test versions.

### Self-improvement wheel
<!-- k: id=term-si-wheel applies=[2.17.4] sources=in-20260929-1455 status=decided -->
The owner's loop: create, run in test, analyse, reconfigure as a new test agent, watch the outside world, owner in the loop. Detail: vision.md `vis-wheel`.

### Sub-agent
<!-- k: id=term-sub-agent applies=[10.1.1],[19.1.1],[21.1.1],[26] sources=D-008,D-018,D-026 status=decided -->
A Claude Code sub-agent in a level's `.claude/agents/`, with its own context and tools (D-008). Examples: the SI sub-agent of each level, the knowledge agent, pre-analysis sub-agents.

### Subscription
<!-- k: id=term-subscription applies=none sources=in-20260929-1452,D-020,D-029 status=decided -->
The owner's first word for the data an agent follows. Today it is the data file links in the agent's links file plus the `on_change` list of its main run.

### System config
<!-- k: id=term-system-config applies=[11.1] sources=D-006,in-20260929-1537 status=decided -->
`system.config.json` [11.1]: the one global config with everything controllable globally (modes, schedule defaults, triggers, notifications). Sections are proposed; long ones move to their own file later.

### System-support agent
<!-- k: id=term-system-support-agent applies=[10.1.1] sources=in-20260929-1455,D-026 status=decided -->
An agent that works on the system itself: development, documentation, improvement, analysis, research. Each role is a sub-agent in the system's `.claude/agents/` [10.1.1], not a folder (D-026).

### Test
<!-- k: id=term-test applies=name:tests.config.json sources=D-025,in-20260929-2036 status=decided -->
A check listed in a level's `tests.config.json`, with an id like `t-scripts-001`: an agent test checks the prompt and sub-agents, a script test checks code. The shared `run-tests` runs them and writes the results back.

### Trigger
<!-- k: id=term-trigger applies=[11.1],name:*.workers.json sources=in-20260929-1455,D-029 status=decided -->
What starts a run: its schedule, or a change to an important file. Common rules (debounce, restart limits) are in [11.1] `triggers`.

### Unique agent name
<!-- k: id=term-unique-name applies=[2.18.1] sources=D-012,D-032 status=decided -->
Every agent's name is unique across all domains and is its ID everywhere: folder, configs, logs, data, docs, index, UI and routes. Names are never changed or reused. Formats: conventions.md.

### Version
<!-- k: id=term-version applies=[2.18.1],[14.1] sources=D-012,D-056,D-058 status=proposed -->
A new agent made from a running one. A changed config, prompt, code or model never changes a running agent in place: it makes a new agent with a new name, tested next to its parent, which it records as `parent`. Test to live makes a new agent too. Detail: conventions.md `conv-clones`, `conv-no-rename`. In the prediction-market domain a version is a variant (`trading-glossary.md`).

### Worker
<!-- k: id=term-worker applies=name:*.worker.*,[14.2] sources=D-007,in-20260929-1545 status=decided -->
A script named `[name].worker.[ext]` that fetches data from a source and writes JSON or Markdown. It runs as a job; shared workers live in [14.2], agent-only ones in the agent's `scripts/`.

### Workers file
<!-- k: id=term-workers-file applies=name:*.workers.json sources=D-029,in-20260930-0938 status=decided -->
An agent's jobs file `configs/[name].workers.json`, where the owner sees, changes and turns off everything the agent runs. Every level has one: [11.10], [19.2.1], [21.2.1], [27.4].

## Changelog
- v0.2 (2026-10-07): trading parts moved to the prediction-market domain's `trading-glossary.md` (D-056, D-058); `term-champion-challenger`, `term-decision-script`, `term-strategy`, `term-strategy-agent` and `term-variant` moved there whole; new term Version (`term-version`).
- v0.1 (2026-09-30): created from file-tree.md v1.15, vision.md v0.19, tools/enrich.py CONCEPTS and the owner inputs (D-033).
