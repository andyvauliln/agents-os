# Input 2026-10-14: keep the knowledge notes without references; remove tree numbers and ids

- From: the owner, in the thread "Interactive file tree UI"
- Date: 2026-10-14

## Raw input
~~~text
ok let's leave it but i don't want that we anywhere make references to them now, addditional knowledge files ll be considered later. 2 Generally if we no need file tree number we can remove it i just don't know why we have it and how we use it, guyes same
~~~

## Answer
~~~text
1. The topic notes move to apps/project-IDE/data/sources/ and the trading notes stay in the prediction-market docs, but no doc, skill or agent refers to them any more; knowledge goes only into the level docs, CLAUDE.md, metadata.md and each item's metadata files. 2. The tree numbers and the node ids came from the old tree notes (vision/docs/file-tree.md), which numbered every item before real files existed; the build, the knowledge tags and the page used them to find an item. Once the tree notes retire, the path is the id, so they go: the tree_number field is removed from every Details file now, and the numbers and ids leave the How it works front matter, the knowledge tags and the page in the move out of vision/.
~~~

## Processed into
- skills, agents, CLAUDE.md and the level docs (references removed)
- every Details file, docs/metadata.md, file-index, the rebuild prompts (tree_number removed)
- the leave-vision plan (numbers and ids removed in the move)
