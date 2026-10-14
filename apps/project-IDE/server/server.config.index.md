---
about: agent-os/apps/project-IDE/server/server.config.json
basis: 0107f331ab6c
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T15:07:13Z
---
# server.config.json

## What it is

The server page's settings: the address and port (only the machine itself), the page folder (`apps/project-IDE/current-ui`) and the store folder (`apps/project-IDE/data/page-store`), whether edits are written straight into their files, the keys file and the key names Claude Code gets (values stay in the keys file), where Claude Code starts (`agents/system`), the model (empty means Claude Code's default), the limits for one request, the tools and commands Claude Code may use without asking, the words that always wait for the owner, the paths nothing may touch, and the log folder. It also names `GROQ_API_KEY`, which only the voice module gets, and its `voice` section lists the Groq models in the order they are tried, the 5 minute limit and the language.

## Who looks after it

It is written by project-ide-agent and the owner.

## When and how it changes

It changes when the owner changes a setting.

## Who uses it, and when

It is read by `apps/project-IDE/server/server.py`, `apps/project-IDE/server/claude_bridge.py` and `apps/project-IDE/server/voice.py`.

## Where it is mentioned

It is described in `apps/project-IDE/server/README.md` and its folder's How it works file `apps/project-IDE/server/server.index.md`.

## Related knowledge

It is read by `apps/project-IDE/server/server.py`, `apps/project-IDE/server/claude_bridge.py` and `apps/project-IDE/server/voice.py`. It links to `.secrets/secrets.index.json` and `apps/project-IDE/data/plans/2026-10-13-leave-vision.md`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `docs/metadata.md`, `apps/docs/README.md` (section "The project IDE"), `apps/project-IDE/docs/README.md` (section "The server") and `agents/system/docs/README.md` (section "Keys and secrets").

## Keep in mind

- Never put a key's value here: name it, and keep the value in the keys file on the machine.
