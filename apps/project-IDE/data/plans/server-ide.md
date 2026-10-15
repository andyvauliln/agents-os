# The File Tree page on the owner's server, with Claude Code behind it

Status: agreed by the owner, who also asked that the IDE live in `apps/` and that Claude Code run from the system folder. The code is written and was tested on a copy of the repository, including a real Claude Code request and the owner's Allow and Refuse buttons. It goes live on the server after the GitHub sync, because the server works from a clone of the repository.

## What the owner gets

The same File Tree page, opened in the browser from the owner's own server. It reads the repository on the server, so it always shows the files as they are right now.

The box at the bottom of every file and folder does more than on claude.ai. A request typed there goes to Claude Code working in the repository, with the project's `CLAUDE.md`, the knowledge base agent, the project IDE agent and their skills. Claude Code can answer a question, change a file, add or move items, or run a skill or an agent. The page shows what it is doing while it works, and reloads the tree when it is done. A follow-up typed in the same box continues the same conversation.

An edit to a file's text, or to its How it works, is written straight into that file. Notes, comments and messages are saved at once as small files in the repository, in the page's store folder, and Claude Code folds them into the docs when the owner types "sync the file tree" in the box, as on claude.ai. Nothing waits on claude.ai.

## How it is put together

**One page, two homes.** The page is the same file everywhere. On claude.ai it keeps the owner's notes in the page's own store and asks Claude on the page. On the server it finds the server's small service next to it and uses that instead: saving writes to the files, and the box talks to Claude Code. Opened anywhere else, it stays view only, as it is today.

**A small service in `apps/project-IDE/server/`**, one of the apps. `server.py` serves the page and its data from the repository, reads and writes files for the page, hands each request to Claude Code, and rebuilds the page data after every change so the page can reload. `claude_bridge.py` runs the requests. `server.config.json` holds the settings, and `README.md` says how to start it and reach it safely.

**Claude Code through the Claude Agent SDK.** Each request is a Claude Code session started in the system folder, `agents/system/`, as the owner decided. From there Claude Code loads the system's own agents and skills as its own, including the system's `CLAUDE.md` in `agents/system/.claude/`, so it follows the same rules as every other Claude on the project. The SDK streams every step back, so the page can show it live, and it reports what each request cost and how long it took; the page shows both. A follow-up resumes the same session.

**Why the system folder.** Claude Code finds agents and skills only in the `.claude/` folder of the place it starts from and the folders above it, never in folders further down. Ours live in `agents/system/.claude/`, so starting there is what makes the knowledge base agent, the project IDE agent and their skills available, with no copies or links.

**Every request is an owner input.** Claude Code files it word for word with its answer, like any other message, because `CLAUDE.md` says so. Each request is also logged with its cost and time in the system's logs, under the project IDE agent.

**After each round** Claude Code rebuilds the page and commits, as `CLAUDE.md` describes. Pushing to GitHub waits for the owner's click on the page.

## Keeping it safe

Whoever can reach this page can make Claude Code change files and run commands on the server. So:

- The service listens only on the machine itself. The owner reaches it from their computer through an SSH tunnel or a private network, never from the open internet.
- Claude Code may read and change files inside the repository and run the project's own scripts without asking.
- Pushing, deleting files, anything outside the repository and anything that touches real money wait for the owner's click on the page. The bridge checks every step before Claude Code takes it, so these limits hold even if a request asks for something else.
- Claude Code never opens the keys folder.
- It signs in with an API key whose value sits in the keys folder on the machine. The settings file holds only the key's name.

## What the owner sets up on the server

1. The repository cloned from GitHub, with a way to push.
2. Node, Python, Claude Code and the Claude Agent SDK installed.
3. An API key for Claude in the keys folder.
4. Start the service, open the tunnel, and open the page in the browser.

## Still open

- How the claude.ai link gets the server's changes: either the cloud project republishes after it pulls, or Claude Code on the server publishes. Whether the server can publish has to be checked.
