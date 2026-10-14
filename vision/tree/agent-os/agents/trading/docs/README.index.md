---
about: agent-os/agents/trading/docs/README.md
node: n-56.1.1
basis: 144895ef93fd
written: 2026-10-14T12:00:00Z
by: knowledge-base-agent
confirmed: 2026-10-12T15:40:56Z
---
# README.md

## What it is

Trading's README: the full, exact description of every part of `agents/trading/` and of what every trading domain holds, with the path to each part's own docs. It describes parts from the outside, never the logic inside an agent.

## Who looks after it

The knowledge base agent writes it with the `readme-doc` skill, after the vision and before the ASD-STE100 version and the rebuild prompt. The owner can also change it on the File Tree page.

## When and how it changes

It changes after every change to a part of trading: a new or removed trading domain, a new study in the research folder, a settled design point, a change to names, accounts, test and live or metrics. The agent rewrites the parts touched, checks that every "Its docs" path exists, and updates "Still open in the design".

## Who uses it, and when

Readers who have read the vision and want the exact picture; the owner after a round of changes; every agent before it works on a part of trading it does not know.

## Where it is mentioned

Trading's vision names it in its last section; the system's README gives it as the docs of trading's domains; `README.asd.md` is written from it; trading's rebuild prompt follows it.

## Related knowledge

Its In short uses the vision's words. `README.asd.md` must say the same in ASD-STE100. The rebuild prompt builds what it describes. The detail of each trading rule is in the trading notes in `agents/trading/prediction-market/docs/`. The system level stays general: nothing about money, markets or orders is written there.

## Keep in mind

- When you change this file, update `README.asd.md` next, with the same headings.
- When a trading domain is added or removed, add or remove its section part, its row in the docs table and its line in the system's README.
- When a part has no docs of its own yet, give its folder's How it works file as its docs path.
