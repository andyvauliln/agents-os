# Input 2026-10-15: ignore local state and runtime files; block the live keys

- From: the owner, in the thread "Interactive file tree UI"
- Date: 2026-10-15

## Raw input
~~~text
about that yes, The docs say `agents/system/.claude/settings.json` blocks `.secrets/live/**`, but the file is empty. Shall I add the block?

* `.gitignore` does not exclude `settings.local.json`, `agent-memory-local/`, or the runtime `logs/` and `data/` folders. Shall I add these lines?
~~~

## Answer
~~~text
Yes to both. settings.json denies Read and Edit of .secrets/live/** and of every .env file. .gitignore ignores **/.claude/settings.local.json, the contents of agent-memory-local/, and the run-time contents of logs/ and data/ under agents/; the folders and their metadata files stay in git. The empty settings.local.json placeholder and its metadata files are removed from git.
~~~

## Processed into
- agents/system/.claude/settings.json
- .gitignore
- D-072; the How it works of settings.json, .gitignore, .claude/ and agent-memory-local/
- agents/system/docs/README.md and its twin, agents/system/docs/rebuild-prompt.md, docs/README.md and its twin, README.questions.md
