---
about: agent-os/apps/project-IDE/data/inputs/
node: n-2.10
basis: 84798c866ad1
written: 2026-10-05T13:25:49Z
by: knowledge-base-agent
confirmed: 2026-10-07T14:22:08Z
---
# inputs/

## Summary

The archive of every owner input, kept with the project's records in `project-IDE/data/`, word for word, from any channel (project chat, threads, comments on files, the File Tree page), so nothing the owner said is lost and every doc can say where its knowledge came from. Each input is one Markdown file with a header, the raw text and what it was processed into; a question is stored with its answer. `index.json` lists every input with its categories and summary for the knowledge map, and `README.md` explains the archive and its categories. The knowledge agent saves each input on receipt, as the first step of processing it; File Tree page messages wait in the page's own store until the next sync. Agents read the archive when a summary is unclear.

## Keep in mind

- When the owner says anything about the system, in any channel, store it here word for word before filing its knowledge.
- When an input is stored, never edit its raw text; corrections go into the docs.
