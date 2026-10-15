---
about: agent-os/agents/trading/researches/
basis: f830bba71381
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T19:42:37Z
---
# researches/

## What it is

The research studies, real files that were in the repository before any trading agent: the prediction-market research (forty-two studies of ways to make money on prediction markets, with their evidence and the pipeline that wrote them), a study of agents that improve themselves, and a study of how trading agents are built (nine architecture specs with their diagrams). The folder keeps the owner's name `researches/`; each agent's own research history lives in its own `research/` folder instead.

## Who looks after it

It is written by the owner (moved the studies here from the repository's top-level researches/), the Polymarket strategy survey sessions (2026-09-20 to 2026-09-29) and the trading-agent architecture and self-improving agents research sessions (2026-09-22).

## When and how it changes

It changes when a new study folder is added, a study is resumed (the survey's files 58 to 84 and stage 3 are still open), or the owner moves or renames a study.

## Who uses it, and when

It is read by the owner; knowledge-base-agent (when it writes the trading docs); and the prediction-market domain agent, when it chooses strategies (stage two).

## Where it is mentioned

It is described in `agents/trading/docs/README.md`, `agents/trading/docs/README.asd.md`, `docs/file-tree.md` and its folder's How it works file `agents/trading/trading.index.md`.

## Related knowledge

It links to `agents/trading/researches/prediction-market-research/`, `agents/trading/researches/self-improving-agents/` and `agents/trading/researches/trding-agents-arhiteches/`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `docs/metadata.md` and `agents/trading/docs/README.md` (section "Research studies").

## Keep in mind

- When you add a study, put it in its own folder here and give it and its files their metadata files.
- When a study leads to a decision, record the decision and link the study; never edit a study's evidence after the fact.
