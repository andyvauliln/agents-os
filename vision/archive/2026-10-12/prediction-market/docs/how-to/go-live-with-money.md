# Agent OS, prediction-market domain: Go live with money (v0.1)

The trading layer of the system's `how-to/promote-to-live.md`: how a test trading agent gets real money. Only the owner approves a funded account, in the UI (vision §12). The money rules are in `trading-safety.md`; the promotion criteria are in `trading-metrics.md` [19.6.11]. Read it together with `how-to/promote-to-live.md`; a later trading domain copies it.

## Steps
<!-- k: id=tr-howto-promote-to-live-steps applies=[19.6.17.2],[19.6.11],[19.2.4],[47.2.1],[19.4.3],[19.6.18.1] sources=D-012,D-023,D-025,D-027,D-029,in-20260929-1455,D-056 status=proposed -->
General rule: see `how-to/promote-to-live.md` (Steps). Each item below adds to the general step with the same number.

- **Step 1, the criteria:** results over the same period and capital as the other variants (test against test), with the promotion criteria in `trading-metrics.md` [19.6.11].
- **Step 2, the proposal:** the strategy agent or its SI sub-agent proposes the promotion.
- **Step 3, the approval:** nothing else can approve live money.
- **Step 4, a funded account:** the owner creates the account and puts its live keys in [47.2.1] `.secrets/live/.env` with the same key names as in test (see `how-to/add-trading-account.md`). In the domain config [19.2.4] `accounts` the account gets `mode: live`, `funded`, `approved_by_owner: true`, the assigned agent and `max_capital_usd`.
- **Step 7, monitoring:** orders are logged in the services logs [19.4.3]; the `live_trade` and `risk_limit_hit` notifications go to the owner. The order stop switch [19.2.4] stops orders (`trading-safety.md`).
- **Step 8, the registry:** the account's row in the domain's `index/accounts.md` [19.6.18.1] says funded yes.

## Checks
<!-- k: id=tr-howto-promote-to-live-checks applies=[19.6.17.2],[19.2.4],[47.2.1],[19.6.18.1],[27.2] sources=D-012,D-023,D-027,D-056 status=proposed -->
- The account shows `approved_by_owner: true`.
- `load-secret` hands live keys only to this agent's approved runs with an owner-approved account.
- The risk caps in its config are no looser than the domain config's `risk` [19.2.4].
- The order stop switch is off, and the owner got the `live_trade` notification for the first trade.

## Changelog
- v0.1 (2026-10-07): created from the trading parts of the system's `how-to/promote-to-live.md` v0.1 (D-056, D-058).
