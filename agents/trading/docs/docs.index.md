---
about: agent-os/agents/trading/docs/
node: n-56.1
basis: 9c4909c8090e
written: 2026-10-12T00:00:00Z
by: knowledge-base-agent
confirmed: 2026-10-12T15:40:56Z
---
# docs/

## What it is

Trading's own docs, for people and for AI: `vision.md` (why trading has its own place and what every trading domain shares), `README.md` (every part of trading exactly, with each part's docs path), `README.asd.md` (the README again in ASD-STE100) and `rebuild-prompt.md` (how an AI builds `agents/trading/` again). Each doc has its How it works, Details, Example and Questions files next to it.

## Who looks after it

The knowledge base agent, with one skill per doc: `vision-doc`, `readme-doc`, the planned `readme-asd-doc` and `rebuild-prompt-doc`. The owner can change any doc on the File Tree page.

## When and how it changes

After an input or a decision that touches what every trading domain shares, the docs are rewritten in a fixed order: the vision, the README, its ASD-STE100 version, then the rebuild prompt. A change here then climbs to the system's docs above.

## Who uses it, and when

The owner and anyone new to trading, first; every trading domain agent as background; an AI rebuilding trading.

## Where it is mentioned

The system's README and rebuild prompt, the folder `agents/trading/`, and every trading domain's docs, which build on these.

## Related knowledge

They sit between the system's docs in `agents/system/docs/` and each trading domain's docs.

## Keep in mind

- When you change one doc here, bring the others in line in the order vision, README, README.asd, rebuild prompt.
- When you write here, describe only what every trading domain shares.
