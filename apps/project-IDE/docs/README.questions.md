# README.md: open questions for the owner

- The skill sets 500 to 2,000 words for an app's README; you asked for the full documentation of the IDE, so this one is about 6,800 words. Keep it as one long manual, or split the page manual into its own file? It decides where readers look for how to use the page.
- Where should shared views live: `apps/project-IDE/views/` with a `views.json` list, as proposed? It decides where every custom view is written in stage one.
- When the working sources leave `vision/`, may we move the page, server and scripts into `apps/project-IDE/` and `agents/system/.claude/skills/ide-build/scripts/` in one round, with the server starting Claude Code in `agents/system/`? Until then the copies there are not the ones that run.
- Should the build get a script that compares the tree with `git ls-files` and fails on any difference? Today this check is done by hand.
