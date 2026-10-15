# Agent OS: Metrics (v0.2)

How any agent is measured, whatever its domain: its AI cost and tokens, how long its runs take, its errors and its tests, and what it needs before it may go live. The owner asked for this doc (in-20260929-1520) and set its aim: run many agents side by side, compare them and keep what works. Which metrics decide success is still an open owner question, so almost everything here is our proposal. Trading adds its own rules in the prediction-market domain's `trading-metrics.md`: capital, PnL, win rate, drawdown, calibration, comparing variants, champion and challengers, promotion thresholds, demotion, retirement and what its dashboard shows. The logs the numbers come from are in data-schemas.md.

## The metrics

### Period and mode
<!-- k: id=metric-basis applies=[2.16],[34],[35] sources=derived,D-056 status=proposed -->
- Every number belongs to one agent, one mode and one period (`from` and `to`, UTC). Test and live numbers are never mixed; a live agent is a separate agent anyway (D-012).
- Standard periods: since creation, the last 7 days and the last 14 days.
- Trading adds its own rules in the prediction-market domain's `trading-metrics.md` (capital, money, the comparison window).

### Cost and tokens
<!-- k: id=metric-cost applies=[2.16],name:runs.jsonl*,path:agents/**/logs,[15.1],[15.4],[11.1],[11.11],name:*.workers.json sources=in-20260929-1455,D-029,derived,D-056 status=proposed -->
- `ai_cost_usd`: total AI cost in the period, the sum of `cost_usd` over the agent's runs in `runs.jsonl` and its other AI jobs in `logs/jobs/*/history.jsonl` [34]. `cost_per_run_usd`: AI cost of main runs divided by the number of main runs; cancelled runs count, since they cost money.
- `tokens_in` and `tokens_out`: totals from `runs.jsonl` and the job logs.
- The system log [15.1] (`costs` lines) gives the same numbers across all agents. Caps: [11.1] `schedules.max_ai_cost_usd_per_day` for the whole system, a job's `max_cost_usd` for one run.
- Sub-agents shared by many agents (e.g. a news digest, [15.4]) count to the level that runs them, not to the readers (open).
- Route matters: the model comes from the job or [11.11], so the same agent on a cheaper model is a new version to compare on cost.
- Trading adds its own rules in the prediction-market domain's `trading-metrics.md` (cost per trade).

### Latency
<!-- k: id=metric-latency applies=[2.16],name:runs.jsonl*,[15.1],[15.2] sources=derived,D-056 status=proposed -->
- **Run time:** median and 95th percentile of `duration_s` of main runs (`runs.jsonl`).
- **Reaction time:** from an important change (`important_change` in [15.1]) to the action it led to (in the services log [15.2]).
- **Data age:** for each input a run read, the run's start minus the input's time (`inputs` are `path@time` in `runs.jsonl`). Old data at decision time is a warning.
- Trading adds its own rules in the prediction-market domain's `trading-metrics.md` (order latency).

### Errors
<!-- k: id=metric-errors applies=[2.16],name:runs.jsonl*,[16.1],path:agents/**/logs,[15.1] sources=D-029,D-031,derived,D-056 status=proposed -->
- `error_rate` = runs with `status: error` divided by all runs. Cancelled runs (restarts) are not errors; they are counted as `restarts`.
- **Job failures:** `fail_count` and `last_result` of each job in [16.1] `scheduler-state.json`, and the lines in `logs/jobs/[job-id]/history.jsonl`, timeouts included.
- **Other signals:** broken required links in the links index [16.1], and `keys_refused` in [15.1].
- Trading adds its own rules in the prediction-market domain's `trading-metrics.md` (orders blocked by the risk check).

### Tests
<!-- k: id=metric-tests applies=[2.16],name:tests.config.json,name:tests.jsonl sources=D-025 status=proposed -->
- Counts of passing, failing and never-run tests from each `tests.config.json` (`last_result`), with recent history from `logs/tests.jsonl`.
- Not a performance number but a gate: going live needs every enabled test passing (`metric-promote-live`).

## Going live

### Test to live candidate
<!-- k: id=metric-promote-live applies=[2.16],[2.11.4],[11.1],name:tests.config.json sources=in-20260929-1455,D-025,derived,D-056 status=proposed -->
A test agent becomes a live candidate only when all of these hold; then the owner decides (how-to/promote-to-live.md):
- its error rate is below the limit, and no required link is broken;
- every enabled test passes, including the `before_promote` tests (D-025).
Its parent or an SI sub-agent proposes; only the owner approves (decided: vision.md `vis-principle-test-first`). Trading adds its own rules in the prediction-market domain's `trading-metrics.md` (champion, PnL, drawdown and calibration conditions, the starting capital).

## Open questions
<!-- k: id=metric-open applies=[2.16],[15.4] sources=in-20260929-1452,in-20260929-1455,derived,D-056 status=open -->
- How are shared sub-agent and worker costs split over the agents that read their outputs?

## Changelog
- v0.2 (2026-10-07): trading parts moved to the prediction-market domain's `trading-metrics.md` (D-056, D-058); this note keeps the general metrics: period and mode, cost, latency, errors, tests and the general conditions for going live.
- v0.1 (2026-09-30): created from file-tree.md v1.16, vision.md v0.19 and the owner inputs (D-033). Includes champion and challengers at the strategy level (D-032).
