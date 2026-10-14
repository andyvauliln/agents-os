---
about: agent-os/agents/trading/prediction-market/docs/trading-flows.md
basis: fcb6b723e682
written: 2026-10-07T18:56:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T15:07:13Z
---
# trading-flows.md

## Summary

The trading layer of the system's `flows.md`: the order steps of a trading run; decision to execution, from the decision script through the risk check in code to a simulated fill in test or a real order in live, each logged in the order log; logs to the dashboard; the self-improvement wheel with the strategy loop; and the owner's flows for creating, reviewing, going live, stopping and approving risk or account changes. The flows are proposed.

## Keep in mind

- When you block an order on a risk cap or a stop switch, log it in the order log and send the owner `risk_limit_hit`.
