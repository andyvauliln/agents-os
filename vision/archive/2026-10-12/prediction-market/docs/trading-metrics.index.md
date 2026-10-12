---
about: agent-os/agents/trading/prediction-market/docs/trading-metrics.md
node: n-19.6.11
basis: 3def12fb3d78
written: 2026-10-07T18:56:50Z
by: knowledge-base-agent
---
# trading-metrics.md

## Summary

How trading agents are measured on money, the trading layer of the system's `metrics.md`: capital, PnL and return, win rate, drawdown, calibration against the market and cost per trade; the rules for comparing variants like for like; champion and challengers in the strategy loop; the daily variant report; when a variant goes live, is cut back or retired; and what the dashboard shows. Almost all of it is proposed, and the owner has set no thresholds yet.

## Keep in mind

- When you compare variants, use the same period and capital, test against test, net of AI cost, and never call a winner below the minimum data.
- When you weigh a backtest, use it for research only; only forward results in test mode decide a promotion.
