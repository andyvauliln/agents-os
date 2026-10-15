# Rebuild apps/

## Your task

You are an AI coding agent, such as Claude Code, working in the Agent OS repository. Build the `apps/` folder so that it ends up as designed today: the same folders and file names, the same docs and metadata files, the same rules for outside code, and every app built by its own rebuild prompt.

This prompt builds only `apps/` itself: its own folders, its docs and their metadata. It assumes the levels above exist: the repository root (`.gitignore`, `README.md`, `.secrets/`) and the system domain `agents/system/`, including `agents/system/.claude/` with the knowledge base agent, the project IDE agent and the skills `vision-doc`, `readme-doc`, `rebuild-prompt-doc`, `file-index`, `ide-build`, `ide-sync` and `change-plan`. Those are built by `agents/system/docs/rebuild-prompt.md`, which calls this prompt in its build order. Each app is built by its own prompt, listed under "Build order".

Never do these things: write a key value anywhere (key names only); set anything live; commit a research clone; push, publish or merge into `main` without the owner's go. Follow the build order, run each step's check before the next one, and ask the owner wherever this prompt says a point is open.

## Apps in brief

Apps are the programs that sit next to the agents and help people and agents work with the system. There are three kinds:

- **Our own apps**, written for the project. The first is the project IDE, the owner's window on the project: the File Tree page, its server and the project's knowledge. The prediction-market domain's dashboard is kept as an empty folder for stage two and may never be needed.
- **Research clones**: outside repositories copied only to study them, kept out of git and deleted when the study is done; findings go to the studying agent's research folder.
- **Apps we use**: outside programs forked on GitHub. In the fork, `main` holds our changes and is what runs; `upstream` follows the source and is never changed by us; updates come in through `upstream` into `main`.

Every app explains itself with its own `docs/`: `vision.md`, `README.md`, `README.asd.md` and `rebuild-prompt.md`. For an outside app these docs are its only metadata for now.

## Ground rules

- **Safety.** No key value in any file of `apps/`. An app that needs a key names it and loads the value from `.secrets/` on the machine at run time. Nothing an app does may act live without the owner's approval.
- **Formats.** Docs in Markdown; metadata in Markdown (`x.index.md`, `x.example.md`, `x.questions.md`) and JSON (`x.meta.json`, starting with `"schema_version": 1`).
- **Metadata next to every item.** Every folder of `apps/` and every file and folder of our own apps has a How it works file and a Details file next to it: a file `vision.md` has `vision.index.md` and `vision.meta.json`; a folder `f/` has `f/f.index.md` and `f/f.meta.json`; `README.asd.md` has `README.asd.index.md` and `README.asd.meta.json`. An index or Details file has none of its own. The four docs in `apps/docs/` also have `x.example.md` (the doc's outline: headings, one line each on what goes there) and `x.questions.md` (open questions for the owner, or "None open.").
- **Outside apps are the exception.** Their `docs/` is all their metadata; never write metadata for files inside an outside app's `repo/`.
- **Git.** `apps/temp/*/repo/` is never committed.
- **Docs for people.** `vision.md` and `README.md` are plain prose with no reference numbers, decision codes or history; `README.asd.md` is the README in ASD-STE100 Simplified Technical English; `rebuild-prompt.md` is for AI.

## The repository tree

```
apps/
├── apps.index.md                      # How it works of apps/
├── apps.meta.json                     # Details of apps/
├── docs/                              # the docs for all apps
│   ├── docs.index.md                  # How it works of docs/
│   ├── docs.meta.json                 # Details of docs/
│   ├── vision.md                      # why the system has apps and what each kind is for
│   ├── vision.index.md / vision.meta.json / vision.example.md / vision.questions.md
│   ├── README.md                      # every app exactly and the path to its own docs; the list of apps
│   ├── README.index.md / README.meta.json / README.example.md / README.questions.md
│   ├── README.asd.md                  # README.md again in ASD-STE100
│   ├── README.asd.index.md / README.asd.meta.json / README.asd.example.md / README.asd.questions.md
│   ├── rebuild-prompt.md              # this file
│   └── rebuild-prompt.index.md / rebuild-prompt.meta.json / rebuild-prompt.example.md / rebuild-prompt.questions.md
├── project-IDE/                       # the owner's IDE; built by apps/project-IDE/docs/rebuild-prompt.md
│   ├── project-IDE.index.md
│   ├── project-IDE.meta.json
│   ├── docs/                          # vision.md, README.md, README.asd.md, rebuild-prompt.md
│   ├── current-ui/                    # file-tree-explorer.html, file-tree.data.json, real-files.json
│   ├── server/                        # README.md, server.py, claude_bridge.py, notes.py, runs.py, run_summary.py, worktrees.py, voice.py, server.config.json
│   └── data/                          # README.md, decisions.md, changelog.md, inputs/, plans/, archive/,
│                                      # overrides.json, page-store/
├── temp/                              # research clones
│   ├── temp.index.md
│   ├── temp.meta.json
│   └── [name]/                        # example pattern, not created now: one folder per clone
│       ├── repo/                      # the clone; ignored by git
│       └── docs/                      # vision.md, README.md, rebuild-prompt.md; only when the owner asks
└── trading-ui/                        # the prediction-market domain's dashboard: empty, stage two
    ├── trading-ui.index.md
    └── trading-ui.meta.json
```

An adopted outside app gets `apps/[name]/` with `docs/` (`vision.md`, `README.md`, `README.asd.md`, `rebuild-prompt.md`) and `repo/` (the fork). None exists now; create none.

## Conventions

- **App folder names:** our own apps keep the names above exactly (`project-IDE`, `trading-ui`); an outside app or clone uses the source repository's name, lowercase, as `[name]`.
- **How it works file format:**

  ```markdown
  ---
  about: agent-os/apps/docs/README.md
  node: n-43.1.2
  written: 2026-10-12T00:00:00Z
  by: knowledge-base-agent
  ---
  # README.md

  ## What it is
  ## Who looks after it
  ## When and how it changes
  ## Who uses it, and when
  ## Where it is mentioned
  ## Related knowledge

  ## Keep in mind

  - When you ..., ...
  ```

  `about` is `agent-os/` plus the item's path (a folder ends with `/`); `node` is the item's id on the File Tree page: `n-43` for `apps/`, `n-43.1` for `apps/docs/`, `n-43.1.1` to `n-43.1.4` for `vision.md`, `README.md`, `README.asd.md`, `rebuild-prompt.md`, `n-53` for `project-IDE/`, `n-55` for `temp/`, `n-45` for `trading-ui/`. A file not yet moved to the six headings has one `## Summary` instead.
- **Details file keys, in this order:** `schema_version`, `about`, `kind`, `state`, `status`, `git`, `secret`, `generated_by`, `writers`, `readers`, `changes_when`, `related` (list of `{"path", "how"}`), `sources` (`{"decisions": [], "inputs": [], "notes": []}`), `update_with` (list of `{"path", "how"}`), `inherits`, `features`, `views`, `how_it_works`. Example for `apps/temp/`:

  ```json
  {
    "schema_version": 1,
    "about": "Repositories cloned from GitHub only to study them; each clone is never committed and is deleted after the study.",
    "kind": "folder",
    "state": "written",
    "status": "decided",
    "git": "tracked; apps/temp/*/repo/ ignored",
    "secret": false,
    "generated_by": null,
    "writers": ["the agent or session doing the research"],
    "readers": ["the agent or session doing the research"],
    "changes_when": "a repository is cloned for research, or a clone is deleted",
    "related": [{"path": ".gitignore", "how": "ignores apps/temp/*/repo/"}],
    "sources": {"decisions": ["D-055"], "inputs": ["in-20261006-2206"], "notes": ["conv-apps"]},
    "update_with": [{"path": "apps/docs/README.md", "how": "a clone gets a row in the list of apps, removed when it is deleted"}],
    "inherits": ["conv-apps"],
    "features": [],
    "views": [],
    "how_it_works": {"written": "2026-10-12T00:00:00Z", "by": "knowledge-base-agent"}
  }
  ```

- **Fork branches:** `main` (ours, what runs) and `upstream` (follows the source's default branch, never changed by us).
- **List of apps row:** name, kind (`ours`, `fork`, `research`), source, fork and branches, commit in use, last update from the source, used by.

## The parts

### 1. The apps folder

Create `apps/` with `apps.index.md` (How it works: what apps are, the three kinds, the apps today, and these Keep in mind lines: clone for study only into `temp/` and never commit it; fork an app we use and change only `main`; when an app is added, updated or removed, update its docs and its row in the list of apps in the same change) and `apps.meta.json`.
Check: both files exist; the JSON parses.

### 2. The apps docs

Create `apps/docs/` with the four docs, written with the skills in `agents/system/.claude/skills/`, in this order:

1. `vision.md` with `vision-doc`, its app outline: in short; what apps are for and who uses them; why the system has apps (the three kinds); how apps should work for us; the apps today; where we stand and what comes next; ideas we are still weighing; open questions; going deeper (naming `apps/docs/README.md`). 300 to 1,000 words. No paths except in "Going deeper".
2. `README.md` with `readme-doc`: in short (pointing to `apps/docs/vision.md`); the apps at a glance (table and picture); how the folder is laid out; the parts (the apps docs, the project IDE, the prediction-market dashboard, research clones, apps we use from outside, the list of apps), each ending with "Its docs: `path`"; what apps take from and give to the system; where each part's docs are; still open in the design. 500 to 2,000 words. The list of apps is a table in this README (default, the owner may change it).
3. `README.asd.md`: the same content and section order as `README.md` in ASD-STE100 (descriptive sentences at most 25 words, procedural at most 20, active voice, present tense, one word for one meaning, numbered steps for procedures, paragraphs of at most 6 sentences). Its first line says it is the ASD-STE100 version and that `README.md` is the source.
4. `rebuild-prompt.md` with `rebuild-prompt-doc`: this file.

Then write each doc's `x.index.md`, `x.meta.json`, `x.example.md` and `x.questions.md`, and the folder's `docs.index.md` and `docs.meta.json` (no Example or Questions file for the folder). Write the How it works files with the `file-index` skill.
Check: the 4 docs and 18 metadata files exist; every `.meta.json` parses and has all 19 keys; no doc holds a key value; the vision and README name no decision codes or `[n]` numbers.

### 3. Research clones

Create `apps/temp/` with `temp.index.md` and `temp.meta.json` only. Make sure `.gitignore` holds these two lines, and add them if it does not:

```text
# Research clones are studied and deleted, never committed
apps/temp/*/repo/
```

Create no clone. When a clone is asked for later: `git clone <source> apps/temp/<name>/repo`, write findings in the studying agent's own research folder, write `apps/temp/<name>/docs/` only if the owner asks, add a `research` row to the list of apps, and delete the folder when the study is done.
Check: `git check-ignore apps/temp/x/repo/file` prints the path; `git ls-files apps/temp` lists only the two metadata files.

### 4. The prediction-market dashboard

Create `apps/trading-ui/` with `trading-ui.index.md` (the domain's dashboard, a Next.js API and web app, empty, stage two, maybe never needed; open: files or an API layer, how it is reached) and `trading-ui.meta.json` only. Build nothing else: it belongs to stage two and is listed under "Do not build".
Check: `apps/trading-ui/` holds only those two files.

### 5. The project IDE

Build it with its own prompt (see "Build order"). This prompt does not describe its files.
Check: the IDE prompt's own checks pass, and the page check prints "page ok".

### 6. Apps we use from outside

Create none now. When the owner decides to adopt one, follow these steps:

1. Fork the source on GitHub (where forks live is open; ask the owner).
2. In the fork, create `upstream` from the source's default branch, and keep `main` for our changes.
3. Add the fork as `apps/<name>/repo/` (as a git submodule: default, the owner may change it): `git submodule add <fork-url> apps/<name>/repo`.
4. Write `apps/<name>/docs/vision.md`, `README.md`, `README.asd.md`, `rebuild-prompt.md` with the doc skills' app outline. The rebuild prompt gives the source, how to fork it, the commit to start from, every change we made and how to set it up, run and test it.
5. Add a `fork` row to the list of apps in `apps/docs/README.md` and bring `apps/docs/` in line.

To update an adopted app: fetch the source; fast-forward `upstream` to it; merge `upstream` into `main`; run the app's tests; update the submodule commit, the app's docs and its row in the list of apps.
Check (when one exists): `apps/<name>/` has `docs/` and `repo/`; `repo/` is on `main`; the app has a row in the list.

## Build order

1. Check that the levels above exist: `.gitignore`, `agents/system/.claude/agents/knowledge-base-agent.md`, `agents/system/.claude/agents/project-ide-agent.md` and the skills named in "Your task". Check: every path exists; if one is missing, stop and build it with `agents/system/docs/rebuild-prompt.md` first.
2. Part 1, the apps folder. Check: part 1 check.
3. Part 3, research clones, and the ignore lines. Check: part 3 check.
4. Part 4, the dashboard folder. Check: part 4 check.
5. Part 5: follow `apps/project-IDE/docs/rebuild-prompt.md`. If that file is empty or exists only as its How it works file, build the IDE from the parts of `agents/system/docs/rebuild-prompt.md` that build the page, its build scripts and the server, and report this to the owner. Check: part 5 check.
6. Part 2, the apps docs, last of the apps folder, so they describe what was built. Check: part 2 check.
7. Part 6 only if the owner handed you an outside app to adopt.
8. Run the acceptance checks and report to the owner.

## Acceptance checks

1. `apps/` holds exactly `apps.index.md`, `apps.meta.json`, `docs/`, `project-IDE/`, `temp/`, `trading-ui/` and, only when the owner asked, adopted apps `apps/<name>/`.
2. `apps/docs/` holds the 4 docs, their 16 metadata files, `docs.index.md` and `docs.meta.json`.
3. Every `.meta.json` under `apps/` outside an outside app's `repo/` parses, starts with `"schema_version": 1` and has all 19 keys.
4. Every folder of `apps/` and every file and folder of `project-IDE/` has its `x.index.md` and `x.meta.json`; `python3 agents/system/.claude/skills/ide-build/scripts/build_map.py --stale` prints nothing for `apps/`.
5. `git ls-files apps/temp` lists only `temp.index.md` and `temp.meta.json`, and `.gitignore` ignores `apps/temp/*/repo/`.
6. `apps/trading-ui/` holds only its two metadata files.
7. No file under `apps/` holds a key value: a search for the key names in `.secrets/` finds names only, never values.
8. Every path in a "Its docs" line of `apps/docs/README.md` exists, except `apps/<name>/docs/README.md` for apps not yet adopted.
9. The IDE's own checks pass and the File Tree page builds: "page ok".

## Do not build

- The prediction-market dashboard's code: `apps/trading-ui/` stays empty (stage two; maybe never needed).
- The dashboard's own `docs/`: nothing until its design starts.
- Any research clone or adopted app: nothing until the owner asks.
- The earlier Polymarket tools as a fork: nothing; open.
- A scheduled check for source updates: nothing; updates run on request.
- The `adopt-app` skill: nothing until the owner asks.
- Shared views in `apps/project-IDE/views/` with `views.json`: leave to the IDE's own prompt; proposed.
- A separate file for the list of apps: none; the table in `apps/docs/README.md`.
