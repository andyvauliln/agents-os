# Rebuild the project IDE

## Your task

You are an AI coding agent, such as Claude Code, working in the Agent OS repository. Build the project IDE, `apps/project-IDE/`, so that it works exactly as described here: the File Tree page, its build, the way the owner's work comes back into the files, and the server that puts Claude Code behind the page. "The same IDE" means every acceptance check at the end passes.

Assume the levels above exist: the repository with `agents/system/` (the system's `CLAUDE.md`, the knowledge base agent with its `file-index` skill, the doc skills), the keys folder `.secrets/` with `test/` and `live/`, and `.gitignore`. Build only the IDE's own folder, its agent, its two skills and its build scripts. The IDE has no child levels with prompts of their own.

Never write a key value anywhere: key names only. Never push, publish or merge without the owner's go. Follow the build order and run each step's check before the next. Where this prompt says a point is open, build nothing for it and ask the owner.

When a reference copy of a file exists in the repository (`apps/project-IDE/current-ui/file-tree-explorer.html`, `agents/system/.claude/skills/ide-build/scripts/*`, `apps/project-IDE/server/*`), start from it and keep its behaviour; this prompt is the spec it must meet. The records in `apps/project-IDE/data/` (the owner's inputs, decisions, changelog and plans) are never written from this prompt: copy them in unchanged as the owner hands them to you.

## The IDE in brief

The project IDE is the owner's window on the Agent OS. The owner builds the system by vibecoding, and the IDE shows the whole project as one clickable tree of every folder and file. For each item it shows what it is, how it works, its text, an example of its structure, its open questions and its details. The owner edits, comments, asks, adds and deletes on the page; the page saves all of it at once in its store; at a sync the project IDE agent writes it into the files and the knowledge base agent sorts it into the docs; then the page is rebuilt from the repository. The same tree gives every AI the full context of any file before it changes it.

The page runs in three places: on claude.ai as a published artifact with its own store; on the owner's server, where a small Python service keeps the store as files, writes edits straight into the files and runs each request as a Claude Code session; and anywhere else as view only. The tree on the page always equals the files in git.

## Ground rules

- **Safety.** No secret value in any file, the page data or a log. `.env` files are never read by the build, the page or the server. Nothing from the page touches `.secrets/` except listing its folders and notes. The server listens only on `127.0.0.1`. Push, history rewrites, deletes other than the item the owner deleted, installs, network tools and anything outside the repository wait for the owner's click.
- **Formats.** The page is one self-contained HTML file with inline CSS and JavaScript (fonts from Google Fonts only). Settings and data are JSON. Docs are Markdown. Build scripts are Python 3.10+ with the standard library only; the page check is Node with Playwright. The server is Python with the standard library plus `claude-agent-sdk`.
- **Generated files.** `file-tree.data.json` and `real-files.json` are built, never edited or merged by hand; after a merge, build again.
- **Metadata next to everything.** Every file and folder you create gets `x.index.md` (How it works) and `x.meta.json` (Details) next to it, named after the item without its extension; a folder keeps them inside it (`server/server.index.md`). A file whose name would clash with a sibling's or its folder's keeps its extension: `server/server.py.index.md`, `server/server.py.meta.json`.
- **Status.** Decided means the owner decided. Anything you add beyond this prompt is marked `proposed` in its Details file.

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
│   ├── file-tree.data.json       the page data (built)
│   └── real-files.json           the text of every file (built; published with the data)
├── server/
│   ├── README.md                 setup, start, safety
│   ├── server.py                 web service
│   ├── claude_bridge.py          Claude Code sessions for page requests
│   ├── voice.py                  speech to text through Groq
│   └── server.config.json        settings
└── data/
    ├── README.md                 what the records are and how they are kept
    ├── inputs/                   [YYYY-MM-DD-HHMM-topic].md per owner input, README.md, index.json
    ├── decisions.md, changelog.md
    ├── plans/[plan].md, plans/index.json, archive/[date]/
    ├── page-store/               nodes/, changes/, inputs/ (server only; one JSON file per document)
    └── overrides.json            the owner's kept edits of the extra tables, keyed by path
agents/system/.claude/
├── agents/project-ide-agent.md
└── skills/
    ├── ide-build/SKILL.md
    │   └── scripts/              README.md, index_files.py, materialize.py, build_map.py, enrich.py,
    │                             tabs.py, check_tree.py, check_page.js, rebuild.py
    └── ide-sync/SKILL.md
start.sh, init.sh                 at the top of the repository: start the IDE, set up the machine once
```

Every file is its own source and is edited where it is; the build copies nothing.

## Conventions

- **Item ids.** An item's id is its path from the top of the repository (`docs/README.md`, `apps/project-IDE`); the top is `agent-os`. An item added on the page is `new-<8 random characters>` until the sync creates it. In the page store, a document key is the id with `/` and every other sign but letters, digits, `.`, `_` and `-` written as `~XX`.
- **Family name.** A file's name without its last extension (`vision.md` → `vision`, `system.workers.json` → `system.workers`); a name with no extension stays whole (`.gitignore`); a folder's own name. Metadata files: `<family>.index.md`, `<family>.meta.json`, `<family>.example.md`, `<family>.questions.md`, `<family>.<type>[.<name>].view.html`.
- **Names on disk.** `|` in a planned name is written `-`; `, ` is written `+`.
- **How it works front matter:**

  ```markdown
  ---
  about: agent-os/apps/project-IDE/docs/README.md
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
   "features": [], "views": [], "how_it_works": {}}
  ```

  `related` and `update_with` hold `{"path": "...", "how": "..."}` objects.
- **Browser storage keys** (wrap every access in try/catch): `ftx-tab2`, `ftx-idx`, `ftx-empty`, `ftx-side`, `ftx-open`, `ftx-sel`, `ftx-ask-<id>`, `ftx-chat-<id>`, `ftx-mdmode`, `ftx-rtheme`, `ftx-rfont`, `ftx-rsize`, `ftx-applied`.

## The parts

### The page: `current-ui/file-tree-explorer.html`

One HTML file. On load it fetches `file-tree.data.json` (no cache), then decides its mode: if `window.claude.use` exists it is on claude.ai and asks for `sample`, `user`, `db` and `comments`; otherwise it fetches `api/health` and, if that answers `{ok: true}`, it is on the owner's server and uses a store shim over `api/store/*` that polls every 4 seconds; otherwise it shows "view only" in the header and disables every save. Colors are tokens on `:root` with a dark set under `prefers-color-scheme: dark` and `[data-theme]`.

Build these features:

1. **Header:** title "Agent OS File Tree"; a version line `v<data_version> · <n> items` plus " · on your server" or " · view only"; the Apply changes button with a count, hidden when nothing is changed; the filter input. Filter rules: text with `*` is a glob on the name; text with `/` matches the path; anything else matches part of the name and is highlighted. Folders on the way to a match open.
2. **Tree:** tabs All and Changed (with count); a "metadata" switch (default on) that shows each item's `.index.md` and `.meta.json` as rows (under a file, first inside a folder) and hides scanned metadata files when off; an "empty" filter (default off) that shows only the empty files and the folders that hold them. Rows show icon, name and a "changed" tag. A first click on a closed folder opens it. Arrow keys move, open and close. Deleted items stay struck through in their place until the sync. The selected item goes into the URL hash.
3. **Sheet:** breadcrumbs, name, Delete (not on the root), a "Changed · reason" chip, the kind, the purpose line, then the tabs.
4. **Tabs:** How it works first, Details last. Files: File, and ASD-STE100, Example and Questions only where their files exist (`README.asd.md`, `x.example.md`, `x.questions.md`). Folders: Contents, and Questions where its file exists. Agent folders add Overview and Agents first; jobs files add Jobs; and the item's `custom_tabs` (Links, Variables, Tests, Capabilities) as editable tables.
5. **How it works:** reads `how_md`; shows the file name and Edit; six fixed headings and Keep in mind, or one Summary; lists messages waiting for the sync and every page change with "Undo this change". Edit opens a Markdown editor (Ctrl+S saves).
6. **File:** the text with a path bar and source; numbered lines, a click on a number opens a line comment; 3,000 lines at a time with "Show more"; lazy texts loaded once from `real-files.json`; "Write it" and "Start from the example" for a file with no text; read-only items show why; Edit opens the editor with a gutter and wrapping lines (Ctrl+S). A Markdown file opens in the Read view: white or black paper (`ftx-rtheme`), an Aa menu (Sans, Legible, Serif; S, M, L), word count and reading time, a Contents list, Read and Source, full screen with a side contents column above 1120 px, a progress line and Esc to close. Every rendered block carries its source lines; a double-click, or two taps within 400 ms, replaces the block with a textarea of those lines; Save or Ctrl+Enter writes only them; Esc cancels.
7. **Contents:** cards for the children, "Add a file or folder" (name, type, purpose), "Comment on this folder".
8. **Example:** an outline (a doc's structure from its skill) or a code box plus a field table (Field, Values, Example, What it is for); jobs and links files build their example from their table.
9. **Questions:** the item's `x.questions.md` in the Read view, and the questions answered on the page.
10. **Details:** the item's `meta` as JSON with the file name.
11. **Notes:** comments `{id, line, snippet, text, at, by, resolved}` on a line or the whole item, re-anchored by snippet; Resolve, Reopen, Delete; resolved hidden by default.
12. **Ask box:** per-item chat kept in the browser (last 30 messages); Enter sends, Shift+Enter breaks; Clear, Stop. Every message is first saved as an `inputs` document with status `new`. On claude.ai: model tiers Most capable (`complex`), Balanced (`default`), Fastest (`quick`); `sample.json` with tools returns `{kind: answer|draft|save|discard, reply, title, changes, qa}`; a draft card lists each changed item and field with a before/after diff, Save (or the word "save") applies it, Discard drops it; an answered question is saved to the item's `qa`. After every save, a "related updates" pass asks Claude for consistent changes to the parents and items that mention the saved ones, never changing another file's `content` or any `how_md`, saved as one undoable change. On the server: `POST api/agent`, then the SSE stream; show steps, an Allow/Refuse box, cost, seconds and changed-file count; keep the session id for follow-ups; reload the data when files changed; mark every touched item `worked`. A microphone button (server only, when voice is available) records up to 300 seconds with a timer and posts to `api/voice`; the text is appended to the box.
13. **Delete and restore:** the delete form with an optional note and "Delete and clean up". On the server it saves the deletion with `cleanup: "claude-code"` and sends `Delete the file|folder <path> and clean the project of it.` plus `Keep in mind: <note>` with `delete: <path>`; on claude.ai it saves `cleanup: "sync"` and an input of kind `delete`. "Bring it back" on the server sends a restore request; on claude.ai "Restore it" clears the flag.
14. **Changed and Apply changes:** one status, changed, with reasons new, edited, removed, commented, asked, worked. Apply changes opens a confirmation; on claude.ai it calls `comments.canSendToClaude()`, posts `comments.sendToClaude({anchor, text})` and saves an `inputs` document of kind `apply` with `count`, `items`, `sent_to_claude` and `thread` or `not_sent`; when that input turns `processed` it loads the new data (higher `data_version`) or offers Reload. On the server it selects the root and runs one Claude Code request starting "Sync the file tree:". A waiting request can be cancelled on claude.ai.
15. **Phone:** below 760 px one pane at a time with a "‹ Tree" back button; nothing wider than the viewport.

Store writes: `nodes/<id>` holds `{fields, comments, qa, new_node, deleted, was, delete_note, cleanup, worked, updated_at, by}`; every save also adds a `changes` document `{at, by, title, instruction, kind: edit|qa|ripple|delete, items: [{node_id, path, kind: set|remove|new|restore|qa, fields: {k: {before, after}}}], undone}`. Editable fields: `name, summary, purpose, link_target, details, writers_readers, updated_when, open_questions, example, fields, custom_tabs, content, how_md`.

Check: `check_page.js` prints "page ok".

### The page data: `current-ui/file-tree.data.json` and `real-files.json`

Top level: `schema_version` (2), `title`, `source {repo, doc_version}`, `generated`, `data_version` (integer, one more each build), `sync`, `status_legend`, `root` (`agent-os`), `concepts`, `decisions`, `nodes`. Each node: `id` (its path), `name, path` (starting `agent-os/`), `type` (file|folder), `parent, children, link, link_target, placeholder, exists, local_only, status, purpose, summary, decisions, open_questions, qa, example {title, lang, body, file}, fields, custom_tabs, agent, how {text, sections, keep, at, by, state}, how_md, how_state, how_file, meta, meta_file, fam, questions_md, questions_file, asd_md, asd_file, content, content_lazy, content_source, content_self, src_file, readonly, empty`. `real-files.json` maps each item id to its text; a file over 200 KB, a non-text file, a keys file and the built files are not in it.

Check: the data parses; every `children` id exists; no node's `content` contains a value from a `.env` file.

### The build: `ide-build` and its scripts

`SKILL.md` gives the inputs table, the scripts table, the steps, the rules and the checks below. The files on disk and their metadata files are the only source; nothing is copied. The scripts, in `agents/system/.claude/skills/ide-build/scripts/`:

- `index_files.py`: the items (`git ls-files --cached --others --exclude-standard`, the folders that hold them and the local `.env` files, listed but never read), each with its path as id; `index_path(item)`, `meta_path(item)`, `load_all()`, `save()`, `missing()`, `orphans()`; stage two (`agents/trading/prediction-market/` outside its `docs/`) gets no new metadata files.
- `materialize.py` (`REPO_DIR` optional): gives every new item outside stage two an empty `x.index.md` and `x.meta.json` (`{}`), keeps a `.gitkeep` in every empty folder and removes it once the folder holds a file, writes `docs/file-tree.md` (every path in git without the metadata files); never creates or reads a `.env` file.
- `build_map.py`: the basis of each How it works file is a hash of its item's content (nothing for a folder, a keys file or a built file) and, for a folder, its items' names and How it works texts; default run prints "how it works files: N fresh, M missing or stale, K orphans ..."; `--stale`, `--empty`, `--context <path>`, `--set <file.json>` (`{path: text}` or `{path: {text, sections: [{title, text}], keep: [...]}}`, writer from `BY`), `--confirm <path>...` (or `-` for stdin), `--orphans`.
- `enrich.py [<out data>]` with `DATA_VERSION=<n>`: reads every item with its How it works, Details, Example, Questions and ASD-STE100 files, the tabs from `tabs.py`, the owner's kept edits from `apps/project-IDE/data/overrides.json` (keyed by path) and the decisions from `apps/project-IDE/data/decisions.md`; marks empty files; writes `apps/project-IDE/current-ui/file-tree.data.json` and `real-files.json` next to it.
- `tabs.py`: field guides; the Variables table for each `.env` (names and purposes, fake example values only); Jobs, Links, Tests and Capabilities tables.
- `check_tree.py`: the page's items are exactly the files in git, the folders that hold them and the top, with the path as each id, plus the local `.env` files; prints "tree ok".
- `check_page.js <page dir> <shots dir|-> <paths...>`: loads the page in Chromium at 1400×900 and 390×844 with an in-memory stand-in for `window.claude` (`db`, `sample`, `user`), opens each item by its path in the URL hash, clicks How it works and File, fails on a page error, a missing item, an address that does not open its item, no tabs rendered, or (at phone width) a document wider than the viewport; saves a screenshot per width and item when given a folder; prints "page ok" or the number of problems and exits non-zero. `PLAYWRIGHT` and `CHROMIUM` override module and browser paths.
- `rebuild.py` (standard library only; run by `start.sh`): runs `materialize.py`; builds the data with `enrich.py` into a scratch folder with the current `data_version` and compares it with `apps/project-IDE/current-ui/file-tree.data.json` without the `generated` key, and the scratch `real-files.json` with the one next to the page; only when either differs runs `enrich.py` in place with `DATA_VERSION` = current + 1, otherwise prints that the data is kept at its version; then prints the `build_map.py` report and runs `check_tree.py`. Exit 0 when the tree check passes, 1 otherwise. It never writes a How it works file and never publishes; a stale one is only reported.

Steps, from the top of the repository, with `S` the scripts folder and `N` = current `data_version` + 1:

```bash
python3 $S/materialize.py
python3 $S/build_map.py --stale                         # write or --confirm each one
DATA_VERSION=N python3 $S/enrich.py
python3 $S/materialize.py                               # rerun the two above if it made files
python3 $S/build_map.py                                 # "fresh, 0 missing or stale, 0 orphans"
python3 $S/check_tree.py                                # "tree ok"
node $S/check_page.js apps/project-IDE/current-ui - agent-os docs/README.md <changed paths>
```

Publish the page by its link, https://claude.ai/artifact/72v2Uppt6jpfXLCjKNX9xs, with `files` mapping `file-tree.data.json` and `real-files.json`, and the capabilities `db`, `sample`, `user` and `comments` (restate all four on every publish that passes capabilities).

Check: the build ends with "tree ok" and "page ok", and no stale or orphaned How it works file.

### The sync: `ide-sync`

`SKILL.md` describes the three collections (`inputs`, `nodes`, `changes`) as in the page part, where they are read (the artifact data tool on the page link; on the server `page-store/<collection>/<id>.json`), and these steps: list new inputs and touched nodes; save each as an owner input word for word with its answer; write `content` into the file, `how_md` into the `.index.md` word for word with `by: owner` then `build_map.py --confirm <path>`, new items onto disk with their metadata files as proposed, edits of the extra tables into `overrides.json`, open comments into open questions unless they ask for a change; run the page requests; hand the inputs to the knowledge base agent; run `ide-build`; mark inputs processed (`processed_at`, `processed_into`) and delete folded `nodes` documents, leaving `changes`; for an Apply changes round mark the `apply` input processed last, then answer and resolve the page comment; report in two to five lines. Its "Deleting an item" section: read the note; delete the item and its metadata files; remove its links, mentions and the parent's How it works entry; file it with a changelog line; rebuild; commit. Bring back is the reverse from git.

Check: after a sync, no `inputs` document is `new`, and every edit is in its file.

### The server: `server/`

- `server.config.json` keys: `repo` (the repository top relative to the server folder: `../../..`), `host` `127.0.0.1`, `port` `8765`, `page_dir`, `page`, `data`, `store_dir`, `write_through` `true`, `log_dir` (`agents/system/logs/subagents/project-ide-agent`), `secrets {file: ".secrets/test/.env", keys: ["ANTHROPIC_API_KEY", "GROQ_API_KEY"]}`, `voice {url: "https://api.groq.com/openai/v1/audio/transcriptions", models: ["whisper-large-v3-turbo", "whisper-large-v3"], key: "GROQ_API_KEY", max_seconds: 300, language: null}`, `claude {cwd, model: null, max_turns: 80, max_budget_usd: 3, approval_timeout_s: 900, allow: [...], ask_owner: ["git push", "git reset", "git rebase", "git checkout --", "git clean", "rm ", "rmdir ", "chmod ", "chown ", "sudo ", "curl ", "wget ", "pip install", "npm install", "kill "], never: [".secrets"]}`. `allow` lists Read, Glob, Grep, LS, Edit, Write, MultiEdit, NotebookEdit, TodoWrite, Task, Agent, Skill, WebSearch, WebFetch and `Bash(...)` for cd, python3, node, ls, cat, head, tail, wc, grep, rg, find, mkdir, cp, mv, jq, diff, git status, ls-files, grep, diff, log, show, add, commit, pull, fetch, merge. `claude.cwd` is `agents/system`. These limits are defaults the owner may change.
- `server.py` (standard library `ThreadingHTTPServer`): exits if `host` is not local; rejects any request whose Host or Origin is not `127.0.0.1`, `localhost` or `::1`. Routes: `GET /` redirects to the page; `GET /<page>`, `/<data>`; `GET /real-files.json` reads scanned files fresh from disk (never under `never` paths); `GET /api/health` → `{ok, server: "project-ide", agent, agent_error, repo, claude_cwd, write_through, voice, voice_max_seconds}`; `GET /api/store/<coll>` → `{docs: [{id, data}]}`; `POST /api/store/<coll>` → `{id}`; `PUT|PATCH /api/store/<coll>/<id>` → `{ok, written}`; `POST /api/agent` `{text, node_id, path, name, num, session, input_id, kind, delete}` → `{run}`; `GET /api/agent/<run>/events` (SSE, `id:` per event, resumable); `POST /api/agent/<run>/answer` `{id, allow}`; `POST /api/agent/<run>/stop`; `POST /api/voice` (raw audio, 25 MB at most) → `{text, model}`. Collections are only `nodes`, `changes`, `inputs`; ids match `^[A-Za-z0-9_.:@+~-]{1,200}$`; files are written atomically. Write-through on `nodes` saves: `content` into the item's `src_file` (and `real_file`), never a text containing "…(cut for the page", never a field equal to the previous save; `how_md` into the item's How it works file next to it on disk, with front matter kept and `written` now, `by: owner`. Secrets are read from the keys file by name only; the Groq key is not passed to Claude Code.
- `claude_bridge.py`: one run per request, id `YYYYMMDD-HHMMSS-<6 hex>`, in a thread; `ClaudeSDKClient` with `cwd` from the config, `add_dirs` the repository, `setting_sources ["project", "local"]`, all skills, the `claude_code` system prompt with an appended note (work for the owner through the page; follow the system's `CLAUDE.md`, file the request, finish the round, never push, never open the keys folder; answer plainly), `allowed_tools` from `allow`, a `PreToolUse` hook and `can_use_tool` both using one check: deny anything naming a `never` path; allow exactly `git rm -r -q --ignore-unmatch <item and its metadata files>` and `rm -rf <same>` for a page deletion; ask for paths outside the repository and commands containing an `ask_owner` word. Asking emits `approval {id, tool, summary, reason}` and waits up to `approval_timeout_s`, then `answered`. Events: `start`, `text`, `tool {tool, summary}`, `approval`, `answered`, `result {text, cost_usd, duration_ms, turns, session, is_error, subtype}`, `error`, `end {changed, seconds}`. `changed` comes from git: files that differ from HEAD at the start or changed during the run, committed or not, never under `never`. Each run is logged as `<log_dir>/<YYYYMMDD>/<run>.json` with node, request, result, changed, steps and the owner's answers. The prompt names the item and, when given, the input file in the page store to mark processed.
- `voice.py`: posts multipart audio to the configured URL with the key as a bearer token; tries the models in order; a 429 parks a model for its `retry-after` (5 to 3,600 seconds); an error moves on; keeps nothing.
- `README.md`: what you need, how to start (`./init.sh` once, then `./start.sh`, with its four steps and its other commands; the manual way `python3 apps/project-IDE/server/server.py` from the repository top), the SSH tunnel, what happens for each page action, the settings table, the files.

Check: start the server, open `http://127.0.0.1:8765/`; the header says "on your server"; a comment creates `page-store/nodes/<id>.json`; a File edit changes the file on disk; a request lists the system's agents; a `git push` waits for Allow.

### The start scripts: `start.sh` and `init.sh` at the top of the repository

Both are Bash, executable, run from any folder (they find the repository top from their own path), and never read a keys file. The service name `project-ide`, the fast-forward-only pull, reporting the page store instead of syncing it, and `.venv/` are defaults the owner may change.

- `start.sh [""|start|--no-pull|stop|status|logs|serve|-h]`. Python is `.venv/bin/python` when it exists, else `python3`; the port is `IDE_PORT` or `port` in `server.config.json` (default 8765); run-time files go to `agents/system/logs/services/project-ide/` (`server.log`, `server.pid`; git ignores them).
  - **sync** (skipped with `--no-pull`): on a branch with an upstream, `git fetch` (60-second limit; on failure start with what is on disk). When behind: `git checkout --` the three built files (`apps/project-IDE/current-ui/file-tree.data.json`, `apps/project-IDE/current-ui/real-files.json`, `docs/file-tree.md`); then `git merge --ff-only` only when there are no local commits and no other tracked file is changed; otherwise warn and skip. Never merge, stash or push. Then count the JSON files in `apps/project-IDE/data/page-store/nodes/` and, when any, say that many items are marked changed and to press Apply changes or say "sync the file tree"; never run the sync.
  - **stop**: `systemctl --user stop project-ide` when the unit exists and is active; then for the pid file and every process listening on the port, kill it (TERM, then KILL after 5 seconds) only when its command line contains `project-IDE/server/server.py`; if another program still holds the port, fail.
  - **rebuild**: `rebuild.py`; a failure is a warning and the server starts with the data on disk.
  - **start** (the default): stop; with the unit, follow its journal, pass `NO_PULL` through the user manager's environment and `systemctl --user start project-ide`; without it, `nohup start.sh serve` in the background with output to `server.log` and its pid in `server.pid`. Poll `GET /api/health` once a second up to 120 seconds (stop early when the unit fails), then print the address, the health answer and `ssh -N -L <port>:127.0.0.1:<port> <user>@<this server>`; exit 1 when it never answers.
  - **serve** (what the unit runs): sync, stop stray servers, rebuild, then `exec` the server in the foreground.
  - **status**: the unit's state and the health answer. **logs**: `journalctl --user -u project-ide -f`, or `tail -f` of `server.log`.
- `init.sh [--no-service]`, safe to run again: check git, curl, `python3` 3.10 or newer (fail without them), and node and `claude` (warn without them); create `.venv/` (git ignores it) with `uv venv`, `python3 -m venv` or `virtualenv`, and install `claude-agent-sdk` into it; unless `--no-service`, write `~/.config/systemd/user/project-ide.service` (`Type=simple`, `ExecStart=/bin/bash <repo>/start.sh serve`, `WorkingDirectory=<repo>`, `Restart=on-failure`, `RestartSec=10`, `TimeoutStartSec=180`, `KillMode=control-group` so a stop also ends the Claude Code runs it started, `WantedBy=default.target`, and `Environment=` lines with the caller's `PATH` without editor-server entries and `CLAUDE_CONFIG_DIR` when set, so the service finds node and `claude` and uses the same sign-in), `daemon-reload` and `enable` it; check lingering with `loginctl show-user`, try `loginctl enable-linger`, else print the `sudo` command; then run `./start.sh`.

Check: `./start.sh` prints the address and a health answer `{"ok": true, ...}`; `./start.sh` again stops the old process and says the data is kept at its version, and `git status` shows no change to the built files; a server started by hand on the port is stopped by the next `./start.sh`; `./start.sh status` shows the unit active; after a reboot the health check answers without a login.

### The agent: `agents/system/.claude/agents/project-ide-agent.md`

Front matter: `name: project-ide-agent`, a description, `tools: Read, Write, Edit, Bash, Grep, Glob`, `model: opus`, `memory: project`, `skills: ide-build, ide-sync, file-index`. Body: its job (build, bring back, run page requests, delete cleanly); how it works with the knowledge base agent (it saves inputs and edits, the knowledge base agent sorts them; the files and their metadata win over the page); where things are; when it runs (sync or Apply changes, after a round that changed the tree or a doc, a waiting request, after a pull, as the server's session); the steps each time (pull, sync, build, publish, report, commit); the rules (never lose the owner's words, never edit the data by hand, decided means the owner decided, no secret values, ask before anything hard to undo, never push from the server).

Check: the file parses as an agent definition and names both skills.

### The docs: `docs/`

`vision.md`, `README.md`, `README.asd.md` and `rebuild-prompt.md`, written by the knowledge base agent with the `vision-doc`, `readme-doc`, `readme-asd-doc` and `rebuild-prompt-doc` skills, in that order, each with its `.index.md`, `.meta.json`, `.example.md` and `.questions.md`.

## Build order

1. Create the folders in the tree with their `.index.md` and `.meta.json`. Check: every folder has both.
2. Write `index_files.py`, `materialize.py`, `tabs.py`, `build_map.py`, `enrich.py`, `check_tree.py`, `rebuild.py`. Check: they run on the repository without an error, `check_tree.py` prints "tree ok", and a second `rebuild.py` keeps the data version.
3. Write the page. Check: it loads the data in a browser in view-only mode.
4. Write `check_page.js`. Check: "page ok" on `agent-os` and `docs/README.md`.
5. Run the full build and fix every stale or orphaned How it works file through `file-index`. Check: "fresh, 0 missing or stale, 0 orphans".
6. Write `ide-build`, `ide-sync` and the agent. Check: a test sync on a stand-in store folds one comment and one edit.
7. Write the server files and their README, then `start.sh` and `init.sh` at the top of the repository. Check: the server checks and the start-script checks above.
8. Write the four docs. Check: they agree with each other and with this prompt.
9. Publish the page at its link (only with the owner's go). Check: the acceptance checks.

## Acceptance checks

- `check_page.js` prints "page ok" for `agent-os`, `docs/README.md` and every changed item.
- `build_map.py` reports every How it works file fresh, none missing, no orphans.
- The tree equals git: `check_tree.py` prints "tree ok" (the item paths in the data equal `git ls-files --cached --others --exclude-standard` with their folders, plus only the two local `.env` files).
- Every file and folder under `apps/project-IDE/` has its `.index.md` and `.meta.json`, and every `.meta.json` has every schema key.
- `grep` finds no key value from `.secrets/*/.env` in the data, `real-files.json`, the store or the logs.
- The server refuses a non-local host and any request with a foreign Origin.
- A page deletion on the server removes exactly the item and its metadata files without a click, and any other `rm` waits for one.
- An Apply changes round ends with its `apply` input processed and the page showing the new data version.
- `./start.sh` run twice leaves the built files unchanged in git and ends with a health answer; the service starts the IDE at boot.

## Do not build

- Custom views (`<family>.<type>.<name>.view.html` and shared views): designed but not built; leave the page's current extra tabs in place. Where shared views live is open.
- Tabs read from real files (Example from `x.example.md`, Questions from `x.questions.md`, an ASD-STE100 tab from `README.asd.md`, shown only when the file exists): stage one work, not built yet; keep today's tabs until it is done.
- Filled Details files everywhere: leave empty templates where nothing is known.
- A scheduled routine that syncs the page store without Apply changes: a proposal, not built.
- Updating the published claude.ai page after work on the server: open.
- Running `check_page.js` on the owner's server: open; Chromium there needs system libraries (`sudo npx playwright install-deps`), which only the owner installs. Do not install them yourself.
- Statuses other than "changed": not built until the owner asks.
- Any file under the prediction-market domain other than its folders: stage two.
