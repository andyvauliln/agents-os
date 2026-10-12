# Inputs vision

This document gives the owner's requirements for the Agent OS. It contains the logic from all owner inputs up to 2026-10-09. A newer input replaces an older input on the same subject. This document does not repeat a rule. It does not contain logic that a newer input cancelled. It does not contain proposals from Claude.

The language follows ASD-STE100 (Simplified Technical English):

- A sentence has one statement or one instruction.
- An instruction has a maximum of 20 words. A description has a maximum of 25 words.
- A rule uses "must", "can" or "do not".
- An instruction starts with a verb.
- One word has one meaning in this document. Section 1.3 gives the terms.

Each rule has an identifier, for example SYS-01. Use the identifier when you refer to a rule.

---

## 1. General

### 1.1 Purpose of the system

The Agent OS is a personal system that operates many AI agents. The agents can be of different kinds, for example trading, social media or management. The agents have a shared base. Each kind of agent adds its own parts.

The system must operate as a wheel. It analyses itself and improves itself all the time.

The owner gives an input to make a new agent. The system makes the agent and connects it into the system. Then the owner monitors the agent on the user interface.

| ID | Rule |
|---|---|
| SYS-01 | The name of the system is "Agent OS". The root folder is `agent-os/`. |
| SYS-02 | The top level of the system must not contain logic about trading or other kinds of agents. |
| SYS-03 | Each agent must have a parent. Only the system agent has no parent. |
| SYS-04 | Each kind of agent can have its own levels below the domain. |
| SYS-05 | The system must know how to make a new agent and connect it into the system. |
| SYS-06 | The system must collect data, give each agent only its data, let agents decide and act, and improve the agents. |
| SYS-07 | The system must make it cheap to operate many variants side by side and compare them. |

### 1.2 Types of agents

There are three types of agents:

1. System support agents. They do development, documentation, improvement, analysis and research.
2. Sub-agents. They take data from workers and do a first analysis for the main agents.
3. Main agents. They operate a strategy and make decisions, in test mode or live mode.

### 1.3 Terms

| Term | Meaning |
|---|---|
| Agent | A harness, a platform and a model that operate one main task. An agent runs one time per interval. |
| Level | One layer of agents: the system, a domain, a strategy, or a running agent. |
| Domain | A group of agents for one field of work, for example prediction markets. |
| Strategy agent | The agent that owns one strategy and its variants. |
| Variant | A modification of a strategy, with its own configuration. |
| Worker | A script or an AI task that runs on a schedule and makes data. |
| Job | One scheduled task in a jobs file. |
| Link | A symbolic link to a file or folder. |
| Metadata file | A file that describes another file or folder. |
| Input | A message, comment or edit from the owner. |
| Page | The File Tree page, the main user interface of the project IDE. |

---

## 2. Repository and top-level layout

The GitHub repository is `trading-oss`. The repository contains the file tree of the system.

| ID | Rule |
|---|---|
| REPO-01 | Use only the repository `andyvauliln/trading-oss` for this project. |
| REPO-02 | The repository must show the real file tree. The page must show the same tree. |
| REPO-03 | The root contains `README.md`, `agents/`, `apps/`, `.gitignore` and `.secrets/`. |
| REPO-04 | Do not put a `CLAUDE.md` file at the root. `CLAUDE.md` is in the `.claude/` folder of an agent. |
| REPO-05 | Do not put a `researches/` folder at the root. Research folders are inside the agents. |
| REPO-06 | The trading studies are in `agents/trading/researches/`. |
| REPO-07 | The folder `agents/` contains only domains. The system is one of the domains. |
| REPO-08 | The folder `apps/` contains our applications and repositories that we use from GitHub. |
| REPO-09 | The project IDE is in `apps/project-IDE/`. |
| REPO-10 | The trading dashboard is in `apps/trading-ui/`. |
| REPO-11 | The tree must show only real files. Do not show examples of names or templates in the tree. |

---

## 3. Agent levels and hierarchy

The agents have levels. The parent is above the child. The order is: system, domains, strategy agents, running agents.

The system agent manages all domains and the development of the system. A domain agent is responsible for its domain. A strategy agent is responsible for one strategy.

| ID | Rule |
|---|---|
| LVL-01 | The system is a domain. It has the same folders as the other domains. |
| LVL-02 | All levels must have the same file structure. |
| LVL-03 | The system must contain all data from all agents, in one subfolder for each agent. |
| LVL-04 | The `CLAUDE.md` file of a domain is the domain owner. Do not make a separate folder for the domain owner. |
| LVL-05 | Each `.claude/` level has a self-improvement sub-agent for that level. |
| LVL-06 | Trading domains are in `agents/trading/`. The prediction market domain is `agents/trading/prediction-market/`. |
| LVL-07 | The next trading domain is `agents/trading/copytrading/`. Make it from the prediction market domain when the owner asks. |
| LVL-08 | All trading logic goes down into the trading domains. |

### 3.1 Names

| ID | Rule |
|---|---|
| NAME-01 | Each agent must have a unique name. |
| NAME-02 | The name of a variant must start with the name of its strategy. |
| NAME-03 | The name of a variant must show its own name, its main platform or model, and its mode (test or live). |
| NAME-04 | The name of a strategy agent must show its mode and its main platform or model. |

---

## 4. Common file rules

### 4.1 The standard agent folder

Each agent at each level has the same folder. The folder contains:

- `.claude/`
- `configs/`, `scripts/`, `logs/`, `data/`, `docs/`, `tests/`, `research/`
- `package.json` (JavaScript dependencies and scripts)
- `requirements.txt` (Python dependencies)
- `init.sh` (one-time setup)
- `start.sh` (starts one run or the scheduler)

| ID | Rule |
|---|---|
| FILE-01 | Each agent must have the standard agent folder. |
| FILE-02 | Each content folder contains the files of its own level. |
| FILE-03 | Each content folder contains `subagents.link/[child-name]/` for each direct child agent. |
| FILE-04 | A link in `subagents.link/` points to the folder of the same kind in the child agent. |
| FILE-05 | Do not keep a `docs/` folder inside `.claude/`. The docs of an agent are in its own `docs/` folder. |

### 4.2 The `.claude/` folder

The `.claude/` folder follows the standard Claude Code layout:

- `CLAUDE.md`
- `settings.json` and `settings.local.json`
- `rules/`, `skills/`, `commands/`, `agents/`, `workflows/`, `output-styles/`
- `agent-memory/` and `agent-memory-local/`

| ID | Rule |
|---|---|
| CLD-01 | Each domain level and each strategy level must have a `.claude/` folder. |
| CLD-02 | Keep `CLAUDE.md` inside `.claude/`. |
| CLD-03 | Do not put specific logic in the template, for example a `security-review/` skill. Add it later. |
| CLD-04 | Sub-agents are Claude Code sub-agents in `.claude/agents/`. Do not make a separate `subagents/` folder. |
| CLD-05 | Do not link `.claude/` folders between levels. |

### 4.3 Links

| ID | Rule |
|---|---|
| LNK-01 | Each link must have `.link` in its name. |
| LNK-02 | Links go from a parent to its children only. A child must not link to its parent. |
| LNK-03 | An agent links individual files. Do not link full folders into an agent. |
| LNK-04 | An agent links only the files that its logic needs. |
| LNK-05 | Select the links when you make the agent. Change them after self-improvement. |
| LNK-06 | The domain does not link to the agents and skills of its strategies. |
| LNK-07 | Each level must have a links config. It tells what to link and from where. |
| LNK-08 | An agent can link data from another agent, from its domain or from another domain. |
| LNK-09 | A script must make the links again when a links config changes. |
| LNK-10 | Run the link script at review time if files changed. An agent runs it after it edits its links config. |

### 4.4 Code files

| ID | Rule |
|---|---|
| CODE-01 | A code file must contain one runnable item: one function, one endpoint or one script. |
| CODE-02 | A code file has one purpose. It can accept different parameters. |
| CODE-03 | Do not make shared files that contain different items. Put related items in a folder, one item in each file. |
| CODE-04 | Write scripts in JavaScript, TypeScript or Python. |
| CODE-05 | Each data file type must have scripts for create, read, update, delete and filter. |

### 4.5 Metadata files

Each file and each folder has metadata files. Each tab on the page shows one metadata file.

| ID | Rule |
|---|---|
| META-01 | Each file and each folder must have metadata files. |
| META-02 | The name of a metadata file is the item name without its extension. Example: `vision.md` has `vision.index.md`. |
| META-03 | "How it works" is in `{name}.index.md`. |
| META-04 | The details of an item are in `{name}.meta.json`. |
| META-05 | The example of an item is in `{name}.example.md`. |
| META-06 | The questions about an item are in `{name}.questions.md`. |
| META-07 | A custom view is in `{name}.{type}.{optional-name}.view.html`. |
| META-08 | A code file, a skill, an agent and a sub-agent must have a tests metadata file. |
| META-09 | The change log of an item must be a JSON file. It records the input, the description and the changed logic. |
| META-10 | A metadata file does not have its own metadata files. |
| META-11 | The metadata of a file must show where the file is used, who updates it and when. |

---

## 5. Configuration

| ID | Rule |
|---|---|
| CFG-01 | There are two types of config: one global system config and one config for each agent. |
| CFG-02 | The global config is one file with sections. Split a section into its own file when it becomes long. |
| CFG-03 | The routing of models and platforms is config. It is a separate file. |
| CFG-04 | The routing tells which model or platform each agent, sub-agent and worker uses. |
| CFG-05 | Each agent must have a jobs file `configs/[name].workers.json`. |
| CFG-06 | The system config must show the jobs of each domain through links. |
| CFG-07 | Each level must have a tests config. |
| CFG-08 | All services that do an action must get test mode or live mode from config. |

### 5.1 Jobs

A job is a script, an agent, a sub-agent, a skill or a workflow. A job runs on a schedule or one time on a date.

| ID | Rule |
|---|---|
| JOB-01 | The owner must be able to see, change and stop each job in the jobs file. |
| JOB-02 | A job must have a schedule, or one date for one run. |
| JOB-03 | A job must tell where it runs, for example in the cloud or headless. |
| JOB-04 | A job must tell its platform and model. |
| JOB-05 | An AI job must have its parameters, for example a prompt, a workspace and a skill. |
| JOB-06 | All system jobs are off for now. |

---

## 6. Scripts, workers, data and logs

| ID | Rule |
|---|---|
| SCR-01 | Workers are scripts. Keep all scripts in `scripts/`. |
| SCR-02 | Describe each worker in config: what it is for, its schedule and how it runs. |
| SCR-03 | Scripts can be workers, decision scripts (for example buy and sell) or system scripts. |
| SCR-04 | Scripts can be shared by the system or belong to one agent. |
| DAT-01 | Keep data in JSON and Markdown files for now. Do not use a database. |
| DAT-02 | Keep data by source: by worker, by agent, by sub-agent and by system. |
| DAT-03 | Keep logs by source: by service, by worker, by sub-agent and by agent. |
| DAT-04 | Do not put logs and data in git. |

---

## 7. Secrets

| ID | Rule |
|---|---|
| SEC-01 | Keep private keys in the `.secrets/` folder at the root. |
| SEC-02 | Do not put `.secrets/` in git. |
| SEC-03 | Keep test keys in `.secrets/test/.env`. Keep live keys in `.secrets/live/.env`. |
| SEC-04 | `live/.env` must have the same structure as `test/.env`. |
| SEC-05 | The Variables view must show the current content of the file. Do not show example values. |
| SEC-06 | The Variables view must let the owner add and edit variables. |
| SEC-07 | The Variables view must show where each variable is used and what it is for. |
| SEC-08 | Update the secrets index each time a file uses a new variable. Do this automatically. |
| SEC-09 | Do not put a key value in docs, inputs, the page or git. |

The `.gitignore` file must contain:

- `.secrets/`
- logs and data
- local Claude Code settings
- local Cursor files (keep all other `.cursor` files, as for `.claude`)

---

## 8. Agent runs

An agent runs one time in an interval. It gets the information that it needs from workers or sub-agents. Then it makes a decision.

The run loop is: read data, analyse, decide, act.

Possible decisions are:

- buy, sell, sell all
- wait for information, set a reminder, schedule the next run
- collect more data, do research with a new sub-agent
- make, subscribe to, unsubscribe from, configure or schedule workers

| ID | Rule |
|---|---|
| RUN-01 | An agent runs on an interval. |
| RUN-02 | An agent runs when an important file changes. |
| RUN-03 | When an important file changes, stop the current run. Start a new run with the new information. |
| RUN-04 | An unimportant change waits for the next run. |
| RUN-05 | An agent can set its own trigger, for example when its research is complete. |
| RUN-06 | A triggered run gets all subscribed data and the result of the trigger. |
| RUN-07 | On each run, an agent reads all new data since its last run. |
| RUN-08 | At the end of a run, the agent compresses the important information. It removes the information that it does not need. |
| RUN-09 | The agent decides to keep its session or to start a new session. |
| RUN-10 | The agent can subscribe to more data, start research or request a worker. |
| RUN-11 | The system must have a maximum number of parallel runs. The limit comes from the server capacity. |
| RUN-12 | A system agent can check the server and set the limit. |

### 8.1 Agents that use other agents

| ID | Rule |
|---|---|
| A2A-01 | An agent can subscribe to the data of another agent. |
| A2A-02 | Urgent data can stop the current run of an agent. Example: a risk agent tells all agents to sell. |
| A2A-03 | A news agent or worker can make data that other agents use. |
| A2A-04 | To get a new worker, an agent asks the worker agent. |
| A2A-05 | The worker agent knows all workers. It extends a worker or makes a new worker. |
| A2A-06 | The worker agent tells the agent where the data is and how to use it. |
| A2A-07 | Do not make duplicate workers. |

---

## 9. Self-improvement

| ID | Rule |
|---|---|
| SI-01 | Each agent must have a self-improvement strategy. |
| SI-02 | You can change and test the self-improvement strategy itself. |
| SI-03 | The self-improvement sub-agent has memory and lives for a long time. |
| SI-04 | It reads the agent logs, data, research, outside information and the owner comments. |
| SI-05 | It makes the strategy fast, cheap, efficient, simple, clear and profitable. It fixes bugs and tests. |
| SI-06 | It uses our templates for self-improvement. It adapts them to the strategy. |
| SI-07 | The strategy agent makes modifications of itself as new test variants. |
| SI-08 | The strategy agent analyses the variants. It changes itself if a variant is better. |
| SI-09 | When a new model or harness is available, update the related logic. Then test new configurations. |
| SI-10 | Self-improvement can change all things that it needs to change. |
| SI-11 | The owner must approve each new strategy configuration before it runs. The owner reads a report first. |
| SI-12 | Agents can make workers and helpers without limits for now. |

---

## 10. Test mode, live mode and back-testing

| ID | Rule |
|---|---|
| MODE-01 | Each agent must have a test mode. |
| MODE-02 | Each action (for example buy and sell) must support test mode and live mode. |
| MODE-03 | Get the mode from config. |
| MODE-04 | For blockchain actions, test mode can use a test network. Live mode uses the main network. |
| MODE-05 | Each agent can operate with different configurations: capital, risk management, personal settings and domain settings. |
| BT-01 | Each strategy can have its own back-testing method and settings. |
| BT-02 | A back-test can replay old data as live data. Example: one month of old data. |
| BT-03 | AI back-tests can leak results that the model knows. Paper trading is the honest test for AI strategies. |

---

## 11. Tests and research

| ID | Rule |
|---|---|
| TST-01 | Each level must have `tests/agents/` and `tests/scripts/`. |
| TST-02 | Each test folder must have a config of all its tests. |
| TST-03 | In the tests config, the owner can enable and disable each test. |
| TST-04 | The tests config shows the last run, the result and the next action for each test. |
| TST-05 | Each test folder must have a script that runs the tests from the config. |
| TST-06 | The page must have a Tests tab. The owner can run a test from it. |
| RES-01 | Each level must have a `research/` folder. |
| RES-02 | Each research folder must have `index.json`. It keeps the history, the results and the decisions of each research. |

---

## 12. Models and platforms

| ID | Rule |
|---|---|
| MOD-01 | Claude Code is the default platform. |
| MOD-02 | Use the most capable model with high effort for thinking, planning, main agents, analysis and improvement. |
| MOD-03 | Use a medium model with medium effort for tasks that are not important. |
| MOD-04 | Cursor is supported. Use it for light tasks that use many tokens, for example workers and data filters. |
| MOD-05 | OpenRouter is supported but not connected. Use a rotation of free models for tasks that are not important. |
| MOD-06 | Codex and Kimi are supported later. |
| MOD-07 | Each object that uses AI must have a configured route to a platform and model. |
| MOD-08 | Later, workers can run on Cursor or Codex. |

---

## 13. Trading domains

| ID | Rule |
|---|---|
| TRD-01 | The first domain is prediction markets on Polymarket. Copy trading is next. |
| TRD-02 | The owner gives the first strategy. Then the wheel starts. Add more strategies after the flow works well. |
| TRD-03 | For now, operate the system agent, the domain agent, the strategy agent and two or three configurations. |
| TRD-04 | Real money starts only after an agent shows good results. |
| TRD-05 | Each strategy selects its own markets and accounts. Decide this when the first strategy is in development. |
| TRD-06 | For now, do trade actions only on blockchains. Support all networks and apps there. |
| TRD-07 | For centralised exchanges and other apps, collect information only. Do not do actions. |
| TRD-08 | Workers and data of the existing Polymarket tools can be used in other strategies. |
| TRD-09 | Strategies can be code, AI or both. Market making and arbitrage need fast event-driven code. |
| TRD-10 | Add protection against instructions in outside text when live trading starts. |
| TRD-11 | `agents/trading/docs/` contains the vision, the README and the rebuild prompt of trading. |

Domain examples from the first brief: prediction markets, crypto trading, copy trading, trading on content from one person (for example one YouTube author), and combinations of strategies.

---

## 14. Documentation and knowledge

### 14.1 Documents

| ID | Rule |
|---|---|
| DOC-01 | Write docs for people. A person who is not technical must understand them. |
| DOC-02 | Write docs as a good book. Give only the important facts for each level. |
| DOC-03 | Do not put reference numbers (for example [2.1]) or identifiers in docs for people. |
| DOC-04 | Do not write history in docs for people, for example "the owner later said". Write the facts as they are now. |
| DOC-05 | Keep relations, decisions and sources in notes for agents only. |
| DOC-06 | Each level (system, domain, strategy, agent) must have the same set of docs, in the same format. |
| DOC-07 | Each level must have a vision, a README and a rebuild prompt. |
| DOC-08 | The vision is the top document. It gives the ideas, the concept, the business logic and examples. |
| DOC-09 | The README gives a full and exact description of all main parts. It gives the path to the docs of each part. |
| DOC-10 | The README of the system must not contain the logic inside the agents. |
| DOC-11 | The rebuild prompt lets an AI build the same working system again. |
| DOC-12 | The three documents are a hierarchy. The vision comes first, then the README, then the rebuild prompt. |
| DOC-13 | When a lower level changes, update the documents of all levels above it. |
| DOC-14 | Each document must have its own skill that tells how to write it. |
| DOC-15 | The docs must include a feature map. It tells which logic belongs to which files. |
| DOC-16 | Large features must have their own files. A small feature belongs to a large feature. |
| DOC-17 | A feature file maps to its files. Each file maps back to its features. |
| DOC-18 | The docs must include `file-tree.md`, data schemas, flows, metrics, shared knowledge and index lists. |
| DOC-19 | The overview must have an "Always keep in mind" section. |

### 14.2 How it works

The "How it works" text explains an item to a person who sees the project for the first time.

| ID | Rule |
|---|---|
| HOW-01 | "How it works" must tell which skill is responsible for the item. |
| HOW-02 | It must tell how and when the item changes, and when AI uses or updates it. |
| HOW-03 | It must tell where other files mention the item. It must tell the related knowledge. |
| HOW-04 | For a folder, it gives a summary of all files in the folder. |
| HOW-05 | Store "How it works" in a file. Do not make it again each time the page opens. |

### 14.3 Inputs and knowledge flow

| ID | Rule |
|---|---|
| KNW-01 | Store each owner input word for word. Put it in a category. |
| KNW-02 | A question from the owner and the answer from AI are one input. Store both. |
| KNW-03 | A knowledge agent extracts the knowledge from each input. It puts the knowledge in the correct files. |
| KNW-04 | Each change to the system goes through the same flow as an input. |
| KNW-05 | The knowledge agent must have a map of all files and their knowledge. The map is many to many. |
| KNW-06 | The knowledge is a hierarchy. A higher level summarises the levels below it. |
| KNW-07 | The knowledge agent can make a new file when no file fits the knowledge. |
| KNW-08 | Do not keep separate lists of decisions, concepts and rules on the page. |
| KNW-09 | Each owner question must find its place in the docs, with an explanation. |
| KNW-10 | When a file changes, update all related files, agents, skills, docs, indexes and logic. |
| KNW-11 | An AI that works on a low item must know the knowledge from the levels above. |
| KNW-12 | Spread new knowledge from each session and each input to the correct files. |
| KNW-13 | The docs must be correct for people and for AI. |

### 14.4 Plans

| ID | Rule |
|---|---|
| PLN-01 | Write a plan before you do a change request. Store the plan. |
| PLN-02 | After the change, move the logic from the plan to the correct files. |
| PLN-03 | If the work continues, update the logic and knowledge in the related files. |
| PLN-04 | Planning is a skill. It is the main skill of the development. |

---

## 15. Project IDE and the File Tree page

The project IDE lets the owner manage, analyse and monitor the system. It gives AI all the context that it needs to make exact changes. The File Tree page is the main document of the system.

### 15.1 The tree

| ID | Rule |
|---|---|
| UI-01 | The page shows the file tree. The owner can click each folder and each file. |
| UI-02 | The tree must show the real files on disk. |
| UI-03 | The page reads its data from a data file. |
| UI-04 | The tree has two tabs: "All" and "Changed". "Changed" shows only changed items. |
| UI-05 | The search must filter the tree by path. It must also find file extensions, for example `.md`. |
| UI-06 | A "metadata" switch shows or hides all metadata files. |
| UI-07 | If a folder contains real files, the folder is real. |
| UI-08 | The page shows only one status for now: "changed". Show it after each page request. |

### 15.2 Tabs of a file

| ID | Rule |
|---|---|
| TAB-01 | File: the file as it is now, also if it is empty or not made yet. |
| TAB-02 | The File tab must let the owner edit, comment, add and save. |
| TAB-03 | Example: the structure of the file and the content of each section. |
| TAB-04 | For a config file, the example shows all fields, all values and an explanation. |
| TAB-05 | How it works: a summary that a person who is not a developer understands. |
| TAB-06 | Questions: the open questions about the item. |
| TAB-07 | Custom tabs: different for each type of item. Example: the Variables table for `.env`. |
| TAB-08 | A custom view can contain custom logic, not only a table. Example: one view for all skills. |
| TAB-09 | Markdown files open in a read view. It has a white mode and a black mode. |
| TAB-10 | Long lines in edit mode must wrap to the screen width. |
| TAB-17 | The owner must be able to edit a file in the Read view. |

### 15.3 Tabs of a folder

| ID | Rule |
|---|---|
| TAB-11 | A folder has Contents, How it works, Questions, notes, rules and custom views. |
| TAB-12 | How it works of a folder gives an overview of all its files. |
| TAB-13 | A folder has no Example tab. |
| TAB-14 | A domain agent has an Overview tab. It shows what the agent does, with a status for each item. |
| TAB-15 | The Overview tab must let the owner add a row for a new task. |
| TAB-16 | A domain agent has an Agents tab. It lists sub-agents, workers and skills with their metadata. |

### 15.4 Requests from the page

| ID | Rule |
|---|---|
| REQ-01 | Each file and folder has a box for a request to AI under the tabs. |
| REQ-02 | If the request is a question, AI gives the answer. Add the answer to the item knowledge. |
| REQ-03 | If the request is a change, AI shows a draft. |
| REQ-04 | The draft shows each changed file. In each file it shows each changed field. |
| REQ-05 | Click a field to see only the changes of that field. |
| REQ-06 | When the owner saves, apply the change immediately. |
| REQ-07 | The owner can select a model and an effort. The default is the most capable model at medium effort. |
| REQ-08 | The model list shows only the latest models. |
| REQ-09 | The page has an "Apply changes" button at the top. It applies all changes and shows the new tree. |
| REQ-10 | Each item has a Delete button. The owner can add a note for AI. |
| REQ-11 | A delete runs the agent. The agent cleans the item from the whole project. |
| REQ-12 | A voice button records the owner for a maximum of 5 minutes. The text goes into the box. |
| REQ-13 | Voice uses free Groq models. If a model has a rate limit or an error, use the next model. |
| REQ-14 | The Groq key is in the secrets folder only. |

### 15.5 The owner server

| ID | Rule |
|---|---|
| SRV-01 | The page must work on the owner server with the same files. |
| SRV-02 | On the server, the page can send requests to Claude Code in the repository. |
| SRV-03 | Claude Code on the server starts in the system folder. |
| SRV-04 | The system must be easy to move to a server with more resources. |
| SRV-05 | The owner must be able to continue the work from Claude Code on the server, through GitHub. |
| SRV-06 | Claude in the cloud and Claude on the server must both know the full context. |

### 15.6 Monitoring of agents

The owner wants a full view of each agent on the user interface.

| ID | Rule |
|---|---|
| MON-01 | Show the performance of each agent. |
| MON-02 | Show all components, logs, used data and made data of each agent. |
| MON-03 | Show all decisions and all improvements of each agent. Show what changed in a test. |
| MON-04 | The owner can approve or not approve an agent for a funded account. |
| MON-05 | The owner can stop or delete an agent. |
| MON-06 | The owner can comment, ask questions and tell an agent how to improve. |

---

## 16. Apps

| ID | Rule |
|---|---|
| APP-01 | Each app in `apps/` has its own docs: a vision, a README and a rebuild prompt. |
| APP-02 | Clone a repository for research into a temporary folder first. |
| APP-03 | Fork an app that we use. Make our own main branch. |
| APP-04 | From time to time, merge the updates of the source into the fork. Then merge them into our main branch. |
| APP-05 | Later, a skill changes an app to the system format when the owner asks. Keep this skill up to date. |

---

## 17. Owner approval

| ID | Rule |
|---|---|
| APR-01 | The owner must approve the funding of live accounts. |
| APR-02 | The owner must approve each new strategy configuration before it runs. |
| APR-03 | Claude can merge a pull request when the owner tells Claude to do it. |

---

## 18. Open subjects

The owner has not decided these subjects yet:

1. The metrics of success for an agent.
2. The budget for AI costs.
3. The capital limits for the first live trades.
4. The channel for notifications to the owner.
5. How to keep live keys when real trading starts.
6. How to detect new data since the last run (a pointer or links).
7. A separate part that executes the decisions of agents.
8. One record of the true positions of all agents.
9. Shared summaries of data, made one time for all agents.
