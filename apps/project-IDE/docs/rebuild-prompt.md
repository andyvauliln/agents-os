# Rebuild the project IDE

## Your task

You are an AI coding agent, such as Claude Code, working in the Agent OS repository. Build the project IDE, `apps/project-IDE/`, so that it works exactly as described here: the File Tree page, its build, the way the owner's work comes back into the files, and the server that puts Claude Code behind the page. "The same IDE" means every acceptance check at the end passes.

Assume the levels above exist: the repository with `agents/system/` (the system's `CLAUDE.md`, the knowledge base agent with its `file-index` skill, the doc skills), the keys folder `.secrets/` with `test/` and `live/`, and `.gitignore`. Build only the IDE's own folder, its agent, its two skills and its build scripts. The IDE has no child levels with prompts of their own.

Never write a key value anywhere: key names only. Never push, publish or merge without the owner's go. Follow the build order and run each step's check before the next. Where this prompt says a point is open, build nothing for it and ask the owner.

When a reference copy of a file exists in the repository (`vision/explorer/file-tree-explorer.html`, `vision/tools/*`, `vision/server/*` while we plan), start from it and keep its behaviour; this prompt is the spec it must meet.

## The IDE in brief

The project IDE is the owner's window on the Agent OS. The owner builds the system by vibecoding, and the IDE shows the whole project as one clickable tree of every folder and file. For each item it shows what it is, how it works, its text, an example of its structure, its open questions and its details. The owner edits, comments, asks, adds and deletes on the page; the page saves all of it at once in its store; at a sync the project IDE agent writes it into the files and the knowledge base agent sorts it into the docs; then the page is rebuilt from the repository. The same tree gives every AI the full context of any file before it changes it.

The page runs in three places: on claude.ai as a published artifact with its own store; on the owner's server, where a small Python service keeps the store as files, writes edits straight into the files and runs each request as a Claude Code session; and anywhere else as view only. The tree on the page always equals the files in git.

## Ground rules

- **Safety.** No secret value in any file, the page data or a log. `.env` files are never read by the build, the page or the server. Nothing from the page touches `.secrets/` except listing its folders and notes. The server listens only on `127.0.0.1`. Push, history rewrites, deletes other than the item the owner deleted, installs, network tools and anything outside the repository wait for the owner's click.
- **Formats.** The page is one self-contained HTML file with inline CSS and JavaScript (fonts from Google Fonts only). Settings and data are JSON. Docs are Markdown. Build scripts are Python 3.10+ with the standard library only; the page check is Node with Playwright. The server is Python with the standard library plus `claude-agent-sdk`.
- **Generated files.** `file-tree.data.json` and `real-files.json` are built, never edited or merged by hand; after a merge, build again.
- **Metadata next to everything.** Every file and folder you create gets `x.index.md` (How it works) and `x.meta.json` (Details) next to it, named after the item without its extension; a folder keeps them inside it (`server/server.index.md`). A file whose name would clash with a sibling's or its folder's keeps its extension: `server/server.py.index.md`, `server/server.py.meta.json`.
- **Status.** Decided means the owner decided. Anything you add beyond this prompt is marked proposed in the tree notes.

## The repository tree

```text
apps/project-IDE/
├── project-IDE.index.md, project-IDE.meta.json
├── docs/
│   ├── vision.md                 what the IDE is for and why (people)
│   ├── README.md                 the full manual (people)
│   ├── README.asd.md             README.md in ASD-STE100
│   ├── rebuild-prompt.md         this file
│   └── [doc].example.md, [doc].questions.md for each doc; docs.index.md, docs.meta.json
├── current-ui/
│   ├── file-tree-explorer.html   the page
│   └── file-tree.data.json       the page data (built)
│   (real-files.json is built next to the data and published with it)
├── server/
│   ├── README.md                 setup, start, safety
│   ├── server.py                 web service
│   ├── claude_bridge.py          Claude Code sessions for page requests
│   ├── voice.py                  speech to text through Groq
│   └── server.config.json        settings
└── data/
    ├── README.md                 how the knowledge is kept
    ├── file-tree.md              the tree notes
    ├── inputs/                   [YYYY-MM-DD-HHMM-topic].md per owner input, README.md, index.json
    ├── decisions.md, changelog.md
    ├── knowledge-map.json        built by build_map.py
    ├── sources/[doc].md          notes behind each doc for people
    ├── page-store/               nodes/, changes/, inputs/ (server only; one JSON file per document)
    ├── overrides.json            the owner's page edits kept in the data, keyed by item number
    ├── memory/[note].md, plans/[plan].md, archive/[date]/
agents/system/.claude/
├── agents/project-ide-agent.md
└── skills/
    ├── ide-build/SKILL.md
    │   └── scripts/              README.md, parse.py, enrich.py, tabs.py, materialize.py,
    │                             index_files.py, build_map.py, check_page.js, overrides.json (until data/ is live)
    └── ide-sync/SKILL.md
```

While the project is planned, the working sources live in `vision/`: the page in `vision/explorer/` (with `file-tree.data.json` and `real-files.json`), the scripts in `vision/tools/`, the server in `vision/server/` (store `vision/page-store/`, logs `vision/logs/project-ide-agent/`), the tree notes and knowledge in `vision/docs/`, the agent and skills in `vision/.claude/`, and the How it works and Details sources in the mirror `vision/tree/agent-os/...`. Build in those places while `vision/` is the source, and let `materialize.py` copy them into the tree above.

## Conventions

- **Item ids.** An item from the tree notes is `n-<number>` (`n-53.4.2` for tree number `53.4.2`; the root is `n-0`). A real file found by the scan is `r-<path with other characters replaced by ->`. An item added on the page is `new-<8 random characters>`.
- **Family name.** A file's name without its last extension (`vision.md` → `vision`, `system.workers.json` → `system.workers`); a name with no extension stays whole (`.gitignore`); a folder's own name. Metadata files: `<family>.index.md`, `<family>.meta.json`, `<family>.example.md`, `<family>.questions.md`, `<family>.<type>[.<name>].view.html`.
- **Names on disk.** `|` in a planned name is written `-`; `, ` is written `+`.
- **How it works front matter:**

  ```markdown
  ---
  about: agent-os/apps/project-IDE/docs/README.md
  node: n-53.4.2
  basis: 1a2b3c4d5e6f
  written: 2026-10-12T00:00:00Z
  by: knowledge-base-agent
  confirmed: 2026-10-12T00:00:00Z
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

  `basis` is set by `build_map.py` only; `confirmed` is optional. Files not yet in the new format have one `## Summary` instead of the six headings.
- **Details schema** (`x.meta.json`), every key present, empty values allowed:

  ```json
  {"schema_version": 1, "about": "", "kind": "", "state": "", "status": "", "git": "", "secret": null,
   "generated_by": null, "writers": [], "readers": [], "changes_when": "", "related": [],
   "sources": {"decisions": [], "inputs": [], "notes": []}, "update_with": [], "inherits": [],
   "features": [], "views": [], "how_it_works": {}, "tree_number": ""}
  ```

  `related` and `update_with` hold `{"path": "...", "how": "..."}` objects.
- **Browser storage keys** (wrap every access in try/catch): `ftx-tab2`, `ftx-idx`, `ftx-planned`, `ftx-side`, `ftx-open`, `ftx-sel`, `ftx-ask-<id>`, `ftx-chat-<id>`, `ftx-mdmode`, `ftx-rtheme`, `ftx-rfont`, `ftx-rsize`, `ftx-applied`.

## The parts

### The page: `current-ui/file-tree-explorer.html`

One HTML file. On load it fetches `file-tree.data.json` (no cache), then decides its mode: if `window.claude.use` exists it is on claude.ai and asks for `sample`, `user`, `db` and `comments`; otherwise it fetches `api/health` and, if that answers `{ok: true}`, it is on the owner's server and uses a store shim over `api/store/*` that polls every 4 seconds; otherwise it shows "view only" in the header and disables every save. Colors are tokens on `:root` with a dark set under `prefers-color-scheme: dark` and `[data-theme]`.

Build these features:

1. **Header:** title "Agent OS File Tree"; a version line `<doc_version> · <n> objects` plus " · on your server" or " · view only"; the Apply changes button with a count, hidden when nothing is changed; the filter input. Filter rules: a bare or bracketed number filters by tree number (prefix match, exact with a closing bracket); text with `*` is a glob on the name; text with `/` matches the path; anything else matches part of the name and is highlighted. Folders on the way to a match open.
2. **Tree:** tabs All and Changed (with count); a "metadata" switch (default on) that shows each item's `.index.md` and `.meta.json` as rows (under a file, first inside a folder) and hides scanned metadata files when off; a "planned" switch (default off) that hides items not on disk (`exists` or `scanned` false), except local-only files. Rows show icon, name, a "changed" tag and `[number]`. A first click on a closed folder opens it. Arrow keys move, open and close. Deleted items stay struck through in their place until the sync. The selected item goes into the URL hash.
3. **Sheet:** breadcrumbs, number, name, Delete (not on the root), a "Changed · reason" chip, the kind, the purpose line, then the tabs.
4. **Tabs:** How it works first, Details last. Files: File, Example, Questions. Folders: Contents, Questions. Agent folders add Overview and Agents first; jobs files add Jobs; and the item's `custom_tabs` (Links, Variables, Tests, Capabilities) as editable tables.
5. **How it works:** reads `how_md`; shows the file name and Edit; six fixed headings and Keep in mind, or a Summary with the knowledge that applies directly and from above, the item's own notes and the inputs that shaped it; lists messages waiting for the sync and every page change with "Undo this change". Edit opens a Markdown editor (Ctrl+S saves).
6. **File:** the text with a path bar and source; numbered lines, a click on a number opens a line comment; 3,000 lines at a time with "Show more"; lazy texts loaded once from `real-files.json`; "Write it" and "Start from the example" for a file with no text; read-only items show why; Edit opens the editor with a gutter and wrapping lines (Ctrl+S). A Markdown file opens in the Read view: white or black paper (`ftx-rtheme`), an Aa menu (Sans, Legible, Serif; S, M, L), word count and reading time, a Contents list, Read and Source, full screen with a side contents column above 1120 px, a progress line and Esc to close. Every rendered block carries its source lines; a double-click, or two taps within 400 ms, replaces the block with a textarea of those lines; Save or Ctrl+Enter writes only them; Esc cancels.
7. **Contents:** cards for the children, "Add a file or folder" (name, type, purpose), "Comment on this folder".
8. **Example:** an outline (a doc's structure from its skill) or a code box plus a field table (Field, Values, Example, What it is for); jobs and links files build their example from their table.
9. **Questions:** open questions with Discuss, answered questions, and for a folder the open questions inside it.
10. **Details:** the item's `meta` as JSON with the file name.
11. **Notes:** comments `{id, line, snippet, text, at, by, resolved}` on a line or the whole item, re-anchored by snippet; Resolve, Reopen, Delete; resolved hidden by default.
12. **Ask box:** per-item chat kept in the browser (last 30 messages); Enter sends, Shift+Enter breaks; Clear, Stop. Every message is first saved as an `inputs` document with status `new`. On claude.ai: model tiers Most capable (`complex`), Balanced (`default`), Fastest (`quick`); `sample.json` with tools returns `{kind: answer|draft|save|discard, reply, title, changes, qa}`; a draft card lists each changed item and field with a before/after diff, Save (or the word "save") applies it, Discard drops it; an answered question is saved to the item's `qa`. After every save, a "related updates" pass asks Claude for consistent changes to the parents and items that mention the saved ones, never changing another file's `content` or any `how_md`, saved as one undoable change. On the server: `POST api/agent`, then the SSE stream; show steps, an Allow/Refuse box, cost, seconds and changed-file count; keep the session id for follow-ups; reload the data when files changed; mark every touched item `worked`. A microphone button (server only, when voice is available) records up to 300 seconds with a timer and posts to `api/voice`; the text is appended to the box.
13. **Delete and restore:** the delete form with an optional note and "Delete and clean up". On the server it saves the deletion with `cleanup: "claude-code"` and sends `Delete the file|folder <path> and clean the project of it.` plus `Keep in mind: <note>` with `delete: <path>`; on claude.ai it saves `cleanup: "sync"` and an input of kind `delete`. "Bring it back" on the server sends a restore request; on claude.ai "Restore it" clears the flag.
14. **Changed and Apply changes:** one status, changed, with reasons new, edited, removed, commented, asked, worked. Apply changes opens a confirmation; on claude.ai it calls `comments.canSendToClaude()`, posts `comments.sendToClaude({anchor, text})` and saves an `inputs` document of kind `apply` with `count`, `items`, `sent_to_claude` and `thread` or `not_sent`; when that input turns `processed` it loads the new data (higher `data_version`) or offers Reload. On the server it selects the root and runs one Claude Code request starting "Sync the file tree:". A waiting request can be cancelled on claude.ai.
15. **Phone:** below 760 px one pane at a time with a "‹ Tree" back button; nothing wider than the viewport.

Store writes: `nodes/<id>` holds `{fields, comments, qa, new_node, deleted, was, delete_note, cleanup, worked, updated_at, by}`; every save also adds a `changes` document `{at, by, title, instruction, kind: edit|qa|ripple|delete, items: [{node_id, path, kind: set|remove|new|restore|qa, fields: {k: {before, after}}}], undone}`. Editable fields: `name, summary, purpose, link_target, details, writers_readers, updated_when, open_questions, example, fields, custom_tabs, content, how_md`.

Check: `check_page.js` prints "page ok".

### The page data: `current-ui/file-tree.data.json` and `real-files.json`

Top level: `schema_version`, `title`, `source {doc, doc_version, also}`, `generated`, `data_version` (integer, one more each build), `sync`, `status_legend`, `root` (`n-0`), `concepts`, `knowledge {id: {heading, doc, status, applies, nodes, text, sources}}`, `inputs {id: {at, where, summary, file}}`, `docs`, `decisions`, `feature_areas`, `retired`, `nodes`. Each node: `id, num, name, path` (starting `agent-os/`), `type` (file|folder), `parent, children, link, link_target, placeholder, exists, scanned, local_only, status, purpose, summary, details, rules, concepts, decisions, features, open_questions, qa, example {title, lang, body, note, kind, skill}, fields [{key, values, example, meaning}], custom_tabs, how {text, sections, keep, at, state}, how_md, how_file, meta, meta_file, fam, content, content_lazy, content_source, content_self, src_file, real_file, readonly, knowledge {direct, inherited}`. `real-files.json` maps scanned node ids to their text; files over 200,000 bytes get `content: null` and a note instead.

Check: the data parses; every `children` id exists; no node's `content` contains a value from a `.env` file.

### The build: `ide-build` and its scripts

`SKILL.md` gives the inputs table, the scripts table, the steps, the rules and the checks below. The scripts:

- `parse.py <out.json>`: reads the tree notes (`file-tree.md`: the numbered tree in a code block and one `### [n]` section per item), `feature-map.md` and `decisions.md`; writes the item list.
- `enrich.py <parsed.json> <out data>` with `DATA_VERSION=<n>` and `REPO_DIR=<repo>`: adds drafts (`DRAFTS` from `index_files.py`, other planning files shown on the File tab), doc outlines from each doc's skill (`DOC_SKILLS`: the first `markdown` block under `## Outline` becomes an outline example), concepts and rules, How it works and Details through `index_files.py`, the knowledge map through `build_map.build()`, the tabs from `tabs.py`; lists every real file under each existing folder that `git ls-files --cached --others --exclude-standard` returns, skipping `.git`, `__pycache__`, `node_modules`, `.DS_Store`, never reading `.env`; writes `real-files.json`; applies `overrides.json` last.
- `tabs.py`: field guides; the Variables table for each `.env` (names and purposes, fake example values only); Jobs, Links, Tests and Capabilities tables.
- `materialize.py <data>` with `REPO_DIR`: creates every planned item on disk (draft text, else empty, `{}` for `.json`), `.gitkeep` in empty folders, placeholder names as written, each item's `.index.md` and `.meta.json` next to it, empty metadata for every other file and folder outside `vision/` that has none; creates `.secrets/test/`, `.secrets/live/` and their notes; creates an empty `.env` only when missing and never reads or overwrites one; creates only folders under the prediction-market domain.
- `index_files.py`: `index_path(node)`, `meta_path(node)`, `ensure_meta(nodes)`, `load_all()`, `save()`, `orphans()`; `DRAFTS` and `DRAFT_DIRS`.
- `build_map.py`: default run rebuilds `knowledge-map.json` and prints problems; `--stale`, `--context <node>`, `--set <file.json>` (`{id: {text, sections: [{title, text}], keep: [...]}}`, writer from `BY`), `--confirm <id>...`, `--orphans`.
- `check_page.js <page dir> <shots dir|-> <ids...>`: loads the page in Chromium at 1400×900 and 390×844 with an in-memory stand-in for `window.claude` (`db`, `sample`, `user`), opens each id by its URL hash, clicks How it works and File, fails on a page error, a missing id, no tabs rendered, or (at phone width) a document wider than the viewport; saves a screenshot per width and id when given a folder; prints "page ok" or the number of problems and exits non-zero. `PLAYWRIGHT` and `CHROMIUM` override module and browser paths.

Steps, in a scratch folder `T` with `N` = current `data_version` + 1:

```bash
python3 parse.py $T/parsed.json
DATA_VERSION=N REPO_DIR=<repo> python3 enrich.py $T/parsed.json <data path>
REPO_DIR=<repo> python3 materialize.py <data path>     # rerun enrich if it created files
cp <data path> <page dir>/file-tree.data.json
python3 build_map.py                                    # until "fresh, 0 missing or stale, 0 orphans"
node check_page.js <page dir> $T/shots n-0 n-53.4.2 <changed ids>
```

Publish the page by its link, https://claude.ai/artifact/72v2Uppt6jpfXLCjKNX9xs, with `files` mapping `file-tree.data.json` and `real-files.json`, and the capabilities `db`, `sample`, `user` and `comments` (restate all four on every publish that passes capabilities).

Check: the build ends with "page ok", no stale or orphaned How it works file, and the tree check below.

### The sync: `ide-sync`

`SKILL.md` describes the three collections (`inputs`, `nodes`, `changes`) as in the page part, where they are read (the artifact data tool on the page link; on the server `page-store/<collection>/<id>.json`), and these steps: list new inputs and touched nodes; save each as an owner input word for word with its answer; write `content` into the file (or `overrides.json` for a file not written yet), `how_md` into the `.index.md` word for word with `by: owner` then `build_map.py --confirm <id>`, new items into the tree notes as proposed, other fields into `overrides.json`, open comments into open questions unless they ask for a change; run the page requests; hand the inputs to the knowledge base agent; run `ide-build`; mark inputs processed (`processed_at`, `processed_into`) and delete folded `nodes` documents, leaving `changes`; for an Apply changes round mark the `apply` input processed last, then answer and resolve the page comment; report in two to five lines. Its "Deleting an item" section: read the note; delete the item and its metadata files; remove its tree line and section (retire its number), links, mentions, the parent's How it works entry and knowledge map entries; file it with a changelog line; rebuild; commit. Bring back is the reverse from git.

Check: after a sync, no `inputs` document is `new`, and every edit is in its file.

### The server: `server/`

- `server.config.json` keys: `repo` (the repository top relative to the server folder: `../..` from `vision/server/`, `../../..` from `apps/project-IDE/server/`), `host` `127.0.0.1`, `port` `8765`, `page_dir`, `page`, `data`, `store_dir`, `write_through` `true`, `log_dir`, `planning_dir` (`vision` while we plan, removed after), `secrets {file: ".secrets/test/.env", keys: ["ANTHROPIC_API_KEY", "GROQ_API_KEY"]}`, `voice {url: "https://api.groq.com/openai/v1/audio/transcriptions", models: ["whisper-large-v3-turbo", "whisper-large-v3"], key: "GROQ_API_KEY", max_seconds: 300, language: null}`, `claude {cwd, model: null, max_turns: 80, max_budget_usd: 3, approval_timeout_s: 900, allow: [...], ask_owner: ["git push", "git reset", "git rebase", "git checkout --", "git clean", "rm ", "rmdir ", "chmod ", "chown ", "sudo ", "curl ", "wget ", "pip install", "npm install", "kill "], never: [".secrets"]}`. `allow` lists Read, Glob, Grep, LS, Edit, Write, MultiEdit, NotebookEdit, TodoWrite, Task, Agent, Skill, WebSearch, WebFetch and `Bash(...)` for cd, python3, node, ls, cat, head, tail, wc, grep, rg, find, mkdir, cp, mv, jq, diff, git status, ls-files, grep, diff, log, show, add, commit, pull, fetch, merge. `claude.cwd` is `vision` while we plan and `agents/system` after. These limits are defaults the owner may change.
- `server.py` (standard library `ThreadingHTTPServer`): exits if `host` is not local; rejects any request whose Host or Origin is not `127.0.0.1`, `localhost` or `::1`. Routes: `GET /` redirects to the page; `GET /<page>`, `/<data>`; `GET /real-files.json` reads scanned files fresh from disk (never under `never` paths); `GET /api/health` → `{ok, server: "project-ide", agent, agent_error, repo, claude_cwd, write_through, voice, voice_max_seconds}`; `GET /api/store/<coll>` → `{docs: [{id, data}]}`; `POST /api/store/<coll>` → `{id}`; `PUT|PATCH /api/store/<coll>/<id>` → `{ok, written}`; `POST /api/agent` `{text, node_id, path, name, num, session, input_id, kind, delete}` → `{run}`; `GET /api/agent/<run>/events` (SSE, `id:` per event, resumable); `POST /api/agent/<run>/answer` `{id, allow}`; `POST /api/agent/<run>/stop`; `POST /api/voice` (raw audio, 25 MB at most) → `{text, model}`. Collections are only `nodes`, `changes`, `inputs`; ids match `^[A-Za-z0-9_.:@+~-]{1,200}$`; files are written atomically. Write-through on `nodes` saves: `content` into the item's `src_file` (and `real_file`), never a text containing "…(cut for the page", never a field equal to the previous save; `how_md` into the item's How it works file with front matter kept and `written` now, `by: owner`, plus its copy next to the item on disk. Secrets are read from the keys file by name only; the Groq key is not passed to Claude Code.
- `claude_bridge.py`: one run per request, id `YYYYMMDD-HHMMSS-<6 hex>`, in a thread; `ClaudeSDKClient` with `cwd` from the config, `add_dirs` the repository, `setting_sources ["project", "local"]`, all skills, the `claude_code` system prompt with an appended note (work for the owner through the page; follow the system's `CLAUDE.md`, file the request, finish the round, never push, never open the keys folder; answer plainly), `allowed_tools` from `allow`, a `PreToolUse` hook and `can_use_tool` both using one check: deny anything naming a `never` path; allow exactly `git rm -r -q --ignore-unmatch <item and its metadata files>` and `rm -rf <same>` for a page deletion; ask for paths outside the repository and commands containing an `ask_owner` word. Asking emits `approval {id, tool, summary, reason}` and waits up to `approval_timeout_s`, then `answered`. Events: `start`, `text`, `tool {tool, summary}`, `approval`, `answered`, `result {text, cost_usd, duration_ms, turns, session, is_error, subtype}`, `error`, `end {changed, seconds}`. `changed` comes from git: files that differ from HEAD at the start or changed during the run, committed or not, never under `never`. Each run is logged as `<log_dir>/<YYYYMMDD>/<run>.json` with node, request, result, changed, steps and the owner's answers. The prompt names the item and, when given, the input file in the page store to mark processed.
- `voice.py`: posts multipart audio to the configured URL with the key as a bearer token; tries the models in order; a 429 parks a model for its `retry-after` (5 to 3,600 seconds); an error moves on; keeps nothing.
- `README.md`: what you need, how to start (`python3 <server path>/server.py` from the repository top), the SSH tunnel, what happens for each page action, the settings table, the files.

Check: start the server, open `http://127.0.0.1:8765/`; the header says "on your server"; a comment creates `page-store/nodes/<id>.json`; a File edit changes the file on disk; a request lists the system's agents; a `git push` waits for Allow.

### The agent: `agents/system/.claude/agents/project-ide-agent.md`

Front matter: `name: project-ide-agent`, a description, `tools: Read, Write, Edit, Bash, Grep, Glob`, `model: opus`, `memory: project`, `skills: ide-build, ide-sync, file-index`. Body: its job (build, bring back, run page requests, delete cleanly); how it works with the knowledge base agent (it saves inputs and edits, the knowledge base agent sorts them; files and notes win over the page); where things are; when it runs (sync or Apply changes, after a round that changed the tree or a doc, a waiting request, after a pull, as the server's session); the steps each time (pull, sync, build, publish, report, commit); the rules (never lose the owner's words, never edit the data by hand, decided means the owner decided, no secret values, ask before anything hard to undo, never push from the server).

Check: the file parses as an agent definition and names both skills.

### The docs: `docs/`

`vision.md`, `README.md`, `README.asd.md` and `rebuild-prompt.md`, written by the knowledge base agent with the `vision-doc`, `readme-doc`, `readme-asd-doc` and `rebuild-prompt-doc` skills, in that order, each with its `.index.md`, `.meta.json`, `.example.md` and `.questions.md`.

## Build order

1. Create the folders in the tree with their `.index.md` and `.meta.json`. Check: every folder has both.
2. Write `index_files.py`, `parse.py`, `tabs.py`, `build_map.py`, `enrich.py`, `materialize.py`. Check: parse and enrich run on the current tree notes without an error.
3. Write the page. Check: it loads the data in a browser in view-only mode.
4. Write `check_page.js`. Check: "page ok" on `n-0` and `n-53.4.2`.
5. Run the full build and fix every stale or orphaned How it works file through `file-index`. Check: "fresh, 0 missing or stale, 0 orphans".
6. Write `ide-build`, `ide-sync` and the agent. Check: a test sync on a stand-in store folds one comment and one edit.
7. Write the server files and their README. Check: the server checks above.
8. Write the four docs. Check: they agree with each other and with this prompt.
9. Publish the page at its link (only with the owner's go). Check: the acceptance checks.

## Acceptance checks

- `check_page.js` prints "page ok" for `n-0`, `n-53.4.2` and every changed item.
- `build_map.py` reports every How it works file fresh, none missing, no orphans.
- The tree equals git: the set of on-disk item paths in the data (`exists` or `scanned`, without `agent-os/`) equals `git ls-files --cached --others --exclude-standard` (folders included as prefixes), plus only the two local `.env` files.
- Every file and folder under `apps/project-IDE/` has its `.index.md` and `.meta.json`, and every `.meta.json` has every schema key.
- `grep` finds no key value from `.secrets/*/.env` in the data, `real-files.json`, the store or the logs.
- The server refuses a non-local host and any request with a foreign Origin.
- A page deletion on the server removes exactly the item and its metadata files without a click, and any other `rm` waits for one.
- An Apply changes round ends with its `apply` input processed and the page showing the new data version.

## Do not build

- Custom views (`<family>.<type>.<name>.view.html` and shared views): designed but not built; leave the page's current extra tabs in place. Where shared views live is open.
- Tabs read from real files (Example from `x.example.md`, Questions from `x.questions.md`, an ASD-STE100 tab from `README.asd.md`, shown only when the file exists): stage one work, not built yet; keep today's tabs until it is done.
- Filled Details files everywhere: leave empty templates where nothing is known.
- A scheduled routine that syncs the page store without Apply changes: a proposal, not built.
- Updating the published claude.ai page after work on the server: open.
- Statuses other than "changed": not built until the owner asks.
- Any file under the prediction-market domain other than its folders: stage two.
