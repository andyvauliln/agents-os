---
name: vision-doc
description: Write or update vision.md, the top-level doc of a level - what we are building there and why, the concept, how it should work, the business logic, worked examples, where it stands and what is still open. Use it at any of the five doc levels (project, system, trading, apps, one app) to build vision.md the first time, and whenever an input changes the goals, the concept, how that level should behave, its business rules, the stage, the plans, an idea or an open question. It is the first of the four docs of a level.
---

# Vision doc

## What vision.md is

The top-level doc of a level: the first one anyone opens there, and the one everything else at that level goes deeper from. It explains what we are building and why, the concept behind it, how it should work, the business logic (how ideas turn into results and how we decide what to keep), with a few worked examples, then where the level stands and what is still open. Someone who reads only the vision can say in their own words what this part of the project is, why it exists and how it should behave.

It stays at that height. How each part is built and laid out, with its folders, files and paths, is the README's job. The exact spec an AI would rebuild the level from is the rebuild prompt's. The vision describes parts only by what they do, and ends by naming the README as the way deeper.

## The five doc levels

Every level has its own `docs/` folder with the same four docs: `vision.md`, `README.md`, `README.asd.md` and `rebuild-prompt.md`. Each level tells only its own story.

| Level | Folder | What its vision covers |
|---|---|---|
| Project | `docs/` at the top of the repository | The whole repository and how the project is worked on: the owner builds it by vibecoding (they say what they want in plain words and AI writes the plans, docs and code), the project IDE is their window on that work, and the work goes in stages. Stage one, now: finish the project IDE, go through every file and folder, write custom views, make all metadata correct, and finish the docs of the project, the system, trading and apps. Stage two: the prediction-market domain and everything below it. |
| System | `agents/system/docs/` | The system domain: the Agent OS as a home for AI agents of any kind, the system agent, the shared machinery every domain uses, and the rules that hold for every agent. |
| Trading | `agents/trading/docs/` | What all trading domains share, why trading is a folder of domains, and how a new trading domain is made from the first one. |
| Apps | `apps/docs/` | What apps are for, the kinds of apps (our own, apps from outside that we fork, research clones), and every app in a sentence or two. |
| One app | `apps/<app>/docs/`, such as `apps/project-IDE/docs/` | That app: what it is for, who uses it, how it should work for us. |

The domains and the levels below them, starting with the prediction-market domain and its strategies, are stage two. Their folders exist, but their docs are not written now. When stage two starts, each domain gives the outlines and lengths of the docs of the levels it defines below itself, in its own `docs/doc-outlines.md`. Until then, a parent level only says that this domain is stage two.

Anything shared with a level above is not explained again: sum it up in a sentence or two ("Like every part of the system, it is tried in test mode first"), then describe only what is different. A parent sums up each child level in a short paragraph and names that child's docs folder.

## Who reads it

- The owner, and people they share the project with, who may not be technical.
- Every agent, for the high-level view of what this level is trying to achieve.
- Claude Code started in `agents/system/`: `agents/system/CLAUDE.md` tells it to read the project vision first and the system vision third.

## The four docs of a level, in order

Inside a level the docs are always written in this order:

1. `vision.md`, with this skill.
2. `README.md`, with `readme-doc`. Its "In short" uses the vision's words.
3. `README.asd.md`, with `readme-asd-doc`, right after the README.
4. `rebuild-prompt.md`, with `rebuild-prompt-doc`, last.

When every level is written fresh, take the levels in this order: project, system, apps, the project IDE, trading. After a child level's vision changes, check what its parent says about it and bring the parent in line, up to the project level.

## What to read before writing

- **The notes:** every owner input word for word, the decisions, the changelog and the answers we gave. While we plan they are in `vision/docs/` (`inputs/`, `decisions.md`, `changelog.md`, `file-tree.md`, the topic notes). Newest wins when they disagree.
- **The owner's requirements by scope:** the inputs vision, kept in `vision/archive/2026-10-12/claude-docs/inputs-vision.md`. It is the best single summary of what the owner wants.
- **The current doc** (often an older draft) and the earlier drafts in `vision/archive/`.
- **What exists today:** the real repository (`git ls-files`, leaving out `vision/archive/`), the File Tree page, the other docs of this level.
- **The level above:** its `vision.md`, so this one agrees with it and does not repeat it.

## Outline

The file always has these sections, in this order. A heading can be worded to fit the level, and a section that has nothing to say at a level is left out (see "What each section holds at each level"), but the order and the purpose stay the same. Write `vision.example.md` next to the doc from this outline, adapted to the level: it is the file's Example tab on the File Tree page. The page build also reads the block below.

```markdown
# [Name of the level]: vision

## In short
One paragraph: what this level is and what it is for. A reader who stops here has the essence.

## Why it exists
The problem or the opportunity, the goals as a short list, and what success looks like.

## The concept
The core idea in a few paragraphs: the kinds of parts this level has, described by what they do, and the ideas that make it work.

## How it should work
The main loop of this level told as a story in numbered steps, with a small picture when it helps. No folder or file names.

## The business logic
How this level turns ideas into results and decides what to keep: the rules, each as a plain statement, and who approves what.

## Examples
Two to four worked examples, each followed from start to end in a short paragraph or a few steps. Real names of sources and services, no file names.

## What the owner sees and does
How the owner uses and steers this level, as a short list.

## Where we are and what comes next
Honest status: the current stage, what exists today, what is designed but not built. Then the next steps in order. No dates unless the owner gave them.

## Principles
The rules of thumb this level follows, each in one or two sentences with the reason behind it.

## Ideas we are still weighing
Not decided. For each idea: the problem, the idea in plain words, and what it would change.

## Open questions
What only the owner can answer about the goals and the way this level should behave, each as one plain question with a sentence on why it matters.

## Going deeper
Two or three sentences: this level's README describes every part exactly, with its path.
```

### What each section holds at each level

- **Project.** In short: the Agent OS project as a whole, the repository that holds it, and how it is built. Why it exists: why the owner wants one system for agents of any kind, and why they build it by vibecoding with one window on it. The concept: the main areas of the repository by what they do (the agents with the system and the domains, the apps with the project IDE, the knowledge base and planning area, the keys folder), the docs at every level, and the metadata next to every file. How it should work: a round of work as a story: the owner gives an input (in chat, on the File Tree page, by voice); it is stored word for word; a change gets a plan the owner sees; it is built; the docs, the metadata and the page are brought in line; the round is saved to git. The business logic: decided means the owner decided; our ideas are proposals; nothing acts live without the owner; what makes a stage done. What the owner sees and does: the File Tree page, the docs, the request box, Apply changes. Where we are: stage one and its work, stage two and what it holds. Going deeper: `docs/README.md`.
- **System.** In short: the Agent OS, a personal system that runs many small AI agents of any kind and keeps the ones that work. The concept: workers, the levels of agents, the helpers, the owner; many small agents with one job each, everything tried safely first, versions that compete, plain files everyone can read, one place to see and steer it all. How it should work: where information comes from, how each agent gets only what it needs, how it decides and acts, when it runs, how it acts safely, how it is tested and improves, how agents work together. The business logic: how an idea becomes an agent and a change becomes a new version, test mode and live mode, how results are compared and the better versions kept, who lets an agent act live, the limits, the costs (AI, the server), and how an agent that does not work is stopped. Examples: a new agent from its idea to its first approved live action; a worker that collects news many agents read; one agent's output used by others through a link. Going deeper: `agents/system/docs/README.md`.
- **Trading.** In short: trading as a folder of trading domains. Why: why trading is the first kind of agent the owner runs. The concept: what every trading domain shares (money and risk rules, accounts, venues, the order stop switch) and what each domain adds. How it should work: how a new trading domain is made by copying the first one. The business logic: the trading rules that hold for every domain. Where we are: the prediction-market domain is the first trading domain and is stage two; a copy-trading domain may come later. Going deeper: `agents/trading/docs/README.md`.
- **Apps.** In short: what an app is in this project and why the system has apps. The concept: the kinds of apps (our own, such as the project IDE; apps from outside that we use and fork; repositories cloned for research). How it should work: how an outside app is adopted and kept up to date, and where a research clone goes. Every app in a sentence or two. Leave out Examples and Principles when they add nothing. Going deeper: `apps/docs/README.md`.
- **One app.** In short: what the app is for and who uses it. Why it exists (for an outside app: why this one, and what we changed or plan to change). How it should work for us. What the owner sees and does with it. Where it stands and what comes next. Open questions. Going deeper: the app's README. The other sections only when they add something. For the project IDE: the owner's window on the project, and the context every AI works from.

## Length

| Level | Length |
|---|---|
| Project | about 1,500 to 3,000 words |
| System | about 2,500 to 4,000 words |
| Trading | 800 to 1,500 words |
| Apps | 500 to 1,200 words |
| One app | 300 to 1,500 words |

Shorter is better when nothing is lost.

## How to write it

Follow "How every doc is written" in the knowledge base agent. For the vision in particular:

- **Lead with purpose, not machinery.** "The system runs many small AI agents side by side and keeps the ones that work" comes before anything about settings or folders.
- **Stay high.** Parts are described by what they do. No folder or file names, no settings keys, no paths, except the one path in "Going deeper".
- **Explain every term the first time**, in a few words.
- **Business rules as plain statements**: "A new agent always starts in test mode." "Only the owner can let an agent act live."
- **Examples are concrete and short**: a real kind of source, a real outside service, what happens step by step, and how it ends. Say plainly that it is an example.
- **Keep the owner's ideas, names for things and examples**, but state them as facts, not as quotes.
- **State facts as they are today.** No "the owner said", no "later it was decided", no dates or earlier versions.
- **Mark what is settled.** Decided things are stated plainly. Use "an idea we are weighing" or "proposed" for our proposals and "still open" for questions.
- **Be clear about the stage.** "Where we are and what comes next" says plainly what is built and what is only designed; elsewhere describe the design in the present tense. Stage two parts are named as stage two, never described as if they exist.
- **No pointers** to other docs or sections, except "Going deeper" at the end.

Too technical:

> Workers write outputs to `data/workers/[worker]/`; agents get them through `*.link.*` symlinks chosen at creation.

Right:

> Small programs called workers collect information on a schedule, such as prices and news, and save it as simple files. Each agent is handed exactly the files its job needs, so it reads only what matters to it.

Too much history and pointing elsewhere:

> The owner later said workers are just scripts, described in config. How that is built: see the README.

Right:

> Workers are plain scripts. Each agent has one list of everything it runs: what each job does, how often, and which AI model it uses.

## When it goes stale

The vision of a level is stale when:

- an input changes the goals, the concept, how that level should behave, its business rules, what the owner does, the stage or the next steps, a principle, an idea or an open question of that level;
- the owner answers an open question or decides on an idea;
- a child level's vision changes what this level says about it (a new domain or app, a stage that ends);
- the level above changes something this level sums up.

A change to a file name, a format or a path alone does not make the vision stale; it makes the README and the rebuild prompt stale.

## Steps

### First build, or a full rebuild

1. Read the sources above.
2. In the notes (never in the doc), list what the vision must say: one line per point, with its status (decided, proposed, open) and where it came from, grouped by section.
3. Write the doc section by section from that list.
4. Run the checks below.
5. Save the section list with its sources in the notes, at `vision/docs/sources/<level>/vision.md` while we plan (`<level>` is `project`, `system`, `trading`, `apps` or the app's folder name), so the next update knows which sections an input touches.
6. Write the README of the level with `readme-doc`, then `README.asd.md` with `readme-asd-doc`, then the rebuild prompt with `rebuild-prompt-doc`.
7. Write or refresh the metadata of `vision.md` with `file-index`: its How it works, its Details, its Example and its Questions (see "Its page on the File Tree").
8. If the parent level sums up this one, check that summary and bring it in line.

### After an input

1. Ask whether it changes anything listed in "When it goes stale" at this level. If not, the vision stays as it is.
2. Find the sections it touches, using the section list in the notes.
3. Rewrite those passages so the doc still reads as one story. Remove what is no longer true. Never add "Update:" notes.
4. An answered question leaves "Open questions" and its answer goes into the section where it belongs. An idea the owner accepts moves from "Ideas we are still weighing" into its section; an idea they reject is removed.
5. Run the checks and update the section list in the notes.
6. Go on with the README, `README.asd.md` and the rebuild prompt of the level, in that order, where the change reaches them.
7. Refresh the metadata of `vision.md` with `file-index`, and climb to the parent level if its summary of this level changed.

## Its page on the File Tree

The File Tree page shows a tab only when its file exists. For `vision.md` these files sit next to the doc:

- **How it works**, `vision.index.md`: short, plain answers under the fixed headings of `file-index`, for someone who sees the project for the first time:
  - **What it is:** one or two sentences, naming the level.
  - **Who looks after it:** the knowledge base agent with this skill; the owner can also change it on the page.
  - **When and how it changes:** the cases in "When it goes stale", and the steps the agent takes.
  - **Who uses it, and when:** everyone first at this level, every agent as background, the knowledge base agent before it writes the other docs of the level.
  - **Where it is mentioned:** the README and the rebuild prompt of the level, the parent level's docs, the child levels' visions, `agents/system/CLAUDE.md` (for the project and system visions), the knowledge base agent and this skill.
  - **Related knowledge:** the docs that must agree with it and what each adds, and the notes behind it.
  - **Keep in mind:** up to four lines, "When you ..., ...".
- **Details**, `vision.meta.json`: the fields described in `file-index`.
- **Example**, `vision.example.md`: the outline above, adapted to the level.
- **Questions**, `vision.questions.md`: the open questions for the owner about this doc, each with why it matters, or "None open."
- **File**: the doc itself.

## Checks

- A non-technical reader can follow every paragraph. Read it once as that person.
- It stays high: no folder or file names, paths or settings keys outside "Going deeper".
- No `[n]` numbers, decision or input codes, hashes or hidden tags.
- No pointers to other docs or sections except "Going deeper", and no "the owner said", dates or earlier versions.
- Every statement rests on an input, a decision or an answer in the notes. Nothing is invented, examples included: an example only shows rules that are decided.
- Nothing proposed or open is presented as decided. Stage two parts are called stage two.
- It covers only its own level and sums up what it shares with the level above in a sentence or two.
- It agrees with the README, `README.asd.md` and the rebuild prompt of the level, with the level above, and uses the glossary's terms.
- It is within the length for its level.
