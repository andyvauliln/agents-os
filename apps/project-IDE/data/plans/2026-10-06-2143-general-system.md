# Plan: plans for every change, features, docs at every level, and a general system

Status: approved · Request: in-20261006-2143, in-20261007-0904 · Updated: 2026-10-06

## The request

You asked for five things at once:

1. Where tests for agents and subagents are kept and how they are named.
2. A plan for every change request, stored, and after the build a decision on which logic goes where; planning as a skill that is the main way we develop.
3. Features as their own files of knowledge, mapped to the files they relate to and back, small features inside bigger ones, holding the logic that is too detailed for the overviews.
4. The vision, the README and the rebuild prompt as a hierarchy: one comes from another, they cover the system and every domain, strategy and agent, and an update low down climbs to the top.
5. A general system: "now it shouldn't be called trading oss", the top level knows nothing about trading, and agents can be anything: trading, social media, management. Each kind can have its own levels below, but every agent still has a parent.

## What it is for

The system grows by many small requests. Without a plan per request, decisions get lost between the chat and the files; without features, detailed logic has nowhere to live except long overviews; without a hierarchy of docs, a change deep down never reaches the top; and a system built only for trading cannot grow into the other kinds of agents you want. After this plan, every change has a plan, every piece of logic has one home, every level explains itself and its children, and the system is a general home for agents of any kind.

## 1. Tests for agents and subagents

**Today.** A test of an agent's instructions, of one of its helpers (subagents) or of a skill lives in the `tests/agents/` folder of the level whose `.claude/` holds it: the system's helpers in `agents/system/tests/agents/`, a domain's in its own, and so on down to each running agent. One test is one file, named by its number at that level: `t-agents-001.test.md`. Inside it says what it tests (Target), the inputs it uses (Fixtures), how to run it (in test mode, with a prompt), what a pass looks like (Expect) and how it is graded. `tests/agents/tests.config.json` lists every test of the folder with on or off, when it runs and the last result. Code tests are the same in `tests/scripts/`: `t-scripts-001.test.js`.

**The problem.** A number says nothing: you cannot tell from `t-agents-007.test.md` which agent or helper it tests.

**Proposed.** Name each test after what it tests and what it checks: `{target}.{check}.test.md`, such as `pm-self-improvement-agent.never-touches-live.test.md` or `relink.refuses-secrets.test.js`. The folder stays the same. The Tests file of the subject (`pm-self-improvement-agent.tests.json`, from the file-set plan) lists its tests, and the folder's test list is built from those Tests files.

## 2. A plan for every change request

**Decided by you, written now.** Every change request gets a plan before it is built. The plan is stored; after the build, its logic is moved to where it belongs and the plan is archived. Later changes update the knowledge in the files it went to.

**The skill.** `change-plan` is drafted (`vision/.claude/skills/change-plan/SKILL.md`): when a plan is needed, where plans live (`plans/`, one file per request named by date and subject, an index, an archive), the statuses (draft, waiting, approved, building, built, distributed, archived, or dropped), the outline every plan follows (this plan follows it), the steps from request to archive, and the rules. It is the main development skill: every AI that changes the system uses it.

**Where it stands.** This plan is the first written with it. `file-set.md`, `github-sync.md` and `server-ide.md` are older plans and keep their names.

## 3. Features as their own knowledge

**The idea.** A feature is one thing the system can do, such as "jobs and the scheduler", "links between agents" or "every file explains itself". Its file holds the whole logic of that thing: how it works end to end, its rules, formats, flows, examples, edge cases and open questions. That is the detail that is too much for a How it works file, a view, the README or the rebuild prompt, which describe the feature in short and point to it.

**Where.** A `features/` folder in the `docs/` of the system and of every agent. The system's features are what every agent shares; a domain's are its own, and so on down.

**Shape.** One feature per file, `features/<feature-name>.md`, with its family files like any other file. A big feature includes its small ones: `jobs-and-scheduler.md` sums up and points to `jobs-file.md`, `scheduler.md` and `run-job.md`, and each small one names its parent.

**The map, both ways.** Each feature's Details file lists the files it relates to and how (reads, writes, defines, uses), its parent and its children. Each file's Details file lists the features it belongs to. One side is written by hand, the feature's; the other is built from it by the build script, so the two never disagree.

**What it replaces.** The feature-map table and, over time, the sections of the topic notes that describe one feature in detail. The file-set plan, once built, becomes the feature `every-file-explains-itself.md` (name proposed) instead of a topic note.

## 4. The three docs at every level, as one hierarchy

**Inside a level.** The vision comes first; the README follows from it and describes every part; the rebuild prompt follows from the README and gives every exact detail.

**Across levels.** Every agent at every level has its own three docs. A parent's docs describe it in general and sum up each child in a few lines, with the path to the child's docs; a child's docs start from the parent and describe only what is its own. The system's docs speak about the system in general and every domain; a domain's about itself and its strategies; a strategy's about itself and its running agents.

**Updates climb.** When a level's docs change, its parent's are checked and updated, up to the system, each time in the order vision, README, rebuild prompt. The system's rebuild prompt covers the system's own parts and lists the children's rebuild prompts in build order, so the whole thing can be rebuilt from the top.

**What it adds.** A rebuild prompt for every domain, strategy and running agent, next to the README and vision their `docs/` folders already list. The three doc skills and the knowledge base agent get the climb rule.

## 5. A general system, not a trading OS

**Decided by you.** The system is not a trading OS. Its top level knows nothing about trading: it runs agents of any kind, such as trading, social media or management. Each kind can have its own levels below, and every agent has a parent. For trading, the levels below a domain are strategies and running agents; other kinds can have other levels.

**The name.** You name it. Until then the docs say "the system". The GitHub repository can keep its name `trading-oss` until you rename it there.

**Kinds as a level (proposed).** Each kind of agent gets its own folder under `agents/`, holding what all its domains share, the same way the system holds what everyone shares:

```text
agents/
├── system/                     the system: runs and improves agents of any kind
├── trading/                    the trading kind: what every trading domain shares
│   ├── prediction-market-agents/    a domain
│   │   └── strategy-1-agent/        a strategy
│   │       └── pm-strategy-1.momentum-v1.opus55-test/   a running agent
│   └── copy-trading-agents/
└── social-media/               another kind, with its own levels later
```

Every folder keeps the standard agent folder. A kind says in its settings which levels it has below it.

**What stays in the system (general).** The standard folder, jobs and the scheduler, workers and data, links, keys, test and live modes for any action that reaches the outside world, logs, tests, research, self-improvement, the knowledge base, the project IDE, the server and the AI models.

**What moves to the trading kind.** Strategies and variations that compete on profit, money safety (accounts with real money, risk limits, the stop switch for orders), the shared buy, sell and risk-check scripts, the trading research and everything about Polymarket. The system keeps a general rule that any agent acting live needs the owner's approval; the trading kind adds the money rules on top.

**The docs.** The system's vision, README and rebuild prompt are rewritten in general terms; the trading kind gets its own three docs, which carry today's trading vision.

## Choices for you

1. **The name of the system.** Until you name it, the docs say "the system".
2. **Kinds as a folder level** (recommended) or only a label in each domain's settings. A level gives the shared trading parts a home; a label keeps the tree flatter, but then the shared trading parts have nowhere to live but the system.
3. **Test names** `{target}.{check}.test.md` (recommended) or numbers as today.
4. **Order of work** as below (recommended).

## Steps

1. ✓ Finish the planning skill: add it to the agents' rules and the tree, start `plans/index.json` with this plan and the three older ones. Check: the skill is on the File Tree page and the index lists four plans.
2. Build the file set (`file-set.md`), which waits for your pick on its card. Check: as in that plan.
3. Restructure into a general system: the kinds level, the moves, the name. Check: no file at the system level talks about trading, `build_map.py` reports no problem, every link still resolves.
4. Build the features layer: `features/` at the system and in every agent's docs, the first features cut from the topic notes and the feature map, the two-way map. Check: every feature has a parent or is top level, every file's Details lists its features.
5. Rewrite the three docs at every level as one hierarchy, which also carries the general-system rewrite, so the docs are rewritten once. Check: each level's three docs exist, each parent sums up its children, and the climb rule is in the skills.
6. Distribute and archive this plan.

## What it touches

The system's `CLAUDE.md`, both helper agents, the skills `knowledge-intake`, `file-index`, `vision-doc`, `readme-doc`, `rebuild-prompt-doc` and the new `change-plan`; the conventions, data formats, flows and feature-map notes; every level's `docs/`; the whole `agents/` tree for the kinds level; the build scripts and the page; the vision, README and rebuild prompt.

## Where the knowledge goes once built

- **Planning:** the skill `change-plan`; the rule in the system's `CLAUDE.md`; one sentence in the README's knowledge base part; the rebuild prompt's knowledge base part.
- **Test names:** the conventions note's tests section and the data formats note; the rebuild prompt.
- **Features:** a feature of its own about features; the conventions note for where they live; the How it works skill for the map; the README in short.
- **Docs hierarchy:** the three doc skills and the knowledge base agent; the README's knowledge base part in short.
- **General system:** the system's three docs and the trading kind's three docs; the conventions note for kinds and levels; the tree notes; the rebuild prompt in full.

## Log

- 2026-10-06 21:43: request received.
- 2026-10-06 21:50: plan drafted; the planning skill drafted; the planning rule written into the system's `CLAUDE.md`.
- 2026-10-06 22:03: step 1 done: the skill and the plans folder are in the tree and on the File Tree page, `plans/index.json` lists four plans, and the vision, the README and the rebuild prompt carry the planning rule. Waiting for your choices.
- 2026-10-07 09:01: part of step 5 done early, on your question "why agents didn't got a rebuild-prompt?": every domain, strategy and trading agent lists its own rebuild prompt in the tree, and the trading agent its own vision; the rebuild prompt skill says every level has one. Writing them stays in step 5.
- 2026-10-07 09:04: your go ("you can continue with a plan"), with the name Agent OS and no kind folder: trading goes into the prediction-market domain, later trading domains are copied from it. The work follows `2026-10-07-0904-agent-os.md`.
- 2026-10-07: step 3 done by plan `2026-10-07-0904-agent-os` (no kinds level: trading lives in the prediction-market domain, the name is the Agent OS, D-056, D-058); step 2 done in part (empty Details files, D-057); step 5 started with the system's vision as the example.
