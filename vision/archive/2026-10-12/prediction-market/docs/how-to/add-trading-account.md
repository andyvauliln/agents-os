# Agent OS, prediction-market domain: Add a trading account (v0.1)

The trading layer of the system's `how-to/add-account-or-secret.md`: how to add a trading account at a venue, with its keys or wallet, and give it to the trading agent that uses it. The money rules are in `trading-safety.md`. Read it together with `how-to/add-account-or-secret.md`; a later trading domain copies it.

## Steps
<!-- k: id=tr-howto-add-account-or-secret-steps applies=[19.6.17.3],[19.2.4],[19.6.18.1],[47.1.1],[47.3],[14.1],[31] sources=D-023,D-027,in-20260930-0804,in-20260930-0812-2,D-056 status=proposed -->
General rule: see `how-to/add-account-or-secret.md` (Steps). Each item below adds to the general step with the same number.

- **Step 1:** the owner creates the account and its key or wallet at the venue.
- **Step 2:** test key names carry a prefix per account, e.g. `POLYMARKET_ACCT1_API_KEY` in [47.1.1].
- **Step 5:** the account goes into the domain config [19.2.4] `accounts` (id, venue, mode, funded, `approved_by_owner`, assigned agent, max capital, ref), and into the domain's `index/accounts.md` [19.6.18.1]. A live entry needs owner approval.
- **Step 7:** a test run with the test key, e.g. `load-secret POLYMARKET_ACCT1_* -- python3 scripts/get-polymarket-data.worker.py` (like [31]).
- **Step 9:** rotation ends by revoking the old key at the venue.

## Checks
<!-- k: id=tr-howto-add-account-or-secret-checks applies=[19.6.17.3],[19.2.4],[19.6.18.1],[14.1] sources=D-023,D-027,D-028,D-056 status=proposed -->
- `load-secret` refuses live keys unless the agent is live-allowed with an owner-approved account.
- The account has its row in `index/accounts.md` [19.6.18.1].

## Changelog
- v0.1 (2026-10-07): created from the trading parts of the system's `how-to/add-account-or-secret.md` v0.1 (D-056, D-058).
