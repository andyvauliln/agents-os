---
name: readme-doc
description: Write or rebuild README.md, the full and exact overview of how the whole system works - every main part, what it holds, how the parts connect, with the path to each part's own docs and no logic inside the agents. Use it to build the README the first time, and after every input, answer or change that touches a part of the system, after the vision and before the rebuild prompt, at any level (system, domain and the levels a domain defines).
---

# README doc

## What README.md is

The second doc, read after the vision by anyone who wants a deeper and exact understanding of how the system works. It is long and complete: it describes every main part of the system, what each part is responsible for, what it holds, what it takes from and gives to the other parts, when and where it runs, and how the parts fit together into one working system. Each part ends with the path to that part's own docs, so the reader knows where to go deeper still. It is written for people and for AI alike: plain sentences, exact names.

It is a descriptive view of the parts. It never describes the logic inside an agent: how an agent decides, what an agent's instructions say, how a script works step by step. That belongs in the agent's own docs, which the README points to. The why, the concept, the business rules and the examples are the vision's; the README opens by saying so, in one sentence with the vision's path. The exact spec an AI would rebuild the system from is the rebuild prompt's.

It is kept current after every change to a part of the system, so it always describes the system as it is designed today.

## Who reads it

- Anyone who has read the vision and wants to know exactly how the system works and where everything is, technical or not.
- The owner, to check the whole picture after a round of changes.
- Every agent, before it works on a part of the system it does not know yet.

## What to read before writing

- **The vision**, already updated for this round: the README uses the same words for the same things, and its "In short" matches the vision's.
- **Your notes:** the tree notes (one section per file and folder), the topic notes (architecture, conventions, data, safety, flows), the decisions and the owner's inputs word for word. Every part's description comes from them.
- **What exists today:** the repo, the File Tree page, the docs and the skills, and each part's own docs where they exist, so the paths you give are real.
- **At a lower level:** the parent's README, and this level's own folders, settings, jobs, links, tests, research and results.

## Outline

The file always has these sections, in this order. A heading can be worded to fit, but the order and the purpose stay the same. The File Tree page shows this outline as the file's Example, so keep it in step with what the doc really looks like.

```markdown
# The Agent OS

## In short
Two or three sentences on what the Agent OS is, in the same words as the vision's "In short"; one sentence on where it stands; then what this document is: the full, exact description of every main part of the system and how the parts fit together, with the path to each part's own docs. Why the system exists, how it should behave and its business logic are in the vision, `agents/system/docs/vision.md`.

## The system at a glance
Every main part in one picture and one table (part, what it is for, where it lives). Then how the parts connect: what passes from part to part, step by step, from information coming in to actions, results and improvements. It describes what moves between the parts, never what happens inside an agent.

## How the project is laid out
The top of the folder tree, then the standard folder every agent has, each entry in one line, as two small pictures; then how a level reaches its children's folders.

## The parts
One section per main part, in the order below. Each says, in this order: what the part is and what it is responsible for; what it holds, by real folder and file names; what it takes from the other parts and what it gives them; when and where it runs; what is decided, proposed or still open about it; and on its last line, where its own docs are ("Its docs: `path`").

### Agents and their levels
### The system agent and the shared files
### Domains
### Workers and data
### Jobs and the scheduler
### Links between agents
### Settings and AI models
### Actions: test and live
### Keys and secrets
### Logs
### Tests
### Research
### Self-improvement helpers
### Each agent's AI setup
### The knowledge base and the docs
### The project IDE
### The server

## Where each part's docs are
One table: the part, the path of its own docs (its README where it has one, otherwise the How it works file of its folder), and what those docs add.

## Still open in the design
The design details not settled yet, grouped by part, one line each. Questions about the goals and the business are in the vision.
```

A part that does not exist at this level is left out; a new main part gets its own section in the place where it fits. The parts a domain defines for itself, such as the prediction-market domain's strategies, trading agents and dashboard, are described in that domain's README; the system's Domains part sums up each domain with the path to its README.

### At other levels

The same idea, for the level's own parts. Each level's README describes only its own parts and sums up what it shares with the level above in a sentence or two ("Like every domain here, it runs in test mode first and keeps its settings in one file").

- **Domain** (for example prediction markets): in short; the domain at a glance; how it is laid out; its parts (the agents one level down, one short section each with the path to that agent's README; the information it collects and shares; its settings; its jobs; its tests and research); where each part's docs are; still open.
- **The levels a domain defines below itself:** the outlines in that domain's `docs/doc-outlines.md`. There a domain says what the README of each of its levels holds, and may say what its own README adds to the Domain outline above.
- **App** (in `apps/`): what it is; how it is laid out (for an outside app: the source, our fork, its `main` and `upstream` branches and the commit we use); its parts, each with its docs path; what it takes from and gives to the rest of the system; how to start it; its tests; for an outside app, how it is updated from the source.

## Length

| Level | Length |
|---|---|
| System | about 6,000 to 10,000 words |
| Domain | 1,500 to 3,000 words |
| Levels below a domain | as that domain's `doc-outlines.md` says |
| App | 500 to 2,000 words |

Long is fine when every paragraph tells the reader something exact. Cut repetition, never a part.

## How to write it

Follow "How every doc is written" in the knowledge base agent. For the README in particular:

- **Lead every part with what it is**, in one sentence, then the detail.
- **Exact and complete.** Every main part is here, with its real folder and file names, the names of its settings files and what each holds. A reader, or an agent, can find anything from this doc.
- **Describe, never explain the inside of an agent.** Say what an agent or a script is for, what it reads and writes, and when it runs; never how it decides or how it works step by step.
- **Pointers only in three places:** the vision's path in "In short", the "Its docs" line at the end of each part, and the table of docs. Nowhere else does the README send the reader away; whatever a part needs is said in its own section.
- **The same facts and words as the vision and the other docs.** The README never says something another doc does not, and never says it differently.
- **Problem first** for a design choice, in one or two sentences: what would go wrong without it, then what the part does about it.
- **Status on every claim.** Decided things are stated plainly. Our proposals say "the plan is to" or "we propose". Open points go to "Still open in the design". Nothing is built yet, and "In short" says so.
- **Pictures** where they explain faster than words: the parts and their connections, the top of the tree, the standard folder.
- **No `[n]` numbers, decision or input codes, hashes or history.** Paths and file names are welcome; reference numbers from the notes are not.

Too vague:

> Each agent has some settings and a list of jobs.

Right:

> Each agent keeps its settings in `configs/[name].config.json` and everything it runs in `configs/[name].workers.json`: one entry per job, saying what it runs, how often, whether it is switched on, where it runs and which AI model it uses. One scheduler reads every agent's jobs file.

Too deep, the inside of an agent (an example from the prediction-market domain):

> The momentum agent buys when the price has risen three times in a row and sells after a 10% gain.

Right:

> Each trading agent runs one variation of its strategy, reads the data files its strategy needs and writes its decisions to its own `logs/`. What it trades and when is described in its own docs: `agents/trading/prediction-market/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/docs/README.md`.

## Steps

### First build, or a full rebuild

1. Read the sources above.
2. In your notes (never in the doc), list what the README must say: one line per point, with its status (decided, proposed, open) and where it came from, grouped by section and part.
3. Check that every "Its docs" path is a real file or folder in the tree; where a part has no docs of its own yet, give its folder's How it works file.
4. Write the doc section by section from that list.
5. Run the checks below.
6. Save the section list with its sources in `sources/readme.md` in the notes, so the next update knows which sections an input touches.
7. Bring the rebuild prompt in line with `rebuild-prompt-doc`.
8. Refresh the How it works panel of `README.md` on the File Tree page (see "Its page on the File Tree").

### After every update

This runs every round that touches a part of the system, after the vision and before the rebuild prompt.

1. Find the parts the change touches, using `sources/readme.md` in the notes. Always check "Still open in the design" and the table of docs.
2. Rewrite those passages so each part still reads as one current description. Remove what is no longer true. Never add "Update:" notes.
3. A settled design detail leaves "Still open in the design" and goes into its part.
4. If the description of the project in "In short" changed, bring the repo's front page in line too: the short `README.md` at the root of the repo, which says in a few lines what the project is and where to start.
5. Run the checks and update `sources/readme.md` in the notes.
6. If the outline or the way the doc is kept changed, refresh the How it works panel too.

## Its page on the File Tree

Every file shows the same tabs on the File Tree page. For `README.md`:

- **Example** shows the outline above: the sections of the file and what goes in each.
- **How it works** shows short, plain answers under fixed headings, for someone who sees the project for the first time. They live in `README.index.md` next to the doc. Write them with the `file-index` skill after every change to the outline or to the way the doc is kept:
  - **What it is:** one or two sentences.
  - **Who looks after it:** the knowledge base agent with this skill; the owner can also change it on the page.
  - **When and how it changes:** after every change to a part of the system, after the vision and before the rebuild prompt, and the steps the agent takes.
  - **Who uses it, and when:** readers after the vision, the owner after each round, every agent before working on a part it does not know.
  - **Where it is mentioned:** the vision's last section, the repo's front page, the agent's instructions and this skill, the rebuild prompt's skill, the README of every lower level.
  - **Related knowledge:** the docs it agrees with and what each adds, and the notes behind it.
  - **Keep in mind:** up to four lines, "When you ..., ...".
- **Questions** and **File** work as for every other file.

## Checks

- A reader who has read the vision can read this alone and then find any part of the system and say what it does and what it connects to. Read it once as that person, and once as an agent looking for a file.
- Every main part has its section, and every section ends with a real path.
- Nothing describes the logic inside an agent.
- No `[n]` numbers, decision or input codes, hashes, hidden tags, "the owner said", dates or earlier versions.
- Every statement rests on an input, a decision, an answer or something that exists. Nothing is invented.
- Nothing proposed or open is presented as decided.
- It agrees with the vision, the rebuild prompt and the other docs, and uses the glossary's terms.
- "Still open in the design" is current.
- It is within the length for its level.
