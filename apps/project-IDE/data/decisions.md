# Agent OS: Decisions (v1.13)

This is the decision log: what the owner decided, when, why, and which inputs and objects it touched. It is history. The rules a decision made live in the topic docs (conventions.md, safety.md, data-schemas.md, common/, how-to/ and the file docs in file-tree.md), and each entry below points to where its rule lives today. When a later decision changes an earlier one, the earlier entry stays and its status says what replaced it. Numbers are never reused. The knowledge agent [10.1.1.2] adds one entry per owner decision (knowledge-intake, step 6). D-033 (the knowledge base itself) is recorded by its own entry.

Status words: **active** (in force), **partly superseded by D-0xx** (some of it replaced, the rest in force), **superseded by D-0xx** (fully replaced, kept for history).

## 2026-09-29

### D-001: Keep symlinks for shared things
<!-- k: id=d-001 applies=[10],name:*.link.*,name:subagents.link sources=in-20260929-1455 status=decided -->
- **Decision:** Shared things (configs, workers, sub-agents, scripts, logs, data) stay in shared places and reach an agent's folder through symlinks, not copies. This settles the v0.1 idea "needed files are symlinked into the agent's folder".
- **Date:** 2026-09-29
- **Why:** the owner's first layout marks every shared folder "common and symlinks for every agent folder"; copies would drift out of date.
- **Status:** active. What gets linked and how changed later: file links (D-020), child links (D-030), the links file (D-031). Pull-based subscriptions (vision §5.2) stay an open alternative.
- **Sources:** in-20260929-1455
- **Changed:** vision.md §7; the shared folders under [10] and every link that followed.
- **Rules now in:** conventions.md `conv-link-names`, `conv-file-links`; common/shared-mechanics.md `common-mech-links`.

### D-002: Every symlink has .link in its name
<!-- k: id=d-002 applies=[2.7],name:*.link.*,name:subagents.link sources=in-20260929-1520 status=decided -->
- **Decision:** Every symlinked file or folder has `.link` in its name, so a link can be told from a real file by its name alone.
- **Date:** 2026-09-29
- **Why:** owner rule: "all symlinked folders or files should have in a name .link".
- **Status:** partly superseded by D-030: links directly inside a `.link` folder (the entries of `subagents.link/`) need no `.link` of their own.
- **Sources:** in-20260929-1520
- **Changed:** the `.link` rule in [2.7]; the example agent's links [26.1], [27.1], [29], [30.1], [30.2], [34.1], [36], [36.1] renamed (file tree v0.5).
- **Rules now in:** conventions.md `conv-link-names`.

### D-003: Per-agent docs live centrally
<!-- k: id=d-003 applies=none sources=in-20260929-1520 status=retired -->
- **Decision:** Each agent's docs lived in `docs/agents/[domain]/[agent-name]/` and were linked into the agent folder as `docs.link/`.
- **Date:** 2026-09-29
- **Why:** the owner asked for "per agent docs symlinked from agent folder".
- **Status:** superseded by D-017: each agent now has its own real `docs/` [46].
- **Sources:** in-20260929-1520
- **Changed:** [2.19] `docs/agents/` and [29] `docs.link/`, both retired since.
- **Rules now in:** conventions.md `conv-docs`.

### D-004: One docs root with common knowledge, indexes, schemas, flows and metrics
<!-- k: id=d-004 applies=[2],[2.14],[2.15],[2.16],[2.17],[2.18] sources=in-20260929-1520 status=decided -->
- **Decision:** `docs/` is the single docs root. Besides the vision it holds common knowledge (`common/`), an index of all things (`index/`), `data-schemas.md`, `flows.md` and `metrics.md`.
- **Date:** 2026-09-29
- **Why:** the owner accepted data schemas, flows and metrics, and asked for "common things and indexes of all things".
- **Status:** partly superseded by D-017: the root moved from the repo top to `agents/system/docs/` [2]. The contents stay.
- **Sources:** in-20260929-1520
- **Changed:** new [2.14], [2.15], [2.16], [2.17], [2.18]; `agents/docs/` [5] merged into [2] ([7] to [2.17.1], [8] to [2.18], [9] to [2.17.2]).
- **Rules now in:** conventions.md `conv-docs`; file docs [2], [2.17], [2.18].

### D-005: Data as JSON and Markdown files for now
<!-- k: id=d-005 applies=[15],[16],[34],[35],[2.14] sources=in-20260929-1455 status=decided -->
- **Decision:** All data, configs and logs are plain JSON, JSONL and Markdown files for now. No database.
- **Date:** 2026-09-29
- **Why:** the owner: "for now let's just use for data json and md files". It is the simplest start.
- **Status:** active.
- **Sources:** in-20260929-1455
- **Changed:** vision.md §10; configs in JSON [11]; data and logs [15], [16], [34], [35].
- **Rules now in:** data-schemas.md `schema-formats`.

### D-006: Two config types: global and per agent
<!-- k: id=d-006 applies=[11],[11.1],[27.2] sources=in-20260929-1537 status=decided -->
- **Decision:** Configs come in two types for now: one global `system.config.json` with sections (split into files later when a section gets long) and one config per agent. Which settings are common and which are individual is worked out with example agents.
- **Date:** 2026-09-29
- **Why:** the owner: "split it to two types of config for now", with "all the things that we can control and configure globally" in one file.
- **Status:** partly superseded by D-014: the per-agent config is a real file in the agent folder, not a central file linked in as `config.link.json`. Jobs (D-029) and links (D-031) later got their own files. The shape is still open.
- **Sources:** in-20260929-1537
- **Changed:** [11.1] (the v0.6 files became its sections; [11.3]-[11.9] retired), [11.2], [27], [27.1], [28] (file tree v0.7).
- **Rules now in:** conventions.md `conv-agent-config-files`; data-schemas.md `schema-system-config`, `schema-agent-config`; common/shared-mechanics.md `common-mech-config-merge`.

### D-007: Workers are scripts
<!-- k: id=d-007 applies=[14],[14.2],[30],[31] sources=in-20260929-1545 status=decided -->
- **Decision:** Workers are just scripts. All scripts live in `scripts/`: workers, decision (buy/sell) and system scripts, either shared or per agent. Workers are described in config: which exist, their schedule, how they run, what they are for.
- **Date:** 2026-09-29
- **Why:** the owner: "how I see workers is just scripts".
- **Status:** partly superseded by D-029: the single `workers.config.json` became one jobs file per agent.
- **Sources:** in-20260929-1545
- **Changed:** [12] retired (scripts in [14.2]); [11.10]; [14] sub-folders `system/`, `workers/`, `decisions/` and the suffix rule; [33] renamed `make-buy.decision.js`; [30.2] retired.
- **Rules now in:** conventions.md `conv-script-kinds`; data-schemas.md `schema-workers-file`.

### D-008: Sub-agents are Claude Code sub-agents
<!-- k: id=d-008 applies=[10.1.1],[19.1.1],[21.1.1],[26] sources=in-20260929-1545 status=decided -->
- **Decision:** Sub-agents are Claude Code sub-agents under `.claude/agents/`, not a separate `subagents/` folder. For now only system-wide ones exist.
- **Date:** 2026-09-29
- **Why:** the owner: "sub agents ... will be sub agents under Claude Code".
- **Status:** partly superseded by D-016 and D-018: sub-agents now exist at every `.claude/` level, not only the system's.
- **Sources:** in-20260929-1545
- **Changed:** [13] moved to [10.1.1].
- **Rules now in:** common/agent-architecture.md `common-agent-subagents`; conventions.md `conv-claude-parts`.

### D-009: Logs are organised by source
<!-- k: id=d-009 applies=[15] sources=in-20260929-1545 status=decided -->
- **Decision:** Shared logs are organised by source (system, services, workers, sub-agents), and some are linked into agents.
- **Date:** 2026-09-29
- **Why:** the owner: logs "by service, by worker, by sub agents, agent".
- **Status:** partly superseded by D-014 (an agent's own logs are real files in its own `logs/` [34]) and D-020 (shared logs are linked file by file).
- **Sources:** in-20260929-1545
- **Changed:** [15.1]-[15.5]; [34].
- **Rules now in:** common/shared-mechanics.md `common-mech-logging`.

### D-010: Data is organised by source
<!-- k: id=d-010 applies=[16] sources=in-20260929-1545 status=decided -->
- **Decision:** Shared data is organised by source (system, workers, sub-agents), and some is linked into agents.
- **Date:** 2026-09-29
- **Why:** the owner: data "per worker, per agent, per sub agent, per system".
- **Status:** partly superseded by D-014 (an agent's own data is real files in its own `data/` [35]) and D-020 (shared data is linked file by file).
- **Sources:** in-20260929-1545
- **Changed:** [16.1]-[16.4]; [35].
- **Rules now in:** conventions.md `conv-producer-outputs`; common/agent-architecture.md `common-agent-data`.

### D-011: Model and platform routing is config
<!-- k: id=d-011 applies=[11.11] sources=in-20260929-1545 status=decided -->
- **Decision:** Which platform and model each agent, sub-agent and AI worker uses is config in its own file, `models.config.json`. There is no `platforms-and-models/` folder.
- **Date:** 2026-09-29
- **Why:** the owner: routing "should be also kind of in the config ... separated file from the common".
- **Status:** active. D-029 added that a job may name its own model; otherwise its route applies.
- **Sources:** in-20260929-1545
- **Changed:** [17] moved to [11.11]; [11.1] lost its routing section.
- **Rules now in:** data-schemas.md `schema-models-config`; how-to/add-platform-or-model.md.

### D-012: Every agent has a globally unique name
<!-- k: id=d-012 applies=[2.7],[2.18.1],[14.1],[23] sources=in-20260929-1607 status=decided -->
- **Decision:** Every agent's name is unique across all domains and is its ID everywhere: folder, configs, logs, data, docs, indexes, UI and routes. The agents index is the registry and create-agent checks it.
- **Date:** 2026-09-29
- **Why:** the owner: "every agent supposed to have unique name". With hundreds of agents in several domains, one ID must mean one agent.
- **Status:** partly superseded by D-032: the proposed name format `[domain]-[modification]-v[N]-agent-[platform-model]-[test|live]` was replaced by the strategy-first format. Uniqueness is unchanged.
- **Sources:** in-20260929-1607
- **Changed:** the naming rule in [2.7]; registry [2.18.1]; the check in `create-agent` [14.1]; [2.11.1]; [22], [23] renamed.
- **Rules now in:** conventions.md `conv-agent-ids`, `conv-no-rename`; data-schemas.md `schema-agent-ids`.

### D-013: System is a domain
<!-- k: id=d-013 applies=[4],[10],[19] sources=in-20260929-1616 status=decided -->
- **Decision:** `system` is a domain like the trading domains. Domains sit directly under `agents/` (`agents/system/`, `agents/prediction-market-agents/`, `agents/copy-trading-agents/`).
- **Date:** 2026-09-29
- **Why:** the owner: "let's at all make system as also domain"; the same shape everywhere.
- **Status:** active.
- **Sources:** in-20260929-1616
- **Changed:** [4]; [10]; [18] `trading-domains/` retired.
- **Rules now in:** conventions.md `conv-standard-folder`, `conv-system-folder`.

### D-014: Every agent has the same folders with its own real files
<!-- k: id=d-014 applies=[27],[30],[34],[35] sources=in-20260929-1616 status=decided -->
- **Decision:** Every agent, system and trading alike, has the same folders `configs/`, `scripts/`, `logs/`, `data/`, holding its own real files. At the time each also had a `system.link/` folder link to the system folder of the same kind.
- **Date:** 2026-09-29
- **Why:** the owner: scripts, configs, data and logs "should have system and per" agent.
- **Status:** partly superseded by D-020: the `system.link/` folder links became individual file links. D-017 and D-025 added `docs/`, `tests/` and `research/`. It replaced the central per-agent config location of D-006 and the agent part of D-009 and D-010.
- **Sources:** in-20260929-1616
- **Changed:** [27], [30], [34], [35] became real folders; [27.2] own config; [35.2] own data; [36], [36.1], [36.2] retired.
- **Rules now in:** conventions.md `conv-standard-folder`.

### D-015: The system holds the shared files and sees every agent
<!-- k: id=d-015 applies=[11],[14],[15],[16] sources=in-20260929-1616 status=decided -->
- **Decision:** The system domain has the same folders, holding the shared files, plus `agents/[agent-name].link/` views of every agent's folder of the same kind, giving one view over everything.
- **Date:** 2026-09-29
- **Why:** the owner: the system has the same folders and "only difference that there also symlinked another agents same directories".
- **Status:** partly superseded by D-030: the flat views became one `subagents.link/` per level, linking only direct children. The shared files stay in the system's folders.
- **Sources:** in-20260929-1616
- **Changed:** views [11.2.1], [14.4.1], [15.5.1], [16.4.1] (now `subagents.link/` entries).
- **Rules now in:** conventions.md `conv-system-folder`, `conv-content-folders`.

### D-016: .claude/ at every domain and strategy level
<!-- k: id=d-016 applies=[10.1],[19.1],[21.1] sources=in-20260929-1616 status=decided -->
- **Decision:** `.claude/` exists at every domain level (including system) and at every strategy level. At the time, each agent's own `.claude/` linked them in.
- **Date:** 2026-09-29
- **Why:** the owner: "we'll have .claude agent on a level of every domain including system and on every strategy".
- **Status:** partly superseded by D-019 (links go parent to child only) and then D-030 (no `.claude` links at all for now). D-024 later gave every level the full standard layout.
- **Sources:** in-20260929-1616
- **Changed:** [10.1], [19.1], [21.1]; upward links [25.1]-[25.3], [26.1]-[26.3] (retired since).
- **Rules now in:** conventions.md `conv-claude-folder`, `conv-no-claude-links`.

### D-017: Docs follow the same pattern
<!-- k: id=d-017 applies=[2],[46],[1] sources=in-20260929-1623 status=decided -->
- **Decision:** Docs follow the same pattern as configs, scripts, logs and data. Each agent has a real `docs/` (README, strategy, changes, decisions, notes). The shared docs move from the top-level `docs/` to `agents/system/docs/`. The repo root keeps only `README.md`, which points there.
- **Date:** 2026-09-29
- **Why:** the owner: "let's do same with a docs and put it in a system docs".
- **Status:** partly superseded by D-020 (the agent's `docs/system.link/` became file links such as `safety.link.md`) and D-030 (the views of every agent's docs became `subagents.link/`). It superseded D-003.
- **Sources:** in-20260929-1623
- **Changed:** [2] moved to `agents/system/docs/` (numbers kept); new [46], [46.1], [46.2], [2.20]; [2.19], [29] retired; [1] is the only root doc.
- **Rules now in:** conventions.md `conv-docs`.

### D-018: Domain owner and self-improvement are sub-agents
<!-- k: id=d-018 applies=[10.1.1.1],[19.1.1.2],[21.1.1.1] sources=in-20260929-1630 status=decided -->
- **Decision:** There are no separate folders for domain agents or self-improvement agents. The domain owner is a sub-agent in the domain's `.claude/agents/`. Self-improvement is a sub-agent at every `.claude/` level, scoped to that level. Their memory was proposed in `agents/system/data/subagents/[name]/`.
- **Date:** 2026-09-29
- **Why:** the owner: the domain owner "will be inside domain .claude", and self-improvement "will be moved to every .claude subagent".
- **Status:** partly superseded by D-022 (the domain's own `CLAUDE.md` is the domain owner, so its sub-agent file is gone) and D-024 (SI memory proposed in `.claude/agent-memory/`). The SI sub-agent per level is active.
- **Sources:** in-20260929-1630
- **Changed:** [20] and [22] retired; new [19.1.1.1] (retired since), [10.1.1.1], [19.1.1.2], [21.1.1.1]; [2.18.3].
- **Rules now in:** common/self-improvement-templates.md `common-si-purpose`; conventions.md `conv-support-names`.

### D-019: .claude links go parent to child only
<!-- k: id=d-019 applies=[10.1],[19.1],[21.1],[24] sources=in-20260929-1649 status=retired -->
- **Decision:** `.claude` links go from parent to child only (system, then domains, then strategies, then agents); lower levels never link up. We also proposed that every run starts at the top, which D-021 withdrew.
- **Date:** 2026-09-29
- **Why:** the owner: "lower level agents should not have links on parents, only parents should have links to all child agents".
- **Status:** superseded by D-030: no `.claude` folder is linked at any level for now (paused, not deleted: if `.claude` links come back, they go parent to child). D-020 answered its follow-up question.
- **Sources:** in-20260929-1649
- **Changed:** down-links [10.1.3], [10.1.4], [19.1.3], [19.1.4], [21.1.3], [21.1.4] (all retired since); upward links [25.1]-[25.3], [26.1]-[26.3] retired; [24] holds own files only.
- **Rules now in:** conventions.md `conv-no-claude-links`.

### D-020: Agents link individual files
<!-- k: id=d-020 applies=[27.1],[30.1],[34.1],[35.1],[46.1] sources=in-20260929-1656 status=decided -->
- **Decision:** Inside an agent's `configs/`, `scripts/`, `logs/`, `data/` and `docs/` there are no folder links. There are individual file links (`[name].link.[ext]`), only to the files that agent's logic needs, from any folder. The set is chosen at creation and updated by self-improvement.
- **Date:** 2026-09-29
- **Why:** the owner: "not a full folder but individual files from all of the folders if they need for this logic".
- **Status:** partly superseded by D-031: the list moved from a `links` section of the agent config to its own links file, and `relink` (not `init.sh`) builds the links. The file-link rules stay. It superseded D-014's folder links for agents.
- **Sources:** in-20260929-1656
- **Changed:** [27.1], [30.1], [34.1], [35.1], [46.1] became file-link sets; [27.3] (then a config section); [40].
- **Rules now in:** conventions.md `conv-file-links`, `conv-file-link-names`; common/agent-architecture.md `common-agent-data`.

### D-021: No domain links to strategies' agents and skills
<!-- k: id=d-021 applies=[10.1],[14.1],[24] sources=in-20260929-1658 status=proposed -->
- **Decision:** The domain level has no `.claude` links down to its strategies' sub-agents and skills. Our proposal in its place: each level runs in its own folder, a trading agent runs in its own folder, and higher-level sub-agents hand their results to agents as data files linked per D-020.
- **Date:** 2026-09-29
- **Why:** the owner: "I don't need here links from strategies agents and skills".
- **Status:** partly superseded by D-030: the removed links are now part of "no `.claude` links at any level". The run-in-own-folder part is still a proposal.
- **Sources:** in-20260929-1658
- **Changed:** [19.1.3], [19.1.4] retired; [10.1] run model; `run-agent` in [14.1]; [24].
- **Rules now in:** common/agent-architecture.md `common-agent-run-start`, `common-agent-subagent-outputs`.

### D-022: Three agent levels, one identical folder
<!-- k: id=d-022 applies=[2.7],[10],[19],[21],[23] sources=in-20260929-1703 status=decided -->
- **Decision:** There are three levels of agents, the system (manages all domains and system development), each domain and each strategy, and every agent folder has the identical file structure. Trading variants under a strategy have the same structure. The domain's own `CLAUDE.md` is the domain owner.
- **Date:** 2026-09-29
- **Why:** the owner: "generally they should be identical by files structure", one level per responsibility.
- **Status:** partly superseded by D-024 (`CLAUDE.md` inside `.claude/`; SI memory in `.claude/agent-memory/`, proposed), D-025 (research out of `data/`) and D-030 (the system's per-agent views became `subagents.link/`).
- **Sources:** in-20260929-1703
- **Changed:** the standard folder [2.7.1]; level files [10.3]-[10.7], [19.2]-[19.11], [21.2]-[21.11]; [19.7] became the domain owner; [19.1.1.1] retired.
- **Rules now in:** conventions.md `conv-standard-folder`.

### D-023: A secrets store outside agents/
<!-- k: id=d-023 applies=[47]/**,[48],[14.1] sources=in-20260929-1706 status=decided -->
- **Decision:** Secrets live in a git-ignored `.secrets/` at the repo root, outside `agents/`, with `test/` and `live/` kept apart and a metadata index without values. Scripts load keys at run time through `load-secret`; secrets are never linked into agent folders, never logged and never put in LLM context. The owner asked for the store; the design was ours.
- **Date:** 2026-09-29
- **Why:** the owner: "let's add secrets for agents or scripts ... where we would store private keys".
- **Status:** partly superseded by D-027: one `.env` per mode instead of one file per account, key names (`secret_keys`) instead of refs for loading, and the Claude Code deny rule covers `.secrets/live/**` only.
- **Sources:** in-20260929-1706
- **Changed:** [47], [48], `load-secret` and the secrets check in `check-links` [14.1]; [2.8]; the `secret_ref` scheme in [2.7]; [2.11.6].
- **Rules now in:** safety.md `safe-secrets-store`, `safe-secret-loading`, `safe-secrets-never`.

### D-024: The standard .claude/ layout at every level
<!-- k: id=d-024 applies=[10.1],[19.1],[21.1],[24] sources=in-20260929-2025 status=decided -->
- **Decision:** Every `.claude/` folder (system, domain, strategy, variant) follows the standard Claude Code layout, with `CLAUDE.md` inside `.claude/` rather than at the folder root. Only generic placeholders for now; concrete skills and logic come later.
- **Date:** 2026-09-29
- **Why:** the owner: "populate .claude folder with a current full structure ... keep CLAUDE.md inside this folder ... we'll fill it later".
- **Status:** partly superseded by D-030 (the `.claude` down-links it kept are gone) and D-027 (the deny rule is `.secrets/live/**`). SI memory in `.claude/agent-memory/` is still proposed.
- **Sources:** in-20260929-2025
- **Changed:** [2.7.2]; [10.1.5]-[10.1.13], [19.1.5]-[19.1.13], [21.1.5]-[21.1.13], [24.5]-[24.13]; [37], [10.3], [19.7], [21.7] moved inside `.claude/`; [48] extended.
- **Rules now in:** conventions.md `conv-claude-folder`, `conv-claude-parts`; data-schemas.md `schema-claude-settings`.

### D-025: Tests and research at every level
<!-- k: id=d-025 applies=[10.8],[10.9],[19.12],[19.13],[21.12],[21.13],[49],[50],[14.1] sources=in-20260929-2036,in-20260929-2059 status=decided -->
- **Decision:** Every level has `tests/` with `agents/` (the prompt and sub-agents) and `scripts/` (code), each with a `tests.config.json` the owner can switch tests on and off in, run by one shared `run-tests` script that writes results back. Every level also has `research/` with an `index.json` history and one folder per item. Placement at the folder root and the fields are our proposal.
- **Date:** 2026-09-29
- **Why:** the owner wanted to enable or disable each test and see its last run, result and next action, and to keep the history of research, results and decisions.
- **Status:** active. A follow-up owner question (in-20260929-2059) gave each test folder its own runner link.
- **Sources:** in-20260929-2036, in-20260929-2059
- **Changed:** [2.7.3]; [10.8], [10.9], [19.12], [19.13], [21.12], [21.13], [49], [50]; `run-tests` in [14.1]; [30.2]; [34.2]; [2.14]; [2.11.7], [2.11.8]; runner links [10.8.1.3], [10.8.2.3], [19.12.1.3], [19.12.2.3], [21.12.1.3], [21.12.2.3], [49.1.3], [49.2.3].
- **Rules now in:** conventions.md `conv-tests-research`, `conv-standard-script-links`; data-schemas.md `schema-tests-config`, `schema-research-index`; how-to/add-or-run-tests.md; how-to/record-research.md.

### D-026: System-support roles are sub-agents
<!-- k: id=d-026 applies=[10.1.1],[10.1.1.2] sources=in-20260929-2147 status=decided -->
- **Decision:** System-support roles (docs, development, improvement, analysis, research) are sub-agents in `agents/system/.claude/agents/`, not agent folders. A role that ever needs its own files and runs becomes a normal agent with the standard folder.
- **Date:** 2026-09-29 (owner edit on the File Tree page)
- **Why:** like the domain owner and SI roles (D-018), a support role needs a prompt and tools, not its own folders.
- **Status:** active. D-033 renamed the example `sys-docs-agent` to `sys-knowledge-agent`.
- **Sources:** in-20260929-2147
- **Changed:** [10.2] retired; [10.1.1.2] added.
- **Rules now in:** conventions.md `conv-standard-folder`, `conv-support-names`.

### D-027: All test keys in one .env
<!-- k: id=d-027 applies=[47.1.1],[47.2.1],[14.1],name:settings.json sources=in-20260929-2147,in-20260930-0804,in-20260930-0812 status=decided -->
- **Decision:** All test keys live in one `.secrets/test/.env`, grouped in sections with prefixed names, and agents may read and update it. `live/.env` mirrors the same key names with live values, owner only, in a later phase. Scripts get only the keys their config declares, through the shared loader.
- **Date:** 2026-09-29 (owner edit); details confirmed on 2026-09-30
- **Why:** test credentials are safe to share with agents, and one file with prefixes is simpler than many files. Live money stays with the owner.
- **Status:** active. On 2026-09-30 the owner dropped the open questions about splitting the file and logging reads, and asked for `live/.env` to be set up the same way.
- **Sources:** in-20260929-2147, in-20260930-0804, in-20260930-0812
- **Changed:** [47.1.1], [47.2.1] became `.env` files; the deny rule in [10.1.6], [19.1.6], [21.1.6], [24.6]; `secret_keys` and `load-secret` in [14.1]; key editing in the UI [45].
- **Rules now in:** safety.md `safe-test-keys`, `safe-live-keys`, `safe-secret-loading`, `safe-settings-deny`; data-schemas.md `schema-env-keys`.

### D-028: .gitignore is a real, commented file
<!-- k: id=d-028 applies=[48] sources=in-20260929-2147,in-20260930-0752 status=decided -->
- **Decision:** The repo `.gitignore` is a real file in which every entry has a comment saying why: secrets, local Claude Code settings and memory, build junk. On 2026-09-30 the owner added runtime logs and data (content ignored, folders kept) and local Cursor state.
- **Date:** 2026-09-29 (owner edit); extended 2026-09-30
- **Why:** keep secrets and machine-local state out of git, and make every ignore line explain itself.
- **Status:** active.
- **Sources:** in-20260929-2147, in-20260930-0752
- **Changed:** [48].
- **Rules now in:** safety.md `safe-gitignore`; conventions.md `conv-git`.

## 2026-09-30

### D-029: A jobs file for every agent
<!-- k: id=d-029 applies=name:*.workers.json,[14.1],[16.1] sources=in-20260930-0938 status=decided -->
- **Decision:** Every agent (system, domain, strategy, variant) has its own jobs file `configs/[name].workers.json`, where it can see, change and turn off everything it runs. A job is a script or an AI run (the agent, a sub-agent, skill, workflow or command) with a schedule, where it runs, the platform and the model. One central scheduler runs them all. The format is our proposal.
- **Date:** 2026-09-30
- **Why:** the owner wants to see and change every schedule, turn jobs off, choose cloud or headless, and later move some jobs to Cursor or Codex.
- **Status:** partly superseded by D-030: the system's jobs view by domain (`configs/workers/[domain]/`, [11.12]) became `configs/subagents.link/` [11.2]. It superseded D-007's single `workers.config.json` and updated D-011.
- **Sources:** in-20260930-0938
- **Changed:** [11.10] renamed `system.workers.json`; new [19.2.1], [21.2.1], [27.4]; [28] moved to [27.4]; `scheduler` and `run-job` in [14.1]; `scheduler-state.json` in [16.1]; [11.1] `schedules`; [11.11]; [2.11.1], [2.11.2], [2.14], [2.18.2], [40], [41].
- **Rules now in:** conventions.md `conv-agent-config-files`; data-schemas.md `schema-workers-file`; common/shared-mechanics.md `common-mech-scheduler`.

### D-030: One content-folder template with subagents.link/
<!-- k: id=d-030 applies=[2.7],name:subagents.link,[10.1],[19.1],[21.1],[24] sources=in-20260930-1045 status=decided -->
- **Decision:** At every level, each content folder (`configs/`, `scripts/`, `logs/`, `data/`, `docs/`, `tests/`, `research/`) holds the level's own files plus `subagents.link/` with one folder link per direct child agent, pointing at the child's folder of the same kind. Trading agents have no children, so no `subagents.link/`. For now no `.claude` folder is linked at any level.
- **Date:** 2026-09-30
- **Why:** the owner wants the same template in every layer, so each level reaches its children's docs, configs, data and so on one step at a time.
- **Status:** active. It replaced the system's flat views (D-015, D-017) and the jobs view (D-029), amended the `.link` rule (D-002) and paused D-019.
- **Sources:** in-20260930-1045
- **Changed:** [2.7.4]; [2.20], [11.2], [14.4], [15.5], [16.4] renamed; new [10.8.3], [10.9.3], [19.2.2], [19.3.1], [19.4.1], [19.5.1], [19.6.1], [19.12.3], [19.13.3], [21.2.2], [21.3.1], [21.4.1], [21.5.1], [21.6.1], [21.12.3], [21.13.3]; [10.1.3], [10.1.4], [21.1.3], [21.1.4] retired; [11.12] merged into [11.2]; `check-links` in [14.1]; [40].
- **Rules now in:** conventions.md `conv-content-folders`, `conv-link-names`, `conv-no-claude-links`.

### D-031: A links file for every agent, and relink
<!-- k: id=d-031 applies=name:*.links.json,name:relink.system.link.js,[14.1],[16.1] sources=in-20260930-1153 status=decided -->
- **Decision:** Every agent layer has its own links file `configs/[name].links.json` saying what is linked from where: the system, its own domain or strategy, another domain, or any other agent by its unique name. One shared `relink` script builds every link from these files plus the child links, removes links nobody lists and checks them. It runs when a links file changes, at review time, and when an agent edits its own links file. The format and the triggers are our proposal.
- **Date:** 2026-09-30
- **Why:** the owner: a strategy agent may need data "from another agent or from domain or from another domain", and a script should relink the project whenever such a config changes.
- **Status:** active. It replaced the `links` section of the agent config and link building in `init.sh` (D-020's file-link rules stay).
- **Sources:** in-20260930-1153
- **Changed:** new [11.13], [19.2.3], [21.2.3]; [27.3] became its own file; `relink` in [14.1]; relink links [19.3.2], [21.3.2], [30.3]; `links.index.json` in [16.1]; [2.7.5]; [2.11.9]; [10.6] installs the git hooks; [40].
- **Rules now in:** conventions.md `conv-links-file`, `conv-relink-only`, `conv-git-hooks`; data-schemas.md `schema-links-file`; common/shared-mechanics.md `common-mech-relink-when`.

### D-032: Variant names start with their strategy
<!-- k: id=d-032 applies=[21],[23],[21.1.1.1],[2.18.1] sources=in-20260930-1453-2,in-20260930-1208 status=decided -->
- **Decision:** A variant's name starts with its strategy: `[strategy-id].[own-name]-v[N].[platform-model]-[test|live]`, e.g. `pm-strategy-1.momentum-v1.opus55-test`. The strategy agent's ID also carries its main platform/model and its mode, e.g. `pm-strategy-1-agent.opus55-test`. The strategy agent, through its SI sub-agent [21.1.1.1], creates modifications of itself as new test variants, compares them and folds a winning change back into the strategy. The rule is the owner's; the exact format is our proposal.
- **Date:** 2026-09-30 (owner's saved draft on the File Tree page)
- **Why:** the strategy is readable from every variant's name and all its variants sort together; the strategy improves itself through its variants.
- **Status:** active. Open: does `v[N]` belong to the variant or to the strategy? Should the strategy folder carry the suffixes too?
- **Sources:** in-20260930-1453-2, in-20260930-1208
- **Changed:** naming in [2.7]; [21]; [23] renamed from `pm-momentum-v1-agent-opus55-test`; [27.2], [27.3], [27.4], [21.6.1.1], [11.13].
- **Rules now in:** conventions.md `conv-variant-names`, `conv-strategy-agent-ids`, `conv-clones`; common/self-improvement-templates.md `common-si-variant-loop`.

### D-033: One knowledge agent keeps a layered knowledge base
<!-- k: id=d-033 applies=[2],[2.1],[2.10],[2.18.8],[10.1.1.2],[10.1.2.1],[10.1.2.2],[14.1],[11.10] sources=in-20260930-1533,in-20260930-1603,in-20260930-1841 status=decided -->
- **Decision:** Every owner input (project chat, a thread, the File Tree page), every answer Claude gives to the owner's questions, and every change to the system goes through one knowledge agent, `sys-knowledge-agent` [10.1.1.2] (was `sys-docs-agent`). With its skills `knowledge-intake` [10.1.2.1] and `knowledge-summarise` [10.1.2.2] it stores the input word for word, puts each piece of knowledge in the one doc that owns it, updates everything that states the same thing, records decisions and history, and refreshes the "How it works" summary of every file and folder, bottom up. A knowledge map [2.18.8] links each doc section to the files and folders it applies to (many to many). Each summary can carry "Always keep in mind" lines. Decisions, concepts and rules are no longer separate lists on the page: their content lives in the topic docs, and this file is history.
- **Date:** 2026-09-30
- **Why:** the owner wants the knowledge of the whole system summarised per file and folder and always current, without maintaining separate lists by hand, and nothing said in chat should get lost.
- **Status:** active. The layers, tag format and summary rules are our proposal.
- **Sources:** in-20260930-1533, in-20260930-1603 (keep in mind), in-20260930-1841 (answers are knowledge)
- **Changed:** docs moved into layers ([2.1] README, [2.10] inputs, [2.21] architecture, [2.18.7] to [2.18.9] index files, how-to [2.11.6] to [2.11.10]); [10.1.1.2] renamed; [10.1.2.1], [10.1.2.2] added; `build-map` in [14.1]; job `knowledge-sync` in [11.10]; the File Tree page shows How it works first and saves every message with its answer.
- **Rules now in:** README.md (layers, tag format, the flow); how-to/process-an-input.md; the two skills.

### D-034: Docs for people live in .claude/docs, one skill per doc
<!-- k: id=d-034 applies=[2],[10.1.1.2],[10.1.2] sources=in-20261001-0800,in-20261001-0845 status=decided -->
- **Decision:** The docs are for people: plain, book-like, readable by a non-technical person, with no reference numbers, ids or decision codes; relations, decisions and sources are kept only in the agent's own notes (in-20261001-0800). Layout set by the owner: `.claude/agents/knowledge-base-agent.md` (the knowledge agent, renamed from `sys-knowledge-agent`), `.claude/docs/` with README.md (everything we know, regenerated after every update), file-tree.md, vision.md, architecture.md, glossary.md and more, plus subagents links to the children's docs; one skill per doc, starting with vision. Order: agent and vision skill for the owner to check, then vision.md, then the other docs one by one, file tree and mapping last; every round improves the agent and the skills. Every level has the same docs with its own specifics.
- **Date:** 2026-10-01
- **Why:** the D-033 docs and page summaries were full of reference numbers and too technical for the owner to read.
- **Status:** partly superseded by D-047 (the docs for people moved from the system's `.claude/docs/` up into its `docs/`); the rest active. Proposed by us, waiting for the owner: the agent's notes in `.claude/knowledge/`; skill folder names `[doc]-doc`; `subagents.link/` inside `docs/`; planning copy at `vision/.claude/`.
- **Sources:** in-20261001-0800, in-20261001-0845, in-20261001-0908 (no references to other docs, no attribution or history: facts as they are now)
- **Changed:** `vision/.claude/agents/knowledge-base-agent.md` (new; old agent archived), `vision/.claude/skills/vision-doc/SKILL.md` (new), knowledge-intake and knowledge-summarise moved to `vision/.claude/skills/`. Docs, summaries and the file tree follow in later rounds.

### D-035: Answers on the vision: runs, approvals, first strategy, scope of actions
<!-- k: id=d-035 applies=[0],[2.2],[10.1.1],[11.1],[11.10],[14.1],[14.2],[19],[21],[21.1.1.1],[23],[45],[47] sources=in-20261001-1037 status=decided -->
- **Decision:** (1) At the end of every run an agent compresses or summarises what matters and clears what it no longer needs; it decides itself whether to keep or renew its session and whether to subscribe to more data, research or ask for a worker. (2) Runs also fire on agent-set triggers, e.g. when research it started is finished; that run gets all subscribed data plus the research. (3) A limit on parallel runs set from the server's capacity, by a system helper that checks the server (the owner said "probably": direction decided, details open). (4) Strategies can be code, AI or a mix. (5) Every strategy may have its own back-testing approach and settings (e.g. a month of old data replayed as live). (6) Protection against instructions hidden in outside text is built with live trading. (7) Agents subscribe to other agents' data; urgent data interrupts a run (a risk agent telling everyone to sell; a news worker on X posts). (8) Agents ask a workers agent for data: it knows existing workers, reuses or extends one, or creates one, and tells the agent how to use the data. (9) First strategy: one Polymarket strategy given by the owner, run the wheel, more after a good flow. (10) Real money after an agent and strategy show good results. (11) Start scale: system, domain and strategy agents plus 2-3 variants. (12) Venues and accounts chosen per strategy while it is built. (13) Workers and data from the existing Polymarket suite are reused across strategies. (14) Runs on one of the owner's servers, easy to move to a bigger one. (15) Every new strategy configuration needs a report and the owner's approval before it starts. (16) Self-improvement may change anything; agents may create workers and helpers freely for now. (17) Every action supports test and live from the start; on blockchains test can use testnets. (18) For now actions only on blockchains (any network and app); centralised exchanges and other apps are data-only. (19) Shared scripts for CRUD and filtering of the JSON lists, for agents.
- **Date:** 2026-10-01
- **Why:** the owner's comments and answers on the first people vision.
- **Status:** active. Still open: success metrics, AI budget, first live capital limits, notification channel, live keys; and the four ideas explained as problem and solution (bookmark, executor, ledger, digest).
- **Sources:** in-20261001-1037
- **Changed:** `.claude/docs/vision.md`; notes vision.md entries (ideas and questions); agent rule "Problem first"; vision skill.

### D-036: Every file's page: Example is its structure, How it works answers fixed questions
<!-- k: id=d-036 applies=[2.2],[2.13],[10.1.1.2],[10.1.2.2],[10.1.2.3] sources=in-20261005-0710 status=decided -->
- **Decision:** On the File Tree page, a file's Example shows the structure of the file and what goes in each section (for a doc, the Outline in its skill). How it works shows only short, plain answers under fixed headings for a newcomer: What it is, Who looks after it (agent and skill), When and how it changes, Who uses it and when, Where it is mentioned, Related knowledge, Keep in mind. Questions and File stay as they are. In edit mode long lines wrap to the screen. vision.md is the first file in this format; the rule is in the knowledge base agent, the vision skill and the summary skill for every file that follows.
- **Date:** 2026-10-05
- **Why:** the How it works tab mixed technical knowledge entries and notes; a newcomer could not see quickly what a file is, who keeps it and how it fits.
- **Status:** active. The heading names and the "Keep in mind" heading are our wording of the owner's list.
- **Sources:** in-20261005-0710
- **Changed:** `.claude/agents/knowledge-base-agent.md`, `.claude/skills/vision-doc/SKILL.md`, `.claude/skills/knowledge-summarise/SKILL.md`, summaries.json `sections` for [2.2], file-tree.md [2.2], tools (build_map, enrich), page v20.

### D-037: The README for people, built the same way as the vision
<!-- k: id=d-037 applies=[1],[2.1],[10.1.1.2],[10.1.2],[10.1.2.4] sources=in-20261005-0735 status=decided -->
- **Decision:** `README.md` is built the same way as `vision.md`: its own skill `readme-doc` with an Outline (shown as the README's Example on the File Tree page) and an "Its page on the File Tree" section, the doc written in plain language from every input, decision and what exists, and its How it works under the fixed headings (D-036). The README holds everything we know at overview depth and is rebuilt last in every round, with "Where things stand", "What comes next" and "Open questions" checked each time.
- **Date:** 2026-10-05
- **Why:** the owner accepted the vision page format and asked for the README next, in the order of D-034.
- **Status:** partly superseded by D-048 (the README's job and outline: every part exactly with paths, the why and business moved to the vision); the rest active. Proposed by us, waiting for the owner: the seventeen-section outline and lengths; the README skill also keeps the root front page [1] in line with "In short"; the earlier knowledge base guide (old [2.1]) is now the agent's notes guide (`vision/docs/README.md`, later `.claude/knowledge/`).
- **Sources:** in-20261005-0735
- **Changed:** `.claude/skills/readme-doc/SKILL.md` (new), `.claude/docs/README.md` (new), `.claude/knowledge/sources/readme.md` (new), `.claude/agents/knowledge-base-agent.md` (docs table, folder, step 5, skills), vision-doc step 6, knowledge-intake intro; file-tree.md [2.1] rewritten, [10.1.2.4] added; summaries for [2.1] (fixed headings), [10.1.2.4], [10.1.2], [10.1.1.2], [10.1], [2]; tools (enrich mappings); page data v17.

### D-038: Markdown files open as a readable page, white or black
<!-- k: id=d-038 applies=[2.13] sources=in-20261005-0908 status=decided -->
- **Decision:** On the File Tree page, a Markdown file's File tab opens in a Read view: the file rendered as a page made for long reading (a text face for the body, the page's condensed face for headings, about 68 characters per line, real lists, tables and code blocks, a properties box for a skill's header), with its own white or black paper chosen in the view and remembered per viewer. It shows the word count and reading time, a contents list, and a full-screen mode with a contents sidebar, reading progress and Esc to close. Source shows the raw lines with line numbers and line comments as before; Edit works from both.
- **Date:** 2026-10-05
- **Why:** the File tab showed Markdown as raw source lines, which is hard to read for long docs such as the README and the vision.
- **Status:** active. The design (faces, sizes, colours, full-screen layout) is ours.
- **Sources:** in-20261005-0908
- **Changed:** page (Read/Source switch, reader, full screen), `.claude/docs/README.md` (the File tab line), tools/README.md, memory.
- **Amended (2026-10-05, in-20261005-0925):** the serif body face was hard to read. The body is now a clean sans (Inter) by default, and an Aa menu in the view picks the face (Sans, Legible, Serif) and the size (S, M, L), remembered per viewer. The faces are our choice.

### D-039: How it works in its own Markdown file, for every file and folder
<!-- k: id=d-039 applies=[10.1.2.2],[10.1.1.2],[2.13] sources=in-20261005-0925 status=decided -->
- **Decision:** The How it works of every file and folder is kept in a Markdown file of its own: `{file name}.index.md` next to a file (the full name is kept, so `run.js` and `run.py` never share one) and `{folder name}/{folder name}.index.md` inside a folder. It replaces `docs/index/summaries.json`. The File Tree page shows it on How it works and edits it like the File tab; the edit waits on the page and is written into the file at the next sync. A skill, `file-index` (replacing `knowledge-summarise`), says how to write and keep these files. The tools and the notes read and write them.
- **Date:** 2026-10-05
- **Why:** the owner wants How it works as files anyone can open and edit, next to what they describe, one for every file and folder.
- **Status:** active. Ours: the file names keep the full file name with its extension; the front matter (about, node, basis, written, by, confirmed); the six headings or one Summary heading until a file's doc is rebuilt; while we plan, files that exist as drafts (the people docs, the agent, the skills) keep theirs next to the draft (owner, 2026-10-05 10:24, in-20261005-1024) and the rest sit in a mirror of the planned tree, `vision/tree/trading-os/...`; an index file has no index file of its own; scripts that list a folder skip them (proposed).
- **Sources:** in-20261005-0925
- **Changed:** `tools/index_files.py` (new), `build_map.py` (reads and writes the files; `--orphans`), `enrich.py` (`how_md`, `how_file`), 317 index files written from `summaries.json` (archived in `vision/archive/2026-10-05/`), file-tree.md v1.17 (new pattern node [51], [2.18.9] retired, [10.1.2.2] renamed), notes (README, data-schemas, architecture, flows, glossary, feature-map, workers, subagents, roadmap, how-to), `.claude/skills/file-index/SKILL.md` (new; knowledge-summarise archived), the agent, knowledge-intake, vision-doc and readme-doc skills, `.claude/docs/README.md`, page (How it works from the file, Edit).

### D-040: The planning project is the owner's window on the project; working from two places through GitHub
<!-- k: id=d-040 applies=[0],[2.1],[2.2],[10.1.1.2] sources=in-20261005-0925 status=decided -->
- **Decision:** The planning project (the File Tree page, the docs, the How it works files and the knowledge behind them) is the owner's personal tool for vibecoding: to understand the project, watch it change, steer it and analyse how the system is doing, while it is planned and later while it is built and run. The owner wants it kept in the GitHub repository so the cloud project and a Claude Code on the owner's server both work on it and both know the full context.
- **Date:** 2026-10-05
- **Why:** the owner builds the system with AI and needs one place to see and steer it, and wants to keep working on the plan from their own server too.
- **Status:** the purpose and the wish to sync through GitHub are decided. How it works is proposed (`vision/plans/github-sync.md`): the repository as the one source; the planning folder as `planning/` with its own `CLAUDE.md`; the cloud thread pushes to its branch with a pull request into `main`; the server works on `main`; pull before and push after every round; generated files rebuilt, never merged; working notes moved from the project memory into `planning/.claude/memory/`. Waiting for the owner: the go-ahead to push, who merges, and the server setup. The `planning/` folder of this plan is replaced by the owner's layout (D-041).
- **Sources:** in-20261005-0925
- **Changed:** `.claude/docs/README.md` (the owner's window; the plan moving into the repository, as an idea), `.claude/docs/vision.md` (What the owner sees and does), the agent ("Your job"), the root How it works, `vision/CLAUDE.md` (new, draft), `vision/plans/github-sync.md` (new), `vision/explorer/` (the page source, copied out of a session scratchpad), `vision/.claude/memory/` (snapshot of the project memory).

### D-041: The repository is the file tree, with the owner's IDE in project-IDE/
<!-- k: id=d-041 applies=[0],[1],[10.1.5],[53],[10.9],[19.13],[2],[10.1],[10.1.1.3],[10.1.2.5],[10.1.2.6],[2.6],[2.9],[2.10],[2.13],[2.18.8] sources=in-20261005-1041,in-20261005-1043,in-20261005-1254 status=decided -->
- **Decision:** The GitHub repository is laid out as the file tree: `CLAUDE.md` and `README.md` at the root; `project-IDE/` with `current-ui/` (the File Tree page the owner uses now) and `data/` (the data the page needs and this project's knowledge: inputs, decisions, changelog, the tree notes, the knowledge map, the notes behind each people doc, the owner's page edits, working notes, plans, archive); `researches/`; `agents/` exactly as the tree is now, which the owner agreed as it stands ("all should be already all confirmed"); `apps/`; `trading-ui/` for the later trading dashboard. The IDE's logic lives in `agents/system/.claude/`: a new project IDE agent (builds the page from the repository, turns the owner's page notes and edits into file changes, metadata and views, runs page requests) with the skills `ide-build` (its scripts inside it) and `ide-sync`, next to the knowledge base agent and its skills; the docs for people are in `agents/system/.claude/docs/`. Every file and folder gets its `.index.md`; a file nobody has written yet exists only as its index file. Next the owner gives the GitHub project and the current tree is synced into it.
- **Date:** 2026-10-05
- **Why:** one repository both sides can work on (the cloud project and the owner's server), and the owner's IDE in a place of its own that anyone can find and rebuild.
- **Status:** partly superseded by D-047 (the docs for people moved from the system's `.claude/docs/` up into its `docs/`); the rest active. Ours, accepted with the layout: the agent and skill names, the build scripts inside `ide-build`, which records go to `project-IDE/data/` (the topic notes stay in `agents/system/docs/`), the first sync's mapping from the planning folder. Open questions inside single files stay open, and ideas inside the docs still marked proposed stay proposed. Waiting for the owner: the GitHub project; who merges; the server setup. The root `CLAUDE.md` and root `researches/` are replaced by D-045 (2026-10-06): `CLAUDE.md` lives in `agents/system/.claude/`, the studies in the agents' research folders, and `trading-ui/` in `apps/`.
- **Sources:** in-20261005-1041, in-20261005-1043, in-20261005-1254
- **Changed:** `file-tree.md` v1.18 (new [52], [53] subtree, [54] subtree, [10.1.1.3], [10.1.2.5] with [10.1.2.5.1], [10.1.2.5.2] and seven scripts, [10.1.2.6], [10.1.14]; [2.1], [2.2] into [10.1.14]; [2.6], [2.9], [2.10], [2.13], [2.18.8] into [53.2]; the 19 proposed items agreed; `build-map` out of [14.1]); `enrich.py` (an item is decided unless marked proposed); `.claude/agents/project-ide-agent.md`, `.claude/skills/ide-build/SKILL.md`, `.claude/skills/ide-sync/SKILL.md`, `tools/check_page.js` (new); the knowledge base agent, knowledge-intake, file-index, readme-doc, vision-doc; `.claude/docs/README.md`, `.claude/docs/vision.md`; `CLAUDE.md` (for the repository root); `plans/github-sync.md` (the layout decided; the first sync's mapping); `tools/README.md`, `docs/README.md`; the page data v22.

### D-042: The page on the owner's server, with Claude Code behind its request box
<!-- k: id=d-042 applies=[53],[53.3],[53.1.1],[10.1.1.3] sources=in-20261005-1433,in-20261005-1452 status=decided -->
- **Decision:** The owner wants the File Tree page on their own server too, with the ability to run an AI agent from it that sends requests to Claude Code working in the Trading OS repository ("i would love to have on a server also ability to run ai agent that can send request to claude code connected to this trading os project").
- **Date:** 2026-10-05
- **Why:** on claude.ai the page cannot reach the agents, so the owner's notes wait for a sync; on the server the page can work with Claude Code directly, and served elsewhere the page is only view only today.
- **Status:** the wish is decided. How it works is proposed (`vision/plans/server-ide.md`): one page file for both homes; a small service in `project-IDE/server/` that serves the page from the repository, saves page edits into the files and runs each request as a Claude Code session in the repository through the Claude Agent SDK; reachable only from the machine or a private network; push, delete and anything outside the repository only on the owner's click. Waiting for the owner: agreement on the design, and the GitHub sync, since the server works from a clone of the repository.
- **Sources:** in-20261005-1433, in-20261005-1452
- **Changed:** `file-tree.md` v1.19 (new proposed [53.3] with [53.3.1]–[53.3.4]; [53], [53.1.1], [53.2.5], [10.1.1.3]); `plans/server-ide.md` (new); `plans/github-sync.md`; `.claude/docs/README.md`; the page data.

### D-043: The project IDE is one of the apps; on the server Claude Code runs from the system folder
<!-- k: id=d-043 applies=[43],[53],[53.3],[53.3.1],[53.3.2],[53.3.3],[53.3.4],[53.2.7],[10.1.1.3],[10.1.2.6] sources=in-20261005-1517 status=decided -->
- **Decision:** `project-IDE/` moves into `apps/` (`apps/project-IDE/`), so `apps/` holds our own applications as well as cloned repositories. On the owner's server, Claude Code behind the page's request box starts in the system folder `agents/system/`, so the system's agents and skills load as its own and the root `CLAUDE.md` loads as its parent's. The owner asked to see the code: the four files of `apps/project-IDE/server/` are written, with the page's store kept as files in `apps/project-IDE/data/page-store/`.
- **Date:** 2026-10-05
- **Why:** the IDE is an application like the others; Claude Code finds agents and skills only in the `.claude/` folder where it starts and above, never below, and ours live in `agents/system/.claude/`.
- **Status:** active. The move and the start folder are the owner's words; the server's design (D-042) is taken as agreed with them, and the settings (port, allow list, the steps that wait for the owner's click, the 15-minute limit on a question, write-through on) are our defaults the owner can change. Tested on a copy of the repository: the page in server mode, the store as files, write-through, a real Claude Code request that listed the system's two agents and six skills, and the owner's Allow and Refuse. Goes live after the GitHub sync. Its note that the root `CLAUDE.md` loads as the parent's is replaced by D-045: there is no root `CLAUDE.md`, and the system's own loads because Claude Code starts in `agents/system/`.
- **Sources:** in-20261005-1517
- **Changed:** `file-tree.md` v1.20 ([53] subtree under [43]; [43] purpose; [53.3] and its files decided, with drafts; new [53.2.7] `page-store/`); the mirror index files moved under `tree/trading-os/apps/`; `vision/server/` (new: `server.py`, `claude_bridge.py`, `server.config.json`, `README.md`); the page (server mode: store, write-through, requests with steps, questions and cost; data reload); `enrich.py` (the server files on the File tab); the project IDE agent, ide-sync, ide-build, knowledge-intake, the knowledge base agent; `CLAUDE.md`, `.claude/docs/README.md`, `plans/github-sync.md`, `plans/server-ide.md`, `tools/README.md`, `docs/README.md`.

### D-044: Delete on the page cleans the project; one status, "changed", for now
<!-- k: id=d-044 applies=[53.1.1],[53.3],[53.3.2],[53.3.3],[53.3.4],[10.1.2.6],[10.1.1.3] sources=in-20261005-1545 status=decided -->
- **Decision:** every file and folder on the File Tree page except the top has a Delete button, with an optional note for Claude about what to keep in mind. Deleting runs the agent: on the owner's server Claude Code deletes the item and its How it works file at once, with no second click for exactly that, then cleans the project of it (its line and section in the tree notes, links, mentions in other files, the parent's How it works, the knowledge map), following the note, files it and commits; on claude.ai the item is marked deleted at once and cleaned up at the next sync. A deleted item stays in the tree, struck through, until the sync, and can be brought back the same way. The page shows no statuses for now: exists, decided, proposed, name pattern and example agent are gone from it. The one status is "changed", set on whatever a request from the page touched (an edit, a note, an added or deleted item, a request in the box, and on the server every file Claude Code changed for a request) until the next sync. More statuses may come later.
- **Date:** 2026-10-05
- **Why:** the owner's words: a deletion should leave nothing behind that points to the item, and the statuses are not needed for now.
- **Status:** active. The button, the agent cleaning up, the optional note and the single "changed" status are the owner's words; the details are our defaults: folders count what is inside, the struck-through row until the sync, "Bring it back", the one delete command that needs no click, the marks cleared at the sync. The tree notes keep decided and proposed on each item for the agents; only the page stops showing them. Tested on a copy of the repository: a real delete with a note (the two start commands moved first, as the note asked; the file and its How it works file deleted with no second click; committed) and a bring-back; and on the claude.ai page with a stand-in store. Two server fixes found while testing: saving an item again could have written an older page edit over a file Claude Code had changed since, and the page missed files Claude Code had already committed.
- **Sources:** in-20261005-1545
- **Changed:** `file-tree.md` v1.21 ([53.1.1], [53.3.2], [53.3.3], [10.1.2.6]); the page (version 34); `vision/server/` (`claude_bridge.py`, `server.py`, `server.config.json`, `README.md`); the ide-sync skill ("Deleting an item", "The changed mark"); the project IDE agent; changelog.

### D-045: The tree lists only real files; no root CLAUDE.md or researches/; trading-ui inside apps/
<!-- k: id=d-045 applies=[0],[1],[10.1],[10.1.5],[10.9],[19.13],[43],[45],[54.1],[54.2],[54.3] sources=in-20261006-1007,in-20261006-1009,in-20261006-1011,in-20261006-1013,in-20261006-1016 status=decided -->
- **Decision:** the owner deleted five items on the File Tree page, each with a note. The tree shows only files and folders that will really be in the system, not examples of names: the `[name].index.md` pattern [51] and the system's `[subagent-name].md` template leave the tree (the rule that every file and folder has its How it works file stays, D-039). There is no root `CLAUDE.md` [52]: the file every Claude reads first is the system's `agents/system/.claude/CLAUDE.md` [10.1.5], which takes over its job next to the system manager prompt. There is no root `researches/` [54]: research lives inside the agents, so the prediction-market studies [54.1] go to the prediction-market domain's `research/` [19.13], and the self-improving-agents [54.2] and trading-agent architecture [54.3] studies to the system's `research/` [10.9], keeping their numbers. The example cloned repo [44] goes; `apps/` [43] holds our own apps and cloned projects, and `trading-ui/` [45] moves into it as `apps/trading-ui/`, empty for now and maybe never needed if the project IDE does its job.
- **Date:** 2026-10-06
- **Why:** the owner's words: the examples were only there to show what kind of thing goes where; CLAUDE.md is kept inside `.claude/`; research folders are inside the agents.
- **Status:** active. The deletions, the CLAUDE.md place, research inside the agents and trading-ui in apps/ are the owner's words. Our defaults: which research folder each study goes to, keeping the numbers [54.1]–[54.3], and the same patterns at the domain, strategy and variant levels staying until the owner says otherwise. This replaces D-041's root `CLAUDE.md` and root `researches/`, and D-043's note that the root `CLAUDE.md` loads as the parent's. Claude Code started at the top of the repository does not load the system's `CLAUDE.md` on its own (tested 2026-10-06: started in `agents/system/` it does). The repository's own `researches/` moves at the GitHub sync.
- **Sources:** in-20261006-1007, in-20261006-1009, in-20261006-1011, in-20261006-1013, in-20261006-1016
- **Changed:** `file-tree.md` v1.22 ([51], [52], [54], [44] retired; [10.1.5] section; [54.1]–[54.3] moved; [45] moved into [43]; [0], [1], [2], [10], [10.1], [43], [53], [53.3], [53.3.3]); the CLAUDE.md draft moved to `vision/.claude/CLAUDE.md`; the mirror How it works files moved or archived (`vision/archive/2026-10-06/`); `index_files.py`; `architecture.md`, `overview.md`, `conventions.md`, `feature-map.md`, `flows.md`, `roadmap.md`, `index/subagents.md` and the knowledge tags naming [51] or [44]; `plans/github-sync.md`, `plans/server-ide.md`; `claude_bridge.py` and the server README; the project IDE agent, ide-build; `.claude/docs/README.md`; memory.

### D-046: An Apply changes button applies the page's changes and shows the new tree
<!-- k: id=d-046 applies=[53.1.1],[10.1.2.6],[10.1.1.3],[53.3] sources=in-20261006-1017 status=decided -->
- **Decision:** the File Tree page has an Apply changes button at the top, with the number of items marked changed. Pressing it carries every change waiting on the page into the files and shows the new tree. On claude.ai it posts one comment on the page and sends it to Claude, which runs ide-sync and ide-build, publishes the new tree, answers the comment and resolves it; the request is also saved in the page's store, and when it turns processed the open page loads the new tree or asks the owner to reload. When no Claude is watching the page, it keeps the request and asks the owner to say "sync the file tree" in the project chat. On the owner's server it starts one Claude Code run with the same request.
- **Date:** 2026-10-06
- **Why:** the owner's words: deleted items stay marked changed on the page, and they need a button at the top that applies the changes so the new file tree shows.
- **Status:** active. The button and what it does are the owner's words; how it reaches Claude (a comment sent to Claude through the page's `comments` capability, the first time with the owner's consent), the saved request, the count and the reload are our defaults.
- **Sources:** in-20261006-1017
- **Changed:** `file-tree.md` v1.22 ([53.1.1], [10.1.2.6]); the page (version 35, with the `comments` capability); ide-sync ("Started by Apply changes"; inputs of kind `apply`); the project IDE agent; the system `CLAUDE.md` draft; the server README.

### D-047: An agent keeps no docs inside .claude/; .claude/docs/ moves up into the agent's own docs/
<!-- k: id=d-047 applies=[2],[2.1],[2.2],[10.1] sources=in-20261006-1140,in-20261006-1144 status=decided -->
- **Decision:** no agent keeps a `docs/` folder inside its `.claude/`. Where one exists, it moves one level up into the same agent's own `docs/`. Only the system had one: its README [2.1] and vision [2.2] now sit in `agents/system/docs/` [2], next to the topic notes agents read, and [10.1.14] is retired. The domain, strategy and trading agent `docs/` folders ([19.6], [21.6], [46]) stay where they are; a level's docs for people go there when they are written.
- **Date:** 2026-10-06
- **Why:** the owner's words at 11:40: "we don't keep docs folder in a agent folders should be in a common root agent level". We asked on a card which folders move; the owner tapped "All in system" at 11:43, then a minute later narrowed it: "just .claude/docs/  move in a level up docs in every agent who has .claude". The later message decides, so the card choice (every agent's docs into the system) is not carried out.
- **Status:** active. Partly supersedes D-034 and D-041 on where the docs for people live (they were in the system's `.claude/docs/`). The planning drafts keep their place in `vision/.claude/docs/` until the GitHub sync, which copies them to `agents/system/docs/`. Proposed, for the owner later: when a doc for people is written on a topic whose agent notes already use that name in [2] (architecture, glossary), the notes move to the sources [53.2.2].
- **Sources:** in-20261006-1140, in-20261006-1144
- **Changed:** `file-tree.md` v1.24 (the tree, [1], [2], [2.1], [2.2], [2.13], [10.1], [10.1.14] retired, [53.2]); the system `CLAUDE.md` draft; the knowledge base agent; knowledge-intake; the people README (the agent folder); the knowledge guide; `plans/github-sync.md`; `index_files.py`; the sources files; How it works files; the page (version 37).

### D-048: The vision on top, the README as the exact map of every part, and a rebuild prompt for AI
<!-- k: id=d-048 applies=[2],[2.1],[2.2],[2.22],[10.1.2.3],[10.1.2.4],[10.1.2.7],[10.1.1.2],[10.1.5],[19.6],[21.6] sources=in-20261006-1243,in-20261006-1259 status=decided -->
- **Decision:** the three main docs each get one job. The vision [2.2] is the top-level doc, read first, mostly for people and for every agent's high-level view: what we are building and why, the concept, ideas, how it should work, the business logic and examples; from it the reader goes deeper. The README [2.1] is the full, long, exact overview of how the whole system works, for people and AI: a descriptive view of every main part with the path to that part's own docs, and nothing about the logic inside agents. A new third doc [2.22] is a prompt from which an AI can rebuild the system and end with the same working system, with its own skill [10.1.2.7]. The vision and README skills are rewritten to match.
- **Date:** 2026-10-06
- **Why:** the owner was confused about how the vision and the README differ (12:43); every vision section was repeated in the README. On the card they chose "Sharpen both" (12:53), then said what each doc is for and asked for the third doc (12:59).
- **Status:** active. The jobs of the three docs and the third doc are the owner's words. Ours, as defaults: the name `rebuild-prompt.md` and its place in `agents/system/docs/`, the skill name `rebuild-prompt-doc`, the outlines and lengths, the order every round (vision, README, rebuild prompt last), the two places the people docs now point onward (the vision's last section, the README's "Its docs" lines), and listing a README and a vision in the domain and strategy `docs/` folders so the README has real paths to point at. Open questions about goals and business stay in the vision; design details still open move to the README.
- **Sources:** in-20261006-1243, in-20261006-1259
- **Changed:** `file-tree.md` v1.25 ([2], [2.1], [2.2], new [2.22], [10.1.2.3], [10.1.2.4], new [10.1.2.7], [10.1.1.2], [19], [21], new [19.6.2], [19.6.3], [21.6.2], [21.6.3]); the vision, README and new rebuild-prompt skills; the knowledge base agent (the docs, the order, where the docs live, the two onward pointers); the system `CLAUDE.md` draft (read the vision first); `vision.md`, `README.md` and `rebuild-prompt.md` rewritten or written; the sources files; How it works files; the page.

### D-049: The IDE and the docs give the owner and every AI the whole context
<!-- k: id=d-049 applies=[0],[2],[2.1],[2.2],[2.22],[10.1.1.2],[10.1.1.3],[10.1.2.1],[10.1.5],[53] sources=in-20261006-2047 status=decided -->
- **Decision:** the custom IDE, the File Tree page and the docs exist so the owner can easily manage, analyse and view the system, and so AI always has all the related context it needs to make changes precisely. The docs must be right for developers and for AI. When a file changes, the AI knows which related files, agents, skills, docs, indexes and logic it has to update, and how. An AI working on a file deep in the hierarchy, such as a helper's skill, knows the knowledge from the levels above that applies to it. New knowledge from every session and every owner input is spread to where it belongs, and every question the owner asks finds its place in the docs, with an explanation of how exactly that thing works.
- **Date:** 2026-10-06
- **Why:** the owner's statement of what the whole IDE and file tree work is for (20:47).
- **Status:** active. The purpose and the five requirements are the owner's words. Ours: today the context of any item comes from `build_map.py --context` (its section, the knowledge that applies directly and from every folder above, its children), now named in `CLAUDE.md` as the step before any change; the ripple step of knowledge-intake now walks the related agents, skills, scripts, index lists and How it works files; a session's findings are filed even when no file changed; every answered question is written into the place the owner should have found it. Proposed, waiting for the owner's go on the file set (`vision/plans/file-set.md`): each file's Details file lists what must change with it and how (`update_with`) and what it inherits from above (`inherits`), shown on the page.
- **Sources:** in-20261006-2047
- **Changed:** `vision.md` (What the owner sees and does; a new principle), `README.md` (the knowledge base and the docs; the project IDE), `rebuild-prompt.md` (whole context for every change; the knowledge base agent; Do not build lists the file set), the knowledge base agent (job, when it runs, step 2), the project IDE agent (job), knowledge-intake (scope, questions, ripple step 5), the system `CLAUDE.md` draft (what the project is for, before you touch a file, rules), `vision/plans/file-set.md` (what it is for; Details fields), `file-tree.md` v1.26 ([10.1.1.2], [10.1.2.1], [10.1.5], [53]), How it works files, the page.

### D-050: One job per code file; a Tests file for code, skills and agents
<!-- k: id=d-050 applies=[14],[30],[10.1.2.5],[10.1.2.5.2],[10.1.5],[2.1],[2.2],[2.22],name:*.js,name:*.py,name:*.sh sources=in-20261006-2104 status=decided -->
- **Decision:** every code file holds one runnable thing (a function, an endpoint, a script) with one purpose. It may take different parameters, but there are no common files that mix different things: related things go in a folder, one per file, each with its own metadata. Every code file, skill, agent and subagent also gets a tests metadata file in its family, shown in a Tests tab with its own view where the owner can run a test; other files have none for now.
- **Date:** 2026-10-06
- **Why:** the owner calls one job per file a common rule and wants it everywhere the docs and further work need it; tests should be visible and runnable from the page.
- **Status:** active for the rule, for all new code. Ours: it covers scripts, workers, decision scripts, hooks, page and server code and the IDE build scripts, and a shared helper is one function in its own file; the planning build scripts and the server code break it today and are split when the file set is applied (step 7 of the plan). The Tests file joins the file set and waits with it for the owner's go: name `x.tests.json`, its fields, test code staying in the level's `tests/` folder, the level's test list built from the Tests files, and Run going to the owner's server or, on claude.ai, to Claude as a request.
- **Sources:** in-20261006-2104
- **Changed:** `conventions.md` v0.2 (One job per code file), `common/common-prompt.md` v0.2 (rule), `common/self-improvement-templates.md` (base template), the system `CLAUDE.md` draft (rules), `vision.md` (principle "One file, one job"), `README.md` (How the project is laid out), `rebuild-prompt.md` (Ground rules: Code; Do not build), `vision/plans/file-set.md` (Tests, One job per code file, steps 6 and 7, where it goes once built), the knowledge base agent (where detail goes; plans), `file-tree.md` v1.27 ([14], [30], [10.1.2.5]), How it works files, the page.

### D-051: A plan for every change request; planning is the main development skill
<!-- k: id=d-051 applies=[10.1.2.8],[10.1.5],[53.2.5] sources=in-20261006-2143 status=decided -->
- **Decision:** every change request gets a plan before it is built, and the plan is stored. After the build, the logic in it is moved to where it belongs; later changes update the logic and knowledge in those files. Planning is a skill we define, keep and develop as the main way the system is developed.
- **Date:** 2026-10-06
- **Why:** the owner wants changes thought through and recorded before they are made, and their knowledge to end up in the right files.
- **Status:** active. Ours: the skill `change-plan` [10.1.2.8] (draft), plans named `YYYY-MM-DD-HHMM-<subject>.md` in `plans/` [53.2.5] with an index and an archive, the statuses, the plan outline, the steps and the exception for small fixes; the rule in the system `CLAUDE.md`. Older plans keep their names. The first plan written with it is `vision/plans/2026-10-06-2143-general-system.md`.
- **Sources:** in-20261006-2143
- **Changed:** `.claude/skills/change-plan/SKILL.md` (new), `.claude/CLAUDE.md` (every round, rules), `vision/plans/2026-10-06-2143-general-system.md` (new), `vision/plans/index.json` (new), `file-tree.md` v1.28 (new [10.1.2.8], [53.2.5]); the vision (the principle on the docs), the README (the knowledge base part) and the rebuild prompt (tree, skills, `CLAUDE.md`).

### D-052: Features as their own knowledge files, mapped both ways
<!-- k: id=d-052 applies=[2],[2.12],[19.6],[21.6] sources=in-20261006-2143 status=decided -->
- **Decision:** some features get their own knowledge file. Features are split out, each with a map to the files it relates to, and each file maps back to its features. Small features relate to and are included in bigger ones. A feature holds the logic too detailed for the overviews (How it works, views, the README, the rebuild prompt). They live in a folder in the docs, for the system and for agents.
- **Date:** 2026-10-06
- **Why:** detailed logic needs one home; overviews should stay short.
- **Status:** the direction is the owner's. How, proposed in `vision/plans/2026-10-06-2143-general-system.md` part 3 and waiting: `features/` in the `docs/` of the system and every agent, one feature per file, parents and children, the map written on the feature's side and built on the file's side, replacing the feature map table over time.
- **Sources:** in-20261006-2143
- **Changed:** `vision/plans/2026-10-06-2143-general-system.md`.

### D-053: The vision, README and rebuild prompt as one hierarchy across levels
<!-- k: id=d-053 applies=[2.1],[2.2],[2.22],[19.6],[19.6.4],[21.6],[21.6.4],[46],[46.3],[46.4],[10.1.2.3],[10.1.2.4],[10.1.2.7] sources=in-20261006-2143 status=decided -->
- **Decision:** the vision, the README and the rebuild prompt form a hierarchy: one comes from another, and they exist for the system in general and for every domain, strategy and agent. When a lower level's docs change, the documents above are updated up to the top.
- **Date:** 2026-10-06
- **Why:** the owner wants every level to explain itself and every change to reach the top docs.
- **Status:** the direction is the owner's. How, proposed in `vision/plans/2026-10-06-2143-general-system.md` part 4 and waiting: inside a level vision, then README, then rebuild prompt; a parent sums up each child with the path to its docs; a rebuild prompt at every level; the system's rebuild prompt lists the children's in build order; the climb rule in the three doc skills and the knowledge base agent.
- **Sources:** in-20261006-2143
- **Changed:** `vision/plans/2026-10-06-2143-general-system.md`; on the owner's question (2026-10-07 08:52, in-20261007-0852) the tree lists a rebuild prompt in every domain, strategy and trading agent's docs, and a vision for the trading agent (`file-tree.md` v1.30); the rebuild prompt skill, the README and the rebuild prompt say every level has one.

### D-054: A general system, not a trading OS
<!-- k: id=d-054 applies=[0],[2.1],[2.2],[2.22] sources=in-20261006-2143 status=decided -->
- **Decision:** the system is no longer called the Trading OS, and its top level and general knowledge know nothing about trading. Agents can be of any kind (trading, social media, management and more); each kind can share parts of the system and have its own, with its own levels below, but every agent has a parent. For trading domains the levels below are strategies and running agents.
- **Date:** 2026-10-06
- **Why:** the owner wants one system for agents of every kind, with trading as one of them.
- **Status:** decided; the docs and the tree still describe the Trading OS until the plan is built. Open: the new name (the owner chooses; "the system" until then); the repository keeps `trading-oss` until the owner renames it. Proposed in `vision/plans/2026-10-06-2143-general-system.md` part 5 and waiting: each kind as a folder level under `agents/` (`agents/trading/` holding what every trading domain shares), what stays general in the system and what moves to the trading kind, and the docs rewritten once, together with the docs hierarchy. Named the Agent OS on 2026-10-07, and trading goes into the prediction-market domain with no kind folder (D-056).
- **Sources:** in-20261006-2143
- **Changed:** `vision/plans/2026-10-06-2143-general-system.md`; the vision's next step 1 (the docs are rewritten for a general system); the How it works of the top folder (no longer called the Trading OS; the change is planned).

### D-055: Every app has its own docs; research clones go to a temp folder; apps we use are forked
<!-- k: id=d-055 applies=[43],[53],[53.4],[55],[48],[2.18.5] sources=in-20261006-2206 status=decided -->
- **Decision:** every app in `apps/` has its own docs. A repository cloned from GitHub for research goes into a temp folder first; on request it can still get a vision, a README and a rebuild prompt. An app we use is forked, with our own main branch; from time to time the source's updates are merged in, then into our main. For now an app's metadata is only these three docs. Later, on request, a skill turns an app fully into the system's way (Details for every file, one job per file, the other docs), and that skill is kept up like every other.
- **Date:** 2026-10-06
- **Why:** outside code needs a clear home: research clones should not weigh on the repository, the apps we use should stay ours and up to date, and every app should explain itself like the rest of the system.
- **Status:** active. Ours: every app's `docs/` holds `vision.md`, `README.md` and `rebuild-prompt.md` [53.4]; research clones in `apps/temp/<name>/` [55] with the clone in `repo/` (never committed) and docs in `docs/` only when asked; an app we use in `apps/<name>/` with `docs/` and our fork in `repo/`; in the fork `main` is ours and `upstream` follows the source; the list of apps [2.18.5] gets kind, source, fork, branches, commit, last update; skill name `adopt-app` proposed, not written. Open in `vision/plans/2026-10-06-2206-apps-docs-clones-forks.md`: submodule or ignored clone for `repo/` (submodule recommended), where forks live on GitHub, how often to update, when the project IDE's three docs are written (with the docs at every level, recommended).
- **Sources:** in-20261006-2206
- **Changed:** `vision/plans/2026-10-06-2206-apps-docs-clones-forks.md` (new); `vision/plans/index.json`; `conventions.md` v0.3 (Apps and outside code); `architecture.md` ([43] row and line); `file-tree.md` v1.29 ([43], [53], new [53.4] to [53.4.3], new [55], [48], [2.18.5]); the vision, README and rebuild prompt skills (an app's outline and length); the README (layout) and the rebuild prompt (tree, apps, do not build).

### D-056: The system is the Agent OS; trading lives in the prediction-market domain
<!-- k: id=d-056 applies=[0],[1],[2],[2.1],[2.2],[2.22],[4],[10],[19] sources=in-20261007-0904 status=decided -->
- **Decision:** the system is named the Agent OS (`agent-os`). Its top level knows nothing about trading: everything about trading moves down into the prediction-market domain, and a later trading domain is copied from it when needed. There is no folder for a kind of agent above the domains.
- **Date:** 2026-10-07
- **Why:** the owner wants one system for agents of any kind; trading is one domain, the first.
- **Status:** active. Ours: history keeps the old name (saved messages, past decisions, past changelog lines); the GitHub repository keeps `trading-oss` until the owner renames it there; a general rule stays at the system level with its trading layer moving down (for example test and live modes and the owner's approval stay general, money limits move); the planned copy-trading domain [42] leaves the tree, to be copied from the prediction-market domain when the owner asks. Settles the name left open in D-054 and the kinds choice of `vision/plans/2026-10-06-2143-general-system.md` (no kind folder). Plan: `vision/plans/2026-10-07-0904-agent-os.md`.
- **Sources:** in-20261007-0904
- **Changed:** `vision/plans/2026-10-07-0904-agent-os.md` (new); the name everywhere outside history; the tree's top folder `agent-os/`; the trading move (in progress).

### D-057: Metadata files are named without the file's extension; an empty metadata file for everything; a metadata switch on the page
<!-- k: id=d-057 applies=[53],[53.1.1],[10.1.2.2],[10.1.2.5] sources=in-20261007-0904 status=decided -->
- **Decision:** every metadata file is named after its file without the file's extension (`vision.index.md`, `vision.meta.json`), and every file and folder gets a metadata file, empty for now. The page's `.index.md` switch becomes a "metadata" switch that shows the metadata files too.
- **Date:** 2026-10-07
- **Why:** the owner wants clean names and every file to have its metadata file, filled in later.
- **Status:** active. Ours, from `vision/plans/file-set.md` (steps 1 and 2, the second with empty files): a folder's files sit inside it with the folder's name (`configs/configs.meta.json`); a name with no extension stays whole (`.gitignore.index.md`); a file whose name would be shared with a sibling or with its own folder keeps its extension (today only `apps/project-IDE/server/server.py`, inside the folder `server/`); the empty `.meta.json` lists the file-set plan's fields. The rest of the file-set plan (examples, questions, changes, tests and views as files) waits.
- **Sources:** in-20261007-0904
- **Changed:** every How it works file renamed; a `.meta.json` for every file and folder; the tools `index_files.py`, `enrich.py`; the page (switch and rows); the file-index skill.

### D-058: How trading moves down: what stays general, where the trading parts go
<!-- k: id=d-058 applies=[10],[11.1],[14],[14.3],[2.7],[2.8],[19],[19.2.4],[19.6],[45],[54.3] sources=in-20261007-0904,D-056 status=proposed -->
- **Decision:** the system level keeps only what holds for any agent: test and live modes for every outside action, the owner's approval to go live, a general stop switch, limits enforced in code that a lower level may only tighten, the key rules, outside text as data, the levels, a new version instead of a change to a running agent, self-improvement that never goes live, and cost, speed, error and test metrics. Everything about trading goes to the prediction-market domain: its own config file [19.2.4] (risk limits, trading accounts, venues, fees, market filters, the currency, the order stop switch, trade notifications), the shared buy, sell and risk scripts [14.3] (number kept), the Polymarket price collector with its logs and data, the `trading-` notes in its `docs/` [19.6], and the trading study [54.3] (number kept).
- **Date:** 2026-10-07
- **Why:** the owner's message: everything about trading goes "down to prediction market domain", and "another trading domain later should be just templated" from it.
- **Status:** proposed, our defaults until the owner says otherwise: script kinds `worker` and `system` stay general and a domain may add its own (`decision` is the prediction-market domain's); a general stop switch at the system level and the order stop switch in the domain; accounts known to the system only by key name and owner approval, money fields in the domain; `apps/trading-ui/` [45] stays where the owner put it, as the domain's dashboard; the system says "agent" and "version", while "strategy", "variant", "champion and challenger" and "trading agent" are the domain's words; the domain's notes take a `trading-` prefix so that a trading agent's links to the system's notes and the domain's never share a name; the currency moves to the domain's config, while the rule that a field's name carries its unit stays general.
- **Sources:** in-20261007-0904, D-056
- **Changed:** the tree notes (new items under [19], [14.3] and [54.3] moved, [42] retired), the topic notes split into general and `trading-` notes, the helper agents and skills, `CLAUDE.md`.

### D-059: Trading is a folder of domains; trading gets its own three docs
<!-- k: id=d-059 applies=[4],[19],[56],[56.1],[2.1],[2.2],[2.22] sources=in-20261009-0940,D-056,D-058 status=decided -->
- **Decision:** `agents/trading/` [56] holds the trading domains: the prediction-market domain moves to `agents/trading/prediction-market/` [19] (numbers kept), and a later one is `agents/trading/copytrading/`. `agents/trading/docs/` [56.1] holds trading's own vision, README and rebuild prompt. The system's three docs are rewritten in general terms. The prediction-market and copy-trading docs are not touched now.
- **Date:** 2026-10-09
- **Why:** the owner's message: "prediction market is a trading domain we can just add it to one folder trading/prediction-market", "put in a trading/docs first 3 documents that relates to trading", "make for system agent also 3 files and that is it for now".
- **Status:** decided. Our defaults: `trading/` has only its `docs/` for now (no agent, configs or scripts of its own); the trading notes, config and scripts stay in the prediction-market domain until the owner says otherwise; the domain's file names (`prediction-market-agents.config.json` and the like) keep their names; the system still reaches each domain through `subagents.link/`.
- **Sources:** in-20261009-0940, D-056, D-058
- **Changed:** the tree notes ([4], [19], new [56]), the paths in the notes, tools and mirror tree, the system's README and rebuild prompt, trading's new three docs.

### D-060: Voice input for the page's AI boxes, transcribed by Groq
<!-- k: id=d-060 applies=[53],[53.1.1],[53.3],[53.3.2],[53.3.4],[53.3.5] sources=in-20261009-1019 status=decided -->
- **Decision:** the request box and the delete note box get a microphone button: press to record (5 minutes at most), the text is added to the box, and the owner sends it as usual. The project IDE server transcribes through Groq's free speech models (`voice.py` [53.3.5], route `api/voice`), trying the models listed in its config in order and moving on after a rate limit or an error. The key `GROQ_API_KEY` sits only in the git-ignored keys file; the page never sees it.
- **Date:** 2026-10-09
- **Why:** the owner's message: "voice button for the ai inputs on ui so when press we start recording 5 min limit", "we ll use groq free model for that rotate them if one have rate limit or problems", "put it in a secretes".
- **Status:** decided. Our defaults: the models `whisper-large-v3-turbo` then `whisper-large-v3`; the text is added to the box, not sent by itself; the button shows only on the owner's server, because claude.ai pages get no microphone and cannot reach Groq.
- **Sources:** in-20261009-1019
- **Changed:** the page [53.1.1], the server [53.3.2], its config [53.3.4], new `voice.py` [53.3.5], the server README [53.3.1].

### D-061: The research studies move to agents/trading/researches/; the page shows the real files
<!-- k: id=d-061 applies=[56],[56.2],[54.1],[54.2],[54.3] sources=in-20261009-1230,D-045,D-059 status=decided -->
- **Decision:** the repository's top-level `researches/` moves to `agents/trading/researches/` [56.2], with its three studies: prediction-market research [54.1], self-improving agents [54.2] and trading-agent architectures [54.3]. The File Tree page marks every item that exists in the repository and lists every real file under such a folder, read from the repository at each build.
- **Date:** 2026-10-09
- **Why:** the owner's message: "get last version from github there will be researches folder move it to trading/researches folder, and make sync that current file tree represent real file tree in a project".
- **Status:** decided. Our defaults: the folder keeps the owner's name `researches/` (every agent's own folder is `research/`); all three studies move, the self-improving-agents study included, as the owner moved the whole folder; every real file is shown, the planning copy `vision/` included (owner, 2026-10-09 14:59: "we always should have real represention of file tree on a disk and on ui"); the texts of real files load when one is opened (`real-files.json`), so the page stays small; real files found by the scan get no How it works file of their own, their folder's describes them.
- **Sources:** in-20261009-1230, D-045, D-059
- **Changed:** the repository (the move), the tree notes ([56], new [56.2], [54], [54.1]-[54.3]), the page build (`enrich.py` lists real files), the mirror tree.

## Changelog
- v1.15 (2026-10-09): D-061 added.
- v1.14 (2026-10-09): D-060 added.
- v1.13 (2026-10-09): D-059 added.
- v1.12 (2026-10-07): D-058 added; D-057 status (the one clash, `server.py`).
- v1.11 (2026-10-07): D-056, D-057 added; D-054 status (named).
- v1.10 (2026-10-07): D-053 changed: a rebuild prompt listed at every level.
- v1.9 (2026-10-06): D-055 added.
- v1.8 (2026-10-06): D-051 to D-054 added.
- v1.7 (2026-10-06): D-050 added.
- v1.6 (2026-10-06): D-049 added.
- v1.5 (2026-10-06): D-048 added.
- v1.4 (2026-10-06): D-047 added.
- v1.3 (2026-10-06): D-045, D-046 added.
- v1.2 (2026-10-05): D-044 added.
- v1.1 (2026-10-05): D-043 added.
- v1.0 (2026-10-05): D-042 added.
- v0.9 (2026-10-05): D-041 added; D-040 status (layout decided).
- v0.8 (2026-10-05): D-039, D-040 added; D-038 amended (reading font).
- v0.7 (2026-10-05): D-038 added.
- v0.6 (2026-10-05): D-037 added.
- v0.5 (2026-10-05): D-036 added.
- v0.4 (2026-10-01): D-035 added.
- v0.3 (2026-10-01): D-034 added.
- v0.2 (2026-09-30): D-033 added.
- v0.1 (2026-09-30): created from file-tree.md v1.15, vision.md v0.19 and the owner inputs (D-033). The seed list D-001 to D-031 that stood in file-tree.md [2.6] moved here.
### D-062: An inputs vision: every owner requirement by scope, in ASD-STE100
<!-- k: id=d-062 applies=[2.23] sources=in-20261009-1938 status=decided -->
- **Decision:** `agents/system/docs/inputs-vision.md` [2.23] holds a detailed overview of the project from all of the owner's inputs only. Repeated logic appears once; logic a newer input contradicts is left out. It is divided by scope of logic (for example the system agent and common file rules) and written in ASD-STE100 style. Before it was written, every owner message in the project chat, its reply threads and this thread was checked against `docs/inputs/`; five messages from 2026-10-09 were missing and are now filed.
- **Date:** 2026-10-09
- **Why:** the owner wants one systematic, documentation-style view of everything they asked for.
- **Status:** decided. Ours: rule codes per scope (`SYS-01` and so on), a terms table, an "Open subjects" list, and the knowledge base agent keeping it current after each input.
- **Changed:** file-tree.md [2.23]; vision/.claude/docs/inputs-vision.md with its metadata files; docs/inputs (5 files added).

