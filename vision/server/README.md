# The project IDE on your server

While the system is planned, everything runs from the planning folder `vision/`: the page is in `vision/explorer/`, the drafts and How it works files are in `vision/`, and Claude Code starts there. When the repository gets `apps/project-IDE/` and `agents/system/`, the paths in `server.config.json` move to them.

This folder runs the File Tree page on your own machine, with Claude Code behind its request box. It is the same page as on claude.ai. Here it reads the repository directly, saves your notes and edits into the repository, and sends what you type in the box at the bottom to Claude Code working in the project.

## What you need

- The repository cloned on the server, with a way to push.
- Python 3.10 or newer, Node, and Claude Code with its SDK: `npm install -g @anthropic-ai/claude-code` and `pip install claude-agent-sdk`.
- A way for Claude Code to sign in. Either put an API key in the keys file `.secrets/test/.env` as `ANTHROPIC_API_KEY=...`, or sign Claude Code in once with `claude` in a terminal. The settings name the key; its value never leaves the keys file.
- For voice input, a Groq key in the same keys file as `GROQ_API_KEY=...` (free at console.groq.com). Without it the microphone button stays hidden.

## Start it

From the top of the repository:

```bash
python3 vision/server/server.py
```

It listens only on the machine itself, at `127.0.0.1:8765`. From your own computer, open a tunnel and then the page:

```bash
ssh -N -L 8765:127.0.0.1:8765 you@your-server
# then open http://127.0.0.1:8765/ in the browser
```

The header of the page says "on your server" when it found the service. Stop the service with Ctrl+C.

Never open the port to the internet or put the service behind a public address. Whoever can reach the page can make Claude Code change files and run commands. The server refuses to listen on any address but the machine's own.

## What happens when you use it

- **Notes, comments and edits** are saved at once as small JSON files in `vision/page-store/`, so they are in the repository and nothing waits on claude.ai. An edit to a file's text is also written straight into the file the page showed (a draft in `vision/`, or a real file in the repository), and an edit to How it works into the item's `.index.md`. An edit to a planned file nobody has written yet waits in the page store until the next sync.
- **A request in the box** runs as a Claude Code session started in `vision/`, the planning folder. From there Claude Code loads the planning copy of the system's agents and skills and its `CLAUDE.md` in `vision/.claude/`, so it works by the same rules as every other Claude on the project: it files your request, does the work, rebuilds the page and commits. The page shows each step while it works, then the answer with its cost and time, and reloads the tree if files changed. A follow-up in the same box continues the same conversation.
- **Delete** next to a file's or folder's name opens a short form with an optional note for Claude, such as what to move or keep first. Claude Code deletes the item and its How it works file straight away, then cleans the project of it: its place in the notes, links to it and mentions of it in other files. It keeps your note in mind, files the deletion and commits. The item stays on the page, struck through, until the next sync, and "Bring it back" undoes it the same way.
- **Voice input**: the microphone button next to the request box and the delete note box records you, up to 5 minutes, with a timer; press it again to stop. The server sends the recording to Groq and the text is added to the box, so you can check it before you send. If one Groq model hits its rate limit or fails, the next one in `server.config.json` is tried. The recording is not kept. The browser asks once for the microphone; open the page as `127.0.0.1` or `localhost`, since browsers allow the microphone only there or over HTTPS.
- **Steps that need your click** show up in the chat with Allow and Refuse buttons: pushing to GitHub, deleting anything other than the item you deleted, installing, network tools, and anything outside the repository. Nothing from the page can open the keys folder. A question nobody answers is refused after fifteen minutes.
- **Apply changes** at the top of the page shows how many items are marked changed. Pressing it starts one Claude Code run in the chat of the top folder: Claude Code brings everything waiting on the page into the files (the sync), rebuilds the page and commits, and the page loads the new tree.
- **The "changed" mark** shows on everything a request from the page touched: your edits and notes, new and deleted items, requests in the box, and every file Claude Code changed for you. The marks stay until the next sync.
- **Every request is logged** with its steps, answer, cost and time in `vision/logs/project-ide-agent/`.
- **"Sync the file tree"** typed in the box works here too: Claude Code folds what is waiting in the page store into the files, the same way it does for the page on claude.ai.

## Settings

`server.config.json`, next to this file:

| Setting | What it does |
|---|---|
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
| `log_dir` | Where each request is logged. |

## Files

- `server.py`: the web service: the page, the store, write-through and the request box.
- `claude_bridge.py`: runs each request as a Claude Code session and checks every step first.
- `voice.py`: turns a recording into text through Groq.
- `server.config.json`: the settings.
