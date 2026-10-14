# Questions: system.workers.json

## Open questions for the owner

None open.

## The owner's questions

### 2026-09-30: How scheduled jobs work in Claude Code

> how in a claude code we do scheduled jobs and where do they stored? tell me more how it works

Claude Code has five ways: `/loop` inside an open session, cloud routines saved in the Claude account and run in Anthropic's cloud, scheduled tasks of the desktop app, GitHub Actions with a `schedule:` line, and the machine's own cron or systemd timer that runs `claude -p`. In the Agent OS every agent lists everything it runs in one jobs file, for the system this file, and one shared scheduler is planned to run every job on the owner's server, where the data and keys are. Today every system job is switched off and the scheduler is not built yet.
