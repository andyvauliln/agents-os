# Input 2026-10-14 09:03: status, inputs, decisions, questions and the Details fields

- From: the owner, in the thread "Interactive file tree UI"
- Date: 2026-10-14

## Raw input
~~~text
what logic we currently have around An idea of an agent is `proposed` until the owner says yes. this, and about inputs and about decision and about questions, and actuality all fields in metadata object, add to this document
~~~

## Answer
~~~text
Added to docs/metadata.md as sections 15 to 19: status (decided, proposed, idea, open) and every place it is written; owner inputs (files, index.json, the knowledge-intake steps); decisions (D numbers, decisions.md, where numbers are used); questions (Questions files, the old open questions in the tree notes, Still open, the Discuss flow); and the true state of every Details field: who fills it, what reads it, how many of the 421 files have it (about 29 written, 257 only {}, 135 only the empty schema; no script reads a field yet; values `skill` and `built` outside the list). Fixed drift found on the way: 10 inputs used "## Words" instead of "## Raw input", 17 input categories were not in the list, 76 rows had no `answered` flag.
~~~

## Processed into
- docs/metadata.md sections 15-20, docs/README.md, docs/README.asd.md, docs/rebuild-prompt.md
- inputs/index.json (categories and answered flags fixed), 10 input headings
