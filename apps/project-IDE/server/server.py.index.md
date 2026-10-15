---
about: agent-os/apps/project-IDE/server/server.py
basis: a6bae833dd18
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T15:07:13Z
---
# server.py

## What it is

The small web service behind the page on the owner's server, standard library only. It serves the page and its data from `apps/project-IDE/current-ui/`, keeps the page's notes, edits and messages as one JSON file each in `apps/project-IDE/data/page-store/`, writes an edit to a file's text straight into that file and an edit to How it works into the `x.index.md` next to the item, and hands each request typed on the page, and each deletion, to `claude_bridge.py`, streaming its progress back. It writes only what a save changed. It answers only to the machine's own address. It also takes a voice recording at `api/voice` and hands it to `voice.py`, which returns the text; the recording is not kept, and the health answer tells the page whether voice is on.

## Who looks after it

It is written by project-ide-agent.

## When and how it changes

It changes when the page's way of talking to the server, the store or the write-through changes.

## Who uses it, and when

It is read by the owner, who starts it; and project-ide-agent.

## Where it is mentioned

It is described in `apps/project-IDE/server/README.md` and its folder's How it works file `apps/project-IDE/server/server.index.md`.

## Related knowledge

It reads `apps/project-IDE/server/server.config.json`, `apps/project-IDE/current-ui/file-tree-explorer.html`, `apps/project-IDE/current-ui/file-tree.data.json`, `apps/project-IDE/server/claude_bridge.py` and `apps/project-IDE/server/voice.py`. It writes `apps/project-IDE/data/page-store/`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `docs/metadata.md`, `apps/docs/README.md` (section "The project IDE") and `apps/project-IDE/docs/README.md` (section "The server").

## Keep in mind

- Never open it to the internet: whoever reaches the page can make Claude Code change files and run commands.
- When you change how the page talks to it, test both: the page on claude.ai and the page served here.
- When the file set is built, split this file into one file per job; today it does several.
