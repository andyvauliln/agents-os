# in-20261006-1144: only .claude/docs/ moves, one level up into the agent's own docs/
- At: 2026-10-06T11:44:34Z · Where: thread "Interactive file tree UI" · Source: chat · Ref: thread cmsg_01Sk8xdkWKCz34CUCfVMyQbxP1hyoB8xVJjehy8MzA6ckj, message cmsg_01Sk8xdkWKCz34CUCfVMyQbxQe77oXU8Hijn6VaSqh3PsZ
- Categories: structure, docs-knowledge
- Summary: The owner narrows in-20261006-1140 and the card choice a minute earlier: only `.claude/docs/` moves, one level up into the docs/ of every agent that has a .claude/.

## Raw input
~~~text
just .claude/docs/  move in a level up docs in every agent who has .claude
~~~

## Answer
~~~text
Got it: only .claude/docs/ moves up into each agent's own docs/. Agent docs folders stay. Starting with the system.
~~~
Then, when done:
~~~text
Done. Only the system had a `.claude/docs/`, so its README and vision now sit in `agents/system/docs/`, next to the notes agents read. The domain, strategy and trading agent `docs/` folders stay as they are, and no agent keeps docs inside `.claude/` any more. The File Tree page shows the change (version 37).
~~~

## Processed into
- D-047: an agent keeps no docs inside its `.claude/`; the system's `.claude/docs/` [10.1.14] is retired and [2.1] README and [2.2] vision moved up into `agents/system/docs/` [2]; the domain, strategy and agent `docs/` ([19.6], [21.6], [46]) stay
- file-tree.md v1.24: the tree, [1], [2], [2.1], [2.2], [2.13], [10.1], [10.1.14] retired, [53.2]
- the system CLAUDE.md draft, the knowledge base agent, knowledge-intake, the people README's agent folder, the knowledge guide, the GitHub sync plan, index_files.py, sources, How it works files; the page v37
