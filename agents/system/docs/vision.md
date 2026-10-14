# The system domain: vision

## In short

The Agent OS is the owner's personal system for running AI agents of any kind: agents that trade, that work on social media or that help with management. It runs many small agents side by side, each with one clear job, tries every idea safely first and keeps what works. The system domain is the top of it. It holds the system agent, which oversees every domain, the health of the whole system and its development, and it holds everything every agent shares: one standard way to lay out an agent, one way to run every job on time, one way to hand each agent exactly the information it needs, one set of safety rules for acting in the outside world, one place for keys, and the helpers that improve the system, keep its knowledge and look after the owner's window on it. Every other domain builds on this base and adds only what is its own. The project is in its first stage: the design is complete and laid out as real files, and nothing of the system runs yet.

## Why we are building it

The Agent OS will run hundreds of agents in several areas of work. Each of them needs the same things: information to work with, a way to run at the right moments, a safe place to try ideas, a way to get better, and a way for the owner to see and steer it. If every area built these for itself, the same work would be done many times over, each copy would drift a little from the others, and a safety rule fixed in one place would stay broken in another. The owner would also face a different set of habits in every area.

So the parts every agent needs are built once, at the top, and every area of work uses them. That top is the system domain.

There is a second reason. The owner builds the whole project by describing what they want in plain words and letting AI write the plans, the docs and later the code. Built this way, a project quickly becomes hard to follow: answers get forgotten, documents disagree, and nobody can say any more what exists and why. The system domain therefore also holds the helpers that keep everything the owner has said, turn it into clear docs, and keep the owner's window on the project true.

The goals:

- one shared base that every kind of agent uses, so a new area of work adds only what is its own;
- the same safety rules for every agent: test first, and only the owner lets anything act for real;
- a system that keeps improving itself with little hand work, and reacts when better AI models and tools appear;
- full visibility: the owner can see every agent, every job and every decision from one place;
- knowledge that is never lost: every input from the owner is kept and placed where it belongs, so the docs always describe the system as it is;
- low running costs, and an easy move to a bigger server when the system grows.

Success means that a new domain can be added by copying the one most like it and changing only what differs; that every agent, in every domain, runs, acts and improves under the same rules; that the owner never has to hunt for what runs, when, and why; and that any AI picking up the work finds everything it needs in the docs. How success is measured in numbers is still open.

## The concept

Everything in the Agent OS is an agent, a helper, a worker or a plain file, and every agent sits in a family tree.

- **An agent** is a small AI-driven program with one job. It reads the information it is given, decides what to do and acts on it. Each agent has a parent above it; only the system agent has none.
- **The system agent** is the root of that tree, the system manager. It oversees every domain, watches the health and costs of the whole system, plans each new domain before it is built, takes care of the system's own development and answers the owner's questions about the whole.
- **A domain** is one area of work, such as trading on prediction markets. Its domain agent owns the area, and the domain arranges its agents in the levels its work needs. The system domain is a domain too, and the first one: it is laid out exactly like every other.
- **Workers** are plain scripts that collect information on a schedule, such as prices and news, and save it as simple files. A worker that agents in several domains use belongs to the system.
- **Helpers** are AI assistants with one task, working inside a level. The system has four kinds:
  - the **self-improvement helper**, which keeps preparing better versions of the system's shared parts and reacts to new AI models and tools;
  - the **knowledge base agent**, which keeps every input from the owner and every change, and writes the docs;
  - the **project IDE agent**, which looks after the owner's window on the project, the File Tree page;
  - the **workers helper**, planned, which knows every worker, so an agent that needs new information gets existing data or an extended worker instead of a duplicate.
- **The shared machinery** is a small set of scripts and settings every agent uses: the script that creates agents, one scheduler that runs every job, the script that hands each agent its files, the loader that hands a script its keys, the test runner, and the global settings with the list of AI models.
- **The owner** gives ideas, approves what runs and what acts for real, and watches and steers everything.

A few ideas make it work.

**What every agent needs lives at the top; what one area needs lives in that area.** Test and live modes, the owner's approval to go live, the safety rules, running jobs on time and handing out information are the same for every kind of agent, so they live in the system domain. Money, orders and trading strategies belong to trading alone, so the system domain knows nothing about them. A new area never has to read past another area's details.

**One standard folder for every agent.** Every agent, from the system agent down to the smallest one, keeps its settings, scripts, records, data, docs, tests and research in the same places. People, tools and agents always know where to look.

**Parents see their children, never the other way round.** The system agent can look into every domain, and each level into the one below it. A lower level never reaches up, so each agent can be understood on its own and a change in one place cannot break agents nobody thought of.

**Shared things are linked, never copied.** An agent that needs a shared file gets a link to the one real file. A fix to that file reaches every agent that uses it.

**Everything an agent runs is in one list.** Each agent has one list of every job it runs: what the job does, when, where and with which AI model. The owner can see, change and switch off any job there.

**Plain files everyone can read.** Settings, records, information and docs are simple files, with no database for now. Nothing important is hidden inside a program.

**Every change is planned, and every input becomes knowledge.** A change to the system starts as a written plan the owner sees first. Every message from the owner is kept word for word and its knowledge is placed in the docs, from the top level down to the single file.

## How it should work

The system domain does its work in a loop that serves every domain at once.

1. **The owner speaks.** The owner leaves a message in the project chat or on the File Tree page: a new idea, a question, an edit or a request. The knowledge base agent keeps it word for word, works out what it changes, and places that knowledge in the docs it belongs to. A question gets its answer written where the owner should have found it.
2. **A change is planned.** When the message asks for a change, a short plan is written and shown to the owner. Only after their go is it built. Once built, what the plan taught moves into the docs, and the plan is archived.
3. **Agents and domains are created the same way.** A new agent or domain is made by one shared script: it checks that the name is new, sets up the standard folder, writes the first settings, gives the agent its links and its list of jobs, all switched off, and starts it in test mode.
4. **One scheduler runs every job.** The scheduler reads every agent's list of jobs and starts each one at its time: workers, agents' own runs, helpers. When a file an agent marks as important changes, its current run stops and a new one starts with the fresh information; other changes wait for the next run. A system helper checks what the server can take and limits how many runs go at once.
5. **Each agent gets exactly what it needs.** Each agent lists the files it uses from elsewhere, and one shared script turns that list into links in the agent's own folder. When an agent needs information nobody collects yet, it asks the workers helper.
6. **Every action passes the same gate.** Every action in the outside world works in a test mode and a live mode. Before a script acts, it checks the mode, the limits and the general stop switch. Keys reach a script only at the moment it runs, and only the keys it is allowed.
7. **Results flow upward through the family tree.** Each agent writes its own records and data in its own folder. The level above reads them through its links to its children, so the system agent can follow anything in any domain, level by level.
8. **The system improves itself.** The system's self-improvement helper reads the system's records, costs, research and the owner's comments, and watches for new AI models and tools. It proposes better versions of the shared parts, which are tried in test mode first.
9. **The window stays true.** After every round, the docs and the File Tree page are brought in line, so the owner and every AI see the system as it is designed now.

```text
  the owner ──► knowledge base agent ──► docs, plans ──► changes to the shared parts
      ▲                                                        │
      │                                                        ▼
  File Tree page ◄── project IDE agent        scheduler ──► workers, agents, helpers
      ▲                                                        │
      │                                                        ▼
      └──── records read level by level ◄──── actions through the test or live gate
                           │
                           ▼
              system self-improvement ──► new test versions
```

## The business logic

These rules hold for every agent in every domain. A domain may add its own rules on top, never against them.

**What belongs to the system.** A file or rule that agents of different domains share lives in the system domain. One that only one domain needs lives in that domain, and one that only one agent needs stays with that agent. The system level never contains logic about trading or about any other kind of work.

**Where new domains come from.** The owner asks for a new area of work, and the system agent plans it. A new domain starts as a copy of the domain most like it, with the same levels, rules and docs, and changes only what is different. Everything the system shares works for it at once.

**Every agent has a parent.** The system agent is the only one without a parent. Every domain is a child of the system, even when it sits inside a folder that groups domains of one kind.

**Test first.** Every action that reaches the outside world, such as posting, buying or selling, works in a test mode and a live mode from the start. Every new agent and every new version starts in test mode, where nothing real happens.

**Only the owner makes anything live.** An agent acts for real only after it has shown good results, and only when the owner approves it, one agent at a time. No agent can approve going live, for itself or for another, and self-improvement never acts live. Agents may use the keys of test accounts; the live keys are for the owner alone and never reach an AI.

**Limits live in code.** A general stop switch that halts every outside action at once, and hard limits that are checked in code before every action, are part of the design as our proposals. A lower level may only make a limit stricter, never looser.

**Improvement makes new versions.** An improvement never changes a running agent; it becomes a new agent in test mode, and starts only after the owner has read a short report and approved it. The better versions are kept. When a new AI model or tool appears, the related logic is updated and new test versions try it.

**Jobs start switched off.** A job runs only when it is switched on. Every job of the system is switched off for now, and stays in the list until the owner turns it on. A job is paused by switching it off, never by deleting it.

**Costs count.** Every AI run costs money, so each kind of work has a fixed model that fits it: the strongest model with high effort for thinking, planning, analysis, improvement and the agents that act; a cheaper one for unimportant work; and a fast, cheap one for light, high-volume work such as collecting and filtering data. How many agents run at once follows what the server can take. The AI budget is still open.

**Knowledge has one home.** Every input from the owner is kept word for word. A fact lives in one place, the levels above sum up the levels below, and when a lower level changes, the docs above it are updated up to the top.

**Decided means the owner decided.** Ideas from the helpers stay proposals until the owner says yes. Anything hard to undo, such as deleting or merging work into the main line, waits for the owner.

## Examples

Three short examples, each followed from start to end.

**Example: a message from the File Tree page becomes knowledge.** The owner opens the system's settings file on the File Tree page and asks why every job is switched off.

1. The question waits on the page until the next sync, or reaches Claude Code at once on the owner's server.
2. The knowledge base agent keeps the question and its answer word for word: every job is off until the owner switches it on, and scheduled AI jobs wait for an AI budget.
3. The answer is written into the How it works of the jobs list, where the owner should have found it.
4. The File Tree page is rebuilt, and the next time anyone opens that file, the answer is there.

**Example: a new domain for social media.** The owner asks for agents that post on social media.

1. The system agent plans the new domain: what its goal is, which levels it needs, where its agents may act and where they only collect information. The owner reads the plan and agrees.
2. The domain is created as a copy of the domain most like it, with the standard folder, its own instructions and its own self-improvement helper.
3. The system's links to its children now reach the new domain, so the system agent and the owner can follow its records like any other.
4. Its first agents start in test mode: their posts are only written down, never published. Only when one has shown good results and the owner approves it does a live version publish for real.

**Example: a new AI model.** A stronger and cheaper AI model is released.

1. The system's self-improvement helper notices it and opens a short piece of research.
2. It proposes a change to the list of AI models and a new test version of an agent that uses the new model, with a short report.
3. The owner approves, and the new version runs in test mode next to the current one.
4. If it does better, it becomes the standard; if not, it is dropped, and the research records why.

## What the owner sees and does

The owner works with the system the way a manager works with a team.

- They describe ideas, questions and changes in plain words, in the project chat or on the File Tree page, by typing or by voice.
- They read a plan before any change to the system is built, and say go or no.
- They read a short report on every new version of an agent and approve it before it starts.
- They decide which jobs run, by switching them on or off in each agent's list of jobs.
- They are the only one who lets an agent act for real, and they can stop or delete any agent at any time.
- They open any file or folder on the File Tree page and read what it is, how it works, who looks after it and what is still open, and they can edit it there.
- They press one button to carry every change they left on the page into the files.

The same window serves the AI doing the work. Before an AI changes a file, it reads what the file is for, how it works, what depends on it and which rules reach it from the levels above, so one change reaches everything that must follow it.

## Where we are and what comes next

The project is in its first stage, and nothing of the system runs yet. The design is complete for the system domain and for trading in general, and the repository already has its final shape: every planned file and folder exists, files with a draft carry their text, the rest are empty, and every file and folder has its How it works and Details notes next to it. The knowledge base agent, the project IDE agent and their skills are written; the File Tree page works on claude.ai and on the owner's own server; every input from the owner so far is kept word for word. The prediction-market domain, the first trading domain, keeps only its folders for now: it is the second stage.

The work of the first stage, in order:

1. Finish the project IDE, the File Tree page and its server.
2. Go through every file and folder, write custom views for each kind of file, and make every file's notes correct.
3. Finish the docs of the project, the system domain, trading in general and the apps, each with a version of its README in Simplified Technical English to compare with the original.

After that, the plan is to build the shared machinery: creating agents, handing out files, running every job on time, loading keys safely and running tests. Then the second stage starts the first domain: one Polymarket strategy chosen by the owner, run in test mode, watched as it acts and improves itself, with more agents once it runs in a good flow.

Later: more trading domains, each copied from the prediction-market domain, such as copy trading; agents of other kinds, such as social media or management; acting live with the owner's approval, together with protection against instructions hidden in outside text; more AI platforms; and a bigger server when the system needs one.

## Principles

**Start simple, improve later.** Use the simplest thing that works today, and upgrade it only when a real problem shows up.

**Test first; the owner approves what acts for real.** Mistakes in test mode cost nothing, and only the owner can let an agent act live.

**The top stays general.** What every agent needs lives at the top; what one area needs lives in that area. So the top never has to change when a new kind of agent arrives.

**One standard folder for every agent.** Tools, people and agents always know where to look, at every level and in every domain.

**Parents see their children, not the other way round.** Every agent stays self-contained, and a change in one place cannot reach where nobody expects it.

**Shared things are linked, never copied.** A fix to the one real file reaches everyone who uses it.

**One file, one job.** Every piece of code does one thing, so it is easy to understand, test and replace.

**Everything is a file the owner can open.** Nothing important is hidden inside a program or a database.

**Everything an agent runs is visible and switchable.** One list per agent shows every job it runs, and each can be turned on or off.

**Keys never travel.** A key reaches only the script that needs it, at the moment it runs, and never a document, a record or an AI.

**Every change starts with a plan, and the docs follow it.** The owner sees each change before it is built; once built, what it taught flows into the docs.

**Every AI works with the whole picture.** The docs are exact enough to act on, and whatever an AI learns is filed where it belongs, so the next one starts knowing it.

## Ideas we are still weighing

These are not decided. Each starts from a problem the system will run into as it grows.

**Agents keep a bookmark instead of having data linked in.**
The problem: an agent is handed its information as links to files when it is created, and on every run it must work out what is new. With hundreds of agents, keeping those links right and replaying the past for tests gets harder and harder.
The idea: an agent subscribes to the data it needs, like following a channel, and keeps a bookmark of how far it has read; each run it asks for everything after it.
What it would change: no data links to keep up, a clear answer to "what is new", and testing on the past as easy as moving the bookmark back. Shared scripts and settings would still be linked.

**Digest shared information once for everyone.**
The problem: many agents may read the same news and prices, and if each one summarises them with AI, the same work is paid for many times over.
The idea: a helper reads the raw information once and writes a short shared digest, such as the day's news that matters to one area, and each agent picks out what concerns it.
What it would change: lower AI costs and faster runs once there are many agents; with only a few it saves little.

## Open questions

These are for the owner to answer.

- **What is the AI budget?** It decides how many agents can run, how often, and when the scheduled AI jobs can be switched on.
- **How is success measured?** Each domain needs numbers that say when a version is better and when an agent is ready to act for real.
- **How is the owner told** about plans and reports waiting for approval, results and problems? Every new version waits for them, so this sets the pace of the whole system.
- **How are live keys kept safe once agents act for real?** They are what lets an agent act in the owner's name.
- **May a self-improvement helper retire a losing version on its own, or only propose it?** With many versions running, it decides how much the owner must handle by hand.

## Going deeper

The README describes every part of the system domain exactly: what each part holds and does, how the parts connect, and where each part's own docs are. It is at `agents/system/docs/README.md`. The project as a whole, including the apps and the records, is described in the project's own vision at `docs/vision.md`, and each domain has its own vision that builds on this one.
