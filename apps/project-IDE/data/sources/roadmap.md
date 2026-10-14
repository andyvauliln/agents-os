# Agent OS: Roadmap (v0.2)

Where the project stands: the current phase, what is done (the decisions so far, by area), what is being worked on now, what comes next and later, and the biggest open design questions. One line per item. Decision texts and dates are in decisions.md; the owner's own open questions are in vision.md. The trading roadmap (MVP strategies, venues, live trading and the trading questions) is the prediction-market domain's `trading-roadmap.md` [19.6.13].

## Current phase: planning
<!-- k: id=road-phase applies=[0],[2.5] sources=in-20260929-1452,in-20260929-1455 status=decided -->
- Nothing is built yet. The design lives in the knowledge base (planning copy `/mnt/project-files/vision/docs/`, later `agents/system/docs/` [2]).
- Order of work, set by the first brief: vision, then file tree, then architecture, then flows, then data structures, then details.
- Method, set by the owner: go through the file tree object by object; the owner answers, and the docs are updated after every input.
- Where we are: vision drafted; file tree v1.16 with one fully expanded example agent [23]; architecture, flows and data schemas at v0.1.

## Done so far
Decisions by area. "Superseded" or "paused" items are kept for history.

### Docs and knowledge
<!-- k: id=road-done-docs applies=[2.5] sources=D-003,D-004,D-017,D-033,in-20260929-1506,in-20260929-1509 status=decided -->
- D-004: one docs root with `common/`, `index/`, data schemas, flows and metrics; feature map and file tree added on request.
- D-003: per-agent docs kept centrally (superseded by D-017).
- D-017: docs follow the shared-folder pattern, in `agents/system/docs/` [2]; the root keeps only `README.md`.
- D-033: the knowledge base, the knowledge agent [10.1.1.2] with its two skills, the knowledge map and layered How it works summaries.

### Layout and levels
<!-- k: id=road-done-layout applies=[2.5] sources=D-013,D-014,D-015,D-016,D-022,D-024,D-056 status=decided -->
- D-013: `agents/` holds domains only, and `system/` is one of them.
- D-014: every agent has the same real content folders.
- D-015: system views of every agent (replaced by D-030).
- D-016: `.claude/` at the domain level and below.
- D-022: one identical folder at every level (system, domain and the levels below); the domain prompt is the domain owner.
- D-024: the standard `.claude/` layout at every level, with `CLAUDE.md` inside it.

### Sub-agents and self-improvement
<!-- k: id=road-done-subagents applies=[2.5] sources=D-008,D-018,D-026 status=decided -->
- D-008: sub-agents are Claude Code sub-agents in `.claude/agents/`.
- D-018: the domain owner and self-improvement are sub-agents, with an SI sub-agent at every level.
- D-026: system-support roles are system sub-agents, not folders.

### Links
<!-- k: id=road-done-links applies=[2.5] sources=D-001,D-002,D-019,D-020,D-021,D-030,D-031 status=decided -->
- D-001: shared things are symlinked into agents.
- D-002: every symlink has `.link` in its name.
- D-019: `.claude` links go parent to child only (paused by D-030).
- D-020: agents link individual files, not folders.
- D-021: no `.claude` links from a domain to the level below it.
- D-030: own files plus `subagents.link/[child]/` in every content folder; no `.claude` links for now.
- D-031: a links file per agent and the shared `relink` script.

### Configs, jobs and routing
<!-- k: id=road-done-configs applies=[2.5] sources=D-006,D-007,D-011,D-029 status=decided -->
- D-006: two config types, one global and one per agent.
- D-007: workers are scripts; all scripts live in `scripts/`.
- D-011: routing lives in `models.config.json`.
- D-029: a jobs file `[name].workers.json` per agent (replaces the single workers config of D-007).

### Data, logs, tests and research
<!-- k: id=road-done-data applies=[2.5] sources=D-005,D-009,D-010,D-025 status=decided -->
- D-005: data as JSON and Markdown files for now.
- D-009, D-010: logs and data organised by source (own logs and data moved into agent folders by D-014).
- D-025: `tests/` and `research/` at every level, with a shared `run-tests`.

### Names
<!-- k: id=road-done-names applies=[2.5] sources=D-012 status=decided -->
- D-012: every agent has a globally unique name that is its ID everywhere.

### Secrets and git
<!-- k: id=road-done-secrets applies=[2.5] sources=D-023,D-027,D-028 status=decided -->
- D-023: one secrets store outside `agents/`, test and live kept apart.
- D-027: all test keys in one `test/.env`; `live/.env` owner-only and later; scripts get keys through the shared loader.
- D-028: `.gitignore` is a real, commented file.

## Now
<!-- k: id=road-now applies=[2],[2.13],[10.1.1.2] sources=D-033,in-20260929-2044,in-20260930-0722,in-20260930-1533,in-20260930-1603,in-20260930-1841 status=decided -->
- Knowledge base: every piece of knowledge placed once, in layers, with knowledge tags (D-033).
- Knowledge agent: the draft sub-agent and its skills `knowledge-intake` and `file-index`.
- Knowledge map rebuilt from the tags; first How it works summaries for every file and folder, bottom up.
- An "Always keep in mind" list in the overview and for every file and folder (in-20260930-1603).
- File Tree explorer: How it works as the main view, per-object tabs, search and a Changed tab.
- Every message on the page is an input, and answers to questions are filed as knowledge (in-20260930-1841).

## Next
<!-- k: id=road-next applies=[2.5] sources=in-20260929-1452,in-20260929-1455,in-20260929-1537,derived status=proposed -->
- Owner review of everything marked proposed, object by object in the file tree.
- Finish the remaining topic docs: flows, conventions, safety, metrics and the decision log.
- Settle the config shapes with two or three concrete example agents.
- Create the repo skeleton from file-tree.md: the system and the first domain.
- Build the core system scripts: create-agent, relink and check-links, scheduler and run-job, load-secret, run-tests, build-map.
- Move the knowledge base, the knowledge agent and its skills into `agents/system/`.
- Run the first agent in test mode.
- The first domain's own next steps (MVP strategies, its price collector, a first trading UI): its `trading-roadmap.md`.

## Later
<!-- k: id=road-later applies=[11.11],[47.2.1],[11.1],[47.1.1] sources=in-20260929-1455,in-20260929-1537,in-20260930-0812,D-027,D-056 status=decided -->
- Codex and Kimi 3 as platforms.
- Connect OpenRouter, for free-model rotation on unimportant work.
- More domains of any kind; a later trading domain is copied from the prediction-market domain (D-056).
- Live actions: `live/.env`, with the owner's approval for every agent that goes live.
- Split long sections of `system.config.json` into their own files when they grow.
- Split `test/.env` per account only if prefixes and sections stop being enough.

### Later, proposed
<!-- k: id=road-later-proposed applies=[14.1],[2.14],[2.13],[11.10],[4] sources=D-023,D-029,in-20260929-1452,derived status=proposed -->
- An OS keychain, a password manager or a vault behind `load-secret`, with the same key names.
- Machine-checkable JSON Schema files next to data-schemas.md.
- A drift check between file-tree.md and the real folders.
- Cloud, desktop and GitHub Actions jobs next to local ones.
- Meta-agents that combine other agents' signals (vision.md `vis-idea-meta-agents`).

## Biggest open questions
The open design questions, grouped by area, one per entry. The owner's own questions (scale, hosting, approvals, autonomy, retention, keys) are in vision.md, Open questions. The trading questions, the owner's (MVP strategies, real money, venues, the Polymarket suite, self-improvement scope and metrics) and ours, are in the prediction-market domain's `trading-vision-notes.md` and `trading-roadmap.md`.

### Repo and setup

#### One repo or several
<!-- k: id=road-q-repo applies=[0] sources=derived status=open -->
One git repo or several (e.g. `apps/` separate)?

#### Where the scheduler runs
<!-- k: id=road-q-scheduler-host applies=[11.10],[14.1] sources=D-029 status=open -->
Which machine runs the local scheduler: the owner's computer or a small always-on server?

#### Symlinks in git
<!-- k: id=road-q-commit-links applies=[11.13],[48] sources=D-031 status=open -->
Commit the symlinks to git, or let relink rebuild them after every clone and pull (proposed: commit them)?

#### Dependencies
<!-- k: id=road-q-deps applies=[38],[39] sources=derived status=open -->
Dependencies per agent, or shared through one workspace and one Python environment?

#### Root CLAUDE.md
<!-- k: id=road-q-root-claude applies=[1],[10.1.5] sources=derived,D-041,D-045 status=decided -->
Should the root `README.md` also serve as a root `CLAUDE.md` for agents working at the root? **Answered:** no. There is no root `CLAUDE.md`; the file every Claude reads first is the system's `.claude/CLAUDE.md` [10.1.5] (owner, 2026-10-06, D-045).

### Agents and runs

#### How CLAUDE.md is built
<!-- k: id=road-q-prompt-composition applies=[24.5],[2.17.3] sources=derived status=open -->
Is each `CLAUDE.md` built from the common prompt by import or link, or copied in at creation?

#### Cursor-routed agents
<!-- k: id=road-q-cursor-variant applies=[24] sources=in-20260929-1455 status=open -->
What does a Cursor-routed agent use instead of `.claude/`?

#### Self-editing
<!-- k: id=road-q-self-edit applies=[27],[46] sources=derived status=open -->
May an agent edit its own config and docs, or only its SI sub-agent and domain agent?

#### Shared skills
<!-- k: id=road-q-shared-skills applies=[25],[10.1.2],[10.1] sources=D-021,D-030 status=open -->
Which skills are common to every agent, and may an agent get a shared skill as a file link in its own `.claude/skills/`?

### Data and logs

#### New since the last run
<!-- k: id=road-q-new-since-last-run applies=[16.1] sources=in-20260929-1452 status=open -->
How is "new since the last run" tracked: file times, or a read cursor per agent in [16.1]?

#### Log format
<!-- k: id=road-q-log-format applies=[15],[34] sources=derived status=open -->
One JSONL log plus a Markdown summary per run? Worker logs as plain text or JSONL?

#### What may be linked
<!-- k: id=road-q-link-contract applies=[11.13] sources=D-031 status=open -->
May an agent link any file of another agent, or only files that agent lists as job outputs?

#### Promoting a worker
<!-- k: id=road-q-worker-promotion applies=[31],[14.2] sources=derived status=open -->
Should an agent-only worker move to the shared folder automatically when a second agent needs it?

### Configs and jobs

#### Config shapes
<!-- k: id=road-q-config-shape applies=[11],[27.2] sources=D-006,in-20260929-1537 status=open -->
The exact config shapes, and which settings are common and which individual (to settle with example agents).

#### Approving shared config changes
<!-- k: id=road-q-shared-config-approval applies=[10],[11.1] sources=derived status=open -->
Must a change to a shared config be approved by the owner before it reaches live agents?

#### Cloud routines
<!-- k: id=road-q-cloud-routines applies=[11.10] sources=D-029 status=open -->
Should the scheduler create cloud routines on its own, or should the owner confirm each one?

#### Routing non-agent jobs
<!-- k: id=road-q-route-name applies=[11.11] sources=D-029 status=open -->
Which name routes a skill, workflow or command job: its job id or its owner agent?

### Tests and research

#### Failing tests
<!-- k: id=road-q-failing-test applies=[49] sources=D-025 status=open -->
Does a failing test block the agent's runs, or only its promotion to live?

### Secrets

#### Where the store lives
<!-- k: id=road-q-secrets-location applies=[47] sources=D-023 status=open -->
Keep `.secrets/` at the repo root, or outside the repo (e.g. `~/.agent-os/secrets/`)?

#### Keeping the secrets index in sync
<!-- k: id=road-q-secrets-sync applies=[47.3] sources=in-20260930-0812-2 status=open -->
What triggers the index sync (a git hook, a scheduled run, the editing session), and how are live key names read without reading values?

### Docs and index

#### Index source
<!-- k: id=road-q-index-source applies=[2.18],[2.18.1] sources=D-012 status=open -->
Are the index lists written by hand, or generated from a JSON registry that the UI also reads (proposed: JSON is the source)?

#### JSON Schema
<!-- k: id=road-q-json-schema applies=[2.14] sources=derived status=open -->
Should machine-checkable JSON Schema files exist, with data-schemas.md as the readable view?

#### Tree drift
<!-- k: id=road-q-drift-check applies=[2.13] sources=derived status=open -->
Should a check compare file-tree.md with the real folders automatically?

### Apps

#### Cloned apps
<!-- k: id=road-q-apps applies=[43] sources=derived status=open -->
Pinned versions for cloned repos, and may agents clone new repos on their own?

## Changelog
- v0.2 (2026-10-07): trading parts moved to the prediction-market domain's `trading-roadmap.md` (D-056, D-058); eleven trading questions moved there whole; `road-q-copy-first` removed (copy trading leaves the tree, D-056).
- v0.1 (2026-09-30): created from file-tree.md v1.15, vision.md v0.19 and the owner inputs (D-033).
