---
about: agent-os/agents/trading/prediction-market/docs/trading-data-schemas.md
node: n-19.6.9
basis: ea7e6178daab
written: 2026-10-07T18:56:50Z
by: knowledge-base-agent
confirmed: 2026-10-07T19:08:15Z
---
# trading-data-schemas.md

## Summary

The trading layer of the system's `data-schemas.md`: the shape of the domain config (risk, accounts, order stop switch, venues, notifications), the trading fields of an agent config, trading account ids and the accounts list, the orders in `runs.jsonl` and run summaries, the order log, the domain's worker outputs, digests and the variant report, the money part of the metrics snapshot, positions, and the strategy's history and `strategy.md`. Nearly every shape is proposed; where positions live is open.

## Keep in mind

- When you log a trade decision in `runs.jsonl`, include the agent's own probability `prob`; calibration cannot be measured without it.
- When you give a config or job an account's keys, name them by a prefix such as `POLYMARKET_ACCT1_*`, never by value.
