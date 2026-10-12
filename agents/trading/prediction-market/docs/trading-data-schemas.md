# Agent OS, prediction-market domain: Trading data schemas (v0.1)

The trading layer of the system's `data-schemas.md`: the domain's own config file [19.2.4], the trading fields of an agent config, trading account ids and their list, the decisions and orders in the logs, positions, the money part of the metrics snapshot, the domain's worker outputs, and the strategy's history and `strategy.md`. Read it together with `data-schemas.md`; a later trading domain copies it.

## Configs

### prediction-market-agents.config.json [19.2.4]
<!-- k: id=tr-schema-system-config applies=[19.6.9],[19.2.4],name:prediction-market-agents.config.link.json,[14.3],[14.1] sources=D-006,in-20260929-1537,D-027,D-029,D-056 status=proposed -->
General rule: see `data-schemas.md` (system.config.json [11.1]).

The domain's own config: the trading settings that sat in the system's [11.1] `system.config.json` until D-056. The sections are proposed, as they were in [11.1]. A section moves to its own file once it gets long (first candidate: `accounts`).

| Section | Fields | Meaning |
|---|---|---|
| `schema_version` | integer | shape version |
| `currency` | `USD` | the currency of the domain's money fields (was [11.1] `defaults.currency`); the rule that a field's name carries its unit stays general (`schema-encoding-time-units`) |
| `kill_switch` | bool | the order stop switch: refuse orders, close positions, set the account back to unfunded. The general [11.1] `modes.kill_switch` stops every outside action, orders included |
| `risk` | `domain.max_total_live_usd`, `domain.max_daily_loss_usd`, `domain.drawdown_stop_pct`; `per_agent.max_capital_usd`, `per_agent.max_position_pct`, `per_agent.max_open_positions`, `per_agent.max_orders_per_hour`; `per_venue` (fields open) | hard caps; lower layers may only tighten them |
| `accounts[]` | `id`, `venue`, `mode`, `funded`, `approved_by_owner`, `assigned_agent`, `max_capital_usd`, `secret_keys` | one trading account each; live needs `funded` and `approved_by_owner` |
| `notifications` | `events.<event>` (low, medium, high) for `live_trade`, `risk_limit_hit` | the domain's trade events; the channels and the general events stay in [11.1] `notifications` |
| `venues`, `fees_bps`, `market_filters`, default jobs | default jobs: fields open | the domain's defaults (were [11.1] `domains.prediction-markets`) |

```json
{
  "schema_version": 1,
  "currency": "USD",
  "kill_switch": false,
  "risk": { "domain": { "max_total_live_usd": 500, "max_daily_loss_usd": 50, "drawdown_stop_pct": 15 },
            "per_agent": { "max_capital_usd": 100, "max_position_pct": 5, "max_open_positions": 10, "max_orders_per_hour": 20 } },
  "accounts": [ { "id": "acct-pm-test-1", "venue": "polymarket", "mode": "test", "funded": false, "approved_by_owner": false,
                  "assigned_agent": "pm-strategy-1.momentum-v1.opus55-test", "max_capital_usd": 0, "secret_keys": ["POLYMARKET_ACCT1_*"] } ],
  "notifications": { "events": { "live_trade": "high", "risk_limit_hit": "high" } },
  "venues": ["polymarket"], "fees_bps": 0, "market_filters": { "min_volume_usd": 10000 }
}
```

- **Merge (proposed):** `run-agent` [14.1] merges this file after [11.1] and before each agent's own config [27.2] into `effective-config.json` (`schema-effective-config`); a lower layer may only tighten a limit.
- **Account keys:** an account's keys follow the system's pattern `[PROVIDER]_[ACCOUNT]_[WHAT]` (`schema-env-keys`), e.g. `POLYMARKET_ACCT1_API_KEY`, `POLYMARKET_ACCT1_WALLET_PRIVATE_KEY`. Configs and jobs name them by a prefix glob such as `POLYMARKET_ACCT1_*`. In the secrets index [47.3] that key group has `kind` `wallet` and the account id in `used_by` (`acct-pm-test-1`).
- **Writers:** the domain agent [19.1.5] and system-support agents; changes to `risk`, `accounts` and `kill_switch` need owner approval (recorded in decisions.md [2.6]).
- **Readers:** every agent of the domain through its file link `prediction-market-agents.config.link.json` (like [27.1]), `run-agent`, the decision and risk-check scripts [14.3] (`kill_switch`, `risk`, `accounts`), `load-secret` (`accounts`), the notifier (`notifications`) and the domain's dashboard [45].
- **Open:** the name `kill_switch` for the order stop switch is our proposal (D-058). The `global` caps covered the whole system while they sat in [11.1]; a cap across several trading domains, once one is copied from this one, has no home yet.

### Agent config: trading fields [27.2]
<!-- k: id=tr-schema-agent-config applies=[19.6.9],[27.2],[27] sources=D-006,D-012,D-014,D-022,D-027,D-029,D-031,D-056 status=proposed -->
The fields a trading agent's config adds to the general agent config (`schema-agent-config`).

| Field | Type | Req. | Meaning |
|---|---|---|---|
| `agent.type` | adds `strategy`, `variant` | yes | its level (D-022) |
| `agent.strategy` | text | variants | the strategy it belongs to |
| `mode` | `test`, `live` | yes | live also needs an owner-approved account in [19.2.4] `accounts` |
| `capital_and_risk.*` | the keys of [19.2.4] `risk.per_agent` | no | only tighter than [19.2.4] |
| `secret_keys` | key names or prefixes, e.g. `POLYMARKET_ACCT1_*` | no | the keys of its trading account |
| `strategy.<param>` | strategy specific | no | the strategy's knobs; a change makes a new variant |

```json
{
  "agent": { "name": "pm-strategy-1.momentum-v1.opus55-test", "type": "variant", "domain": "prediction-markets",
             "strategy": "strategy-1", "parent": null, "created": "2026-09-29" },
  "mode": "test",
  "capital_and_risk": { "max_capital_usd": 100, "max_position_pct": 3 },
  "secret_keys": ["POLYMARKET_ACCT1_*"],
  "strategy": { "momentum_window_h": 24, "entry_threshold": 0.08, "exit_threshold": -0.04 }
}
```

- **Level equivalents:** the domain level's config is [19.2.4]; whether it also carries an `agent` block like this file is open. The tree does not show one yet at the strategy level [21.2] (open).
- **Writers:** besides `create-agent` [14.1], the strategy SI sub-agent [21.1.1.1] and the domain agent [19.1.5] write new variants' configs.
- **In `effective-config.json`:** the agent's `capital_and_risk` and `strategy` are merged in with the rest (`schema-effective-config`).

## IDs and indexes

### Trading account IDs
<!-- k: id=tr-schema-other-ids applies=[19.6.9],[19.2.4],[19.6.18.1],[47.3] sources=D-025,D-029,derived,D-056 status=proposed -->
| Thing | Format | Unique within | Example |
|---|---|---|---|
| Trading account | text (format open) | the system | `acct-pm-test-1` |

The other ids are in `data-schemas.md` (`schema-other-ids`). An account id appears in [19.2.4] `accounts`, in `index/accounts.md` [19.6.18.1] and in `used_by` of the secrets index [47.3].

### index/accounts.md [19.6.18.1]
<!-- k: id=tr-schema-index-tables applies=[19.6.9],[19.6.18.1],[2.18.1] sources=D-012,D-029,D-030,D-056 status=proposed -->
A Markdown table like the system's index tables (`schema-index-tables`), one row per trading account. Columns: id, venue, mode, funded, approved_by_owner, capital (`max_capital_usd`), used_by, keys (key names only, never values), status. It takes over the `funded` column of the registry `agents.md` [2.18.1], which no longer has a `funded` or a `strategy` column; a trading agent's strategy shows in its name (`trading-conventions.md`) and its path.

```markdown
| id | venue | mode | funded | approved_by_owner | capital | used_by | keys | status |
|---|---|---|---|---|---|---|---|---|
| acct-pm-test-1 | polymarket | test | no | no | 0 | pm-strategy-1.momentum-v1.opus55-test | POLYMARKET_ACCT1_* | example |
```

## Logs

### runs.jsonl: decisions
<!-- k: id=tr-schema-runs-jsonl applies=[19.6.9],name:runs.jsonl*,[34],[33] sources=in-20260929-1452,derived,D-056 status=proposed -->
A trading agent's `decisions[]` in `runs.jsonl` (`schema-runs-jsonl`) carry the order:
- Fields: `market`, `action`, `size_usd`, `reason`; proposed also `price` and `prob`.
- `action` adds the order values `buy_yes`, `buy_no`, `sell`, `sell_all` (proposed, from the owner's run loop) to the general ones.
- `prob` is the agent's own probability for the outcome it trades. Calibration cannot be measured without it (`metric-calibration`).

```jsonl
{"run":"r-20260929-1000","agent":"pm-strategy-1.momentum-v1.opus55-test","mode":"test","job":"main-run","started":"2026-09-29T10:03:12Z","duration_s":88,"trigger":"important_change","inputs":["data/polymarket-prices.link.json@2026-09-29T10:05:00Z"],"decisions":[{"market":"0x5f1c...","action":"buy_yes","size_usd":3,"price":0.37,"prob":0.46,"reason":"24h momentum +0.11 > 0.08"}],"model":"opus-5.5","tokens_in":48211,"tokens_out":2310,"cost_usd":0.41,"status":"ok"}
```

### Run summary: orders
<!-- k: id=tr-schema-run-summary-md applies=[19.6.9],name:runs.jsonl*,[34] sources=derived,D-056 status=proposed -->
In a trading agent's `run-[date].md` (`schema-run-summary-md`), **Decided** names the orders and **Did** their fills:

```markdown
## r-20260929-1000 (important_change, test)
- Read: polymarket-prices 10:05 (187 markets, 12 moved > 5%), news-digest 09:58
- Decided: buy_yes 0x5f1c for $3 (24h momentum +0.11 > 0.08)
- Did: simulated fill at 0.37
- Cost: $0.41, 88 s
- Memory note: momentum signals cluster after Fed news; check spread before entry
```

### Order log [19.4.3]
<!-- k: id=tr-schema-log-services applies=[19.6.9],[19.4.3],[14.3],[33] sources=derived,D-056 status=proposed -->
One JSONL line per order action of an acting service, in the domain's `logs/services/[service]/` [19.4.3] (for example a Polymarket executor, `polymarket-exec/`). These lines are the source of every PnL number (`trading-metrics.md`). The general line is in `data-schemas.md` (`schema-log-services`).

| Field | Values | Meaning |
|---|---|---|
| `ts`, `service`, `mode`, `agent`, `account` | | who acted, where, in which mode |
| `action` | `place_order`, `cancel_order`, `close_position` | |
| `market`, `side`, `size_usd`, `price` | | the order |
| `result` | `simulated_fill`, `filled`, `partial`, `rejected`, `blocked_by_risk`, `blocked_by_kill_switch` | |
| `fee_usd`, `order_id` | | when known |

```jsonl
{"ts":"2026-09-29T10:04:40Z","service":"polymarket-exec","mode":"test","agent":"pm-strategy-1.momentum-v1.opus55-test","account":"acct-pm-test-1","action":"place_order","market":"0x5f1c...","side":"buy_yes","size_usd":3,"price":0.37,"result":"simulated_fill","fee_usd":0}
```

## Data outputs

### Worker outputs
<!-- k: id=schema-worker-outputs applies=[19.6.9],[19.5.3],[19.5.2],[19.3.5],[19.3.3],[35.2],[35.1],[31],[32] sources=D-007,D-010,derived,D-056 status=proposed -->
The folder layout and the envelope every output uses are in `data-schemas.md` (`schema-latest-files`). The rows of the domain's producers, which grow as workers are built:

| Producer | File | Rows |
|---|---|---|
| `polymarket-prices` (domain job in [19.2.1], script [19.3.5]) | `data/polymarket-prices/latest.json` [19.5.3] | `market`, `question`, `price_yes`, `volume_usd`, `ts` |
| `markets-catalog` (domain job, script [19.3.3]) | `data/markets-catalog/latest.json` [19.5.2] | `markets[]`: `id`, `question`, `category`, `liquidity_usd`, `resolves`, `tradable` |
| `get-polymarket-data` [31] | `data/get-polymarket-data/latest.json` | `id`, `question`, `price_yes`, `volume_usd` |

- The `polymarket-prices` draft is still a bare array of rows, not the envelope.

```json
{ "ts": "2026-09-29T10:00:00Z", "producer": "prediction-market-agents",
  "markets": [ { "id": "0x9a02...", "question": "Will BTC close above $120k on Oct 31?", "category": "crypto", "liquidity_usd": 480000, "resolves": "2026-10-31T23:59:00Z", "tradable": true } ] }
```

### Digests and the variant report
<!-- k: id=tr-schema-subagent-outputs applies=[19.6.9],name:news-digest.link.md,[35.1],[21.5] sources=D-008,D-021,derived,D-056 status=proposed -->
For trading agents each digest bullet (`schema-subagent-outputs`) names the market id and its question. The strategy's `data/variant-report/latest.md` [21.5] follows the same pattern.

```markdown
# news-digest: 2026-09-29 09:58 UTC
- 0x9a02 (Fed cut in November?) sentiment +0.4: two Fed speakers lean dovish. [source]
- 0x5f1c (BTC > $120k Oct 31) sentiment -0.2: ETF outflows for 3 days. [source]
```

### Metrics snapshot: money and forecasts
<!-- k: id=tr-schema-metrics-snapshot applies=[19.6.9],[35],[21.5],[19.6.11] sources=derived,D-056 status=proposed -->
A trading agent's `data/metrics/latest.json` (`schema-metrics-snapshot`) adds the money and forecast numbers: `capital_usd`, `pnl_usd` (`realised`, `unrealised`, `ai_cost`, `net`), `return_pct`, `trades`, `win_rate`, `max_drawdown_pct`, `current_drawdown_pct`, `brier`, `market_brier`, `resolved_forecasts`. At the strategy level, proposed: `data/variant-report/latest.json` next to the report `latest.md` [21.5]. Definitions of every number: `trading-metrics.md`.

```json
{ "schema_version": 1, "agent": "pm-strategy-1.momentum-v1.opus55-test", "mode": "test",
  "period": { "from": "2026-09-16T00:00:00Z", "to": "2026-09-30T00:00:00Z" }, "capital_usd": 100,
  "pnl_usd": { "realised": 4.2, "unrealised": -0.8, "ai_cost": 38.1, "net": -34.7 }, "return_pct": -34.7,
  "trades": 41, "win_rate": 0.56, "max_drawdown_pct": 6.1, "current_drawdown_pct": 2.0,
  "brier": 0.21, "market_brier": 0.23, "resolved_forecasts": 29,
  "runs": 1302, "cost_per_run_usd": 0.03, "tokens_in": 51200000, "tokens_out": 2900000,
  "median_run_sec": 71, "error_rate": 0.01, "tests": { "passing": 12, "failing": 1 } }
```

### Portfolio and positions
<!-- k: id=schema-positions applies=[19.6.9],[35],[19.4.3] sources=derived,D-056 status=open -->
Where positions live is open ([35]; the vision notes' `vis-idea-ledger` proposes a ledger that owns the portfolio, with agents seeing a read-only snapshot). Until then positions are rebuilt from the order log [19.4.3]. A position record needs at least: `agent`, `account`, `market`, `side`, `shares`, `avg_price`, `opened`, `closed`, `realised_pnl_usd`.

## Agent docs

### The strategy's history and a variant's changes.md
<!-- k: id=tr-schema-changes-md applies=[19.6.9],[21.5],[46.6] sources=D-020,D-022,D-025,D-031,D-056 status=proposed -->
- **A variant's own** `docs/changes.md` ([46.6]) has the general shape (`schema-changes-md`); its **What differs** names the strategy knobs it changed.
- **The strategy's cross-variant history** `data/changes.md` ([21.5]): one entry per event (variant created, retired or folded back): date, variant, parent, change, result, decision.

```markdown
# changes.md: pm-strategy-1.momentum-v2.opus55-test
Parent: pm-strategy-1.momentum-v1.opus55-test · Created by: pm-strategy-1-self-improvement-agent · 2026-09-22

## What differs
- strategy.momentum_window_h: 24 -> 6 (research r-0001)

## Being tested
- Win rate and drawdown over 14 days in test mode vs the parent
```

### strategy.md
<!-- k: id=tr-schema-agent-docs applies=[19.6.9],[46.5],[21.6] sources=D-017,D-022,D-056 status=proposed -->
Besides README, decisions and notes (`schema-agent-docs`), every agent of the domain keeps `strategy.md` ([46.5] for the example variant): its strategy in plain words. At the strategy level [21.6] this holds the strategy definition itself (proposed home, [21]).

## Changelog
- v0.1 (2026-10-07): created from the trading parts of the system's `data-schemas.md` v0.1 (D-056, D-058); the copy-trading `whale-signals` output row and link examples were left out (copy trading retired, D-056).
