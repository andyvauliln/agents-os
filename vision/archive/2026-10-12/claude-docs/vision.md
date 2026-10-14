# The Agent OS: vision

## In short

The Agent OS is a personal system that runs AI agents of any kind: agents that trade, that work on social media or that help with management. It runs many small agents at the same time, each with one clear job, and keeps the ones that work. An agent is a small AI-driven program that reads the information it is given, decides what to do and acts on it. Agents are grouped by area, called domains; each domain arranges its agents in the levels its work needs, and every agent has a parent above it. Small programs collect information such as prices and news, each agent is given only what its job needs, every new idea is tried in test mode first, and a self-improvement helper keeps preparing better versions of each agent, like a wheel that keeps turning. Trading on prediction markets is the first domain. The owner steers everything from one place: they give ideas in plain words, approve every new version before it starts, and are the only one who can let an agent act for real. The project is being planned, and nothing of it is built yet.

## Why we are building it

There is far more useful work for AI agents than one person can set up and watch by hand, and in every area most first ideas do not work. Trading alone offers many ways to make money: on prediction markets, where people trade on the outcome of events such as elections or sports, there are up to about eighty approaches. Other areas, such as social media or management, bring their own kinds of work.

Building one agent at a time is slow. The Agent OS makes trying ideas cheap: it runs many agents side by side, each a small variation of an idea, and lets the results show which ones work. Good ideas can then be combined; in trading, for example, by blending the strategies with the best win rates.

Agents of different kinds need many of the same things: information, running on time, safe testing, getting better and being visible to the owner. Some parts are the same for every kind and some differ, so the shared parts are built once.

The goals:

- agents that are fast, cheap to run, simple, easy to understand and good at their job;
- every change tested before it acts for real, and mistakes found and fixed along the way;
- a system that keeps improving with little hand work;
- full visibility: the owner can see and control every agent and every decision from one place;
- one shared base for every kind of agent, so a new area adds only what is its own.

Success means agents that reliably reach their goal in test mode, then for real once the owner has approved them, while the system keeps finding better versions of them. Each domain says what its goal is: for a trading domain it is money. How success is measured in numbers is still open.

## The concept

Instead of one large program that does everything, the Agent OS is made of many small parts, each with one clear job.

- **Workers** collect information on a schedule, such as prices and news, and save it as simple files.
- **The workers helper** knows every worker. An agent that needs new information asks it, and it points the agent to data that already exists, extends a running worker or creates a new one, so hundreds of agents never build the same worker twice.
- **AI helpers** prepare raw information for the agents, for example by boiling the day's news down to what matters for one topic.
- **The system and its domains.** The **system agent** looks after the whole Agent OS: its domains, its health and its own development. A **domain** is one area of work, such as prediction markets. Its **domain agent** owns the area: it finds and creates the agents of the domain, makes sure they reach the domain's goal, and answers the owner's questions about it.
- **Levels inside a domain.** Each domain arranges its agents in the levels its work needs, and every agent has a parent above it. The prediction-market domain, for example, has strategy agents, each owning one way to make money, and below each strategy its trading agents, the variations of that strategy that actually trade. Another domain may arrange its agents differently.
- **Versions.** Any agent can have versions that differ in settings, instructions, code or AI model. They run side by side and compete, and the better ones are kept. An agent can be plain code, AI or a mix: some jobs need fast code that reacts at once, others gain from an AI's judgement.
- **Self-improvement helpers** sit at every level. The one above a group of agents prepares new versions of them, a domain's compares its agents and proposes new ones, and the system's improves the system itself and reacts to new AI models and tools. They keep a memory between runs and are built from shared templates, so they improve agents in a similar, well-tested way.
- **Support helpers** work on the system itself: the knowledge base agent keeps the docs in line with every input and change, and the project IDE agent looks after the owner's window on the project.
- **The owner** gives ideas, approves what runs and what acts for real, and watches and steers everything.

Five ideas make it work: **many small agents with one job each**, simple, easy to understand and cheap to run; **everything tried safely first**, in test mode, where mistakes cost nothing; **versions that compete**, so results decide what becomes the standard; **plain files everyone can read**, for all information and for each agent's settings and jobs, with no database for now; and **one place to see and steer it all**. Because every agent's name includes its AI model, even agents that differ only by model can run side by side and be compared.

One more idea keeps the system general: what every agent needs, such as test and live modes, the owner's approval, the safety rules and running jobs on time, is built once at the top, and what only one area needs, such as money and orders for trading, lives in that area's domain. A new domain starts as a copy of the one most like it.

## How it should work

The system works in a loop.

1. **Collecting information.** Workers watch sources such as prices, news, important events and errors on a schedule, and save what they find as simple files.
2. **Giving each agent only what it needs.** When an agent is created, it is handed exactly the information its job uses. Each run it reads what is new since the last one, and at the end it keeps what matters, compressed or summarised, and clears out the rest, so the next run starts light. The agent decides this itself, including whether to continue in the same AI session, and whether it needs more: other information, research, or a new worker from the workers helper.
3. **Deciding and acting.** Every run follows the same four steps: read, analyse, decide, act. An agent can act in the outside world in the ways its domain allows (a trading agent buys and sells), wait for more information, set a reminder for its next run, collect extra data, start research, or ask for a worker to be created or changed.
4. **Running at the right moments.** Agents run on a regular interval and when something they care about happens. When important information changes, the current run stops and a new one starts with it; unimportant changes wait for the next run. When something the agent waits for is ready, such as research it started, it runs again with the result. A system helper checks what the server can take and limits how many agents run in parallel.
5. **Acting safely.** Every action that reaches the outside world works in a test mode and a live mode, chosen in the agent's settings. New agents start in test mode; acting for real needs good results and the owner's approval.
6. **Testing on the past.** Where it makes sense, an agent has its own way of being tested on past data, such as replaying a month of old data as if it were live. One thing to watch: an AI model may already know how past events turned out, so an AI agent can look better on old data than it really is. Every level also has its own tests, which the owner can switch on and off.
7. **Getting better.** A self-improvement helper studies the agents' results, logs and decisions, research, outside news and the owner's comments, and prepares a new version with a short report. Once the owner approves it, the new version runs in test mode next to the current ones. The versions compete, and the winners become the new standard.
8. **Agents listening to each other.** An agent can subscribe to what other agents produce. New data reaches it on its next run or, if it is urgent, interrupts the run in progress.
9. **Watching the outside world.** When something new appears, such as a better AI model or a new tool, the system updates the related logic and starts new test agents to see whether it helps.

```text
   sources ──► workers ──► files ──► agents ──► actions (test or live)
                                      ▲   ▲               │
                                      │   └── other agents ▼
                             self-improvement ◄── results, logs, the owner's comments
```

## The business logic

The Agent OS reaches its goals by trying many ideas cheaply and safely, keeping what works and letting an agent act for real only once it has proven itself. These rules hold in every domain; a domain adds its own on top, as trading adds its limits on money.

**Where agents come from.** The owner describes an idea in plain words, and the system builds the agent and fits it in. The system also starts agents itself: domain agents create agents for their area, self-improvement helpers prepare new versions, and a better AI model or tool leads to new test agents. The first domain is prediction markets, and its first agent follows one Polymarket strategy chosen by the owner; more follow once it runs in a good flow.

**From an agent to its versions.** An improvement never changes a running agent; it always becomes a new agent in test mode, and starts only after the owner has read a short report on it and approved it. Versions run side by side and are compared on their results; the winners become the new standard, and a winning change is folded back into the agent above them. What counts as winning is set by each domain's measures of success, which are still open for trading.

**Test first.** Every action that reaches the outside world, such as buying, selling or posting, works in a test mode and a live mode from the start. Every new agent starts in test mode, where nothing real happens. The mode is part of every agent's name, so a test agent and a live agent are always two different agents.

**Where agents may act.** Each domain says where its agents may act and where they only collect information. The prediction-market domain, for example, acts only on blockchains for now and only collects information from centralised exchanges.

**Acting for real.** An agent acts live only after it has shown good results, and only when the owner approves it, one agent at a time. No agent can approve going live, for itself or another, and self-improvement never acts live. Agents may use the keys to test accounts; the live keys are for the owner only and never reach an AI. Acting live comes together with protection against instructions hidden in outside text, such as news.

**Limits and costs.** How many agents run at once follows what the server can take; for now that is one of the owner's own servers, and the system is built to move easily to a bigger one. A stop switch that halts every outside action at once, and hard limits written in code that a domain or an agent may only make stricter, are part of the design but still proposals; the money limits of trading belong to the prediction-market domain. Every AI run costs money, so each kind of work has a fixed model that fits it: the strongest for thinking, planning, improving and acting, cheaper ones for light, high-volume work. Being cheap to run is a goal every agent is improved toward; the AI budget is still open.

**Stopping what does not work.** A version that does not beat the current standard never becomes the standard. The owner can stop or delete any agent at any time, and an urgent message from one agent can interrupt the runs of the agents that listen to it. Whether a self-improvement helper may retire a losing version on its own, or only propose it, is still open.

## Examples

Four short examples, each followed from start to end; the first three come from the prediction-market domain.

**Example: a Polymarket strategy, from idea to its first live trade.** Say the owner describes a strategy: find Polymarket markets whose price is far from the real odds of the event, and buy the side that is too cheap.

1. The prediction-market domain agent sets up an agent for the strategy and two or three versions of it, for example the same strategy on the strongest AI model and on a cheaper one. The owner reads a short report on each and approves them.
2. The versions ask the workers helper for Polymarket prices and news. If a worker from the earlier Polymarket tools already collects them, they get that data; otherwise the helper creates one.
3. They run in test mode, and the strategy is also tested on a month of old markets replayed as if live.
4. The self-improvement helper prepares a new version, say one that sells earlier. The owner approves it, it runs next to the others, and if it does better it becomes the standard.
5. When a version has shown good results, the owner approves it to act for real. Its live version, a separate agent with "live" in its name, places the first real trade on Polymarket.

**Example: a news worker on X, shared by many agents.** A worker follows posts on X (Twitter) about one topic, say an upcoming election, and saves them as data. An agent trading a Polymarket market on that election finds the posts useful and subscribes, so new posts arrive with its information on every run. When another agent wants posts on a related topic, the workers helper extends the running worker instead of building a second one.

**Example: an urgent message interrupts other agents.** In the prediction-market domain, a risk-management agent reads that markets are collapsing, say because a big war has broken out, and writes an urgent message: sell everything. The trading agents subscribe to what it produces, so the message interrupts their runs, and each sells everything it holds, in test or, if it is an approved live agent, for real. The owner sees every decision in one place.

**Example: a second trading domain, copied from the first.** Say the owner wants agents that trade crypto. The new domain starts as a copy of the prediction-market domain, with the same levels, rules and notes, and changes only what is different, such as where it may act and what information it collects. Everything shared, from running jobs on time to the owner's approval before anything goes live, works for it at once, and its first agents start in test mode.

## What the owner sees and does

The owner works with the system the way a manager works with a team.

- They describe an idea in plain words, and the system builds the agent and fits it in: its setup, model, workers and place on the dashboard.
- They read a short report on every new version of an agent and approve it before it starts.
- They watch each agent's results.
- They approve or refuse letting an agent act for real (for a trading agent, giving it an account with real money), and they can stop or delete any agent.
- They leave comments, ask an agent questions and get answers, and say what it should do better.
- They can open any agent and see everything about it: its parts, logs, results, the information it uses and produces, every decision it made, every improvement and exactly what is being tested.

The owner builds the system by vibecoding: they say what they want in plain words, and AI writes the plans, the docs and later the code. That is fast, but it soon becomes hard to see what exists and why, so the owner has their own window on the project: the File Tree page, a clickable map of every folder and file that explains what each one is for and how it works, together with the docs. There they understand, watch, steer and analyse the project, now and while it is built and run. Every question or change they leave there is saved and folded into the docs.

The same window serves the AI doing the work. Before changing a file, an AI sees what it is for, how it works, what depends on it and which rules reach it from the levels above, so one change reaches everything that must follow. Every question the owner asks ends up explained in the docs, so nothing is asked twice.

## Where we are and what comes next

The Agent OS is in its planning phase. Nothing of it is built yet: everything described here is the design.

What exists today:

- a plan of every folder and file, about four hundred items, in which the shared parts say only what holds for every agent and everything about trading sits in the prediction-market domain, with one trading agent worked out in full as an example;
- the File Tree page, the owner's window on the plan;
- the knowledge base agent and the project IDE agent, in draft;
- the docs in plain language, including a prompt from which an AI can rebuild the whole system;
- research on ways to make money on prediction markets, plus studies of self-improving agents and of how trading agents are built;
- earlier Polymarket tools, whose workers and data will be reused where they fit.

The next steps, in order:

1. Finish rewriting the docs at every level for a general system, starting with this vision, then move the plan into one GitHub repository chosen by the owner, shared by the project and the owner's server.
2. Settle the parts of the plan that are still proposals, one by one.
3. Settle which settings are shared and which belong to each agent, with two or three concrete example agents.
4. Build the skeleton for the first run: the system agent, the prediction-market domain agent, one strategy agent and two or three trading agents below it.
5. Build the core tools: creating agents, handing each agent its information, running every job on time, loading keys safely and running tests.
6. Start the wheel with one Polymarket strategy chosen by the owner: run it in test mode and watch how it acts and improves itself.
7. Build a first dashboard: the list of agents, their logs and results, and approvals. Whether it is an app of its own or part of the owner's window on the project is still open.
8. Add more agents to the first domain once the first one runs in a good flow.

Later: more trading domains, each copied from the prediction-market domain, such as copy trading, crypto and trading on what well-known people say; agents of other kinds, such as social media or management; acting live with the owner's approval, together with protection against hidden instructions in outside text; more AI platforms.

## Principles

**Start simple, improve later.** Use the simplest thing that works today, and upgrade it only when a real problem shows up.

**Test first; the owner approves what runs and what acts for real.** Mistakes in test mode cost nothing, and only the owner can let an agent act live.

**Free to act inside those limits.** Agents create workers, helpers and research as they need, and self-improvement may change anything, so small steps never wait for permission.

**Everything is a file the owner can open.** Nothing important is hidden inside a program.

**One standard folder for every agent.** Tools, people and agents always know where to look, at every level and in every domain.

**One file, one job.** Every piece of code does one thing, so it is easy to understand, test and replace.

**Shared things are linked, never copied.** A fix to the one real file reaches everyone who uses it.

**Shared things live at the nearest level that shares them.** What every agent needs lives at the top; what one domain needs lives in that domain, and the rest stays with the agent. So the top stays general, and a new kind of agent never has to read past another kind's details.

**Parents see their children, not the other way round.** The system looks into each domain, and each level into the one below it; lower levels never reach up, so every agent stays self-contained.

**Everything an agent runs is visible and switchable.** One list per agent shows every job it runs, and each can be turned on or off, moved or given another model.

**Every name says what it is.** An agent's name alone tells where it belongs, its version, its model and its mode.

**Every change starts with a plan, and the docs follow it.** The owner sees each change as a plan before it is built; once built, what it taught flows into the docs, so they always describe the system as it is.

**Every AI works with the whole picture.** The docs are exact enough to act on, and whatever an AI learns is filed where it belongs, so the next one starts knowing it.

## Ideas we are still weighing

These two are not decided. Each starts from a problem the system will run into as it grows.

**Agents keep a bookmark instead of having data linked in.**
The problem: an agent is handed its information as links to files when it is created, and every run it must work out what is new. With hundreds of agents, keeping those links right and replaying the past for tests gets harder and harder.
The idea: an agent subscribes to the data it needs, like following a channel, and keeps a bookmark of how far it has read; each run it asks for everything after it. Workers never need to know who reads.
What it would change: no data links to keep up, a clear answer to "what is new", and testing on the past as easy as moving the bookmark back; shared scripts and settings would still be linked.

**Digest shared information once for everyone.**
The problem: many agents may read the same news and prices, and if each summarises them with AI, the same work is paid for many times over.
The idea: a helper reads the raw information once and writes a short shared digest, such as "today's news that matters for crypto markets", and each agent picks out what concerns it.
What it would change: lower AI cost and faster runs once there are many agents; with only a few it saves little.

## Open questions

These are for the owner to answer.

- **What is the AI budget?** It decides how many agents can run, and how often, as the system grows.
- **How is the owner notified** of reports waiting for approval, results and problems? Every new version waits for them, so this sets the pace of the wheel.
- **How are live keys kept safe once agents act for real?** They are what lets an agent act in the owner's name.
- **May a self-improvement helper retire a losing version on its own, or only propose it?** With many versions running, it decides how much the owner must handle by hand.

## Going deeper

The README describes every part of the system exactly: what each part holds and does, how the parts connect, and where each part's own docs are. It is at `agents/system/docs/README.md`. Each domain has its own vision and README, which build on this one.
