---
about: agent-os/apps/project-IDE/server/server.config.json
basis: 0107f331ab6c
written: 2026-10-05T16:17:55Z
by: knowledge-base-agent
confirmed: 2026-10-14T15:07:13Z
---
# server.config.json

## Summary

The server page's settings: the address and port (only the machine itself), the page and store folders, whether edits are written straight into their files, the keys file and the key names Claude Code gets (values stay in the keys file), where Claude Code starts (`agents/system`), the model (empty means Claude Code's default), the limits for one request, the tools and commands Claude Code may use without asking (reading, searching, moving between folders, editing, committing), the words that always wait for the owner, the paths nothing may touch, and the log folder. Since voice input it also names `GROQ_API_KEY`, which only the voice module gets, never Claude Code, and its `voice` section lists the Groq models in the order they are tried, the 5 minute limit and the language. Since voice input it also names `GROQ_API_KEY`, which only the voice module gets, never Claude Code, and its `voice` section lists the Groq models in the order they are tried, the 5 minute limit and the language.

## Keep in mind

- Never put a key's value here: name it, and keep the value in the keys file on the machine.
