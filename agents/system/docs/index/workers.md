# Agent OS: Workers index (v0.2)

Every job the tree and the File Tree page's examples name [2.18.2], from the four workers files: system [11.10], domain [19.2.1], strategy [21.2.1] and the example variant [27.4] (D-029). A "worker" here is any job: a plain script or an AI run (the agent itself, a sub-agent, a skill, a workflow or a command). It is written by hand for now; later it is built by scanning `agents/**/configs/*.workers.json` (real files only). Job fields and schedule strings: see data-schemas.md, `schema-workers-job-fields` and `schema-workers-schedule`. Agent IDs: see agents.md.

## Jobs
<!-- k: id=idx-workers applies=[2.18.2],[11.10],[19.2.1],[21.2.1],[27.4],[19.3.5],[19.5.3] sources=D-029,D-033,in-20260930-0938,derived,D-056 status=proposed -->
The rows are the Jobs examples of the File Tree page (tools/tabs.py `JOBS`), checked against each workers file's doc in the tree. `Runner` is where it runs, the platform, and for AI runs the model and effort (`route` = look it up in [11.11], see models.md). Paths in `Output` are relative to the owner agent's folder. `Read by` comes from the links files (see links.md). Every job is in `test` mode, logs each run to the owner agent's `logs/jobs/[id]/`, and keeps its runtime state in [16.1] `scheduler-state.json`.

| Owner agent (file) | Job id | On | Type | Runs | Schedule | Runner | Output | Read by |
|---|---|---|---|---|---|---|---|---|
| `sys-system-agent` ([11.10]) | `relink` | yes | script | `node scripts/system/relink.system.js --changed` ([14.1]) | `cron 0 4 * * *`, and on a change of `agents/**/configs/*.links.json` | local, none | not set; relink writes the links index [16.1] and logs to [15.1] | - |
| `sys-system-agent` ([11.10]) | `check-links` | yes | script | `node scripts/system/check-links.system.js` ([14.1]) | `cron 0 * * * *` (hourly) | local, none | not set; report only | - |
| `sys-system-agent` ([11.10]) | `news-digest` | yes | subagent | `news-digest` | `every 6h` | local, claude-code, `sonnet-5.5` low | `data/subagents/news-digest/latest.md` ([16.3]) | `pm-strategy-1.momentum-v1.opus55-test` |
| `sys-system-agent` ([11.10]) | `system-self-improvement` | yes | subagent | `sys-self-improvement-agent` ([10.1.1.1]) | `cron 0 3 * * *` | local, claude-code, `opus-5.5` high | not set; may write `research/**` ([10.9]) | - |
| `sys-system-agent` ([11.10]) | `knowledge-sync` | yes | subagent | `sys-knowledge-agent` ([10.1.1.2]) | `cron 30 2 * * *`, and on a change of `agents/**` or `agents/system/docs/inputs/**` | local, claude-code, `opus-5.5` medium | `docs/index/knowledge-map.json` ([2.18.8]), every `[name].index.md` ([51]) | - |
| `sys-system-agent` ([11.10]) | `scripts-review` | no | command | `/review-scripts` | `cron 0 9 * * 5` | cloud, codex, `route` | not set; report only | - |
| `pm-domain-agent` ([19.2.1]) | `domain-session` | yes | agent | the domain session ([19.1.5]) | `every 4h` | local, claude-code, `route` high | not set; may write `data/**`, `docs/**` | - |
| `pm-domain-agent` ([19.2.1]) | `markets-catalog` | yes | script | `python scripts/markets-catalog.worker.py` | `every 1h` | local, none | `data/markets-catalog/latest.json` ([19.5]) | `pm-strategy-1-agent.opus55-test`, `pm-strategy-1.momentum-v1.opus55-test` |
| `pm-domain-agent` ([19.2.1]) | `polymarket-prices` | yes | script | `python scripts/polymarket-prices.worker.py` ([19.3.5]) | `every 5m` | local, none | `data/polymarket-prices/latest.json` ([19.5.3]) | `pm-strategy-1.momentum-v1.opus55-test`; the domain session reads it in place |
| `pm-domain-agent` ([19.2.1]) | `domain-self-improvement` | yes | subagent | `pm-self-improvement-agent` ([19.1.1.2]) | `cron 0 2 * * *` | local, claude-code, `opus-5.5` high | not set | - |
| `pm-domain-agent` ([19.2.1]) | `election-night-check` | yes | skill | `polymarket-resolution-check` | `once 2026-11-03 20:00` (America/New_York) | local, claude-code, `sonnet-5.5` medium | not set; report to the owner | - |
| `pm-strategy-1-agent.opus55-test` ([21.2.1]) | `strategy-session` | yes | agent | the strategy session ([21.1.5]) | `cron 0 23 * * *` (daily) | local, claude-code, `route` high | not set | - |
| `pm-strategy-1-agent.opus55-test` ([21.2.1]) | `compare-variants` | yes | workflow | `compare-variants` | `after strategy-session` | local, claude-code, `sonnet-5.5` medium | `data/variant-report/latest.json` and `latest.md` ([21.5]) | - |
| `pm-strategy-1-agent.opus55-test` ([21.2.1]) | `strategy-self-improvement` | yes | subagent | `pm-strategy-1-self-improvement-agent` ([21.1.1.1]) | `cron 30 3 * * *` | local, claude-code, `opus-5.5` xhigh | not set; new test variants via `create-agent` [14.1], research in [21.13] | - |
| `pm-strategy-1.momentum-v1.opus55-test` ([27.4]) | `main-run` | yes | agent | the agent's own session ([24.5]) | `every 15m`, and restart on a change of `data/polymarket-prices.link.json` | local, claude-code, `opus-5.5` high; keys `POLYMARKET_ACCT1_*` | not set; may write `data/**` | - |
| `pm-strategy-1.momentum-v1.opus55-test` ([27.4]) | `get-polymarket-data` | yes | script | `python scripts/get-polymarket-data.worker.py` ([31]) | `every 15m` | local, none | `data/get-polymarket-data/latest.json` ([35.2]) | - |
| `pm-strategy-1.momentum-v1.opus55-test` ([27.4]) | `clean-data` | yes | script | `node scripts/clean-data.system.js` ([32]) | `after get-polymarket-data` | local, none | not set | - |
| `pm-strategy-1.momentum-v1.opus55-test` ([27.4]) | `close-before-resolution` | yes | command | `/close-before-resolution` | `once 2026-10-31 18:00` (UTC) | local, claude-code, `route` | not set; report to the owner | - |

- **Named in the tree, no job yet:** [11.10] also lists tests and index rebuilds among the system's jobs; neither has a job id. Tests with `schedule: on_change` or `interval:[x]` are started by the scheduler ([14.1]).
- **Retired:** `docs-refresh` (system) was replaced by `knowledge-sync` (D-033).
- **Scripts in the domain:** `markets-catalog.worker.py` is [19.3.3] and `polymarket-prices.worker.py` is [19.3.5]. The price collector was the system's shared-worker example in [14.2] until it moved to the domain (D-058).
- **File `agent` field:** the files are named after the folder (`system`, `prediction-market-agents`, `strategy-1-agent`, the variant's name), so the `agent` field of the level files is not the level agent's ID in agents.md. Open, tied to the D-032 question about strategy folder names.

## Changelog
- v0.2 (2026-10-07): the `polymarket-prices` job moved to `pm-domain-agent` with its new paths ([19.3.5], [19.5.3]); the copy-trading note removed (D-056, D-058).
- v0.1 (2026-09-30): created from file-tree.md v1.16, vision.md v0.19, tools/tabs.py and the owner inputs (D-033).
