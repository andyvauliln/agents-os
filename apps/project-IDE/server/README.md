# The project IDE on your server

This folder runs the File Tree page on your own machine, with Claude Code behind its request box. It is the same page as on claude.ai. Here it reads the repository directly, writes your edits into the repository, sends what you type or say to Claude Code working in the project, and shows every note and every Claude Code run in one panel, each run on its own branch until it is merged into `main`.

## What you need

- The repository cloned on the server, with a way to push.
- Python 3.10 or newer, Node, and Claude Code with its SDK: `npm install -g @anthropic-ai/claude-code`, and the Python package `claude-agent-sdk`, which `./init.sh` installs into `.venv/` at the top of the repository (git ignores that folder).
- A way for Claude Code to sign in. Either put an API key in the keys file `.secrets/test/.env` as `ANTHROPIC_API_KEY=...`, or sign Claude Code in once with `claude` in a terminal. The settings name the key; its value never leaves the keys file.
- For voice input, a Groq key in the same keys file as `GROQ_API_KEY=...` (free at console.groq.com). Without it the microphone button stays hidden.

## Start it

Run once, from the top of the repository:

```bash
./init.sh
```

It checks the tools (git, curl, Python 3.10 or newer, Node, Claude Code), makes `.venv/` with the SDK of the request box, installs a systemd user service named `project-ide` that starts the IDE when the server boots, and then runs `./start.sh`. It is safe to run again. `./init.sh --no-service` does the same without the service. If the server does not keep user services running before you log in, it tries `loginctl enable-linger` or prints the `sudo` command to run.

After that, start or restart the IDE with:

```bash
./start.sh
```

Each start does four things in order:

1. **Sync.** It fetches from GitHub. When the branch is behind, it first puts back the three built files (the page data, `real-files.json` and `docs/file-tree.md`, which the rebuild makes again), then moves the branch forward, but only when no other file has local changes and there are no local commits. Otherwise it skips the pull with a warning; it never merges, stashes or pushes. It also says how many items on the page are marked changed and waiting; it does not sync them itself, so press Apply changes on the page or say "sync the file tree" to Claude Code.
2. **Stop.** It stops the service and any server still running from a start by hand, but only a process running `apps/project-IDE/server/server.py`, never another program on the port.
3. **Rebuild.** It rebuilds the page data. When nothing changed, the data keeps its version, so a restart leaves git clean.
4. **Start.** It starts the service, or a background process when no service is installed, shows its output, waits until the server answers its health check, and prints the address and the tunnel command.

Other commands: `./start.sh --no-pull` (the same without the sync), `./start.sh stop`, `./start.sh status` (the service and the health check), `./start.sh logs` (follow the server's output) and `./start.sh serve` (the sync, the stop and the rebuild, then the server in the foreground; this is what the service runs). Without the service, the output and the process id go to `agents/system/logs/services/project-ide/`, which git ignores. The scripts use `.venv/bin/python` when it exists, and the port from `server.config.json` or `IDE_PORT`.

The manual way still works: `python3 apps/project-IDE/server/server.py` from the top of the repository, stopped with Ctrl+C. Use it only when the service is stopped.

The server listens only on the machine itself, at `127.0.0.1:8765`. From your own computer, open a tunnel and then the page:

```bash
ssh -N -L 8765:127.0.0.1:8765 you@your-server
# then open http://127.0.0.1:8765/ in the browser
```

The header of the page says "on your server" when it found the service.

Never open the port to the internet or put the service behind a public address. Whoever can reach the page can make Claude Code change files and run commands. The server refuses to listen on any address but the machine's own.

## What happens when you use it

- **Comments and edits** are saved at once as small JSON files in `apps/project-IDE/data/page-store/`, so they are in the repository and nothing waits on claude.ai. An edit to a file's text is also written straight into that file in the repository, and an edit to How it works into the item's `.index.md` next to it.
- **A message in the ask box** becomes a note in the Notes and runs panel and goes out at once as its own run. Claude Code loads the system's `CLAUDE.md`, agents and skills as its own, so it works by the same rules as every other Claude on the project: it files your words, does the work, rebuilds the page and commits. The chat shows each step while it works, then the answer with its cost and time. A follow-up in the same box continues the same conversation, on the same branch.
- **Notes and runs**, the button in the header, opens a panel with every note and every Claude Code run in this repository, from the page or from a terminal. The button shows how many are at work, or "N need you" in red. Rows that need you come first, then the ones at work, then the newest; 10 show at a time, with Show more. You add a note in the box at the top of the panel (Ctrl+Enter), by the microphone there, or by selecting text on an item's sheet and pressing "Record about this" or "Note", which keeps the selected text, its line, the tab and the item. A note can be edited, sent, cancelled or deleted, and its Details say where it came from and which versions it was sent from and merged at. Send all sends every checked ready note together as one run. The send options above it (Where: Local, Cloud later; Merge: Auto merge or Ask me; Tests: Related, All or None; Check for bugs; Report) start as `send_options` in `server.config.json` and are remembered in your browser.
- **Statuses.** A note or a run is transcribing, ready, queued, sending, planning, working, need human, need manual test, done, in main, failed or cancelled. A run says how it ended on its last line (`STATUS: done`, `STATUS: need manual test: ...` or `STATUS: need human: ...`), and the server reads it. After a restart, notes and runs that were at work show as failed.
- **Each run from the page works on its own branch.** The server makes the branch `ide/<date>-<subject>` from the last commit of `main`, in a worktree in `.worktrees/<run>/` at the top of the repository (git ignores it), and Claude Code starts in its `agents/system/`. So several runs can work at once, and none touches the files the server shows. Your page edits not yet committed are not in the run's branch. When a run ends done with Auto merge, or when you press **Merge into main** on its page, the server brings the branch up to date with `main` (a conflict only in the built files is solved by building them again; any other conflict stops with "need human"), moves `main` forward here and rebuilds the page. Nothing is pushed. **Discard the branch** removes it without merging. Delete and Apply changes still work in the repository itself.
- **The page of a run** opens from its row, in place of the item's sheet: the summary in ASD-STE100 (written by Claude Haiku for about half a cent to one cent, again with Write it again), the request, the answer, the notes, the send options, the git state, what it used, the checks, the plan, and every step, which opens to show its input and output. Copy gives `claude --resume <session>` to go on in a terminal. Make PR and Make PR and merge are shown but off: pull requests come in a later step.
- **Delete** next to a file's or folder's name opens a short form with an optional note for Claude, such as what to move or keep first. Claude Code deletes the item and its How it works file straight away, then cleans the project of it: its place in the notes, links to it and mentions of it in other files. It keeps your note in mind, files the deletion and commits. The item stays on the page, struck through, until the next sync, and "Bring it back" undoes it the same way.
- **Voice input**: the microphone in the ask box, in the panel and on "Record about this" records you, up to 5 minutes, with a timer; press it again to stop. The recording becomes a note at once, with the status transcribing; the server sends it to Groq in the background and the text comes into the note, which you edit in the panel. "Send after transcript" sends it by itself when the text is in. The microphone in the delete note box adds the text to that box instead. If one Groq model hits its rate limit or fails, the next one in `server.config.json` is tried. The recording is not kept. Whisper may write a few words, such as "Thank you.", for a silent recording. The browser asks once for the microphone; open the page as `127.0.0.1` or `localhost`, since browsers allow the microphone only there or over HTTPS.
- **Steps that need your click** show up in the chat with Allow and Refuse buttons: pushing to GitHub, deleting anything other than the item you deleted, installing, network tools, and anything outside the repository. Nothing from the page can open the keys folder. While one waits, the run shows as need human in the panel. A question nobody answers is refused after fifteen minutes.
- **Apply changes** at the top of the page shows how many items are marked changed. Pressing it starts one Claude Code run in the chat of the top folder: Claude Code brings everything waiting on the page into the files (the sync), rebuilds the page and commits, and the page loads the new tree.
- **The "changed" mark** shows on everything a request from the page touched: your edits and notes, new and deleted items, requests in the box, and every file Claude Code changed for you. The marks stay until the next sync.
- **Every request is logged** with its steps, answer, cost and time in `agents/system/logs/subagents/project-ide-agent/`, and every run has a record in its `runs/` folder (status, notes, branch, summary, tags). Notes wait in `apps/project-IDE/data/page-store/notes/`. Git ignores both.
- **"Sync the file tree"** typed in the box works here too: Claude Code folds what is waiting in the page store into the files, the same way it does for the page on claude.ai.

## Settings

`server.config.json`, next to this file:

| Setting | What it does |
|---|---|
| `repo` | The top of the repository, relative to this folder (`../../..`). |
| `host`, `port` | Where the service listens; only the machine's own address is accepted. |
| `page_dir`, `page`, `data` | The page and its data file. |
| `store_dir` | Where your notes, edits and messages are kept. |
| `write_through` | Write file and How it works edits straight into their files. |
| `secrets` | The keys file and the key names Claude Code gets; values stay in the keys file. |
| `claude.cwd` | Where Claude Code starts: the system folder. |
| `claude.model` | Which model; empty means Claude Code's default. |
| `claude.max_turns`, `claude.max_budget_usd` | Limits for one request. |
| `claude.allow` | Tools and commands Claude Code may use without asking. |
| `claude.ask_owner` | Words in a command that always wait for your click. |
| `claude.never` | Paths nothing may touch. |
| `log_dir` | Where each request is logged, with the run records in `runs/`. |
| `voice` | The Groq address, the models in order, the key name, the five-minute limit, the language. |
| `send_options` | The defaults of the send options: `where` (`local`), `merge` (`auto`), `tests` (`related`), `bug_check` (`true`), `report` (`true`). |
| `worktrees.folder`, `worktrees.main` | Where each run's worktree goes (`.worktrees`) and the branch runs start from and merge into (`main`). |
| `runs.claude_config_dir` | Where Claude Code keeps its transcripts; empty means `CLAUDE_CONFIG_DIR`, else `~/.claude`. |
| `runs.live_seconds` | A run shows as live while its transcript changed in the last 90 seconds. |
| `runs.max_text` | How much of a step's input or output comes with the run page (1,200 characters); the rest loads when you ask. |
| `runs.summary_model` | The model that writes each run's summary and tags (`haiku`). |

## Files

- `server.py`: the web service: the page, the store, write-through, the request box and the routes of the Notes and runs panel.
- `claude_bridge.py`: runs each request as a Claude Code session and checks every step first.
- `notes.py`: the notes and the run records, their statuses, and sending notes as one run.
- `runs.py`: reads Claude Code's own transcripts into runs, with every step.
- `run_summary.py`: writes each run's summary and tags with Claude Haiku.
- `worktrees.py`: each run's branch and worktree, and the merge into `main`.
- `voice.py`: turns a recording into text through Groq.
- `server.config.json`: the settings.

The start and set-up scripts, `start.sh` and `init.sh`, sit at the top of the repository.
