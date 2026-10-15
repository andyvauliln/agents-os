# Rebuild the Agent OS repository: the top level

## Your task

You are an AI coding agent, such as Claude Code, in an empty git repository. Build the top level of the Agent OS repository so that it ends up the same as the repository it was written from: the same top folders and files, the same names and formats, the same keys folder without any key value, the same project docs and the same metadata files. Then build every level below it by following that level's own rebuild prompt, in the order under "Build order". "The same repository" means every check under "Acceptance checks" passes.

This prompt builds only the top level: the root files, `.gitignore`, `.secrets/`, `docs/`, and the top folders `agents/` and `apps/` with their own metadata files. It never builds the inside of a level; each level's prompt does that. The project's records (the owner's inputs word for word, the decisions, the changelog and the plans, in `apps/project-IDE/data/`) are not built from a spec: the project IDE's prompt copies them in as the owner hands them to you.

Never do any of these:

- Write a key value anywhere: in a file, a commit, a log, a prompt or a message. Key names only.
- Create a `.env` file with content, read one, or add one to git.
- Act in the outside world: publish the File Tree page, push, open or merge a pull request, without the owner's word. Commit only when the owner asks.
- Create any file inside `agents/trading/prediction-market/`: it is stage two, folders only.
- Install anything globally, or register a background service or a scheduled job.

How to work:

- Follow "Build order" step by step. Run each step's check and fix any failure before the next step.
- Build what this file states, including what is marked "default, the owner may change it".
- Where this file says a point is open, leave what it says in its place and list the point in your report. Never invent an answer.
- Where you must choose a detail this file does not settle, choose the simplest thing that passes the checks, write it down as "default, the owner may change it" in that item's How it works file, and report it.
- If the owner hands you material from the current repository (the records, the research studies, the page, the server), copy it in unchanged at the path this file or a lower prompt names, then check it.
- Call the owner "the owner", and "they" when a pronoun is needed.
- When you finish, report in short plain lines: what you built, every default you chose, every open point you left, and the result of every acceptance check.

## The project in brief

The Agent OS is the owner's personal system for running AI agents of any kind: agents that trade, that work on social media or that help with management. It runs many small agents side by side, each with one clear job, tries every idea safely in test mode first and keeps what works. Trading on prediction markets is its first area of work. Nothing of the system runs yet.

The owner builds it by vibecoding: they say what they want in plain words, and AI writes the plans, the docs and later the code. Every input is kept word for word, every change gets a plan the owner sees first, and the docs at every level are brought in line in a fixed order. The owner follows everything through the project IDE: the File Tree page, a clickable map of every file and folder with a plain How it works for each, on claude.ai and on the owner's server with Claude Code behind its request box.

The repository is described in levels: the project (the whole repository, in `docs/`), the system (`agents/system/docs/`), trading (`agents/trading/docs/`), the apps (`apps/docs/`) and each app, the project IDE first (`apps/project-IDE/docs/`). Each level has a vision, a README, the README again in ASD-STE100 Simplified Technical English, and a rebuild prompt. Every file and folder has metadata files beside it. Keys stay on the machine: only their names are in git.

The project is in stage one: finish the project IDE, make all metadata correct, and write the docs at the project, system, trading and apps levels. The prediction-market domain is stage two and exists only as folders.

## Ground rules

**Keys.** Every private key lives only in `.secrets/` at the repository root. `.secrets/test/.env` and `.secrets/live/.env` hold the values and never go into git; everything else in `.secrets/` does. Settings and docs name keys, never values. The File Tree page lists a `.env` file as local-only and never reads, shows or edits it.

**Formats.** Markdown for docs and notes, JSON for settings, indexes and Details files. UTF-8, LF line endings, no BOM. JSON pretty-printed with 2 spaces. Every JSON file you own starts with `"schema_version": 1`, except an empty `{}` placeholder and the tool files that have their own format.

**Names.** File and folder names are exact as written here, character for character. Names in `[brackets]` are placeholders and are created as written. In a name, `|` becomes `-`.

**Metadata files.** Every file and folder has metadata files beside it, named after the item without its extension:

- `x.index.md`: How it works, plain prose for people.
- `x.meta.json`: Details, the facts about the item.
- `x.example.md`: the item's outline; only for the main docs and the `.env` files for now.
- `x.questions.md`: open questions for the owner; only for the main docs and the `.env` files for now.

A file `vision.md` has `vision.index.md`; a file without an extension keeps its whole name (`.gitignore.index.md`); a folder `f/` keeps its own inside it (`f/f.index.md`, `f/f.meta.json`); the repository root, standing for `agent-os/`, has `agent-os.index.md` and `agent-os.meta.json`. When two names in a folder would be the same, or a file is named like its folder, the file keeps its extension (`server.py.index.md`). A metadata file has no metadata files of its own. The `.env` files' Example is `.env.example`, holding key names only.

**Docs for people.** The vision and the README of every level are plain, book-like prose: no reference numbers, no decision or input codes, no history. Paths are fine in a README.

**Git.** Everything that defines the project is committed. Keys files, dependencies, caches and editor state are not. A folder with nothing in it keeps a `.gitkeep`.

## The repository tree

The top level, as you build it. Lines marked "lower prompt" are built by that level's own prompt; lines marked "copied" are copied from what the owner hands you.

```text
agent-os/                          # the repository root (the GitHub repository is andyvauliln/trading-oss)
├── agent-os.index.md              # How it works of the whole repository
├── agent-os.meta.json             # Details of the whole repository
├── README.md                      # the front page; empty for now (open)
├── README.index.md
├── README.meta.json
├── HANDOFF.md                     # planning handoff; copied
├── HANDOFF.index.md
├── HANDOFF.meta.json
├── init.sh                        # sets up the owner's server once and starts the IDE; built by the project IDE prompt
├── init.index.md
├── init.meta.json
├── start.sh                       # starts or restarts the project IDE; built by the project IDE prompt
├── start.index.md
├── start.meta.json
├── .gitignore                     # exactly as under "The parts"
├── .gitignore.index.md
├── .gitignore.meta.json
├── .secrets/                      # keys; in git without the .env files
│   ├── .secrets.index.md
│   ├── .secrets.meta.json
│   ├── secrets.index.json         # key names and what uses them; never values
│   ├── secrets.index.index.md
│   ├── secrets.index.meta.json
│   ├── test/
│   │   ├── test.index.md
│   │   ├── test.meta.json
│   │   ├── .env                   # created empty only if missing; never in git, never read
│   │   ├── .env.example           # key names only, no values
│   │   ├── .env.index.md
│   │   ├── .env.meta.json
│   │   └── .env.questions.md
│   └── live/
│       ├── live.index.md
│       ├── live.meta.json
│       ├── .env                   # created empty only if missing; owner only; never in git
│       ├── .env.example
│       ├── .env.index.md
│       ├── .env.meta.json
│       └── .env.questions.md
├── docs/                          # the project docs
│   ├── docs.index.md
│   ├── docs.meta.json
│   ├── vision.md                  # + vision.index.md, vision.meta.json, vision.example.md, vision.questions.md
│   ├── README.md                  # + README.index.md, README.meta.json, README.example.md, README.questions.md
│   ├── README.asd.md              # + README.asd.index.md, README.asd.meta.json, README.asd.example.md, README.asd.questions.md
│   ├── rebuild-prompt.md          # this file; + rebuild-prompt.index.md, .meta.json, .example.md, .questions.md
│   ├── file-tree.md               # built; + file-tree.index.md, file-tree.meta.json
│   └── metadata.md                # the metadata logic in ASD-STE100; + metadata.index.md, metadata.meta.json
├── agents/
│   ├── agents.index.md
│   ├── agents.meta.json
│   ├── system/                    # lower prompt: agents/system/docs/rebuild-prompt.md
│   └── trading/                   # lower prompt: agents/trading/docs/rebuild-prompt.md
├── apps/
│   ├── apps.index.md
│   ├── apps.meta.json
│   ├── docs/                      # lower prompt: apps/docs/rebuild-prompt.md
│   ├── project-IDE/               # lower prompt: apps/project-IDE/docs/rebuild-prompt.md
│   ├── temp/                      # lower prompt: apps/docs/rebuild-prompt.md
│   └── trading-ui/                # lower prompt: apps/docs/rebuild-prompt.md
```

## Conventions

**Docs per level.** Every level's `docs/` folder holds `vision.md`, `README.md`, `README.asd.md` and `rebuild-prompt.md`, written in that order. The project level adds `file-tree.md` and `metadata.md`. Each doc has its How it works and Details files; the four written docs also have their Example and Questions files. Levels, with their docs folders:

| Level | Docs folder |
|---|---|
| Project | `docs/` |
| System | `agents/system/docs/` |
| Trading | `agents/trading/docs/` |
| Prediction-market domain (stage two) | `agents/trading/prediction-market/docs/` (folder only) |
| Apps | `apps/docs/` |
| Project IDE | `apps/project-IDE/docs/` |

**`README.asd.md`.** The README of its level again, with the same content and section order, in ASD-STE100: one topic per sentence; descriptive sentences at most 25 words, procedural sentences at most 20; active voice; present tense; approved simple words; one word for one meaning, the names exactly as in `README.md`; numbered steps for procedures; paragraphs of at most six sentences. Its first line says it is the ASD-STE100 version of `README.md` and that `README.md` is the source.

**How it works file.** Front matter, then one heading with the item's name, then six fixed headings, then "Keep in mind":

```markdown
---
about: agent-os/docs/vision.md
node: n-57.1
written: 2026-10-12T00:00:00Z
by: knowledge-base-agent
---
# vision.md

## What it is
## Who looks after it
## When and how it changes
## Who uses it, and when
## Where it is mentioned
## Related knowledge

## Keep in mind

- When you ..., ...
```

`about` is the path from `agent-os/`, which is also the item's id on the File Tree page. A file not yet moved to this format has one `## Summary` instead of the six headings. The build adds a `basis` line and may add `confirmed`; never write them by hand.

**Details file.** JSON with exactly these fields, filled where known and empty otherwise:

```json
{
  "schema_version": 1,
  "about": "What it is for, in one line.",
  "kind": "file",
  "state": "written",
  "status": "decided",
  "git": "tracked",
  "secret": false,
  "generated_by": null,
  "writers": ["the knowledge base agent (vision-doc skill)"],
  "readers": ["the owner", "every AI session"],
  "changes_when": "an input changes the project as a whole",
  "related": [{"path": "docs/README.md", "how": "follows it"}],
  "sources": {"decisions": [], "inputs": [], "notes": []},
  "update_with": [{"path": "docs/README.md", "how": "same words for the same things"}],
  "inherits": [],
  "features": [],
  "views": [],
  "how_it_works": {"written": "2026-10-12T00:00:00Z", "by": "knowledge-base-agent"}
}
```

`kind` is `file`, `folder`, `file link` or `folder link`; `state` is `written`, `not written yet`, `built` or `name pattern`; `status` is `decided`, `proposed` or `example`; `git` is `tracked` or `ignored`. An item with nothing known yet gets the same fields with empty values.

**Example file.** The doc's outline as a Markdown skeleton: its title, each heading in order, and one line under each saying what goes there.

**Questions file.** One short question per line item for the owner, each with a sentence on why it matters, or the line "None open."

## The parts

### Root files

- `README.md`: create it empty. What the front page says is open; do not write it.
- `HANDOFF.md`: copy it as the owner hands it to you. If you have none, do not create it.
- `init.sh` and `start.sh` (executable Bash): the set-up and start scripts of the project IDE on the owner's server. Their exact spec is in `apps/project-IDE/docs/rebuild-prompt.md`; write them when you follow that prompt. They are not `agents/system/init.sh` and `agents/system/start.sh`.
- `agent-os.index.md`: How it works of the whole repository in at most 200 words: what the Agent OS is, the top folders and what each holds, the stage, and up to four system-wide "Keep in mind" lines (key names only, never a value; the page tree equals the disk; decided only on the owner's word; plan every change).
- Every root file gets its How it works and Details files.

Check: `ls` at the root shows exactly the root entries of the tree above (plus `.git/`).

### .gitignore

Write it exactly:

```text
# Keys files never go in git: every .env (the keys folder .secrets/ itself and its notes do)
.env
.env.*
!.env.example
# How it works and Details files of a keys file hold no keys, so they stay in git
!.env.index.md
!.env.meta.json
!.env.questions.md

# Dependencies and build output
node_modules/
dist/
build/
.venv/
venv/

# Python
__pycache__/
*.py[cod]
*.egg-info/
.pytest_cache/
.mypy_cache/

# OS and editor
.DS_Store
*.swp
.idea/
.vscode/

# Cursor local state
.cursor/

# Research clones stay out of git
apps/temp/*/repo/

# Claude Code local state: one person's settings and one machine's memory stay out of git
# (the folder's How it works and Details files stay in git)
**/.claude/settings.local.json
**/.claude/agent-memory-local/*
!**/.claude/agent-memory-local/*.index.md
!**/.claude/agent-memory-local/*.meta.json
!**/.claude/agent-memory-local/.gitkeep

# Runtime logs and data: what agents and workers write at run time is not source;
# the folders, their How it works, Details and Questions files and .gitkeep stay in git
agents/**/logs/**
!agents/**/logs/**/
!agents/**/logs/**/.gitkeep
!agents/**/logs/**/*.index.md
!agents/**/logs/**/*.meta.json
!agents/**/logs/**/*.questions.md
agents/**/data/**
!agents/**/data/**/
!agents/**/data/**/.gitkeep
!agents/**/data/**/*.index.md
!agents/**/data/**/*.meta.json
!agents/**/data/**/*.questions.md

# The project IDE: each run's worktree, and the owner's notes waiting on the server page
# (a note's words are filed as an owner input by the run that takes it)
.worktrees/
apps/project-IDE/data/page-store/notes/
```

Every new ignore line gets a comment saying why.

Check: `git check-ignore .secrets/test/.env .secrets/live/.env` prints both paths; `git check-ignore .secrets/test/.env.index.md .secrets/test/.env.example .secrets/test/.env.questions.md` prints nothing.

### .secrets/

Create `.secrets/`, `.secrets/test/` and `.secrets/live/`. Set the folder to `chmod 700` and each `.env` file to `chmod 600` (default, the owner may change it).

- `.secrets/test/.env` and `.secrets/live/.env`: create each empty, only if it does not exist. Never read, overwrite or commit one. Only the owner puts values in them; only the owner ever touches `live/.env`.
- `.secrets/test/.env.example` and `.secrets/live/.env.example`: the key names, one `NAME=` per line under comment sections, with no values; the only line with a value is the mode, `AGENT_OS_ENV=test` in the test file and `AGENT_OS_ENV=live` in the live file, which is not a secret. Today the names include `AGENT_OS_ENV`, `ANTHROPIC_API_KEY` (Claude Code on the owner's server) and `GROQ_API_KEY` (voice input on the page), `OPENROUTER_API_KEY` and `NOTIFY_TELEGRAM_BOT_TOKEN`; take the full list from the owner's material or from the system's prompt.
- `.secrets/secrets.index.json`: `{}` until the first key is listed; then `"schema_version": 1` and, per key name, what kind it is, its mode and what uses it. Never a value.
- How it works, Details and Questions files as in the tree.

Check: `git ls-files .secrets` lists no file named `.env`; `grep '=.' .secrets/*/.env.example` prints only the two `AGENT_OS_ENV` lines.

### docs/

Write the project docs in this order, each with its own skill when the skills exist (`vision-doc`, `readme-doc`, `readme-asd-doc`, `rebuild-prompt-doc`):

1. `docs/vision.md`: what the Agent OS project is and why; the way of working (vibecoding, the project IDE as the owner's window); the concept (the system, the levels of docs, metadata next to everything, the way of working, the IDE, the records); a round of work as a story; the rules the project follows; examples; what the owner sees and does; the stages; principles; ideas still weighed; open questions; and last, the path `docs/README.md`. Plain prose, no paths except that one.
2. `docs/README.md`: every part of the repository exactly, with the path to each part's own docs: the front page and handoff, the project docs, agents, the system with `agents/system/CLAUDE.md`, trading, apps, the project IDE, keys, metadata files, the records; then how a round of work goes, the stages, a table of every part's docs, and what is still open.
3. `docs/README.asd.md`: `README.md` again in ASD-STE100, as under "Conventions".
4. `docs/rebuild-prompt.md`: this file.
5. Each doc's Example and Questions files.
6. `docs/metadata.md`: the full logic of the metadata files, in ASD-STE100, in twenty numbered sections: what metadata is; why the system needs it; the metadata files of an item; how the names are made; the How it works file; the Details file with every field; Example, Questions and the ASD-STE100 twin; when a file becomes stale; how the build finds stale files (the basis, confirm, the ripple, orphans); how to update metadata after a change; how the build uses it; how the page shows and changes it; who does what; the rules; status (decided, proposed, idea, open) and where it is written; owner inputs; decisions; questions; the true state of each Details field (who fills it, what reads it, how many files have it); what is not built yet. It must agree with the `file-index` skill.
7. `docs/file-tree.md`: never written by hand. The IDE build writes it every round: every path in the repository, one per line, in tree order, with nothing else on the line. Until the build exists, create it empty.

If the owner handed you the current docs, copy them in unchanged instead of writing them, then check them against this list.

Check: the five docs and their metadata files exist; `docs/README.asd.md` has the same `##` headings, in the same order, as `docs/README.md`.

### agents/ and apps/

Create `agents/` and `apps/`, each with its own How it works and Details files. `agents/agents.index.md` says that every child is a domain, the system is one, trading is a folder of domains, and every agent has the same standard folder. `apps/apps.index.md` says what apps are (our own, outside ones we fork, research clones in `temp/`) and names the project IDE. Everything inside them is built by the lower prompts.

Check: both folders and their two metadata files exist.

## Build order

1. Write the root files and `.gitignore`. Check: the root files and `.gitignore` checks.
2. Create `.secrets/` (never any key value). Check: the `.secrets/` checks.
3. Create `agents/` and `apps/` with their metadata files. Check: their check.
4. Write or copy `docs/` (step 7 of its list waits for the build). Check: the `docs/` check.
5. Follow the lower rebuild prompts, in this order, running each one's own checks:
   1. `agents/system/docs/rebuild-prompt.md`: the system agent, the shared parts, `agents/system/CLAUDE.md`, the helper agents and skills, the build scripts.
   2. `apps/docs/rebuild-prompt.md`: the apps folder, `apps/temp/`, `apps/trading-ui/`, and in its turn `apps/project-IDE/docs/rebuild-prompt.md`, the File Tree page, its server and its data.
   3. `agents/trading/docs/rebuild-prompt.md`: the folder of trading domains, its research studies, and the prediction-market domain as folders only (stage two).
   If a prompt in this list is still empty, create that level's folder with its four docs as empty files and their metadata files, report it, and go on.
6. Write every missing or stale How it works file with the `file-index` skill, children before their folders, until `build_map.py --stale` prints nothing.
7. Run the IDE build (`ide-build`), which also writes `docs/file-tree.md`. Check: the page check prints "page ok".
8. Run every acceptance check and report to the owner.

## Acceptance checks

1. The root holds exactly the entries of the tree above, and every file and folder has its `x.index.md` and `x.meta.json`.
2. No key value is in git: `git ls-files | grep -E '(^|/)\.env$'` prints nothing, and for every key name listed in `secrets.index.json` or an `.env.example`, `git grep -E "<NAME>=.+"` finds nothing.
3. Every JSON file you wrote parses (`python3 -m json.tool <file>`).
4. `docs/` holds the five docs with their metadata files, and `README.asd.md` follows `README.md` section by section.
5. Every lower prompt in the build order ran and its checks passed, or it was empty and is reported.
6. `agents/trading/prediction-market/` holds its folders, `.gitkeep` files and its own How it works and Details files, and its `docs/` the earlier trading notes kept for stage two with their metadata files; nothing else.
7. `build_map.py --stale` and `build_map.py --orphans` print nothing.
8. The page tree equals the disk: the paths the page lists are exactly `git ls-files --cached --others --exclude-standard`, plus the two local-only `.env` files.
9. `docs/file-tree.md` lists the same paths.
10. Nothing was pushed, published or merged without the owner's word.

## Do not build

Leave each as stated, and list it in your report.

- The front page text: `README.md` stays empty.
- A new name for the rebuild prompt (`reverse-prompt.md`): keep `rebuild-prompt.md`.
- A new name for the repository or its top folder: keep them.
- Extra information on each line of `docs/file-tree.md`: none.
- Example, Questions, Tests and changelog files for items other than the main docs and the `.env` files: none.
- Custom views (`x.{type}.{name}.view.html`): none from this prompt.
- Anything inside `agents/trading/prediction-market/` beyond its folders: nothing; it is stage two.
- The copy-trading domain and any other domain not in a lower prompt: nothing.
- Live keys, live actions and anything that acts in the outside world: nothing.
