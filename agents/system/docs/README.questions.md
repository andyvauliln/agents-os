# Questions: README.md

## Open questions for the owner

- **Do we commit the symlinks, or does `init.sh` make them again after each clone?**
- **Does the system agent need its own settings file in addition to `system.config.json`?**
- **How does the common prompt go into the instructions of each level: by import or by copy?**
- **Which default model effort is correct?** The sources do not agree. They give high, xhigh, and medium on the page.

## The owner's questions

### 2026-10-15: Ignore local state and runtime files; block the live keys

> about that yes, The docs say `agents/system/.claude/settings.json` blocks `.secrets/live/**`, but the file is empty. Shall I add the block? * `.gitignore` does not exclude `settings.local.json`, `agent-memory-local/`, or the runtime `logs/` and `data/` folders. Shall I add these lines?

Yes. `settings.json` now denies Read and Edit of `.secrets/live/**` and of every `.env` file. `.gitignore` now ignores `settings.local.json`, the contents of `agent-memory-local/`, and the run-time contents of `logs/` and `data/` under `agents/`. The metadata files of these folders stay in git. The empty `settings.local.json` is removed from git.

Docs improved: `.gitignore` How it works, `settings.json` How it works, `agents/system/docs/README.md`, `agents/system/docs/rebuild-prompt.md`, `docs/README.md`.

None recorded yet.
