# Agent OS: Conventions (v0.5)

The rules that keep hundreds of agents consistent and machine-readable: how agents are named, how links are named and made, how scripts and config files are named, the standard folders every agent has, where a new file goes, and the rules for docs and git. File formats are in data-schemas.md; keys, live actions and approvals are in safety.md; how the mechanisms run (scheduler, relink, merge order) is in common/shared-mechanics.md. The section numbers [2.7.1] to [2.7.5] are the ones the file tree and the other docs cite. The owner approves changes to these rules; each change is recorded in decisions.md and changelog.md. The prediction-market domain adds its own rules (strategy and variant names, decision scripts, the trading fields of an agent's config) in its `trading-conventions.md`.

## Agent names
<!-- k: id=conv-agent-ids applies=[2.18.1],[2.18.3],[14.1],[10],[19],[21],[23],[27.2],[11.11] sources=D-012,in-20260929-1607 status=decided -->
- Every agent has a name that is unique across all domains (D-012).
- The name is the agent's ID everywhere: in its configs, logs, data and docs, its row in the registry [2.18.1], the UI and its route in [11.11]. A running agent's folder, its config file names and its entry in its parent's `subagents.link/` folders carry the name too; level folders keep structural names (`conv-level-ids`).
- The registry [2.18.1] lists every agent ever created, retired ones too. `create-agent` [14.1] checks the name's format, rejects a name already in the registry and reserves it before it scaffolds anything.
- A local ID (a job, a test, a research item) is written `[agent-id]/[id]` when it is used outside its agent. Formats of local IDs: data-schemas.md, `schema-other-ids`.

### Domain codes
<!-- k: id=conv-variant-name-format applies=[14.1],[2.18.1],[10],[19] sources=D-032,D-056 status=proposed -->
- Every agent ID starts with its domain's code: `sys` the system, `pm` the prediction-market domain [19]. Each domain has its own code.
- Trading adds its own rules in the prediction-market domain's `trading-conventions.md` (strategy and variant names).

### Level agent IDs and folder names
<!-- k: id=conv-level-ids applies=[10],[19],[2.18.1] sources=D-012,D-032,D-056 status=proposed -->
- Domain and system agents: `[code]-domain-agent` for a domain (`pm-domain-agent` for [19]), `sys-system-agent` for [10].
- Level folders keep their structural names (`system/`, `prediction-market/`). The ID lives in the level's config and in the registry [2.18.1]. A running agent's folder name is its ID.
- Trading adds its own rules in the prediction-market domain's `trading-conventions.md` (strategy agent IDs).

### Sub-agent and support agent names
<!-- k: id=conv-support-names applies=path:agents/**/.claude/agents/*.md,[2.18.3],[2.18.1] sources=D-012,D-018,D-026 status=proposed -->
- Sub-agents and support agents: `[domain]-[scope]-[role]-agent`. The scope names a level below the domain and is left out at system and domain level. Examples: `sys-knowledge-agent` [10.1.1.2], `sys-self-improvement-agent` [10.1.1.1], `pm-self-improvement-agent` [19.1.1.2]; with a scope, for example, in the prediction-market domain, `pm-strategy-1-self-improvement-agent` [21.1.1.1].
- The file is the name plus `.md`, in the level's `.claude/agents/`.
- Sub-agent names are unique too, checked against the registry [2.18.1] and the sub-agent index [2.18.3].
- System-support roles (knowledge, development, improvement, analysis, research) are sub-agents named this way, not agent folders (D-026).

### Clones and versions
<!-- k: id=conv-clones applies=[23],[27.2],[27.4],[46.2],[2.18.1] sources=D-012,D-032,D-056 status=proposed -->
- A clone always gets a new name.
- A changed config, prompt, code or model makes a new version: a new agent with a new name.
- A change to a job's logic (prompt, model, tools, inputs) in the workers file (e.g. [27.4]) counts as a config change and makes a new version. The owner turning a job on or off, or moving its time, does not.
- The new agent records `parent` (the agent it came from) in its config [27.2] and in the registry [2.18.1], and says exactly what differs in its `docs/changes.md` [46.6].
- A new version always starts as a test agent.
- Trading adds its own rules in the prediction-market domain's `trading-conventions.md` (variants and `v[N]`).

### Never rename, never reuse; live is a new agent
<!-- k: id=conv-no-rename applies=[23],[2.18.1],[14.1],[2.11.4],[2.11.5] sources=D-012 status=proposed -->
- An agent is never renamed. Its name is a permanent ID.
- Names are never reused, even after deletion: retired names stay in the registry [2.18.1].
- Test to live creates a new agent with the same name ending in `-live` and `parent` set to the test agent. The test agent keeps running or is retired. Who may approve it: safety.md, `safe-owner-approval`; the steps: how-to/promote-to-live.md.
- The planning example [23] was renamed once (D-032), before any agent existed. From the first real agent on, names are fixed.

## The .link naming rule
<!-- k: id=conv-link-names applies=[2.7],name:*.link.*,name:subagents.link,path:agents/**/subagents.link/* sources=D-002,D-030,in-20260929-1520,in-20260930-1045 status=decided -->
- Every symlinked file or folder has `.link` in its name (D-002), e.g. `relink.system.link.js`, `subagents.link/`.
- Links directly inside a `.link` folder are named after their child only, without `.link` of their own; the folder name marks them (D-030). Example: `docs/subagents.link/prediction-market/`.
- A path with neither is a real file or folder, owned by the folder it sits in.
- In the file tree, `A -> B` means A is a symlink to B.

### File links
<!-- k: id=conv-file-links applies=[27.1],[30.1],[34.1],[35.1],[46.1],name:*.link.* sources=D-020,D-031,in-20260929-1656 status=decided -->
- Inside an agent's `configs/`, `scripts/`, `logs/`, `data/` and `docs/`, links are individual file links, one per file the agent's logic needs (D-020). There are no folder links there; the only folder links are the child links in `subagents.link/` ([2.7.4]).
- A file link may point at a file anywhere under `agents/`: the system, the agent's own domain or another level above it, another domain, or another agent's outputs.
- Every file link is listed in the agent's links file ([2.7.5]). The set is chosen at creation and changed later by the agent, its SI sub-agent or the owner.
- Linked files are read-only for the agent. It writes only its own real files.
- Nothing links into `.secrets/` [47] or into any `.claude/` folder.

#### File link names
<!-- k: id=conv-file-link-names applies=[27.1],[30.1],[34.1],[35.1],[46.1] sources=D-020 status=proposed -->
- `[name].link.[ext]`: `[name]` is the target's base name and `[ext]` its extension, e.g. `safety.link.md` for [2.8] `safety.md`, `system.config.link.json` for [11.1].
- A target with a generic name (`latest.md`) is named after its producer: `news-digest.link.md` for `data/subagents/news-digest/latest.md`.
- If two names would clash, add a short source hint, e.g. `[worker-name].worker.link.log`.
- A link to a script keeps the script's kind: `relink.system.link.js`, `run-tests.system.link.js`.

## Metadata file names
<!-- k: id=conv-metadata-names applies=[53],[53.1.1],[10.1.2.2],[10.1.2.5.2.6] sources=in-20261007-0904,D-057 status=decided -->
- Every file and folder has two metadata files: its How it works (`.index.md`) and its Details (`.meta.json`). More endings follow with the file-set plan (`plans/file-set.md`).
- They are named after the file without its extension: `vision.md` has `vision.index.md` and `vision.meta.json`. A folder `configs/` keeps its own inside it: `configs/configs.index.md`, `configs/configs.meta.json`.
- A name without an extension stays whole: `.gitignore.index.md`.
- When two files in one folder would share a name (`run.js` and `run.py`), or a file is named like its folder (`server/server.py`), the file keeps its extension: `server.py.index.md`. Today that is the only case.
- A metadata file has no metadata files of its own. The Details files are empty for now; their fields are listed in the file-set plan.

## Script kinds and suffixes
<!-- k: id=conv-script-kinds applies=[14],[30],name:*.worker.py,name:*.system.* sources=D-007,in-20260929-1455,in-20260929-1545,D-056 status=decided -->
- A script's name says its kind: `[name].[kind].[ext]`. Two kinds hold for every agent: `worker` (fetches and prepares data) and `system` (the machinery: setup, cleaning, scheduling, links, tests).
- A domain may add kinds of its own. Trading adds its own rules in the prediction-market domain's `trading-conventions.md` (the kind `decision`).
- Examples: `[worker-name].worker.py`, `clean-data.system.js` [32].
- Scripts are JS/TS or Python for now.
- A script is either shared (in the system's `scripts/` [14], or in a domain's `scripts/` when only that domain uses it, `conv-promotion`) or belongs to one agent (in its own `scripts/`, e.g. [30]).

### One job per code file
<!-- k: id=conv-one-job-per-file applies=[14],[14.1],[14.2],[14.3],[30],[10.1.2.5.2],[53.3],name:*.js,name:*.py,name:*.sh sources=in-20261006-2104,D-050 status=decided -->
- Every code file holds one runnable thing (one function, one endpoint, one script, one worker) with one purpose. It may take parameters; it never mixes several jobs. No common files that collect different things.
- Related things are grouped in a folder, one per file, each with its own How it works and metadata. A shared helper is one function in its own file.
- Ours (proposed): this covers scripts of every kind, workers, hooks, the page and server code and the IDE build scripts. The planning build scripts and the server code break it today and are split when the file set is applied (`vision/plans/file-set.md`).

### Shared script folders
<!-- k: id=conv-shared-script-folders applies=[14],[14.1],[14.2] sources=D-007,D-056 status=proposed -->
- The shared scripts are sorted by kind twice, by sub-folder and by suffix: `system/` [14.1] holds `*.system.js|py`, `workers/` [14.2] holds `*.worker.py|js`.
- A script in the wrong folder for its suffix is a naming error.
- Trading adds its own rules in the prediction-market domain's `trading-conventions.md` (its shared `scripts/decisions/` [14.3]).

### Links to shared scripts
<!-- k: id=conv-script-links applies=[30.1],name:*.system.link.js,name:*.decision.link.js sources=D-020 status=decided -->
- An agent uses a shared script through a file link named after it, in its own `scripts/` or test folder (D-020). It never copies a shared script, so fixes and improvements reach every agent at once.
- The link keeps the target's kind in its name, so `relink.system.link.js` is still a system script.

#### Standard script links at every level
<!-- k: id=conv-standard-script-links applies=name:relink.system.link.js,name:run-tests.system.link.js sources=D-025,D-031,in-20260929-2059,in-20260930-1153 status=proposed -->
- Every level below the system has `scripts/relink.system.link.js` to the shared `relink` [14.1]: [19.3.2], [21.3.2], [30.3]. Called through it, relink works on that agent only. The system runs [14.1] directly.
- Every `tests/agents/` and `tests/scripts/` folder has its own `run-tests.system.link.js` to the shared `run-tests` [14.1]. Called from there, it presets the kind (`agents` or `scripts`) and that folder's `tests.config.json`.
- A running agent's `scripts/run-tests.system.link.js` (like [30.2]) runs both kinds (for the scheduler, `before_promote` and `npm test`).
- `create-agent` [14.1] adds these links when it scaffolds a new agent.

## Per-agent config files
<!-- k: id=conv-agent-config-files applies=[27],[27.2],name:*.workers.json,name:*.links.json,[11],[19.2],[21.2] sources=D-006,D-014,D-029,D-031,in-20260930-0938,D-056 status=decided -->
Every agent keeps its own config files as real files in its own `configs/`:

| File | What it holds | Examples |
|---|---|---|
| `[name].config.json` | the agent's own config: mode, its own settings, `secret_keys` | [27.2] |
| `[name].workers.json` | its jobs (D-029) | [11.10], [19.2.1], [21.2.1], [27.4] |
| `[name].links.json` | its file links (D-031) | [11.13], [19.2.3], [21.2.3], [27.3] |

- `[name]` is `system` for the system agent, the domain folder name for a domain agent (`prediction-market-agents`), and the agent's name otherwise (`[agent-id].config.json`).
- The shared configs have fixed names: [11.1] `system.config.json` (global settings) and [11.11] `models.config.json` (routing). An agent reaches them through file links named `system.config.link.json` and `models.config.link.json` [27.1].
- Scripts find these files by scanning `agents/**/configs/*.workers.json` and `agents/**/configs/*.links.json`, real files only.
- Formats: data-schemas.md, `schema-agent-config`, `schema-workers-file`, `schema-links-file`.
- Trading adds its own rules in the prediction-market domain's `trading-conventions.md` (the domain's own config [19.2.4], the trading fields of an agent's config).

## Standard agent folder ([2.7.1])
<!-- k: id=conv-standard-folder applies=[10],[19],[21],[23],name:package.json,name:requirements.txt,name:init.sh,name:start.sh sources=D-022,D-024,D-025,D-026,D-030,D-031,in-20260929-1703 status=decided -->
Every agent folder has the identical structure at every level: the system [10], each domain (like [19]) and every level a domain defines below it, for example, in the prediction-market domain, each strategy [21] and each trading agent [23] (D-022).

```text
[agent-folder]/
├── .claude/           # standard Claude Code folder ([2.7.2])
├── configs/           # [name].config.json, [name].workers.json, [name].links.json + file links + subagents.link/
├── scripts/           # own *.[kind].* scripts + file links + subagents.link/
├── logs/              # own logs + file links + subagents.link/
├── data/              # own data (outputs, history) + file links + subagents.link/
├── docs/              # README, role, changes, decisions, notes + file links + subagents.link/
├── tests/             # agents/ + scripts/, each with tests.config.json ([2.7.3]) + subagents.link/
├── research/          # index.json + [research-id]-[slug]/ ([2.7.3]) + subagents.link/
├── package.json       # JS deps + npm scripts
├── requirements.txt   # Python deps
├── init.sh            # setup: installs deps, then runs relink for this agent
└── start.sh           # starts this agent's session or one run
```

- Folder names are plural everywhere (`configs/`, `scripts/`, `logs/`, `docs/`).
- The level's prompt is `.claude/CLAUDE.md`, not a file at the folder root (D-024).
- Agents at the lowest level have no children, so their content folders have no `subagents.link/`.
- System-support roles are sub-agents, not folders (D-026). A role that needs its own files and runs becomes a normal agent with this folder under its domain.
- `create-agent` [14.1] scaffolds this folder; the steps are in how-to/create-agent.md.

### The system folder holds the shared files
<!-- k: id=conv-system-folder applies=[10],[2],[11],[14],[15],[16] sources=D-013,D-015,D-017,D-022 status=decided -->
- The system [10] is a domain and an agent like the others, with the same folder. Its one difference: its content folders also hold the shared files every agent uses, the shared docs [2], configs [11], scripts [14], logs [15] and data [16].
- Like every level, it reaches its children (the domains) only through `subagents.link/` ([2.7.4]). The levels each domain defines are further down, one `subagents.link/` step per level.

## Standard .claude/ folder ([2.7.2])
<!-- k: id=conv-claude-folder applies=[10.1],[19.1],[21.1],[24],name:CLAUDE.md,name:settings.json,name:settings.local.json sources=D-024,in-20260929-2025 status=decided -->
Every level has the same `.claude/` (D-024): system [10.1], domain [19.1] and the levels below it (in the prediction-market domain, strategy [21.1] and trading agent [24]).

```text
.claude/
├── CLAUDE.md                               # [x.5]  the level's prompt
├── settings.json                           # [x.6]  permissions, hooks, env, model, statusLine, outputStyle; committed
├── settings.local.json                     # [x.7]  personal overrides; git-ignored
├── rules/[topic].md                        # [x.8]
├── skills/[skill-name]/SKILL.md            # [x.2]
├── commands/[command-name].md              # [x.9]
├── agents/[subagent-name].md               # [x.1]
├── workflows/[workflow-name].js            # [x.10]
├── output-styles/[style-name].md           # [x.11]
├── agent-memory/[subagent-name]/MEMORY.md  # [x.12]
└── agent-memory-local/                     # [x.13] git-ignored
```

- Numbering: `x` is the level's `.claude` number ([10.1], [19.1], [21.1], [24]); for the example agent [23], `skills/` is [25] and `agents/` is [26].
- The tree holds generic placeholders only. Concrete skills, commands, rules and sub-agents are added later. The named ones so far are each level's self-improvement sub-agent (D-018) and the knowledge agent [10.1.1.2] with its skills [10.1.2.1] and [10.1.2.2] (D-033).
- The deny rules every `settings.json` must carry are in safety.md, `safe-settings-deny`; its keys are in data-schemas.md, `schema-claude-settings`.

### Parts of .claude/
<!-- k: id=conv-claude-parts applies=name:rules,name:skills,name:commands,path:agents/**/.claude/agents,name:workflows,name:output-styles,name:agent-memory,name:agent-memory-local,name:[topic].md,name:[skill-name]/SKILL.md,name:[command-name].md,name:[subagent-name].md,name:[workflow-name].js,name:[style-name].md,name:[subagent-name]/MEMORY.md sources=D-024,in-20260929-2025 status=decided -->
- `rules/`: topic-scoped instructions, one topic per file. A `paths:` frontmatter loads a rule only when matching files are read. Subfolders are fine.
- `skills/`: reusable prompts, one folder per skill with `SKILL.md` as its entry point and any supporting files next to it. Invoked as `/name` or automatically.
- `commands/`: single-file prompts, each invoked as `/name`.
- `agents/`: sub-agents, each with its own context window and tools. Names: `conv-support-names`.
- `workflows/`: dynamic workflow scripts (`*.js`); each becomes a `/<name>` command.
- `output-styles/`: output styles shared by the level (`*.md`).
- `agent-memory/[subagent-name]/MEMORY.md`: the persistent memory of a sub-agent with `memory: project`; committed.
- `agent-memory-local/`: the same for sub-agents with `memory: local`; kept out of git.
- File contents: data-schemas.md, `schema-claude-md-files`. Where each level's SI sub-agent keeps its memory: common/agent-architecture.md, `common-agent-memory`.

### No .claude links
<!-- k: id=conv-no-claude-links applies=[10.1],[19.1],[21.1],[24],[25],[26] sources=D-030,in-20260930-1045 status=decided -->
- For now no `.claude/` folder is linked at any level, in or out (D-030). Each session sees only its own `.claude/`.
- A parent that needs a child's skill or sub-agent reads it by path. How higher-level results reach an agent instead: common/agent-architecture.md, `common-agent-subagent-outputs`.
- The earlier parent-to-child `.claude` links (D-019) are paused. If they ever come back, they go parent to child only.

## Tests and research at every level ([2.7.3])
<!-- k: id=conv-tests-research applies=[10.8],[10.9],[19.12],[19.13],[21.12],[21.13],[49],[50],path:agents/**/tests/agents,path:agents/**/tests/scripts,name:tests.config.json,name:[test-id].test.md,name:[test-id].test.[js|py],name:tests.jsonl,path:agents/**/research/index.json,name:[research-id]-[slug] sources=D-025,in-20260929-2036 status=decided -->
Every level has `tests/` and `research/`: system [10.8], [10.9]; domain [19.12], [19.13]; and every level below (in the prediction-market domain, strategy [21.12], [21.13] and trading agent [49], [50]) (D-025).

```text
tests/
├── agents/                        # tests of the level's CLAUDE.md and sub-agents (LLM behaviour)
│   ├── tests.config.json          # every agent test: enabled, schedule, last run, result, next action
│   ├── [test-id].test.md          # scenario, fixtures, expected behaviour, how it is graded
│   └── run-tests.system.link.js   # runs this folder's config
└── scripts/                       # tests of the level's scripts
    ├── tests.config.json
    ├── [test-id].test.[js|py]
    └── run-tests.system.link.js
research/
├── index.json                     # every research item: question, status, results, decisions, links
└── [research-id]-[slug]/          # one folder per item: README.md + artifacts
```

- A test of the prompt, a sub-agent or a skill goes in the `tests/agents/` folder of the level whose `.claude/` holds it; a test of code goes in `tests/scripts/`. One test per file, named by its id at that level: `t-agents-001.test.md`, `t-scripts-001.test.js`; the file says what it tests (Target). Naming each test after its target and check instead (`{target}.{check}.test.md`) is proposed in `vision/plans/2026-10-06-2143-general-system.md`. Every test has an entry in that folder's `tests.config.json`, where the owner switches it on or off.
- Test results are written back to the config and appended to the level's `logs/tests.jsonl` (e.g. [34.2]).
- Research goes in `research/`, not in `data/`. History a level keeps as data stays in its `data/`, for example, in the prediction-market domain, the strategy's cross-variant `changes.md` [21.5].
- Formats: data-schemas.md, `schema-tests-config`, `schema-test-files`, `schema-research-index`. Steps: how-to/add-or-run-tests.md, how-to/record-research.md.

### Placement at the folder root
<!-- k: id=conv-tests-research-placement applies=[10.8],[10.9],[19.12],[19.13],[21.12],[21.13],[49],[50] sources=D-025 status=proposed -->
- `tests/` and `research/` sit at the level's folder root, next to `scripts/`, not inside `.claude/`.
- Why: tests target scripts and data as well as prompts, and `.claude/` keeps Claude Code's own layout (D-024).
- The alternative, `.claude/tests/` and `.claude/research/`, is another reading of the owner's "every claude layer". It was not chosen, and the owner has not confirmed either.

## Content folders and child links ([2.7.4])
<!-- k: id=conv-content-folders applies=name:subagents.link,path:agents/**/subagents.link/* sources=D-030,in-20260930-1045 status=decided -->
- Each content folder (`configs/`, `scripts/`, `logs/`, `data/`, `docs/`, `tests/`, `research/`) holds the level's own files and, if the level has child agents, `subagents.link/` (D-030).
- `subagents.link/` is a real folder holding one folder link per direct child, named after the child's folder and pointing at the child's folder of the same kind: system to its domains, each domain to the level below it, and so on down.
- Example for docs, in the prediction-market domain:

```text
agents/system/docs/                                        # system's own docs [2]
└── subagents.link/prediction-market/                      # [2.20.1] -> agents/trading/prediction-market/docs/
agents/trading/prediction-market/docs/                      # domain's own docs [19.6]
└── subagents.link/strategy-1-agent/                       # [19.6.1.1] -> .../strategy-1-agent/docs/
agents/trading/prediction-market/strategy-1-agent/docs/     # strategy's own docs [21.6]
└── subagents.link/pm-strategy-1.momentum-v1.opus55-test/  # [21.6.1.1] -> that agent's docs/ [46]
```

- These are the only folder links in the system, and they are links, never copies.
- A parent reads its children's files through them and writes only its own files. Grandchildren are one more `subagents.link/` down.
- `relink` [14.1] makes them from the folder tree and removes them once the child is gone. They are not listed in any links file.
- `.claude/` folders are not linked (`conv-no-claude-links`).

### Scans never follow links
<!-- k: id=conv-link-scans applies=name:subagents.link,[14.1] sources=D-030 status=proposed -->
- Tools never follow `.link` folders recursively. A scan of `agents/**` sees every real file once; anything that wants a child's files goes down one `subagents.link/` at a time.
- Scripts that list files (scheduler, relink, build-map, the index builders) read real files only.
- `check-links` [14.1] flags cycles, symlinks that neither have `.link` nor sit in a `.link` folder, folder links outside `subagents.link/`, and `subagents.link/` entries that are not a direct child's folder of the same kind.

## Links file per agent ([2.7.5])
<!-- k: id=conv-links-file applies=name:*.links.json,name:relink.system.link.js,[14.1] sources=D-031,in-20260930-1153 status=decided -->
- Every agent at every level has `configs/[name].links.json` (`[name]` as in `conv-agent-config-files`): [11.13], [19.2.3], [21.2.3], [27.3] (D-031).
- Each entry says where the link appears in the agent's own folders (`to`) and which file it points at (`from`): something in the system, its own domain or another level above it, another domain, or any other agent by its unique name.
- The shared `relink` script [14.1] builds every link in the project from these files plus the child links ([2.7.4]).
- After editing its links file, an agent reruns relink (`node scripts/relink.system.link.js`). Relink also runs when any links file changes and at review time; when exactly: common/shared-mechanics.md, `common-mech-relink-when`.
- Fields, the `from` short forms and the entry rules: data-schemas.md, `schema-links-file`, `schema-links-from`, `schema-links-rules`. Steps: how-to/add-or-change-link.md.

### Only relink makes links
<!-- k: id=conv-relink-only applies=name:*.links.json,name:init.sh,[14.1],name:*.link.* sources=D-031 status=proposed -->
- Only `relink` [14.1] creates or removes links. `init.sh`, `create-agent`, stop-or-delete and every agent call it; nobody makes a symlink by hand.
- A `.link` symlink that no links file lists and that is not a child link is removed by relink.
- Every link is a relative symlink.

## Where a new file goes
<!-- k: id=conv-file-placement applies=[0],[4],[10],[43],[45],[47],[2],[46],[15],[15.1],[15.2],[15.3],[15.4],[16],[16.1],[16.2],[16.3] sources=in-20260929-1455,D-009,D-010,D-013,D-017,D-023,D-025,D-056 status=decided -->
- A file used by two or more agents lives in the matching folder of the nearest level they share: the system's [10] for agents of different domains, their domain's for agents of one domain (`conv-promotion`). A file for one agent lives in that agent's own folder as a real file. An agent that needs someone else's file links it ([2.7.5]).
- Shared logs and data are sorted by source: `system/`, `services/`, `workers/[worker]/`, `subagents/[subagent]/` in [15]; `system/`, `workers/[worker]/`, `subagents/[subagent]/` in [16] (D-009, D-010).
- Shared docs go in [2], an agent's own docs in its `docs/` (e.g. [46]). The repo root holds only `README.md` [1]; the file every Claude reads first is the system's `.claude/CLAUDE.md` [10.1.5] (D-045).
- Our own apps, the apps we use and research clones go in `apps/` [43] (see Apps and outside code), the prediction-market domain's dashboard in `apps/trading-ui/` [45] (D-045), secrets only in `.secrets/` [47], never under `agents/`.
- Tests go in the level's `tests/`, research in its `research/` ([2.7.3]).

### Apps and outside code
<!-- k: id=conv-apps applies=[43],[53],[53.4],[53.4.1],[53.4.2],[53.4.3],[55],[48],[2.18.5] sources=in-20261006-2206,D-055 status=decided -->
- Every app in `apps/` has a `docs/` folder with `vision.md`, `README.md` and `rebuild-prompt.md`, written like the system's (the vision, README and rebuild prompt skills have an outline for an app). For an outside app these three docs are its only metadata for now: no How it works or Details for each of its files (owner, 2026-10-06, D-055).
- **Research clone:** a repository cloned to study it goes into `apps/temp/<name>/` [55]: the clone in `repo/`, never committed (ignored in [48]); our three docs in `docs/` only when the owner asks. Findings go to the research folder of the agent that studies it ([2.7.3]). The clone is deleted when the research is done.
- **An app we use:** forked on GitHub and kept in `apps/<name>/`: our docs in `docs/`, our fork in `repo/` (as a git submodule, proposed). In the fork, `main` is ours (every change of ours, what we run) and `upstream` follows the source's main branch and is never changed by us. From time to time `upstream` is updated from the source and merged into `main`, the app's tests run, and the update is noted in its docs and in the list of apps [2.18.5].
- Every app has a row in the list of apps [2.18.5]: kind (ours, fork, research clone), source, fork, branches, the commit in use, last update from the source, used by.
- Turning an app fully into the system's way (Details for every file, one job per file, features, the other docs) is a skill written on the owner's request (`adopt-app`, proposed) and kept up like every skill.

### Promotion to shared
<!-- k: id=conv-promotion applies=[10],[31],[14.2],[30] sources=D-020,derived,D-056 status=proposed -->
- When a second agent needs an agent-local file, it moves into the matching shared folder of the nearest level both agents share: their domain's for two agents of one domain, the system's [10] (e.g. [14.2]) for agents of different domains. Every agent that needs it gets a file link to it.
- Until then it stays in the one agent's folder.

### Producer outputs
<!-- k: id=conv-producer-outputs applies=[35.2],[16.2],[16.3],[15.3],[34],[31],[14.2] sources=D-010,D-020 status=proposed -->
- An agent's own scripts write logs to its `logs/` [34] and data to `data/[producer]/`, one folder per producer [35.2].
- Every producer also keeps a stable `latest.*` file next to its dated files, and links point at it, so file links do not break when dated files rotate: data-schemas.md, `schema-latest-files`.
- Runtime state (a job's last run, result, next run) never goes into a workers file; the scheduler keeps it in [16.1].

## Docs
<!-- k: id=conv-docs applies=[2],[46],[46.1],[46.2],[19.6],[21.6],[1] sources=D-004,D-005,D-017,D-020,in-20260929-1623 status=decided -->
- Docs are Markdown files (D-005).
- The shared docs are real files in `agents/system/docs/` [2]. Each agent's own docs are real files in its own `docs/`: README, role (in the prediction-market domain, strategy), changes, decisions, notes ([46.2]).
- An agent reaches a shared doc through a file link in its `docs/`, e.g. `safety.link.md` [46.1] (D-020). A parent reaches its children's docs through `docs/subagents.link/` ([2.7.4]).
- The repo root has only `README.md` [1], which points into [2].
- Until the repo exists, the working copy of [2] is `vision/docs/`.

### Doc format, versions and numbers
<!-- k: id=conv-docs-format applies=path:agents/system/docs/*.md,path:agents/system/docs/how-to/*.md,path:agents/system/docs/common/*.md,[2.10.3] sources=derived status=proposed -->
- Every doc starts with its title and version, `# Agent OS: <Title> (vX.Y)`, and ends with a `## Changelog`. Every change bumps the version and adds a changelog line with the date and the input or decision behind it.
- Every folder and file in the tree has a number `[n]`. Numbers are never reused. A moved or retired object keeps a stub section ("moved to [x]", "retired") so old references still resolve.
- `file-tree.md` [2.13] and `feature-map.md` [2.12] stay in sync: every [n] the feature map names exists in the tree.
- Docs refer to files by number and name, e.g. "the links file [27.3]". Plain English, short sentences, no em-dashes.

### One fact in one place
<!-- k: id=conv-docs-one-fact applies=[2],[2.1],[2.6],[2.13],[2.10],[2.10.1],[2.10.2],[10.1.1.2] sources=D-033,in-20260930-1533 status=decided -->
- Each fact lives in one place. A file doc in [2.13] says what the file is and points to the topic doc that holds a shared rule. The topic doc's knowledge tag says which files the rule applies to, so one rule covers many files and one file gets many rules (the owner's "map many to many").
- Decisions are history, not a separate kind of knowledge: the rule a decision made lives in a topic doc, and decisions.md [2.6] records when and why.
- Raw owner inputs in [2.10] are stored word for word and never edited.
- The tag format and the layers: docs/README.md [2.1]. The flow every input and change goes through: how-to/process-an-input.md.

## Git
<!-- k: id=conv-git applies=[0],[48],name:settings.json,name:settings.local.json,name:agent-memory-local,path:agents/**/logs,path:agents/**/data sources=D-028,in-20260930-0752 status=decided -->
- Everything that defines the system is committed: configs, scripts, prompts, docs, tests, research, and every shared `.claude/` and `.cursor/` file (sub-agents, skills, `settings.json`).
- Runtime output (the content of `logs/` and `data/`), machine-local tool state and secrets are not committed. The folders themselves stay in git through `.gitkeep`, so a fresh clone has the right shape.
- The exact ignore list, and why each line is there: safety.md, `safe-gitignore`.

### Git hooks
<!-- k: id=conv-git-hooks applies=[10.6],[14.1] sources=D-031 status=proposed -->
- The system's `init.sh` [10.6] installs the repo's git hooks, so running it once after a clone sets them up.
- The hooks run relink at review time: `pre-commit` blocks a commit that leaves a required link broken; `post-merge` and `post-checkout` relink after a pull or a branch switch. Details: common/shared-mechanics.md, `common-mech-relink-when`.

## Open questions
<!-- k: id=conv-open applies=[27.3],[30],[11.13] sources=D-031,D-032,derived,D-056 status=open -->
- Is a change to an agent's links file [27.3] a new version, or may small additions happen in place?
- Are there script kinds besides worker and system ([30])? Proposed (D-058): a domain may add its own, as the prediction-market domain adds `decision`.
- Are the symlinks themselves committed, or rebuilt by relink after every clone and pull ([11.13], proposed: commit them)? The runtime `logs/` and `data/` ignore rules would also ignore the links inside those folders.

## Changelog
- v0.5 (2026-10-07): trading parts moved to the prediction-market domain's `trading-conventions.md` (D-056, D-058); the copy-trading code `ct`, its example and [42] removed (D-056).
- v0.4 (2026-10-07): metadata file names without the file's extension, and the empty Details files (D-057, in-20261007-0904).
- v0.3 (2026-10-06): apps and outside code (D-055).
- v0.2 (2026-10-06): one job per code file (D-050).
- v0.1 (2026-09-30): created from file-tree.md v1.15, vision.md v0.19 and the owner inputs (D-033).
