---
about: agent-os/apps/project-IDE/server/voice.py
node: n-53.3.5
basis: 88848f43be9f
written: 2026-10-09T10:29:08Z
by: knowledge-base-agent
---
# voice.py

## Summary

Voice input for the page's request boxes. The page records the owner for up to 5 minutes and posts the recording to the server; this module sends it to Groq's speech-to-text service and returns the words, which the page adds to the box for the owner to check and send. It tries the Groq models listed in the server's settings in order: a model that answers with a rate limit is skipped until its wait is over, and an error moves on to the next one, so a busy model never stops the owner. The recording is not kept. The Groq key is read from the keys file by name and never reaches the page, the logs or Claude Code.

## Keep in mind

- When a Groq model is retired or a better free one appears, change the list in `server.config.json`; the first in the list is tried first.
- Never write the key's value anywhere but the keys file on the machine.
