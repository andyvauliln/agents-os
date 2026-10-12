---
name: readme-doc
description: Write or rebuild README.md, the full and exact overview of how a level works - every main part, what it holds, how the parts connect, with the path to each part's own docs and no logic inside the agents. Use it at any of the five doc levels (project, system, trading, apps, one app) to build the README the first time, and after every input, answer or change that touches a part of that level, after the vision and before README.asd.md and the rebuild prompt.
---

# README doc

## What README.md is

The second doc of a level, read after the vision by anyone who wants a deeper and exact understanding of how that level works. It is long and complete: it describes every main part, what each part is responsible for, what it holds, what it takes from and gives to the other parts, when and where it runs, and how the parts fit together. Each part ends with the path to that part's own docs, so the reader knows where to go deeper still. It is written for people and for AI alike: plain sentences, exact names.

It is a descriptive view of the parts. It never describes the logic inside an agent: how an agent decides, what its instructions say, how a script works step by step. That belongs in the part's own docs, which the README points to. The why, the concept, the business rules and the examples are the vision's; the README opens by saying so, in one sentence with the vision's path. The exact spec an AI would rebuild the level from is the rebuild prompt's.

Right after every change to the README, `README.asd.md` is written again from it with `readme-asd-doc`, so the owner can compare the two.

## The five doc levels

Every level has its own `docs/` folder with the same four docs: `vision.md`, `README.md`, `README.asd.md` and `rebuild-prompt.md`. Each README describes only its own level's parts.

| Level | Folder | What its README covers |
|---|---|---|
| Project | `docs/` at the top of the repository | The whole repository, part by part, and how the project is worked on: every top folder and file, the metadata next to every item, the planning area `vision/`, the keys folder, the rounds of work, the stages. |
| System | `agents/system/docs/` | The system domain: every part of the system agent's folder and the shared machinery every domain uses. |
| Trading | `agents/trading/docs/` | What `agents/trading/` holds and what every trading domain shares, with each trading domain summed up and its docs path. |
| Apps | `apps/docs/` | What `apps/` holds, the kinds of apps and the rules for each kind, and every app with the path to its docs. |
| One app | `apps/<app>/docs/`, such as `apps/project-IDE/docs/` | That app's parts. For the project IDE the README is the app's full documentation. |

The domains and the levels below them, starting with the prediction-market domain and its strategies, are stage two. Their folders exist, but their docs are not written now. When stage two starts, each domain gives the outlines and lengths of the docs of the levels it defines below itself, in its own `docs/doc-outlines.md`. Until then a parent README describes such a domain by its folder and says it is stage two, without describing files inside it.

A level sums up what it shares with the level above in a sentence or two ("Like every part of the repository, each file here has its How it works and Details files next to it"), then describes only what is its own.

## Who reads it

- Anyone who has read the vision of the level and wants to know exactly how it works and where everything is, technical or not.
- The owner, to check the whole picture after a round of changes, and to compare it with `README.asd.md`.
- Every agent, before it works on a part it does not know yet.
- Claude Code started in `agents/system/`: `agents/system/CLAUDE.md` tells it to read the project README second and the system README fourth, and the project IDE README after the file tree.

## The four docs of a level, in order

Inside a level the docs are always written in this order:

1. `vision.md`, with `vision-doc`.
2. `README.md`, with this skill.
3. `README.asd.md`, with `readme-asd-doc`, right after the README.
4. `rebuild-prompt.md`, with `rebuild-prompt-doc`, last.

When every level is written fresh, take the levels in this order: project, system, apps, the project IDE, trading. After a child level's README changes a path or a part its parent names, bring the parent's README in line, up to the project level.

## What to read before writing

- **The vision of the level**, already updated for this round: the README uses the same words, and its "In short" matches the vision's.
- **The notes:** the tree notes (`vision/docs/file-tree.md`, one section per file and folder), the topic notes (architecture, conventions, data schemas, safety, flows), the decisions, the changelog and the owner's inputs word for word, all in `vision/docs/` while we plan. Newest wins when they disagree.
- **What exists today:** the real repository (`git ls-files`, leaving out `vision/archive/`), the File Tree page, the skills and agents, and each part's own docs, so every path you give is real.
- **The level above:** its README, so this one agrees with it and does not repeat it.

## Outline

The file always has these sections, in this order. A heading can be worded to fit the level, but the order and the purpose stay the same. Write `README.example.md` next to the doc from this outline, adapted to the level: it is the file's Example tab on the File Tree page. The page build also reads the block below.

```markdown
# [Name of the level]

## In short
Two or three sentences on what this level is, in the same words as the vision's "In short"; one sentence on the current stage; then what this document is: the full, exact description of every main part of the level and how the parts fit together, with the path to each part's own docs. Why it exists, how it should behave and its business logic are in the vision, at its path.

## At a glance
Every main part in one picture and one table (part, what it is for, where it lives). Then how the parts connect: what passes from part to part, step by step. It describes what moves between the parts, never what happens inside an agent.

## How it is laid out
The tree of this level's folder, each entry in one line, as a small picture; then how this level reaches the folders of its children.

## The parts
One section per main part. Each says, in this order: what the part is and what it is responsible for; what it holds, by real folder and file names; what it takes from the other parts and what it gives them; when and where it runs; what is decided, proposed or still open about it; and on its last line, where its own docs are ("Its docs: `path`").

### [Part]

## Where each part's docs are
One table: the part, the path of its own docs (its README where it has one, otherwise the How it works file of its folder), and what those docs add.

## Still open in the design
The design details not settled yet, grouped by part, one line each. Questions about the goals and the business are in the vision.
```

### The parts at each level

A part that does not exist at a level is left out; a new main part gets its own section where it fits.

- **Project.** The top of the repository: the front page `README.md`, `.gitignore`, the project docs in `docs/` (the four docs and `docs/file-tree.md`, the plain list of every path, built by the IDE build); `agents/` with the system domain and the trading folder; `apps/` with the project IDE; the keys folder `.secrets/` (in git without the `.env` files, which stay on the machine); the planning area `vision/` (the knowledge base, the drafts, the mirror of metadata, the build tools, the archive); the metadata files next to every file and folder; how the project is worked on (the owner's inputs, plans, the knowledge base agent and the project IDE agent, the page build, git, pull requests into `main`); the stages, with what stage one holds and what waits for stage two; `agents/system/CLAUDE.md` as the way in for Claude Code.
- **System.** Agents and their levels; the system agent and its shared files; domains (each summed up with its docs path; trading's at `agents/trading/docs/`); workers and data; jobs and the scheduler; links between agents; settings and AI models; actions in test and live; keys and secrets; logs; tests; research; self-improvement helpers; each agent's AI setup (`.claude/`, `CLAUDE.md`); the knowledge base agent, the project IDE agent and their skills; the project IDE in one short part with its docs path; the server.
- **Trading.** What `agents/trading/` holds (`docs/`, `researches/` with the research studies, one folder per trading domain); what every trading domain shares; how a new trading domain is made; the prediction-market domain summed up as stage two, by its folder only; where the trading parts that every domain uses live.
- **Apps.** What `apps/` holds (`docs/`, one folder per app, `temp/` for research clones that are never committed); the kinds of apps and the rules for each (our own app; an outside app we use, forked with our `main` and an `upstream` branch that follows the source; a research clone); every app with what it is, its state and its docs path (`project-IDE/`, `trading-ui/` and any other).
- **One app.** What it is; how it is laid out (for an outside app: the source, our fork, its `main` and `upstream` branches and the commit we use); its parts, each with its docs path; what it takes from and gives to the rest of the project; how to start it; its tests; for an outside app, how it is updated from the source. For the project IDE, the full documentation: the File Tree page and its data, every tab and the metadata file behind it, the metadata switch, edits, notes and deletes, Apply changes, the request box and voice input, the server on the owner's machine, the build and the sync, the knowledge it is built from, and how to start and check it.

## Length

| Level | Length |
|---|---|
| Project | about 3,000 to 6,000 words |
| System | about 6,000 to 10,000 words |
| Trading | 1,000 to 2,500 words |
| Apps | 800 to 2,000 words |
| One app | 500 to 2,000 words; the project IDE, as its full documentation, about 3,000 to 8,000 |

Long is fine when every paragraph tells the reader something exact. Cut repetition, never a part.

## How to write it

Follow "How every doc is written" in the knowledge base agent. For the README in particular:

- **Lead every part with what it is**, in one sentence, then the detail.
- **Exact and complete.** Every main part is here, with its real folder and file names, the names of its settings files and what each holds. A reader, or an agent, can find anything from this doc.
- **Describe, never explain the inside of an agent.** Say what an agent or a script is for, what it reads and writes, and when it runs; never how it decides or how it works step by step.
- **Pointers only in three places:** the vision's path in "In short", the "Its docs" line at the end of each part, and the table of docs. Nowhere else does the README send the reader away.
- **The same facts and words as the vision and the other docs.** The README never says something another doc does not, and never says it differently. Use the same name for a thing every time: `README.asd.md` keeps those names exactly.
- **Problem first** for a design choice, in one or two sentences: what would go wrong without it, then what the part does about it.
- **Status on every claim.** Decided things are stated plainly. Our proposals say "the plan is to" or "we propose". Open points go to "Still open in the design". "In short" says what is built and what is only designed. Stage two parts are named as stage two and never described as if they exist.
- **Pictures** where they explain faster than words: the parts and their connections, the tree of the level.
- **No `[n]` numbers, decision or input codes, hashes or history.** Paths and file names are welcome; reference numbers from the notes are not.

Too vague:

> Each agent has some settings and a list of jobs.

Right:

> Each agent keeps its settings in `configs/[name].config.json` and everything it runs in `configs/[name].workers.json`: one entry per job, saying what it runs, how often, whether it is switched on, where it runs and which AI model it uses. One scheduler reads every agent's jobs file.

Too deep, the inside of an agent:

> The momentum agent buys when the price has risen three times in a row and sells after a 10% gain.

Right:

> Each trading domain keeps its agents in its own folder; what each agent trades and when is described in that agent's own docs.

## When it goes stale

The README of a level is stale when:

- a part of that level is added, removed, renamed or moved, or a file or folder in it changes what it holds;
- a format, a settings file, a job, a link or a rule of a part changes;
- the path of a part's docs changes, or a part gets its own docs;
- a design point is settled, or a new one opens;
- the vision of the level changed its "In short" or a name;
- a child level's README changed a path or a part this README names.

When the README changes, `README.asd.md` is stale at once, and the rebuild prompt of the level usually is too.

## Steps

### First build, or a full rebuild

1. Read the sources above.
2. In the notes (never in the doc), list what the README must say: one line per point, with its status (decided, proposed, open) and where it came from, grouped by section and part.
3. Check that every "Its docs" path is a real file or folder in the repository; where a part has no docs of its own yet, give its folder's How it works file.
4. Write the doc section by section from that list.
5. Run the checks below.
6. Save the section list with its sources in the notes, at `vision/docs/sources/<level>/readme.md` while we plan, so the next update knows which sections an input touches.
7. Write `README.asd.md` from the new README with `readme-asd-doc`, then the rebuild prompt with `rebuild-prompt-doc`.
8. Write or refresh the metadata of `README.md` with `file-index`: its How it works, its Details, its Example and its Questions.

### After every update

This runs every round that touches a part of the level, after the vision and before `README.asd.md` and the rebuild prompt.

1. Find the parts the change touches, using the section list in the notes. Always check "Still open in the design" and the table of docs.
2. Rewrite those passages so each part still reads as one current description. Remove what is no longer true. Never add "Update:" notes.
3. A settled design detail leaves "Still open in the design" and goes into its part.
4. If the project's description in the project README's "In short" changed, bring the repository's front page `README.md` in line too: it says in a few lines what the project is and where to start.
5. Run the checks and update the section list in the notes.
6. Write `README.asd.md` again with `readme-asd-doc`, then update the rebuild prompt.
7. Refresh the metadata of `README.md` with `file-index`, and climb to the parent level if a path or part it names changed.

## Its page on the File Tree

The File Tree page shows a tab only when its file exists. For `README.md` these files sit next to the doc:

- **How it works**, `README.index.md`: short, plain answers under the fixed headings of `file-index`:
  - **What it is:** one or two sentences, naming the level.
  - **Who looks after it:** the knowledge base agent with this skill; the owner can also change it on the page.
  - **When and how it changes:** the cases in "When it goes stale", after the vision and before `README.asd.md` and the rebuild prompt.
  - **Who uses it, and when:** readers after the vision, the owner after each round, every agent before working on a part it does not know, Claude Code through `agents/system/CLAUDE.md`.
  - **Where it is mentioned:** the vision's last section, `README.asd.md`, the parent level's README, the repository's front page (project level), `agents/system/CLAUDE.md`, the knowledge base agent and this skill.
  - **Related knowledge:** the docs it agrees with and what each adds, and the notes behind it.
  - **Keep in mind:** up to four lines, "When you ..., ...".
- **Details**, `README.meta.json`: the fields described in `file-index`.
- **Example**, `README.example.md`: the outline above, adapted to the level.
- **Questions**, `README.questions.md`: the open questions for the owner about this doc, each with why it matters, or "None open."
- **ASD-STE100**, `README.asd.md`: the same README in Simplified Technical English, written with `readme-asd-doc`.
- **File**: the doc itself.

## Checks

- A reader who has read the vision can read this alone and then find any part of the level and say what it does and what it connects to. Read it once as that person, and once as an agent looking for a file.
- Every main part has its section, and every section ends with a real path.
- Nothing describes the logic inside an agent.
- No `[n]` numbers, decision or input codes, hashes, hidden tags, "the owner said", dates or earlier versions.
- Every statement rests on an input, a decision, an answer or something that exists. Nothing is invented. Stage two parts are not described as if they exist.
- Nothing proposed or open is presented as decided.
- It agrees with the vision, the rebuild prompt, the level above and the other docs, and uses the glossary's terms.
- "Still open in the design" is current.
- It is within the length for its level.
- `README.asd.md` was written again from this version.
