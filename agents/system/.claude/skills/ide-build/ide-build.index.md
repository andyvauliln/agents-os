---
about: agent-os/agents/system/.claude/skills/ide-build/
node: n-10.1.2.5
basis: 12b21ee74904
written: 2026-10-05T13:25:49Z
by: knowledge-base-agent
confirmed: 2026-10-14T10:21:35Z
---
# ide-build/

## Summary

The skill that builds the File Tree page from the repository, checks it and publishes it, with its scripts inside it so the two move together. `SKILL.md` gives the steps; `scripts/` holds the build scripts and the page check. The project IDE agent runs it after every round that changes the tree, a doc or a How it works file.
