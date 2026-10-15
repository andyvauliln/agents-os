# Input 2026-10-14: two types of questions

- From: the owner, in the thread "Interactive file tree UI"
- Date: 2026-10-14

## Raw input
~~~text
for question i think we need 2 types one we should record mine in metadata if not do that (with an answer), tell me state of it, questions created when we do plan, or by skill to analyse and make questions
~~~

## Answer
~~~text
State before: the owner's questions were only in the inputs, not on their items; the agents' open questions were only in 22 Questions files made while the docs were written; no skill analysed items for questions. Now every Questions file has two parts, "Open questions for the owner" and "The owner's questions". Past owner questions were recorded on their items with the answers (53 questions in 21 files). Plans write their choices as open questions (change-plan), and the new make-questions skill analyses an item, a folder or a level and writes the questions only the owner can answer. Explained in docs/metadata.md section 18.
~~~

## Processed into
- docs/metadata.md (section 18, 7.2, 3, who does what)
- skills change-plan, knowledge-intake, ide-sync, file-index, make-questions (new), both copies
- agents/system/CLAUDE.md, docs/README.md, docs/README.asd.md, apps/project-IDE/docs/README.md, README.asd.md
- every Questions file (two parts); 17 new Questions files with the owner's questions
