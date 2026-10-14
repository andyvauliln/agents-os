# Questions: SKILL.md

## Open questions for the owner

None open.

## The owner's questions

### 2026-10-05: How do notes and comments on the page become agent work?

> also not clear how we now hanlding agentic works from the ui comments and notes on files and folders?

The page saves each thing that you leave on it at once, in the store of the page. It marks the item "changed".

You push Apply changes or say "sync the file tree". Then this skill does these steps:

1. It records each message as an owner input, word for word.
2. It writes the edits into their files.
3. It applies the notes that are changes. It makes the other open notes into open questions.
4. It does the requests.
5. It completes the deletions.
6. It gives the inputs to the knowledge base agent.
7. It builds the page again with `ide-build`.

On the owner's server, the page writes the edits into the files at once. A request starts Claude Code immediately.

Docs improved: agents/system/.claude/skills/ide-sync/SKILL.md, agents/system/.claude/skills/ide-sync/SKILL.index.md.
