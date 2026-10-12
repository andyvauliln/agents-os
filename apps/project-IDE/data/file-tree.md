# Agent OS: File tree (v1.34)

> Skeleton of the folder layout from the owner's v0.2 input (see `vision.md` §7). Every object is numbered. We will go through them one by one: the owner answers the open questions and this file is updated. Names in `[brackets]` are placeholders. One example agent (`pm-strategy-1.momentum-v1.opus55-test`, named per D-012) is fully expanded. "Momentum" is only a placeholder modification name.

## 1. Tree

```text
agent-os/                                   # [0] repo/workspace root
├── .gitignore                                # [48] ignores secrets, local Claude settings/memory, build junk; each entry commented (D-028)
├── .secrets/                                 # [47] SECRETS STORE (D-023): git-ignored, chmod 700, outside agents/
│   ├── test/                                 # [47.1] test keys
│   │   └── .env                              # [47.1.1] ALL test keys in one file, sections + prefixed names (D-027); agents may read/update it
│   ├── live/                                 # [47.2] live keys, only for agents the owner approved for live
│   │   └── .env                              # [47.2.1] same keys, live values; owner only; later phase (D-027)
│   └── secrets.index.json                    # [47.3] metadata only (ref, kind, env, used by, rotate_by); never values
├── README.md                                 # [1] the front page for people: what this is and where to start
├── agents/                                   # [4] all domains; every child is a domain (system is one)
│   ├── system/                               # [10] SYSTEM-LEVEL AGENT (standard folder [2.7.1]) + shared files + subagents.link/ to each domain (D-030)
│   │   ├── .claude/                          # [10.1] system-domain Claude Code
│   │   │   ├── CLAUDE.md                     # [10.1.5] read first by every Claude: the project's rules, read order and rounds, and the system manager prompt (D-024; took over the root CLAUDE.md, D-045)
│   │   │   ├── settings.json                 # [10.1.6] permissions (deny .secrets/live/**, D-027), hooks, env, model, statusLine, outputStyle; committed
│   │   │   ├── settings.local.json           # [10.1.7] personal overrides; git-ignored
│   │   │   ├── rules/                        # [10.1.8] topic rules; `paths:` frontmatter; subfolders ok
│   │   │   │   └── [topic].md
│   │   │   ├── skills/                       # [10.1.2] skills: one folder each
│   │   │   │   ├── knowledge-intake/SKILL.md # [10.1.2.1] one input or change -> stored, placed in the docs, rippled, recorded (D-033)
│   │   │   │   ├── file-index/SKILL.md       # [10.1.2.2] How it works of every file and folder, one [name].index.md each, children first (D-033, D-039, D-057)
│   │   │   │   ├── vision-doc/SKILL.md       # [10.1.2.3] how to write vision.md, the top-level doc, the same sections at every level (D-034, D-048)
│   │   │   │   ├── readme-doc/SKILL.md       # [10.1.2.4] how to write README.md, every part exactly with the path to its docs (D-034, D-048)
│   │   │   │   ├── rebuild-prompt-doc/SKILL.md # [10.1.2.7] how to write rebuild-prompt.md, the spec an AI rebuilds the system from (D-048)
│   │   │   │   ├── change-plan/SKILL.md      # [10.1.2.8] a plan for every change request: write, show, build, move its knowledge home, archive (D-051)
│   │   │   │   ├── ide-build/                # [10.1.2.5] builds the File Tree page from the repo, checks it and publishes it; its scripts live inside it (D-041)
│   │   │   │   │   ├── SKILL.md              # [10.1.2.5.1] the steps: parse, enrich, map, test, publish
│   │   │   │   │   └── scripts/              # [10.1.2.5.2] the build scripts (Python, standard library only) and a page check
│   │   │   │   │       ├── README.md         # [10.1.2.5.2.1] what each script does and how to run them
│   │   │   │   │       ├── parse.py          # [10.1.2.5.2.2] reads the tree notes [2.13] into a list of items
│   │   │   │   │       ├── enrich.py         # [10.1.2.5.2.3] adds drafts, examples, knowledge, How it works and tabs; writes the page data [53.1.2]
│   │   │   │   │       ├── tabs.py           # [10.1.2.5.2.4] the field guides and extra tabs (settings fields, jobs, links, tests, key names)
│   │   │   │   │       ├── build_map.py      # [10.1.2.5.2.5] the knowledge map [2.18.8]; finds stale or orphaned How it works files, writes and confirms them
│   │   │   │   │       ├── index_files.py    # [10.1.2.5.2.6] where each .index.md and .meta.json lives; reads and writes them
│   │   │   │   │       └── check_page.js     # [10.1.2.5.2.7] smoke test of the page on a desktop and a phone width before publishing
│   │   │   │   ├── ide-sync/SKILL.md         # [10.1.2.6] the way back from the page: notes, edits and requests -> files, metadata, views (D-041)
│   │   │   │   └── [skill-name]/SKILL.md     # + supporting files
│   │   │   ├── commands/                     # [10.1.9] single-file prompts, /name
│   │   │   │   └── [command-name].md
│   │   │   ├── agents/                       # [10.1.1] sub-agents (own context/tools)
│   │   │   │   ├── sys-self-improvement-agent.md # [10.1.1.1] self-improvement sub-agent, this level (D-018)
│   │   │   │   ├── knowledge-base-agent.md   # [10.1.1.2] knowledge base agent: keeps every input and change in its notes, writes the docs for people (D-034; was sys-knowledge-agent, D-033)
│   │   │   │   └── project-ide-agent.md      # [10.1.1.3] looks after the IDE [53]: builds the page from the repo, turns page notes and edits into file changes, runs page requests (D-041)
│   │   │   ├── workflows/                    # [10.1.10] workflow scripts; each becomes /<name>
│   │   │   │   └── [workflow-name].js
│   │   │   ├── output-styles/                # [10.1.11]
│   │   │   │   └── [style-name].md
│   │   │   ├── agent-memory/                 # [10.1.12] `memory: project` sub-agent memory (incl. SI)
│   │   │   │   └── [subagent-name]/MEMORY.md
│   │   │   └── agent-memory-local/           # [10.1.13] `memory: local`; git-ignored
│   │   ├── docs/                             # [2] SHARED DOCS (D-017): the vision, the README and the rebuild prompt (D-047, D-048), the topic docs agents read + subagents.link/ (D-030)
│   │   │   ├── vision.md                     # [2.2] the top-level doc, read first: why, the concept, how it should work, the business logic, examples (D-034, D-048)
│   │   │   ├── README.md                     # [2.1] every part of the system exactly, how the parts connect, and the path to each part's own docs; read after the vision (D-034, D-048)
│   │   │   ├── rebuild-prompt.md             # [2.22] the prompt an AI follows to rebuild the whole system the same: the tree, names, formats, build order, checks (D-048)
│   │   │   ├── inputs-vision.md              # [2.23] every owner requirement from all inputs, newest wins, by scope, in ASD-STE100 (D-062)
│   │   │   ├── overview.md                   # [2.3] how the whole OS works, with diagrams
│   │   │   ├── architecture.md               # [2.21] how it is built: levels, folders, links, jobs, configs (D-033)
│   │   │   ├── glossary.md                   # [2.4] shared vocabulary for owner and agents
│   │   │   ├── roadmap.md                    # [2.5] phases, current focus, next steps
│   │   │   ├── conventions.md                # [2.7] naming (incl. .link rule), formats, config keys
│   │   │   ├── safety.md                     # [2.8] hard limits, secrets, approval to go live
│   │   │   ├── feature-map.md                # [2.12] feature/logic area -> files that implement it
│   │   │   ├── data-schemas.md               # [2.14] shape of every JSON/MD file
│   │   │   ├── flows.md                      # [2.15] data flows + user (owner) flows
│   │   │   ├── metrics.md                    # [2.16] how agents are measured and compared, going live
│   │   │   ├── how-to/                       # [2.11] step-by-step runbooks
│   │   │   │   ├── create-agent.md           # [2.11.1] create + integrate a new agent
│   │   │   │   ├── add-worker.md             # [2.11.2] add a worker/sub-agent + subscriptions
│   │   │   │   ├── add-platform-or-model.md  # [2.11.3] add/route a platform or model
│   │   │   │   ├── promote-to-live.md        # [2.11.4] test -> live with owner approval
│   │   │   │   ├── stop-or-delete-agent.md   # [2.11.5] stop, retire, delete an agent
│   │   │   │   ├── add-account-or-secret.md  # [2.11.6] add a key or account (D-023, D-027)
│   │   │   │   ├── add-or-run-tests.md       # [2.11.7] add, enable or run a test (D-025)
│   │   │   │   ├── record-research.md        # [2.11.8] record a research item (D-025)
│   │   │   │   ├── add-or-change-link.md     # [2.11.9] link a file from anywhere, then relink (D-031)
│   │   │   │   └── process-an-input.md       # [2.11.10] owner input or change -> knowledge base (D-033)
│   │   │   ├── common/                       # [2.17] common knowledge shared by all agents
│   │   │   │   ├── agent-architecture.md     # [2.17.1] how agents work inside (was [7])
│   │   │   │   ├── shared-mechanics.md       # [2.17.2] triggers, modes, symlinks, run loop, logs (was [9])
│   │   │   │   ├── common-prompt.md          # [2.17.3] base prompt every agent's CLAUDE.md builds on
│   │   │   │   └── self-improvement-templates.md     # [2.17.4] base templates for every level's self-improvement agent
│   │   │   ├── index/                        # [2.18] index of all things (was catalog [8])
│   │   │   │   ├── agents.md                 # [2.18.1] every agent: type, domain, route, mode, status
│   │   │   │   ├── workers.md                # [2.18.2] every worker: source, schedule, output, subscribers
│   │   │   │   ├── subagents.md              # [2.18.3] every sub-agent: input, output, route
│   │   │   │   ├── services.md               # [2.18.4] every acting service: test/live, credentials
│   │   │   │   ├── apps.md                   # [2.18.5] every cloned repo in apps/
│   │   │   │   ├── models.md                 # [2.18.6] platforms, models, status, who routes to them
│   │   │   │   └── links.md                  # [2.18.7] every file link: agent, where, from, why (D-031)
│   │   │   └── subagents.link/               # [2.20] one folder link per domain (D-030)
│   │   │       └── [domain-name]/            # [2.20.1] -> that domain's docs/ [19.6]
│   │   ├── configs/                          # [11] shared configs (JSON) + subagents.link/ (D-030)
│   │   │   ├── system.config.json            # [11.1] global: defaults, modes (incl. the general stop switch), schedules, triggers, notifications
│   │   │   ├── system.workers.json           # [11.10] system's own jobs: when, where it runs, platform, model (D-029; was workers.config.json)
│   │   │   ├── models.config.json            # [11.11] platforms + which model each agent/sub-agent/worker uses
│   │   │   ├── system.links.json             # [11.13] system's own file links: what, from where (D-031; format for every level)
│   │   │   └── subagents.link/               # [11.2] one folder link per domain (D-030)
│   │   │       └── [domain-name]/            # [11.2.1] -> that domain's configs/ [19.2], incl. its workers file
│   │   ├── scripts/                          # [14] shared scripts; kind by folder + suffix; + subagents.link/
│   │   │   ├── system/                       # [14.1] *.system.*: create-agent, run-agent, scheduler, run-job, relink, check-links, notifier, run-tests
│   │   │   ├── workers/                      # [14.2] *.worker.*: shared data collectors
│   │   │   └── subagents.link/               # [14.4] one folder link per domain (D-030)
│   │   │       └── [domain-name]/            # [14.4.1] -> that domain's scripts/ [19.3]
│   │   ├── logs/                             # [15] shared logs by source + subagents.link/ (D-030)
│   │   │   ├── system/                       # [15.1] scheduler, triggers, relink + link checks, errors, costs
│   │   │   ├── services/[service]/           # [15.2] acting services (test/live actions)
│   │   │   ├── workers/[worker]/             # [15.3] shared worker runs
│   │   │   ├── subagents/[subagent]/         # [15.4] sub-agent calls
│   │   │   └── subagents.link/               # [15.5] one folder link per domain (D-030)
│   │   │       └── [domain-name]/            # [15.5.1] -> that domain's logs/ [19.4]
│   │   ├── data/                             # [16] shared data by source + subagents.link/ (D-030)
│   │   │   ├── system/                       # [16.1] registry, run state, read cursors, links index (D-031)
│   │   │   ├── workers/[worker]/             # [16.2] shared worker outputs
│   │   │   ├── subagents/[subagent]/         # [16.3] sub-agent outputs
│   │   │   └── subagents.link/               # [16.4] one folder link per domain (D-030)
│   │   │       └── [domain-name]/            # [16.4.1] -> that domain's data/ [19.5]
│   │   ├── tests/                            # [10.8] system tests (D-025); run by run-tests [14.1]
│   │   │   ├── agents/                       # [10.8.1] tests of the prompt + sub-agents (LLM behaviour)
│   │   │   │   ├── tests.config.json         # [10.8.1.1] every agent test: enabled, last_run, last_result, next_action
│   │   │   │   ├── [test-id].test.md         # [10.8.1.2] scenario, fixtures, expected behaviour
│   │   │   │   └── run-tests.system.link.js  # [10.8.1.3] -> [14.1] run-tests; runs this folder's tests.config.json (--kind agents preset)
│   │   │   ├── scripts/                      # [10.8.2] tests of scripts
│   │   │   │   ├── tests.config.json         # [10.8.2.1] every script test (same fields)
│   │   │   │   ├── [test-id].test.[js|py]    # [10.8.2.2]
│   │   │   │   └── run-tests.system.link.js  # [10.8.2.3] -> [14.1] run-tests; runs this folder's tests.config.json (--kind scripts preset)
│   │   │   └── subagents.link/               # [10.8.3] one folder link per domain (D-030)
│   │   │       └── [domain-name]/            # [10.8.3.1] -> that domain's tests/ [19.12]
│   │   ├── research/                         # [10.9] system research history (D-025)
│   │   │   ├── index.json                    # [10.9.1] every item: question, status, results, decisions, links
│   │   │   ├── [research-id]-[slug]/         # [10.9.2] one folder per item: README.md + artifacts
│   │   │   └── subagents.link/               # [10.9.3] one folder link per domain (D-030)
│   │   │       └── [domain-name]/            # [10.9.3.1] -> that domain's research/ [19.13]
│   │   ├── package.json                      # [10.4] JS deps (shared scripts)
│   │   ├── requirements.txt                  # [10.5] Python deps (shared scripts)
│   │   ├── init.sh                           # [10.6] installs the git hooks, runs relink for the whole project (D-031)
│   │   ├── start.sh                          # [10.7] starts the scheduler (all jobs, D-029) + system session
│   └── trading/                              # [56] TRADING: a folder of trading domains, with trading's own docs (owner, D-059)
│       ├── researches/                       # [56.2] EXISTS: the research studies, moved here from the repo's top-level researches/ (owner, 2026-10-09, D-061)
│       │   ├── prediction-market-research/   # [54.1] EXISTS: about 57 studies of prediction-market strategies, their evidence, and the pipeline that wrote them
│       │   ├── self-improving-agents/        # [54.2] EXISTS: study: approaches and architectures for agents that improve themselves
│       │   └── trding-agents-arhiteches/     # [54.3] EXISTS: study: trading agent architectures: specs, diagrams, a page
│       ├── docs/                             # [56.1] trading's own docs for people
│       │   ├── README.md                     # [56.1.1] every part of trading exactly: its domains and where each part's docs are
│       │   ├── vision.md                     # [56.1.2] why trading, what all trading domains share, how a new one is made
│       │   └── rebuild-prompt.md             # [56.1.3] how an AI builds trading's folder again; lists its domains' prompts in order
│       └── prediction-market/                # [19] DOMAIN-LEVEL AGENT (standard folder [2.7.1]), moved into trading/ (D-059)
│           ├── .claude/                          # [19.1] domain-level Claude Code
│           │   ├── CLAUDE.md                     # [19.1.5] DOMAIN OWNER prompt (was [19.7]) (D-024: inside .claude/)
│           │   ├── settings.json                 # [19.1.6] permissions (deny .secrets/live/**, D-027), hooks, env, model, statusLine, outputStyle; committed
│           │   ├── settings.local.json           # [19.1.7] personal overrides; git-ignored
│           │   ├── rules/                        # [19.1.8] topic rules; `paths:` frontmatter; subfolders ok
│           │   │   └── [topic].md
│           │   ├── skills/                       # [19.1.2] skills: one folder each
│           │   │   └── [skill-name]/SKILL.md     # + supporting files
│           │   ├── commands/                     # [19.1.9] single-file prompts, /name
│           │   │   └── [command-name].md
│           │   ├── agents/                       # [19.1.1] sub-agents (own context/tools)
│           │   │   ├── pm-self-improvement-agent.md # [19.1.1.2] self-improvement sub-agent, this level (D-018)
│           │   │   └── [subagent-name].md
│           │   ├── workflows/                    # [19.1.10] workflow scripts; each becomes /<name>
│           │   │   └── [workflow-name].js
│           │   ├── output-styles/                # [19.1.11]
│           │   │   └── [style-name].md
│           │   ├── agent-memory/                 # [19.1.12] `memory: project` sub-agent memory (incl. SI)
│           │   │   └── [subagent-name]/MEMORY.md
│           │   └── agent-memory-local/           # [19.1.13] `memory: local`; git-ignored
│           ├── configs/                          # [19.2] domain config + file links
│           │   ├── prediction-market-agents.config.json # [19.2.4] domain settings: risk limits, trading accounts, venues, fees, market filters, currency, the order stop switch, trade notifications (D-058)
│           │   ├── prediction-market-agents.workers.json # [19.2.1] domain jobs: when, where it runs, platform, model (D-029)
│           │   ├── prediction-market-agents.links.json   # [19.2.3] domain file links: what, from where (D-031)
│           │   └── subagents.link/               # [19.2.2] one folder link per strategy agent (D-030)
│           │       └── [agent-name]/             # [19.2.2.1] -> that strategy's configs/ [21.2]
│           ├── scripts/                          # [19.3] domain scripts + file links
│           │   ├── markets-catalog.worker.py     # [19.3.3] domain worker: catalogue of the markets the domain trades -> data/markets-catalog/ (job in [19.2.1])
│           │   ├── decisions/                    # [14.3] *.decision.*: shared buy/sell/risk-check blocks for every trading agent (moved from the system, number kept, D-058)
│           │   ├── polymarket-prices.worker.py   # [19.3.5] domain worker: Polymarket prices -> data/polymarket-prices/ (job in [19.2.1]; was the system's shared-worker example, D-058)
│           │   ├── relink.system.link.js         # [19.3.2] -> [14.1] relink; relinks this agent (D-031)
│           │   └── subagents.link/               # [19.3.1] one folder link per strategy agent (D-030)
│           │       └── [agent-name]/             # [19.3.1.1] -> that strategy's scripts/ [21.3]
│           ├── logs/                             # [19.4] domain session + domain SI logs
│           │   ├── jobs/[job-id]/                # [19.4.2] run logs of the domain's jobs: history.jsonl + latest.log (D-058)
│           │   ├── services/[service]/           # [19.4.3] acting services' order logs (test/live), the source of every PnL number (D-058)
│           │   └── subagents.link/               # [19.4.1] one folder link per strategy agent (D-030)
│           │       └── [agent-name]/             # [19.4.1.1] -> that strategy's logs/ [21.4]
│           ├── data/                             # [19.5] domain data + file links
│           │   ├── markets-catalog/              # [19.5.2] latest.json from [19.3.3]; strategies and variants link it (@domain)
│           │   ├── polymarket-prices/            # [19.5.3] latest.json + dated files from [19.3.5]; trading agents link it (@domain, D-058)
│           │   └── subagents.link/               # [19.5.1] one folder link per strategy agent (D-030)
│           │       └── [agent-name]/             # [19.5.1.1] -> that strategy's data/ [21.5]
│           ├── docs/                             # [19.6] domain docs + file links
│           │   ├── README.md                     # [19.6.2] every part of the domain exactly, with the path to each part's docs (D-034, D-048)
│           │   ├── vision.md                     # [19.6.3] the domain's own vision: why it, how it makes money, examples (D-034, D-048)
│           │   ├── rebuild-prompt.md             # [19.6.4] how an AI builds the domain's own folder again exactly (D-053)
│           │   ├── trading-overview.md           # [19.6.5] the trading layer of the overview: run loop with orders, strategy loop (D-058)
│           │   ├── trading-architecture.md       # [19.6.6] strategy and trading-agent levels, variants
│           │   ├── trading-conventions.md        # [19.6.7] strategy and variant names, account ids, decision scripts, trading config fields
│           │   ├── trading-safety.md             # [19.6.8] money rules: live gate with accounts, risk limits, order stop switch, positions on stop
│           │   ├── trading-data-schemas.md       # [19.6.9] domain config, trading fields, decisions, order log, positions, metrics snapshot
│           │   ├── trading-flows.md              # [19.6.10] decision to execution, strategy loop, promote with money, stop with positions
│           │   ├── trading-metrics.md            # [19.6.11] PnL, win rate, drawdown, calibration, promotion thresholds
│           │   ├── trading-glossary.md           # [19.6.12] trading words: strategy, variant, champion and challenger, funded account, PnL
│           │   ├── trading-roadmap.md            # [19.6.13] strategies, venues, live trading, trading open questions
│           │   ├── trading-feature-map.md        # [19.6.14] trading features -> files that implement them
│           │   ├── doc-outlines.md               # [19.6.15] outlines and lengths of the strategy and trading-agent docs
│           │   ├── common/                       # [19.6.16] trading knowledge every trading agent shares
│           │   │   ├── trading-agent-architecture.md # [19.6.16.1] run loop with buy, sell, sell all; positions; memory across variants
│           │   │   ├── trading-prompt.md         # [19.6.16.2] the trading layer of the common prompt
│           │   │   └── strategy-si-templates.md  # [19.6.16.3] templates the self-improvement agents build strategies from
│           │   ├── how-to/                       # [19.6.17] trading runbooks
│           │   │   ├── create-strategy-or-variant.md # [19.6.17.1] create a strategy or a variant
│           │   │   ├── go-live-with-money.md     # [19.6.17.2] test -> live with a funded account and the owner's approval
│           │   │   ├── add-trading-account.md    # [19.6.17.3] add a trading account and its keys
│           │   │   └── stop-trading-agent.md     # [19.6.17.4] stop a trading agent: close positions, unfund the account
│           │   ├── index/                        # [19.6.18] the domain's own lists
│           │   │   └── accounts.md               # [19.6.18.1] every trading account: venue, funded, approved by the owner, capital, used by
│           │   └── subagents.link/               # [19.6.1] one folder link per strategy agent (D-030)
│           │       └── [agent-name]/             # [19.6.1.1] -> that strategy's docs/ [21.6]
│           ├── tests/                            # [19.12] domain tests (D-025); run by run-tests [14.1]
│           │   ├── agents/                       # [19.12.1] tests of the prompt + sub-agents (LLM behaviour)
│           │   │   ├── tests.config.json         # [19.12.1.1] every agent test: enabled, last_run, last_result, next_action
│           │   │   ├── [test-id].test.md         # [19.12.1.2] scenario, fixtures, expected behaviour
│           │   │   └── run-tests.system.link.js  # [19.12.1.3] -> [14.1] run-tests; runs this folder's tests.config.json (--kind agents preset)
│           │   ├── scripts/                      # [19.12.2] tests of scripts
│           │   │   ├── tests.config.json         # [19.12.2.1] every script test (same fields)
│           │   │   ├── [test-id].test.[js|py]    # [19.12.2.2]
│           │   │   └── run-tests.system.link.js  # [19.12.2.3] -> [14.1] run-tests; runs this folder's tests.config.json (--kind scripts preset)
│           │   └── subagents.link/               # [19.12.3] one folder link per strategy agent (D-030)
│           │       └── [agent-name]/             # [19.12.3.1] -> that strategy's tests/ [21.12]
│           ├── research/                         # [19.13] domain research history (D-025)
│           │   ├── index.json                    # [19.13.1] every item: question, status, results, decisions, links
│           │   ├── [research-id]-[slug]/         # [19.13.2] one folder per item: README.md + artifacts
│           │   └── subagents.link/               # [19.13.3] one folder link per strategy agent (D-030)
│           │       └── [agent-name]/             # [19.13.3.1] -> that strategy's research/ [21.13]
│           ├── package.json                      # [19.8]
│           ├── requirements.txt                  # [19.9]
│           ├── init.sh                           # [19.10] setup; runs relink for this agent (D-031)
│           ├── start.sh                          # [19.11] starts the domain session
│           └── strategy-1-agent/                 # [21] STRATEGY-LEVEL AGENT (standard folder [2.7.1])
│               ├── .claude/                      # [21.1] strategy-level Claude Code
│               │   ├── CLAUDE.md                 # [21.1.5] STRATEGY MANAGER prompt (was [21.7]) (D-024: inside .claude/)
│               │   ├── settings.json             # [21.1.6] permissions (deny .secrets/live/**, D-027), hooks, env, model, statusLine, outputStyle; committed
│               │   ├── settings.local.json       # [21.1.7] personal overrides; git-ignored
│               │   ├── rules/                    # [21.1.8] topic rules; `paths:` frontmatter; subfolders ok
│               │   │   └── [topic].md
│               │   ├── skills/                   # [21.1.2] skills: one folder each
│               │   │   └── [skill-name]/SKILL.md # + supporting files
│               │   ├── commands/                 # [21.1.9] single-file prompts, /name
│               │   │   └── [command-name].md
│               │   ├── agents/                   # [21.1.1] sub-agents (own context/tools)
│               │   │   ├── pm-strategy-1-self-improvement-agent.md # [21.1.1.1] self-improvement sub-agent, this level (D-018)
│               │   │   └── [subagent-name].md
│               │   ├── workflows/                # [21.1.10] workflow scripts; each becomes /<name>
│               │   │   └── [workflow-name].js
│               │   ├── output-styles/            # [21.1.11]
│               │   │   └── [style-name].md
│               │   ├── agent-memory/             # [21.1.12] `memory: project` sub-agent memory (incl. SI)
│               │   │   └── [subagent-name]/MEMORY.md
│               │   └── agent-memory-local/       # [21.1.13] `memory: local`; git-ignored
│               ├── configs/                      # [21.2] strategy config + file links
│               │   ├── strategy-1-agent.workers.json # [21.2.1] strategy jobs, e.g. the strategy session and its SI run (D-029)
│               │   ├── strategy-1-agent.links.json   # [21.2.3] strategy file links: what, from where (D-031)
│               │   └── subagents.link/           # [21.2.2] one folder link per trading agent (D-030)
│               │       └── [agent-name]/         # [21.2.2.1] -> that agent's configs/ [27]
│               ├── scripts/                      # [21.3] strategy scripts + file links
│               │   ├── relink.system.link.js     # [21.3.2] -> [14.1] relink; relinks this agent (D-031)
│               │   └── subagents.link/           # [21.3.1] one folder link per trading agent (D-030)
│               │       └── [agent-name]/         # [21.3.1.1] -> that agent's scripts/ [30]
│               ├── logs/                         # [21.4] strategy session + strategy SI logs
│               │   └── subagents.link/           # [21.4.1] one folder link per trading agent (D-030)
│               │       └── [agent-name]/         # [21.4.1.1] -> that agent's logs/ [34]
│               ├── data/                         # [21.5] strategy data: cross-variant history
│               │   └── subagents.link/           # [21.5.1] one folder link per trading agent (D-030)
│               │       └── [agent-name]/         # [21.5.1.1] -> that agent's data/ [35]
│               ├── docs/                         # [21.6] strategy definition, docs + file links
│               │   ├── README.md                 # [21.6.2] every part of the strategy exactly, with the path to each part's docs (D-034, D-048)
│               │   ├── vision.md                 # [21.6.3] the strategy's own vision: why it, how it makes money, examples (D-034, D-048)
│               │   ├── rebuild-prompt.md         # [21.6.4] how an AI builds the strategy's own folder again exactly (D-053)
│               │   └── subagents.link/           # [21.6.1] one folder link per trading agent (D-030)
│               │       └── [agent-name]/         # [21.6.1.1] -> that agent's docs/ [46]
│               ├── tests/                        # [21.12] strategy tests (D-025); run by run-tests [14.1]
│               │   ├── agents/                   # [21.12.1] tests of the prompt + sub-agents (LLM behaviour)
│               │   │   ├── tests.config.json     # [21.12.1.1] every agent test: enabled, last_run, last_result, next_action
│               │   │   ├── [test-id].test.md     # [21.12.1.2] scenario, fixtures, expected behaviour
│               │   │   └── run-tests.system.link.js # [21.12.1.3] -> [14.1] run-tests; runs this folder's tests.config.json (--kind agents preset)
│               │   ├── scripts/                  # [21.12.2] tests of scripts
│               │   │   ├── tests.config.json     # [21.12.2.1] every script test (same fields)
│               │   │   ├── [test-id].test.[js|py] # [21.12.2.2]
│               │   │   └── run-tests.system.link.js # [21.12.2.3] -> [14.1] run-tests; runs this folder's tests.config.json (--kind scripts preset)
│               │   └── subagents.link/           # [21.12.3] one folder link per trading agent (D-030)
│               │       └── [agent-name]/         # [21.12.3.1] -> that agent's tests/ [49]
│               ├── research/                     # [21.13] strategy research history (D-025)
│               │   ├── index.json                # [21.13.1] every item: question, status, results, decisions, links
│               │   ├── [research-id]-[slug]/     # [21.13.2] one folder per item: README.md + artifacts
│               │   └── subagents.link/           # [21.13.3] one folder link per trading agent (D-030)
│               │       └── [agent-name]/         # [21.13.3.1] -> that agent's research/ [50]
│               ├── package.json                  # [21.8]
│               ├── requirements.txt              # [21.9]
│               ├── init.sh                       # [21.10] setup; runs relink for this agent (D-031)
│               ├── start.sh                      # [21.11] starts the strategy session
│               └── pm-strategy-1.momentum-v1.opus55-test/       # [23] EXAMPLE variant of strategy 1 (standard folder [2.7.1])
│                   ├── .claude/                            # [24] agent-level Claude Code (own files only; no .claude links, D-030)
│                   │   ├── CLAUDE.md                       # [24.5] trading agent prompt (was [37]) (D-024: inside .claude/)
│                   │   ├── settings.json                   # [24.6] permissions (deny .secrets/live/**, D-027), hooks, env, model, statusLine, outputStyle; committed
│                   │   ├── settings.local.json             # [24.7] personal overrides; git-ignored
│                   │   ├── rules/                          # [24.8] topic rules; `paths:` frontmatter; subfolders ok
│                   │   │   └── [topic].md
│                   │   ├── skills/                         # [25] skills: one folder each
│                   │   │   └── [skill-name]/SKILL.md       # + supporting files
│                   │   ├── commands/                       # [24.9] single-file prompts, /name
│                   │   │   └── [command-name].md
│                   │   ├── agents/                         # [26] sub-agents (own context/tools)
│                   │   │   └── [subagent-name].md
│                   │   ├── workflows/                      # [24.10] workflow scripts; each becomes /<name>
│                   │   │   └── [workflow-name].js
│                   │   ├── output-styles/                  # [24.11]
│                   │   │   └── [style-name].md
│                   │   ├── agent-memory/                   # [24.12] `memory: project` sub-agent memory (incl. SI)
│                   │   │   └── [subagent-name]/MEMORY.md
│                   │   └── agent-memory-local/             # [24.13] `memory: local`; git-ignored
│                   ├── configs/                            # [27] own configs + file links
│                   │   ├── pm-strategy-1.momentum-v1.opus55-test.config.json  # [27.2] own config: mode, risk, strategy
│                   │   ├── pm-strategy-1.momentum-v1.opus55-test.workers.json # [27.4] own jobs: main run, workers, one-off jobs (D-029)
│                   │   ├── pm-strategy-1.momentum-v1.opus55-test.links.json   # [27.3] own file links: what, from where (D-031; was the `links` section of [27.2])
│                   │   ├── system.config.link.json         # [27.1] -> [11.1] system/configs/system.config.json
│                   │   ├── prediction-market-agents.config.link.json # [27.1] -> [19.2.4] its domain's config (@domain, D-058)
│                   │   └── models.config.link.json         # [27.1] -> [11.11] system/configs/models.config.json
│                   ├── scripts/                            # [30] own scripts + file links; kind in suffix
│                   │   ├── get-polymarket-data.worker.py   # [31] worker: fetch market data
│                   │   ├── clean-data.system.js            # [32] system script: clean/normalise
│                   │   ├── make-buy.decision.js            # [33] decision script (buy/sell)
│                   │   ├── risk-check.decision.link.js     # [30.1] -> [14.3] its domain's scripts/decisions/risk-check.decision.js (@domain)
│                   │   ├── relink.system.link.js           # [30.3] -> [14.1] relink; the agent reruns it after editing its links file (D-031)
│                   │   └── run-tests.system.link.js        # [30.2] -> [14.1] system/scripts/system/run-tests.system.js (D-025)
│                   ├── logs/                               # [34] own logs + file links (only if needed)
│                   │   ├── runs.jsonl                      # own run log, one line per run
│                   │   ├── run-[date].md                   # one readable report per run
│                   │   ├── polymarket-prices.worker.link.log  # [34.1] -> [19.4.2] its domain's logs/jobs/polymarket-prices/latest.log (@domain)
│                   │   └── tests.jsonl                     # [34.2] one line per test run (D-025)
│                   ├── data/                               # [35] own data + file links
│                   │   ├── get-polymarket-data/            # [35.2] own outputs, one folder per producer
│                   │   ├── polymarket-prices.link.json     # [35.1] -> [19.5.3] its domain's data/polymarket-prices/latest.json (@domain)
│                   │   ├── news-digest.link.md             # [35.1] -> [16.3] system/data/subagents/news-digest/latest.md
│                   │   └── markets-catalog.link.json       # [35.1] -> [19.5] its domain's data/markets-catalog/latest.json (@domain, D-031)
│                   ├── docs/                               # [46] own docs + file links
│                   │   ├── README.md                           # [46.2] what it is, its parent variant, route and mode
│                   │   ├── strategy.md                         # [46.5] its strategy in plain words
│                   │   ├── changes.md                          # [46.6] exactly what differs from its parent and what is being tested
│                   │   ├── decisions.md                        # [46.7] a summary of its notable decisions
│                   │   ├── notes.md                            # [46.8] the owner's comments and the answers
│                   │   ├── vision.md                           # [46.3] what the agent tests and why, results so far, what comes next (D-034, D-053)
│                   │   ├── rebuild-prompt.md                   # [46.4] how an AI builds this agent's folder again exactly (D-053)
│                   │   ├── safety.link.md                  # [46.1] -> [2.8] system/docs/safety.md
│                   │   ├── agent-architecture.link.md      # [46.1] -> [2.17.1] system/docs/common/agent-architecture.md
│                   │   ├── trading-safety.link.md          # [46.1] -> [19.6.8] its domain's docs/trading-safety.md (@domain, D-058)
│                   │   └── trading-agent-architecture.link.md # [46.1] -> [19.6.16.1] its domain's docs/common/trading-agent-architecture.md (@domain, D-058)
│                   ├── tests/                              # [49] agent tests (D-025); run by run-tests [14.1]
│                   │   ├── agents/                         # [49.1] tests of the prompt + sub-agents (LLM behaviour)
│                   │   │   ├── tests.config.json           # [49.1.1] every agent test: enabled, last_run, last_result, next_action
│                   │   │   ├── [test-id].test.md           # [49.1.2] scenario, fixtures, expected behaviour
│                   │   │   └── run-tests.system.link.js    # [49.1.3] -> [14.1] run-tests; runs this folder's tests.config.json (--kind agents preset)
│                   │   └── scripts/                        # [49.2] tests of scripts
│                   │       ├── tests.config.json           # [49.2.1] every script test (same fields)
│                   │       ├── [test-id].test.[js|py]      # [49.2.2]
│                   │       └── run-tests.system.link.js    # [49.2.3] -> [14.1] run-tests; runs this folder's tests.config.json (--kind scripts preset)
│                   ├── research/                           # [50] agent research history (D-025)
│                   │   ├── index.json                      # [50.1] every item: question, status, results, decisions, links
│                   │   └── [research-id]-[slug]/           # [50.2] one folder per item: README.md + artifacts
│                   ├── package.json                        # [38] JS deps + npm scripts
│                   ├── requirements.txt                    # [39] Python deps
│                   ├── init.sh                             # [40] setup; runs relink for this agent (D-031)
│                   └── start.sh                            # [41] start one run / the scheduler
└── apps/                                     # [43] applications: our own, such as the project IDE; apps we use, forked from GitHub; research clones in temp/ (D-055)
    ├── project-IDE/                          # [53] the owner's IDE: the File Tree page and everything it needs (owner, D-041)
    │   ├── docs/                             # [53.4] the app's own docs, like every app's (D-055)
    │   │   ├── vision.md                     # [53.4.1] what the IDE is for and why
    │   │   ├── README.md                     # [53.4.2] its parts and where they are
    │   │   └── rebuild-prompt.md             # [53.4.3] how to build it again exactly
    │   ├── current-ui/                       # [53.1] the page the owner uses now, published on claude.ai
    │   │   ├── file-tree-explorer.html       # [53.1.1] the page: tree, tabs, edits, notes, questions
    │   │   └── file-tree.data.json           # [53.1.2] the page's data; built by ide-build, never edited or merged by hand
    │   ├── server/                           # [53.3] the page on the owner's server, with Claude Code behind its request box (D-042, D-043)
    │   │   ├── README.md                     # [53.3.1] how to start it and reach it safely
    │   │   ├── server.py                     # [53.3.2] serves the page from the repository, keeps page notes as files, writes edits into files, runs requests
    │   │   ├── claude_bridge.py              # [53.3.3] runs each request as a Claude Code session started in agents/system/ and streams it to the page
    │   │   ├── voice.py                      # [53.3.5] turns a voice recording from the page into text through Groq, switching models on limits (D-060)
    │   │   └── server.config.json            # [53.3.4] address, model, what Claude Code may do, what waits for the owner's click, the voice models
    │   └── data/                             # [53.2] this project's knowledge and the data the page is built from
    │       ├── README.md                     # [53.2.1] how the knowledge is kept: layers, knowledge tags, the flow (was the knowledge base guide)
    │       ├── file-tree.md                  # [2.13] this document: the tree notes, annotated tree + one section per object (was [6])
    │       ├── decisions.md                  # [2.6] decision log: what was decided, why, when
    │       ├── changelog.md                  # [2.9] what changed, when and why
    │       ├── inputs/                       # [2.10] every owner input, verbatim and categorised (D-033)
    │       │   ├── README.md                 # [2.10.3] how the archive works; the categories
    │       │   ├── index.json                # [2.10.2] one row per input: categories, summary, what it changed
    │       │   └── YYYY-MM-DD-HHMM-[topic].md # [2.10.1] one raw input per file
    │       ├── knowledge-map.json            # [2.18.8] which knowledge applies to which file or folder; built by build_map.py (D-033)
    │       ├── sources/                      # [53.2.2] the notes behind each people doc: what every part rests on
    │       │   └── [doc].md                  # [53.2.2.1] one file per people doc
    │       ├── page-store/                   # [53.2.7] on the server: the page's notes, edits and messages, one JSON file each (D-043)
    │       ├── overrides.json                # [53.2.3] the owner's page edits kept in the page data, by object number
    │       ├── memory/                       # [53.2.4] working notes for every Claude: how the owner wants us to work, what is open
    │       │   └── [note].md                 # [53.2.4.1] one note per file; MEMORY.md is the index
    │       ├── plans/                        # [53.2.5] one plan per change request, an index, and older plans (D-051)
    │       │   └── [plan].md                 # [53.2.5.1] one plan per file, YYYY-MM-DD-HHMM-<subject>.md
    │       └── archive/                      # [53.2.6] retired files, one folder per date
    │           └── [date]/                   # [53.2.6.1] everything retired that day
    ├── temp/                                 # [55] research clones: each one's repo/ never committed, its docs/ only when asked (D-055)
    └── trading-ui/                           # [45] the prediction-market domain's dashboard (Next.js API + UI): empty for now, maybe never needed (owner, D-045)
```

Note: the shared docs [2] now live in the system domain at `agents/system/docs/` (D-017); section numbers [2.x] are kept, and `docs/…` below means that folder. The owner's input first placed `vision.md` under top-level `docs/` [2.2]. Everything under `docs/` other than `vision.md` is **proposed**, except where the owner asked for it (feature-map, file-tree, data-schemas, flows, metrics, common, index, per-agent docs). This file is `docs/file-tree.md` [2.13]. `agents/docs/` [5] was merged into it; the top-level `docs/` was then moved into the system domain (D-017). **Every symlinked file or folder has `.link` in its name** (owner rule, see [2.7]); `A -> B` in the tree means A is a symlink to B. **Layout rule (D-013–D-016):** `agents/` holds domains only, and `system/` is one of them. Every agent has the same folders (`configs/`, `scripts/`, `logs/`, `data/`); each holds the agent's own files plus **individual file links** to only the files its logic needs (D-020). Each agent lists those links in its own `configs/[name].links.json`, and the shared `relink` script builds them (D-031). The system domain holds shared files. Every level's content folders also hold `subagents.link/[child-name]/` folder links to its direct children's folders of the same kind (D-030, [2.7.4]); `.claude/` folders are not linked. The current working copies live in `/mnt/project-files/vision/` (the knowledge base, D-033) until the tree exists. **Repo layout (owner, D-041, D-045):** the repository is this tree: the root `README.md` [1], `agents/` exactly as below (the owner agreed the tree as it stands), and `apps/` [43] with the owner's IDE `apps/project-IDE/` [53] (the File Tree page and this project's knowledge; moved into `apps/`, owner 2026-10-05 15:17) and the trading dashboard `apps/trading-ui/` [45]. There is no root `CLAUDE.md` (the rules every Claude reads first are in the system's `.claude/CLAUDE.md` [10.1.5]) and no root `researches/` (the studies sit in the agents' own research folders) (owner, 2026-10-06). The tree lists only real files, not examples of names (owner, 2026-10-06). Every file and folder gets its `.index.md` next to it (D-039); a file nobody has written yet exists only as its index file, and a placeholder such as `[agent-name]/` is a folder holding only its index file.

## 2. Objects

Each object lists its **purpose**, **contents**, **writers / readers** and **open questions**.

### [0] `agent-os/` (root)
- **Purpose:** the workspace holding the whole OS.
- **Contents:** the objects below.
- **Writers / readers:** owner, system-support agents.
- **One repository (owner, D-041):** the GitHub repository is this tree: `README.md` [1], `agents/` [4], `apps/` [43] (with `apps/project-IDE/` [53] and `apps/trading-ui/` [45] inside), plus `.gitignore` [48]; no root `CLAUDE.md` and no root `researches/` (owner, 2026-10-06, D-045); `.secrets/` [47] stays on the machine and out of git. Which GitHub project it goes into, the owner gives next.
- **Open:** Where does it run (local machine, VPS)? Is `apps/` part of the repository or cloned next to it?

### [1] `README.md`
- **Purpose:** entry point for humans and agents: what the OS is and where things are.
- **Contents:** short summary, links to the docs for people ([2.1], [2.2] in the system's `docs/` [2], D-047), the IDE [53] and the shared docs [2], how to start the system/UI. The file for agents is the system's `.claude/CLAUDE.md` [10.1.5] (D-045).
- **Writers / readers:** system-support agents write it. Everyone reads it.
- **Draft (owner edit on the page, 2026-09-30):**
  ```markdown
  # Agent OS
  An agentic trading system: workers collect data, agents at system / domain / strategy level decide and self-improve, and a UI lets the owner watch and approve.

  - Start here: agents/system/.claude/docs/README.md
  - Vision: agents/system/.claude/docs/vision.md
  - File tree: apps/project-IDE/ (the File Tree page and its data)
  - Run: ./agents/system/start.sh   UI: cd trading-ui && npm run dev
  ```
- **Owner (2026-09-30):** "for now let it be like this, later we'll figure out better format and self update mechanics". Keeping it current is the knowledge agent's job (D-033).
- **Resolved (D-041, D-045):** it does not double as the file for agents; that is [10.1.5] in the system's `.claude/`.
- **Path (D-045):** the dashboard is now `apps/trading-ui/` [45], so the draft's `cd trading-ui` becomes `cd apps/trading-ui` when the README is next written (the owner's draft is left as they wrote it).
- **Paths (D-041):** the owner's draft above points at the new places: `agents/system/.claude/docs/README.md`, `agents/system/.claude/docs/vision.md` and `apps/project-IDE/` for the file tree.
- **Paths (D-047):** README and vision are now `agents/system/docs/README.md` and `agents/system/docs/vision.md`; the draft's two `.claude/docs/` lines change when the README is next written (left as they are until then).
- **Order (D-048):** the vision is read first and the README after it, so "Start here" points to the vision when the front page is next written (the owner's draft is left as they wrote it until then).
- **Agent OS (D-056, D-058):** the draft's title follows the new name. When the front page is next written, its first line describes the system in general terms (a system that runs AI agents of any kind), trading is named as the prediction-market domain's, and the dashboard line points to `apps/trading-ui/` [45] as that domain's app (the owner's draft is left as they wrote it until then).
- **Open:** better format later (owner).

### [51] (retired: the `[name].index.md` pattern leaves the tree, owner 2026-10-06, D-045)
- **Why:** the tree lists only real files, not examples of names (owner: "it just also example we don't need it in a tree right now only files that will be in a system").
- **The rule stays (D-039):** every file and folder has its How it works file next to it (a file `vision.md`: `vision.index.md`, named without its extension since D-057; a folder `f/`: `f/f.index.md`), with an empty Details file of the same name ending `.meta.json` beside it, and the page shows each as its own row. Its format, where it goes and how it is written are in the `file-index` skill [10.1.2.2]; where each one lives while we plan, in `index_files.py` [10.1.2.5.2.6].

### [52] (retired: no root `CLAUDE.md`; it moved into the system's `.claude/` as [10.1.5], owner 2026-10-06, D-045)
- **Owner (2026-10-06):** "we right now keep CLAUDE.md inside .claude folder no top level CLAUDE".

### [2] `agents/system/docs/` (moved from top-level `docs/` by D-017; numbers kept)
- **Purpose:** the shared docs of the whole OS (self-support logic), living in the system domain like the other shared folders (`configs/`, `scripts/`, `logs/`, `data/`). This is the first place any agent or person reads to understand the system.
- **Pattern (D-017, same as D-014/D-015; links per D-020):** shared docs are real files here; every agent has its own real `docs/` [46] with individual file links [46.1] to the shared docs it needs; and [2.20] `subagents.link/` holds one folder link per domain's `docs/` (D-030); each domain's docs link on to its strategies' and each strategy's to its agents', so every agent's docs can be reached from here.
- **Scope:** vision, how it works, rules, decisions, roadmap, runbooks, schemas, flows, metrics, common agent knowledge [2.17], the index of all things [2.18], and the links to each domain's docs [2.20].
- **Repo root:** `README.md` [1] only; the file for agents is the system's `.claude/CLAUDE.md` [10.1.5] (D-041, D-045). **Root `docs/`? No strong reason to keep it.** Repo-level dev docs (how to work on this repo) fit here too, e.g. in `how-to/`. The one caveat is that some tools look for docs at the root (GitHub shows the root README; Claude Code loads a root `CLAUDE.md`), and a short root `README.md` covers that.
- **Docs for people here (owner, 2026-10-06, D-047):** an agent keeps no docs inside its `.claude/`; its `.claude/docs/` moved one level up into its own `docs/`. So [2.1] README and [2.2] vision, and the others as each is rewritten for people, sit in this folder next to the topic docs agents read.
- **The three main docs (owner, 2026-10-06, D-048):** [2.2] the vision is the top-level doc, read first; [2.1] the README goes deeper, part by part, with the path to each part's own docs; [2.22] the rebuild prompt is the spec an AI rebuilds the same system from. They are kept in that order every round.
- **Split (D-041, D-047):** the docs for people are here; the records of how the project got here ([2.10] inputs, [2.6] decisions, [2.9] changelog, [2.13] the tree notes, [2.18.8] the knowledge map) are in `apps/project-IDE/data/` [53.2]. This folder keeps the topic docs agents read while they work. Their numbers are kept.
- **Knowledge base (D-033):** together these folders are the system's knowledge base, in layers: every owner input [2.10]; one file doc per object in [2.13]; topic docs for knowledge shared by many files ([2.3], [2.21], [2.15], [2.14], [2.7], [2.8], [2.4], [2.16], [2.5], [2.11], [2.17]); history ([2.6], [2.9]); and the index [2.18] with the knowledge map [2.18.8] (which knowledge applies to which file or folder, many to many) and the How it works of every file and folder, each in its own `[name].index.md` (D-039), written bottom up. The format and the flow are in [2.1]. The planning copy lives in `/mnt/project-files/vision/docs/` until the repo exists.
- **Writers / readers:** the owner gives inputs; the knowledge agent [10.1.1.2] `sys-knowledge-agent` (D-033; was `sys-docs-agent`, D-026) files every input and every system change into these files with its skills [10.1.2.1] and [10.1.2.2]. All agents read them through [46.1] (read-only); the UI reads them here.
- **Contents:** [2.2] vision, [2.1] README and [2.22] the rebuild prompt (D-047, D-048), [2.3]–[2.5], [2.7], [2.8], [2.11], [2.12], [2.14]–[2.18], [2.20], [2.21]; [2.6], [2.9], [2.10], [2.13], [2.18.8] in [53.2] (D-041). ([2.19] retired.)
- **Format:** Markdown only (vision §10). Every file starts with a title and version, and ends with a changelog.
- **Open (proposed):** when a doc for people is written on a topic whose agent notes already sit here under the same name (architecture, glossary), the notes move to the sources [53.2.2] so the name is free.

### [2.1] `docs/README.md` (D-034, D-041, D-047, D-048; was `.claude/docs/README.md`, and before that the knowledge base guide, D-033)
- **Purpose (owner, 2026-10-06, D-048):** the full, long overview of how the whole system works, read after the vision for a deeper and exact understanding, by people and by AI. It describes every main part of the system (what it is, what it holds, what it takes and gives, when and where it runs) and gives the path to each part's own docs. It never describes the logic inside an agent. Owner: "README suppose to be full long docs with a overview how it works all system, to read for deeper and exact understanding how system works good for human and for ai, it should not contain also information about any logic inside the agents, but should have just descriptional view on all main parts of the system with a provided paths to the main documentation README for specific part of the sytem".
- **Outline:** the sections of the README skill [10.1.2.4] (In short · The system at a glance · How the project is laid out · The parts, one per main part, each ending with "Its docs" · Where each part's docs are · Still open in the design); the page shows them as the Example.
- **Writers / readers:** the knowledge base agent [10.1.1.2] with the README skill, after the vision and before the rebuild prompt in every round that touches a part; the owner can edit it on the page. Readers come to it from the vision; every agent reads it before working on a part it does not know.
- **Updated:** after every input, answer or change that touches a part of the system (the raw input goes to [2.10] first). "Still open in the design" and the table of docs are checked every time.
- **Where (D-047):** in the system's `docs/` [2] with the other docs for people (moved up from `.claude/docs/`).
- **Root README [1]:** stays a short front page; the README skill keeps its first paragraph in line with "In short".
- **Draft:** `/mnt/project-files/vision/.claude/docs/README.md` (the planning copy keeps its place; it goes to `agents/system/docs/` at the GitHub sync). The earlier guide to the knowledge base (layers, tag format, the input flow) is now [53.2.1], drafted in `vision/docs/README.md`.

### [2.2] `docs/vision.md` (D-034, D-041, D-047, D-048; was `.claude/docs/vision.md`, and before that [3])
- **Purpose (owner, 2026-10-06, D-048):** the top-level doc, read first, from which the reader goes deeper: what we are building and why, the concept, ideas, how it should work, the business logic and worked examples, then where we are and what is open. Mostly for people, and every agent reads it for the high-level view. Owner: "vision yes like mostly for human but also for ai for high level view, ideas concept examples, busness logic, what we are bulding how it should works. So vision it's top level document, from where after we go deeper to have better understanding how things works."
- **Outline:** the sections of the vision skill [10.1.2.3] (In short · Why we are building it · The concept · How it should work · The business logic · Examples · What the owner sees and does · Where we are and what comes next · Principles · Ideas we are still weighing · Open questions · Going deeper); the page shows them as the Example. It names no folders or files; its last section points to the README [2.1].
- **Writers / readers:** the knowledge base agent [10.1.1.2] with the vision skill, first of the three main docs in every round that touches it; the owner can edit it on the page. Everyone reads it first; all agents may read it.
- **Updated:** after each owner input that touches the goals, the concept, how the system should work, the business logic, the plans, a principle, an idea or an open question (the raw input goes to [2.10] first).
- **Where (D-047):** in the system's `docs/` [2] (moved up from `.claude/docs/`).
- **Draft:** `/mnt/project-files/vision/.claude/docs/vision.md` (planning copy; it goes to `agents/system/docs/` at the GitHub sync); the earlier technical version is the agent's notes in `vision/docs/vision.md`, which go with the sources [53.2.2] in the repo.

### [2.22] `docs/rebuild-prompt.md` (owner, 2026-10-06, D-048)
- **Purpose:** a prompt for an AI coding agent such as Claude Code: given only this file and an empty repository, it rebuilds the Agent OS and ends with the same working system (the same tree, names, formats, scripts, agents and helpers, safety rules and project IDE). It is the full and exact spec of the system as designed today. Owner: "let's make one more document it ll be prompt for ai, from what we can rebuild the system that at the end we have same working system".
- **Outline:** the sections of its skill [10.1.2.7] (Your task · The system in brief · Ground rules · The repository tree · Conventions · The parts · Build order · Acceptance checks · Do not build); the page shows them as the Example.
- **Writers / readers:** the knowledge base agent [10.1.1.2] with its skill, last of the three main docs after every change to the system's design. An AI agent reads it to rebuild the system or check it against its spec; the owner reads it to check.
- **Rules:** written for AI: instructions, exact paths and formats; no reference numbers, decision codes or history; never a secret value; decided things are built, our proposals are built and marked as defaults, ideas and open questions are listed under "Do not build".
- **Name and place (proposed):** the name `rebuild-prompt.md` and its place next to the vision and the README are our defaults. Every level has its own (owner, D-053): every domain [19.6.4], strategy [21.6.4] and trading agent [46.4], and every app [53.4.3] (D-055). A lower level's prompt builds only its own folder, assumes the levels above exist, and lists its children's prompts in build order; the system's lists the domains' and the apps'.
- **Draft:** `/mnt/project-files/vision/.claude/docs/rebuild-prompt.md` (planning copy; it goes to `agents/system/docs/` at the GitHub sync).

### [2.23] `docs/inputs-vision.md` (owner, 2026-10-09, D-062)
- **Purpose:** a detailed overview of the project made only from the owner's inputs: repeated points once, overruled points left out, the newest input wins. Divided by scope of logic (system, levels, common file rules, configs, jobs, runs, self-improvement, modes, tests, models, trading, docs and knowledge, project IDE, apps, approvals, open subjects). Written in ASD-STE100 (Simplified Technical English), one rule per line with a code such as `FILE-01`.
- **Writers / readers:** the knowledge base agent [10.1.1.2] updates it after every owner input that changes how the system should be. People and AI read it for the owner's wishes; the vision, README and rebuild prompt are checked against it.
- **Rules:** only the owner's words, never Claude's defaults or proposals; no key values.
- **Draft:** `/mnt/project-files/vision/.claude/docs/inputs-vision.md` (planning copy; it goes to `agents/system/docs/` at the GitHub sync).

### [2.3] `docs/overview.md` (D-041; today's `overview.md`)
- **Purpose:** how the whole OS works end to end: the "how" behind the vision, with diagrams.
- **Outline:** The idea in one paragraph · Components (workers, data, agents, self-improvement, UI, platforms) · Data flow · Agent run loop and triggers · Self-improvement wheel · Test vs live · Where things live (links to [2.13], [2.15]).
- **Writers / readers:** knowledge agent writes it. New agents and the owner read it.
- **Updated:** when vision or architecture changes. Agent-internal detail belongs in [2.17.1], not here.

### [2.4] `docs/glossary.md` (D-041)
- **Purpose:** one meaning per term, so the owner, agents and the UI use the same words.
- **Outline:** alphabetical terms. Seed list: agent, main agent, main domain agent, sub-agent, worker, system-support agent, self-improvement agent, strategy, modification/variant, domain, platform, model, route, test mode, live mode, run, trigger, important file, subscription, champion/challenger.
- **Writers / readers:** knowledge agent writes it. Everyone reads it.
- **Updated:** when a new term appears in inputs or docs.

### [2.5] `docs/roadmap.md` (D-041)
- **Purpose:** what is built now, next and later; keeps agents working on the right thing.
- **Outline:** Current phase and goal · Now (in progress) · Next · Later (e.g. Codex, Kimi 3, OpenRouter connection, more domains) · Done.
- **Writers / readers:** the owner sets priorities; main domain agents and the knowledge agent update status. System-support agents read it before choosing work.
- **Updated:** when priorities change or an item is finished.

### [2.6] `apps/project-IDE/data/decisions.md` (D-041; number kept)
- **Purpose:** append-only log of decisions, so settled questions are not reopened and agents know why things are as they are.
- **Outline:** one entry per decision: ID and date · Decision · Why · Alternatives considered · Source (link to [2.10] input or vision question) · Status (active/superseded).
- **Writers / readers:** the knowledge agent [10.1.1.2] records owner decisions (knowledge-intake, step 6). System-support and self-improvement agents may add proposals marked "pending owner". Everyone reads it.
- **Updated:** each time an open question is resolved (e.g. every "[resolved]" mark in vision §6).
- **Where (D-041):** with the project's other records in `apps/project-IDE/data/` [53.2].
- **The log (D-033):** `/mnt/project-files/vision/docs/decisions.md`, one entry per decision from D-001 on with date, decision, why, status (active, partly superseded, superseded) and the inputs it came from. It is history: the rules a decision made live in the topic docs, which point back to it.

### [2.7] `docs/conventions.md` (D-033: rules moved to the doc)
- **Purpose:** the rules that make hundreds of agents consistent and machine-readable. The rules themselves live in `docs/conventions.md`, each section tagged with the files and folders it applies to; this section only describes the file.
- **Sections:** agent names (unique IDs, versions, clones, no renames; the strategy and variant name formats are the prediction-market domain's [19.6.7], D-058) · the `.link` naming rule and file links · script kinds · per-agent config files · **[2.7.1]** standard agent folder · **[2.7.2]** standard `.claude/` folder · **[2.7.3]** tests and research at every level · **[2.7.4]** content folders and child links · **[2.7.5]** links file per agent · where a new file goes · docs · git · open questions. The numbers [2.7.1] to [2.7.5] are kept as section names so older references still find them.
- **Writers / readers:** the knowledge agent [10.1.1.2] writes it (knowledge-intake); every agent that creates files, names agents or adds links reads it; `create-agent` and `relink` [14.1] enforce parts of it.
- **Updated:** when the owner decides or changes a rule; the decision goes to [2.6], the rule here.

### [2.8] `docs/safety.md` (D-041)
- **Purpose:** the rules no agent may break: outside actions, keys and approvals. The money rules are the prediction-market domain's [19.6.8] (D-058).
- **Outline:** Test vs live (every acting service reads its mode from config) · Approval to go live (only the owner) · Hard limits enforced in code, a lower level may only tighten them · The general stop switch · **Secrets and wallets (D-023, D-027):** stored only in [47] `.secrets/`, one `.env` per mode (test, live); configs name the keys they need in `secret_keys`; loaded by scripts at execution time via `load-secret` [14.1], never in LLM context, prompts, docs, data or logs; never linked into agent folders; only the owner adds live keys (proposed); rotation rules · External text is untrusted · What self-improvement may change without approval · Stop/kill switch.
- **Writers / readers:** the owner decides; the knowledge agent writes it down. Every agent reads it; executors and risk checks implement it.
- **Updated:** only on explicit owner decision.

### [2.9] `apps/project-IDE/data/changelog.md` (D-041; number kept)
- **Purpose:** system-level history: what changed in the OS, when and why (not per-agent changes, which stay in agent folders/logs).
- **Outline:** reverse-chronological entries: Date · Change · Area (docs, system, domain, UI, routing) · Link to decision/input.
- **Writers / readers:** the knowledge base agent [10.1.1.2] adds an entry for every round (knowledge-intake); system-support agents append entries. The owner and the UI read it.
- **Updated:** on every system-level change.
- **Where (D-041):** with the project's other records in `apps/project-IDE/data/` [53.2].
- **Draft:** `/mnt/project-files/vision/docs/changelog.md`.

### [2.10] `apps/project-IDE/data/inputs/` (D-033, D-041; number kept)
- **Purpose:** every owner input, word for word, from any channel (project chat, threads, comments on files, the File Tree page), so nothing the owner said is lost and every doc can say where its knowledge came from.
- **Contents:** [2.10.1] `YYYY-MM-DD-HHMM-[topic].md`, one input per file: header (id `in-YYYYMMDD-HHMM`, time, channel, categories, one-line summary), the raw text unchanged, then "Processed into" (decisions, docs and [n] objects it changed). [2.10.2] `index.json`: one row per input with categories (setup, vision, structure, agents, configs, links, workers-jobs, docs-knowledge, secrets-safety, tests-research, naming, ui, process, question), summary and `processed_into`; the knowledge map reads it. [2.10.3] `README.md`: how the archive works.
- **Writers / readers:** the knowledge agent saves each input on receipt (knowledge-intake, step 1) and never edits the raw text. Messages sent on the File Tree page wait in the page's `inputs` store until the next sync. Agents read the archive when a summary is unclear.
- **Updated:** on every owner input.
- **Where (D-041):** with the project's other records in `apps/project-IDE/data/` [53.2]; the IDE is where most inputs now arrive.
- **Draft:** `/mnt/project-files/vision/docs/inputs/` (69 inputs so far, 2026-09-29 to 2026-10-05).

### [2.11] `docs/how-to/` (D-041)
- **Purpose:** step-by-step runbooks that agents (and the owner) follow for recurring operations. These are what makes "create a new agent based on this input" repeatable (vision §13).
- **Contents:**
  - [2.11.1] `create-agent.md` (same steps for any new agent, D-022; a strategy or variant adds the steps of [19.6.17.1], D-058): input → pick the domain and the parent → name per [2.7] and check it is unique in [2.18.1] (D-012) → scaffold the standard agent folder (`.claude/`, `configs/`, `scripts/`, `logs/`, `data/`, `docs/`, `tests/` with two empty `tests.config.json` and a runner link `run-tests.system.link.js` next to each, `research/` with an empty `index.json`; D-025) → write its own config [27.2] → write its links file `[agent-name].links.json` [27.3] with the file links its logic needs, plus the default `scripts/relink.system.link.js` (D-031) → run `init.sh` [40], which runs `relink` (its file links + its entries in the parent's `subagents.link/` folders, D-030) → scaffold its `docs/` [46] (README, changes; a trading agent also strategy) → set its route in [11.11] `models.config.json` → write its jobs file `[agent-name].workers.json` [27.4] (at least the main run; its parent sees it through `configs/subagents.link/`, D-030) → test mode → `run-tests` passes [2.11.7] → register in index [2.18] and UI → first run.
  - [2.11.2] `add-worker.md`: check existing workers/data first (index [2.18.2]) → write the script (shared [14.2] or agent-local [30]) → add it as a job to the owning agent's workers file (shared workers: [11.10] `system.workers.json`; otherwise the agent's own, e.g. [27.4]; D-029) with schedule, where it runs, platform and model → mark its output as `on_change` for agents that must restart on it → add the data file link to each reader's links file [27.3]; relink runs on the change (D-031).
  - [2.11.3] `add-platform-or-model.md`: add to [11.11] `models.config.json` → set status (supported/later) → route objects → test run.
  - [2.11.4] `promote-to-live.md`: criteria (incl. all enabled tests passing, `before_promote` tests run; D-025, proposed) → owner approval in UI → switch mode → monitoring; a trading agent also needs a funded account ([19.6.17.2], D-058).
  - [2.11.6] `add-account-or-secret.md` (D-023, proposed): owner creates the key → adds a `KEY=value` line (prefixed per account/platform) to [47.1] `test/.env`, or for live the owner adds it to [47.2] `live/.env` (chmod 600; D-027) → adds metadata to [47.3] → adds the key names to [11.11] `platforms` or to the domain's accounts (the prediction-market domain: [19.2.4] `accounts`, runbook [19.6.17.3]; live: owner approval) and to that agent's `secret_keys` → test run with test keys → `check-links` passes. Rotation: replace the value under the same key name, update `rotate_by`, delete the old key at the provider.
  - [2.11.7] `add-or-run-tests.md` (D-025, proposed): pick the level and kind (`agents` for prompt/sub-agent behaviour, `scripts` for code) → write the test file ([test-id].test.md with scenario, fixtures and expected behaviour, or [test-id].test.js|py) → add an entry to that `tests.config.json` (id, target, schedule, owner, `enabled`) → run `node tests/[agents|scripts]/run-tests.system.link.js --id [test-id]` (the link in that test folder) → check the written-back `last_result` and `logs/tests.jsonl` → set `next_action` if it fails. Enable/disable from the UI or by editing `enabled`.
  - [2.11.8] `record-research.md` (D-025, proposed): add an item to the level's `research/index.json` (status `planned`) → create `research/[research-id]-[slug]/README.md` (question, method) → run it, keeping artifacts in that folder (`running`) → write `results_summary` and `decisions` (`done` or `abandoned`) → link what it led to in `related` (new variant, `changes.md`, tests, decision log [2.6]) → the SI sub-agent saves a pointer in its `agent-memory/`.
  - [2.11.9] `add-or-change-link.md` (D-031, proposed): find the file to read (index [2.18]; the links index [16.1] shows who else reads it; prefer a stable `latest.*` output) → add or change one entry in your own links file [27.3]: `to`, `from`, `why`, `required` → relink runs by itself (hook or scheduler watch), or run `node scripts/relink.system.link.js` → check its report: the link exists and points where you expect → if a change to that file should restart your main run, add it to that job's `on_change` [27.4]. To remove a link, delete its entry or set `enabled: false`; relink removes the symlink.
  - [2.11.10] `process-an-input.md` (D-033): the owner-input runbook: store → extract → place → ripple → record → rebuild the map → summarise; the knowledge agent follows it through its knowledge-intake skill [10.1.2.1].
  - [2.11.5] `stop-or-delete-agent.md`: stop → (a trading agent: close or flatten positions and unfund the account, [19.6.17.4], D-058) → archive the agent folder (its own logs/data live there now) → run `relink`: it removes the agent's entries from the parent's `subagents.link/` folders (D-030) and warns every agent whose links file still points at its files (D-031) → mark retired in index [2.18]; the archived folder keeps its docs [46] for history.
- **Writers / readers:** knowledge agent and system-support agents write them. The create-agent script [14], main domain agents and self-improvement agents follow them.
- **Updated:** when the process changes. Scripts in [14] should match these steps.

### [2.12] `docs/feature-map.md` (owner request)
- **Purpose:** map each feature/logic area to the folders and files that implement it, so any agent can find where a piece of logic lives and what a change will touch.
- **Outline:** Agent-type legend · one table per feature area (data collection, pre-analysis, subscriptions and triggers, run loop, decision and execution test/live, self-improvement wheel, agent creation, routing, UI, logging and analytics, docs/self-support, safety and risk). Each table has the columns: logic in plain words · files/folders with [n] numbers · owning agent type. It ends with a gaps list (features with no files yet).
- **Writers / readers:** knowledge agent / system-support agents write it. All agents read it before changing things; self-improvement agents read it to locate what to change; the owner reads it to review.
- **Updated:** whenever a feature or file is added, moved, renamed or removed (keep in sync with [2.13] `file-tree.md`).
- **Draft:** `/mnt/project-files/vision/docs/feature-map.md`.

### [2.13] `apps/project-IDE/data/file-tree.md` (this document; was [6]; D-041)
- **Purpose:** the annotated, numbered tree of the whole OS, plus one fully expanded example agent. It is where every folder and file is explained, and it is the basis for going through objects one by one with the owner.
- **Outline:** header (version, how to read, placeholders) · Tree (code block with [n] numbers and inline # comments) · Objects: one section per [n] with purpose, contents, writers/readers, open questions · Changelog.
- **Writers / readers:** knowledge agent / system-support agents write it after owner answers. The owner reviews it. All agents read it to know where things are; the create-agent logic [2.11.1] follows its example-agent layout.
- **Updated:** whenever a folder or file is added, moved, renamed or removed. It stays in sync with [2.12] `feature-map.md`: every [n] referenced there must exist here. Numbers are never reused, and moved objects keep a stub.
- **Where (D-041):** with the project's records in `apps/project-IDE/data/` [53.2], since the page is built from it. A file tree doc for people comes last into [2] (D-034, D-047).
- **Open:** Should a drift check compare it with the real folders automatically? Later the page may be built by walking the repository and its `.index.md` files, and this file generated from it (plan [53.2.5]).

### [2.14] `docs/data-schemas.md` (owner request)
- **Purpose:** the shape of every JSON/MD file in the system, so workers, agents, scripts and the UI read and write the same format.
- **Outline:** General rules (encoding, timestamps, IDs, file naming, versioning of schemas) · Worker outputs (per worker: path, fields, example) · Sub-agent outputs · Configs ([11.1] `system.config.json` sections, workers files in the [11.10] format (D-029), links files in the [11.13] format and the links index [16.1] (D-031), [11.11], the agent config [27.2]) · Routing ([11.11] `models.config.json`) · Run logs and job logs · Index entries [2.18] · **Tests config** `tests.config.json` (D-025): `schema_version`, `level` (agent id), `kind` (agents|scripts), `tests[]` with `id`, `name`, `target` (file under test), `file` (test file), `enabled`, `schedule` (manual | on_change | interval:[x] | before_promote), `owner` (who maintains it), `last_run`, `last_result` (success | fail | error | skipped | never), `last_duration_ms`, `fail_count`, `notes`, `next_action` (what should be done) · **Research index** `research/index.json` (D-025): `schema_version`, `level`, `items[]` with `id`, `slug`, `topic`, `question`, `status` (planned | running | done | abandoned), `started`, `finished`, `ran_by`, `requested_by`, `folder`, `results_summary`, `decisions[]` (`decision`, `by`, `approved_by`, `date`, `decision_ref`), `links[]` (files used/produced), `related` (`agents`, `changes`, `tests`, `research`), `tags` · Owner comments/questions from the UI · MD file templates (run summary, memory note, changes). The domain config, decision records, order logs, positions and the metrics snapshot are the prediction-market domain's [19.6.9] (D-058).
- **Writers / readers:** whoever adds or changes a file type updates its schema (system-support, domain or SI agent). Every script, agent and the UI API read it.
- **Updated:** whenever a JSON/MD file type is added or its fields change; a change is recorded in [2.9].
- **Open:** Should schemas also exist as machine-checkable JSON Schema files (e.g. `agents/system/configs/schemas.link/`), with this MD as the readable view?

### [2.15] `docs/flows.md` (owner request)
- **Purpose:** every flow step by step. **Data flows:** how data moves through the system. **User flows:** what the owner does and what happens next.
- **Outline:** *Data flows:* worker → data store → `.link` → agent · sub-agent pre-analysis · trigger (interval / important file change → cancel and restart) · run loop → decision → action (test/live) · logs → UI · self-improvement wheel (analyse → new config → new test agent) · outside-world signals (new model/harness/news) → routing update. *User flows:* create an agent from input · review performance · approve/reject a funded account · stop/delete · comment / ask a question / "do better" · review a proposed change. Each flow has a diagram, the files touched ([n] numbers) and the owning agent type.
- **Writers / readers:** knowledge agent / system-support agents write it. The owner reads it to review behaviour; agents and the UI build on it.
- **Updated:** whenever a flow changes. It stays consistent with [2.12] feature-map (the same files per feature).

### [2.16] `docs/metrics.md` (owner request)
- **Purpose:** how any agent is measured and compared, and the general conditions for going live.
- **Outline:** The metrics every agent has (period and mode, cost and tokens, latency, errors, tests), how each is computed and from which files ([34], [35]) · Going live: the general conditions for a test-to-live candidate (then owner approval, [2.11.4]) · Open questions. PnL, win rate, drawdown, calibration, champion and challenger, and demotion with money are the prediction-market domain's [19.6.11] (D-058).
- **Writers / readers:** the owner sets targets and thresholds; system-support/SI agents propose changes as "pending owner" in [2.6]. SI agents, domain agents and the UI read it.
- **Updated:** when a metric or rule changes (owner decision).

### [2.17] `docs/common/` (owner request: "common things")
- **Purpose:** knowledge shared by every agent, written once and read by all. It replaces the former `agents/docs/architecture.md` [7] and `shared.md` [9].
- **Contents:**
  - [2.17.1] `agent-architecture.md` (was [7]): how an agent works inside: folder parts, run loop, sub-agents, memory, how it gets data.
  - [2.17.2] `shared-mechanics.md` (was [9]): triggers and cancel-and-restart, test/live modes, the general stop switch, `.link` symlinks and `relink` (D-031), logging, config merge order (with a domain's own config, like [19.2.4], between [11.1] and the agent's config). The order stop switch and positions on stop are the prediction-market domain's [19.6.8] (D-058).
  - [2.17.3] `common-prompt.md` (proposed): the base prompt every agent's `.claude/CLAUDE.md` ([24.5] and the level equivalents) builds on (v0.1 "common prompt"), including the rule "after editing your links file, run relink" (D-031).
  - [2.17.4] `self-improvement-templates.md` (proposed): the base templates every level's SI sub-agent ([10.1.1.1], [19.1.1.2], [21.1.1.1]) starts from (vision §8); the strategy templates are the prediction-market domain's [19.6.16.3] (D-058).
- **Writers / readers:** system-support agents write; changes to [2.17.3] need owner approval (proposed). All agents read it; agent `CLAUDE.md` files link to it.
- **Updated:** when shared behaviour changes.
- **Resolved (D-017, D-020):** an agent links the individual common docs it needs into its `docs/` [46.1] (e.g. `agent-architecture.link.md`).

### [2.18] `docs/index/` (owner request: "indexes of all things")
- **Purpose:** one index per kind of thing, so the owner, agents and the UI can find anything. It replaces the former catalog [8].
- **Contents (one line per item, with path and [n] type):**
  - [2.18.1] `agents.md`: **the registry of agent names (D-012)**: one row per agent ever created, including retired ones, so names are never reused. Fields: name (unique ID), type (system/domain/strategy level agent, main/variant, support; D-022), domain, parent, route, mode, status (active/paused/retired), created date, path (its docs are in `[path]/docs/`). If a JSON registry is chosen, it is the source and this MD is generated from it.
  - [2.18.2] `workers.md`: every job from all workers files (found by scanning `agents/**/configs/*.workers.json`, real files only; D-029/D-030): owner agent, type, schedule, where it runs, platform, model, on/off, output path, readers.
  - [2.18.3] `subagents.md`: every sub-agent (unique name, D-012): level (system/domain/strategy) and path of its `.claude/agents/` file, role (pre-analysis, domain owner, self-improvement), input, output, memory/state path ([16.3]), schedule, route, used by.
  - [2.18.4] `services.md`: every acting service, its test/live mode and credential refs (never secrets).
  - [2.18.5] `apps.md`: every app in [43] (D-055): kind (ours, fork, research clone), source, our fork and its branches, the commit in use, last update from the source, used by.
  - [2.18.6] `models.md`: platforms/models, status (default/supported/later), what routes to them (view of [11.11]).
  - [2.18.7] `links.md` (D-031): every file link from every links file: agent, where it appears, where it points, why (view of the links index [16.1]).
  - [2.18.8] `knowledge-map.json` (D-033; now in `apps/project-IDE/data/` [53.2], D-041): built by `build_map.py` [10.1.2.5.2.5] from the knowledge tags and the tree: every knowledge entry and the files and folders it applies to, every node with its file doc, the knowledge applying directly and from folders above, and the hash its summary must match; plus problems (tags that match nothing, nodes with no knowledge).
  - `summaries.json` is retired (D-039): the How it works of every file and folder now lives in its own `[name].index.md` (D-039); the last version is in `vision/archive/2026-10-05/`.
- **Writers / readers:** create/stop scripts [14] and system-support agents update it on every add/remove. Everyone reads it; the UI lists from it.
- **Updated:** whenever an agent, worker, sub-agent, service, app or model is added, changed or retired.
- **Open:** Hand-written MD, or generated from a JSON registry (e.g. `agents/system/data/registry.json`) that the UI also reads? (Proposed: JSON is the source, MD is generated.)

### [2.19] (retired: central per-agent docs)
- D-017 (supersedes D-003): each agent's docs are now real files in its own `docs/` [46]. The system reaches them through [2.20] `subagents.link/` and the links below it (D-030).

### [2.20] `agents/system/docs/subagents.link/` (D-030; was the `agents/` view of every agent, D-017)
- **Purpose:** one folder link per domain, [2.20.1] `[domain-name]/` → that domain's `docs/` [19.6]. The domain's docs link on to its strategies' ([19.6.1]) and each strategy's to its agents' ([21.6.1]), so all docs can be read from here, level by level ([2.7.4]).
- **Writers / readers:** `relink` [14.1] adds the link from the folder tree (the domain's `init.sh` [19.10] runs it) and removes it after `stop-or-delete`. Read by the UI, the system session, SI sub-agents and the knowledge agent.

### [2.21] `docs/architecture.md` (D-033)
- **Purpose:** how the system is built, one section per mechanism: domains and agent levels, the standard agent folder and `.claude/`, child links and file links, configs and routing, workers, jobs and the scheduler, scripts, logs and data, secrets, tests and research, docs, UI and apps. Each section's tag says which files it applies to.
- **Writers / readers:** the knowledge agent writes it. Agents and the owner read it after [2.3].
- **Updated:** when a mechanism changes. Formats go to [2.14], rules to [2.7] and [2.8], step-by-step flows to [2.15].
- **Draft:** `/mnt/project-files/vision/docs/architecture.md`.

### [3] (moved to [2.2])
- Kept as a number so the other object numbers stay stable.

### [4] `agents/` (D-013)
- **Purpose:** all agents. Its children are the system domain `system/` [10] and the folders of kinds of domains, today `trading/` [56], which holds the prediction-market domain `trading/prediction-market/` [19] (owner, D-059). More domains and kinds come later; the next trading domain is `trading/copytrading/` (not in the tree yet). The old `trading-domains/` [18] is retired.
- **Shape of a domain:** `.claude/` (domain level, D-016), then the levels the domain defines (the prediction-market domain: strategy folders, then trading agents). The system domain also holds the shared `configs/`, `scripts/`, `logs/`, `data/` [11]–[16].
- **Belongs elsewhere:** nothing doc-related: shared docs are in the system domain [2], agent docs in each agent [46]; cloned repos → `apps/` [43]; the prediction-market domain's dashboard → `apps/trading-ui/` [45]; secrets → repo-root `.secrets/` [47], outside `agents/` (configs hold only key names, `secret_keys`; D-023, D-027).
- **Writers / readers:** the create-agent script [14.1] creates agent folders; the domain agent [19.1.5] and SI sub-agents [21.1.1.1] create variants; agents run here.
- **Resolved (D-026):** system-support agents are sub-agents in the system `.claude/agents/` ([10.1.1.2]), not folders; [10.2] is retired.
- **Levels (D-022, D-058):** every agent is a folder with the standard structure [2.7.1]: **system** [10] (manages all domains and system development), then each **domain** [19] (responsible for its domain), then the levels the domain defines. The prediction-market domain has **strategy** [21] (one concrete strategy) and, under it, its trading variants [23], same structure; a later trading domain copies it.

### [5] (merged into [2])
- `agents/docs/` was merged into the shared docs [2] (now `agents/system/docs/`) so docs are not duplicated. [6] → [2.13], [7] → [2.17.1], [8] → [2.18], [9] → [2.17.2].

### [6] (moved to [2.13])
- The file tree covers the whole OS, so it lives in the shared docs [2].

### [7] (moved to [2.17.1])

### [8] (moved to [2.18])
- The catalog became the index: one file per kind of thing.

### [9] (moved to [2.17.2])

### [10] `agents/system/` (system domain, D-013 / D-015)
- **Purpose:** the system domain and the **system-level agent** (D-022): it manages all domains and the development of the system. It has the standard agent folder [2.7.1]; the only difference is that it (a) holds the **shared** files every agent uses and (b), like every level, links to its children: each content folder has `subagents.link/[domain-name]/` → that domain's folder of the same kind ([2.7.4], D-030). Strategies and agents are reached one level further down each time. This replaces the flat views of every agent (D-015).
- **Child links, not copies:** `data/subagents.link/[domain-name]/` etc. are **folder links** to each child's real folder. Copies would duplicate data and drift out of date.
- **Level files (D-022):** [10.1.5] `.claude/CLAUDE.md` holds the project's rules every Claude reads first (D-045) and the system manager prompt (oversees domains, system health, system development, answers owner questions about the whole system) · [10.4] `package.json`, [10.5] `requirements.txt` for the shared scripts · [10.6] `init.sh` installs the git hooks and runs relink for the whole project (D-031) · [10.7] `start.sh` starts the scheduler [14.1] (every agent's jobs, D-029) and the system session.
- **Contents:** [10.1] `.claude/` · [2] `docs/` · [11] `configs/` · [10.1.5] `.claude/CLAUDE.md`, [10.4]–[10.7] level files · [14] `scripts/` · [15] `logs/` · [16] `data/` · [10.8] `tests/`, [10.9] `research/` (D-025, [2.7.3]). System-support roles are sub-agents in [10.1.1] (D-026), such as the knowledge agent [10.1.1.2].
- **Belongs here:** anything shared by two or more agents. Anything for one agent stays in that agent's folder (real files). **Promotion rule (proposed):** when a second agent needs an agent-local thing (e.g. [31]), it moves into the matching shared folder here, and agents that need it get a file link to it (D-020).
- **Link mechanics (proposed):**
  - All links use relative paths and always have `.link` in the name ([2.7]).
  - **Agent links are individual file links (D-020, supersedes D-014's folder links for agents):** inside an agent's `configs/`, `scripts/`, `logs/`, `data/`, `docs/`, each link points to **one file** its logic needs, from any folder: system (e.g. [11.1], [16.3]), domain (e.g. [14.3], [19.5.3]) or strategy level, or another agent's outputs. Examples: [27.1], [30.1], [34.1], [35.1], [46.1]. There are no `system.link/` folders in agents any more.
  - **Which links (D-031):** each agent lists them in its own links file `configs/[name].links.json` ([11.13] system, [19.2.3] domain, [21.2.3] strategy, [27.3] variant). `create-agent` [14.1] writes the first version; afterwards the agent itself, its SI sub-agent or the owner edit it. A link may come from anywhere under `agents/`: the system, the agent's own domain or strategy, another domain, or another agent (by unique name). The shared `relink` script [14.1] builds every link from these files.
  - **Stable targets (proposed):** producers keep a stable file per output (e.g. `latest.json`, `latest.md`, `latest.log`), so file links do not break when dated files rotate.
  - **No `.claude` links (D-030, for now):** the D-019 down-links [10.1.3]/[10.1.4] and [21.1.3]/[21.1.4] are removed; the domain level never had any (D-021).
  - **Child links (D-030):** every level's content folders hold `subagents.link/[child-name]/` → the child's folder of the same kind: system [11.2.1], [14.4.1], [15.5.1], [16.4.1], [2.20.1], [10.8.3.1], [10.9.3.1] → domains; domain [19.2.2.1], [19.3.1.1], [19.4.1.1], [19.5.1.1], [19.6.1.1], [19.12.3.1], [19.13.3.1] → strategies; strategy [21.2.2.1], [21.3.1.1], [21.4.1.1], [21.5.1.1], [21.6.1.1], [21.12.3.1], [21.13.3.1] → its agents.
  - `relink` [14.1] creates the agent's file links **and** its entries in the parent's `subagents.link/` folders, and removes links nobody wants any more. `init.sh` [40] and `create-agent` call it; after `stop-or-delete` it removes the deleted agent's entries. When it runs is listed in [14.1].
  - **Loops:** agents now hold only file links, so the old `system.link/` → view → agent cycle is gone. The `subagents.link/` entries are folder links, so tools must still **not follow `.link` folders recursively**. `check-links.system.js` [14.1] checks for cycles, broken links, symlinks that neither have `.link` nor sit in a `.link` folder, folder links outside `subagents.link/`, `subagents.link/` entries that are not a direct child's folder of the same kind, any `.claude` link, and any mismatch with [27.3].
  - Agents treat every linked file as **read-only** and write only to their own real files.
- **When shared files change (proposed):** configs are read at the start of each run, so a change applies from the next run of every agent. The general stop switch in [11.1] `modes` is checked before every outside action (the prediction-market domain adds its order stop switch, [19.2.4], D-058).
- **Open:** Should changes to shared configs require owner approval before they reach live agents?
- **Resolved (D-020, answers the D-019 follow-up):** agents have no `system.link/` folders. They hold individual file links to exactly what they need, chosen at creation and by self-improvement. The system views stay as they are. `.claude` keeps D-019 (parent → child folder links); D-020 applies only to `configs/`, `scripts/`, `logs/`, `data/`, `docs/`, so the two rules do not overlap. *Later (D-030):* the system views became per-level `subagents.link/` folders and the `.claude` links were removed.

### [10.1] `agents/system/.claude/` (D-008, D-016)
- **Purpose:** the system domain's Claude Code level: system-wide sub-agents [10.1.1]; the tree lists only the real ones (owner, 2026-10-06, D-045): [10.1.1.1] `sys-self-improvement-agent.md` (D-018: improves the system itself: shared scripts, configs, routing, docs; reacts to new models/harnesses), [10.1.1.2] the knowledge base agent and [10.1.1.3] the project IDE agent; and system-wide skills [10.1.2]. A new sub-agent gets its own line when it is written. Sub-agents' models come from [11.11]; their outputs go to [16.3] and their logs to [15.4].
- **Writers / readers:** system-support agents write; domain-owner/SI sub-agents propose.
- **Down-links (removed, D-030):** [10.1.3]/[10.1.4] are gone for now; no level links another level's `.claude/`. System-support roles are sub-agents in this `.claude/agents/` itself ([10.1.1.2], D-026).
- **~~Runs always start from the top~~ (D-019 proposal, withdrawn by D-021):** the domain level no longer links down to strategies, so a session started at `agents/system/` cannot see the strategies and agents.
- **How levels and agents run now (proposed, D-021), the simplest option:** **each level runs in its own folder.**
  - The system session runs at `agents/system/` (system SI, pre-analysis sub-agents).
  - Each domain session runs at its domain folder (domain owner, domain SI).
  - Each strategy session runs at its strategy folder (strategy SI; it reads its agents' files through its `subagents.link/` folders, D-030).
  - An agent runs in **its own folder** (here a trading agent): `run-agent` [14.1] starts Claude Code there, with its `.claude/CLAUDE.md` [24.5], its own `.claude/` and its file links (D-020).
  - **How an agent gets shared things:** higher-level sub-agents do not run inside agent sessions. They run in their own level's session and write outputs (e.g. `news-digest/latest.md`), which the agent links as data files (D-020, e.g. [35.1] `news-digest.link.md`). Shared rules and knowledge reach it the same way, as doc/config file links.
  - **Not chosen:** copying shared skills into agents at create time, because copies drift and miss self-improvement updates.
- **Full contents (D-024):** standard `.claude/` [2.7.2]: [10.1.5] `CLAUDE.md` (system manager), [10.1.6] `settings.json`, [10.1.7] `settings.local.json`, [10.1.8] `rules/`, [10.1.2] `skills/`, [10.1.9] `commands/`, [10.1.1] `agents/`, [10.1.10] `workflows/`, [10.1.11] `output-styles/`, [10.1.12] `agent-memory/` (incl. the system SI memory), and [10.1.13] `agent-memory-local/`; no `docs/` here: the docs for people moved one level up into [2] (D-047).
- **Resolved (D-030):** the remaining `.claude` down-links are removed for now; a level reads a child's skills or sub-agents by path if it needs them.
- **Open (D-021):** if an agent needs a shared **skill** (not just outputs), may it get an individual file link in its own `.claude/skills/` (D-020 style)? That would be an upward link, which D-019 forbids for `.claude`.

### [10.1.5] `agents/system/.claude/CLAUDE.md` (D-024; took over the root CLAUDE.md, D-045)
- **Purpose:** the first file a Claude reads when it works on the project from the system folder, as Claude Code does on the owner's server (D-043): what the project is for (the owner's vibecoding window, D-040), what to read first, where things are, the rules, and how a round works (pull, file every input, rebuild, commit and push); and the system manager prompt (oversees the domains, system health and system development, answers the owner's questions about the whole system). It describes the system in general terms; trading duties sit in the prediction-market domain's prompt [19.1.5] (D-058).
- **Contents:** what this project is for · read first, in order ([2.1], [10.1.1.2], [10.1.1.3], [53.2.4], the newest [2.9] entries and `git log`, [2.6]) · where things are · every round · rules · the File Tree page · the system manager's job.
- **Writers / readers:** the knowledge base agent [10.1.1.2] keeps it current. Claude Code loads it by itself when it starts in `agents/system/` (tested 2026-10-06); a Claude that starts at the top of the repository does not load it on its own and reads it first by hand.
- **Updated:** when the layout, the read order, the rules or the way of syncing change.
- **Whole context (D-049):** the window is also the AI's context: before a change, read the item's How it works and run `build_map.py --context` for it (the levels above included); after it, bring everything related in line; what you learn and every answer to the owner go into the docs.
- **Draft:** `/mnt/project-files/vision/.claude/CLAUDE.md` (was `vision/CLAUDE.md`).

### [10.1.3], [10.1.4], [21.1.3], [21.1.4] (retired: `.claude` down-links, D-030)
- Owner decision D-030: for now no `.claude` folder is linked at any level. The system → domain links [10.1.3]/[10.1.4] and the strategy → agent links [21.1.3]/[21.1.4] (D-019) are removed; the domain → strategy links [19.1.3]/[19.1.4] were already gone (D-021). Levels see each other's files through `subagents.link/` in their content folders instead ([2.7.4]).

### [10.2] (retired: `agents/system/[sys-agent-name]/` folders, D-026)
- Owner decision D-026: system-support work (vision §8 type 1: development, docs, improvement, analysis, research) gets no agent folder under `agents/system/`. Each role is a Claude Code sub-agent file in the system's `.claude/agents/` ([10.1.1.2], e.g. `sys-docs-agent.md`, `sys-improvement-agent.md`), like the domain owner and SI roles (D-018). The system `.claude` has no down-links to them. Shared system files stay in the system agent's own `configs/`, `scripts/`, `logs/`, `data/`, `docs/`. If a support role ever needs its own files and runs, it becomes a normal agent with the standard folder [2.7.1] under its domain.

### [10.1.1.2] `agents/system/.claude/agents/knowledge-base-agent.md` (D-034; was `sys-knowledge-agent.md`, D-033, and `sys-docs-agent.md`, D-026)
- **Purpose:** the knowledge base agent. It keeps everything we know in its own notes and turns it into plain, book-like docs for people (D-034): every owner input (project chat, threads, the File Tree page), every answer we give and every change to the system's files goes through it. It writes each doc with that doc's own skill and keeps the three main docs in line in this order every round: [2.2] the vision ([10.1.2.3]), [2.1] the README ([10.1.2.4]), then [2.22] the rebuild prompt ([10.1.2.7]) (D-048). The rules for writing every doc are in this file. The File Tree page and the way into and out of it belong to the project IDE agent [10.1.1.3] (D-041); page messages that carry knowledge come to this agent through knowledge-intake. Other support roles (development, improvement, analysis, research) are sibling `.md` files here.
- **How it works:** its skill [10.1.2.1] `knowledge-intake` stores the input [2.10], extracts the knowledge, finds where it lives through the knowledge map [2.18.8], writes it there (or creates a new section or doc when nothing fits), ripples it to every file doc and topic that states the same thing, records decisions [2.6] and the changelog [2.9], and rebuilds the map. Its skill [10.1.2.2] `file-index` then rewrites the How it works file [51] of every file and folder the change made stale, children first, up to the root.
- **Rules:** one fact in one place; honest status (decided only on the owner's word); raw inputs never edited; no secret values anywhere; nothing committed without the owner.
- **Whole context (D-049):** the docs are the context every AI works from, exact enough to act on. Before a change it walks the file's relations and the knowledge from the levels above (`build_map --context`); what must follow changes in the same round; a session's findings are filed even when no file changed; every owner question gets its answer written where the owner should have found it.
- **Runs:** after every owner input and every system change, in the session that received it; plus the `knowledge-sync` job in [11.10] (on a change under `agents/**` or `docs/inputs/**`, and nightly) that picks up anything missed, incl. messages left on the File Tree page. Model from [11.11]; memory in [10.1.12]; logs to [15.4].
- **Draft:** `/mnt/project-files/vision/.claude/agents/knowledge-base-agent.md` (renamed by the owner, 2026-10-01).

### [10.1.2.1] `knowledge-intake/SKILL.md` (D-033)
- **Purpose:** process one owner input or one system change into the knowledge base: store → extract (fact, rule, format, flow, rename, removal, decision, question answered or raised; decided, proposed or open) → find where each item lives (map, grep) → write → ripple → record → rebuild the map → summarise → report two to five lines to the owner.
- **Whole context (D-049):** it also takes what a session learned when no file changed; every question gets a home (the explanation goes where the owner should have found it, and is sharpened when the docs already cover it); the ripple step walks the related agents, skills, scripts, index lists and How it works files, the levels above included.
- **Draft:** `/mnt/project-files/vision/.claude/skills/knowledge-intake/SKILL.md`.

### [10.1.2.2] `file-index/SKILL.md` (D-039; was `knowledge-summarise`, D-033)
- **Purpose:** how the knowledge base agent writes and keeps the How it works of every file and folder, one `[name].index.md` each (D-039): where the file goes, its front matter, the fixed headings (D-036) or `## Summary` for files not moved yet, the Keep in mind lines, lengths, and plain words for someone new to the project. `build-map --stale` lists the stale ones children first; `build-map --context` gives what each is written from; a file that is still right is confirmed instead of rewritten, which stops the ripple. The owner's edits on the File Tree page (How it works, Edit) are written into the index file at the next sync and confirmed.
- **Draft:** `/mnt/project-files/vision/.claude/skills/file-index/SKILL.md` (the knowledge-summarise draft is archived in `vision/archive/2026-10-05/`).

### [10.1.2.3] `vision-doc/SKILL.md` (D-034, D-048)
- **Purpose:** how the knowledge base agent writes and updates `vision.md` [2.2], the top-level doc: what we are building and why, the concept, how it should work, the business logic, worked examples, where we are, principles, ideas, open questions and where to go deeper. Twelve sections in the same order at every level (system, domain, app; the levels below a domain from that domain's `doc-outlines.md`, such as [19.6.15], D-058), lengths per level, examples of too technical versus right, the steps for a first build and for an update after an input, its page on the File Tree, and checks. It keeps the vision high: no folders, files or paths except the pointer to the README.
- **Draft:** `/mnt/project-files/vision/.claude/skills/vision-doc/SKILL.md`.

### [10.1.2.4] `readme-doc/SKILL.md` (D-034, D-036, D-048)
- **Purpose:** how the knowledge base agent writes and keeps `README.md` [2.1]: the full, exact overview of every main part of the system, with the path to each part's own docs and nothing about the logic inside agents. Its Outline (In short, the system at a glance, the layout, one section per part, the table of docs, still open), the same idea for a domain or an app (the levels below a domain from that domain's `doc-outlines.md`, such as [19.6.15], D-058), lengths per level, examples of too vague and too deep versus right, the steps for a first build and for the update after the vision and before the rebuild prompt, the README's page on the File Tree, and checks.
- **Draft:** `/mnt/project-files/vision/.claude/skills/readme-doc/SKILL.md`.

### [10.1.2.7] `rebuild-prompt-doc/SKILL.md` (owner, 2026-10-06, D-048)
- **Purpose:** how the knowledge base agent writes and keeps `rebuild-prompt.md` [2.22], the prompt an AI rebuilds the whole system from: its Outline, how lower levels get their own, lengths per level, how to write for AI (instructions, exact names, status, no secrets, checks you can run), the steps for a first build and for the update that runs last after every design change, its page on the File Tree, and checks.
- **Name (proposed):** `rebuild-prompt-doc`, after the `[doc]-doc` naming of the other doc skills.
- **Draft:** `/mnt/project-files/vision/.claude/skills/rebuild-prompt-doc/SKILL.md`.

### [10.1.2.8] `change-plan/SKILL.md` (owner, 2026-10-06, D-051)
- **Purpose:** the main development skill: every change request gets a plan before it is built (owner: "plan also should be a skill that we need define support and develope as main things in development"). When a plan is needed, where plans live [53.2.5], their statuses, the outline every plan follows, the steps from request to build to moving its knowledge into its homes, the archive, and the rules.
- **Used by:** every AI that changes the system: the session that receives the request, the helpers, later the agents' own improvements. The knowledge base agent [10.1.1.2] distributes a built plan's knowledge with knowledge-intake.
- **Name (proposed):** `change-plan`.
- **Draft:** `/mnt/project-files/vision/.claude/skills/change-plan/SKILL.md`.

### [10.1.1.3] `project-ide-agent.md` (owner request, D-041)
- **Purpose:** the project IDE agent: looks after the owner's IDE [53]. It builds the File Tree page from the repository and publishes it (ide-build [10.1.2.5]); at a sync it turns what the owner left on the page (messages, notes, edits to a file or to a How it works, new, moved or deleted items) into changes to files, metadata and views (ide-sync [10.1.2.6]); and it runs the requests the owner sends from the page.
- **Split with the knowledge base agent [10.1.1.2]:** that agent owns the knowledge and the docs, and every input goes through its knowledge-intake; this one owns the page and the way into and out of it. A page message that carries knowledge is handed to knowledge-intake; a page edit to a file is written into the file and filed as an input too.
- **Runs:** when the owner says "sync the file tree", after every round that changed the tree, a doc or a How it works file (rebuild and republish), and when a page request asks for work. Model from [11.11]; logs to [15.4].
- **Server (D-042, D-043):** also looks after the page on the owner's server [53.3], where page requests run as Claude Code sessions in the repository and page edits go straight into the files.
- **Draft:** `/mnt/project-files/vision/.claude/agents/project-ide-agent.md`.

### [10.1.2.5] `ide-build/` (D-041)
- **Purpose:** the skill that builds the page data from the repository, checks it, tests the page and publishes it. Its scripts sit inside it, so the skill and its tools move together.
- **Contents:** [10.1.2.5.1] `SKILL.md` (parse the tree notes, enrich with the next data version, build the map until every How it works file is fresh with no orphans, copy the data next to the page [53.1.2], test on desktop and phone width, publish at the same link, report in plain words) and [10.1.2.5.2] `scripts/`.
- **Draft:** `/mnt/project-files/vision/.claude/skills/ide-build/SKILL.md`; the scripts are still in `vision/tools/`.
- **One job per file (D-050):** the build scripts break the rule today (`build_map.py` builds the map, lists stale files, prints context, confirms and writes texts); splitting them into one-job files is step 7 of the file-set plan, waiting for the owner.

### [10.1.2.5.2] `ide-build/scripts/` (D-041)
- **Purpose:** the build scripts, in Python with the standard library only, plus one page check in JavaScript.
- **Contents:** [10.1.2.5.2.1] `README.md` (what each script does and how to run them), [10.1.2.5.2.2] `parse.py` (reads the tree notes [2.13] into a list of items), [10.1.2.5.2.3] `enrich.py` (adds drafts, examples, knowledge, How it works and tabs; writes the page data [53.1.2]), [10.1.2.5.2.4] `tabs.py` (the field guides and extra tabs), [10.1.2.5.2.5] `build_map.py` (the knowledge map [2.18.8]; lists stale or orphaned How it works files, prints a node's context, writes and confirms index files), [10.1.2.5.2.6] `index_files.py` (where each `.index.md` lives; reads and writes them), [10.1.2.5.2.7] `check_page.js` (opens the page on a desktop and a phone width with a stand-in for the artifact runtime; fails on a page error, a missing tab or a page wider than the phone; the only script in JavaScript, it needs Playwright). `build-map` was planned as a system script [14.1]; it lives here now.
- **Writers / readers:** the project IDE agent [10.1.1.3] runs them; the knowledge base agent [10.1.1.2] runs `build_map.py` for the How it works files (file-index [10.1.2.2]).
- **Draft:** `/mnt/project-files/vision/tools/`.

### [10.1.2.5.2.1] `ide-build/scripts/README.md` (D-041)
- **Purpose:** the guide to the build scripts: how to build the page data, where the page lives and how to publish it, how How it works files are found and written, and how the owner's page saves reach the files at a sync.
- **Draft:** `/mnt/project-files/vision/tools/README.md`.

### [10.1.2.5.2.2] `parse.py` (D-041)
- **Purpose:** reads the tree notes [2.13]: the numbered tree (each line becomes an item with its parent, path, number and comment), the section of every item, the retired items, the decisions and the feature map. Writes them as one JSON file for `enrich.py`.
- **Draft:** `/mnt/project-files/vision/tools/parse.py`.

### [10.1.2.5.2.3] `enrich.py` (D-041)
- **Purpose:** turns the parsed tree into the page data [53.1.2]: status (decided unless marked proposed; placeholder; example), examples, the text of drafts and of files that already exist in the repository, the tabs from `tabs.py`, the owner's overrides [53.2.3], the knowledge map and every item's How it works from its `.index.md`. Takes the next data version from `DATA_VERSION`.
- **Draft:** `/mnt/project-files/vision/tools/enrich.py`.

### [10.1.2.5.2.4] `tabs.py` (D-041)
- **Purpose:** the field guides shown as a settings file's Example (each key, its values, an example and what it means) and the extra tabs some items have: an agent's overview, jobs and links, a test list, the key names of a keys file (never values).
- **Draft:** `/mnt/project-files/vision/tools/tabs.py`.

### [10.1.2.5.2.5] `build_map.py` (D-041; was the system script `build-map`, D-033)
- **Purpose:** builds the knowledge map [2.18.8] from the knowledge tags in the notes and the tree, and keeps the How it works files honest: `--stale` lists the missing or stale ones children first, `--orphans` the ones whose item is gone, `--context <id>` prints what one is written from, `--confirm <id>` marks one still right, `--set <file.json>` writes many at once.
- **Draft:** `/mnt/project-files/vision/tools/build_map.py`.

### [10.1.2.5.2.6] `index_files.py` (D-041)
- **Purpose:** knows where every `.index.md` and `.meta.json` lives (D-039, D-057), makes the empty `.meta.json` files (next to the draft for items that have one, otherwise in the mirror tree while we plan; next to the real file in the repository), and reads and writes them with their front matter.
- **Draft:** `/mnt/project-files/vision/tools/index_files.py`.

### [10.1.2.5.2.7] `check_page.js` (D-041)
- **Purpose:** the page check before publishing: opens the page with a stand-in for the artifact runtime on a desktop and a phone width, opens How it works and File for the given items, and fails on a page error, a missing tab or a page wider than the phone. Saves screenshots when given a folder. Needs Node and Playwright with Chromium.
- **Draft:** `/mnt/project-files/vision/tools/check_page.js`.

### [10.1.2.6] `ide-sync/SKILL.md` (D-041)
- **Purpose:** the way back from the page: read everything waiting in the page's store (messages, notes, file edits, How it works edits, new, moved or deleted items, requests), file each through knowledge-intake [10.1.2.1], write file edits into their files and How it works edits into their `.index.md` word for word, fold the rest into the tree notes [2.13] or the overrides [53.2.3], run the requests, then rebuild and republish with ide-build [10.1.2.5] and clear what was folded.
- **Deleting an item (D-044):** a deletion from the page is one round: read the owner's note first; delete the item and its How it works file; clean the project of it (its line and section in the tree notes, with its number retired; link files and rows in the links and workers files; mentions in other files and How it works files; the parent's How it works; the knowledge map); file it with the note and a changelog line; rebuild and commit. Earlier inputs and decisions stay as history. On the server Claude Code does this at once; at the sync it is only checked.
- **The changed mark (D-044):** the sync clears the page's "changed" marks when it deletes the folded documents.
- **Started by Apply changes (D-046):** the page's Apply changes button [53.1.1] starts the same round. It ends in this order: the new page published, the folded documents cleared, the `apply` input marked processed last (the open page watches it), and on claude.ai the button's comment answered and resolved.
- **Draft:** `/mnt/project-files/vision/.claude/skills/ide-sync/SKILL.md`.

### [10.1.14] (retired: `.claude/docs/` moved one level up into the agent's own `docs/` [2], owner 2026-10-06, D-047)
- **Owner (2026-10-06):** "just .claude/docs/ move in a level up docs in every agent who has .claude". Only the system had one; its [2.1] README and [2.2] vision are now in [2]. The domain, strategy and trading agent keep their `docs/` ([19.6], [21.6], [46]); a level's docs for people go there when they are written.

### [11] `agents/system/configs/` (D-006 as amended by D-014)
- **Purpose:** the shared configs, in JSON (D-005): [11.1] `system.config.json`, [11.10] `system.workers.json` (the system's own jobs, D-029), [11.11] `models.config.json`, [11.13] `system.links.json` (the system's own file links, D-031); plus [11.2] `subagents.link/` with each domain's `configs/` (D-030), which also shows each domain's jobs files by domain.
- **Direction (D-014, supersedes D-006's central per-agent location):** each agent's own config is a **real file in the agent folder** ([27.2]); the agent links the shared config files it needs ([27.1], D-020); the system reaches each domain's configs through [11.2.1], and the strategies' and agents' one `subagents.link/` further down each time (D-030).
- **Not decided (open):** the exact shape of the files, and which settings are common vs individual (to be worked out with example agents).
- **Merge rule (proposed), lowest to highest priority:** global [11.1] → domain (the prediction-market domain's [19.2.4], D-058) → agent [27.2] → owner overrides from the page (stop, pause, approve).
  - Objects deep-merge by key; arrays and single values are replaced by the higher layer.
  - Jobs come only from each agent's own workers file (D-029: [11.10], [19.2.1], [21.2.1], [27.4]). Routes come from [11.11] unless a job names its model.
  - **Safety exceptions:** limits can only be **tightened** by a lower layer. **Live** needs the global live allowlist and the owner's approval; an agent can never switch itself to live. The general **stop switch** overrides everything and is checked before every outside action. **Secrets** appear in no config, only references. The prediction-market domain adds its money rules (risk caps, funded accounts, the order stop switch) in [19.2.4] (D-058).
  - At run start `run-agent` [14.1] writes the merged result to the agent's logs [34] as `effective-config.json`.
- **Writers / readers:** system-support agents write the shared files; changes to `modes` need owner approval (recorded in [2.6]), as do the domain's `risk` and `accounts` [19.2.4]. All agents, scripts and the UI read. Shapes go in [2.14].
- **Numbering:** [11.3]–[11.9] (v0.6 drafts) are retired.

### [11.1] `system.config.json` (D-006, D-041)
- **Purpose:** the single place for everything controllable globally, except jobs (each agent's workers file, D-029) and routing [11.11].
- **Sections (proposed outline):**
  - `defaults`: timezone, log level, run timeout, data retention, languages; `by_agent_type` (system/domain/main/sub/support/SI, plus the types a domain adds, such as the prediction-market domain's strategy: allowed actions, memory on/off).
  - `modes`: `default_mode: "test"`, `kill_switch` (the general stop switch: stops every outside action), per-service test/live, `live_allowlist`.
  - `schedules`: scheduling defaults for every workers file: time zone, default run intervals per agent type, max concurrent runs, quiet hours, which `run_on` targets are allowed, daily AI cost cap. (Each job's own schedule is in its agent's workers file, D-029.)
  - `triggers`: important/unimportant file patterns, debounce, min time between restarts, max restarts per hour, `on_unimportant: "wait_next_run"`.
  - `notifications`: channels and events → severity (agent error, promotion proposed, stop switch, live action); a domain adds its own events.
- **Moved to the domain (D-058):** `risk`, trading `accounts`, the currency, and the per-domain settings (venues, fees, market filters, default workers, tighten-only risk) are the prediction-market domain's, in [19.2.4] `prediction-market-agents.config.json`; the order meaning of the stop switch and the events `live_trade` and `risk_limit_hit` went with them.
- **Writers / readers:** system-support agents; owner approval for `modes`. Read by everything.
- **Updated:** when a global setting changes. A section is split out into its own file once it gets long.

### [11.10] `system.workers.json` (D-029; was `workers.config.json`, D-007)
- **Purpose:** the system agent's own **jobs**: everything the system runs on a schedule or on demand, such as the data collectors shared by several domains [14.2], relinking and link checks, tests, index rebuilds and its sub-agent runs (SI [10.1.1.1]; the knowledge agent [10.1.1.2] as the `knowledge-sync` job, on changes under `agents/**` or `docs/inputs/**` and nightly, D-033). Every other agent has the same file for its own jobs in its `configs/` (domain [19.2.1], strategy [21.2.1], agent [27.4]), all in this format. The system sees each domain's file through [11.2] `subagents.link/` (D-030), and deeper ones one level down at a time.
- **All off for now (owner, page 2026-10-09, in-20261009-1040):** every system job has `enabled: false`; they stay in the file and run only once the owner turns them on.
- **What a job is (D-029):** either a plain **script** (`platform: none`) or an **AI run** on a coding-agent platform: the agent itself (`agent`: its main run, in its own folder), a `subagent`, a `skill`, a `workflow` or a slash `command`.
- **Job fields (proposed):** `id` (unique in the file) · `enabled` (turn off without deleting) · `purpose` · `type` (script | agent | subagent | skill | workflow | command) · `run` (the command for a script; the sub-agent, skill, workflow or command name otherwise) · `schedule` · `timezone` · `run_on` (local | cloud | desktop | github-actions) · `platform` (none | claude-code | cursor | codex) · `model` (`route` = take it from [11.11]) · `effort` · for AI runs: `prompt` (text, or `@path` to a prompt file), `workspace` (the folder it runs in; default the owner agent's folder), `allowed_tools`, `permission_mode`, `max_turns`, `max_cost_usd` · `secret_keys` (local runs only) · `inputs`, `outputs` · `on_change` (paths whose change starts the job; for the main run it cancels and restarts the current run) · `timeout`, `retries`, `concurrency` (skip | queue | restart) · `mode` (test | live; live needs owner approval) · `notify` (never | failure | always). The file's `defaults` fill in anything a job leaves out.
- **`schedule` (proposed, one short string):** `every 15m` / `every 6h` / `every 1d` · `cron 0 22 * * 1-5` · `once 2026-11-03 20:00` (runs one time, then shows as done) · `after [job-id]` (when that job succeeds) · `manual` (only from the UI or a command). Time zone from the job, else the file's `defaults`, else [11.1] `defaults.timezone`.
- **Where it runs (`run_on`, proposed):** `local` (default): headless on the machine that runs the scheduler [14.1], with the local files, links and test secrets. `cloud`: the platform's own cloud (Claude Code routines, Codex cloud, Cursor background agents): a fresh copy of the repo, no local files, no secrets; Claude Code routines run at most hourly. `desktop`: a Claude desktop scheduled task; it runs only while the app is open. `github-actions`: a scheduled workflow in the repo. The scheduler runs `local` jobs itself and registers the others on their platform.
- **How AI runs start (proposed):** `run-job` [14.1] builds the platform's headless command in the job's `workspace`: Claude Code `claude -p`, Cursor `cursor-agent -p`, Codex `codex exec`, with the job's model, prompt, tools, permission mode and turn limit. Adding a platform later means adding one command template to `run-job`.
- **Rules (proposed):** a `live` job needs owner approval and a live-allowed agent ([11.1] `modes`). `cloud`, `desktop` and `github-actions` jobs get no `secret_keys` and cannot act live. To pause a job, set `enabled: false`; never delete it to pause. Runtime state (last run, result, next run, fail count) is not written here: the scheduler keeps it in [16.1] `scheduler-state.json` and logs every run to the owner agent's `logs/jobs/[job-id]/`, so this file changes only when someone changes a job.
- **Writers / readers:** the owner (on the page: turn on/off, change when, where, platform, model); the owner agent's domain or SI sub-agents propose changes. Read by the scheduler and `run-job` [14.1], the index [2.18.2] and the UI.
- **Updated:** whenever a job is added, changed, rescheduled, turned off or removed.
- **Open:** Which machine runs the `local` scheduler: the owner's computer or a small always-on server? Should the scheduler create cloud routines by itself, or should the owner confirm each one?

### [11.11] `models.config.json` (D-011)
- **Purpose:** which platform/model/effort each agent, sub-agent and AI-using worker uses, plus the list of platforms and their status (vision §9).
- **Key fields (proposed):** `{ "platforms": { "claude-code": { "status": "default", "secret_keys": [...] }, "cursor": { "status": "supported" }, "openrouter": { "status": "supported-not-connected" }, "codex": { "status": "later" }, "kimi": { "status": "later" } }, "models": { "opus-5.5": { "platform": "claude-code", "effort": "xhigh" }, "sonnet-5.5": {...}, "composer-2.5": { "platform": "cursor" } }, "defaults_by_type": { "main": "opus-5.5", "domain": "opus-5.5", "si": "opus-5.5", "sub": "composer-2.5", "worker": "composer-2.5", "support": "sonnet-5.5" }, "routes": { "[agent|subagent|worker name]": "[model]" } }`
- **Rule (proposed):** the route is `routes[name]`, else `defaults_by_type[type]`. A job in a workers file may name its own model instead (D-029); `model: "route"` uses this file. It must name a platform whose status allows use. Where a domain puts the platform and model in an agent's name (the prediction-market domain does, [19.6.7]), they must match its route (check in [14.1]).
- **Writers / readers:** system-support agents write; SI agents propose route changes (a route change makes a new test version of the agent). The run scripts, the index [2.18.6] and the UI read it.
- **Updated:** when a model/platform is added or its status changes ([2.11.3]), or a route changes.
- **Open questions (found 2026-09-30 while building the index lists):**
  - Default effort: this file says `xhigh` for opus-5.5, but the owner asked for opus-5.5 at medium effort as the page default (2026-09-29). Is medium the default everywhere, or only on the page?
  - Sub-agent default: `composer-2.5` here, `sonnet-5.5` in the page's Routes example. Which one?
  - `defaults_by_type` has no entry for the system or strategy agent types, and the fable and haiku models the owner asked for are not listed yet.

### [11.13] `system.links.json` (D-031)
- **Purpose:** the system agent's own file links, and the **format every level uses**. Every agent has the same file in its `configs/`: domain [19.2.3], strategy [21.2.3], variant [27.3] (`[name]` as for the workers file: `system`, the domain name, or the agent name). For each link it says which file, from where, where it appears and why. The system's own list is short; most links sit in the agents at the lowest levels.
- **Fields (proposed):** `schema_version` · `agent` · `links[]`, one entry per link: `enabled` (off = relink removes the symlink but keeps the entry) · `to` (where the link appears, inside the agent's own `configs/`, `scripts/`, `logs/`, `data/`, `docs/`, `tests/` or `research/`; the name carries `.link`, e.g. `data/news-digest.link.md`) · `from` (the file it points at, see below) · `why` · `required` (true: a missing target is an error and the agent's main run does not start; false: a warning, and no link is made until the file exists) · `added_by` (create-agent, the agent itself, its SI sub-agent, owner) · `added` (date).
- **`from` (proposed):** a path under `agents/`, or a short form: `@system/…` (the system folder), `@domain/…` (the agent's own domain), `@strategy/…` (its own strategy, a level the prediction-market domain defines), `@[name]/…` (any domain or agent by its unique name, D-012, looked up in the registry [2.18.1], so the entry keeps working if that folder moves). Examples: `@system/data/subagents/news-digest/latest.md`, `@domain/data/markets-catalog/latest.json`, `@[other-domain]/data/[output]/latest.json` (another domain), `@[agent-name]/data/[output]/latest.json` (an agent anywhere, by its unique name).
- **Rules (proposed):** file links only (D-020): `from` is one real file; if it is itself a link, relink points at the real file behind it, so there are no chains. Never anything in `.secrets/` (D-023) or in any `.claude/` (D-030). `to` is always inside the agent's own folders, never inside `subagents.link/`. Links are relative symlinks and read-only for the agent. Child links (`subagents.link/`, D-030) are **not** listed here: relink builds them from the folder tree.
- **Writers / readers:** create-agent writes the first version; then the agent itself, its SI sub-agent and the owner (UI) edit it. `relink` and `check-links` [14.1] read it; the links index [16.1] and the UI show who links what.
- **Open:** Commit the symlinks themselves to git (a fresh clone works at once; the pre-commit hook keeps them in step), or git-ignore them and let relink rebuild them after every clone and pull? Proposed: commit them. May an agent link any file of another agent, or only files that agent lists as `outputs` of its jobs (a public contract)?

### [11.12] (retired: `configs/workers/` jobs view; merged into [11.2], D-030)
- D-030: every level's `configs/` has `subagents.link/[child]/`, so the system sees each domain's configs, including its workers file, in [11.2.1], and the strategies' and agents' files one level further down each time. The scheduler finds every workers file by scanning `agents/**/configs/*.workers.json` (real files only).

### [11.2] `agents/system/configs/subagents.link/` (D-030)
- **Purpose:** one folder link per domain, [11.2.1] `[domain-name]/` → that domain's `configs/` [19.2], including its workers file [19.2.1] and its own `subagents.link/` [19.2.2] to its strategies. The system, the UI and SI agents read configs and jobs domain by domain from here ([2.7.4]).
- **Was:** the central home of per-agent config files (D-006 direction, superseded by D-014), then a flat view of every agent's configs (D-015), then also the jobs view [11.12] (D-029). D-030 replaced both with this folder.

### [12] (moved: workers are scripts)
- D-007: shared worker scripts are in [14.2]. Their jobs are in [11.10] `system.workers.json` (D-029).

### [13] (moved to [10.1.1])
- D-008: sub-agents are Claude Code subagents in `.claude/agents/`.

### [14] `agents/system/scripts/` (D-007, D-015)
- **Purpose:** the shared scripts (JS/TS or Python) plus [14.4] `subagents.link/` to each domain's scripts (D-030).
- **Naming (proposed):** kind by sub-folder and by suffix `[name].[kind].[ext]`, where kind is `worker` or `system`; a domain may add its own kinds (the prediction-market domain's `decision`, D-058).
- **One job per file (owner, 2026-10-06 21:04, D-050):** "every code file should have only one function, endpoint or whatever runable one, could with different params, but have one purpose". Related scripts are grouped in a folder, each file with its own How it works and metadata.
- **Contents (proposed):**
  - [14.1] `system/`: `*.system.js|py`, e.g. `create-agent` (**uniqueness check point for D-012**: validates the name format [2.7], rejects any name already in the registry [2.18.1] including retired ones, reserves the name, then scaffolds the folder and runs `init.sh`), `run-agent` (starts Claude Code in the agent's own folder (proposed, D-021), merges config, writes `effective-config.json`), `scheduler` (D-029; was `trigger-watcher`: finds every workers file by scanning `agents/**/configs/*.workers.json` (real files only, D-030), runs due jobs, watches `on_change` files with cancel-and-restart for main runs, registers cloud/desktop/GitHub jobs on their platform, keeps state in [16.1] `scheduler-state.json`, logs to [15.1]), `run-job` (D-029: runs one job: the script, or the platform's headless command in the job's workspace with its model, prompt and tools; passes only the job's `secret_keys` via `load-secret`; logs to the owner agent's `logs/jobs/[job-id]/`), `relink` (D-031: builds every link in the project from the links files ([11.13] format, found by scanning `agents/**/configs/*.links.json`, real files only) plus the child links from the folder tree (D-030): creates missing links, fixes changed ones, removes `.link` symlinks that no file lists, then runs the `check-links` rules; writes the links index [16.1] `links.index.json` (every link: owner agent, `to`, real target, required, status) and logs each change to [15.1]; re-runnable and safe at any time, one run at a time (lock). Options: `--agent [name]` (one agent; what `scripts/relink.system.link.js` presets when called from an agent folder), `--changed [files]` / `--staged` (works out which agents the changed files affect: a links file, an added, removed or moved agent folder, or a moved or deleted link target, using the links index), `--check` (report only; exit 1 if anything is wrong). **When it runs:** (1) a links file changes: the `relink` job in [11.10] watches `agents/**/configs/*.links.json` (`on_change`) and runs `--changed`, plus one full run a day; (2) review time: git hooks installed by the system `init.sh` [10.6]: `pre-commit` runs `--staged` and blocks the commit if a required link is broken, `post-merge` and `post-checkout` run `--changed` after a pull or branch switch, and the owner approving a change in the UI runs it too; (3) the agent itself: after editing its links file it runs `node scripts/relink.system.link.js` (rule in [2.17.3]), and a `PostToolUse` hook in its `.claude/settings.json` does it automatically ([2.7.2]); (4) `create-agent`, `init.sh` [40] and `stop-or-delete`), `check-links` (run by relink after every change and hourly on its own: broken links, cycles, symlinks without `.link` outside a `.link` folder, any `.claude` link (none for now, D-030), `subagents.link/` entries that are not a direct child's folder of the same kind, and any link or copy whose target is inside [47] `.secrets/` (D-023: never allowed)), `load-secret` (D-023, D-027: returns a key for the calling script at execution time, only if that agent's config lists it in `secret_keys` and, for `live/`, only if the owner approved the agent for live (in the prediction-market domain also with a funded, owner-approved account, [19.6.8]); returns the value to the process only, never to logs or the LLM), `notifier`, `run-tests` (D-025: runs a level's tests from its `tests.config.json` files, writes results back and to that level's `logs/tests.jsonl`; linked into each `tests/agents/` and `tests/scripts/` folder at every level as `run-tests.system.link.js`, which the level's links file lists, and into an agent's own `scripts/` (such as the trading agent's [30.2]) to run both kinds, which presets the kind and that folder's config; agent tests run Claude Code headless in test mode with no secrets, see [2.7.3]).
  - [14.2] `workers/`: `*.worker.py|js`, data collectors shared by several domains; each runs as a job in [11.10] `system.workers.json` (D-029). A collector one domain needs lives in that domain (the Polymarket prices: [19.3.5], D-058).
  - [14.3] `decisions/` moved to the prediction-market domain's `scripts/` (number kept, D-058).
  - [14.4] `subagents.link/` (D-030): [14.4.1] `[domain-name]/` → that domain's `scripts/` [19.3].
- **Writers / readers:** system-support agents write the shared scripts; domain/SI agents propose. Agents link the individual scripts they need ([30.2], D-020).
- **Scheduler (proposed, D-029):** one central `scheduler` process for all agents, started by [10.7] and kept alive by the OS (launchd/systemd); agents' `start.sh` only does one run. Where it runs is open in [11.10].

### [15] `agents/system/logs/` (D-009 as amended by D-014 / D-015)
- **Purpose:** shared logs by source, plus [15.5] `subagents.link/` to each domain's logs (D-030); the UI starts here and goes down level by level.
- **Contents:** [15.1] `system/` (scheduler, triggers, relink and link checks, errors, costs) · [15.2] `services/[service]/` (every outside action of a shared service, test or live; a domain's own acting services log in the domain, such as the order logs [19.4.3]) · [15.3] `workers/[worker]/` (shared workers) · [15.4] `subagents/[subagent]/` · [15.5] `subagents.link/` (D-030): [15.5.1] `[domain-name]/` → that domain's `logs/` [19.4].
- **Agent side:** each agent's own logs are real files in its `logs/` [34], and it links only the shared log files it needs ([34.1], D-020; read-only). This replaces the v0.8 "agent logs central, only own logs linked" default.
- **Open:** Log format (JSONL + MD run summary?) and retention?

### [16] `agents/system/data/` (D-010 as amended by D-014 / D-015)
- **Purpose:** shared data by source, plus [16.4] `subagents.link/` to each domain's data (D-030).
- **Contents:** [16.1] `system/` (registry, run state, read cursors, `scheduler-state.json` with every job's last run, result and next run, D-029; `links.index.json` with every link in the project: owner agent, where it appears, real target, required, status, written by relink, D-031) · [16.2] `workers/[worker]/` (workers shared by several domains) · [16.3] `subagents/[subagent]/` · [16.4] `subagents.link/` (D-030): [16.4.1] `[domain-name]/` → that domain's `data/` [19.5].
- **Agent side:** own data is real files in [35]; shared data (e.g. subscribed workers' outputs) is linked file by file ([35.1], D-020). This replaces the per-worker links [36] and the central own-data link [36.1].
- **Open:** How is "new since last run" tracked: file timestamps, or a per-agent cursor in [16.1] (vision §5.2)?

### [17] (moved to [11.11])
- D-011: routing and platforms are in [11.11] `models.config.json`.

### [18] (retired: `trading-domains/`)
- D-013: domains sit directly under `agents/`, and `system/` is one of them.

### [56] `agents/trading/` (owner, D-059)
- **Purpose:** the folder of all trading domains. Today it holds the prediction-market domain `prediction-market/` [19]; the next trading domain is `copytrading/`, copied from it when the owner asks (D-056). Every trading domain keeps its own standard agent folder inside.
- **Holds for now (D-059, D-061):** `docs/` [56.1], `researches/` [56.2] with the research studies (the first real files of the tree), and its domains. It has no agent, settings or scripts of its own; the shared trading notes, the domain config and the buy, sell and risk scripts stay in the prediction-market domain until the owner says otherwise.
- **Writers / readers:** the knowledge base agent [10.1.1.2] keeps its docs; the system reaches each trading domain through `subagents.link/` as before.

### [56.2] `agents/trading/researches/` (owner, 2026-10-09, D-061)
- **Purpose:** the research studies, real files in the repository: [54.1] prediction-market strategies, [54.2] self-improving agents, [54.3] trading-agent architectures. The owner moved the repository's top-level `researches/` here: "move it to trading/researches folder".
- **Real file tree:** this is the first part of the tree that exists in the repository. The page marks what exists and lists every real file under it, read from the repository at each build (D-061).
- **Open:** the name `researches/` differs from the `research/` folder every agent has (D-025); kept as the owner named it.

### [56.1] `agents/trading/docs/` (owner, D-059)
- **Purpose:** trading's own docs for people, the same three every level has (D-053): [56.1.1] `README.md`, [56.1.2] `vision.md` and [56.1.3] `rebuild-prompt.md`.
- **Writers / readers:** the knowledge base agent [10.1.1.2] with the vision, README and rebuild prompt skills; the system's docs point here; each trading domain's docs build on these.
- **Planning copy:** `vision/docs/trading/` while we plan.

### [56.1.1] `agents/trading/docs/README.md` (owner, D-059)
- **Purpose:** every part of trading exactly: its layout, each trading domain with the path to its README, and what is still open. Its In short uses the vision's words. Written 2026-10-09.

### [56.1.2] `agents/trading/docs/vision.md` (owner, D-059)
- **Purpose:** why trading has its own folder, the trading domains, the rules every trading domain shares, how a new trading domain is copied from the prediction-market domain, examples, where it stands and what is open. Written 2026-10-09.

### [56.1.3] `agents/trading/docs/rebuild-prompt.md` (owner, D-059)
- **Purpose:** how an AI builds `agents/trading/` again: only this folder and its docs, assuming the system exists, then its domains' rebuild prompts in build order (prediction market first, copy trading later). Written 2026-10-09.

### [19] `agents/trading/prediction-market/`
- **Purpose:** prediction-market domain (Polymarket first) and the **domain-level agent** (D-022), responsible for its domain. It has the standard agent folder [2.7.1]: [19.1] `.claude/`, [19.2] `configs/`, [19.3] `scripts/`, [19.4] `logs/`, [19.5] `data/`, [19.6] `docs/`, [19.1.5] `.claude/CLAUDE.md`, [19.8] `package.json`, [19.9] `requirements.txt`, [19.10] `init.sh`, [19.11] `start.sh`, [19.12] `tests/`, [19.13] `research/` (D-025, [2.7.3]).
- **[19.1.5] `.claude/CLAUDE.md` = the domain owner (D-022 reconciles D-018):** the domain's own prompt now carries the domain-owner role (strategies, health, Q&A, owner comments). Since D-058 it also carries the trading duties that sat in the system manager's prompt: it oversees every area of trading in the domain, and a hard limit on money or risk goes in code, in the decision scripts and the risk check [14.3], never only in a prompt. The separate sub-agent file `pm-domain-owner-agent.md` [19.1.1.1] is retired. The domain SI sub-agent [19.1.1.2] stays in `.claude/agents/`.
- **[19.11] `start.sh`:** starts the domain session in this folder (as the `domain-session` job in [19.2.1], D-029, and on owner questions from the UI).
- **Contents:** [19.1] `.claude/` (domain level, D-016): [19.1.1] `agents/` (domain sub-agents) and [19.1.2] `skills/` (domain skills, e.g. Polymarket API usage). No `.claude` links in or out (D-021, D-030). Its content folders link down to its strategies through `subagents.link/` ([19.2.2], [19.3.1], [19.4.1], [19.5.1], [19.6.1], [19.12.3], [19.13.3]; D-030), and the system links down to them ([11.2.1], [14.4.1], [15.5.1], [16.4.1], [2.20.1], [10.8.3.1], [10.9.3.1]). Also [21] strategies. Domain settings (risk limits, trading accounts, venues, fees, market filters, currency, the order stop switch) are in its own [19.2.4] `prediction-market-agents.config.json` (D-058). There is no separate domain-agent folder any more (D-018).
- **Docs (D-034, D-048):** [19.6] `docs/` holds the domain's own [19.6.2] `README.md` (every part of the domain, with each strategy's README path) [19.6.3] `vision.md` (why this domain, how money is made here, examples) and [19.6.4] `rebuild-prompt.md` (how an AI builds the domain's folder again, D-053), written with the README, vision and rebuild prompt skills when the domain's docs are written; a later trading domain has the same. Listing them in the tree is our default, so the system README has a real path for each domain.
- **Trading lives here (owner, 2026-10-07 09:04, D-056, D-058):** "remove all related to trading agent down to trading agents in our case i think to prediction market domain, another trading domain later should be just templated if needs from the prediction market agent". Everything about trading that sat at the system level is in this domain now: its config [19.2.4], the shared buy, sell and risk scripts [14.3], the Polymarket price collector [19.3.5] with its job logs [19.4.2] and data [19.5.3], the order logs [19.4.3], the `trading-` notes in [19.6] ([19.6.5] to [19.6.18.1]) and the study of trading-agent architectures [54.3]. A later trading domain is copied from this one under its own name.
- **Open:** Does it contain only Polymarket, or other venues (Kalshi, etc.) too?

### [19.2.4] `prediction-market-agents.config.json` (D-058)
- **Purpose:** the domain's own settings, everything about money and markets that used to sit in the system's [11.1]: `risk` (hard caps for the whole domain, per agent and per venue: capital, daily loss, drawdown stop, position %, open positions, orders per hour; agents may only tighten them), `accounts` (trading accounts: id, venue, mode, funded, `approved_by_owner`, assigned agent, max capital, `secret_keys`), `venues` with their fees, market filters, default workers, the `currency`, the order stop switch `kill_switch` (refuse orders, close positions, set the account back to unfunded; the name is our proposal) and the trade notifications (`live_trade`, `risk_limit_hit`).
- **Merge (proposed):** after the system's [11.1] and before each agent's own config [27.2]; a lower layer may only tighten a limit.
- **Writers / readers:** the domain agent [19.1.5] and system-support agents write it; changes to `risk` and `accounts` need the owner's approval (recorded in [2.6]). Every agent of the domain links it ([27.1]); the run scripts and the page read it. Its shape is in [19.6.9].

### [14.3] `scripts/decisions/` (prediction-market domain; moved from the system's `scripts/`, number kept, D-058)
- **Purpose:** `*.decision.js|py`, the shared buy, sell and risk-check building blocks that every trading agent's decision scripts [33] call; `risk-check.decision.js` checks every order against the limits of [19.2.4] and the agent's config before it is placed.
- **Writers / readers:** the domain agent and system-support agents write them; trading agents link the ones they use ([30.1], D-020). `decision` is the prediction-market domain's own script kind; the system's kinds are `worker` and `system` ([2.7]).

### [19.3.5] `polymarket-prices.worker.py` (D-058; was the system's shared-worker example)
- **Purpose:** collects Polymarket prices on a schedule into [19.5.3] `data/polymarket-prices/`; it runs as a job in the domain's [19.2.1], with its run logs in [19.4.2]. Trading agents link its `latest.json` ([35.1]).

### [19.4.2] `logs/jobs/[job-id]/` (D-029, D-058)
- **Purpose:** the run logs of the domain's own jobs (for example `polymarket-prices`, `markets-catalog`): `history.jsonl`, one line per run, and `latest.log`, the output of the last run, written by `run-job` [14.1]. Trading agents link a worker's `latest.log` when they need it ([34.1]).

### [19.4.3] `logs/services/[service]/` (D-058; the trading part of the system's [15.2])
- **Purpose:** the order logs of the domain's acting services, one folder per service (for example a Polymarket executor), test and live: every order placed, its market, side, size and fill. They are the source of every PnL number. Format in [19.6.9].

### [19.5.3] `data/polymarket-prices/` (D-058)
- **Purpose:** the output of [19.3.5]: `latest.json`, a stable file trading agents link ([35.1]), plus dated files. Rotation and retention follow the system's data rules.

### [19.6.5], [19.6.6], [19.6.7], [19.6.8], [19.6.9], [19.6.10], [19.6.11], [19.6.12], [19.6.13], [19.6.14], [19.6.15] the domain's `trading-` notes and `doc-outlines.md` (D-058)
- **Purpose:** the trading layer of the system's topic notes, one note each, read together with the system's note of the same subject: [19.6.5] `trading-overview.md` (overview [2.3]), [19.6.6] `trading-architecture.md` ([2.21]), [19.6.7] `trading-conventions.md` ([2.7]), [19.6.8] `trading-safety.md` ([2.8] and the money part of [2.17.2]), [19.6.9] `trading-data-schemas.md` ([2.14]), [19.6.10] `trading-flows.md` ([2.15]), [19.6.11] `trading-metrics.md` ([2.16]), [19.6.12] `trading-glossary.md` ([2.4]), [19.6.13] `trading-roadmap.md` ([2.5]), [19.6.14] `trading-feature-map.md` ([2.12]), and [19.6.15] `doc-outlines.md`, the outlines and lengths of the strategy and trading-agent docs that the three doc skills use below the domain.
- **Names (D-058):** the `trading-` prefix keeps a trading agent's links to the system's notes and to these apart (`safety.link.md` and `trading-safety.link.md`, [46.1]). A later trading domain copies them.
- **Writers / readers:** the knowledge base agent [10.1.1.2] keeps them, like the system's notes; every trading agent reads the ones it links.
- **Planning copy:** `vision/docs/prediction-market-agents/` while we plan.

### [19.6.16] `docs/common/` (prediction-market domain, D-058)
- **Purpose:** trading knowledge every trading agent shares: [19.6.16.1] `trading-agent-architecture.md` (the run loop with buy, sell and sell all, positions, memory across variants; the trading layer of [2.17.1]), [19.6.16.2] `trading-prompt.md` (the trading layer of the common prompt [2.17.3], which the strategy [21.1.5] and trading-agent [24.5] prompts add), [19.6.16.3] `strategy-si-templates.md` (the domain, strategy and variant templates the self-improvement agents build strategies from; the trading part of [2.17.4]).

### [19.6.17] `docs/how-to/` (prediction-market domain, D-058)
- **Purpose:** the trading runbooks, each the money part of a system runbook: [19.6.17.1] `create-strategy-or-variant.md` ([2.11.1]), [19.6.17.2] `go-live-with-money.md` ([2.11.4]), [19.6.17.3] `add-trading-account.md` ([2.11.6]), [19.6.17.4] `stop-trading-agent.md` (close positions, unfund the account; [2.11.5]).

### [19.6.18] `docs/index/` (prediction-market domain, D-058)
- **Purpose:** the domain's own lists: [19.6.18.1] `accounts.md`, every trading account: id, venue, funded, approved by the owner, capital, used by (moved out of the system's agents list [2.18.1] and secrets index [47.3]).

### [19.2.1] `prediction-market-agents.workers.json` (D-029)
- **Purpose:** the domain agent's jobs in the [11.10] format, e.g. the domain session (`agent`, every 4h), the domain SI sub-agent [19.1.1.2] (`subagent`, nightly), domain-wide Polymarket collectors (`script`: `markets-catalog` [19.3.3], `polymarket-prices` [19.3.5]) and one-off checks on special dates (`once`). The system sees it through [11.2.1] (D-030).

### [19.2.3] `prediction-market-agents.links.json` (D-031)
- **Purpose:** the domain agent's file links in the [11.13] format, e.g. the system's news digest for the domain session (`@system/data/subagents/news-digest/latest.md`) or another domain's data it wants to compare against. The system sees it through [11.2.1] (D-030).

### [19.3.3] `markets-catalog.worker.py` (added 2026-09-30, D-041)
- **Purpose:** the domain's own worker: every hour it writes the catalogue of Polymarket markets the domain cares about to [19.5.2] `data/markets-catalog/latest.json` (job `markets-catalog` in [19.2.1]). It was in the jobs example but had no file in the tree.
- **Readers:** the domain session; the strategy [21.2.3] and every variant [35.1] through their `@domain` links.
- **Fields (proposed):** `markets[]` with `id`, `question`, `category`, `liquidity_usd`, `resolves`, `tradable` (`trading-data-schemas.md` [19.6.9]).
- **Open:** whether resolutions (needed for calibration) are added here or by a separate worker.

### [19.5.2] `data/markets-catalog/` (added 2026-09-30, D-041)
- **Purpose:** output folder of [19.3.3]: `latest.json` plus dated history. Domain data, so it lives in the domain's own `data/`, and lower levels read it only through links.

### [19.6.2], [19.6.3], [19.6.4] `docs/README.md`, `docs/vision.md`, `docs/rebuild-prompt.md` (domain level, D-034, D-048, D-053)
- **Purpose:** the domain's own docs for people. [19.6.2] `README.md` describes every part of the domain exactly (its strategies, the information it collects and shares, its settings and venues, its jobs, tests and research), each with the path to its own docs, and nothing about the logic inside its agents. [19.6.3] `vision.md` says why this domain, its concept, how money is made here, examples, where it stands and what is open; it builds on the system's vision and adds only what differs. [19.6.4] `rebuild-prompt.md` is the prompt an AI follows to build the domain's own folder again exactly; it assumes the system exists, names what it takes from it and lists its strategies' prompts in build order.
- **Writers / readers:** the knowledge base agent [10.1.1.2] with the README skill [10.1.2.4], the vision skill [10.1.2.3] and the rebuild prompt skill [10.1.2.7] (their "At other levels" outlines), in that order, when the domain's docs are written; the system README [2.1] and rebuild prompt [2.22] point here. A later trading domain has the same three files.
- **Status:** the README and vision are listed by our default (D-048), following "the same docs at every level" (D-034); the rebuild prompt follows the owner's D-053 (every level has all three; added to the tree after the owner asked on 2026-10-07 "why agents didn't got a rebuild-prompt?"). Not written yet.

### [19.3.2] `relink.system.link.js` (D-031)
- **Purpose:** file link to the shared `relink` [14.1]. Run from here it relinks only this agent: its file links from [19.2.3] and its entry in the system's `subagents.link/` folders. Every level has one ([21.3.2], [30.3]); the system runs [14.1] directly.

### [19.2.2], [19.3.1], [19.4.1], [19.5.1], [19.6.1], [19.12.3], [19.13.3] `subagents.link/` (domain level, D-030)
- **Purpose:** in each of the domain's content folders, one folder link per strategy agent, named after the strategy's folder ([19.2.2.1], [19.3.1.1], [19.4.1.1], [19.5.1.1], [19.6.1.1], [19.12.3.1], [19.13.3.1] `[agent-name]/`), pointing at that strategy's folder of the same kind ([21.2], [21.3], [21.4], [21.5], [21.6], [21.12], [21.13]). The domain session and the domain SI read their strategies' configs, jobs, logs, data, docs, tests and research here ([2.7.4]).
- **Built by:** `relink` [14.1] from the folder tree (the strategy's `init.sh` [21.10] runs it); removed by relink after `stop-or-delete` [2.11.5]. Read-only for the domain.

### [19.1.3], [19.1.4] (retired: domain → strategy `.claude` links)
- D-021 (owner: no links from the domain level to strategies' agents and skills). The domain session runs at the domain folder with its own sub-agents only.

### [19.1.1.1] (retired: `pm-domain-owner-agent.md`)
- D-022: the domain owner role moved into the domain's own [19.1.5] `.claude/CLAUDE.md`, since the domain folder is now an agent itself.

### [19.1.1.2] `pm-self-improvement-agent.md` (D-018, D-041)
- **Purpose:** self-improvement at domain scope: compares strategies and their variants across the domain, proposes new strategies/variants, and spots domain-wide issues.
- **Memory / state (proposed, D-024 updates D-022):** memory in [19.1.12] `.claude/agent-memory/pm-self-improvement-agent/MEMORY.md` (`memory: project`); research in [19.13] `research/` (D-025); logs in [19.4]. The system sees them through its `subagents.link/` folders (D-030).

### [20] (retired: `main-domain-agents/`)
- D-018: the domain owner became the sub-agent [19.1.1.1]; D-022 then moved the role into the domain's own [19.1.5] `.claude/CLAUDE.md`.

### [21] `strategy-1-agent/`
- **Purpose:** one strategy family and the **strategy-level agent** (D-022), responsible for one concrete strategy. It has the standard agent folder [2.7.1]: [21.1] `.claude/`, [21.2] `configs/`, [21.3] `scripts/`, [21.4] `logs/`, [21.5] `data/`, [21.6] `docs/` (incl. the strategy definition), [21.1.5] `.claude/CLAUDE.md` (strategy manager prompt: runs and compares its variants, coordinates its SI sub-agent), [21.8] `package.json`, [21.9] `requirements.txt`, [21.10] `init.sh`, [21.11] `start.sh` (starts the strategy session), [21.12] `tests/`, [21.13] `research/` (D-025, [2.7.3]). Its ID carries the main platform/model it runs with and its mode: `pm-strategy-1-agent.[platform-model]-[test|live]`, e.g. `pm-strategy-1-agent.opus55-test` (owner, D-032); the folder keeps the structural name `strategy-1-agent/`. It holds its strategy-level Claude Code [21.1] ([21.1.1] strategy sub-agents incl. the SI sub-agent [21.1.1.1]; [21.1.2] strategy skills; D-016; no `.claude` links, D-030) and all its variants [23], whose names start with this strategy's ID. Its content folders link to its trading agents through `subagents.link/` ([21.2.2], [21.3.1], [21.4.1], [21.5.1], [21.6.1], [21.12.3], [21.13.3]; D-030).
- **Self-improvement loop (owner, D-032; proposed):** the strategy agent, through its SI sub-agent [21.1.1.1], creates modifications of itself as new variants [23], runs them in test mode, analyses the results (cross-variant history in [21.5], research in [21.13]) and updates the strategy definition [21.6], its own config [21.2] and prompt [21.1.5] when a modification wins.
- **Docs (D-034, D-048):** [21.6] `docs/` holds the strategy's own [21.6.2] `README.md` (its parts and variations, with each trading agent's README path) and [21.6.3] `vision.md` (the idea, why it should work, its business rules, an example), next to the strategy definition; written with the README and vision skills. Listing them in the tree is our default.
- **Open:** Should the folder carry a real strategy name (e.g. `market-making/`)? Where is the strategy definition itself (template) stored: [21.1.2] as a skill, or in [21.6] `docs/` (proposed)?
- **Open:** Should the strategy folder name itself carry the `.[platform-model]-[test|live]` suffixes, or only the ID in config and the index? (Renaming the folder touches every [21.x] path.)

### [21.2.1] `strategy-1-agent.workers.json` (D-029)
- **Purpose:** the strategy agent's jobs in the [11.10] format, e.g. the strategy session that compares its variants (`agent`, daily) and its SI sub-agent [21.1.1.1] (`subagent`, nightly). The domain sees it through [19.2.2.1] (D-030).

### [21.2.3] `strategy-1-agent.links.json` (D-031)
- **Purpose:** the strategy agent's file links in the [11.13] format, e.g. the domain's market catalog (`@domain/data/markets-catalog/latest.json`) to compare variants market by market. The domain sees it through [19.2.2.1] (D-030).

### [21.6.2], [21.6.3], [21.6.4] `docs/README.md`, `docs/vision.md`, `docs/rebuild-prompt.md` (strategy level, D-034, D-048, D-053)
- **Purpose:** the strategy's own docs for people. [21.6.2] `README.md` describes every part of the strategy exactly: its variations (each a trading agent, in a small table with what differs, model, mode and status, and the path to that agent's README [46.2]), the information it uses, how it is tested on past data, its jobs and its research; how the strategy decides stays in the strategy definition. [21.6.3] `vision.md` says the idea, why it should work, how it should behave, its business rules and one worked example, then where it stands and what is open. [21.6.4] `rebuild-prompt.md` is the prompt an AI follows to build the strategy's own folder again exactly; it assumes the system and the domain exist and lists its trading agents' prompts in build order.
- **Writers / readers:** the knowledge base agent [10.1.1.2] with the README skill [10.1.2.4], the vision skill [10.1.2.3] and the rebuild prompt skill [10.1.2.7] (their "At other levels" outlines), in that order, when the strategy's docs are written; the domain README [19.6.2] and rebuild prompt [19.6.4] point here.
- **Status:** the README and vision are listed by our default (D-048, D-034); the rebuild prompt follows the owner's D-053, added to the tree on 2026-10-07. Not written yet.

### [21.3.2] `relink.system.link.js` (D-031)
- **Purpose:** the same link as [19.3.2]: run from here it relinks only the strategy agent (its file links from [21.2.3] and its entry in the domain's `subagents.link/` folders).

### [21.2.2], [21.3.1], [21.4.1], [21.5.1], [21.6.1], [21.12.3], [21.13.3] `subagents.link/` (strategy level, D-030)
- **Purpose:** in each of the strategy's content folders, one folder link per trading agent (variant), named after the agent ([21.2.2.1], [21.3.1.1], [21.4.1.1], [21.5.1.1], [21.6.1.1], [21.12.3.1], [21.13.3.1] `[agent-name]/`), pointing at that agent's folder of the same kind ([27], [30], [34], [35], [46], [49], [50]). The strategy session and its SI sub-agent compare variants from here ([2.7.4]).
- **Built by:** `relink` [14.1] from the folder tree (the agent's `init.sh` [40] runs it at creation); removed by relink after `stop-or-delete` [2.11.5]. Read-only for the strategy.

### [21.1.1.1] `pm-strategy-1-self-improvement-agent.md` (D-018; was [22])
- **Purpose:** self-improvement at strategy scope, as a Claude Code sub-agent in the strategy's `.claude/agents/`. It runs from time to time, reads the variants' logs/data/docs (through the strategy's own `subagents.link/` folders [21.4.1], [21.5.1], [21.6.1], D-030), past research ([21.13], variants' [50]), outside news and owner comments, then creates new test variants via create-agent [2.11.1]. It records each investigation in [21.13] `research/` and adds or runs tests ([21.12], variants' [49]) for what it changes (D-025). Goal: fast, cheap, efficient, simple, understandable, profitable; fix bugs; test. Templates come from [2.17.4].
- **Levels (D-018):** every `.claude/` level has its own SI sub-agent, scoped to that level: system [10.1.1.1], domain [19.1.1.2], strategy [21.1.1.1].
- **Runs (proposed):** as the `strategy-self-improvement` job (`type: subagent`) in the strategy's workers file [21.2.1] (D-029); defaults from [11.1] `schedules`. Model from the job, else [11.11].
- **Memory / state (proposed, D-024 updates D-022):** memory in [21.1.12] `.claude/agent-memory/pm-strategy-1-self-improvement-agent/MEMORY.md` (`memory: project`); research in [21.13] `research/` (D-025); `changes.md` (cross-variant history) in [21.5] `data/`; logs in [21.4]. Each variant's own change record stays in its [46] `changes.md`.
- **Open:** Can it retire variants or only create them?

### [22] (retired: `pm-strategy-1-self-improvement-agent/` folder)
- D-018: now the strategy-level sub-agent [21.1.1.1]; its memory moved to [16.3] (proposed).

### [23] `pm-strategy-1.momentum-v1.opus55-test/` (example; named per D-012, D-032; was `pm-momentum-v1-agent-opus55-test/`)
- **Purpose:** one variant (modification) of strategy 1 = one harness/platform/model + mode. It runs one run at a time and makes decisions. Variants are created, tested and analysed by the strategy agent's self-improvement sub-agent [21.1.1.1]; a good result can be folded back into the strategy itself (D-032).
- **Shape (D-014, D-022):** the standard agent folder [2.7.1]; every agent has the same folders: `.claude/` [24], `configs/` [27], `scripts/` [30], `logs/` [34], `data/` [35], `docs/` [46], `tests/` [49], `research/` [50] (D-025), each with its own real files plus individual file links to what its logic needs (D-020); plus `.claude/CLAUDE.md` [24.5] (D-024), `package.json`, `requirements.txt`, `init.sh`, `start.sh`.
- **Naming (owner, D-032; format proposed):** a globally unique name that is its ID everywhere (D-012). A variant name always starts with its strategy, then its own name, then the suffixes: `[strategy-id].[own-name]-v[N].[platform-model]-[test|live]` ([2.7]). Example: `pm-strategy-1.momentum-v1.opus55-test`. The strategy is readable from the name alone and all variants of one strategy sort together.
- **Where variants come from (D-032):** the strategy agent [21] and its SI sub-agent [21.1.1.1] propose a modification, create it as a new variant folder here, run it in `test` mode, compare its results against the other variants (cross-variant history in [21.5] `data/`, research in [21.13]) and either retire it or fold the change back into the strategy and its own config and prompt. Whether the SI sub-agent may retire a variant itself or only propose it is still open ([21.1.1.1]).
- **Resolved (proposed):** switching test → live creates a new agent (same name with `…-live`, `parent` = this one); names are never changed.
- **Open:** Does the `v[N]` belong to the variant name or to the strategy (`strategy-1` → `strategy-1-v2`)?

### [24] `.claude/` (agent level)
- **Full contents (D-024):** standard `.claude/` [2.7.2]: [24.5] `CLAUDE.md`, [24.6] `settings.json`, [24.7] `settings.local.json`, [24.8] `rules/`, [25] `skills/`, [24.9] `commands/`, [26] `agents/`, [24.10] `workflows/`, [24.11] `output-styles/`, [24.12] `agent-memory/`, [24.13] `agent-memory-local/`. Same pattern at [19.1.5]–[19.1.13] and [21.1.5]–[21.1.13].
- **Purpose:** the agent's own Claude Code config: its own skills [25] and sub-agents [26] only. **No `.claude` links** in or out (D-030, for now).
- **How it runs (proposed, D-021):** `run-agent` starts Claude Code in this agent's own folder. It uses its own skills/sub-agents plus its file links (D-020). Outputs of system/domain/strategy sub-agents reach it as linked data files (see [10.1]).
- **Open:** What does a Cursor-routed variant use instead (`.cursor/`)?

### [25] `.claude/skills/`
- **Purpose:** agent-specific skills (real files). Not linked from anywhere (D-030).
- **Open:** Which skills should be common to every agent (and so live at system level [10.1.2])?

### [25.1], [25.2], [25.3] (retired: upward skill links)
- D-019: replaced by parent → child links [10.1.4], [21.1.4] ([19.1.4] later retired by D-021; the rest removed by D-030).

### [26] `.claude/agents/`
- **Purpose:** the agent's own Claude Code sub-agents (D-008; real files, later). Not linked from anywhere (D-030).

### [26.1], [26.2], [26.3] (retired: upward sub-agent links)
- D-019: replaced by parent → child links [10.1.3], [21.1.3] ([19.1.3] later retired by D-021; the rest removed by D-030).

### [27] `configs/` (real folder; was `config.link.json`)
- **Purpose:** the agent's configs (D-014). [27.2] `[agent-name].config.json` is the agent's own config; [27.4] `[agent-name].workers.json` is its jobs file (D-029); [27.3] `[agent-name].links.json` is its links file (D-031); [27.1] are file links to the shared config files it needs (e.g. `system.config.link.json`, `models.config.link.json`, and its domain's `prediction-market-agents.config.link.json` [19.2.4]; D-020). Its strategy sees this folder through [21.2.2.1] (D-030).
- **[27.2] sections (proposed, shape open):** `agent` (name, type, domain, strategy, parent) · `mode` (test/live request; live still needs owner approval) · `capital_and_risk` (tighten-only) · `strategy` (strategy-specific parameters). No `route`: routes live in [11.11].
- **Writers / readers:** create-agent [14.1] scaffolds it; the SI sub-agent [21.1.1.1] and the domain agent [19.1.5] write new variants' configs; the agent itself reads it (write access open). The UI shows and compares configs via [11.2].
- **Updated:** on creation and on each tested change (a changed config = a new variant, recorded in [46] `changes.md`).
- **Open:** Which settings are individual vs common (to be decided with example agents)? May the agent edit its own config?

### [27.3] `pm-strategy-1.momentum-v1.opus55-test.links.json` (D-031; was the `links` section of [27.2], D-020)
- **Purpose:** every file link this agent wants, in the [11.13] format: which file, from where (the system, its domain or strategy, another domain, another agent), where it appears in its own folders, and why. `relink` [14.1] builds the links from it and `check-links` verifies them.
- **Example links:** `configs/system.config.link.json` ← `@system/configs/system.config.json` · `configs/prediction-market-agents.config.link.json` ← `@domain/configs/prediction-market-agents.config.json` · `data/polymarket-prices.link.json` ← `@domain/data/polymarket-prices/latest.json` · `data/markets-catalog.link.json` ← `@domain/data/markets-catalog/latest.json` · `scripts/risk-check.decision.link.js` ← `@domain/scripts/decisions/risk-check.decision.js` · `docs/trading-safety.link.md` ← `@domain/docs/trading-safety.md` · `scripts/relink.system.link.js` ← `@system/scripts/system/relink.system.js`.
- **Writers:** `create-agent` [14.1] at creation; then the agent itself (it reruns relink after each edit, D-031), its strategy SI sub-agent [21.1.1.1] and the owner. Reading a shared worker's output adds the matching data link here.
- **Change log (proposed):** each added (`+ to <- from: why`) or removed (`- to: why`) link is written to [46] `changes.md` under `Links`.
- **Open:** Is a link change a new variant (D-012), or may small additions (one more data file) happen in place? D-031 lets the agent edit its own file; whether that bumps `v[N]` is still open.

### [27.4] `pm-strategy-1.momentum-v1.opus55-test.workers.json` (D-029)
- **Purpose:** the trading agent's jobs in the [11.10] format: its main run (`agent`, e.g. every 15m, restarted when an important data link changes via `on_change`; replaces [28]), its own worker [31] (`script`), and one-off jobs on special dates (`once`, e.g. an hour before a market resolves). Its strategy sees it through [21.2.2.1] (D-030).
- **Rule (proposed):** a change to a job's logic (prompt, model, tools, inputs) is a config change and makes a new variant (D-012); the owner turning a job on or off or moving its time does not.
- **Open questions (found 2026-09-30 while writing flows and metrics):**
  - The owner may set the model per job, yet a model change makes a new variant and the model is part of the variant's name. Does an owner model change on a trading agent's job create a new variant, or is it allowed in place?
  - Important files are declared twice: the `triggers` patterns in [11.1] and each main run's `on_change` here. Which one wins when they differ?
  - A test's own `schedule` in `tests.config.json` [49.1.1] is not seen by the scheduler, which reads only workers files. Should run-tests get a job per test folder here?

### [28] (moved to [27.4]: the agent's workers file)
- D-029: the agent's jobs, its run interval and the files whose change restarts a run (`on_change`, was the important-files list) are in its own workers file [27.4]. Global defaults stay in [11.1] `schedules` and `triggers`.

### [29] (retired: `docs.link/`)
- D-017: replaced by the agent's real `docs/` folder [46].

### [30] `scripts/` (real folder)
- **Purpose:** the agent's own scripts (D-007) in JS/TS or Python; kind by suffix `.worker.`, `.decision.`, `.system.`. [30.1] are file links to the shared scripts it uses, e.g. `risk-check.decision.link.js` → [14.3] in its domain (D-020, D-058); [30.3] `relink.system.link.js` → [14.1] relink (D-031). Its strategy sees this folder through [21.3.1.1] (D-030).
- **Rule (proposed):** own scripts write logs to the agent's [34] and data to its [35.2]; an own worker runs as a job in the agent's workers file [27.4] (D-029).
- **One job per file (D-050):** each script is one runnable thing with one purpose, parameters allowed; related ones go in a folder.
- **Open:** Are there other kinds besides worker/decision/system?

### [30.2] (retired: `workers.link/`)
- `workers.link/` is no longer needed: shared workers are reached via [30.1]. The number was given again to the run-tests link `scripts/run-tests.system.link.js` in v1.11, before the never-reuse rule was checked; that link keeps it.

### [30.3] `relink.system.link.js` (D-031)
- **Purpose:** file link to the shared `relink` [14.1]. Called from here it presets `--agent` to this agent, so `node scripts/relink.system.link.js` rebuilds only this agent's links and its entries in its strategy's `subagents.link/`. The agent runs it after editing [27.3]; the hook in its `settings.json` [24.6] runs it too. Same link at every level: [19.3.2], [21.3.2].

### [31] `get-polymarket-data.worker.py`
- **Purpose:** agent-local worker fetching Polymarket data. It runs as the `get-polymarket-data` job in [27.4] (D-029); output → [35.2] `data/get-polymarket-data/`, logs → [34].
- **Open:** It moves to [14.2] when a second agent needs it (promotion rule [10]). Should that be automatic?

### [32] `clean-data.system.js`
- **Purpose:** clean/normalise raw data before the agent reads it.
- **Open:** Is it agent-local, or should it move to [14.1] as a shared system script?

### [33] `make-buy.decision.js`
- **Purpose:** decision/action step (buy/sell); reads the mode (test/live) from config; may call shared blocks in [14.3] via [30.1].
- **Open:** Is the decision made by code, the LLM, or both (the LLM proposes, code enforces risk limits, vision §5.3)?

### [34] `logs/` (real folder; was `logs.link/`)
- **Purpose:** the agent's own logs: per-run inputs used, reasoning, decisions, actions, cost, `effective-config.json`. [34.1] are file links to shared log files it needs, only if needed (e.g. its data worker's `latest.log`; D-020). Its strategy (and so the UI, level by level) sees this folder through [21.4.1.1] (D-030).
- **Open:** Should it be one JSONL decision log plus an MD run summary per run?

### [35] `data/` (real folder)
- **Purpose:** the agent's own data: [35.2] `[worker-or-source]/`, one folder per producer (own workers, own outputs, decisions). [35.1] are file links to the data files it uses: its domain's worker outputs ([19.5.2], [19.5.3]), shared worker outputs [16.2], sub-agent outputs [16.3], or another agent's outputs (D-020). Its strategy sees this folder through [21.5.1.1] (D-030).
- **Open:** Where are portfolio/positions stored (in [35.2], or a ledger, vision §5.4)?

### [36], [36.1], [36.2] (retired)
- The per-worker data links, the central own-data link and the sub-agent data link are replaced by individual file links [35.1] (D-020) and real own data in [35.2] (D-014).

### [46] `docs/` (agent's own docs, real folder; D-017)
- **Purpose:** the agent's own docs, in its folder like its configs/scripts/logs/data.
- **Contents:** [46.2] `README.md` (what it is, parent variant, route, mode) · [46.5] `strategy.md` · [46.6] `changes.md` (exactly what differs from its parent / what is being tested) · [46.7] `decisions.md` (notable decisions summary; raw decisions stay in [34]) · [46.8] `notes.md` (owner comments and answers). One tree line each since 2026-10-07, so each has its own How it works and metadata files (D-057). [46.3] `vision.md` (what makes it different from its siblings, what it is testing, results so far, what comes next; the vision skill's "Trading agent" outline, D-034) and [46.4] `rebuild-prompt.md` (how an AI builds this agent's folder again exactly: its settings, prompt, scripts and links, assuming the levels above exist; D-053, added 2026-10-07). Not written yet. [46.1] are file links to the shared docs it needs (e.g. `safety.link.md`, `agent-architecture.link.md`; D-020).
- **Writers / readers:** create-agent [14.1] scaffolds it; the agent itself, its strategy SI sub-agent [21.1.1.1] and the domain agent [19.1.5] update it. The owner and the UI read it here, or from its strategy through [21.6.1.1] (D-030).
- **Updated:** on creation, on every change tested, and when the owner comments.
- **Resolved:** the "what changed in this variant" record is `changes.md` here; the strategy SI sub-agent keeps the cross-variant history in [21.5] `data/` (D-022/D-025).
- **Open:** Should the agent be allowed to edit its own docs, or only its SI/domain agent?

### [46.2] `README.md` (the trading agent's README)
- **Purpose:** what this agent is: its parent variant, its route (platform and model), its mode (test or live) and its status, with pointers to its other docs.
- **Writers / readers:** create-agent [14.1] writes it at creation; the agent, its strategy SI sub-agent [21.1.1.1] and the domain agent [19.1.5] keep it current. The owner, the UI and the agent at each run read it. Format proposed.

### [46.5] `strategy.md`
- **Purpose:** the strategy this agent runs, in plain words: what it looks for, when it buys and sells, and its limits.
- **Writers / readers:** written at creation from its strategy [21]; changed only together with the agent's config [27]. The agent reads it at each run; the owner and the UI read it here. Format proposed.

### [46.6] `changes.md`
- **Purpose:** exactly what differs from its parent and what is being tested, including its links: `+ to <- from: why` for an added link, `- to: why` for a removed one.
- **Writers / readers:** written when the variant is created or changed (create-agent [14.1], the strategy SI sub-agent [21.1.1.1]); read by the owner, the UI and the strategy when it compares variants. Format proposed.

### [46.7] `decisions.md`
- **Purpose:** a short summary of the agent's notable decisions; the raw records stay in its logs [34] (`runs.jsonl`).
- **Writers / readers:** the agent adds to it after a run with a notable decision; the owner, the UI and the strategy read it. Format proposed.

### [46.8] `notes.md`
- **Purpose:** the owner's comments on this agent and the answers to them, newest last under `## YYYY-MM-DD HH:MM [who]`.
- **Writers / readers:** the owner (on the page) and the agents that answer; the agent reads it at each run. Format proposed.

### [37] (moved to [24.5]: `CLAUDE.md` now sits inside `.claude/`, D-024)
- Level equivalents moved the same way: [10.3] → [10.1.5], [19.7] → [19.1.5], [21.7] → [21.1.5].

### [24.5] `.claude/CLAUDE.md` (trading agent prompt; D-024)
- **Purpose:** the main agent's instructions: strategy, run loop, allowed actions, links to config/docs. Every level has one: [10.1.5] system manager, [19.1.5] domain owner, [21.1.5] strategy manager, [24.5] trading agent.
- **Open:** Is it composed from the common prompt [2.17.3] plus an agent prompt (v0.1 idea): by `@import`/link, or copied in at creation?

### [38] `package.json`
- **Purpose:** JS/TS dependencies and npm scripts (`start`, `test`).
- **Open:** Should dependencies be per agent or shared via a workspace at the root?

### [39] `requirements.txt`
- **Purpose:** Python dependencies.
- **Open:** Should each agent have its own venv, or share one?

### [40] `init.sh` (every level has one: [10.6], [19.10], [21.10], [40])
- **Purpose:** setup, re-runnable: install deps, then run `relink --agent [self]` [14.1] (D-031), which builds the agent's file links from its links file [27.3] ([27.1], [30.1], [30.3], [34.1], [35.1], [46.1]; D-020) and its entry in each of its parent's `subagents.link/` folders (D-030: a trading agent in its strategy's [21.2.2.1]–[21.13.3.1], a strategy in its domain's, a domain in the system's); register in the index [2.18] and UI. The system's `init.sh` [10.6] also installs the git hooks that run relink at review time, and runs relink for the whole project.
- **Resolved (D-031):** links are rebuilt automatically after every change to a links file, by `relink` [14.1], without re-running `init.sh`.
- **Open:** Is it generated by the create-agent script [14]?

### [41] `start.sh` (every level has one: [10.7], [19.11], [21.11], [41])
- **Purpose:** start the agent: one run. The central scheduler [14.1] calls it for the agent's main-run job in its workers file (D-029, proposed); the owner can also run it by hand.

### [42] (retired: the copy-trading domain leaves the tree, owner 2026-10-07, D-056)
- **Why:** trading lives in the prediction-market domain [19]; a later trading domain, such as copy trading, is copied from it when the owner asks ("another trading domain later should be just templated if needs from the prediction market agent").
- **Gone with it:** the cross-domain links to its `top-traders` and `whale-signals` files (the trading agent's `whale-signals.link.json` [35.1] and the domain's `top-traders` link). Its open questions (which wallets to copy first, who produces those files) wait for that domain.

### [43] `apps/`
- **Purpose:** applications and projects, our own or from GitHub: the owner's IDE [53] `project-IDE/` (moved here, owner 2026-10-05 15:17, D-043) and the prediction-market domain's dashboard [45] `trading-ui/` (moved here, owner 2026-10-06, D-045; the domain's app, D-058). An outside app gets its own folder here when one is needed; the tree shows no example of one (owner, 2026-10-06).
- **Every app has its own docs (owner, 2026-10-06 22:06, D-055):** "apps folder also will contains apps and inside them docs". Each app's `docs/` holds `vision.md`, `README.md` and `rebuild-prompt.md` (for the IDE: [53.4]). For an outside app these three are its only metadata for now ("the app metadata for now only nessasary for this 3 files"): no How it works or Details for each of its files.
- **Two kinds of outside code (D-055):** a research clone goes to [55] `temp/` first, never committed, with its docs only on request. An app we use is forked on GitHub and kept in `apps/<name>/`: `docs/` (ours) and `repo/`, our fork (as a git submodule, proposed). In the fork, `main` is ours and `upstream` follows the source; from time to time `upstream` is updated from the source and merged into `main` (owner: "forked and made new main branch where we ll once in a time merge udpate from the source and then merge them in our main fork"). Every app has a row in [2.18.5].
- **Later, on request (D-055):** a skill (`adopt-app`, proposed) turns an app fully into the system's way: Details for every file, one job per file, features and the other docs. It is kept up like every skill. Not written yet.
- **Open:** Can agents clone new repos on their own? Does the Polymarket suite v2 come in as a forked app (a question for the prediction-market domain, [19.6.13])? Submodule or ignored clone for `repo/`, where the forks live on GitHub, how often to update (plan `2026-10-06-2206-apps-docs-clones-forks.md`).

### [44] (retired: the example `apps/[some-github-repo]/` is gone, owner 2026-10-06, D-045)
- **Owner (2026-10-06):** it was only an example that `apps/` holds apps and projects, our own or from GitHub; `trading-ui/` [45] moves here instead. Its open question went to [43].

### [47] `.secrets/` (D-023, D-027, D-041)
- **Purpose:** the single store for private keys, wallet keys, API keys and tokens for outside accounts (such as the prediction-market domain's trading accounts, [19.2.4] `accounts`) and platforms [11.11] `platforms`.
- **Location (proposed):** repo root, **outside `agents/`**, so no agent or level session (which run inside `agents/…`) has it in its folder, and no `subagents.link/` or file link reaches it. Git-ignored via [48]. Folder `chmod 700`, files `chmod 600`, owned by the user that runs the scripts. Stronger option: keep it outside the repo entirely (e.g. `~/.agent-os/secrets/`) with the same layout.
- **Contents (D-027 updates D-023):** [47.1] `test/.env` holds **all** test keys in one file (`KEY=value`, keys prefixed per account/platform, e.g. `POLYMARKET_ACCT1_API_KEY` in the prediction-market domain); [47.2] `live/.env` will mirror it with the same key names and live values (later phase; the owner decides per key which values stay the same and which change, e.g. real-money accounts). Splitting into one file per account can come later if the file gets unwieldy. [47.3] `secrets.index.json` with metadata only: `{ "[ref]": { "kind": "wallet|api-key|token", "env": "test|live", "used_by": ["[account-id]"], "created", "rotate_by" } }`, never values.
- **Access (D-027):** agents and the dev workflow may read and update `test/.env` (safe test credentials; content grows with the project, no fixed schema yet). Nobody but the owner writes `live/.env`; agents never get write access to it. Each level's `.claude/settings.json` denies `.secrets/live/**` (not all of `.secrets/**` any more).
- **Loading (proposed, D-027):** nothing opens the file inline. An agent or worker declares the keys it needs in its own config (e.g. `"secret_keys": ["POLYMARKET_ACCT1_*"]`). The shared loader `load-secret` [14.1] (shell + Python twin) reads `.secrets/[test|live]/.env` and exports only those keys into the child process of that run: `load-secret POLYMARKET_ACCT1_* -- python3 scripts/get-polymarket-data.worker.py`. The mode comes from `AGENT_OS_ENV` (default `test`); `live` is refused unless the run is owner-approved. A missing key fails fast with the key name. The loader logs only key names, mode and result, never values.
- **Editing from a UI (owner request):** create/edit keys from the local trading UI [45] (it runs next to the files; values never leave the machine). The planning explorer page cannot and should not hold secret values.
- **Access rule (proposed):**
  - Agents never get a link or copy of anything in here; `check-links` [14.1] fails on any link or file whose target is inside `.secrets/`.
  - Configs hold only key names (`secret_keys`, D-027) or refs ([19.2.4] `accounts`, [11.11] `platforms`), never values.
  - Scripts that act (executor/decision [14.3], [33]; workers that call private APIs) call `load-secret` [14.1] at execution time. It returns the value only if that agent's config references the ref, and `live/` refs only if the owner approved the agent for live ([11.1] `modes`; in the prediction-market domain also a funded, owner-approved account, [19.2.4] `accounts`).
  - **Live values never in LLM context:** they are passed to the script process only (env injection), never into prompts or Claude Code sessions. Each level's `.claude/settings.json` ([10.1.6], [19.1.6], [21.1.6], [24.6]) denies `.secrets/live/**`. Test values may be seen by an agent that updates `test/.env` (D-027); they are still never copied into configs, docs, data or logs.
  - **Never logged:** loggers redact anything resolved by `load-secret`; [2.14] schemas forbid secret fields in data/logs.
- **Test vs live:** separate folders and separate refs. A test agent can never resolve a `live/` ref.
- **Rotation (proposed):** `rotate_by` in [47.3]. The notifier warns before expiry. Rotation writes a new value under the same ref (configs stay unchanged), then revokes the old key at the provider. Runbook in [2.11.6].
- **Writers / readers:** the owner writes live keys; agents may read and update the test `.env` (D-027). Scripts get only the keys their config declares, through `load-secret` [14.1].
- **Upgrade path (later):** replace the file backend of `load-secret` with the OS keychain, a password manager CLI (e.g. 1Password) or a vault (e.g. HashiCorp Vault). The `secret_keys` lists and the configs stay the same.

### [47.1.1] `.secrets/test/.env` (D-027; owner edits 2026-09-30)
- **Purpose:** one file with every test credential as `KEY=value` lines, grouped in comment sections per type of variable (mode, models, platforms/accounts, notifications, optional), keys prefixed per account or platform (e.g. `POLYMARKET_ACCT1_API_KEY`).
- **One file (owner, decided):** no splitting into many files; prefixes plus sections are enough. If that ever stops working it is split later; it is not an open question now.
- **Who loads it (owner, decided):** scripts. Workers, decision and system scripts get their keys through the shared loader `load-secret` [14.1] at the start of a run, so values live only in that process. Sub-agents normally get no secrets; they call scripts that already have them.
- **Agent access in test mode (owner, decided):** agents and the dev workflow may read and update this file. An agent may read a value itself when no script provides it (a quick API check, setting up a new account); no extra logging is needed. This holds only for `test/`.
- **Variables tab (owner, decided):** the page's Variables tab is the current picture of the real local file, not a copy of the example: one row per key really in the file (section, what it is for, which files or scripts read it, required, format, notes). Empty for now; never holds values. New keys go in the matching section with the account/platform prefix and get a row there.
- **Editing:** keys are created and edited from the local trading UI [45], which runs next to the files, so values never leave the machine. The planning page never holds secret values.

### [47.2.1] `.secrets/live/.env` (D-027; owner edits 2026-09-30)
- **Purpose:** the live twin of [47.1.1]: the same single-file shape, the same sections and key names, live values. Later phase: not created yet.
- **Same names, different values:** nothing in the code changes between modes. The owner decides per key which value stays the same (non-sensitive config) and which must be a real live value (real-money accounts, live API keys). A key added to `test/.env` is added here too, in the matching section.
- **Access (owner, decided):** only the owner edits it. No agent reads or writes it; reading `.secrets/live/**` is denied at every Claude Code level. Scripts get live keys only through `load-secret`, only for owner-approved live runs.

### [47.3] `.secrets/secrets.index.json` (D-023; owner edit 2026-09-30)
- **Purpose:** metadata about every key (ref, kind, env, used by, `rotate_by`); never values.
- **Always in sync (owner, 2026-09-30):** every time a key or key group is added, renamed or removed in [47.1.1] or [47.2.1], the matching entry here changes in the same change. This happens automatically, not by hand: the knowledge agent [10.1.1.2] processes every system change (D-033) and updates the files that depend on it, including this index and any config that lists `secret_keys` (proposed).
- **Check (proposed):** a `check-secrets-index` script next to `check-links` [14.1] compares the key names in the .env files with the entries here and fails when they drift apart. It reads key names only.
- **Open:** What triggers the sync: a git hook, a scheduled run, or the session that edited the .env file? How are key names read from `live/.env` without reading values (names-only read, or the owner runs it)?

### [48] `.gitignore` (D-028)
- **Purpose:** keep secrets, local machine state and generated runtime files out of git, while keeping every shared config and folder structure in the repo. Each entry carries a comment saying why (D-028).
- **Content (owner edit on the page, 2026-09-30):**
  ```text
  # Secrets: never commit credentials (D-023, D-027)
  .secrets/
  *.env
  .env.*
  !.env.example

  # Claude Code local state: machine-specific, not shared (D-024)
  **/.claude/settings.local.json
  **/.claude/agent-memory-local/

  # Cursor local state: same rule as .claude - only local files, the rest is committed
  **/.cursor/settings.local.json
  **/.cursor/state/
  **/.cursor/cache/

  # Runtime logs: written by agents at run time, not source
  logs/**
  !logs/**/
  !logs/**/.gitkeep
  agents/**/logs/**
  !agents/**/logs/**/
  !agents/**/logs/**/.gitkeep

  # Runtime data: produced by agents/workers, not source
  data/**
  !data/**/
  !data/**/.gitkeep
  agents/**/data/**
  !agents/**/data/**/
  !agents/**/data/**/.gitkeep

  # Research clones: outside code we only study, never committed (D-055)
  apps/temp/*/repo/

  # Dependency and build artifacts: regenerated, not source
  node_modules/
  dist/
  build/
  .venv/
  venv/
  __pycache__/
  *.py[cod]
  *.egg-info/
  .pytest_cache/
  .mypy_cache/

  # OS and editor noise
  .DS_Store
  *.swp
  .idea/
  .vscode/

  ```
- **Rules (owner, 2026-09-30):** logs and data are runtime output: their content is ignored, but the folders stay in git through `.gitkeep` files, so a fresh clone has the right shape without any run output. Local-only tool state is ignored for both `.claude/` and `.cursor/` (`settings.local.json`, local memory and state folders); every shared `.claude/` and `.cursor/` file (agents, skills, shared settings) is committed. Every ignore line has a comment saying why.
- **Resolved (owner, 2026-09-30):** runtime `logs/` and `data/` content is ignored (was open).

### [49] `tests/` (agent level; D-025, D-041)
- **Purpose:** the agent's tests, so every change (by the owner, create-agent or the SI sub-agent) can be checked before and after it runs. Same at every level: [10.8], [19.12], [21.12]. Layout and rules in [2.7.3], fields in [2.14].
- **Contents:** [49.1] `agents/`: tests of [24.5] `CLAUDE.md` and [26] sub-agents ([49.1.2] scenario files, [49.1.1] `tests.config.json`, [49.1.3] runner link). [49.2] `scripts/`: tests of [31]–[33] and linked scripts ([49.2.2] test files, [49.2.1] `tests.config.json`, [49.2.3] runner link). Results are written back to the configs and appended to [34.2] `logs/tests.jsonl`.
  - [49.1] `agents/`: tests of the agent's prompt and sub-agents. Run with `node tests/agents/run-tests.system.link.js [--id t-agents-001]`. Each test runs Claude Code headless in a temporary copy of the agent folder on the test's fixtures, in test mode, with no secrets, and is graded by script checks or a judge sub-agent (see [2.7.3]).
  - [49.1.3] `run-tests.system.link.js`: file link to the shared [14.1] `run-tests.system.js`. Because it is called from `tests/agents/`, it presets `--kind agents` and reads [49.1.1] `tests.config.json` in this folder.
  - [49.2] `scripts/`: tests of the agent's scripts and linked scripts. Run with `node tests/scripts/run-tests.system.link.js`; each `[test-id].test.[js|py]` runs with node or pytest on fixture data, no network, no secrets.
  - [49.2.3] `run-tests.system.link.js`: the same link; called from `tests/scripts/`, it presets `--kind scripts` and reads [49.2.1].
  - [30.2] `scripts/run-tests.system.link.js` stays: it runs both kinds (used by the scheduler, `before_promote` and `npm test`).
- **Writers / readers:** create-agent scaffolds empty configs. The SI sub-agent and system-support agents add tests. The owner enables/disables tests from the UI. `run-tests` writes the state fields. The UI, the SI sub-agent and promote-to-live [2.11.4] read them.
- **When tests run (proposed):** per test `schedule`: `manual`, `on_change` (the target file changed; via the scheduler [14.1]), `interval:[x]`, `before_promote`.
- **Open:** Is a backtest (strategy on past data) a test here, a research item [50], or both (research runs it, a test guards the result)? Should a failing test block the agent's runs, or only promotion?
- **Example** `tests/scripts/tests.config.json`:
  ```json
  {
    "schema_version": 1,
    "level": "pm-strategy-1.momentum-v1.opus55-test",
    "kind": "scripts",
    "tests": [
      {
        "id": "t-scripts-001",
        "name": "make-buy respects max position size",
        "target": "scripts/make-buy.decision.js",
        "file": "tests/scripts/t-scripts-001.test.js",
        "enabled": true,
        "schedule": "on_change",
        "owner": "pm-strategy-1-self-improvement-agent",
        "last_run": "2026-09-29T10:00:00Z",
        "last_result": "fail",
        "last_duration_ms": 420,
        "fail_count": 1,
        "notes": "cap ignored when two signals arrive in one run",
        "next_action": "fix the cap check in make-buy, then re-run"
      }
    ]
  }
  ```

### [50] `research/` (agent level; D-025)
- **Purpose:** the history of research done for this agent: what was asked, what was found, what was decided. Same at every level: [10.9], [19.13], [21.13] (strategy-level research on its variants usually lives at [21.13]).
- **Contents:** [50.1] `index.json`, one entry per item. [50.2] `[research-id]-[slug]/`, one folder per item with `README.md` (question, method, results, decisions) and its artifacts.
- **Writers / readers:** mainly the level's SI sub-agent. Also the owner (requests), domain/strategy agents and system-support agents. The UI shows the index; the SI reads past items before starting new ones, so it does not repeat work.
- **Replaces:** research kept in the level's `data/` (D-022/D-024).
- **Example** `research/index.json` entry:
  ```json
  {
    "id": "r-0001",
    "slug": "momentum-window-length",
    "topic": "signal tuning",
    "question": "Does a 6h momentum window beat 24h on the markets this agent trades?",
    "status": "done",
    "started": "2026-09-20T09:00:00Z",
    "finished": "2026-09-22T18:00:00Z",
    "ran_by": "pm-strategy-1-self-improvement-agent",
    "requested_by": "owner",
    "folder": "research/r-0001-momentum-window-length/",
    "results_summary": "6h window: higher hit rate in test mode, more trades, similar drawdown.",
    "decisions": [
      { "decision": "create variant v2 with a 6h window", "by": "pm-strategy-1-self-improvement-agent", "approved_by": null, "date": "2026-09-22", "decision_ref": null }
    ],
    "links": ["data/get-polymarket-data/2026-09.json", "logs/runs.jsonl"],
    "related": { "agents": ["pm-strategy-1.momentum-v2.opus55-test"], "changes": ["pm-strategy-1.momentum-v2.opus55-test/docs/changes.md"], "tests": ["t-scripts-001"], "research": [] },
    "tags": ["momentum", "window"]
  }
  ```

### [45] `apps/trading-ui/` (moved from the root, owner 2026-10-06, D-045)
- **Purpose:** Next.js API + UI for monitoring and control (vision §12).
- **Now (owner, 2026-10-06):** empty for now. It may never be needed: the project IDE [53] may do this job.
- **Not the IDE (D-041):** the owner's File Tree page and its data are in [53] `apps/project-IDE/`; this folder is the trading dashboard, built later.
- **The domain's app (D-058):** it stays here, where the owner put it, as the prediction-market domain's dashboard; the system's own view is the project IDE [53].
- **Open:** Does it read the JSON/MD files directly or through an API layer? How is it accessed (local only, auth)?


### [53] `apps/project-IDE/` (owner request, D-041)
- **Purpose:** the owner's IDE for the project: the File Tree page they use to understand, watch and steer the project (D-040), and everything the page needs. It sits in `apps/` [43] with the other applications (owner, 2026-10-05 15:17, D-043), and it can be rebuilt from either place the owner works (the cloud project or their own server).
- **Contents:** [53.1] `current-ui/` (the page as published now), [53.3] `server/` (the page on the owner's server with Claude Code behind it) and [53.2] `data/` (this project's knowledge and the data the page is built from).
- **Writers / readers:** the project IDE agent [10.1.1.3] builds and publishes the page with ide-build [10.1.2.5] and folds the owner's notes and edits back in with ide-sync [10.1.2.6]; the knowledge base agent [10.1.1.2] keeps the knowledge in [53.2]. The owner uses the page; every Claude reads [53.2] to catch up.
- **Not here:** the trading dashboard, which is [45] `apps/trading-ui/`; the IDE's agent and skills, which live with the system's other agents and skills in [10.1].
- **Server (D-042, D-043):** the page also runs on the owner's server, with Claude Code behind its request box [53.3] (plan [53.2.5] `server-ide.md`).
- **What it is for (owner, 2026-10-06 20:47, D-049):** "that i can easly mange, analayse, view the system with and this interface, and ai always know all related and needed context to more precisely make all changes". For any file the IDE shows, to the owner and to every AI, what it is for, how it works, what depends on it, what must change with it and what holds for it from the levels above.

### [53.4] `apps/project-IDE/docs/` (owner, 2026-10-06, D-055)
- **Purpose:** the IDE's own docs, like every app's in [43]: [53.4.1] `vision.md` (what the IDE is for: the owner's window on the project and the whole context for every AI, D-040, D-049), [53.4.2] `README.md` (its parts: the page [53.1], the server [53.3], the data [53.2], with each part's docs path) and [53.4.3] `rebuild-prompt.md` (how to build the IDE again exactly).
- **Written by:** the knowledge base agent [10.1.1.2] with the vision, README and rebuild prompt skills ([10.1.2.3], [10.1.2.4], [10.1.2.7]), using their outline for an app.
- **When (proposed):** with the docs at every level (plan `2026-10-06-2143-general-system.md` step 5), so they are written once inside the new hierarchy. Until then the system's README and rebuild prompt describe the IDE.

### [53.1] `apps/project-IDE/current-ui/` (D-041)
- **Purpose:** the File Tree page as the owner uses it now: its source and the data file it loads.
- **Contents:** [53.1.1] `file-tree-explorer.html`, [53.1.2] `file-tree.data.json`.
- **Writers / readers:** the project IDE agent [10.1.1.3] (ide-build [10.1.2.5]) rebuilds the data, tests the page and republishes it at the same link; the owner opens it.
- **Updated:** after every round that changes the tree, a doc or a How it works file.

### [53.1.1] `file-tree-explorer.html` (D-041)
- **Purpose:** the page itself: the tree with search and filters, and for every file and folder its tabs (How it works, File, Example, Questions, and extra tabs such as jobs, links, tests or key names). The owner can edit a file or its How it works, leave notes and messages and ask questions; all of that waits in the page's own store until the next sync (ide-sync [10.1.2.6]).
- **Voice button (owner, D-060):** on the owner's server, the request box and the delete note box have a microphone button: press to record, press again to stop (at most 5 minutes, with a timer); the server turns the recording into text [53.3.5] and the page adds it to the box to check and send. On claude.ai the button is hidden, because a claude.ai page gets no microphone and cannot reach Groq.
- **Index files in the tree (owner, 2026-10-05 14:03):** every file and folder shows its `.index.md` as its own row (a file's right under it, a folder's first inside it); clicking it opens the item's How it works, which is that file. A `☑ metadata` switch above the tree hides or shows them, together with the Details files (`.meta.json`) since D-057; the filter finds them by name ("README.index").
- **On its own File tab (owner, 2026-10-05 14:21):** the page shows its own source, the same file that is published. `enrich.py` [10.1.2.5.2.3] reads it from `explorer/` when it builds the data, so the finished page goes there first. A long file shows 3,000 lines at a time with a button for more, and its size.
- **Opened elsewhere (owner question, 2026-10-05 14:33):** served by any web server next to [53.1.2], it shows the same page, view only: saving and asking Claude come from claude.ai, so the header says "view only" and a message sent there says it reaches no one. Opening the file straight from disk does not load the data. The claude.ai link changes only when the files are published to it again.
- **Opening folders (owner question, 2026-10-06 11:29):** folders start closed except the top levels, so a file deep inside (such as the system's `vision.md` or the vision skill) shows only once its folders are open; the search opens the folders on the way to each match. A first click on a closed folder now opens it as well as selecting it; a click on the selected folder, or on its arrow, closes it again.
- **Apply changes (owner, 2026-10-06, D-046):** a button at the top of the page, with the number of items marked changed, carries every change waiting on the page into the files and shows the new tree. On claude.ai it posts one comment on the page and sends it to Claude (the page's `comments` capability); the Claude watching the page runs ide-sync [10.1.2.6] and ide-build [10.1.2.5], publishes the new tree, answers the comment and resolves it. The request is also saved in the page's store as an input of kind `apply`; when that input turns processed, the open page loads the new tree or asks the owner to reload. When no Claude is watching, the page keeps the request and asks the owner to say "sync the file tree" in the project chat. On the server [53.3] it starts one Claude Code run with the same request in the top folder's chat.
- **Proposed:** a routine that checks the page's store on a schedule and runs ide-sync [10.1.2.6] when something is waiting, so the owner need not press Apply changes.
- **On the server (D-042, D-043):** when the page finds the server's service [53.3] next to it, it saves straight into the files and sends requests to Claude Code instead of using the page's store; it is no longer view only there.
- **Delete (owner, 2026-10-05 15:45, D-044):** every file and folder except the top has a Delete button next to its name. It opens a short form: what goes (a folder with how many items inside), an optional note for Claude about what to keep in mind, and "Delete and clean up". On the server the page sends it to Claude Code at once [53.3.3]; on claude.ai it is marked deleted and cleaned up at the next sync (ide-sync [10.1.2.6], "Deleting an item"). The deleted item stays in the tree, struck through, until the sync, with "Restore it" (claude.ai) or "Bring it back" (server, again through Claude Code). The deletion and the note are filed as an input.
- **One status: changed (owner, 2026-10-05 15:45, D-044):** the page shows no statuses for now (no dots, no legend, no exists, decided, proposed, name pattern or example agent). A "changed" tag marks whatever a request from the page touched: an edit, a note, an added or deleted item, a request in the box, and on the server every file Claude Code changed for a request. The marks stay until the next sync, and the Changed tab lists them. More statuses may come later. The tree notes keep decided and proposed for the agents.
- **Published at:** https://claude.ai/artifact/72v2Uppt6jpfXLCjKNX9xs.
- **Draft:** `/mnt/project-files/vision/explorer/file-tree-explorer.html`.

### [53.1.2] `file-tree.data.json` (D-041)
- **Purpose:** everything the page shows, in one generated file: every item with its notes, status, example, content, How it works, knowledge and tabs, plus the lists of inputs, decisions and docs.
- **Writers / readers:** built by `enrich.py` [10.1.2.5.2.3] from the tree notes [2.13], the drafts, the knowledge and the `.index.md` files (D-039); never edited by hand and never merged by hand (rebuilt after any merge). The page loads it.
- **On its own File tab (owner, 2026-10-05 14:21):** the file cannot hold a copy of itself, so the page shows it exactly as it loaded it, read-only.
- **Draft:** `/mnt/project-files/vision/explorer/file-tree.data.json`.

### [53.3] `apps/project-IDE/server/` (D-042, D-043)
- **Purpose:** the File Tree page on the owner's own server, with an agent behind its request box: a request typed on the page goes to Claude Code working in the repository from the system folder `agents/system/` (D-043), with the system's `CLAUDE.md` [10.1.5], the knowledge base agent [10.1.1.2], the project IDE agent [10.1.1.3] and their skills. Claude Code can answer, change files, add items, run a skill or an agent; the page shows its progress and reloads the tree when it is done. Notes, comments and edits made on this page go straight into the files, with no sync.
- **Contents:** [53.3.1] `README.md`, [53.3.2] `server.py`, [53.3.3] `claude_bridge.py`, [53.3.4] `server.config.json`, [53.3.5] `voice.py`.
- **One page, two homes:** the page [53.1.1] is the same file. On claude.ai it keeps notes in the page's store and asks Claude on the page; on the server it finds this service next to it and uses it instead.
- **Built (D-043):** the four files are written and tested on a copy of the repository; it goes live on the server after the GitHub sync.
- **Safety:** listens only on the machine (127.0.0.1); the owner reaches it through an SSH tunnel or a private network, never the open internet, because whoever reaches it can make Claude Code change files and run commands. Claude Code never reads `.secrets/` [47], never pushes, deletes or acts live (in trading: touches real money) without the owner's click; checks before every tool call enforce it.
- **Writers / readers:** the project IDE agent [10.1.1.3] looks after it; the owner starts it on the server. Each request is filed as an owner input [2.10] like any message, and logged with its cost and time in [15.4].
- **Plan:** [53.2.5] `server-ide.md`.
- **Open:** how the claude.ai link gets updated from the server (Claude Code signed in to the owner's claude.ai account, or the cloud project republishes after a pull).

### [53.3.1] `apps/project-IDE/server/README.md` (D-043)
- **Purpose:** for the owner: what is needed on the server, how to start the service and reach it through an SSH tunnel, what happens to notes, edits and requests, which steps wait for the owner's click, and every setting.
- **Draft:** `/mnt/project-files/vision/server/README.md`.

### [53.3.2] `server.py` (D-043)
- **Purpose:** the web service, standard library only: serves the page [53.1.1] and its data [53.1.2] from the repository; keeps the page's store (notes, edits, messages, changes) as JSON files in [53.2.7] `page-store/`, so the page works as on claude.ai; writes an edit to a file's text straight into the file and an edit to How it works into its `.index.md` (`by: owner`), never inside `.secrets/` [47] or outside the repository; hands requests to [53.3.3] and streams their progress to the page. It answers only to the machine's own address and refuses to listen on any other. Write-through writes only what a save changed, so saving the same item again (a comment, a "changed" mark) never writes an older page edit over a file Claude Code has changed since (D-044).
- **Draft:** `/mnt/project-files/vision/server/server.py`; tested on a copy of the repository (page, store, write-through, a real Claude Code request, owner approvals).

### [53.3.3] `claude_bridge.py` (D-043)
- **Purpose:** runs each request as a Claude Code session through the Claude Agent SDK, started in the system folder `agents/system/` (owner, 2026-10-05 15:17), so the system's agents and skills in `agents/system/.claude/` [10.1] load as its own, with the system's `CLAUDE.md` [10.1.5] (D-045); a follow-up in the same box continues the same session. Before every step: anything touching `.secrets/` [47] is refused; a file outside the repository and every tool or command not on the allow list of [53.3.4] (push, delete, installs, network tools) wait for the owner's Allow or Refuse on the page (refused after 15 minutes). Streams text, steps, questions and the result with cost and time; logs each request in [15.4], with every step that waited for the owner in full.
- **Delete from the page (D-044):** a Delete pressed on the page runs as a request of its own: Claude Code deletes exactly that item and its How it works file with one command that needs no second click (any other deletion still waits for the owner), cleans the project of it as ide-sync [10.1.2.6] says, keeping the owner's note in mind, files it and commits. "Bring it back" restores it from git the same way. After each request it tells the page every file that changed, also when Claude Code committed them, so the page marks them changed.
- **Draft:** `/mnt/project-files/vision/server/claude_bridge.py`.

### [53.3.4] `server.config.json` (D-043)
- **Purpose:** the server's settings: address and port (127.0.0.1:8765), the page and store folders, write-through on or off, the keys file and the key names Claude Code gets (`ANTHROPIC_API_KEY`; values stay in `.secrets/test/.env` [47.1]), where Claude Code starts (`agents/system`), the model (empty: Claude Code's default, later from [11.11]), limits per request (turns, dollars), the allow list, the words that always wait for the owner (`git push`, `rm `, `curl `, installs ...), the paths nothing may touch, the log folder.
- **Voice (D-060):** `secrets.keys` also names `GROQ_API_KEY`, which only `voice.py` [53.3.5] gets, never Claude Code; `voice` lists the Groq address, the models in the order they are tried (`whisper-large-v3-turbo`, then `whisper-large-v3`), the key name, the 300-second limit and the language (empty: detected).
- **Draft:** `/mnt/project-files/vision/server/server.config.json`.

### [53.3.5] `voice.py` (owner, D-060)
- **Purpose:** voice input for the page's request boxes. The page records up to 5 minutes in the browser and posts the audio to `api/voice` on the server [53.3.2]; this module sends it to Groq's speech-to-text API and returns the text, which the page adds to the box for the owner to check and send. It tries the models listed in the config [53.3.4] in order; a model that answers with a rate limit is skipped until its wait is over, and an error moves on to the next one. The recording is not kept. Standard library only.
- **Key:** `GROQ_API_KEY` from the keys file `.secrets/test/.env` [47.1]; the value never reaches the page, the logs or Claude Code.
- **Writers / readers:** the project IDE agent [10.1.1.3] keeps it; the server calls it.
- **Draft:** `/mnt/project-files/vision/server/voice.py`; tested with a stand-in for Groq (a rate limit on the first model, the answer from the second) and on a test server with a recorded voice message in the browser. Groq itself was not reachable from the planning machine.

### [53.2] `apps/project-IDE/data/` (owner request, D-041)
- **Purpose:** this project's knowledge and the data the page is built from, in one place any Claude can read to catch up: every owner input, the decisions and the changelog, the tree notes, the knowledge map, the notes behind the people docs, the owner's page edits, the working notes, the plans and retired files.
- **Contents:** [53.2.1] `README.md`, [2.13] `file-tree.md`, [2.6] `decisions.md`, [2.9] `changelog.md`, [2.10] `inputs/`, [2.18.8] `knowledge-map.json`, [53.2.2] `sources/`, [53.2.7] `page-store/` (on the server), [53.2.3] `overrides.json`, [53.2.4] `memory/`, [53.2.5] `plans/`, [53.2.6] `archive/`.
- **Split:** the topic docs agents read while they work stay in [2] `agents/system/docs/`; the docs for people are there too (D-047); the records of how the project got here are here.
- **Writers / readers:** the knowledge base agent [10.1.1.2] (knowledge-intake [10.1.2.1]) writes inputs, decisions, changelog, notes and sources; the project IDE agent [10.1.1.3] reads it to build the page and writes the owner's page edits into it. Every Claude reads it at the start of a round.
- **Draft:** today spread over `/mnt/project-files/vision/`: `docs/` (records and notes), `tools/overrides.json`, `.claude/knowledge/sources/`, `.claude/memory/`, `plans/`, `archive/`.

### [53.2.7] `apps/project-IDE/data/page-store/` (D-043)
- **Purpose:** on the owner's server, the page's own store as files: `nodes/`, `changes/`, `inputs/`, one JSON document per file, the same documents the page keeps on claude.ai. Written by [53.3.2]; read by ide-sync [10.1.2.6], which folds them into the files like the claude.ai store. Requests typed on the page are in `inputs/` with their answer, cost and session.

### [53.2.1] `apps/project-IDE/data/README.md` (D-041; was the knowledge base guide, D-033)
- **Purpose:** how the project keeps its knowledge, for agents: the layers, the knowledge tag format (`<!-- k: id=… applies=… sources=… status=… -->`), and the flow from an input to the docs.
- **Draft:** `/mnt/project-files/vision/docs/README.md`.

### [53.2.2] `sources/` (D-034, D-041)
- **Purpose:** the agent's notes behind each people doc: for each part of the doc, the inputs, decisions and notes it rests on, and its status. The doc's skill reads it to find which parts an input touches. The earlier technical vision notes, whose knowledge tags the map still reads, go here too.
- **Contents:** [53.2.2.1] `[doc].md`, one per people doc (today `readme.md` and `vision.md`).
- **Draft:** `/mnt/project-files/vision/.claude/knowledge/sources/`.

### [53.2.3] `overrides.json` (D-041)
- **Purpose:** the owner's edits from the page that are kept in the page data rather than in a file of their own, such as a draft typed on the page for a file nobody has written yet, keyed by object number. `enrich.py` applies them last, so they win over the parsed notes. Rebuilding without it loses those edits.
- **Draft:** `/mnt/project-files/vision/tools/overrides.json`.

### [53.2.4] `memory/` (D-040, D-041)
- **Purpose:** short working notes for every Claude: how the owner wants us to work, decisions about the way of working, and what is open. One note per file with `MEMORY.md` as the index. It is the shared copy of the cloud project's memory, so a Claude on the owner's server knows the same.
- **Contents:** [53.2.4.1] `[note].md`, plus `MEMORY.md`.
- **Draft:** `/mnt/project-files/vision/.claude/memory/`.

### [53.2.5] `plans/` (D-041, D-051)
- **Purpose:** one plan per change request, written with the `change-plan` skill [10.1.2.8] before anything is built (owner, 2026-10-06 21:43, D-051: "for every change request we should make plans and store them somewhere"); after the build its knowledge moves to the files it belongs to and the plan goes to `archive/plans/` [53.2.6].
- **Contents:** [53.2.5.1] `[plan].md` (`YYYY-MM-DD-HHMM-<subject>.md`; older plans keep their names): `github-sync.md`, `server-ide.md`, `file-set.md`, `2026-10-06-2143-general-system.md`; `index.json`, every plan with its status (proposed).
- **Draft:** `/mnt/project-files/vision/plans/`.

### [53.2.6] `archive/` (D-041)
- **Purpose:** retired files kept for history, one folder per date: old drafts, and How it works files whose object is gone.
- **Contents:** [53.2.6.1] `[date]/`.
- **Draft:** `/mnt/project-files/vision/archive/`.

### [55] `apps/temp/` (owner, 2026-10-06, D-055)
- **Purpose:** repositories cloned from GitHub for research (owner: "first just clone in a temp if it's for research"). Each one is `temp/<name>/`: the clone in `repo/`, never committed ([48]); our `vision.md`, `README.md` and `rebuild-prompt.md` in `docs/` only when the owner asks.
- **Writers / readers:** the agent or session doing the research clones here and writes its findings in its own `research/` ([2.7.3]); the clone is deleted when the research is done. An app we decide to use is forked instead and moves to its own folder in [43].

### [54] (retired: no root `researches/`; research lives inside the agents, owner 2026-10-06, D-045)
- **Owner (2026-10-06):** "now all researches folders inside agents".
- **Now (owner, 2026-10-09, D-061):** all three studies sit in `agents/trading/researches/` [56.2], moved there in the repository by the owner's word: "move it to trading/researches folder".
- **Before (our default, replaced by D-061):** each moves, with its number, into the research folder of the level it serves: [54.1] into the prediction-market domain's `research/` [19.13]; [54.2] into the system's `research/` [10.9]; [54.3] first into the system's, then into the prediction-market domain's (2026-10-07, D-058). The files inside are the research itself; each folder's How it works describes them as a group, so they get no index files of their own. The move happens in the repository at the GitHub sync.

### [54.1] `agents/trading/researches/prediction-market-research/` (real; moved by the owner, D-061)
- **Purpose:** about 57 studies of ways to make money on prediction markets (market making, arbitrage across venues, trading on news and feeds, forecasting models, copy trading and more), each with the evidence on whether it works (`_evidence/`), plus `_pipeline/`, the scripts and notes that produced them. The first Polymarket strategy is chosen from here.
- **Real files:** the page lists every file in it as found in the repository; the folder's How it works describes them.

### [54.2] `agents/trading/researches/self-improving-agents/` (real; moved by the owner, D-061)
- **Purpose:** one study of approaches and architectures for agents that improve themselves; background for the self-improvement helpers at every level. It sits with the trading research because the owner moved the whole folder; whether it belongs to the system's research instead is open.

### [54.3] `agents/trading/researches/trding-agents-arhiteches/` (real; moved by the owner, D-061)
- **Purpose:** how trading agents are built: a README, specs, diagrams and a page that shows them. Background for the trading-agent architecture [19.6.16.1] (name kept as in the repository).
- **Open:** fix the spelling of `trding-agents-arhiteches`?

## Changelog

- **v0.1** – initial skeleton from owner's v0.2 input.
- **v0.2** – detailed [2] `docs/`: proposed files [2.1]–[2.11] with purpose, outline, writers/readers and update rules; `vision.md` moved from [3] to [2.2].
- **v0.3** – added [2.12] `docs/feature-map.md` (owner request): maps features/logic to files; draft created.
- **v0.4** – moved this file from [6] `agents/docs/file-tree.md` to [2.13] `docs/file-tree.md` (owner request); [6] is now a stub; updated references and the [2.1] read order.
- **v0.5** – owner input: added [2.14] `data-schemas.md`, [2.15] `flows.md`, [2.16] `metrics.md`, [2.17] `docs/common/`, [2.18] `docs/index/`, [2.19] `docs/agents/` (per-agent docs, central; agent folder links in via [29] `docs.link/`). Merged `agents/docs/` [5] into `docs/` ([7]→[2.17.1], [8]→[2.18], [9]→[2.17.2]). New `.link` naming rule for every symlink (recorded in [2.7], decision D-002 in [2.6]); example agent renamed/added links [26.1], [27.1], [29], [30.1], [30.2], [34.1], [36], [36.1].
- **v0.6** – detailed [4] `agents/` and [10] `agents/system/` (what belongs where, `.link` mechanics via `init.sh`, promotion rule, when shared changes apply) and [11] `configs/` with proposed files [11.1]–[11.9] and a merge order (defaults → agent type → domain → strategy → agent → owner runtime; risk tighten-only; live only via allowlist + approved account; `effective-config.json` per run). The logs-link direction is still open.
- **v0.7** – owner decision D-006: configs collapsed to two types: [11.1] `system.config.json` (the v0.6 files [11.1]–[11.9] became its sections; [11.3]–[11.9] retired) and [11.2] per-agent configs, central in `configs/agents/[domain]/[agent-name].config.json`, linked into the agent as [27] `config.link.json` (direction proposed). [27.1] is now `system.config.link.json`; [28] is now the `workers` section of the agent config. Merge rule simplified to global → agent → owner UI with the same safety exceptions (proposed). [17] no longer holds routing. The shape and the common/individual split are still open.
- **v0.8** – owner decisions D-007–D-011: [12] workers → scripts [14.2] + definitions in [11.10] `workers.config.json`; [13] sub-agents → Claude Code [10.1.1] in `agents/system/.claude/` (location proposed); [15] logs and [16] data are organised by source ([15.1]–[15.5], [16.1]–[16.4]) and linked into agents as needed (settles the logs-link question: [34] is now `logs.link/`, [34.1] retired); [17] → [11.11] `models.config.json`, and [11.1] no longer has `routing`. Scripts [14] now have sub-folders `system/`, `workers/`, `decisions/` plus a suffix rule; [33] renamed `make-buy.decision.js`; [30.2] retired; new links [25.1], [36.1], [36.2].
- **v0.9** – owner decision D-012: every agent has a globally unique name that is its ID everywhere. Added the naming rule and proposed format to [2.7] (clone → new name/version, no renames, test → live = new agent, no reuse); [2.18.1] is the registry that enforces it; [14.1] `create-agent` is the check point; [2.11.1] and [23] updated.
- **v1.0** – owner input (interpreted as D-013–D-016): `agents/` holds domains only, and `system/` [10] is a domain ([18] `trading-domains/` retired). Every agent has the same real folders `configs/` [27], `scripts/` [30], `logs/` [34], `data/` [35], each with `system.link/` ([27.1], [30.1], [34.1] reinstated, [35.1]). The system domain holds the shared files plus the views [11.2.1], [14.4.1], [15.5.1], [16.4.1] of every agent. `.claude/` at domain ([10.1], [19.1]) and strategy ([21.1]) levels, linked into agents ([25.1]–[25.3], [26.1]–[26.3]). New: [10.2] system-support agents, [27.2] own config file, [35.2] own data. Retired: [36], [36.1], [36.2]. Renamed per D-012: [22], [23]. Added link-cycle rule. Supersedes D-006 (location), D-009/D-010 (agent part).
- **v1.1** – owner decision D-017 (supersedes D-003): docs follow the same pattern as configs/scripts/logs/data. The shared docs [2] moved from top-level `docs/` to `agents/system/docs/` (numbers [2.x] kept; the root keeps only `README.md` [1]). New: agent `docs/` [46] with [46.1] `system.link/` and [46.2] own files; system view [2.20] / [2.20.1]. Retired: [2.19], [2.19.1], [29] `docs.link/`.
- **v1.2** – owner decision D-018: [20] `main-domain-agents/` → domain-owner sub-agent [19.1.1.1] `pm-domain-owner-agent.md`; [22] SI agent folder → SI sub-agents at every `.claude/` level ([10.1.1.1], [19.1.1.2], [21.1.1.1]); their memory/state in [16.3] (proposed); [2.18.3] extended; [20], [22] retired.
- **v1.3** – owner decision D-019: `.claude` links go parent → child only. New down-links [10.1.3]/[10.1.4] (system → domains, system agents), [19.1.3]/[19.1.4] (domain → strategies), [21.1.3]/[21.1.4] (strategy → agents); agent `.claude` [24] holds own files only; upward links [25.1]–[25.3], [26.1]–[26.3] retired. Proposed: runs start at `agents/system/` with an allowlist for the target branch. Open question added in [10]: same rule for `system.link/` folders? `init.sh` [40], `check-links` [14.1] and [2.7] updated.
- **v1.4** – owner decision D-020: agents' `system.link/` folders replaced by individual file links (`[name].link.[ext]`) to only the files each agent needs, from any folder; the list lives in the new `links` section [27.3] (proposed), is set by create-agent, updated by the SI sub-agent, rebuilt by `init.sh` [40] and checked by `check-links` [14.1]; link changes are logged in [46] `changes.md` (new variant, proposed). [27.1], [30.1], [34.1], [35.1], [46.1] redefined as file-link sets; example agent shows concrete links. The D-019 follow-up question is resolved. The system views and `.claude` down-links are unchanged.
- **v1.5** – owner decision D-021: domain → strategy `.claude` links [19.1.3]/[19.1.4] removed (stubs). The "runs start at `agents/system/`" proposal is withdrawn; proposed instead: each level runs in its own folder, a trading agent runs in its own folder ([14.1] `run-agent`, [24]), and higher-level sub-agents deliver outputs as data files linked per D-020. Open questions added in [10.1]: keep [10.1.3]/[10.1.4] and [21.1.3]/[21.1.4]? File links for shared skills in agent `.claude`?
- **v1.6** – owner decision D-022: three levels of agents (system [10], domain [19], strategy [21]) plus variants [23], all with the identical standard folder, now defined in [2.7.1]. Added level files [10.3]–[10.7], [19.2]–[19.11], [21.2]–[21.11]. Domain `CLAUDE.md` [19.7] is the domain owner, so [19.1.1.1] is retired. SI memory moved to the level's own `data/` ([19.5], [21.5]). System views stay folder links (not copies) and now cover all levels.
- **v1.7** – owner request D-023: secrets store [47] `.secrets/` at repo root (git-ignored; `test/`, `live/`, metadata index [47.3]) and [48] `.gitignore`. `load-secret` and a secrets rule added to `check-links` [14.1]. Safety outline [2.8], conventions [2.7] (`secret_ref` scheme) and a new runbook [2.11.6] `add-account-or-secret.md` updated. All proposed.
- **v1.8** – owner decision D-024: full standard `.claude/` at every level ([2.7.2]; [10.1.5]–[10.1.13], [19.1.5]–[19.1.13], [21.1.5]–[21.1.13], [24.5]–[24.13]) with generic placeholders. `CLAUDE.md` moved inside `.claude/` ([10.3], [19.7], [21.7], [37] → [x.5]; [37] stub). SI memory proposed in `.claude/agent-memory/` (updates D-022). `.gitignore` [48] extended. Template [2.7.1] updated.
- **v1.9** – owner request D-025: `tests/` and `research/` in the standard agent folder at every level ([2.7.3]; [10.8]/[10.9], [19.12]/[19.13], [21.12]/[21.13], [49]/[50]), shared `run-tests` [14.1] linked as [30.2], results in [34.2]. Schemas in [2.14], how-tos [2.11.7]/[2.11.8], create-agent and promote-to-live updated. Research moved out of `data/`.
- **v1.10** – fix: [46] cross-variant history points to [21.5] (was stale [16.3]).
- **v1.12** – owner edits from the explorer: D-026 [10.2] support-agent folders retired, support roles are sub-agents ([10.1.1.2] `sys-docs-agent.md` added; [10.1.3]/[10.1.4] only link domains). D-027 test secrets in one `.secrets/test/.env` ([47.1.1], [47.2.1] now `.env`), agent read/update access to test only, loader via `secret_keys` + `load-secret`, UI editing in [45]. D-028 `.gitignore` [48] shows the real commented file.
- **v1.13** – owner request D-029: every agent has a jobs file `configs/[name].workers.json` (format in [11.10]): scripts or AI runs (agent, sub-agent, skill, workflow, command) with on/off, schedule (every, cron, once on a date, after a job, manual), where it runs (local, cloud, desktop, GitHub Actions), platform (Claude Code, Cursor, Codex), model and AI-run parameters. [11.10] `workers.config.json` → `system.workers.json`; new [11.12] `configs/workers/[domain]/` links every workers file by domain; new [19.2.1], [21.2.1], [27.4]; [28] moved to [27.4]; [14.1] `trigger-watcher` → `scheduler` + `run-job`; state in [16.1] `scheduler-state.json`; [11.1] `schedules`, [11.11] rule, [2.11.1], [2.11.2], [2.14], [2.18.2], [40], [41] updated.
- **v1.14** – owner decision D-030: one template for every level's content folders ([2.7.4]): own files + `subagents.link/[child-name]/` → the child's folder of the same kind. System: [2.20], [11.2], [14.4], [15.5], [16.4] renamed from `agents/` views to `subagents.link/` (one link per domain), new [10.8.3], [10.9.3]. Domain: new [19.2.2], [19.3.1], [19.4.1], [19.5.1], [19.6.1], [19.12.3], [19.13.3]. Strategy: new [21.2.2], [21.3.1], [21.4.1], [21.5.1], [21.6.1], [21.12.3], [21.13.3]. No `.claude` links for now: [10.1.3], [10.1.4], [21.1.3], [21.1.4] retired. Jobs view [11.12] merged into [11.2]; the scheduler scans `agents/**/configs/*.workers.json`. `.link` rule amended (links inside a `.link` folder); [2.7], [2.7.1], [2.7.2], [2.11.1], [2.11.5], [2.18.2], [10], [10.1], [14.1] `check-links`, [40] updated.
- **v1.15** – owner request D-031: every agent has a links file `configs/[name].links.json` (format in the new [11.13] `system.links.json`; new [19.2.3], [21.2.3]; [27.3] turned from the `links` section of [27.2] into the variant's own file): which file, from where (system, own domain or strategy, another domain, any agent by unique name), where it appears, why, required. New shared `relink` script [14.1] builds every link from these files plus the child links, removes stale ones, runs the `check-links` rules and writes the links index [16.1]; it runs on a links-file change (scheduler watch), at review time (git pre-commit, post-merge, post-checkout; owner approval in the UI), when an agent edits its own links file (it reruns relink; `PostToolUse` hook in `settings.json`) and from create-agent/init.sh. New relink links [19.3.2], [21.3.2], [30.3]; new runbook [2.11.9]. Updated [2.6], [2.7], [2.7.1], [2.7.2], [2.7.4], [2.7.5], [2.11.1], [2.11.2], [2.11.5], [2.14], [2.17], [10], [11], [11.10], [15], [16], [27], [30], [40]; `init.sh` now only calls relink. Fixed a stale [11.12] reference in [2.11.1].
- **v1.16** – owner input D-032 (saved draft on [23]): variant names start with their strategy, `[strategy-id].[own-name]-v[N].[platform-model]-[test|live]`; the example agent [23] renamed to `pm-strategy-1.momentum-v1.opus55-test` everywhere; the strategy agent's ID carries its platform/model and mode (`pm-strategy-1-agent.opus55-test`, folder name unchanged); the strategy self-improvement loop in [21], [23], [2.7]. Owner request D-033: the knowledge base. This file moved to `vision/docs/file-tree.md` with the other docs; [2] describes the layers; [2.1] the tag format and flow; [2.6] points to `docs/decisions.md` (the seed list moved there); [2.10] inputs with `index.json` [2.10.2] and `README.md` [2.10.3]; runbooks [2.11.6]–[2.11.8] added to the tree and [2.11.10] `process-an-input.md` new; [2.18.7] `links.md`, [2.18.8] `knowledge-map.json`, [2.18.9] `summaries.json`; new [2.21] `architecture.md`; [10.1.1.2] is now `sys-knowledge-agent.md` with skills [10.1.2.1] `knowledge-intake` and [10.1.2.2] `knowledge-summarise`; `build-map` in [14.1]; job `knowledge-sync` in [11.10] replaces `docs-refresh`; "docs agent" renamed to "knowledge agent" throughout. Page edits folded: [48] `.gitignore` (runtime logs/data and local Cursor state ignored), new sections [47.1.1], [47.2.1], [47.3] (index kept in sync automatically), [1] README draft.
- **v1.11** – owner request: every `tests/agents/` and `tests/scripts/` folder gets its own runner link `run-tests.system.link.js` → [14.1] ([10.8.1.3]/[10.8.2.3], [19.12.1.3]/[19.12.2.3], [21.12.1.3]/[21.12.2.3], [49.1.3]/[49.2.3]); called from a test folder it presets the kind and that folder's `tests.config.json`. [30.2] stays for running both kinds. Described how agent tests run (headless Claude Code on fixtures in a temp copy, test mode, no secrets). Updated [2.7.3], [2.11.7], [14.1], [49].
- **v1.34** – owner, 2026-10-09 12:30 (D-061): the repository's `researches/` moved to `agents/trading/researches/` [56.2] with [54.1], [54.2] and [54.3]; the page lists the real files found there.
- **v1.33** – owner, 2026-10-09 09:40 (D-059): new [56] `agents/trading/` with [56.1] `docs/` and its three docs [56.1.1] to [56.1.3]; the prediction-market domain [19] moves to `agents/trading/prediction-market/` with its numbers and file names; [4] says its children are the system and the kinds of domains.
- **v1.32** – owner, 2026-10-07 09:04 (D-056, D-058): trading moves down into the prediction-market domain [19]: new [19.2.4] domain config, [19.3.5] Polymarket price collector, [19.4.2] job logs, [19.4.3] order logs, [19.5.3] its data, the `trading-` notes [19.6.5] to [19.6.15] with [19.6.16] `common/`, [19.6.17] `how-to/`, [19.6.18] `index/`; [14.3] `scripts/decisions/` and [54.3] the trading study move into the domain with their numbers; [42] copy-trading retired with the `whale-signals` and `top-traders` links; the system's sections ([1], [4], [10], [11], [11.1], [11.10], [11.11], [11.13], [14], [15], [16], [2.7], [2.8], [2.14], [2.16], [2.17], [2.18], [47]) say only what holds for any agent; the trading agent links its domain's config, scripts, data and `trading-safety.md`; the research index's `related.variants` is now `related.agents`.
- **v1.31** – owner, 2026-10-07 09:04 (D-056, D-057): the system is the Agent OS, root [0] `agent-os/`; every How it works file is named without the file's extension and every file and folder has an empty Details file (`.meta.json`), shown on the page with the `☑ metadata` switch; one tree line per file: the trading agent's docs [46.2] split into `README.md` [46.2], `strategy.md` [46.5], `changes.md` [46.6], `decisions.md` [46.7], `notes.md` [46.8], and its logs line into `runs.jsonl` and `run-[date].md`.
- **v1.30** – owner, 2026-10-07 08:52 (D-053): every domain, strategy and trading agent lists its own rebuild prompt (new [19.6.4], [21.6.4], [46.4]); the trading agent also its own vision (new [46.3]); [2.22] says every level has one.
- **v1.29** – owner, 2026-10-06 22:06 (D-055): every app has its own docs; [43] rules for research clones and forked apps; new [53.4] to [53.4.3] (the IDE's own docs), new [55] `apps/temp/`; [48] ignores research clones; [2.18.5] lists every app.
- **v1.28** – owner, 2026-10-06 21:43 (D-051 to D-054): new [10.1.2.8] `change-plan/SKILL.md`; [53.2.5] holds one plan per change request. Features (D-052), the docs hierarchy (D-053) and the general system (D-054) are planned in `2026-10-06-2143-general-system.md` and wait for the owner.
- **v1.27** – owner, 2026-10-06 21:04 (D-050): one job per code file, written into [14], [30] and [10.1.2.5]; a Tests file for every code file, skill, agent and subagent joins the file-set plan.
- **v1.26** – owner, 2026-10-06 20:47 (D-049): the IDE and the docs give the owner and every AI the whole context. [53] gets its purpose; [10.1.1.2], [10.1.2.1] and [10.1.5] get the rules (context before a change, the levels above included; everything related in line after it; a session's findings filed; every question answered in the docs).
- **v1.25** – owner, 2026-10-06 12:53 and 12:59 (D-048): the three main docs get sharp jobs: [2.2] the vision is the top-level doc (concept, how it should work, business logic, examples), [2.1] the README describes every part exactly with the path to each part's docs and no logic inside agents, and new [2.22] `rebuild-prompt.md` is the prompt an AI rebuilds the same system from, with its skill [10.1.2.7]. The skills [10.1.2.3] and [10.1.2.4] are rewritten. Domain and strategy `docs/` list their own README and vision ([19.6.2], [19.6.3], [21.6.2], [21.6.3]).
- **v1.24** – owner, 2026-10-06 11:44 (D-047): the system's `.claude/docs/` [10.1.14] is retired; [2.1] README and [2.2] vision moved one level up into the system's `docs/` [2]. An agent keeps no docs inside `.claude/`; the domain, strategy and agent `docs/` folders stay.
- **v1.23** – owner question, 2026-10-06 11:29: a first click on a closed folder opens it [53.1.1].
- **v1.22** – the owner's deletions on the page, 2026-10-06 (D-045): [52] root `CLAUDE.md` retired, its role in the system's [10.1.5] `.claude/CLAUDE.md`; [51] the `[name].index.md` pattern and the system's `[subagent-name].md` pattern leave the tree (only real files); [54] `researches/` retired, its studies [54.1]–[54.3] moved into the agents' research folders [19.13] and [10.9]; [44] the cloned-repo example retired; [45] `trading-ui/` moved into [43] `apps/`, empty for now. The page gets an Apply changes button [53.1.1] (D-046).
- **v1.21** – owner request D-044 (2026-10-05, in-20261005-1545): a Delete button with an optional note for Claude, and one "changed" status on the page [53.1.1]; [53.3.2] write-through writes only what a save changed; [53.3.3] deletes from the page and reports files changed also after a commit; [10.1.2.6] deleting an item and the changed mark.
- **v1.20** – owner request in-20261005-1517 (D-043): [53] `project-IDE/` moved into [43] `apps/` (numbers kept; [43] now holds our own apps too); the server's Claude Code sessions start in `agents/system/` [53.3], [53.3.3]; the server code drafted ([53.3.1]–[53.3.4]).
- **v1.19** – owner wish in-20261005-1452 (D-042): new proposed [53.3] `project-IDE/server/` with [53.3.1]–[53.3.4]: the page on the owner's server with Claude Code behind its request box; [53], [53.2.5], [53.1.1], [10.1.1.3] updated.
- **v1.18.3** – owner question in-20261005-1433: [53.1.1] says what works when the page is opened outside claude.ai; a scheduled sync check is proposed.
- **v1.18.2** – owner question in-20261005-1421: the page's own two files show their real content on the File tab [53.1.1], [53.1.2].
- **v1.18.1** – owner question in-20261005-1403: the page tree shows every item's `.index.md` [51] as its own row [53.1.1].
- **v1.18** – owner request D-041 (2026-10-05, in-20261005-1041, -1043, -1254): the repository is this tree. New at the root: [52] `CLAUDE.md`, [53] `project-IDE/` with [53.1] `current-ui/` (the page and its data) and [53.2] `data/` (README [53.2.1], sources [53.2.2], overrides [53.2.3], memory [53.2.4], plans [53.2.5], archive [53.2.6]), [54] `researches/` with its three folders. Moved, numbers kept: [2.6], [2.9], [2.10], [2.13], [2.18.8] into [53.2]; [2.1], [2.2] into the new [10.1.14] `.claude/docs/`. New in the system `.claude/`: [10.1.1.3] `project-ide-agent.md`, skills [10.1.2.5] `ide-build/` (with [10.1.2.5.1] `SKILL.md` and the scripts [10.1.2.5.2]) and [10.1.2.6] `ide-sync/SKILL.md`; `build-map` left [14.1]. The 19 items marked proposed are agreed (owner: "all should be already all confirmed"); open questions inside sections stay open. [0], [1], [2], [2.1], [2.2], [10.1], [10.1.1.2], [45], [51] updated; [1]'s draft points at the new paths.
- **v1.17** – owner request D-039 (2026-10-05): the How it works of every file and folder moves from `summaries.json` into one Markdown file each, the new pattern node [51] `[name].index.md` (file: `x.index.md` next to it; folder: `f/f.index.md`); [2.18.9] `summaries.json` retired; [10.1.2.2] renamed `file-index/SKILL.md` (was `knowledge-summarise`); [2] and [10.1.1.2] updated.
