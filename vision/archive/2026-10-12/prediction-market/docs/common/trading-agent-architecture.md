# Agent OS, prediction-market domain: Trading agent architecture (v0.1)

The trading layer of the system's `common/agent-architecture.md`: what a trading agent's run may decide (buy, sell, sell all), how it acts through its decision scripts, where the history across a strategy's variants lives, and the open questions about trading decisions and positions. Read it together with `common/agent-architecture.md`; a later trading domain copies it.

## The run loop of a trading agent
<!-- k: id=tr-common-agent-run-loop applies=[19.6.16.1],[24.5],[33],[23] sources=in-20260929-1452,in-20260929-1455,D-056 status=decided -->
General rule: see `common/agent-architecture.md` (The run loop).

A trading agent's run may also decide to buy, sell or sell all. A trading agent is one harness, platform and model; it runs one run at a time, and each run takes all new data since the last one.

### How a trading run acts
<!-- k: id=tr-common-agent-run-start applies=[19.6.16.1],[33],[14.3],[30.1] sources=D-021,D-029,D-056 status=proposed -->
When a trading agent decides (step 4 of "How a run starts" in `common/agent-architecture.md`), its actions go only through its decision scripts (like [33]), which read the mode and call the shared risk check [14.3] (linked as [30.1]).

## Memory across variants
<!-- k: id=tr-common-agent-memory applies=[19.6.16.1],[21.5],[46.6] sources=D-024,D-025,D-056 status=proposed -->
The cross-variant history lives in the strategy's `data/` [21.5], and each variant's own change record in its `docs/changes.md`. A trading agent's own memory and its "previous and next run" info have no home yet.

## Open questions
<!-- k: id=tr-common-agent-open applies=[19.6.16.1],[33],[35] sources=derived,D-056 status=open -->
- Is a trading decision made by code, by the LLM, or both ([33])?
- Where are portfolio and positions kept ([35])?

## Changelog
- v0.1 (2026-10-07): created from the trading parts of the system's `common/agent-architecture.md` v0.1 (D-056, D-058).
