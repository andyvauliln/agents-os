---
about: agent-os/agents/trading/prediction-market/docs/subagents.link/
basis: 45be2ed5538f
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T19:42:37Z
---
# subagents.link/

## What it is

The domain's view of its strategies' docs: one folder link per strategy, named after the strategy's folder and pointing at that strategy's `docs/`. Today it holds only the name pattern `[agent-name]/`; no link exists yet. Relink, a planned shared script, is meant to build the links from the folder tree and remove them when a strategy goes; they are read-only for the domain and never listed in a links file.

## Who looks after it

It is written by relink (stage two script).

## When and how it changes

In stage two, relink adds or removes an entry when a strategy is created or stopped. It belongs to stage two and is not built yet.

## Who uses it, and when

It is read by the prediction-market domain agent (stage two).

## Where it is mentioned

It is described in `agents/system/docs/rebuild-prompt.md` and its folder's How it works file `agents/trading/prediction-market/docs/docs.index.md`.

## Related knowledge

It has the same format as `agents/system/docs/subagents.link/`. It links to `agents/trading/prediction-market/strategy-1-agent/docs/`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `agents/system/CLAUDE.md` (section "Where the project is now: stage one"), `agents/trading/docs/README.md` (section "The trading domains"), `agents/system/docs/README.md` (section "How a level reaches its children") and `agents/system/docs/rebuild-prompt.md` (section "Child links").

## Keep in mind

- When you scan files, never follow this folder recursively; go down one `subagents.link/` at a time.
- When a link is missing or stale, let relink fix it; never add or remove a child link by hand.
