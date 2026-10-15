# Plan: one panel for AI notes and runs, with a page for every run

Status: waiting (second version, with the owner's answers) · Request: in-20261015-0925 · Updated: 2026-10-15

## The request

The owner wants every AI note to become a job they can follow. Today a note works only inside the box at the bottom of one file or folder, and it is gone from view once sent. They asked for:

- a notifications panel in the header, hidden or shown with a toggle button, where each note is a row: "I can cancel them, delete, I can send them, I can edit them after transcribe";
- statuses "transcribing, sending, working, done";
- "send all" at the bottom, and checkboxes to leave a note out; "when i send all or selected it combine in one and tracking it all in one run";
- "from which version it sends and in which it was fixed";
- the note's details and context: where it was recorded or sent, the text selected on the page, more context later;
- a "send after transcript" button; the text box grows with the message, in the panel and at the bottom of the page;
- runs from Claude Code in the terminal in the same list, the current one too, and "add last 3 runs already there including this one";
- a page for every run: "all details about this run step by step" with collapsible steps: files read, skills, subagents, MCP, tools, plugins, workflows, files changed, the context at every step, the input and output of each tool and subagent, the request and the answer, git status, workspace and branch, test data, the plan if there is one, a summary in ASD-STE100, tags such as "question", and buttons "make PR" and "make PR and merge";
- select text on a file or folder page, press record, and the selection goes with the note as context.

## What it is for

The owner works by talking to the system. Right now a spoken or typed note disappears into one item's chat, and a run is a stream of one-line steps that is gone after a reload. After this change every note and every run, from the page or from the terminal, is one row in one list. The owner sees what is waiting, what is working and what is done, can batch notes into one run, and can open any run to see exactly what the agent read, used, changed and spent, then turn its commits into a pull request with one click.

## What exists today

- **The ask box** at the bottom of each item sheet (`file-tree-explorer.html`, `#ask`, one row high). On the server it sends one request to `POST /api/agent`, and the chat shows the run's events from `GET /api/agent/<run>/events`. The conversation is kept per item in the browser only.
- **Voice input** (`voice.py`, the microphone button): the recording is turned into text by Groq and the text is put into the box. Nothing shows while it transcribes except "Writing…" on the button.
- **Runs** (`claude_bridge.py`): one Claude Code session per request. Its events live in memory until the server restarts; a short log (`request`, `result`, one line per step, `changed`) is written to `agents/system/logs/subagents/project-ide-agent/<day>/<run>.json`, which git ignores.
- **Claude Code's own transcripts.** Every Claude Code session, from the page or from a terminal, writes its full transcript to `$CLAUDE_CONFIG_DIR/projects/<folder>/<session>.jsonl`: every message, every tool call with its input and output, the token use of every step, and the subagents' transcripts in `<session>/subagents/`. For this repository there are five such folders. The newest sessions are this one (`252b08b9`, 2026-10-15, started in `agents/system/`), `524693f7` (2026-10-13, started at the top) and `6307c1fb` (2026-09-29, the prediction-market research).
- **The page store** on the server: `apps/project-IDE/data/page-store/<collection>/<id>.json`, collections `inputs`, `nodes`, `changes`.
- **Git and GitHub.** Runs from the page commit on `main` on the server and never push. `gh` is installed but not signed in.

## The change

### 1. Notes: one record per note, in the page store

A note is anything the owner says or types to Claude Code on the page: the ask box, the microphone, the delete note. Each note is a file `apps/project-IDE/data/page-store/notes/<id>.json`:

```json
{
  "id": "20261015-0931-a1b2c3",
  "text": "the Details tab should show the status first",
  "status": "ready",
  "include": true,
  "send_after_transcript": false,
  "context": {
    "where": "ask box",
    "path": "apps/project-IDE/current-ui/file-tree-explorer.html",
    "tab": "Details",
    "selection": {"text": "\"status\": \"proposed\"", "line": 6},
    "recorded": true,
    "at": "2026-10-15T09:31:04Z"
  },
  "sent": {"at": null, "commit": null, "data_version": null},
  "run": null,
  "fixed": {"commit": null, "data_version": null}
}
```

**Statuses** (the owner's list, with `queued` and `sending` added for the moments between):

| Status | Meaning |
|---|---|
| `transcribing` | The recording is with Groq. The row shows a spinner. |
| `ready` | The text is in. The owner can edit it, send it or leave it. |
| `queued` | It goes out by itself when its text is in ("Send after transcript"). |
| `sending` | It is on its way to the server. |
| `planning` | Its run is writing a plan (the `change-plan` skill), before it builds. |
| `working` | Its run is building. |
| `need human` | The run cannot go on without the owner: an Allow or Refuse button, a plan that waits for "go", or a question. These rows go to the top. |
| `need manual test` | The run is finished, but says that a person must try the change, and what to try. |
| `done` | The run is finished and its branch is ready. It is not in `main` yet. |
| `in main` | Its branch is merged into `main`, and the server has pulled it. |
| `failed` | The transcript or the run failed. The row says why and offers to retry. |
| `cancelled` | The owner cancelled it. A cancelled run is stopped and its worktree removed. |

A run has the same statuses from `planning` on. The run tells its own state: it ends its answer with one line, `STATUS: done`, `STATUS: need manual test: <what to try>` or `STATUS: need human: <what it needs>`, and the server reads that line.

**Versions.** When a note is sent, it records the commit of `main` (`git rev-parse --short HEAD`) and the page data version it was sent from. When its run is merged, it records the commit on `main` that holds the fix and the data version built from it. The row shows, for example, "sent at 3f2a1c9 · page v75 → in main at 8b0d2e4 · page v76". Before the merge it shows the run's branch and last commit.

### 2. The panel in the header

A new header button, **Notes and runs**, shows the number of active rows. It opens and closes the panel; the page remembers whether it was open.

```text
┌ Notes and runs ─────────────────────────────────────────────── [Hide] ┐
│ [All] [Notes] [Runs]                                                  │
│ ☑ ● ready        docs/README.md                           09:31       │
│     "the second table should list the server too"                     │
│     [Edit] [Send] [Delete]                                            │
│ ☑ ◌ transcribing apps/project-IDE/server   (selection: line 12)       │
│     [Send after transcript] [Cancel]                                  │
│ ☐ ● ready        agents/system/CLAUDE.md                  09:28       │
│ ─ ▶ working      run 0931 · 2 notes · page · 1m 12s     [Stop]        │
│ ─ ✓ done         run 252b08b9 · terminal · #setup #question · $1.84   │
│                                                                       │
│                        [Send selected (2)]  [Send all]                │
└───────────────────────────────────────────────────────────────────────┘
```

- **A note row** shows its checkbox, status, the path it came from, its time and its text, and its buttons: Edit (the text becomes a box that grows with the text), Send, Send after transcript (while it transcribes), Cancel, Delete. A click on the row opens the note's details: its full text, its context (where it was recorded or sent, the tab, the selected text and line, the time), its versions and its run.
- **A run row** shows its status, where it came from (page or terminal), its notes, its tags, its time and its cost, with Stop while it works. A click opens the run's page (section 4).
- **The order:** rows that need the owner first, then the rows at work, then the rest by the time they last changed, newest first. The panel shows 10 rows, with **Show more** for the next 10.
- **The send options**, above Send all, remembered by the page:
  - **Where:** *Local* (default): a new worktree on this server. *Cloud*: shown but off, for a later plan.
  - **Merge:** *Ask me* (default): the run stops at `done` and waits for the PR buttons. *Auto merge*: the run opens the pull request and merges it when its checks pass.
  - **Tests:** *Related* (default): the checks of the build and the tests of the files the run changed. *All*: every check and test there is. *None*.
  - **Check for bugs:** off by default. When on, the run reviews its own diff with the `code-review` skill before it finishes, fixes what it finds, and lists the rest.
  - **Report:** on by default. The run writes a short report (what was asked, what changed, the checks and their results, what is left) that goes on the run page and in the pull request.
- **Send selected** and **Send all** combine the chosen notes into one request and start one run. Each note goes in with its own context, so Claude Code knows which file each one is about. The run row lists the notes it carries, and each note row links to the run.
- The ask box at the bottom of an item, and the edit box of a note, grow with the text up to half the screen height.
- Sending from the ask box works as today, and the note also appears in the panel.
- The panel is a part of the server page only. Opened anywhere else, the header button is hidden.

### 3. Recording with the selected text

When the owner selects text on an item's sheet (File, How it works, Questions or another tab), a small **Record about this** button shows next to the selection, with **Note** next to it for typing. The note keeps the selected text, its line when the tab shows lines, the tab and the item's path as its context. The microphone in the ask box also takes the selection when one exists.

### 4. Runs: every Claude Code session for this repository

**Where the details come from.** The server reads Claude Code's own transcripts on demand and copies nothing. A new file, `apps/project-IDE/server/runs.py`, finds the transcript folders of this repository (every folder under `$CLAUDE_CONFIG_DIR/projects/` whose path is inside the repository) and turns a transcript into a run. Runs started from the page are the same sessions, so they are read the same way. A small record per run holds what the transcript lacks: status, notes, versions, tags, summary and pull request. It goes in `agents/system/logs/subagents/project-ide-agent/runs/<session>.json`, which git ignores.

**The list** shows the 50 newest runs, newest first. The three runs the owner asked for are already there, because they are the newest transcripts: this session, `524693f7` and `6307c1fb`. A terminal session that is still being written shows as working.

**The run page** opens in the place of the item sheet, at the address `#run/<session>`:

- **Header:** the title (the first request, shortened), its status, page or terminal, where it started (folder, branch, workspace), the start time, the length, the cost, the model, and the tags.
- **Summary:** five to ten short sentences in ASD-STE100: what the owner asked, what the agent did, what changed, what is still open.
- **Request and answer:** the first message in full, and the last answer in full.
- **Git:** the branch and the commit at the start and at the end, the commits the run made, and the files it changed, each with a link to its item in the tree. The current `git status`, if files are still not committed.
- **Totals:** the files read, the skills, the subagents, the MCP servers and their tools, the tools, the plugins and the workflows used, each with a count. A click on one filters the steps.
- **Steps:** one collapsible row per step, in order. Each row has an icon by kind (read, edit, command, skill, subagent, MCP, web, workflow, text), a one-line summary, the time and the context size at that step (the tokens the model had in view, from the transcript's usage numbers), shown as a small bar. Opened, a step shows its full input and its output, shortened to the first 200 lines with a button for the rest. A subagent step opens into the subagent's own steps, from its transcript.
- **Checks and test data:** the build and check commands the run ran (`build_map.py`, `check_tree.py`, `check_page.js` and any test) with their results, taken from the steps.
- **Plan:** when the run wrote or changed a plan in `apps/project-IDE/data/plans/`, a link to it and its status.
- **Notes:** the notes the run carried, with their context.
- **Buttons:** Make PR, Make PR and merge (section 6), Stop while it works, Copy the session id to continue it in a terminal (`claude --resume <id>`).

**Tags.** One to four short tags per run, from a fixed list first, with a new tag only when none fits: `question`, `change`, `fix`, `docs`, `ui`, `server`, `setup`, `sync`, `plan`, `research`, `delete`, `failed`, `waiting`.

**Summary and tags are written by a small model** after a run ends: Claude Haiku reads the request, the answer, the list of steps and the files changed, and returns the ASD-STE100 summary and the tags (about one cent a run). For a terminal run, it runs when the page first opens it. The summary can be written again with a button.

### 5. The server

| Route | What it does |
|---|---|
| `GET /api/notes`, `PUT`, `PATCH /api/notes/<id>` | The page store's `notes` collection, as today's store routes. |
| `POST /api/notes/send` with `{"ids": [...]}` | Combines the notes into one request and starts one run. Sets each note to `sending`, then `working`, and records the versions. |
| `GET /api/runs` | The run list: the newest 50, from the transcripts and the run records. |
| `GET /api/runs/<session>` | One run in full, with its steps and subagents. |
| `GET /api/runs/<session>/steps/<n>` | The full input and output of one step, for long ones. |
| `POST /api/runs/<session>/summary` | Writes the summary and tags again. |
| `POST /api/runs/<session>/pr` with `{"merge": false}` | Makes the pull request (section 6). |

New files, one job each: `runs.py` (transcripts into runs), `notes.py` (notes, statuses, combining, versions), `run_summary.py` (summary and tags with the small model), `run_pr.py` (pull requests). `claude_bridge.py` takes a list of notes in one run, writes the run record and sets each note's status as the run moves. `voice.py` is unchanged; the page creates the note before it sends the recording.

### 6. Where a run works, and pull requests

**Each run from the page works in its own git worktree,** so several runs can work at the same time and none of them touches the files the server shows:

1. The server makes a branch `ide/<date>-<subject>` from the current `main`, and a worktree for it in `.worktrees/<run>/` at the top of the repository (git ignores this folder, so the tree on the page does not list it).
2. Claude Code starts in `.worktrees/<run>/agents/system/`, so it loads the same `CLAUDE.md`, skills and agents. It does the work and commits on the branch. It never pushes.
3. When it ends at `done`, the run page shows its branch, its commits and its diff.
4. **Make PR** pushes the branch and opens a pull request into `main`, with the report as its description. **Make PR and merge** also merges it. With *Auto merge* chosen at send time, the run does both by itself when its checks pass. The merge happens on GitHub, outside this server; the button or the option is the owner's word for that one run.
5. After a merge the server pulls `main`, rebuilds the page and marks the run and its notes `in main`. The worktree is removed.

**Built files.** Every run rebuilds the page data, so two branches always differ in `file-tree.data.json`, `real-files.json` and `docs/file-tree.md`. Before it pushes, the server brings the branch up to date with `origin/main`; when only these built files conflict, it rebuilds them and commits the result. Any other conflict stops the run at `need human`.

**GitHub.** `git push` already works on this server. Opening and merging a pull request uses the `gh` command, which is installed but not signed in; the owner signs it in once with `gh auth login`.

**The cloud.** Running a note in a Claude Code cloud session (claude.ai/code) is shown as an option but stays off in this plan: it needs its own plan for how the cloud session gets the note and how its result comes back.

**Edits on the page stay as they are.** An edit the owner makes on the page itself (a file's text, a How it works) is still written straight into the files on `main`, as now. Only the runs work in worktrees.

## Choices for the owner

Answered by the owner on 2026-10-15 (in the plan's Questions file and in the chat):

1. **Summary and tags:** Claude Haiku after each run.
2. **Pull requests:** each run in its own worktree and branch, local by default, the cloud later; Make PR and Make PR and merge; the send options auto merge, tests, check for bugs and report.
3. **Run records:** not answered; the recommended default holds: they stay in the logs folder, out of git.
4. **Terminal runs:** 10 shown, with Show more; runs that need the owner first, then the newest.
5. **Statuses:** the owner's list, with `queued` and `sending` added.
6. **Browser test:** the owner installs the Chromium libraries.

Still open, with the default the build follows:

7. **Send options' defaults:** Local, Ask me before merging, Related tests, no bug check, report on.
8. **Worktree folder:** `.worktrees/` at the top of the repository, ignored by git. Other option: a folder next to the repository, `../trading-oss-worktrees/`.

## Steps

1. **Run reader.** `runs.py` reads a transcript into a run with steps, subagents, totals, files and context sizes. Check: it reads the three newest sessions, the step counts match the transcripts, and this session shows the Bash, Edit, Write, Skill and Agent steps and the knowledge-base agent's steps inside the Agent step.
2. **Worktrees.** `worktrees.py` makes the branch and worktree for a run, lists them, removes them, and brings a branch up to date with `origin/main`, rebuilding the built files when only they conflict. Check: on a copy of the repository, two worktrees at once, then an update with a conflict in `file-tree.data.json` only.
3. **The bridge.** `claude_bridge.py` starts a run in its worktree with many notes and the send options in its prompt, writes the run record, reads the `STATUS:` line, and sets each note's status as the run moves. Check: one test run with two notes on a test branch ends `done` or `need manual test`, both notes point to it, and its versions are filled.
4. **Notes.** `notes.py` and the routes. Check: create, edit, send, cancel and delete through the routes on a copy of the store; sending two notes starts one run; cancelling a working run stops it and removes its worktree.
5. **Summary and tags.** `run_summary.py`. Check: the summary of this session is in ASD-STE100, under 200 words, with tags from the list.
6. **Pull requests.** `run_pr.py`: push, open, merge, then pull `main`, rebuild and mark `in main`. Check: on a test repository with a local bare remote, everything but the `gh` calls; then one real pull request after the owner signs in `gh`.
7. **The panel** on the page: the button, the rows in their order, 10 with Show more, statuses, edit, send, send after transcript, checkboxes, the send options, Send selected and Send all, note details, growing text boxes. Check: `check_page.js` with new checks for the panel at desktop and phone width, in light and dark; nothing wider than the phone.
8. **The run page:** header, summary and report, git and branch, totals, collapsible steps, subagents, checks, plan, notes, PR buttons. Check: this session's page opens at `#run/252b08b9-...` and shows its steps; screenshots at both widths.
9. **Record with the selection.** Check: selecting text on a File tab and pressing Record makes a note whose context has the text and line.
10. **The editor bug.** The page's in-place editor turned a file name in a heading into an `http://` link when the owner saved a Questions file. Find the cause in the Markdown round trip and fix it. Check: saving a heading with a file name keeps it as plain text.
11. **Build, restart and look.** `./start.sh`, then the owner opens the page. Check: health is ok, the three runs are in the list, and a recorded note goes from `transcribing` to `done`.
12. **Distribute** the knowledge (below), rebuild, commit.

## What it touches

- The page: `apps/project-IDE/current-ui/file-tree-explorer.html`.
- The server: `server.py`, `claude_bridge.py`, `server.config.json` (transcript folders, summary model, worktree folder, send option defaults), and the new `runs.py`, `worktrees.py`, `notes.py`, `run_summary.py`, `run_pr.py`, each with its How it works and Details files.
- `.gitignore` (`.worktrees/`) and `start.sh` (it removes worktrees whose run is gone).
- The page store: a new `notes` collection; the `ide-sync` skill (notes are owner inputs: a sync files the notes that are done and clears them).
- The build check: `agents/system/.claude/skills/ide-build/scripts/check_page.js` (panel and run page checks).
- The docs: `apps/project-IDE/server/README.md`, `apps/project-IDE/docs/vision.md`, `README.md`, `README.asd.md`, `rebuild-prompt.md`, the apps and project READMEs where they list the server's files, and `docs/metadata.md` only if the notes collection counts as owner inputs there.
- The records: `decisions.md`, `changelog.md`, `plans/index.json`.

## Where the knowledge goes once built

- **How the panel and the run page work, for the owner:** `apps/project-IDE/docs/README.md`, new parts "Notes and runs" and "The page of a run", and its ASD-STE100 twin.
- **Why:** one sentence in `apps/project-IDE/docs/vision.md`: every note and every run, from the page or the terminal, is one row the owner can follow, batch and open.
- **The routes, files and settings:** `apps/project-IDE/server/README.md`, and each new file's How it works.
- **The exact formats** (the note record, the run record, the statuses, the `STATUS:` line, the send options, the step kinds, the tag list, the routes): `apps/project-IDE/docs/rebuild-prompt.md`.
- **How runs use worktrees and branches:** `apps/project-IDE/docs/README.md` and `agents/system/CLAUDE.md` (a run from the page commits on its own branch, never on `main`).
- **Notes as owner inputs at a sync:** `agents/system/.claude/skills/ide-sync/SKILL.md`.

## Log

- 2026-10-15 09:25: request filed (in-20261015-0925).
- 2026-10-15 09:40: plan drafted and shown to the owner (waiting).
- 2026-10-15 10:05: the owner answered in the Questions file and the chat. Second version: worktree per run, send options, the owner's statuses, 10 runs with Show more, Haiku summary, the editor bug. Shown again (waiting).

## Plan in ASD-STE100

**Goal.** Show every note and every run in one panel. Give each run a page with all of its steps. Each run works in its own worktree, so many runs can work at the same time.

**Decisions of the owner.**

1. Claude Haiku writes the summary and the tags after each run.
2. Each run works in its own worktree and branch. The default place is local. The cloud comes in a later plan.
3. The owner chooses options when they send notes: merge, tests, check for bugs, and report.
4. The panel shows 10 rows. "Show more" shows 10 more. Rows that need the owner go first.
5. The statuses are: transcribing, ready, queued, sending, planning, working, need human, need manual test, done, in main, failed, cancelled.
6. The owner installs the Chromium libraries on the server.

**Open choices.** The build uses these defaults if the owner does not choose:

1. Send options: Local, "Ask me" before a merge, related tests, no bug check, report on.
2. The worktree folder is `.worktrees/` at the top of the repository. Git ignores this folder.

**Procedure.**

1. Write `runs.py`. It reads a Claude Code transcript and makes a run with steps. Check: the three newest sessions show the correct number of steps. Risk: a new version of Claude Code can change the transcript format.
2. Write `worktrees.py`. It makes a branch and a worktree for each run, and it removes them. It updates a branch from `origin/main`. Check: make two worktrees on a copy of the repository. Risk: two branches change the same file. The built files are rebuilt. Other conflicts stop the run with the status "need human".
3. Change `claude_bridge.py`. It starts each run in its worktree, sends many notes in one run, keeps a run record, and reads the `STATUS:` line at the end of the run. Check: one test run with two notes ends with "done" or "need manual test". Risk: a test run costs money.
4. Write `notes.py`. Add the note routes to `server.py`. Check: create, edit, send, cancel and delete a note on a copy of the store.
5. Write `run_summary.py`. It writes the ASD-STE100 summary and the tags with Claude Haiku. Check: the summary of this session has less than 200 words. Risk: a small cost for each run.
6. Write `run_pr.py`. It pushes the branch, opens the pull request, and merges when the owner asks. Then it pulls `main`, rebuilds the page and sets the status "in main". Check: test it with a local test remote. Then make one real pull request. Risk: a merge acts outside this server. Only the owner's button or the "Auto merge" option starts it. The owner must sign in `gh` one time.
7. Add the panel to `file-tree-explorer.html`. Check: `check_page.js` at desktop width and phone width, in light and dark. Risk: the page is large, so a change can break other parts.
8. Add the run page. Check: the page of this session opens and shows its steps.
9. Add "Record about this" for selected text. Check: the note keeps the selected text and the line number.
10. Repair the editor bug. The editor changed a file name in a heading into an `http://` link. Check: a saved heading keeps the file name as plain text.
11. Run `./start.sh`. Open the page. Check: the list shows the three runs. A recorded note goes from "transcribing" to "done".
12. Write the docs and the metadata. Rebuild the page. Commit and push.
