# Questions: CLAUDE.md

## Open questions for the owner

None open.

## The owner's questions

### 2026-10-05: What is updated after a change to the logic?

> also if we do something and update some logic what we update after that in knowledges i want understand how we do it

Every change follows the round in this file: pull, file the input, plan the change, record the decision and the changelog, update the docs it touches level by level (vision, README, README.asd, rebuild prompt), update the metadata of every changed file, rebuild and check the page, then commit and push. The table "When and how to update each doc" says which change makes which doc stale and which skill writes it.

Docs improved: none, the answer was already in agents/system/CLAUDE.md (the round and the table "When and how to update each doc").

### 2026-10-13: Why the memory notes are needed

> and explain me why we need all of this this new files in a memory folder, and how we ll use it

They told a new session the lasting rules, wishes and decisions, and were put in git because Claude Code on the owner's server cannot read the cloud project memory. This changed later: the owner decided that agents use the docs and the metadata instead, so the new version keeps no memory notes in git, and the lasting rules are in this file under "Rules".

Docs improved: agents/system/CLAUDE.md, agents/system/CLAUDE.index.md, agents/system/.claude/skills/claude-md-doc/SKILL.md, vision/.claude/memory/README.md.

### 2026-10-13: Why keep anything in a memory at all?

> i am just not sure why we need keep it in a memory in a new version agent should use documentation and index files, and not keep that much in a memory also i think most of it somehow already in a docs, and explain why we would better keep something of you suggest there what we don't have and it's not a place in a documentation or metadata

No memory folder is needed: nearly all of it was already in the docs. The few missing parts go to their places: the owner's wishes into the rules of this file, the rule that system text stays general into the trading README, and open questions into the Questions files of their items; facts about the cloud project only stay in the cloud project memory. This is decided, and `vision/.claude/memory/` is deleted, not moved, when `vision/` goes.

Docs improved: agents/system/CLAUDE.md, agents/trading/docs/README.md, agents/trading/docs/README.asd.md.
