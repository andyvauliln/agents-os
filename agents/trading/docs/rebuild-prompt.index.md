---
about: agent-os/agents/trading/docs/rebuild-prompt.md
basis: d578bb146c31
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T19:42:37Z
---
# rebuild-prompt.md

## What it is

The prompt an AI coding agent follows to build `agents/trading/` again, assuming the system is already built: the exact tree, the names and formats of the metadata files, the four docs and how each is written, the research folder restored as it is, the prediction-market domain as empty folders, the build order and the checks.

## Who looks after it

The knowledge base agent writes it with the `rebuild-prompt-doc` skill, last of trading's docs. The owner can also change it on the File Tree page.

## When and how it changes

It changes after every change to trading's design: a new file or folder, a new metadata rule, a settled open point, a new trading domain. The agent updates the tree, the parts, the build order, the checks and "Do not build".

## Who uses it, and when

An AI agent rebuilding trading or checking it against its spec; the owner, to check that nothing is missing.

## Where it is mentioned

The system's rebuild prompt lists it in its build order; trading's vision and README skills end by bringing it in line; the prediction-market domain's own prompt follows it in stage two.

## Related knowledge

It must agree with trading's vision and README and use their names. It takes the metadata formats from the `file-index` skill and the file-set plan, and the domain's folders from the real tree.

## Keep in mind

- When you build from it, never create files inside `agents/trading/prediction-market/` other than `.gitkeep` until stage two.
- When a trading domain gets its own rebuild prompt, add it to the build order here.
- When you write here, never include a key value; key names only.
