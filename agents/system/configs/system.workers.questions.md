# Questions: system.workers.json

## Open questions for the owner

None open.

## The owner's questions

### 2026-09-30: How do scheduled jobs work in Claude Code?

> how in a claude code we do scheduled jobs and where do they stored? tell me more how it works

Claude Code has five methods:

1. `/loop` in an open session.
2. Cloud routines. The Claude account keeps them, and they run in the cloud of Anthropic.
3. Scheduled tasks of the desktop app.
4. GitHub Actions with a `schedule:` line.
5. The cron or systemd timer of the machine, which runs `claude -p`.

In the Agent OS, each agent lists all its jobs in one jobs file. For the system, it is this file. The plan is one shared scheduler that runs each job on the owner's server. The data and the keys are on that server.

Today all system jobs are off. The scheduler is not built yet.

Docs improved: agents/system/configs/system.workers.index.md.
