# Agent OS, prediction-market domain: Accounts index (v0.1)

The trading layer of the system's `index/agents.md`: every trading account of the domain [19.6.18.1], with its venue, whether it is funded, whether the owner approved it, its capital and the agent that uses it. The system's agents list no longer keeps a `funded` column (D-058). It is written by hand for now, from the `accounts` of the domain config [19.2.4] and the secrets index [47.3]. Read it together with `index/agents.md`; a later trading domain copies it.

## Accounts
<!-- k: id=tr-idx-agents applies=[19.6.18.1],[19.2.4],[47.3],[27.2] sources=D-012,D-022,D-023,D-027,derived,D-056 status=proposed -->
General rule: see `index/agents.md` (Agents).

Nothing is built yet, so no account exists and none is funded. The only account the docs name is an example. Fields: `id`, `venue`, `mode`, `funded`, `approved_by_owner`, capital (`max_capital_usd`), `used_by` (the assigned agent) and the key names it uses (never values).

| id | venue | mode | funded | approved_by_owner | capital (`max_capital_usd`) | used_by | keys | status |
|---|---|---|---|---|---|---|---|---|
| `acct-pm-test-1` | polymarket | test | no | no | 0 | `pm-strategy-1.momentum-v1.opus55-test` | `POLYMARKET_ACCT1_*` | example |

- **Where it comes from:** the `accounts` example of the domain config (`trading-data-schemas.md`; before the move, data-schemas.md `schema-system-config`) and the secrets index example [47.3], whose `used_by` names this account.
- **Funded column:** the system's agents list said `funded: no` for every prediction-market agent; funding now lives only here and in [19.2.4] `accounts`.
- **Open:** the account id format (trading-data-schemas.md, `tr-schema-other-ids`: "format open").

## Changelog
- v0.1 (2026-10-07): created from the `funded` column of the system's `index/agents.md` v0.1, the `accounts` example of [11.1] and the secrets index [47.3] (D-056, D-058).
