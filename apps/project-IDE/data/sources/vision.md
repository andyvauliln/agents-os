# Agent OS: Vision notes (v0.3)

What the owner wants and why, in their terms: what the Agent OS is, what it does, the building blocks as they described them, what every agent must have, the ideas still being weighed, the principles they stated across their inputs, and the questions still open. How it is built (folders, links, configs, jobs) is in architecture.md; the decision log is decisions.md. The trading parts are in the prediction-market domain's `trading-vision-notes.md` (D-056). This is the knowledge-base copy of `docs/vision.md` [2.2]; it replaces `vision/vision.md` v0.19, whose folder layout (§7) now lives in architecture.md and file-tree.md.

## What it is
<!-- k: id=vis-what-it-is applies=[0] sources=in-20260929-1452,in-20260929-1455,D-056 status=decided -->
A personal **Agent OS**: an agentic system that runs hundreds of agents of any kind across several domains (D-056). The agents share a common base and differ by domain and configuration. The owner gives an input ("create a new agent based on this"), the system creates, runs and improves the agents like a wheel that keeps turning, and the owner watches and steers everything from a UI.

## The five things it does
<!-- k: id=vis-five-things applies=[0] sources=in-20260929-1452,D-056 status=decided -->
1. Continuously collects data from many sources.
2. Lets each agent consume only the data relevant to it.
3. Lets agents decide and act.
4. Improves the agents over time.
5. Makes it cheap to run many versions and configurations of an agent side by side and see which ones work.

## Building blocks (the owner's model)

### Workers and sub-agents
<!-- k: id=vis-block-workers applies=[14.2],[31],[10.1.1] sources=in-20260929-1452,in-20260929-1455,in-20260929-1545 status=decided -->
- Workers run periodically, as scheduled scripts or agents. They watch sources, prepare data and write it into the shared data store. Examples: an important-events collector, news, prices, errors, running a sub-agent.
- Sub-agents (worker plus AI) take data from workers and pre-analyse it for the main agents.
- The owner later said workers are just scripts, described in config (D-007). How that is built now: architecture.md `arch-jobs`.

### Data
<!-- k: id=vis-block-data applies=[16],[35] sources=in-20260929-1452,in-20260929-1455 status=decided -->
The central store of everything workers produce. For now it is JSON and Markdown files (D-005). How it is split between the system and each agent: architecture.md `arch-logs-data`.

### Agents
<!-- k: id=vis-block-strategy-agents applies=[21],[23] sources=in-20260929-1452,in-20260929-1455,D-056 status=decided -->
- Each agent belongs to a domain and is subscribed to the data it needs. It knows which data relates to it, and how and when to get it.
- It runs periodically, and each run takes all new data since the last run.
- The owner's first idea: the needed files are symlinked into the agent's folder. They kept it (D-001), as individual file links (D-020).
- Context compression is needed; how is still open (`vis-idea-compress-context`).
- A main agent is one harness, platform and model. It runs one run at a time and pulls whatever it needs from workers or sub-agents to decide.
- Every run is read data, analyse, decide, act, with the decisions listed in common/agent-architecture.md `common-agent-run-loop`.

### The agent folder (the owner's first list)
<!-- k: id=vis-block-agent-folder applies=[23] sources=in-20260929-1452,D-056 status=decided -->
One folder per agent with: config, common config, docs, logs, common prompt, agent prompt, memory, self-improvement strategy, list of workers and subscriptions, data, previous run and next runs info. Where each item lives now: architecture.md `arch-owner-list`. Still without a home: an agent's own memory and its previous and next run info (roadmap.md). The owner's list also named trading accounts, the current portfolio and analytics: they are the prediction-market domain's (its `trading-vision-notes.md`).

### Agent types
<!-- k: id=vis-agent-types applies=[10.1.1],[19.1.5],[21.1.1.1],[23] sources=in-20260929-1455,D-018,D-022,D-026,D-056 status=decided -->
The owner named three types, plus two roles inside a domain:
1. **System-support agents:** development, documentation, improvement, analysis and research of the system itself. Now sub-agents of the system level (D-026).
2. **Sub-agents (worker plus AI):** pre-analyse worker data for the main agents.
3. **Main agents:** decide and act, in test or live mode, at the levels each domain defines.
- **Main domain agent:** owns the whole domain: finds, analyses, creates and updates its agents and their self-improvement agents; makes sure the domain runs smoothly; answers the owner's questions and addresses their comments. Now the domain's own prompt [19.1.5] (D-022).
- **Self-improvement agent:** long-lived, with memory; runs from time to time on the latest logs, data, research, outside news and the owner's comments; researches when needed; dynamic per agent but built from shared templates. Now a sub-agent at every level (D-018).

## Requirements for every agent
<!-- k: id=vis-requirements applies=[10],[19],[21],[23] sources=in-20260929-1452,D-056 status=decided -->
- Has a **self-improvement strategy**, which itself can be varied and tested.
- Has a **test mode**.
- Runs with **different configurations**: personal settings, domain settings.
- Purpose: run and compare many versions, combine approaches, keep what works.
- **Shared base behaviour** for all agents, with domain-specific parts on top.

## Models and platforms (the owner's preferences)
<!-- k: id=vis-models applies=[11.11] sources=in-20260929-1455,in-20260929-1545,D-056 status=decided -->
Every AI-using object (agent, sub-agent, AI worker) gets an explicit route: "object X does these things with this platform and model". The platform/model is part of an agent's name, so agents that differ only by model can run side by side.

| Platform / model | Status | Use for |
|---|---|---|
| Claude Code, Opus 5.5, xhigh effort | default | thinking, planning, intelligent tasks, main agents, analysis, improvements |
| Claude Code, Sonnet 5.5, medium effort | supported | unimportant tasks |
| Cursor, Composer 2.5 | supported | easy jobs, data handling, light analysis, filtering; mostly workers and sub-agents; many tokens but no intelligent work |
| OpenRouter, free-model rotation | supported, not connected yet | unimportant things |
| Codex | later | |
| Kimi 3 | later | |

Where routes are configured: architecture.md `arch-routing`.

## The self-improvement wheel
<!-- k: id=vis-wheel applies=[10.1.1.1],[19.1.1.2],[21.1.1.1],[2.17.4] sources=in-20260929-1455,in-20260930-1453-2,D-056 status=decided -->
1. **Create.** The owner or the system gives an input for a new agent. The system knows how to create it and fit it in: folder, config, routing, workers, subscriptions, UI.
2. **Run.** The agent runs in test mode, on its interval and on important file changes.
3. **Analyse.** The self-improvement logic analyses the agent and researches more if needed.
4. **Reconfigure.** It makes a new configuration (or a code or prompt change) as a **new test agent**. It may change anything in the agent: config, prompts, code, model or platform.
5. **Watch the outside world.** It takes in related news, a new harness or a new model, updates the related logic and starts new agents to test the new configuration.
6. **Owner in the loop.** The owner sees everything in the UI, comments, approves going live, and stops or deletes agents.

The goal: agents that are fast, cheap, efficient, simple, understandable and better at their goal, with bugs fixed and changes tested.

## What the owner wants to see and do
<!-- k: id=vis-ui applies=[0] sources=in-20260929-1455,D-056 status=decided -->
In the UI (for monitoring and analysis of all agents and the system) the owner can:
- create a new agent from a plain input;
- see each agent's performance;
- approve or reject an agent going live; stop and delete agents;
- leave comments, ask an agent questions (answered by AI), and say what to do better;
- see an agent in full: all its parts, logs, performance, the data it uses and produces, every decision it made, and every improvement and exact change being tested.

### The File Tree page (planning explorer)
<!-- k: id=vis-explorer applies=[2.13],[10.1.2.2] sources=in-20260929-2044,in-20260930-0722,in-20260930-0744,in-20260930-0830,in-20260930-0905,in-20260930-1533,in-20260930-1841 status=decided -->
- The main document for understanding the whole system: click any folder or file to see what it is for and the rules and concepts that apply to it; a file not created yet shows its structure or an example.
- How it works is the main view: the summarised knowledge of the current system, written bottom up from files to folders to the root.
- Every message on the page is an input. A question gets an answer, and the answer is knowledge too; a requested change is drafted, shown file by file and field by field, and saved on the owner's word.
- Domain agents get an Overview tab (what the agent can do, with status, as a table the owner can add rows to) and an Agents tab (sub-agents, workers, skills).
- Search filters the tree, also by file type, and a Changed tab shows only changed files.

### Each run ends with a memory step
<!-- k: id=vis-run-memory applies=[21],[23] sources=in-20261001-1037 status=decided -->
At the end of every run an agent compresses or summarises the important information and clears what it no longer needs. It decides itself whether to continue in the same session or start a new one, what it needs each run, and whether to subscribe to more data, research or ask for a worker.

### Agents set their own triggers
<!-- k: id=vis-run-triggers applies=[21],[23],[11.10] sources=in-20261001-1037,in-20260929-1455 status=decided -->
Besides the interval and important file changes, an agent can set triggers, e.g. run again when research it started is finished; that run gets all its subscribed data plus the research.

### A limit on parallel runs
<!-- k: id=vis-parallel-limit applies=[11.1],[10.1.1] sources=in-20261001-1037 status=decided -->
The number of agents running at once is limited by the server's capacity; a system helper checks the server and sets the limit. The owner said "probably": the direction is decided, the details (where the limit lives, which helper) are open.

### What the system acts on
<!-- k: id=vis-action-scope applies=[0] sources=in-20261001-1037,D-056 status=decided -->
Every action supports test and live from the start.

### Scripts for the JSON lists
<!-- k: id=vis-json-scripts applies=[14.1] sources=in-20261001-1037 status=decided -->
Data stays in JSON files for now, so shared scripts give agents create, read, update, delete and filter operations on them.

### Every new configuration is approved
<!-- k: id=vis-approve-configs applies=[21.1.1.1] sources=in-20261001-1037,D-056 status=decided -->
When a new agent configuration is created, the owner reads a report about it and approves it; only then does it start.

## Ideas under evaluation
These came from an earlier discussion (the first brief, section 5). They are not decisions: each is weighed on its own.

### Pull instead of symlinks
<!-- k: id=vis-idea-pull applies=[16.1],[35.1] sources=in-20260929-1452,D-001,D-020,in-20261001-1037 status=open -->
Open, re-explained to the owner as problem and solution (in-20261001-1037): agents subscribe to data and keep a bookmark of how far they have read, instead of data links; shared scripts and settings stay linked. Also answers how "new since the last run" is tracked (roadmap.md `road-q-new-since-last-run`).

### Compress context upstream
<!-- k: id=vis-idea-compress-context applies=[16.3],[10.1.1] sources=in-20260929-1452,in-20261001-1037 status=proposed -->
Partly decided: each agent compresses or summarises what matters at the end of its run (D-035, `vis-run-memory`). Still proposed, re-explained to the owner: a shared digest built once for many agents, which each filters.

### External text is untrusted input
<!-- k: id=vis-idea-untrusted-text applies=[2.8] sources=in-20260929-1452,in-20261001-1037,D-056 status=open -->
Deferred: protection layers against instructions hidden in outside text (news, videos, posts) are built together with the first live actions. Proposed until then: hard limits in code, not in prompts.

### Agents use other agents' data
<!-- k: id=vis-idea-meta-agents applies=[4] sources=in-20260929-1452,in-20261001-1037,D-056 status=decided -->
Decided: agents subscribe to other agents' data. New data reaches the subscriber on its next run, or interrupts the current run when urgent. Example: a news worker or agent following X posts on a topic, whose data other agents subscribe to.

### A workers agent handles worker requests
<!-- k: id=vis-idea-worker-requests applies=[2.11.2],[2.18.2] sources=in-20260929-1452,in-20261001-1037 status=decided -->
Decided: an agent that needs data asks a workers agent, which knows how to create workers and which ones exist. It reuses existing data, extends a running worker or creates a new one, and tells the agent where the data is and when and how to use it. Agents may ask freely.

## Principles the owner stated
Rules of thumb that run through their inputs. Each points to where the rule is written out.

### Unique names that say what an agent is
<!-- k: id=vis-principle-unique-names applies=[2.18.1],[23] sources=in-20260929-1607,in-20260930-1453-2,D-012,D-032,D-056 status=decided -->
Every agent has a unique name, its ID everywhere, and the name says what the agent is. Format: conventions.md. For example, in the prediction-market domain a variant's name starts with its strategy and carries its platform/model and mode (`trading-conventions.md`).

### Everything is a file
<!-- k: id=vis-principle-files applies=[0] sources=in-20260929-1455,in-20260929-2036,in-20260930-0938,in-20260930-1153 status=decided -->
For now data is JSON and Markdown files (D-005), and everything the owner wants to see and control is a file they can open and edit: each agent's config, jobs, links, tests and research. No database yet.

### Shared things are linked, never copied, and every link says so
<!-- k: id=vis-principle-symlinks applies=name:*.link.*,name:subagents.link sources=in-20260929-1455,in-20260929-1520,in-20260929-1656,D-001,D-002,D-020 status=decided -->
Shared files reach an agent as symlinks, one per file its logic needs, chosen at creation and updated by self-improvement. Every symlinked file or folder has `.link` in its name.

### A config says what is linked, and a script keeps it true
<!-- k: id=vis-principle-links-config applies=name:*.links.json sources=in-20260930-1153,D-031 status=decided -->
Every agent layer has a config saying what is linked from where (its own level, its domain, another domain, another agent), and one script relinks the project whenever a links config changes, at review time, and when an agent edits its own. Detail: architecture.md `arch-file-links`.

### One standard folder, one template
<!-- k: id=vis-principle-one-folder applies=[10],[19],[21],[23] sources=in-20260929-1616,in-20260929-1703,in-20260930-1045,D-013,D-022,D-030 status=decided -->
The system is a domain like the others. Every level (the system, each domain and the levels each domain defines) and every agent has the identical folder, and every content folder uses the same template: its own files plus `subagents.link/` to its children.

### Parents see children, not the other way
<!-- k: id=vis-principle-parents-see-children applies=name:subagents.link sources=in-20260929-1649,in-20260930-1045,D-019,D-030 status=decided -->
Only parents link down to their children, in the order system, domains, then the levels each domain defines. For now no `.claude/` folder is linked at any level.

### Everything an agent runs is visible and switchable
<!-- k: id=vis-principle-visible-jobs applies=name:*.workers.json sources=in-20260930-0938,D-029 status=decided -->
In one config per agent the owner sees and changes every scheduled thing it runs: the schedule, on or off, where it runs (cloud or headless), platform and model, including one-off runs on a special date.

### The docs follow every input and every change
<!-- k: id=vis-principle-knowledge-flow applies=[2],[10.1.1.2] sources=in-20260929-1452,in-20260930-0812-2,in-20260930-0839,in-20260930-1533,in-20260930-1841,D-033 status=decided -->
The vision is updated after every owner input. Any edit rewrites all related things: other files, summaries, questions. Files that depend on a change (such as the secrets index) update automatically. Every input, every system change and every answer to a question goes through the knowledge agent, which keeps a many-to-many map of knowledge to files and layered How it works summaries; there are no separate Decisions, Concepts or Rules objects to maintain. Flow: docs/README.md.

### Test first, the owner approves going live
<!-- k: id=vis-principle-test-first applies=[11.1] sources=in-20260929-1455,D-056 status=decided -->
Every service that acts has a test and a live mode taken from config, and only the owner approves an agent going live. Mechanics: common/shared-mechanics.md `common-mech-modes`.

### Simple now, better later
<!-- k: id=vis-principle-simple-now applies=[0] sources=in-20260929-1537,in-20260929-2025,in-20260930-0812 status=decided -->
Start with the simplest thing that works: one global config file split later if it grows, generic placeholders now and concrete logic later, one test `.env` until it stops working. Fix a problem when it shows up instead of designing for it upfront.

## Open questions
The owner's open questions from the first brief and their second input. Answered ones say where.

### Scale and budget
<!-- k: id=vis-q-scale applies=[11.1] sources=in-20260929-1452,in-20261001-1037 status=open -->
Partly answered: the first run is the system agent and the first domain, prediction markets, with its domain agent, one strategy agent and 2-3 variants. A limit on parallel runs follows the server's capacity (`vis-parallel-limit`). Open: the AI budget.

### Stack, hosting and storage
<!-- k: id=vis-q-hosting applies=[0],[11.10] sources=in-20260929-1452,in-20260929-1455,in-20261001-1037 status=decided -->
Answered: scripts in JS/TS and Python, data as JSON and Markdown files, UI in Next.js; it runs on one of the owner's servers for now and must move easily to a bigger machine. The repo and scheduler questions that follow: roadmap.md, Repo and setup.

### Human approval and notifications
<!-- k: id=vis-q-approvals applies=[2.8],[11.1] sources=in-20260929-1452,in-20260929-1455,in-20261001-1037,D-056 status=open -->
Partly answered: the owner approves going live, can stop or delete agents, and approves every new agent configuration after reading a report on it, before it starts (D-035). Open: the notification channel.

### Autonomy to create workers and sub-agents
<!-- k: id=vis-q-autonomy applies=[2.11.2],[21.1.1.1] sources=in-20260929-1452,in-20261001-1037 status=decided -->
Answered: free for now; agents ask the workers agent for workers (`vis-idea-worker-requests`). Whether an SI sub-agent may retire the agents it made is open; for variants: the prediction-market domain's `trading-roadmap.md` `road-q-si-retire`.

### History retention
<!-- k: id=vis-q-retention applies=[15],[16] sources=in-20260929-1452,in-20261001-1037 status=decided -->
Answered: per agent. Each agent has its own back-testing plan where applicable and keeps the history that needs; each run compresses what matters (`vis-run-memory`).

### Keys
<!-- k: id=vis-q-keys applies=[47] sources=in-20260929-1452,D-023,D-027,in-20261001-1037,D-056 status=open -->
Partly answered: one store `.secrets/` with test and live kept apart, test keys in one `test/.env` agents may use, live keys owner-only. Every action supports test and live from the start. Open: how live keys are handled when that phase starts. Where the store sits: roadmap.md `road-q-secrets-location`.

### UI needs
<!-- k: id=vis-q-ui applies=[45] sources=in-20260929-1452,in-20260929-1455 status=decided -->
Answered by the owner's second input: see `vis-ui`.

### Templates for self-improvement agents
<!-- k: id=vis-q-si-templates applies=[2.17.4] sources=in-20260929-1455,D-056 status=open -->
Which exact templates are the self-improvement agents built from? First draft: common/self-improvement-templates.md, and for strategies the prediction-market domain's `common/strategy-si-templates.md`.

### How important file changes are declared
<!-- k: id=vis-q-important-files applies=name:*.workers.json sources=in-20260929-1455,D-029 status=proposed -->
Answer proposed: the `on_change` list of the agent's main-run job in its workers file (D-029), with common rules in [11.1] `triggers`. Waiting for the owner.

### OpenRouter free-model rotation
<!-- k: id=vis-q-openrouter applies=[11.11] sources=in-20260929-1455 status=open -->
What is the rotation policy for OpenRouter free models once it is connected?

### How system-support agents are scheduled and routed
<!-- k: id=vis-q-support-agents applies=[10.1.1],[11.10] sources=in-20260929-1455,D-011,D-026,D-029 status=decided -->
Answered: they are sub-agents of the system level (D-026), run as jobs in `system.workers.json` [11.10] (D-029), routed by `models.config.json` [11.11] (D-011).

## Changelog
- v0.3 (2026-10-07): trading parts moved to the prediction-market domain's `trading-vision-notes.md` (D-056, D-058): `vis-domains`, `vis-idea-strategy-instance`, `vis-idea-executor`, `vis-idea-ledger`, `vis-idea-strategy-kinds`, `vis-idea-champion-challenger`, `vis-idea-backtest-leak`, `vis-q-mvp`, `vis-q-real-money`, `vis-q-venues`, `vis-q-polymarket-suite`, `vis-q-si-scope` and `vis-q-variant-folder` moved there; the copy-trading plan removed from `vis-domains` and `vis-q-mvp`.
- v0.2 (2026-10-01): the owner's comments and answers (in-20261001-1037, D-035). This file is now the knowledge base agent's notes; the people doc is `.claude/docs/vision.md`.
- v0.1 (2026-09-30): created from file-tree.md v1.15, vision.md v0.19 and the owner inputs (D-033). Takes over `vision/vision.md` §1-6 and §8-14; §7 (folder layout and decisions) moved to architecture.md and decisions.md.
