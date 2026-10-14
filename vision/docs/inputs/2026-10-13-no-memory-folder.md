# Input 2026-10-13: no memory folder in the new version

- From: the owner, in the thread "Interactive file tree UI"
- Date: 2026-10-13

## Raw input
~~~text
i am just not sure why we need keep it in a memory in a new version agent should use documentation and index files, and not keep that much in a memory also i think most of it somehow already in a docs, and explain why we would better keep something of you suggest there what we don't have and it's not a place in a documentation or metadata
~~~

## Answer
~~~text
Agreed: checked the 13 notes against the docs; almost all is already in CLAUDE.md, the READMEs, the visions, decisions and changelog. Missing parts and their place: owner wishes (ASD answers on request, low token use) into CLAUDE.md rules; the rule "system text general, money and markets in prediction-market" into agents/trading/docs/README.md; open questions for the owner into the x.questions.md of their items; cloud-only facts stay only in the cloud project memory. Proposed: vision/.claude/memory/ is deleted, not moved; apps/project-IDE/data/memory/ keeps only its template or is removed. Waiting for the owner's yes or no.
~~~

## Processed into
- apps/project-IDE/data/plans/2026-10-13-leave-vision.md (memory row, D-066)

## Follow-up 2026-10-13
~~~text
yes and print me update filee with what new or will be updated
~~~
Recorded as D-066. The files plan now deletes the 14 notes (no move) and says where each part goes; counts: delete 628, move 184.
