# Agent OS, prediction-market domain: Trading feature map (v0.1)

The trading layer of the system's feature map: which files hold this domain's trading logic (data defaults and the price collector, the run loop with orders, decision and execution, the strategy loop, strategies and variants, the dashboard, trading analytics, money safety) and the trading gaps. Read it together with the system's `feature-map.md`; a later trading domain copies it. Section numbers follow the system's feature map, which holds every general row. Numbers `[n]` refer to `file-tree.md`. **(proposed)** marks anything not stated by the owner.

Agent types, beyond the system's: **Main** = a trading agent (strategy, decisions) · **Strategy** = strategy-level agent [21] (D-022) · **SI** = self-improvement sub-agent, here also at the strategy level [21.1.1.1].

## 1. Data collection (workers)
<!-- k: id=tr-fm-data-collection-workers applies=[19.2.4],[19.2.1],[19.3.5],[19.5.3],[19.4.2] sources=derived,D-056 status=decided -->
General rule: see the system's `feature-map.md` (1. Data collection).

| Logic in plain words | Files / folders | Owner |
|---|---|---|
| Per-domain defaults (venues, fees, filters) | [19.2.4] `prediction-market-agents.config.json` (was the `domains` section of [11.1], D-058) | Domain, Support |
| The Polymarket price collector, a job of this domain (was the system's shared-worker example) | [19.3.5] `polymarket-prices.worker.py`, its job in [19.2.1], its data [19.5.3] `data/polymarket-prices/`, its run logs [19.4.2] | Domain |

## 4. Agent run loop
<!-- k: id=tr-fm-agent-run-loop applies=[24.5],[33],[35],[27.2],[19.2.4],[45] sources=derived,D-056 status=decided -->

| Logic | Files / folders | Owner |
|---|---|---|
| Instructions: strategy, loop, allowed actions (buy, sell, sell all) | [24.5] `.claude/CLAUDE.md`, with the trading layer `common/trading-prompt.md` | Main |
| Read data → analyse → decide → act through decision scripts | [24.5], [33] `make-buy.decision.js`, [35] | Main |
| Trading agent config: capital and risk next to the mode and workers (D-014) | [27.2] `[agent-name].config.json`; the domain config [19.2.4] through a file link | Main, SI |
| Config merge for trading (proposed): risk tighten-only, live only with an owner-approved account, the order stop switch wins; owner overrides from the dashboard | [19.2.4], [27.2], [45] | Support |

## 5. Decision and execution (test / live)
<!-- k: id=tr-fm-decision-and-execution-test-live applies=[33],[30],[14.3],[19.2.4],[27.2],[19.6.8] sources=derived,D-056 status=decided -->

| Logic | Files / folders | Owner |
|---|---|---|
| Decision/action scripts (`*.decision.*`) | [33] `make-buy.decision.js`, [30] `scripts/`, the domain's shared blocks [14.3] `scripts/decisions/` | Main |
| The order stop switch: refuse orders, close positions, unfund the account (proposed default, D-058) | [19.2.4], [19.6.8] `trading-safety.md` | Support |
| Hard risk limits in code, separate from the LLM (proposed, vision §5.3) | [19.6.8] `trading-safety.md` (rules), [19.2.4] `risk` section (tighten-only caps); no executor file yet | Support |

## 6. Self-improvement wheel
<!-- k: id=tr-fm-self-improvement-wheel applies=[21.1.1.1],[21],[23],[21.5],[21.4],[21.6.1.1],[46],[27.3],[19.6.11],[19.6.17.1],[19.1.5] sources=derived,D-056 status=decided -->

| Logic | Files / folders | Owner |
|---|---|---|
| Strategy-level SI and its cross-variant history | [21.1.1.1] SI sub-agent; data/logs [21.5]/[21.4] (cross-variant `changes.md`) | SI |
| Compare variants and decide promotion/retirement | [19.6.11] `trading-metrics.md` | SI, Domain, Owner |
| Produce a new configuration/code as a new test variant | [21.1.1.1] → new [23]-style folder, [19.6.17.1] `how-to/create-strategy-or-variant.md` | SI |
| Whether a link change makes a new variant is open (proposed) | [27.3], [46] `changes.md`; `trading-roadmap.md` `road-q-new-variant` | SI, Main |
| Record what changed in each variant | the variant's own [46] `docs/changes.md` (its strategy reads it through [21.6.1.1]); cross-variant history in [21.5] | SI |
| Domain-level: find/create/update strategies and their SI sub-agents | [19.1.5] domain `.claude/CLAUDE.md` (domain owner); [21] | Domain |

## 7. Agent creation
<!-- k: id=tr-fm-agent-creation applies=[21.1.5],[21.11],[19.6.7],[23],[21],[2.18.1],[21.1.1.1],[21.2.1],[45],[19.6.17.1] sources=derived,D-056 status=decided -->

| Logic | Files / folders | Owner |
|---|---|---|
| Strategy manager: runs and compares its variants, coordinates its SI | [21.1.5] strategy `.claude/CLAUDE.md`, [21.11] `start.sh` | Strategy |
| Variant names start with their strategy: `[strategy-id].[own-name]-v[N].[platform-model]-[test\|live]`; the strategy agent's ID carries its platform/model and mode (D-032) | [19.6.7] `trading-conventions.md` naming rule, [23], [21], [2.18.1] | Strategy, Support |
| Strategy self-improvement loop: the strategy agent creates, tests and compares its own variants and folds winners back (D-032) | [21.1.5] strategy `CLAUDE.md`, [21.1.1.1] SI sub-agent, [21.2.1] workers file | Strategy, SI |
| Create a new strategy or variant | [19.6.17.1] `how-to/create-strategy-or-variant.md` | Support, Domain, SI |
| Show a new trading agent in the domain's dashboard | [45] `apps/trading-ui/` | Support |

## 9. The domain's dashboard: monitoring and control
<!-- k: id=tr-fm-ui-monitoring-and-control applies=[45],[19.2.4],[19.6.17.2],[19.6.17.4],[19.6.11] sources=derived,D-056 status=decided -->
`apps/trading-ui/` [45] is this domain's dashboard, empty for now; the project IDE [53] may do its job (owner, 2026-10-06).

| Logic | Files / folders | Owner |
|---|---|---|
| Performance, logs, data used/produced, decisions, improvements of the trading agents | [45] reading the shared logs and data and this domain's, level by level (D-030); [19.6.11] `trading-metrics.md` | Support |
| Approve/reject a funded live account; stop/delete (writes [19.2.4] `accounts` and the system's `modes`) | [45], [19.6.17.2] `how-to/go-live-with-money.md`, [19.6.17.4] `how-to/stop-trading-agent.md` | Owner |

## 10. Logging and analytics
<!-- k: id=tr-fm-logging-and-analytics applies=[19.6.11],[19.4.2],[19.4.3],[34] sources=derived,D-056 status=decided -->

| Logic | Files / folders | Owner |
|---|---|---|
| Performance metrics per trading agent (PnL, win rate, …) | [19.6.11] `trading-metrics.md` (definitions + promotion rules); no computing script yet | Support, SI |
| Order logs of the domain's acting services, the source of every PnL number | [19.4.3] `logs/services/[service]/` | Support |
| Run logs of the domain's jobs, such as the Polymarket price collector | [19.4.2] `logs/jobs/[job-id]/` | Support |

## 12. Safety and risk
<!-- k: id=tr-fm-safety-and-risk applies=[19.6.8],[19.2.4],[19.6.18.1],[19.6.17.3],[47],[14.1] sources=derived,D-056 status=decided -->

| Logic | Files / folders | Owner |
|---|---|---|
| Rules: owner approval for money, the order stop switch, risk limits | [19.6.8] `trading-safety.md` | Owner |
| Hard money limits enforced in code | [19.2.4] `risk` section; no enforcing file yet | Support |
| Wallets and trading accounts: configs hold key names and account refs only | [19.2.4] `accounts`, [19.6.18.1] `index/accounts.md`; runbook [19.6.17.3] `how-to/add-trading-account.md`; the keys themselves in the system's `.secrets/` [47] | Owner, Support |
| Trade notifications (`live_trade`, `risk_limit_hit`) | [19.2.4]; the system's notifier in [14.1] | Owner, Support |

## 13. Gaps: trading features with no files yet
<!-- k: id=tr-fm-gaps applies=[33],[19.6.11],[50],[21.13],[49] sources=derived,D-056 status=open -->
These were gaps 1, 2, 4 and 11 of the system's feature map before its v1.13.

1. **Executor / risk-check layer.** Trades go through [33] only; there is no separate executor or risk-enforcement script.
2. **Portfolio, positions and trading accounts.** These were in the v0.1 agent folder but are missing from the v0.2 layout (ledger idea, vision §5.4).
3. **Trading analytics.** PnL, win rate and the other trading metrics are defined in [19.6.11] `trading-metrics.md`, but there is no script that computes them and no stored results file.
4. **Backtesting.** Partly placed by D-025: backtest runs and outputs can live as research items ([50], [21.13]) and a guarding test in [49]; no backtest engine, historical data store or schema yet (open in [49]).

## Changelog
- v0.1 (2026-10-07): created from the trading parts of the system's `feature-map.md` v1.12 (D-056, D-058).
