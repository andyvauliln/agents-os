# in-20260930-0919: How do scheduled jobs work in Claude Code?
- At: 2026-09-30T09:19:49Z · Where: thread: Interactive file tree UI · Source: chat · Ref: cmsg_01Sk8xdkWKCz34CUCfVMyQbxVLSuyaiRCjZZ6M5h7YQvM6
- Categories: question, workers-jobs
- Summary: The owner asked how scheduled jobs work in Claude Code and where they are stored.

## Raw input
~~~text
how in a claude code we do scheduled jobs and where do they stored? tell me more how it works
~~~

## Answer (given in chat)
~~~text
Good question. I'll check the current Claude Code docs on scheduled jobs and where they're stored, then explain.

Claude Code has five ways to run scheduled jobs. They differ in where the job is stored and which machine runs it:

1. **`/loop` inside a session**, e.g. `/loop 10m check prices`. It lives in the open session only, runs on your machine, and stops when the session ends. It comes back only if you resume that session, and recurring loops expire after 7 days. Good for watching something for an hour.
2. **Cloud routines** (claude.ai/code/routines, or `/schedule` in the CLI). They're saved in your Claude account and run in Anthropic's cloud, even with your laptop off. Each run starts in a fresh container that clones the repo from GitHub. The minimum interval is 1 hour, and they can also be started by an API call or a GitHub event. They can't see local files, so no local data, logs or `.secrets`.
3. **Desktop app scheduled tasks** (Routines tab, then Local). The prompt is stored in `~/.claude/scheduled-tasks/<name>/SKILL.md` and the schedule in the app. They run on your computer, only while the app is open and the computer is awake, and after sleep they catch up once.
4. **GitHub Actions.** A `schedule:` cron line in `.github/workflows/*.yml` in the repo runs Claude on GitHub's machines.
5. **Your own cron or systemd timer** running `claude -p "…"` (headless, one run, then exit) in a folder. The schedule sits in your crontab or timer file, and it runs wherever that machine is on.

**For Trading OS**, I'd suggest:
- **Workers** (fetch data every 5 minutes) don't need Claude at all. They're plain scripts on cron or systemd, which is cheaper and on time.
- **Agent runs and self-improvement** should be cron or systemd calling `claude -p` inside the agent's own folder, on the machine that holds the data and `.secrets`. That way each run picks up that level's `.claude/` settings and CLAUDE.md.
- **Cloud routines** fit repo-only jobs, like a nightly "sync the file tree" or a docs review. Trading loops need local data, so they don't fit there.

I checked this against the current Claude Code docs (code.claude.com/docs/en/scheduled-tasks, routines, desktop-scheduled-tasks, github-actions).
~~~

## Processed into
- answered in chat
