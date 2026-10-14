---
about: agent-os/apps/project-IDE/server/voice.py
basis: 437deb7f2846
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T15:07:13Z
---
# voice.py

## What it is

Voice input for the page's request boxes. The page records the owner for up to 5 minutes and posts the recording to the server; this module sends it to Groq's speech-to-text service and returns the words, which the page adds to the box for the owner to check and send. It tries the Groq models listed in the server's settings in order: a model that answers with a rate limit is skipped until its wait is over, and an error moves on to the next one, so a busy model never stops the owner. The recording is not kept. On claude.ai the page gets no microphone, so the button is hidden; there, use the device's own dictation (the microphone on a phone's keyboard, Fn twice on a Mac, Win+H on Windows). The Groq key is read from the keys file by name and never reaches the page, the logs or Claude Code.

## Who looks after it

It is written by project-ide-agent.

## When and how it changes

It changes when a Groq model is retired or added, or the voice flow changes.

## Who uses it, and when

It is read by `apps/project-IDE/server/server.py`.

## Where it is mentioned

It is described in `apps/project-IDE/server/README.md` and its folder's How it works file `apps/project-IDE/server/server.index.md`.

## Related knowledge

It is read by `apps/project-IDE/server/server.py`. It reads `apps/project-IDE/server/server.config.json` and `.secrets/test/.env`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `docs/metadata.md`, `apps/docs/README.md` (section "The project IDE"), `apps/project-IDE/docs/README.md` (section "The server") and `agents/system/docs/README.md` (section "Keys and secrets").

## Keep in mind

- When a Groq model is retired or a better free one appears, change the list in `server.config.json`; the first in the list is tried first.
- Never write the key's value anywhere but the keys file on the machine.
