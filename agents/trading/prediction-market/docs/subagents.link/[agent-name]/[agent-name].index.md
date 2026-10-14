---
about: agent-os/agents/trading/prediction-market/docs/subagents.link/[agent-name]/
basis: 981c7ce4dc3d
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T15:07:13Z
---
# [agent-name]/

## What it is

The name pattern for one folder link per strategy, named after the strategy's folder (for example `strategy-1-agent/`) and pointing at that strategy's `docs/`. Through it the domain would read the strategy's docs without copies, and its variants' docs one `subagents.link/` further down. Relink, a planned shared script, is meant to build and remove it; it is read-only and never listed in a links file.

## Who looks after it

It is written by relink (stage two script).

## When and how it changes

In stage two, relink makes a real link when a strategy is created and removes it when the strategy is stopped. It is a name pattern, not a real item: it tells what each item made from it will hold.

## Who uses it, and when

It is read by the prediction-market domain agent (stage two).

## Where it is mentioned

It is described in `agents/system/docs/rebuild-prompt.md` and its folder's How it works file `agents/trading/prediction-market/docs/subagents.link/subagents.link.index.md`.

## Related knowledge

It links to `agents/trading/prediction-market/strategy-1-agent/docs/`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `agents/system/CLAUDE.md` (section "Where the project is now: stage one"), `agents/trading/docs/README.md` (section "The trading domains") and `agents/system/docs/rebuild-prompt.md` (section "Child links").

## Keep in mind

- When you need a strategy's files changed, leave it to the strategy; the domain writes only its own files.
