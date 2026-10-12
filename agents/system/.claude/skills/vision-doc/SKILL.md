---
name: vision-doc
description: Write or update vision.md, the top-level doc - what we are building and why, the concept, how it should work, the business logic, worked examples, where we are and what is still open. Use it to build vision.md the first time, and whenever an input changes the goals, the concept, how the system should behave, the business rules, the plans, an idea or an open question, at any level (system, domain and the levels a domain defines).
---

# Vision doc

## What vision.md is

The top-level doc: the first one anyone opens, and the one everything else goes deeper from. It explains what we are building and why, the concept behind it, how the system should work, the business logic (how the system turns ideas into results and decides what to keep), with a few worked examples, then where the project stands and what is still open. Someone who reads only the vision can say in their own words what the Agent OS is, why it exists, how it should behave and how it decides what is worth keeping.

It is written mostly for people, and every agent reads it too, for the high-level view of what the system is trying to achieve.

It stays at that height. How each part of the system is built and laid out, with its folders, files and paths, is the README's job; the exact spec an AI would rebuild the system from is the rebuild prompt's. The vision describes parts only by what they do. It ends by saying where to go deeper: the README.

## Who reads it

The owner, people they share the project with, who may not be technical, and every agent in the system.

## What to read before writing

- **Your notes:** every owner input word for word, the decisions, and the answers we gave. The owner's first vision brief and their first description of the folders and the workflow are where the vision starts; later inputs refine it.
- **The other docs**, so that the vision agrees with them, and the README's "In short", which uses the same words.
- **What exists today:** the repo (for example the research in each domain), the File Tree page, the docs.
- **At a lower level:** the parent's `vision.md`, and this level's own prompt and configs.

## Outline

The file always has these sections, in this order, at every level. A heading can be worded to fit, but the order and the purpose stay the same. The File Tree page shows this outline as the file's Example, so keep it in step with what the doc really looks like.

```markdown
# The Agent OS: vision

## In short
One paragraph: what we are building and what it is for. A reader who stops here has the essence.

## Why we are building it
The problem or the opportunity, the goals as a short list, and what success looks like.

## The concept
The core idea in a few paragraphs: the kinds of parts the system has, described by what they do (workers, the levels of agents, the helpers, the owner), and the ideas that make it work: many small agents with one job each, everything tried safely first, versions that compete, plain files everyone can read, one place to see and steer it all.

## How it should work
The main loop told as a story in numbered steps: where information comes from, how each agent gets only what it needs, how it decides and acts, when it runs, how it acts safely, how it is tested and gets better, how agents work with each other. A small picture of the loop. No folder or file names.

## The business logic
How the system turns ideas into results and decides what lives: how an idea becomes an agent and a change becomes a new version, test mode and live mode, how results are compared and the better versions kept, when an agent may act live and who approves it, what limits apply, what costs count (AI, the server) and how an agent that does not work is stopped. Each rule as a plain statement.

## Examples
Two to four worked examples, each followed from start to end in a short paragraph or a few steps: for instance a new agent from its idea to its first approved live action, a worker that collects news many agents read, one agent's output used by others through a link. Real names of sources and services, no file names.

## What the owner sees and does
How the owner uses and steers the system day to day, as a short list, and how they work with it while it is being planned.

## Where we are and what comes next
Honest status in a few sentences: what exists today, what is designed but not built. Then the next steps in order, and the longer-term plans in one short paragraph. No dates unless the owner gave them.

## Principles
The rules of thumb the system follows, each in one or two sentences with the reason behind it.

## Ideas we are still weighing
Not decided. For each idea, three short parts: the problem (what goes wrong without it, with enough context to see why it comes up), the idea in plain words, and what it would change. When the owner decides, the idea moves into the section it belongs to, or is removed.

## Open questions
What only the owner can answer about the goals, the business and the way the system should behave, each as one plain question with a sentence on why it matters. Design details still to settle are in the README.

## Going deeper
Two or three sentences: the README describes every part of the system exactly, how the parts fit together and where each part's own docs are, at `agents/system/docs/README.md`.
```

### At other levels

- **Domain** (for example prediction markets): in short; why this domain; the concept here; how it reaches its goal (the business logic); examples; where it stands and what comes next; its own principles, ideas and questions; going deeper (this domain's README).
- **The levels a domain defines below itself:** the outlines in that domain's `docs/doc-outlines.md`. There a domain says what the vision of each of its levels holds, and may say what its own vision adds to the Domain outline above.
- **App** (in `apps/`, ours or from outside): what it is for and who uses it; why we have it (for an outside app: why this one, and what we changed or plan to change); how it should work for us; where it stands and what comes next; open questions; going deeper.

Anything shared with the level above is not explained again: sum it up in a sentence or two ("Like every agent here, it is tried in test mode first and improved through new versions that compete"), then describe only what is different.

## Length

| Level | Length |
|---|---|
| System | about 2,500 to 4,000 words |
| Domain | 800 to 1,500 words |
| Levels below a domain | as that domain's `doc-outlines.md` says |
| App | 300 to 1,000 words |

Shorter is better when nothing is lost.

## How to write it

Follow "How every doc is written" in the knowledge base agent. For the vision in particular:

- **Lead with purpose, not machinery.** "The system runs many small AI agents side by side and keeps the ones that work" comes before anything about settings or folders.
- **Stay high.** Parts are described by what they do. No folder or file names, no settings keys, no paths, except the one path in "Going deeper".
- **Explain every term the first time**, in a few words.
- **Business rules as plain statements**: "A new agent always starts in test mode." "Only the owner can let an agent act live."
- **Examples are concrete and short**: a real kind of source, a real outside service, what happens step by step, and how it ends. Say plainly that it is an example.
- **Keep the owner's ideas, names for things and examples**, but state them as facts about the system, not as quotes.
- **State facts as they are today.** No "the owner said", no "later it was decided", no dates or earlier versions.
- **Mark what is settled.** Decided things are stated plainly as how the system works. Use "an idea we are weighing" for proposals and "still open" for questions.
- **Be clear that nothing is built yet.** "Where we are and what comes next" says it plainly; elsewhere describe the design in the present tense.
- **No pointers** to other docs or sections, except "Going deeper" at the end.

Too technical:

> Workers write outputs to `data/workers/[worker]/`; agents get them through `*.link.*` symlinks chosen at creation.

Right:

> Small programs called workers collect information on a schedule, such as prices and news, and save it as simple files. Each agent is handed exactly the files its job needs, so it reads only what matters to it.

Too much history and pointing elsewhere:

> The owner later said workers are just scripts, described in config. How that is built: see the README.

Right:

> Workers are plain scripts. Each agent has one list of everything it runs: what each job does, how often, and which AI model it uses.

## Steps

### First build, or a full rebuild

1. Read the sources above.
2. In your notes (never in the doc), list what the vision must say: one line per point, with its status (decided, proposed, open) and where it came from, grouped by section.
3. Write the doc section by section from that list.
4. Run the checks below.
5. Save the section list with its sources in `sources/vision.md` in the notes, so the next update knows which sections an input touches.
6. Bring the README in line with the `readme-doc` skill (its "In short" uses the same words), then the rebuild prompt with `rebuild-prompt-doc`.
7. Refresh the How it works panel of `vision.md` on the File Tree page (see "Its page on the File Tree").

### After an input

1. Ask whether it changes the goals, the concept, how the system should work, the business logic, what the owner does, where we are, the plans, a principle, an idea or an open question. If not, the vision stays as it is.
2. Find the sections it touches, using `sources/vision.md` in the notes.
3. Rewrite those passages so the doc still reads as one story. Remove what is no longer true. Never add "Update:" notes.
4. An answered question leaves "Open questions" and its answer goes into the section where it belongs. An idea the owner accepts moves from "Ideas we are still weighing" into its section; an idea they reject is removed.
5. Run the checks and update `sources/vision.md` in the notes.
6. If the outline or the way the doc is kept changed, refresh the How it works panel too.

## Its page on the File Tree

Every file shows the same tabs on the File Tree page. For `vision.md`:

- **Example** shows the outline above: the sections of the file and what goes in each.
- **How it works** shows short, plain answers under fixed headings, for someone who sees the project for the first time. They live in `vision.index.md` next to the doc. Write them with the `file-index` skill after every change to the doc or this skill:
  - **What it is:** one or two sentences.
  - **Who looks after it:** the knowledge base agent with this skill; the owner can also change it on the page.
  - **When and how it changes:** which kinds of input change it, and the steps the agent takes.
  - **Who uses it, and when:** everyone first, every agent as background, the knowledge base agent before writing the other docs.
  - **Where it is mentioned:** the README and the rebuild prompt, the agent's instructions and this skill, the vision of every lower level, the file tree.
  - **Related knowledge:** the docs that must agree with it and what each adds, and the notes behind it.
  - **Keep in mind:** up to four lines, "When you ..., ...".
- **Questions** and **File** work as for every other file.

## Checks

- A non-technical reader can follow every paragraph. Read it once as that person.
- It stays high: no folder or file names, paths or settings keys outside "Going deeper".
- No `[n]` numbers, decision or input codes, hashes or hidden tags.
- No pointers to other docs or sections except "Going deeper", and no "the owner said", dates or earlier versions.
- Every statement rests on an input, a decision or an answer in your notes. Nothing is invented, examples included: an example only shows rules that are decided.
- Nothing proposed or open is presented as decided.
- It agrees with the README and the rebuild prompt, and uses the glossary's terms.
- It is within the length for its level.
