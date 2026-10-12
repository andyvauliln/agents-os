# Agent OS, prediction-market domain: Trading glossary (v0.1)

The trading layer of the system's glossary: the words for strategies, trading agents and their variants, champion and challenger, decision scripts and the domain config. Read it together with the system's `glossary.md`, which holds every general term; a later trading domain copies it. Terms are in alphabetical order. The money metrics (PnL, win rate, drawdown, calibration) are defined in `trading-metrics.md`. Numbers [n] are the objects in file-tree.md.

## Terms

### Champion and challenger
<!-- k: id=term-champion-challenger applies=[19.6.11] sources=in-20260929-1452,D-056 status=proposed -->
An idea under evaluation: self-improvement makes a challenger that is tested against the current best agent, the champion, and replaces it only if it does better. The strategy loop (D-032) is scored this way: `trading-metrics.md` `metric-champion`.

### Decision script
<!-- k: id=term-decision-script applies=name:*.decision.*,[14.3] sources=D-007,in-20260929-1455,D-056 status=decided -->
A script named `[name].decision.[ext]` that makes or checks a trading action, such as buy, sell or a risk check. It reads the mode from config; the domain's shared ones live in `scripts/decisions/` [14.3]. `decision` is this domain's own script kind; the system's kinds are `worker` and `system` (proposed default, D-058).

### Domain config
<!-- k: id=tr-term-system-config applies=[19.2.4] sources=D-006,in-20260929-1537,D-056 status=decided -->
`prediction-market-agents.config.json` [19.2.4]: this domain's own config, with what the system config held for trading: risk limits, trading accounts, venues, fees, market filters, default workers, the currency, the order stop switch and trade notifications (proposed default, D-058). The system config itself: the system's glossary, System config.

### Level agent (in this domain)
<!-- k: id=tr-term-level-agent applies=[19],[21] sources=D-022,D-056 status=decided -->
In this domain the managing agents are the domain agent [19] and the strategy agents [21], above the trading variants. Detail: `trading-architecture.md`.

### Strategy
<!-- k: id=term-strategy applies=[21.6] sources=in-20260929-1452,D-022,D-056 status=decided -->
One way to make money in a domain, such as market making. Its definition is kept by its strategy agent (in `docs/` [21.6], proposed) and run by its variants.

### Strategy agent
<!-- k: id=term-strategy-agent applies=[21] sources=D-022,D-032,D-056 status=decided -->
The level agent [21] responsible for one strategy. Through its SI sub-agent it creates variants of itself, compares them and folds winning changes back (D-032). Its ID carries its main platform/model and mode, e.g. `pm-strategy-1-agent.opus55-test`.

### Trading agent
<!-- k: id=tr-term-agent applies=[23] sources=in-20260929-1452,in-20260929-1455,D-022,D-056 status=decided -->
The agents of this domain are its domain agent, its strategy agents and its trading variants. A trading agent is a trading variant [23]; its prompt is the trading agent prompt [24.5].

### Variant (modification)
<!-- k: id=term-variant applies=[23] sources=D-022,D-032,in-20260930-1453-2,D-056 status=decided -->
One trading agent under a strategy: the strategy with one set of changes, one platform/model and one mode, e.g. `pm-strategy-1.momentum-v1.opus55-test` [23]. Its name starts with its strategy's ID. It is this domain's form of a version (the system's glossary, Version).

## Changelog
- v0.1 (2026-10-07): created from the trading parts of the system's `glossary.md` v0.1 (D-056, D-058); `term-champion-challenger`, `term-decision-script`, `term-strategy`, `term-strategy-agent` and `term-variant` moved here whole.
