---
about: agent-os/apps/project-IDE/server/voice.py
basis: 437deb7f2846
written: 2026-10-14T12:00:00Z
by: knowledge-base-agent
confirmed: 2026-10-14T15:07:13Z
---
# voice.py

## Summary

Voice input for the page's request boxes. The page records the owner for up to 5 minutes and posts the recording to the server; this module sends it to Groq's speech-to-text service and returns the words, which the page adds to the box for the owner to check and send. It tries the Groq models listed in the server's settings in order: a model that answers with a rate limit is skipped until its wait is over, and an error moves on to the next one, so a busy model never stops the owner. The recording is not kept. On claude.ai the page gets no microphone, so the button is hidden; there, use the device's own dictation (the microphone on a phone's keyboard, Fn twice on a Mac, Win+H on Windows). The Groq key is read from the keys file by name and never reaches the page, the logs or Claude Code.

## Keep in mind

- When a Groq model is retired or a better free one appears, change the list in `server.config.json`; the first in the list is tried first.
- Never write the key's value anywhere but the keys file on the machine.
