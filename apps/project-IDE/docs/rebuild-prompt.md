# Rebuild the project IDE

## Your task

You are an AI coding agent, such as Claude Code, working in the Agent OS repository. Build the project IDE, `apps/project-IDE/`, so that it works exactly as described here: the File Tree page, its build, the way the owner's work comes back into the files, and the server that puts Claude Code behind the page. "The same IDE" means every acceptance check at the end passes.

Assume the levels above exist: the repository with `agents/system/` (the system's `CLAUDE.md`, the knowledge base agent with its `file-index` skill, the doc skills), the keys folder `.secrets/` with `test/` and `live/`, and `.gitignore`. Build only the IDE's own folder, its agent, its two skills and its build scripts. The IDE has no child levels with prompts of their own.

Never write a key value anywhere: key names only. Never push, publish or merge without the owner's go. Follow the build order and run each step's check before the next. Where this prompt says a point is open, build nothing for it and ask the owner.

When a reference copy of a file exists in the repository (`apps/project-IDE/current-ui/file-tree-explorer.html`, `agents/system/.claude/skills/ide-build/scripts/*`, `apps/project-IDE/server/*`), start from it and keep its behaviour; this prompt is the spec it must meet. The records in `apps/project-IDE/data/` (the owner's inputs, decisions, changelog and plans) are never written from this prompt: copy them in unchanged as the owner hands them to you.

## The IDE in brief

The project IDE is the owner's window on the Agent OS. The owner builds the system by vibecoding, and the IDE shows the whole project as one clickable tree of every folder and file. For each item it shows what it is, how it works, its text, an example of its structure, its open questions and its details. The owner edits, comments, asks, adds and deletes on the page; the page saves all of it at once in its store; at a sync the project IDE agent writes it into the files and the knowledge base agent sorts it into the docs; then the page is rebuilt from the repository. The same tree gives every AI the full context of any file before it changes it.

The page runs in three places: on claude.ai as a published artifact with its own store; on the owner's server, where a small Python service keeps the store as files, writes edits straight into the files and runs each request as a Claude Code session; and anywhere else as view only. On the server the page also has a Notes and runs panel: every note the owner types or records and every Claude Code run in the repository, from the page or a terminal, is one row; notes sent together become one run; each run from the page works on its own branch in a git worktree and the server merges it into `main`; each run has its own page with every step, read from Claude Code's transcripts. The tree on the page always equals the files in git.

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
│   ├── claude_bridge.py          Claude Code sessions for page requests and notes
│   ├── notes.py                  notes, run records, statuses, combining notes into one request
│   ├── runs.py                   Claude Code transcripts into runs with every step
│   ├── run_summary.py            each run's ASD-STE100 summary and tags (Claude Haiku)
│   ├── worktrees.py              each page run's branch and worktree; the local merge into main
│   ├── voice.py                  speech to text through Groq
│   └── server.config.json        settings
└── data/
    ├── README.md                 what the records are and how they are kept
    ├── inputs/                   [YYYY-MM-DD-HHMM-topic].md per owner input, README.md, index.json
    ├── decisions.md, changelog.md
    ├── plans/[plan].md, plans/index.json, archive/[date]/
    ├── page-store/               nodes/, changes/, inputs/, notes/ (server only; one JSON file per document; git ignores notes/)
    └── overrides.json            the owner's kept edits of the extra tables, keyed by path
agents/system/.claude/
├── agents/project-ide-agent.md
└── skills/
    ├── ide-build/SKILL.md
    │   └── scripts/              README.md, index_files.py, materialize.py, build_map.py, enrich.py,
    │                             tabs.py, check_tree.py, check_page.js, rebuild.py
    └── ide-sync/SKILL.md
start.sh, init.sh                 at the top of the repository: start the IDE, set up the machine once
.worktrees/<run>/                 at the top of the repository: one checkout per page run (git ignores it)
agents/system/logs/subagents/project-ide-agent/runs/<run>.json   one record per run (git ignores logs)
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
- **Browser storage keys** (wrap every access in try/catch): `ftx-tab2`, `ftx-idx`, `ftx-empty`, `ftx-side`, `ftx-open`, `ftx-sel`, `ftx-ask-<id>`, `ftx-chat-<id>`, `ftx-mdmode`, `ftx-rtheme`, `ftx-rfont`, `ftx-rsize`, `ftx-applied`, `ftx-tier`, and on the server `ftx-jobs-open` (the panel open), `ftx-jobs-show` (its tab), `ftx-jnew` (unsent text of the new-note box) and `ftx-send-opts` (the send options).

## The parts

### The page: `current-ui/file-tree-explorer.html`

One HTML file. On load it fetches `file-tree.data.json` (no cache), then decides its mode: if `window.claude.use` exists it is on claude.ai and asks for `sample`, `user`, `db` and `comments`; otherwise it fetches `api/health` and, if that answers `{ok: true}`, it is on the owner's server and uses a store shim over `api/store/*` that polls every 4 seconds; otherwise it shows "view only" in the header and disables every save. Colors are tokens on `:root` with a dark set under `prefers-color-scheme: dark` and `[data-theme]`.

Build these features:

1. **Header:** title "Agent OS File Tree"; a version line `v<data_version> · <n> items` plus " · on your server" or " · view only"; the Apply changes button with a count, hidden when nothing is changed; the filter input. Filter rules: text with `*` is a glob on the name; text with `/` matches the path; anything else matches part of the name and is highlighted. Folders on the way to a match open.
2. **Tree:** tabs All and Changed (with count); a "metadata" switch (default on) that shows each item's `.index.md` and `.meta.json` as rows (under a file, first inside a folder) and hides scanned metadata files when off; an "empty" filter (default off) that shows only the empty files and the folders that hold them. Rows show icon, name and a "changed" tag. A first click on a closed folder opens it. Arrow keys move, open and close. Deleted items stay struck through in their place until the sync. The selected item goes into the URL hash.
3. **Sheet:** breadcrumbs, name, Delete (not on the root), a "Changed · reason" chip, the kind, the purpose line, then the tabs.
4. **Tabs:** How it works first, Details last. Files: File, and ASD-STE100, Example and Questions only where their files exist (`README.asd.md`, `x.example.md`, `x.questions.md`). Folders: Contents, and Questions where its file exists. Agent folders add Overview and Agents first; jobs files add Jobs; and the item's `custom_tabs` (Links, Variables, Tests, Capabilities) as editable tables.
5. **How it works:** reads `how_md`; shows the file name and Edit; six fixed headings and Keep in mind, or one Summary; lists messages waiting for the sync and every page change with "Undo this change". Edit opens a Markdown editor (Ctrl+S saves).
6. **File:** the text with a path bar and source; numbered lines, a click on a number opens a line comment; 3,000 lines at a time with "Show more"; lazy texts loaded once from `real-files.json`; "Write it" and "Start from the example" for a file with no text; read-only items show why; Edit opens the editor with a gutter and wrapping lines (Ctrl+S). A Markdown file opens in the Read view: white or black paper (`ftx-rtheme`), an Aa menu (Sans, Legible, Serif; S, M, L), word count and reading time, a Contents list, Read and Source, full screen with a side contents column above 1120 px, a progress line and Esc to close. Every rendered block carries its source lines; a double-click, or two taps within 400 ms, makes the block editable in place; Save or Ctrl+Enter writes only its lines; Esc cancels. When the block turns back into Markdown, an `<a>` with no address, or whose address without `http://`, `https://` or `mailto:` and a final `/` equals its text (a link the browser made by itself, such as `x.md` turned into `http://x.md`), is written as its plain text; any other link becomes `[text](address)`.
7. **Contents:** cards for the children, "Add a file or folder" (name, type, purpose), "Comment on this folder".
8. **Example:** an outline (a doc's structure from its skill) or a code box plus a field table (Field, Values, Example, What it is for); jobs and links files build their example from their table.
9. **Questions:** the item's `x.questions.md` in the Read view, and the questions answered on the page.
10. **Details:** the item's `meta` as JSON with the file name.
11. **Notes:** comments `{id, line, snippet, text, at, by, resolved}` on a line or the whole item, re-anchored by snippet; Resolve, Reopen, Delete; resolved hidden by default.
12. **Ask box:** per-item chat kept in the browser (last 30 messages); Enter sends, Shift+Enter breaks; Clear, Stop. Every message is first saved as an `inputs` document with status `new`. On claude.ai: model tiers Most capable (`complex`), Balanced (`default`), Fastest (`quick`); `sample.json` with tools returns `{kind: answer|draft|save|discard, reply, title, changes, qa}`; a draft card lists each changed item and field with a before/after diff, Save (or the word "save") applies it, Discard drops it; an answered question is saved to the item's `qa`. After every save, a "related updates" pass asks Claude for consistent changes to the parents and items that mention the saved ones, never changing another file's `content` or any `how_md`, saved as one undoable change. On the server: a message is first made a note (`POST api/notes` with `context.where: "ask box"`) and sent at once as its own run (`POST api/notes/send` with that id, the send options, the chat's `session` and the item as `node`); no `inputs` document is kept for it; then the SSE stream of the run; show steps, an Allow/Refuse box, cost, seconds and changed-file count; keep the session id for follow-ups; reload the data when files changed; mark every touched item `worked`. The box grows with its text up to half the viewport height. A microphone button (server only, when voice is available) records up to 300 seconds with a timer; in the ask box, the panel and the selection bar it first makes a note with `recording: true` (status `transcribing`) and posts the audio to `api/notes/<id>/audio`; in the delete note box it posts to `api/voice` and appends the text to that box.
13. **Delete and restore:** the delete form with an optional note and "Delete and clean up". On the server it saves the deletion with `cleanup: "claude-code"` and sends `Delete the file|folder <path> and clean the project of it.` plus `Keep in mind: <note>` with `delete: <path>`; on claude.ai it saves `cleanup: "sync"` and an input of kind `delete`. "Bring it back" on the server sends a restore request; on claude.ai "Restore it" clears the flag.
14. **Changed and Apply changes:** one status, changed, with reasons new, edited, removed, commented, asked, worked. Apply changes opens a confirmation; on claude.ai it calls `comments.canSendToClaude()`, posts `comments.sendToClaude({anchor, text})` and saves an `inputs` document of kind `apply` with `count`, `items`, `sent_to_claude` and `thread` or `not_sent`; when that input turns `processed` it loads the new data (higher `data_version`) or offers Reload. On the server it selects the root and runs one Claude Code request starting "Sync the file tree:". A waiting request can be cancelled on claude.ai.
15. **Phone:** below 760 px one pane at a time with a "‹ Tree" back button; nothing wider than the viewport.
16. **Notes and runs panel** (server only, when `api/health` answers `jobs: true`; hidden elsewhere): a header button "Notes and runs" with the number of active rows, or "N need you" in red when any row is `need human`; it opens or closes the panel under the header (`ftx-jobs-open`). The panel: tabs All, Notes, Runs (`show=all|notes|runs`), Refresh, Hide; a new-note box that grows with its text, Ctrl+Enter or Add note adds it (`context.where: "notes panel"`), with a microphone; the rows from `GET api/jobs?offset&limit&show` (10 a page), a line "N of M" and Show more (10 more); a folded line "Options: local · auto merge · related tests · bug check · report" that opens the send options (Where: Local, Cloud disabled; Merge: Auto merge, Ask me; Tests: Related, All, None; Check for bugs; Report), kept in `ftx-send-opts`, defaults from `send_options` in the health answer; Send all (N) posts every checked `ready` note to `api/notes/send`. Poll every 4 seconds while open.
    - A note row: checkbox (`include`), status, the item's path (click opens it), tags "selection · line N" and "voice", time, text; buttons by status: Send after transcript (while `transcribing`; sets `send_after_transcript`), Edit with Save and Cancel edit (`PATCH api/notes/<id>`), Send, Open run, Cancel (`POST api/notes/<id>/cancel`), Delete (`POST api/notes/<id>/delete`), Details (where, item, tab, line, selected text, typed or voice, made, page version, run, sent from, in main at, note id); and the version line `sent at <commit> · page v<N> → in main at <commit> · page v<M>`.
    - A run row: status, title (click opens `#run/<id>` and closes the panel), tags, origin (page or terminal), branch, steps, cost (page) or largest context (terminal), time, number of notes; Stop while at work; Merge into main for a finished page run with a branch.
    - Selecting text on an item's sheet shows a small bar with "Record about this" (microphone) and "Note" (prefills the new-note box); the note's context keeps `selection` (the text), `line` when the tab shows lines, `tab`, `path`, `node_id` and `name`.
17. **The page of a run** at `#run/<id>`, in place of the item sheet; the ask box hides; "‹ Back" returns. From `GET api/runs/<id>`: title, status, origin, tags, folder, branch, start, length, model, cost, largest context, tokens written, steps. Buttons: Stop, Merge into main, Discard the branch, Make PR and Make PR and merge (rendered disabled), Copy `claude --resume <session>`. Sections: Summary (with Write it again, `POST api/runs/<id>/summary`), Request, Answer, Notes with their context, Send options, Git (sent from and in main at, branch and its commits, files changed with links to their items, commits during the run, the repository's current branch and uncommitted files), What it used (chips for kinds, tools, skills, subagents, MCP, plugins, workflows, web; files read and edited; a chip filters the steps), Checks and tests, Plan; Steps: one collapsible row per step with an icon by kind, summary, time, duration and a bar for the context size; opened, input and output, "Show all of it" (`GET api/runs/<id>/steps/<step>`) when cut, a subagent's steps nested inside; Open all, Close all. A live run refreshes every 4 seconds.

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

- `server.config.json` keys: `repo` (the repository top relative to the server folder: `../../..`), `host` `127.0.0.1`, `port` `8765`, `page_dir`, `page`, `data`, `store_dir`, `write_through` `true`, `log_dir` (`agents/system/logs/subagents/project-ide-agent`), `secrets {file: ".secrets/test/.env", keys: ["ANTHROPIC_API_KEY", "GROQ_API_KEY"]}`, `voice {url: "https://api.groq.com/openai/v1/audio/transcriptions", models: ["whisper-large-v3-turbo", "whisper-large-v3"], key: "GROQ_API_KEY", max_seconds: 300, language: null}`, `claude {cwd, model: null, max_turns: 80, max_budget_usd: 3, approval_timeout_s: 900, allow: [...], ask_owner: ["git push", "git reset", "git rebase", "git checkout --", "git clean", "rm ", "rmdir ", "chmod ", "chown ", "sudo ", "curl ", "wget ", "pip install", "npm install", "kill "], never: [".secrets"]}`. `allow` lists Read, Glob, Grep, LS, Edit, Write, MultiEdit, NotebookEdit, TodoWrite, Task, Agent, Skill, WebSearch, WebFetch and `Bash(...)` for cd, python3, node, ls, cat, head, tail, wc, grep, rg, find, mkdir, cp, mv, jq, diff, git status, ls-files, grep, diff, log, show, add, commit, pull, fetch, merge. `claude.cwd` is `agents/system`. These limits are defaults the owner may change. Also: `send_options {where: "local", merge: "auto", tests: "related", bug_check: true, report: true}` (the defaults of the panel's send options; `where` is `local` or `cloud`, `merge` is `auto` or `ask`, `tests` is `related`, `all` or `none`), `worktrees {folder: ".worktrees", main: "main"}` and `runs {claude_config_dir: null, live_seconds: 90, max_text: 1200, summary_model: "haiku"}` (`claude_config_dir` null means `CLAUDE_CONFIG_DIR`, else `~/.claude`). Every section may carry an `_about` line; code ignores keys starting with `_`. The send option defaults are the owner's choice; the other values are defaults the owner may change.
- `server.py` (standard library `ThreadingHTTPServer`): exits if `host` is not local; rejects any request whose Host or Origin is not `127.0.0.1`, `localhost` or `::1`. Routes: `GET /` redirects to the page; `GET /<page>`, `/<data>`; `GET /real-files.json` reads scanned files fresh from disk (never under `never` paths); `GET /api/health` → `{ok, server: "project-ide", agent, agent_error, repo, claude_cwd, write_through, voice, voice_max_seconds, jobs: true, send_options, summaries}`; `GET /api/store/<coll>` → `{docs: [{id, data}]}`; `POST /api/store/<coll>` → `{id}`; `PUT|PATCH /api/store/<coll>/<id>` → `{ok, written}`; `POST /api/agent` `{text, node_id, path, name, num, session, input_id, kind, delete}` → `{run}`; `GET /api/agent/<run>/events` (SSE, `id:` per event, resumable); `POST /api/agent/<run>/answer` `{id, allow}`; `POST /api/agent/<run>/stop`; `POST /api/voice` (raw audio, 25 MB at most) → `{text, model}`. The Notes and runs routes: `GET /api/jobs?offset&limit&show=all|notes|runs` → `{rows, total, offset}` (each row `type: "note"` with the note's fields, or `type: "run"` with `id, session, title, status, detail, origin, kind, tags, summary, notes, branch, cwd, steps, cost_usd, max_context, start, end, updated, live, sent, fixed`; sorted `need human` first, then `transcribing`, `queued`, `sending`, `planning`, `working`, then by `updated`, newest first; `limit` 10 by default); `GET /api/notes`; `POST /api/notes` `{text, recording, include, send_after_transcript, context}` → the note; `PATCH|PUT /api/notes/<id>` (only `text`, `include`, `send_after_transcript`, `status`); `POST /api/notes/<id>/audio` (raw audio; the note is `transcribing`, the server turns it into text in the background, then `ready`, or out at once when `send_after_transcript` is set); `POST /api/notes/<id>/cancel`; `POST /api/notes/<id>/delete` (refused while its run is at work); `POST /api/notes/send` `{ids, options, session, node}` → `{run}`; `GET /api/runs/<id>` (a run by its record id or session id: the transcript's run merged with its record); `GET /api/runs/<id>/steps/<step>` (one step in full); `POST /api/runs/<id>/summary|merge|discard|stop`. Collections are only `nodes`, `changes`, `inputs`; ids match `^[A-Za-z0-9_.:@+~-]{1,200}$`; files are written atomically. Write-through on `nodes` saves: `content` into the item's `src_file` (and `real_file`), never a text containing "…(cut for the page", never a field equal to the previous save; `how_md` into the item's How it works file next to it on disk, with front matter kept and `written` now, `by: owner`. Secrets are read from the keys file by name only; the Groq key is not passed to Claude Code.
- `claude_bridge.py`: one run per request, id `YYYYMMDD-HHMMSS-<6 hex>`, in a thread; `ClaudeSDKClient` with `cwd` from the config, `add_dirs` the repository, `setting_sources ["project", "local"]`, all skills, the `claude_code` system prompt with an appended note (work for the owner through the page; follow the system's `CLAUDE.md`, file the request, finish the round, never push, never open the keys folder; answer plainly), `allowed_tools` from `allow`, a `PreToolUse` hook and `can_use_tool` both using one check: deny anything naming a `never` path; allow exactly `git rm -r -q --ignore-unmatch <item and its metadata files>` and `rm -rf <same>` for a page deletion; ask for paths outside the repository and commands containing an `ask_owner` word. Asking emits `approval {id, tool, summary, reason}` and waits up to `approval_timeout_s`, then `answered`. Events: `start`, `text`, `tool {tool, summary}`, `approval`, `answered`, `result {text, cost_usd, duration_ms, turns, session, is_error, subtype}`, `error`, `end {changed, seconds}`. `changed` comes from git: files that differ from HEAD at the start or changed during the run, committed or not, never under `never`. Each run is logged as `<log_dir>/<YYYYMMDD>/<run>.json` with node, request, result, changed, steps and the owner's answers. The prompt names the item and, when given, the input file in the page store to mark processed. A run with notes (from `POST /api/notes/send`) gets a worktree from `worktrees.py` unless it is a delete, starts Claude Code in `.worktrees/<run>/agents/system/` with `add_dirs` the worktree, checks paths against that checkout, and its prompt says it works on its branch and must not push or merge; a follow-up with the same `session` continues on the same branch while its worktree exists and the run is not `in main` or `cancelled`. Delete and Apply changes runs work in the repository itself. The bridge writes the run record, sets `working` on the run and its notes with `sent` (`git rev-parse --short HEAD` and the page `data_version`), `planning` while the run uses the `change-plan` skill, `need human` while an Allow/Refuse waits, then at the end `cancelled` on Stop, `failed` on error, else the `STATUS:` line (`done` when there is none), and emits `status` events; when the run ends `done` with `options.merge` = `auto` it calls `merge` and sets `in main` with `fixed` and `merged`. Stop works before Claude Code has connected. A start that fails removes its new worktree. After each page run it asks `run_summary.py` for the summary.
- `notes.py` (class `Jobs`): a note is `apps/project-IDE/data/page-store/notes/<id>.json`, id `YYYYMMDD-HHMMSS-<6 hex>`:

  ```json
  {"id": "20261015-093104-a1b2c3", "text": "the Details tab should show the status first", "status": "ready",
   "include": true, "send_after_transcript": false,
   "context": {"where": "selection", "path": "apps/project-IDE/server/README.md", "node_id": "apps/project-IDE/server/README.md",
               "name": "README.md", "tab": "File", "selection": "\"status\": \"proposed\"", "line": 12, "page_version": 75,
               "recorded": false, "at": "2026-10-15T09:31:04Z"},
   "created": "2026-10-15T09:31:04Z", "updated": "2026-10-15T09:31:04Z", "run": null, "error": null,
   "sent": {"at": "...", "commit": "3f2a1c9", "data_version": 75}, "fixed": {"at": "...", "commit": "8b0d2e4", "data_version": 76}}
  ```

  `context.where` is `ask box`, `notes panel` or `selection`; `sent` and `fixed` are null until set. A run record is `agents/system/logs/subagents/project-ide-agent/runs/<run>.json` with `id, origin (page|terminal), kind (notes|request|delete|sync), session, status, status_detail, request, node, notes (ids), options, worktree {branch, path, base}, started, ended, sent, fixed, merged, result {cost_usd, duration_ms, turns}, answer, changed, branch_state {head, commits, dirty}, summary, tags, summary_error, error, updated`. Statuses, for notes and runs: `transcribing, ready, queued, sending, planning, working, need human, need manual test, done, in main, failed, cancelled`. `combine(notes, options)` makes one request: per note a heading `Note <i> (id <id>), typed|recorded by voice on <path>, <tab> tab, from the <where>:`, the selected text with its line in a `~~~text` fence, the note's text in a `~~~text` fence; then the options as instructions (the tests to run; with `bug_check`, review the whole diff and fix what is found; with `report`, end with a "Report" heading; commit on the current branch, never push, never merge into main); and last: the final line of the answer is exactly `STATUS: done`, `STATUS: need manual test: <what to try>` or `STATUS: need human: <what it needs>`. `read_status` takes the last such line. On start, `recover` turns notes and page runs left `sending`, `planning`, `working` or `need human` (and notes left `transcribing`) into `failed` with the reason. Git ignores both folders; the run that takes a note files its words as an owner input.
- `runs.py` (class `Transcripts`): reads `<claude_config_dir>/projects/<folder>/<session>.jsonl` for every folder whose sessions' `cwd` is inside the repository, and subagents from `<session>/subagents/agent-<id>.jsonl`. A list row: `id` (session), `title` (Claude Code's ai-title, else the first prompt, 90 characters), `origin` (`page` when the entrypoint starts with `sdk`, else `terminal`), `cwd`, `branch`, `model`, `start`, `end`, `steps`, `max_context`, `live` (file changed in the last `live_seconds`). A run adds `steps`, each `{id ("3", or "5.2" inside a subagent), kind, tool, at, ms, summary, input, output, more, error, context, out_tokens}` with `kind` one of `prompt, notification, text, read, edit, command, skill, subagent, mcp, web, workflow, tool` (Read/Glob/Grep/LS are read, Edit/Write/MultiEdit/NotebookEdit edit, Bash command, Skill skill, Agent/Task subagent, `mcp__*` mcp, WebFetch/WebSearch web, Workflow workflow); input and output cut to `max_text` characters with `more` set; `context` is the input plus cache tokens of that message; a subagent step holds its own `steps`. Also `totals {tools, skills, subagents, mcp, plugins, workflows, web, read, edited}`, `checks` (command steps running `build_map.py`, `check_tree.py`, `check_page.js`, `rebuild.py`, `./start.sh` or a test runner), `plans` (files edited in `apps/project-IDE/data/plans/`), `commits` (made in the repository between start and end), and the cost only when the record has it. It never writes.
- `run_summary.py`: `TAGS = question, change, fix, docs, ui, server, setup, sync, plan, research, delete, failed, waiting`; the brief is the title, folder, branch, first request (6,000 characters), one line per step (160 steps at most), the answer and the files changed; it calls the Agent SDK with `model` = `runs.summary_model`, a short system prompt (write 4 to 10 ASD-STE100 sentences: what was asked, what was done, what changed, the checks, what is open; 1 to 4 tags from the list, a new lowercase one only if none fits; answer JSON `{"summary", "tags"}`), from a temporary folder outside the repository with no setting sources, so it loads no project settings and its own transcript never lists as a run. It writes `summary` and `tags` (or `summary_error`) into the run record. It runs after each page run, in the background for finished terminal rows shown in the list that have no summary, and on `POST /api/runs/<id>/summary`.
- `worktrees.py` (class `Worktrees`): `create(run, subject)` makes branch `ide/<YYYYMMDD-HHMM>-<slug of the subject, 40 characters>` (with `-2`, `-3` when taken) from `main` and `git worktree add .worktrees/<run>`; returns `{branch, path, base}`. `update(run)` commits anything left uncommitted on the branch, merges `main` into it, and when the only conflicts are the built files (`apps/project-IDE/current-ui/file-tree.data.json`, `apps/project-IDE/current-ui/real-files.json`, `docs/file-tree.md`) takes main's side and runs `rebuild.py` in the worktree, else aborts and raises. `merge(run)`: `update`, check that the repository is on `main`, `git checkout --` the three built files in the repository, `git merge --ff-only <branch>`, then `rebuild.py` in the repository; returns `{commit, from, branch}`. `remove(run, branch, delete_branch)` and discard remove the worktree and the branch. It never pushes.
- `voice.py`: posts multipart audio to the configured URL with the key as a bearer token; tries the models in order; a 429 parks a model for its `retry-after` (5 to 3,600 seconds); an error moves on; keeps nothing.
- `README.md`: what you need, how to start (`./init.sh` once, then `./start.sh`, with its four steps and its other commands; the manual way `python3 apps/project-IDE/server/server.py` from the repository top), the SSH tunnel, what happens for each page action (the ask box, Notes and runs, statuses, each run's branch and merge, the page of a run, voice), the settings table, the files.
- `.gitignore` (at the top of the repository, built by the project prompt) must also hold `.worktrees/` and `apps/project-IDE/data/page-store/notes/`.

Check: start the server, open `http://127.0.0.1:8765/`; the header says "on your server"; a comment creates `page-store/nodes/<id>.json`; a File edit changes the file on disk; a request lists the system's agents; a `git push` waits for Allow; two notes sent together make one run on a branch `ide/...` in `.worktrees/`, which ends `done` and, with Auto merge, `in main`; a Stop right after sending ends `cancelled`; the run list shows this repository's terminal sessions; a run page opens at `#run/<id>` with its steps; a summary is written for a small run.

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
7. Write the server files (`server.py`, `claude_bridge.py`, `voice.py`, then `notes.py`, `runs.py`, `worktrees.py`, `run_summary.py`) and their README, then `start.sh` and `init.sh` at the top of the repository, and the panel and run page on the page. Check: the server checks and the start-script checks above, and `check_page.js` on the server page with the panel open and a run page, at desktop and phone width.
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
- On the server, the Notes and runs panel lists this repository's terminal sessions; two notes sent together run as one run on its own `ide/...` branch in `.worktrees/`, end with a `STATUS:` line, and with Auto merge reach `main` without a push; a conflict outside the three built files stops at `need human`; `git status` never lists `.worktrees/` or `page-store/notes/`.
- Nothing on the panel or a run page is wider than a 390 px screen, in light and dark.

## Do not build

- Custom views (`<family>.<type>.<name>.view.html` and shared views): designed but not built; leave the page's current extra tabs in place. Where shared views live is open.
- Tabs read from real files (Example from `x.example.md`, Questions from `x.questions.md`, an ASD-STE100 tab from `README.asd.md`, shown only when the file exists): stage one work, not built yet; keep today's tabs until it is done.
- Filled Details files everywhere: leave empty templates where nothing is known.
- A scheduled routine that syncs the page store without Apply changes: a proposal, not built.
- Updating the published claude.ai page after work on the server: open.
- Installing Chromium's system libraries on the owner's server (`sudo npx playwright install-deps chromium`): only the owner runs it. Do not install them yourself.
- Item statuses other than "changed": not built until the owner asks. Notes and runs have their own statuses (built).
- Pull requests from a run (a `run_pr.py` that pushes the branch, opens and merges a pull request with `gh`): not built; when is open. Render Make PR and Make PR and merge disabled; a merge stays local and nothing is pushed.
- The Cloud send option (a run in a Claude Code cloud session): render it disabled; it needs its own plan.
- Putting run records in git: not built; they stay in the logs folder (default, the owner may change it).
- Any file under the prediction-market domain other than its folders: stage two.
