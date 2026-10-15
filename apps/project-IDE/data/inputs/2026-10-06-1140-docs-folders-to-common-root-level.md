# in-20261006-1140: no docs folders inside agent folders; one common place at the root agent level
- At: 2026-10-06T11:40:39Z · Where: thread "Interactive file tree UI" · Source: chat · Ref: thread cmsg_01Sk8xdkWKCz34CUCfVMyQbxP1hyoB8xVJjehy8MzA6ckj, message cmsg_01Sk8xdkWKCz34CUCfVMyQbxPxaHeJ18sYJhSz3saLxXs3
- Categories: structure, docs-knowledge
- Summary: The owner says docs folders are not kept inside agent folders; docs belong in one common place at the root agent level.

## Raw input
~~~text
we don't keep docs folder in a agent folders should be in a common root agent level
~~~

## Answer
~~~text
Understood: no docs folders inside agent folders, one common docs place at the root. I'll check what moves first.
~~~
Then a decision card (2026-10-06 11:41): "Move which docs folders into one common docs folder?" Options: All in system (recommended: every agent's docs/ and .claude/docs/ move into agents/system/docs/, one subfolder per agent), README and vision only, or agents/docs/ on top. Nothing in the tree changes until the owner picks.

## The owner's choice
- 11:43: the owner tapped "All in system" on the card.
- 11:44: the owner narrowed it in their own words (in-20261006-1144): "just .claude/docs/  move in a level up docs in every agent who has .claude". That message decides: only `.claude/docs/` moves, one level up into the same agent's `docs/`; the agents' own `docs/` folders stay. The card choice is not carried out.

## Processed into
- D-047, with in-20261006-1144
