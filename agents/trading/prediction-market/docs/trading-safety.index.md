---
about: agent-os/agents/trading/prediction-market/docs/trading-safety.md
basis: baffb209619a
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T15:07:13Z
---
# trading-safety.md

## What it is

An earlier note with the domain's money rules: only the owner approves an account with real money; a live order needs a funded, owner-approved account; risk caps sit in the domain config, are enforced in code and may only be tightened below; and an order stop switch refuses orders. It is kept for stage two and not referenced now.

## Who looks after it

Nobody writes it now.

## When and how it changes

Not changed until the owner starts stage two; then the domain's docs are written from it.

## Who uses it, and when

Nobody reads it now.

## Where it is mentioned

It is described in `agents/trading/docs/README.md` and its folder's How it works file `agents/trading/prediction-market/docs/docs.index.md`.

## Related knowledge

The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `agents/system/CLAUDE.md` (section "Where the project is now: stage one") and `agents/trading/docs/README.md` (section "The trading domains").

## Keep in mind

- When stage two starts, write the domain's own docs from this note; until then, do not point to it from another file.
