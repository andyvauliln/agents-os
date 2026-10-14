# in-20261005-1403: index files not visible in the tree; how answers and changes update the knowledge
- At: 2026-10-05T14:03:26Z · Where: thread "Interactive file tree UI" · Source: chat · Ref: cmsg_01Sk8xdkWKCz34CUCfVMyQbxMe7TLqMdmLNioQq2yNUqeA
- Categories: ui, docs-knowledge, process, question
- Summary: The owner still cannot see the .index.md files in the File Tree page's tree, and asks how knowledge is updated: when they ask a question and get an answer, and when something is done or some logic changes.

## Raw input
~~~text
i still can't see .index.md files in a the tree files, why? telll me for example i have question you answer me do we update any knowledge from that? also if we do something and update some logic what we update after that in knowledges i want understand how we do it
~~~

## Answer
~~~text
Why they were not visible: the tree listed only the planned files and folders. Each item's .index.md was shown inside its How it works tab, never as a row of its own. Now every file has its x.index.md row right under it and every folder has f.index.md as its first row; clicking one opens How it works, and a switch above the tree hides them.

A question and its answer: yes. The question and the answer are stored together as one input, word for word. If the answer adds something new (a fact, a rule, a decision, an open question) that goes into the notes, decisions and changelog when decided, the docs it touches, the How it works files of the items it touches, and the README last. If the answer only explains what is already written, only the input record is added. Example: the 10:24 question on why only README and vision had their .index.md next to them changed the rule, so the file-index skill, the build scripts, the index files and the page all changed.

A change to logic: the same flow, larger. Example, the repo layout today: input stored, tree notes, decision and changelog, the docs that mention it (README, vision, CLAUDE.md, the GitHub plan), the agents' and skills' instructions, then the How it works files of every changed item and its parents (the build lists them deepest first, each is rewritten or confirmed), the page rebuilt, checked and published, and the working notes last.
~~~

## Processed into
- docs/file-tree.md v1.18.1: [53.1.1] index rows in the tree; changelog v1.18.1
- File Tree page version 28: every .index.md as a row, a switch to hide them, the filter finds them
- .claude/docs/README.md: one clause on where the How it works file shows in the tree
- changelog.md: 2026-10-05 line
- No new decision: the answer explains the existing flow (knowledge-intake, file-index, ide-build)
