# Questions: CLAUDE.md

## Open questions for the owner

None open.

## The owner's questions

### 2026-10-05: What do we update after a change to the logic?

> also if we do something and update some logic what we update after that in knowledges i want understand how we do it

Each change follows the round in this file:

1. Pull.
2. Record the input.
3. Plan the change.
4. Record the decision and the changelog.
5. Update the docs that the change is about, level by level: vision, README, README.asd, rebuild prompt.
6. Update the metadata of each changed file.
7. Build the page again and check it.
8. Commit and push.

The table "When and how to update each doc" tells which change makes which doc stale. It also tells which skill writes that doc.

Docs improved: none, the answer was already in agents/system/CLAUDE.md (the round and the table "When and how to update each doc").

### 2026-10-13: Why do we need the memory notes?

> and explain me why we need all of this this new files in a memory folder, and how we ll use it

The memory notes told a new session the lasting rules, wishes and decisions. They were in git because Claude Code on the owner's server cannot read the cloud project memory.

This changed later: the owner decided that agents use the docs and the metadata instead. The new version keeps no memory notes in git. The lasting rules are in this file, under "Rules".

Docs improved: agents/system/CLAUDE.md, agents/system/CLAUDE.index.md, agents/system/.claude/skills/claude-md-doc/SKILL.md, vision/.claude/memory/README.md.

### 2026-10-13: Why keep a memory at all?

> i am just not sure why we need keep it in a memory in a new version agent should use documentation and index files, and not keep that much in a memory also i think most of it somehow already in a docs, and explain why we would better keep something of you suggest there what we don't have and it's not a place in a documentation or metadata

We do not need a memory folder. Almost all of its content was already in the docs. The few missing parts go to these locations:

1. The owner's wishes go into the rules of this file.
2. The rule that system text stays general goes into the trading README.
3. Open questions go into the Questions files of their items.
4. Facts about the cloud project stay only in the cloud project memory.

This is decided. When `vision/` goes, we delete `vision/.claude/memory/`. We do not move it.

This changed later: on 2026-10-14 `vision/` was removed, with its memory folder. `apps/project-IDE/data/memory/` was deleted too.

Docs improved: agents/system/CLAUDE.md, agents/trading/docs/README.md, agents/trading/docs/README.asd.md.
