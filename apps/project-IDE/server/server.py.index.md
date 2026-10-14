---
about: agent-os/apps/project-IDE/server/server.py
node: n-53.3.2
basis: 3ab7494ff6ae
written: 2026-10-07T14:21:32Z
by: knowledge-base-agent
confirmed: 2026-10-09T10:30:32Z
---
# server.py

## Summary

The small web service behind the page on the owner's server, standard library only. It serves the page and its data from the repository, keeps the page's notes, edits and messages as one JSON file each in `data/page-store/`, writes an edit to a file's text straight into that file and an edit to How it works into its How it works file, and hands each request typed on the page, and each deletion, to `claude_bridge.py`, streaming its progress back. It writes only what a save changed, so saving the same item again for a note or a mark never puts an older page edit over a file Claude Code has changed since. It answers only to the machine's own address and refuses to listen on any other. It also takes a voice recording from the page at `api/voice` and hands it to `voice.py`, which returns the text; the recording is not kept, and the health answer tells the page whether voice is on. It also takes a voice recording from the page at `api/voice` and hands it to `voice.py`, which returns the text; the recording is not kept, and the health answer tells the page whether voice is on.

## Keep in mind

- Never open it to the internet: whoever reaches the page can make Claude Code change files and run commands.
- When you change how the page talks to it, test both: the page on claude.ai and the page served here.
- When the file set is built, split this file into one file per job; today it does several.
