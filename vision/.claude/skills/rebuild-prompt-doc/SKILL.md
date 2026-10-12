---
name: rebuild-prompt-doc
description: Write or update rebuild-prompt.md, the prompt an AI coding agent follows to rebuild one level of the Agent OS from what exists above it and end with the same working result - the exact tree of that level's folder, names and formats, every part, the build order, the checks and the child levels' prompts. Use it at any of the five doc levels (project, system, trading, apps, one app) to build the prompt the first time, and after every change to that level's design, last, after the vision, the README and README.asd.md.
---

# Rebuild prompt doc

## What rebuild-prompt.md is

A prompt for an AI coding agent, such as Claude Code. Given this file and the levels above it, the agent rebuilds this level's folder and ends with the same working result: the same folders and file names, the same file formats and settings, the same scripts doing the same jobs, the same agents and helpers with the same instructions in substance, the same safety rules. It is the full and exact spec of the level as it is designed today, written as instructions.

Each prompt builds only its own level's folder. It assumes the levels above exist, names what it takes from them, builds the rest, and lists its children's prompts in build order. The project prompt is the top: an agent that follows it, and then every prompt it lists, rebuilds the whole repository from an empty one.

It is kept current after every change to the level's design, last of the four docs, so that at any moment the level could be rebuilt from it.

It is not a doc for reading through like the vision or the README, although the owner can read it to check. It holds no history, no reasons beyond a line where a reason prevents a wrong guess, no runtime data, logs or results, and never a secret value.

## The five doc levels

Every level has its own `docs/` folder with the same four docs: `vision.md`, `README.md`, `README.asd.md` and `rebuild-prompt.md`.

| Level | Folder | What its prompt builds | Children's prompts it lists |
|---|---|---|---|
| Project | `docs/` at the top of the repository | The top of the repository: the front page `README.md`, `.gitignore`, `docs/` (with how `docs/file-tree.md` is built), the keys folder `.secrets/` (folders, `secrets.index.json` with key names only, empty `.env` files that git ignores), the rule that every file and folder outside `vision/` has its metadata files, the planning area `vision/` and its build tools, `agents/` and `apps/` as folders, and how the project is worked on (git, branches, pull requests into `main`). | system, apps, trading |
| System | `agents/system/docs/` | `agents/system/`: `CLAUDE.md`, the system agent's `.claude/` with its helper agents and skills, configs, scripts, logs, data, docs, tests, research, the start and init scripts. | none in stage one; each domain's prompt in stage two |
| Trading | `agents/trading/docs/` | `agents/trading/`: its `docs/`, its `researches/` (named as existing content, not generated), and one folder per trading domain, with the stage two domains as empty folders. | each trading domain's prompt, in stage two |
| Apps | `apps/docs/` | `apps/`: its `docs/`, one folder per app with its `docs/`, the `temp/` rule for research clones. | each app's prompt |
| One app | `apps/<app>/docs/`, such as `apps/project-IDE/docs/` | That app. For our own app, the exact spec of its parts. For an outside app: the source, how to fork it (our `main`, an `upstream` branch that follows the source), the commit to start from, every change we made, and how to set it up, run and test it; not the outside code file by file. | none |

The domains and the levels below them, starting with the prediction-market domain and its strategies, are stage two. Their folders exist, but their docs are not written now. A prompt above them builds their folders empty and lists them under "Do not build" until stage two. When stage two starts, each domain gives what each prompt of its lower levels covers and how long it is, in its own `docs/doc-outlines.md`.

Until a level's parts are designed, its prompt is only its How it works file.

## Who reads it

- An AI coding agent rebuilding the level, or a part of it.
- An agent checking whether the level still matches its spec.
- The owner, to check that nothing important is missing.

## The four docs of a level, in order

Inside a level the docs are always written in this order: `vision.md` (`vision-doc`), `README.md` (`readme-doc`), `README.asd.md` (`readme-asd-doc`), then this prompt, last. When every level is written fresh, take the levels in this order: project, system, apps, the project IDE, trading. When a child's prompt changes its name, path or what it takes from above, bring the parent's list of child prompts and its tree in line.

## What to read before writing

- **The tree notes** (`vision/docs/file-tree.md`, one section per file and folder, with every name, format and rule) and the real repository (`git ls-files`, leaving out `vision/archive/`). Every path in the prompt comes from them; where they disagree, the newest decision wins, and the conflict goes in your report.
- **The topic notes:** conventions, data schemas, safety, flows, architecture, the how-to runbooks and the common knowledge, for the exact formats and rules.
- **The decisions and the changelog**, so you know what is decided, what is our proposal and what is open.
- **What exists today:** the helper agents and their skills, the build tools in `vision/tools/`, the File Tree page and its server. Where a part exists, the prompt describes it as it is.
- **The vision, the README and `README.asd.md` of the level**, already updated for this round: the prompt uses the same names and never contradicts them.
- **The prompt of the level above**, so this one takes from it exactly what it builds.

## Outline

The file always has these sections, in this order. A heading can be worded to fit the level, but the order and the purpose stay the same. Write `rebuild-prompt.example.md` next to the doc from this outline, adapted to the level: it is the file's Example tab on the File Tree page. The page build also reads the block below.

```markdown
# Rebuild [name of the level]

## Your task
Who you are (an AI coding agent), what you build (this level's folder), what must exist before you start (the levels above), what "the same result" means (the checks at the end), what you never do (write a secret value, set anything live, push or publish without the owner's go), and how to work: follow the build order, run each step's check before the next, and ask the owner whenever this prompt says a point is open.

## The level in brief
What this level is and how it works, in about 300 words, in the same words as its vision: enough to make sensible choices wherever this prompt leaves room.

## What you take from above
The files and rules of the levels above that this level uses, by exact path, one line each.

## Ground rules
The rules every file of this level follows: safety (keys, test and live, approvals), formats (JSON for settings, Markdown for docs, the script languages), names, links, what git ignores, one job per code file, and the metadata files next to every file and folder.

## The tree
This level's complete tree as one code block: every folder and file with a one-line comment. Placeholders in [brackets] with their name format; examples marked as examples; stage two folders marked as empty.

## Conventions
Exact names and formats this level uses, each with an example.

## The parts
One section per part, in the same order as the README's parts. For each: the files to create, by exact path; what each file holds, with the exact schema or key list where one is decided, as a short JSON or Markdown example; what each script does (inputs, outputs, options, errors, what it logs); how the part connects to the others; and the check that proves the part works.

## Build order
Numbered steps from what exists above to the finished level, each ending with its check. The last step runs the children's prompts.

## The children's prompts
The prompt of every level below, by path, in build order, with what each builds in one line.

## Acceptance checks
The list that proves the rebuilt level is the same: the tree matches, every settings file parses and fits its schema, every link is built and none is broken, the tests pass, nothing can act live without the owner's approval, no secret value is in git, every file and folder outside `vision/` has its `.index.md` and `.meta.json`, the File Tree page builds and its tree equals the files on disk.

## Do not build
Ideas still being weighed, questions still open and stage two parts, one line each, with what to leave in their place: nothing, an empty folder, a placeholder or a setting switched off.
```

## Length

| Level | Length |
|---|---|
| Project | about 3,000 to 6,000 words |
| System | about 8,000 to 15,000 words |
| Trading | 1,000 to 3,000 words |
| Apps | 800 to 2,000 words |
| One app | 300 to 3,000 words; the project IDE, about 3,000 to 8,000 |

Every word must help the agent build the right thing. Long is fine; vague is not.

## How to write it

This doc is written for AI, so the rules for docs for people bend here; the knowledge base agent's other rules still hold.

- **Instructions, in the second person and the imperative:** "Create `agents/system/configs/system.config.json` with these keys."
- **Exact everywhere.** Real paths, file names, keys, formats and name patterns, the same as in the tree notes and on disk, character for character. When a format is decided, give it here with a short example.
- **Complete for its own folder.** Every item in this level's tree is covered. If the agent would have to guess, the prompt is not finished: give the detail, or say that the point is open and what to leave in its place. Do not describe the inside of a child level; name its prompt.
- **Status is explicit.** Build what is decided. Build our proposals as they stand, since they are part of the design today, and mark them "default, the owner may change it". Never build an idea still being weighed, an open question or a stage two part: list them under "Do not build".
- **No references from the notes.** No `[n]` numbers, decision or input codes, hashes or hidden tags. Name things by their paths.
- **No history.** Only the level as it is designed now.
- **Never a secret value.** Key names only, and where each key's value is loaded from. A `.env` file is created empty and never read.
- **Checks you can run.** Each check is a command or an observation with a clear pass: "the `check-links` script reports no broken link."
- **Same words** as the vision, the README and the glossary.

Too loose:

> Set up the configs for each agent.

Right:

> In every agent folder create `configs/[name].config.json` (the agent's settings), `configs/[name].workers.json` (every job the agent runs, one entry each with `enabled`, `id`, `purpose`, `type`, `schedule` and, for a script, `run`, for an AI run, `platform`, `model` and `prompt`) and `configs/[name].links.json` (every shared file the agent uses). `[name]` is `system` for the system agent, the domain's folder name for a domain, and the agent's name otherwise. Check: every file parses as JSON and the `check-links` script reports no broken link.

## When it goes stale

The rebuild prompt of a level is stale when anything in the level's design changes: a file or folder added, removed, renamed or moved; a format, schema, key, name pattern or script changed; a rule or a safety setting changed; the build order or a check changed; a proposal decided or dropped; a child level's prompt added, renamed or changed in what it takes from this level; a stage two part moved into stage one. It is updated last, after the vision, the README and `README.asd.md` of the level.

## Steps

### First build, or a full rebuild

1. Read the sources above.
2. In the notes (never in the doc), list every part and every file the prompt must cover, with its status (decided, proposed, open, stage two) and where it came from.
3. Write the doc section by section from that list. Take every path and format from the tree notes and the disk, never from memory.
4. Run the checks below.
5. Save the list with its sources in the notes, at `vision/docs/sources/<level>/rebuild-prompt.md` while we plan, so the next update knows which sections a change touches.
6. Write or refresh the metadata of `rebuild-prompt.md` with `file-index`: its How it works, its Details, its Example and its Questions.
7. Check the parent level's prompt: its tree and its list of children's prompts must match this one.

### After every change

This runs every round that changes the level's design, last of the four docs.

1. Find the sections the change touches, using the list in the notes. Always check the tree, the build order, the children's prompts, the acceptance checks and "Do not build".
2. Rewrite those passages so the prompt still describes one level, as it is designed now. Remove what is no longer true.
3. A point the owner decided leaves "Do not build" and goes into its part, the tree and the build order.
4. Run the checks and update the list in the notes.
5. Refresh the metadata of `rebuild-prompt.md` with `file-index`, and climb to the parent's prompt if this change reaches it.

## Its page on the File Tree

The File Tree page shows a tab only when its file exists. For `rebuild-prompt.md` these files sit next to the doc:

- **How it works**, `rebuild-prompt.index.md`: short, plain answers under the fixed headings of `file-index`:
  - **What it is:** one or two sentences, naming the level.
  - **Who looks after it:** the knowledge base agent with this skill; the owner can also change it on the page.
  - **When and how it changes:** the cases in "When it goes stale", last of the four docs of the level.
  - **Who uses it, and when:** an AI agent rebuilding the level or checking it against its spec; the owner, to check it.
  - **Where it is mentioned:** the parent level's prompt, the children's prompts, the knowledge base agent and this skill, the other doc skills' last steps.
  - **Related knowledge:** the docs and notes it must agree with and what each adds.
  - **Keep in mind:** up to four lines, "When you ..., ...".
- **Details**, `rebuild-prompt.meta.json`: the fields described in `file-index`.
- **Example**, `rebuild-prompt.example.md`: the outline above, adapted to the level.
- **Questions**, `rebuild-prompt.questions.md`: the open questions for the owner about this doc, or "None open."
- **File**: the doc itself.

## Checks

- An AI agent that has never seen the project could build this level from this file and the levels above without guessing. Read it once as that agent, step by step.
- Every path and name matches the tree notes and the disk; every format matches the topic notes.
- Every item of this level's tree is covered, every build step has a check, and every child level's prompt is listed.
- Nothing still weighed, open or stage two is told to be built; every proposal is marked as a default.
- No `[n]` numbers, decision or input codes, hashes, hidden tags or history.
- No secret value anywhere.
- It agrees with the vision, the README and `README.asd.md` of the level, and with the parent's prompt.
- It is within the length for its level.
