# Agent OS: Architecture (v0.2)

How the system is built, one section per mechanism: the repo root, domains, the agent levels, the standard agent folder and `.claude/`, sub-agents, child links and file links, configs and routing, jobs and the scheduler, scripts, logs and data, docs and the knowledge base, secrets, tests and research, apps, and how runs work per level. Each section says how the parts fit together and points to the doc that holds the detailed rule: names, layouts and the `.link` rule in conventions.md, file shapes in data-schemas.md, keys, live actions and approvals in safety.md, step-by-step flows in flows.md, one agent inside in common/agent-architecture.md, triggers, modes, logging and the config merge in common/shared-mechanics.md. Numbers [n] are the objects in file-tree.md. The trading layer (the strategy and trading-agent levels, variants, the domain's config and dashboard) is the prediction-market domain's `trading-architecture.md` [19.6.6].

## Repository root
<!-- k: id=arch-repo-root applies=[0],[1],[48] sources=D-013,D-017,D-023,D-028,in-20260929-1455,D-056 status=decided -->
| Path | What it holds |
|---|---|
| `README.md` [1] | the entry point and the only doc at the root; points to `agents/system/docs/` (D-017) |
| `agents/` [4] | every domain, the system included (D-013) |
| `apps/` [43] | our own apps, the project IDE [53] and the prediction-market domain's dashboard [45] `apps/trading-ui/`; apps we use, forked from GitHub; research clones in `apps/temp/` [55]; each app with its own `docs/` (D-045, D-055) |
| `.secrets/` [47] | every key, outside `agents/` (D-023; location proposed) |
| `.gitignore` [48] | a commented file: secrets, local Claude Code and Cursor state, runtime log and data content, build junk (D-028) |

There is no root `docs/` (D-017), no root `CLAUDE.md` (the file every Claude reads first is the system's `.claude/CLAUDE.md` [10.1.5]) and no root `researches/` (research sits in each level's `research/`) (owner, 2026-10-06, D-045). Whether this is one git repo or several is open (roadmap.md `road-q-repo`).

## Domains under agents/
<!-- k: id=arch-domains applies=[4],path:agents/* sources=D-013,D-015,in-20260929-1616 status=decided -->
- `agents/` holds the domains: `system/` [10] directly, and the trading domains inside the folder `trading/` [56], starting with `trading/prediction-market/` [19] (D-059). There is no extra `domains/` level.
- `system/` is a domain like the others. It differs in two ways only: its level agent runs the whole system, and its content folders also hold the shared files every agent uses.
- A domain's folder is its domain agent's folder. The agents below it are sub-folders of it, in the levels the domain defines. The prediction-market domain's strategy and variant folders: its `trading-architecture.md`.

## Agent levels
<!-- k: id=arch-levels applies=[10],[19] sources=D-018,D-022,D-026,in-20260929-1703 status=decided -->
Every agent sits at a level, and every level has the same standard folder (D-022). The system defines the first two levels; each domain defines the levels below its domain agent:

| Level | Folder | Prompt | Responsible for | Children |
|---|---|---|---|---|
| System | `agents/system/` [10] | [10.1.5] system manager | all domains, system health and development, the shared files, the owner's questions about the whole system | domains |
| Domain | e.g. `trading/prediction-market/` [19] | [19.1.5] domain owner | its domain: finds, creates and updates its agents, keeps the domain running smoothly, answers the owner's questions and comments | the first level the domain defines |

- Every agent has a parent, and a parent sees its children through `subagents.link/` (`arch-child-links`).
- The domain-owner role is the domain's own prompt, not a sub-agent (D-022 reconciles D-018).
- System-support roles are not a level: they are sub-agents of the system level (D-026, `arch-subagents`).
- Level agents have IDs in config and the index (e.g. `sys-system-agent`, `[code]-domain-agent`) while their folders keep structural names (D-032). Format: conventions.md `conv-level-ids`.
- The prediction-market domain's own levels (strategy agents and trading variants): its `trading-architecture.md`.

## The standard agent folder
<!-- k: id=arch-standard-folder applies=[2.7],[10],[19],[21],[23] sources=D-014,D-022,D-025,D-030,in-20260929-1703 status=decided -->
- Every agent, at every level, is one folder with the same parts (D-022): `.claude/`, the content folders `configs/`, `scripts/`, `logs/`, `data/`, `docs/`, `tests/`, `research/`, and the level files. Exact layout: conventions.md `conv-standard-folder`; what each part does for the agent: common/agent-architecture.md `common-agent-parts`.
- Every content folder follows one template: the level's own real files, file links to what its logic needs (`arch-file-links`), and at a level with children `subagents.link/` (`arch-child-links`).
- Because every agent looks the same, the shared machinery works on any of them unchanged: `create-agent` scaffolds, `relink` links, the scheduler finds jobs, and the UI, SI sub-agents and the knowledge agent read a child the same way at every level.
- The system level is the one exception in content: its folders also hold the shared files (conventions.md `conv-system-folder`).

### Where the owner's first agent-folder list lives
<!-- k: id=arch-owner-list applies=[23],[27],[24] sources=in-20260929-1452,derived status=proposed -->
The owner's first list (vision.md `vis-block-agent-folder`) mapped onto the standard folder: config → `configs/[name].config.json`; common config → the file link `system.config.link.json` [27.1]; docs, logs, data → their folders; agent prompt → `.claude/CLAUDE.md` [24.5], built on common/common-prompt.md; memory → `.claude/agent-memory/` [24.12]; self-improvement strategy → the SI sub-agents and their templates [2.17.4]; workers and subscriptions → the jobs file [27.4] and the links file [27.3]; previous and next runs → the scheduler state [16.1]. The trading items of the list (trading accounts, portfolio, analytics): the prediction-market domain's `trading-architecture.md`.

### Level files
<!-- k: id=arch-level-files applies=name:init.sh,name:start.sh sources=D-022,D-029,D-031 status=proposed -->
The level files exist at every level (D-022); how they tie into the machinery is proposed:
- Every `init.sh` ends by running `relink` for its agent. The system's `init.sh` [10.6] also installs the git hooks that run relink at review time and relinks the whole project.
- Every `start.sh` does one run of its agent or one level session; the scheduler calls it for the main-run job. The system's `start.sh` [10.7] also starts the scheduler.

## The standard .claude/ folder
<!-- k: id=arch-claude-folder applies=name:.claude sources=D-016,D-024,D-030,in-20260929-2025,in-20260930-1045 status=decided -->
- Every level has its own full Claude Code folder (D-024), so a session started in a level's folder loads that level's prompt, settings, skills, commands and sub-agents, and nothing else. Layout: conventions.md `conv-claude-folder`, `conv-claude-parts`.
- Levels do not share `.claude/` content through links for now (D-030; conventions.md `conv-no-claude-links`). Results of higher-level sub-agents reach agents as data files instead (`arch-subagents`).
- Only generic placeholders exist for now; concrete skills, commands and rules come later.
- Proposed: a `PostToolUse` hook in `settings.json` reruns relink when the session edits its links file (common/shared-mechanics.md `common-mech-relink-when`); sub-agent memory in `agent-memory/` (common/agent-architecture.md `common-agent-memory`).

## Sub-agents
<!-- k: id=arch-subagents applies=[10.1.1],[19.1.1],[21.1.1],[26] sources=D-008,D-018,D-022,D-026,D-056 status=decided -->
Sub-agents are Claude Code sub-agents in a level's `.claude/agents/`, each with its own context and tools (D-008). Their names are unique, like agent names.

| Level | Self-improvement (SI) sub-agent (D-018) | Other sub-agents |
|---|---|---|
| System [10.1.1] | `sys-self-improvement-agent` [10.1.1.1]: improves the system itself (shared scripts, configs, routing, docs) and reacts to new models and harnesses | system-support roles (D-026): the knowledge agent [10.1.1.2], later development, improvement, analysis, research; system-wide pre-analysis such as a news digest |
| Domain, e.g. [19.1.1] | the domain's SI sub-agent, e.g. [19.1.1.2]: compares the agents across the domain and proposes new ones | domain sub-agents |
| A level the domain defines | its SI sub-agent, where the domain gives that level one | the level's own sub-agents |

For example, in the prediction-market domain, the strategy level's SI sub-agent [21.1.1.1] runs the strategy loop, and a trading variant [26] has none (its `trading-architecture.md`).

- Higher-level sub-agents never run inside a running agent's session: they write outputs that agents link as data files (common/agent-architecture.md `common-agent-subagent-outputs`; flows.md `flow-subagent-digest`).
- Each sub-agent runs as a `subagent` job in its level's workers file (proposed). SI templates: common/self-improvement-templates.md.

### The knowledge agent
<!-- k: id=arch-knowledge-agent applies=[10.1.1.2],[10.1.2.1],[10.1.2.2] sources=D-026,D-033,in-20260930-1533,in-20260930-1841 status=decided -->
- `sys-knowledge-agent` [10.1.1.2] owns the knowledge base [2] (D-033; was `sys-docs-agent`, D-026). Every owner input, every answer to an owner question and every system change goes through it.
- Skill `knowledge-intake` [10.1.2.1]: store the input, extract its knowledge, place it, ripple it to every doc that states the same thing, record it, rebuild the map. Skill `file-index` [10.1.2.2]: rewrite the stale How it works summaries, children first, up to the root.
- It runs in the session that received the input, plus a `knowledge-sync` job in [11.10] that picks up anything missed (proposed). Steps: how-to/process-an-input.md; the flow: flows.md `flow-user-input`.

## Child links: subagents.link/
<!-- k: id=arch-child-links applies=name:subagents.link sources=D-015,D-029,D-030,in-20260930-1045,D-056 status=decided -->
- Child links give every level a view of its direct children and nothing else: system to domains, each domain to the first level it defines, and each level to the next (D-030). The system reaches any agent one `subagents.link/` at a time.
- The UI, SI sub-agents, the knowledge agent and the index builders walk the system this way, reading children's configs, jobs, logs, data, docs, tests and research without copies.
- They replaced the system's flat views of every agent (D-015) and the jobs view by domain (D-029).
- Rules (only folder links, read-only, made by relink, never followed recursively): conventions.md `conv-content-folders`, `conv-link-scans`.

## File links and the links file
<!-- k: id=arch-file-links applies=name:*.link.*,name:*.links.json sources=D-002,D-020,D-031,in-20260929-1656,in-20260930-1153 status=decided -->
- An agent's view of the rest of the system is exactly its file links: one symlink per file its logic needs, from anywhere under `agents/` (the system, its own domain or a level above, another domain, any agent by unique name) (D-020). Examples in the example agent [23]: [27.1], [30.1], [34.1], [35.1], [46.1].
- The set is declared, not built by hand: each agent lists its links in its own links file ([11.13], [19.2.3], [21.2.3], [27.3]; D-031), and the shared `relink` script turns the lists into symlinks (`arch-relink`). `create-agent` writes the first list; then the agent itself, its SI sub-agent or the owner edit it.
- Rules and names: conventions.md `conv-file-links`, `conv-links-file`, `conv-relink-only`. Format: data-schemas.md `schema-links-file`. Steps: how-to/add-or-change-link.md.

### relink and check-links
<!-- k: id=arch-relink applies=[14.1],name:relink.system.link.js,[16.1],[15.1] sources=D-031,in-20260930-1153 status=decided -->
- One shared `relink` script [14.1] builds every link in the project from all links files plus the child links, fixes changed ones, removes links nobody lists, and writes the links index `links.index.json` [16.1], so anyone can see who reads which file. Every level below the system has a `scripts/relink.system.link.js` that relinks only that agent ([19.3.2], [21.3.2], [30.3]); the system runs the script directly from [14.1].
- It runs when a links file changes, at review time (before a commit, after a pull or merge, when the owner approves a change), and when an agent edits its own links file. How each moment is wired: common/shared-mechanics.md `common-mech-relink-when`; the flow: flows.md `flow-relink`.
- `check-links` [14.1] runs after every relink and on its own (proposed) and reports anything that breaks the link rules.

## Configs
<!-- k: id=arch-configs applies=name:configs,[11.1],[27.2] sources=D-006,D-011,D-014,D-029,D-031,in-20260929-1537 status=decided -->
Two kinds of config (D-006), routing in its own file (D-011), and two per-agent lists (D-029, D-031):

| File | Where | Holds |
|---|---|---|
| `system.config.json` [11.1] | system `configs/` | everything controllable globally: modes and kill switch, schedule defaults, triggers, notifications (sections proposed; a long section moves to its own file later) |
| `models.config.json` [11.11] | system `configs/` | platforms and routes (`arch-routing`) |
| `[name].config.json` | each agent's `configs/`, e.g. [27.2] | the agent's own settings, a real file in its folder (D-014) |
| `[name].workers.json` | every level, e.g. [27.4] | the agent's jobs (`arch-jobs`) |
| `[name].links.json` | every level, e.g. [27.3] | the agent's file links (`arch-file-links`) |

- An agent reads the shared configs through file links, e.g. `system.config.link.json` and `models.config.link.json` [27.1].
- How the layers merge and the safety exceptions: common/shared-mechanics.md `common-mech-config-merge`. File names: conventions.md `conv-agent-config-files`. Shapes: data-schemas.md. Which settings are common and which individual is open (roadmap.md `road-q-config-shape`).
- The prediction-market domain keeps its trading settings (risk limits, accounts, venues) in its own config: its `trading-architecture.md`.

### Routing
<!-- k: id=arch-routing applies=[11.11],name:models.config.link.json sources=D-011,D-029,in-20260929-1455,in-20260929-1545 status=decided -->
- Every AI-using object (agent, sub-agent, AI worker) gets an explicit platform and model in `models.config.json` [11.11], a file separate from the global config (D-011). There is no `platforms-and-models/` folder.
- A job in a workers file may name its own model instead; `model: "route"` takes it from this file (D-029).
- Where an agent's name carries its platform/model, it must match its route (proposed check in `create-agent`). Lookup and fields: data-schemas.md `schema-models-config`; the owner's platform table: vision.md `vis-models`.

## Workers, jobs and the scheduler
<!-- k: id=arch-jobs applies=name:*.workers.json,[14.2],[31] sources=D-007,D-029,D-030,in-20260929-1545,in-20260930-0938 status=decided -->
- Workers are scripts (D-007): shared collectors in [14.2], agent-only ones in the agent's `scripts/`, like [31].
- Every agent, at every level, has one jobs file `configs/[name].workers.json`: [11.10], [19.2.1], [21.2.1], [27.4] (D-029). Everything the agent runs is a job there: a plain script, or an AI run (the agent's own main run, a sub-agent, a skill, a workflow, a slash command). Each job has on/off, a schedule (every N, cron, once on a date, after another job, manual), where it runs (local headless, cloud, desktop, GitHub Actions), platform and model.
- A parent sees its children's jobs files through `configs/subagents.link/` (D-030).
- Fields and schedule strings: data-schemas.md `schema-workers-job-fields`; steps: how-to/add-worker.md.

### One scheduler
<!-- k: id=arch-scheduler applies=[14.1],[10.7],[16.1] sources=D-029,D-030 status=proposed -->
- One central `scheduler` process [14.1] runs the jobs of every agent; `run-job` [14.1] runs one job, either the script or the platform's headless command. The system's `start.sh` [10.7] starts the scheduler and the OS keeps it alive; an agent's own `start.sh` only does one run.
- Jobs files only say what should run. Runtime state lives in `scheduler-state.json` [16.1] and each run's log in the owner agent's `logs/jobs/[job-id]/`, so a jobs file changes only when someone changes a job.
- Adding a platform means adding one command template to `run-job`. Step by step: flows.md `flow-scheduler`; restart rules: common/shared-mechanics.md `common-mech-scheduler`. Which machine runs it is open (roadmap.md `road-q-scheduler-host`).

## Scripts
<!-- k: id=arch-scripts applies=name:scripts,[14.1],[14.2],[14.3] sources=D-007,in-20260929-1455,in-20260929-1545,in-20260929-1616,D-056 status=decided -->
- All code is scripts in JS/TS or Python: the shared ones in the system's `scripts/` [14], each agent's own in its `scripts/` (e.g. [30]). An agent uses a shared script through a file link, so an improvement reaches every agent at once.
- Kinds (`worker` and `system`; a domain may add its own, as the prediction-market domain adds `decision`, proposed default, D-058), suffixes, shared sub-folders and promotion to shared: conventions.md `conv-script-kinds`, `conv-shared-script-folders`, `conv-promotion`.

### Shared system scripts
<!-- k: id=arch-system-scripts applies=[14.1] sources=D-012,D-021,D-023,D-025,D-029,D-031,D-033 status=proposed -->
The machinery the whole system runs on, one line each (detail: file-tree.md [14.1]):
- `create-agent`: checks that the name is valid and unused, scaffolds the standard folder, runs `init.sh`.
- `run-agent`: merges the config, writes `effective-config.json`, starts Claude Code in the agent's own folder.
- `scheduler`, `run-job`: run every job (`arch-scheduler`).
- `relink`, `check-links`: build and check every link (`arch-relink`).
- `load-secret`: gives a script the keys its config lists, at run time only (safety.md `safe-secret-loading`).
- `run-tests`: runs a level's tests from its `tests.config.json` files.
- `notifier`: sends the owner's notifications (channel open).
- `build-map`: builds the knowledge map and lists stale summaries (D-033; planning copy `tools/build_map.py`).

## Logs and data
<!-- k: id=arch-logs-data applies=name:logs,name:data,[15],[16] sources=D-009,D-010,D-014,D-015,D-020,D-028,D-030 status=decided -->
- Shared logs and data live in the system level, organised by source: logs [15] (system [15.1], services [15.2] for outside actions, workers [15.3], sub-agents [15.4]) and data [16] (system state [16.1], workers [16.2], sub-agents [16.3]).
- Each agent's own logs and data are real files in its own folder (D-014): runs, decisions, job logs and `tests.jsonl` in `logs/` [34]; one folder per producer in `data/` [35.2].
- An agent reads shared files or other agents' files through file links (D-020); a parent reads its children's through `subagents.link/` (D-030).
- Runtime content is git-ignored while the folders stay (D-028, [48]). Logging rules: common/shared-mechanics.md `common-mech-logging`; producer outputs: conventions.md `conv-producer-outputs`; shapes: data-schemas.md.

## Docs
<!-- k: id=arch-docs applies=name:docs,[2] sources=D-004,D-017,D-030,in-20260929-1623 status=decided -->
Docs are built like the other content folders (D-017): the shared docs in `agents/system/docs/` [2], each agent's own `docs/` with file links to the shared docs it needs, and children's docs one `subagents.link/` down. Rules: conventions.md `conv-docs`, `conv-docs-format`.

### The knowledge base
<!-- k: id=arch-knowledge-base applies=[2],[2.1],[2.10],[2.18.8],[10.1.2.2] sources=D-033,in-20260930-1533 status=decided -->
The shared docs [2] are the system's knowledge base (D-033), in layers: every owner input word for word [2.10]; one file doc per object [2.13]; topic docs; history ([2.6], [2.9]); and the index with the knowledge map [2.18.8] (which knowledge applies to which file or folder, many to many) and the How it works of every file and folder, each in its own `[name].index.md` [51]. The knowledge agent keeps it (`arch-knowledge-agent`). Layers, tag format and flow: docs/README.md.

## Secrets store
<!-- k: id=arch-secrets applies=[47],[47.3] sources=D-023,D-027 status=decided -->
- The keys sit in one store, `.secrets/` [47], at the repo root and outside `agents/` (location proposed): `test/.env` [47.1.1] with all test keys, `live/.env` [47.2.1] for the later live phase, and `secrets.index.json` [47.3] with metadata only (D-023, D-027).
- Because it sits outside `agents/`, no agent folder, file link or child link reaches it; scripts get keys only through `load-secret` (`arch-system-scripts`).
- Location, files, access and loading rules: safety.md `safe-secrets-store`, `safe-secrets-location`, `safe-secret-loading`. Key format: data-schemas.md `schema-env-keys`.

## Tests and research
<!-- k: id=arch-tests-research applies=name:tests,name:research,name:tests.config.json sources=D-025,in-20260929-2036,in-20260929-2059 status=decided -->
- Every level has `tests/` with `agents/` (tests of the level's prompt and sub-agents) and `scripts/` (tests of its scripts). Each holds a `tests.config.json` listing every test and a runner link `run-tests.system.link.js` to the shared `run-tests` [14.1], which runs that folder's tests and writes the results back and to `logs/tests.jsonl`.
- Every level has `research/`: an `index.json` history of every research item and one folder per item. The level's SI sub-agent is the main writer.
- Where the folders sit (proposed: the level's folder root): conventions.md `conv-tests-research-placement`. How a test runs: flows.md `flow-tests`. Fields: data-schemas.md `schema-tests-config`, `schema-research-index`. Steps: how-to/add-or-run-tests.md, how-to/record-research.md.

## apps/
<!-- k: id=arch-apps-ui applies=[43],[53] sources=in-20260929-1455,in-20260929-1545,D-056 status=decided -->
- `apps/` [43]: our own apps, the project IDE [53] and the prediction-market domain's dashboard [45] (its `trading-architecture.md`); apps we use, forked from GitHub with our `main` and an `upstream` branch, in `apps/<name>/` with `docs/` and `repo/`; research clones in `apps/temp/<name>/` [55], never committed. Every app has its own `docs/` with a vision, a README and a rebuild prompt, and a row in `index/apps.md` [2.18.5] (D-045, D-055).

## How runs work per level
<!-- k: id=arch-runs-per-level applies=[10],[19],name:start.sh sources=D-021,D-029,D-030 status=proposed -->
- Each level runs in its own folder: the system session at `agents/system/`, each domain session at its domain folder, and each agent below at its own folder, started by `run-agent` [14.1].
- A session sees only its own `.claude/` and its own links, and reads its children's files through `subagents.link/`.
- Higher-level sub-agents run in their own level's session and hand their outputs to agents as linked data files.
- Every session is an `agent` job in its level's workers file (e.g. the domain session every 4h), run by the scheduler through `start.sh`. The prediction-market domain's strategy and variant runs: its `trading-architecture.md`.
- Not chosen: running everything from the top (a D-019 idea, withdrawn by D-021), and copying shared skills into agents (copies drift and miss improvements).

## Changelog
- v0.2 (2026-10-07): trading parts moved to the prediction-market domain's `trading-architecture.md` (D-056, D-058); `arch-strategy-variants` moved there whole; copy trading [42] removed from the domains.
- v0.1 (2026-09-30): created from file-tree.md v1.15, vision.md v0.19 and the owner inputs (D-033). Points to conventions.md, safety.md and flows.md for rules and steps they hold.
