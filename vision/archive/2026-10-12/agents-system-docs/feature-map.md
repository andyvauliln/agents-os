# Agent OS: Feature map (v1.13)

> Draft of `agents/system/docs/feature-map.md` ([2.12] in `file-tree.md` [2.13]; shared docs live in the system domain, D-017). Maps each feature/logic area to the folders and files that hold it, and to the agent type that owns it. Numbers `[n]` refer to `file-tree.md`. It is kept in line with the rest of the knowledge base by the knowledge agent [10.1.1.2] (D-033). **(proposed)** marks anything not stated by the owner. Anything with no files yet is listed as a gap in §13. The trading features (decision and execution, risk, portfolio, backtesting, the trading dashboard) are in the prediction-market domain's `trading-feature-map.md` [19.6.14].

Agent types (vision §8): **Support** = system-support agent · **Sub** = sub-agent (worker + AI) · **Main** = main agent (the agent that runs and decides) · **System** = system-level agent [10] (D-022) · **Domain** = domain-level agent, its `.claude/CLAUDE.md` is the domain owner [19.1.5] (D-022, D-024) · **SI** = self-improvement sub-agent at any level (D-018) · **Owner** = you.

## 1. Data collection (workers)
<!-- k: id=fm-data-collection-workers applies=[14.2],[31],[11.10],[19.2.1],[21.2.1],[27.4],[11.2],[32],[14.1],[2.14],[16.1],[16.2],[16.3],[16.4.1],[19.5.1],[21.5.1],[35],[35.2],[35.1],[2.11.2],[2.18.2] sources=derived status=decided -->

| Logic in plain words | Files / folders | Owner |
|---|---|---|
| Workers are scripts that fetch data on a schedule and write JSON/MD (D-007) | [14.2] `scripts/workers/*.worker.*` (shared), [31] `*.worker.py` (agent-local) |
| Jobs per agent (D-029): scripts and AI runs, on/off, schedule (every, cron, once, after, manual), where they run, platform, model, AI-run parameters | [11.10] `system.workers.json` (format), [19.2.1], [21.2.1], [27.4]; by domain through [11.2] `configs/subagents.link/` (D-030); the scheduler scans `agents/**/configs/*.workers.json` | Support, Domain, Owner |
| Clean/normalise raw data before agents read it | [32] `clean-data.system.js`, [14.1] `scripts/system/` | Support |
| Shape of every JSON/MD file | [2.14] `data-schemas.md` | Support |
| Data (D-010 amended by D-014/D-015): shared data by source in the system domain; each agent's own data in its folder | [16.1]–[16.3] shared; [16.4.1] link to each domain's data, and on down through [19.5.1], [21.5.1] (D-030); agent: [35] `data/` with [35.2] own outputs and [35.1] file links to the data files it uses (D-020) | Support |
| Check existing workers/data before adding a new one (proposed) | [2.11.2] `how-to/add-worker.md`, [2.18.2] `index/workers.md` | Support, Domain |
| Promote an agent-local worker to shared when reused (proposed) | [31] → [14.2] | Support |

## 2. Pre-analysis (sub-agents)
<!-- k: id=fm-pre-analysis-sub-agents applies=[10.1.1],[19.1.1],[21.1.1],[16.3],[15.4],[35.1],[34.1] sources=derived status=decided -->

| Logic | Files / folders | Owner |
|---|---|---|
| Sub-agents (Claude Code subagents, D-008/D-016) read worker data and pre-analyse it for main agents | system [10.1.1], domain [19.1.1] and each level below, e.g. [21.1.1]; each level runs its own; a parent reads its children's outputs through `subagents.link/` (D-030) | Sub |
| Sub-agent outputs and logs | [16.3] `data/subagents/`, [15.4] `logs/subagents/`; agents read them via [35.1] / [34.1] | Sub |

## 3. Subscriptions and triggers
<!-- k: id=fm-subscriptions-and-triggers applies=[27.4],[27.3],[14.1],[10.1],[24],[35.1],[27.1],[30.1],[34.1],[46.1],[11.13],[19.2.3],[21.2.3],[21.1.1.1],[2.7],[2.17.2],[11.10],[19.3.2],[21.3.2],[30.3],[10.6],[16.1],[2.11.9],[2.20],[11.2],[14.4],[15.5],[16.4],[10.8.3],[10.9.3],[19.2.2],[19.3.1],[19.4.1],[19.5.1],[19.6.1],[19.12.3],[19.13.3],[21.2.2],[21.3.1],[21.4.1],[21.5.1],[21.6.1],[21.12.3],[21.13.3],[40],[4],[10],[19],[19.1],[21],[21.1],[11.1] sources=derived status=decided -->

| Logic | Files / folders | Owner |
|---|---|---|
| Which workers/sub-agents an agent runs | its workers file [27.4] (D-029; was [28]); data it reads from others in its links file [27.3] (D-031) | Main, SI |
| No `.claude` links at any level for now (D-030; D-019 down-links paused, [10.1.3], [10.1.4], [21.1.3], [21.1.4] retired) | [14.1] `check-links` reports any `.claude` link | Support |
| Where sessions run (proposed, D-021): each level in its own folder, down to the running agent; higher-level sub-agent outputs reach agents as linked data files | [14.1] `run-agent`, [10.1], [24], [35.1] | Support |
| Shared things reach an agent as individual file links `[name].link.[ext]`, only what its logic needs, from any folder (D-020; `.link` rule D-002) | [27.1], [30.1], [34.1], [35.1], [46.1]; listed in each agent's links file ([11.13] format; [19.2.3], [21.2.3], [27.3]; D-031), from anywhere: system, own domain or a level above, another domain, another agent; first written by [14.1] `create-agent`, then edited by the agent itself, its SI [21.1.1.1] or the owner; built by [14.1] `relink`; checked by [14.1] `check-links`; rule in [2.7], [2.7.5], [2.17.2] | Support |
| Links follow the links files (D-031): relink runs when a links file changes, at review time (git pre-commit, post-merge, post-checkout; owner approval in the UI), when an agent edits its own links file (it reruns relink; `PostToolUse` hook) and from create-agent/init.sh; it keeps a links index of who reads what | [14.1] `relink` + `check-links`; job `relink` in [11.10]; relink links [19.3.2], [21.3.2], [30.3]; hook in each level's `settings.json` ([2.7.2]); git hooks installed by [10.6] `init.sh`; index in [16.1]; runbook [2.11.9] | Support, Main, SI |
| Each level sees its children (D-030): own files + `subagents.link/[child]/` in every content folder, same template at every level | system [2.20], [11.2], [14.4], [15.5], [16.4], [10.8.3], [10.9.3]; domain [19.2.2], [19.3.1], [19.4.1], [19.5.1], [19.6.1], [19.12.3], [19.13.3]; the levels below, e.g. [21.2.2], [21.3.1], [21.4.1], [21.5.1], [21.6.1], [21.12.3], [21.13.3]; made by the child's [40] `init.sh`; checked by [14.1] `check-links`; rule [2.7.4] | Support |
| Layout: `agents/[domain]/`, `system` is a domain; `.claude/` at the domain level and below (D-013, D-016) | [4], [10], [10.1], [19], [19.1], [21], [21.1]; system-support roles are sub-agents (D-026) | Support |
| Run on a schedule or once on a date, locally or in the cloud (proposed) | each agent's workers file ([11.10] format, D-029), [11.1] `schedules` (defaults), [14.1] `scheduler` + `run-job`, state [16.1] `scheduler-state.json` | Support |
| Important file change cancels the current run and restarts; unimportant changes wait | `on_change` on the main-run job in [27.4] (D-029), [11.1] `triggers` section (common rules), [14.1] `scheduler` (proposed) | Support |
| Track "new since last run" | [16.1] cursors / file timestamps (mechanism open) | Support |

## 4. Agent run loop
<!-- k: id=fm-agent-run-loop applies=[24.5],[2.17.3],[25],[24.8],[41],[14.1],[30],[35],[26],[10.1.1],[27],[27.2],[27.1],[11.1],[34] sources=derived status=decided -->

| Logic | Files / folders | Owner |
|---|---|---|
| Instructions: role, loop, allowed actions | [24.5] `.claude/CLAUDE.md` (built on [2.17.3] `common-prompt.md`), [25] `.claude/skills/`, [24.8] `.claude/rules/` | Main |
| Start a run (single run or loop) | [41] `start.sh`, [14.1] `run-agent.system.js` (proposed) | Main |
| Read data → analyse → decide → act | [24.5], the agent's scripts [30], [35] | Main |
| Call sub-agents during a run | [26] `.claude/agents/` → [10.1.1] | Main |
| Agent config (mode, workers, own settings): a real file in the agent (D-014) | [27] `configs/` → [27.2] `[agent-name].config.json`; shared config files via [27.1] file links (e.g. `system.config.link.json`) | Main, SI |
| Config merge (proposed): global → agent → owner UI overrides; limits tighten-only, live only with owner approval, kill switch wins; `effective-config.json` per run | [11.1], [27.2], [34] | Support |

## 5. Actions (test / live)
<!-- k: id=fm-decision-and-execution-test-live applies=[11.1],[27.2],[23],[2.7],[2.8] sources=derived status=decided -->

| Logic | Files / folders | Owner |
|---|---|---|
| Every acting service reads test/live mode from config; kill switch | [11.1] `modes` section, [27.2] `mode` | Support |
| Mode shown in the agent name | [23] naming, [2.7] `conventions.md` | Support |
| Hard limits in code, separate from the LLM; a lower layer may only tighten them (proposed) | [2.8] `safety.md` (rules); no enforcing file yet | Support |

## 6. Self-improvement wheel
<!-- k: id=fm-self-improvement-wheel applies=[10.1.1.1],[19.1.1.2],[21.1.1.1],[2.17.4],[10.1.12],[19.1.12],[21.1.12],[10.9],[19.13],[21.13],[50],[16.3],[15.4],[19.5],[19.4],[2.16],[2.11.1],[27.3],[46],[10.8],[19.12],[21.12],[49],[49.1.1],[49.2.1],[2.14],[2.11.7],[14.1],[30.2],[34.2],[2.11.4],[50.1],[50.2],[2.11.8],[11.11],[14.2],[11.10],[19.1.5],[19.11] sources=derived status=decided -->

| Logic | Files / folders | Owner |
|---|---|---|
| Self-improvement at every level (D-018): reads logs, data, docs, research and owner comments | SI sub-agents [10.1.1.1] system, [19.1.1.2] domain, and the levels below, e.g. [21.1.1.1]; templates [2.17.4] | SI |
| SI memory and state (proposed, D-024 updates D-022): memory in the level's `.claude/agent-memory/[si-name]/MEMORY.md`; research in `research/` (D-025); history in `data/`; logs in `logs/` | memory: system [10.1.12], domain [19.1.12], and below, e.g. [21.1.12]; research [10.9], [19.13], [21.13], [50]; data/logs: [16.3]/[15.4], [19.5]/[19.4] | SI |
| Compare versions of an agent and decide promotion or retirement | [2.16] `metrics.md` | SI, Domain, Owner |
| Produce a new configuration/code as a new test agent | the level's SI sub-agent → a new agent folder, [2.11.1] `create-agent.md` | SI |
| Link changes (by the agent itself, its SI or the owner): logged in the `Links` section of its `changes.md` | [27.3], [46] `changes.md` | SI, Main |
| Record what changed in each new agent | the agent's own [46] `docs/changes.md`, read by its parent through `subagents.link/` | SI |
| Tests per level (D-025, proposed): `tests/agents/` (prompt + sub-agent behaviour) and `tests/scripts/` (code), each with a `tests.config.json` (enabled, schedule, owner, last run, result, next action) | [10.8], [19.12], [21.12], [49] ([49.1.1], [49.2.1]); template [2.7.3]; schema [2.14]; runbook [2.11.7] | SI, Support, Owner (enable/disable in UI) |
| Run tests from the config, write results back and to logs; `before_promote` tests gate promotion (proposed) | [14.1] `run-tests.system.js`, linked as [30.2]; results [34.2] `logs/tests.jsonl`; [2.11.4] | Support |
| Research history per level (D-025): `index.json` (question, status, results, decisions, related agents, changes and tests) + one folder per item | [10.9], [19.13], [21.13], [50] ([50.1] `index.json`, [50.2] items); schema [2.14]; runbook [2.11.8] | SI, Domain, Owner |
| Watch the outside world (news, new harness/model) and update related logic | [11.11] (routing updates), [14.2] + [11.10] (news worker jobs) | SI, Domain, Support |
| Domain-level: find, create and update the domain's agents; domain health | [19.1.5] domain `.claude/CLAUDE.md` (domain owner), started by [19.11] | Domain |

## 7. Agent creation
<!-- k: id=fm-agent-creation applies=[2.11.1],[14.1],[40],[27.3],[38],[39],[10],[19],[21],[23],[10.4],[10.5],[10.6],[10.7],[19.2],[19.3],[19.4],[19.5],[19.6],[19.8],[19.9],[19.10],[19.11],[21.2],[21.3],[21.4],[21.5],[21.6],[21.8],[21.9],[21.10],[21.11],[41],[10.1.5],[10.1.6],[10.1.7],[10.1.8],[10.1.9],[10.1.10],[10.1.11],[10.1.12],[10.1.13],[19.1.5],[19.1.6],[19.1.7],[19.1.8],[19.1.9],[19.1.10],[19.1.11],[19.1.12],[19.1.13],[21.1.5],[21.1.6],[21.1.7],[21.1.8],[21.1.9],[21.1.10],[21.1.11],[21.1.12],[21.1.13],[24.5],[24.6],[24.7],[24.8],[24.9],[24.10],[24.11],[24.12],[24.13],[10.1.2],[10.1.1],[19.1.2],[19.1.1],[21.1.2],[21.1.1],[25],[26],[48],[2.7],[2.18.1],[2.18],[46],[2.10] sources=derived status=decided -->

| Logic | Files / folders | Owner |
|---|---|---|
| Owner/system input → new agent integrated into the system | [2.11.1] `create-agent.md`, [14.1] `create-agent.system.js` (proposed) | Support, Domain, SI |
| Scaffold: install, write the links file, relink, register | [40] `init.sh` (runs [14.1] `relink`, D-031), [27.3] links file, [38] `package.json`, [39] `requirements.txt` | Support |
| Standard agent folder, identical at every level (D-022): system [10], domain [19], and the levels below, e.g. [21], [23] | [2.7.1] template; level files [10.4]–[10.7], [19.2]–[19.11], [21.2]–[21.11], [38]–[41] | Support |
| Standard `.claude/` at every level (D-024): `CLAUDE.md`, `settings.json` (permissions incl. `.secrets/**` deny, hooks, env, model), `settings.local.json`, `rules/`, `skills/`, `commands/`, `agents/`, `workflows/`, `output-styles/`, `agent-memory/`, `agent-memory-local/`; generic placeholders for now | [2.7.2] template; [10.1.5]–[10.1.13], [19.1.5]–[19.1.13], [21.1.5]–[21.1.13], [24.5]–[24.13]; skills/agents [10.1.2]/[10.1.1], [19.1.2]/[19.1.1], [21.1.2]/[21.1.1], [25]/[26]; [48] ignores local files | Support |
| System manager: all domains + system development | [10.1.5] system `.claude/CLAUDE.md`, [10.7] `start.sh` (also starts the scheduler) | System |
| Unique agent name = ID everywhere (D-012): format check, reserve, never reuse | [2.7] naming rule, [2.18.1] `index/agents.md` (registry), [14.1] `create-agent.system.js` (check point) | Support |
| Register in index and UI; scaffold the agent's own docs | [2.18] `index/`, [46] agent `docs/` + its entries in the parent's `subagents.link/` (D-030) | Support |
| Save the owner's raw input | [2.10] `docs/inputs/` | Support |

## 8. Model and platform routing
<!-- k: id=fm-model-and-platform-routing applies=[11.11],[2.18.6],[14.1],[24],[2.11.3] sources=derived status=decided -->

| Logic | Files / folders | Owner |
|---|---|---|
| Routing: which model/platform each agent, sub-agent and worker uses (D-011) | [11.11] `models.config.json` (`routes`, `defaults_by_type`) | Support |
| List of platforms/models and status | [11.11] `platforms` / `models`, [2.18.6] `index/models.md` | Support |
| A route change is tested as a new version; where the name carries the model, it must match the route | [11.11], check in [14.1] | Support, SI |
| Platform-specific harness config | [24] `.claude/` (Cursor equivalent open) | Support |
| Add a new platform/model | [2.11.3] `add-platform-or-model.md` | Support |

## 9. UI: monitoring and control
<!-- k: id=fm-ui-monitoring-and-control applies=[53],[15],[16],[11.2],[2.20],[2.18],[2.16],[11.1],[2.11.4],[2.11.5],[2.11.1],[14.1] sources=derived status=decided -->

The owner's UI: the project IDE [53] may do this job (owner, 2026-10-06). The prediction-market domain's own dashboard [45] is in its `trading-feature-map.md`.

| Logic | Files / folders | Owner |
|---|---|---|
| Performance, logs, data used/produced, decisions, improvements | the owner's UI reading [15] (shared logs + `subagents.link/`), [16] (shared data + `subagents.link/`), [11.2] (configs by domain), [2.20] (docs by domain), each followed down level by level (D-030), [2.18], [2.16] metrics | Support |
| Approve/reject going live; stop/delete (writes [11.1] `modes`) | the owner's UI, [2.11.4] `promote-to-live.md`, [2.11.5] `stop-or-delete-agent.md` | Owner |
| Comments, questions to an agent, "what to do better" | the owner's UI (storage of comments not defined yet) | Owner, Domain, SI |
| Create an agent from the UI | the owner's UI → [2.11.1] / [14.1] | Owner, Support |

## 10. Logging and analytics
<!-- k: id=fm-logging-and-analytics applies=[34],[21.4.1.1],[15.5],[15.1],[15.2],[15.3],[15.4],[15.5.1],[34.1],[2.16] sources=derived status=decided -->

| Logic | Files / folders | Owner |
|---|---|---|
| Per-run logs: inputs, reasoning, decisions, actions, cost | agent's own [34] `logs/`; its parent's view through `subagents.link/`, e.g. [21.4.1.1] | Main |
| Shared logs by source (D-009 amended by D-014/D-015): system, services, workers, subagents; plus [15.5] `subagents.link/` to each domain's logs (D-030) | [15.1]–[15.4], [15.5.1]; agents read them via [34.1] | Support |
| Metrics per agent: cost, latency, errors, tests | [2.16] `metrics.md` (definitions + the general promotion rule); no computing script yet | Support, SI |

## 11. Docs and self-support
<!-- k: id=fm-docs-and-self-support applies=[10.1.1.2],[10.1.2.1],[10.1.2.2],[2.1],[2.18.8],[2.21],[2.2],[2.10],[2.3],[2.17.1],[2.15],[2.18],[2],[46],[46.1],[2.20],[19.6.1],[21.6.1],[2.13],[2.12],[2.7],[2.4],[2.6],[2.5],[2.9],[10.1.5],[19.1.5],[43] sources=derived status=decided -->

| Logic | Files / folders | Owner |
|---|---|---|
| Owner vision and raw inputs | [2.2] `vision.md`, [2.10] `inputs/` | Support |
| Knowledge base: every owner input (and Claude's answer to it) and every system change is stored, placed in the one doc that owns it, rippled to everything it applies to, and summarised as "How it works" for every file and folder, bottom up (D-033) | [10.1.1.2] `sys-knowledge-agent`, skills [10.1.2.1] `knowledge-intake` and [10.1.2.2] `file-index`, [2.1] `README.md` (layers and tag format), [2.18.8] `knowledge-map.json`, [51] `[name].index.md` files, [14.1] `build-map`, job `knowledge-sync` in [11.10] | System, Support |
| Architecture: the system's parts and how they connect | [2.21] `architecture.md` | Support |
| How the OS works; agent architecture; flows | [2.3] `overview.md`, [2.17.1] `common/agent-architecture.md`, [2.15] `flows.md` | Support |
| Index of all agents, workers, sub-agents, services, apps, models | [2.18] `docs/index/` | Support |
| Shared docs in the system domain; each agent's own real `docs/` + file links to the shared docs it needs; every level reaches its children's docs through `docs/subagents.link/` (D-017, D-030) | [2] `agents/system/docs/`, [46], [46.1], [2.20], [19.6.1], [21.6.1] | Main, SI, Domain, Support |
| Layout and mapping | [2.13] `docs/file-tree.md`, [2.12] `docs/feature-map.md` (kept in sync) | Support |
| Rules, terms, decisions, plan, history | [2.7], [2.4], [2.6], [2.5], [2.9] | Support, Owner |
| Answer owner questions about system state; address owner comments | [10.1.5] system `.claude/CLAUDE.md` (whole system), [19.1.5] domain `.claude/CLAUDE.md` (per domain) | System, Domain |
| Cloned external repos | [43] `apps/`, one folder each when needed (D-045) | Support |

## 12. Safety
<!-- k: id=fm-safety-and-risk applies=[2.8],[11.1],[47],[47.1],[47.2],[47.3],[48],[11.11],[14.1],[2.11.6] sources=derived status=decided -->

| Logic | Files / folders | Owner |
|---|---|---|
| Rules: test vs live, owner approval to go live, kill switch | [2.8] `safety.md` | Owner |
| Hard limits enforced in code; a lower layer may only tighten them | [2.8] `safety.md`; no enforcing file yet | Support |
| Keys: stored in a git-ignored store, test/live separated, loaded by scripts at execution time, never linked, logged or put in LLM context (D-023, proposed) | [47] `.secrets/` ([47.1] test, [47.2] live, [47.3] index), [48] `.gitignore`; refs in [11.11] `platforms` and in configs' `secret_keys`; [14.1] `load-secret`, `check-links`; deny rule in each `.claude/settings.json` ([x.6], D-024); runbook [2.11.6]; rules [2.8] |
| Owner notifications | [11.1] `notifications` section; `notifier.system.js` in [14.1] (proposed) | Owner, Support |
| External text treated as untrusted | [2.8] | Support |

## 13. Gaps: features with no files yet
<!-- k: id=fm-gaps applies=[24.12],[2.16],[46],[2.14],[14.1],[4] sources=derived status=open -->

1. **Main-agent memory and previous/next run info.** These were in v0.1; only SI sub-agents have memory, now proposed in each level's `.claude/agent-memory/` ([x.12], D-024). A main agent could use its own [24.12] `agent-memory/` the same way (open).
2. **Metrics.** The general metrics (cost, latency, errors, tests) have a home in [2.16] `metrics.md`, but there is no script that computes them and no stored results file.
3. **Owner comments and questions from the UI.** Partly placed: per-agent `notes.md` in [46]; the data file and its schema in [2.14] are still missing.
4. ~~Secrets / keys / wallets~~: closed by D-023 ([47] `.secrets/`, `load-secret`; proposed design).
5. **Scheduler / trigger watcher.** Only a proposed script in [14.1]; its form is undecided (central vs per agent).
6. **System-support agents.** No folder yet ([4] open question).
7. ~~Self-improvement templates~~: now [2.17.4] (doc only; no code templates yet).
8. **Outside-world watchers** (new models, harnesses, news). No dedicated worker defined.

Before v1.13 this list also held the trading gaps (1 executor and risk check; 2 portfolio, positions and trading accounts; 4 trading analytics; 11 backtesting); they are now in the prediction-market domain's `trading-feature-map.md`.

---

## Changelog

- **v0.1** – initial draft from vision v0.2 and file-tree v0.3.
- **v0.2** – file tree moved to [2.13] `docs/file-tree.md`; references updated.
- **v0.3** – synced with file-tree v0.5: `.link` symlinks, data-schemas [2.14], flows [2.15], metrics [2.16], common [2.17], index [2.18] (replaces catalog [8]), per-agent docs [2.19]; gaps 4, 5, 9 updated.
- **v0.4** – synced with file-tree v0.6: configs [11.1]–[11.9] mapped (modes, risk, schedules, triggers, routing link, accounts, notifications, domains), merge rule row; gap 6 updated.
- **v0.5** – synced with file-tree v0.7 (D-006): all config references point to [11.1] `system.config.json` sections or [11.2.1] per-agent config (linked as [27] `config.link.json`); merge rule simplified to global → agent → owner UI.
- **v0.6** – synced with file-tree v0.8 (D-007–D-011): workers = scripts [14.2] + [11.10]; sub-agents = Claude Code [10.1.1]; logs [15.x] and data [16.x] central by source; routing in [11.11] `models.config.json`; `[33]` renamed `make-buy.decision.js`.
- **v0.7** – added D-012 row (unique agent names: [2.7], [2.18.1], [14.1]).
- **v0.8** – synced with file-tree v1.0 (D-013–D-016): system is a domain; agents own real `configs/`, `scripts/`, `logs/`, `data/` with `system.link/`s; system views of every agent; `.claude/` at domain and strategy levels; retired [36]–[36.2].
- **v0.9** – synced with file-tree v1.1 (D-017): shared docs in `agents/system/docs/` [2]; agent docs are real [46] with [46.1] `system.link/`; view [2.20]; [2.19] and [29] retired.
- **v1.0** – synced with file-tree v1.2 (D-018): domain owner and SI are sub-agents ([19.1.1.1]; [10.1.1.1], [19.1.1.2], [21.1.1.1]); memory in [16.3]; [20], [22] retired.
- **v1.1** – synced with file-tree v1.3 (D-019): `.claude` down-links only; upward [25.x]/[26.x] removed; open question on `system.link/` folders noted.
- **v1.2** – synced with file-tree v1.4 (D-020): agents use individual file links listed in `links` [27.3]; no `system.link/` folders in agents.
- **v1.3** – synced with file-tree v1.5 (D-021): no domain → strategy `.claude` links; run-location row added.
- **v1.4** – synced with file-tree v1.6 (D-022): three level agents with the standard folder; domain owner = domain `CLAUDE.md`; SI memory in level `data/`.
- **v1.5** – synced with file-tree v1.7 (D-023): secrets store [47], `load-secret`, runbook [2.11.6]; gap 6 closed.
- **v1.6** – synced with file-tree v1.8 (D-024): standard `.claude/` row; `CLAUDE.md` references moved to [x.5] ([10.1.5], [19.1.5], [21.1.5], [24.5]); SI memory in `.claude/agent-memory/`; gap 3 updated.
- **v1.7** – synced with file-tree v1.9 (D-025): tests and research rows in §6; SI research moved to `research/`; gap 11 (backtesting) partly placed.
- **v1.8** – fix: cross-variant history points to [21.5] (was stale [16.3]), synced with file-tree v1.10.
- **v1.9** – synced with file-tree v1.13 (D-029): jobs rows point to the per-agent workers files [11.10]/[19.2.1]/[21.2.1]/[27.4] and the view [11.12]; `trigger-watcher` → `scheduler` + `run-job`.
- **v1.10** – synced with file-tree v1.14 (D-030): system views and the jobs view [11.12] → `subagents.link/` in every level's content folders; `.claude` link rows retired.
- **v1.12** (2026-09-30) – knowledge base (D-033): rows for the knowledge agent and architecture; variant naming and the strategy loop (D-032); stale [10.2], [2.19] and D-019 references fixed; knowledge tags added.
- **v1.11** – synced with file-tree v1.15 (D-031): links files per agent ([11.13], [19.2.3], [21.2.3], [27.3]) and the `relink` script; new row for when relink runs.
- v1.13 (2026-10-07): trading parts moved to the prediction-market domain's `trading-feature-map.md` (D-056, D-058); [42] removed from the layout; gaps renumbered.
