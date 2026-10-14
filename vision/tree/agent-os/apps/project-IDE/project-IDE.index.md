---
about: agent-os/apps/project-IDE/
node: n-53
basis: b31579384259
written: 2026-10-14T12:00:00Z
by: knowledge-base-agent
confirmed: 2026-10-14T10:21:35Z
---
# project-IDE/

## Summary

The owner's IDE for the project, one of the apps: the File Tree page they use to manage, analyse and view the Agent OS while it is built with AI, and everything the page is built from. It serves every AI as much as the owner: for any file it shows what it is for, how it works, what depends on it and what holds for it from the levels above, so changes land everywhere they should. Like every app it has its own `docs/`: a vision, a README (the full manual of the IDE), its ASD-STE100 twin and a rebuild prompt. `current-ui/` holds the page and its data, as published on claude.ai; `server/` runs the same page on the owner's server, with Claude Code behind its request box; `data/` holds this project's knowledge: every owner input word for word, the decisions, the changelog, the tree notes, the knowledge map, the notes behind each doc, the page's store on the server, the owner's page edits, working notes, plans and retired files. The project IDE agent builds and publishes the page; the knowledge base agent keeps the knowledge. It is not the prediction-market domain's trading dashboard, which is `trading-ui/`.

## Keep in mind

- When something changes on the page or in the files it is built from, rebuild the page; never edit its data by hand.
- When the IDE's parts change, bring its own vision, README and rebuild prompt in line, in that order.
