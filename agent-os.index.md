---
about: agent-os/
node: n-0
basis: 0de59e2b20ed
written: 2026-10-09T09:55:29Z
by: knowledge-base-agent
---
# agent-os/

## Summary

The system's workspace, the Agent OS: a home for AI agents of any kind, such as trading, social media or management. Trading is the first kind and lives in `agents/trading/`, a folder of trading domains; its first, the prediction-market domain, runs many trading agents side by side, tests every idea in test mode first and keeps what works, with the owner approving anything that touches real money; the next trading domain, copy trading, is copied from it. The system level keeps only what holds for any agent: test and live modes, the owner's approval to go live, a general stop switch, limits in code, the key rules and the shared machinery.

Agents at every level work in the same standard folder, and everything is a plain file the owner can open. The workspace is one GitHub repository: `README.md` at the top; `agents/`, with every agent, the shared files, the docs for people and `agents/system/.claude/CLAUDE.md`, which AI sessions read first; `apps/`, with our own apps and the outside ones, each with its own docs, among them `project-IDE/`, the owner's File Tree page; and `.secrets/`, which stays on the machine and out of git. Every file and folder has a short How it works file (`vision.index.md` for `vision.md`) and a Details file (`.meta.json`, empty for now). Nothing is built yet.

## Keep in mind

- When anything needs a secret, list the key name in `secret_keys` and let `load-secret` load it; never write a value anywhere.
- When you add or change a link, edit the agent's links file and let `relink` build it; never make a symlink by hand.
- When you change a file, read its whole context first (the levels above included), bring everything related in line, and run what you learned through the knowledge agent.
- When you write about the system as a whole, write in general terms: it runs agents of any kind, and trading is one kind that lives in its domain.
