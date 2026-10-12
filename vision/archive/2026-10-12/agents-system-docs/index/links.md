# Agent OS: Links index (v0.3)

Every file link [2.18.7] listed in the four example links files: system [11.13], domain [19.2.3], strategy [21.2.3] and the example variant [27.3] (D-031). It is written by hand for now; later it is a view of the links index [16.1] `links.index.json`, which `relink` [14.1] writes. Child links (`subagents.link/`, D-030) are built from the folder tree and are never listed. File format and the `from` short forms: see data-schemas.md, `schema-links-file` and `schema-links-from`. Agent IDs: see agents.md.

## Links
<!-- k: id=idx-links applies=[2.18.7],[11.13],[19.2.3],[21.2.3],[27.3],[16.1] sources=D-020,D-031,in-20260930-1153,derived,D-056 status=proposed -->
The rows are the Links examples of the File Tree page (tools/tabs.py `LINKS`), checked against each links file's doc in the tree. `To` is where the link appears, relative to the agent's own folder. Every entry is `enabled`. `Node` is the link's number in the tree, when it has one.

| Agent (file) | To | From | Why | Required | Added by | Node |
|---|---|---|---|---|---|---|
| `sys-system-agent` ([11.13]) | `tests/agents/run-tests.system.link.js` | `@system/scripts/system/run-tests.system.js` | run the agent tests next to their config | yes | create-agent | [10.8.1.3] |
| `sys-system-agent` ([11.13]) | `tests/scripts/run-tests.system.link.js` | `@system/scripts/system/run-tests.system.js` | run the script tests next to their config | yes | create-agent | [10.8.2.3] |
| `pm-domain-agent` ([19.2.3]) | `docs/safety.link.md` | `@system/docs/safety.md` | hard limits every domain follows | yes | create-agent | - |
| `pm-domain-agent` ([19.2.3]) | `tests/agents/run-tests.system.link.js` | `@system/scripts/system/run-tests.system.js` | run the agent tests next to their config | yes | create-agent | [19.12.1.3] |
| `pm-domain-agent` ([19.2.3]) | `tests/scripts/run-tests.system.link.js` | `@system/scripts/system/run-tests.system.js` | run the script tests next to their config | yes | create-agent | [19.12.2.3] |
| `pm-domain-agent` ([19.2.3]) | `scripts/relink.system.link.js` | `@system/scripts/system/relink.system.js` | rerun after editing this file | yes | create-agent | [19.3.2] |
| `pm-strategy-1-agent.opus55-test` ([21.2.3]) | `data/markets-catalog.link.json` | `@domain/data/markets-catalog/latest.json` | compare variants market by market | yes | create-agent | - |
| `pm-strategy-1-agent.opus55-test` ([21.2.3]) | `docs/trading-metrics.link.md` | `@domain/docs/trading-metrics.md` | how variants are compared and promoted | yes | create-agent | - |
| `pm-strategy-1-agent.opus55-test` ([21.2.3]) | `tests/agents/run-tests.system.link.js` | `@system/scripts/system/run-tests.system.js` | run the agent tests next to their config | yes | create-agent | [21.12.1.3] |
| `pm-strategy-1-agent.opus55-test` ([21.2.3]) | `tests/scripts/run-tests.system.link.js` | `@system/scripts/system/run-tests.system.js` | run the script tests next to their config | yes | create-agent | [21.12.2.3] |
| `pm-strategy-1-agent.opus55-test` ([21.2.3]) | `scripts/relink.system.link.js` | `@system/scripts/system/relink.system.js` | rerun after editing this file | yes | create-agent | [21.3.2] |
| `pm-strategy-1.momentum-v1.opus55-test` ([27.3]) | `configs/system.config.link.json` | `@system/configs/system.config.json` | global modes, triggers | yes | create-agent | [27.1] |
| `pm-strategy-1.momentum-v1.opus55-test` ([27.3]) | `configs/prediction-market-agents.config.link.json` | `@domain/configs/prediction-market-agents.config.json` | the domain's risk limits, trading accounts and order stop switch | yes | create-agent | [27.1] |
| `pm-strategy-1.momentum-v1.opus55-test` ([27.3]) | `configs/models.config.link.json` | `@system/configs/models.config.json` | its model route | yes | create-agent | [27.1] |
| `pm-strategy-1.momentum-v1.opus55-test` ([27.3]) | `data/polymarket-prices.link.json` | `@domain/data/polymarket-prices/latest.json` | price input for make-buy | yes | create-agent | [35.1] |
| `pm-strategy-1.momentum-v1.opus55-test` ([27.3]) | `data/news-digest.link.md` | `@system/data/subagents/news-digest/latest.md` | news context for the main run | no | create-agent | [35.1] |
| `pm-strategy-1.momentum-v1.opus55-test` ([27.3]) | `data/markets-catalog.link.json` | `@domain/data/markets-catalog/latest.json` | which markets it may trade | yes | create-agent | [35.1] |
| `pm-strategy-1.momentum-v1.opus55-test` ([27.3]) | `scripts/risk-check.decision.link.js` | `@domain/scripts/decisions/risk-check.decision.js` | shared risk gate | yes | create-agent | [30.1] |
| `pm-strategy-1.momentum-v1.opus55-test` ([27.3]) | `scripts/run-tests.system.link.js` | `@system/scripts/system/run-tests.system.js` | run both kinds of tests | yes | create-agent | [30.2] |
| `pm-strategy-1.momentum-v1.opus55-test` ([27.3]) | `tests/agents/run-tests.system.link.js` | `@system/scripts/system/run-tests.system.js` | run the agent tests next to their config | yes | create-agent | [49.1.3] |
| `pm-strategy-1.momentum-v1.opus55-test` ([27.3]) | `tests/scripts/run-tests.system.link.js` | `@system/scripts/system/run-tests.system.js` | run the script tests next to their config | yes | create-agent | [49.2.3] |
| `pm-strategy-1.momentum-v1.opus55-test` ([27.3]) | `scripts/relink.system.link.js` | `@system/scripts/system/relink.system.js` | rerun after editing this file | yes | create-agent | [30.3] |
| `pm-strategy-1.momentum-v1.opus55-test` ([27.3]) | `logs/polymarket-prices.worker.link.log` | `@domain/logs/jobs/polymarket-prices/latest.log` | see when prices are stale | no | create-agent | [34.1] |
| `pm-strategy-1.momentum-v1.opus55-test` ([27.3]) | `docs/safety.link.md` | `@system/docs/safety.md` | rules it may never break | yes | create-agent | [46.1] |
| `pm-strategy-1.momentum-v1.opus55-test` ([27.3]) | `docs/agent-architecture.link.md` | `@system/docs/common/agent-architecture.md` | how agents work inside | yes | create-agent | [46.1] |
| `pm-strategy-1.momentum-v1.opus55-test` ([27.3]) | `docs/trading-safety.link.md` | `@domain/docs/trading-safety.md` | money rules it may never break | yes | create-agent | [46.1] |
| `pm-strategy-1.momentum-v1.opus55-test` ([27.3]) | `docs/trading-agent-architecture.link.md` | `@domain/docs/common/trading-agent-architecture.md` | how a trading agent works inside | yes | create-agent | [46.1] |

- **Most read files:** `markets-catalog/latest.json` (strategy and variant), `safety.md` (domain and variant), `run-tests.system.js` (two links at every level, three in the variant), `relink.system.js` (one link at every level below the system, which runs [14.1] directly).
- **Moved to the domain (D-058):** the Polymarket price collector with its logs and data, the risk check, the domain config and the comparison rules now sit in the prediction-market domain, so the variant and the strategy link them with `@domain`, and the domain session reads its own `data/polymarket-prices/` in place.
- **Open:** `@[name]` can name a domain by its folder (e.g. `@prediction-market-agents/…`), not by an agent ID; whether a level ID such as `pm-domain-agent` also works as `@[name]` is open (data-schemas.md, `schema-links-from`).

## Changelog
- v0.3 (2026-10-07): trading parts moved to the prediction-market domain: prices, price logs, the risk check and the comparison rules come from `@domain`; new rows for the domain config and the `trading-` docs; the domain's own price link removed; the `top-traders` and `whale-signals` rows removed with the copy-trading domain (27 links) (D-056, D-058).
- v0.2 (2026-09-30): the test runner links of the system, domain and strategy test folders are now in their links files (28 links).
- v0.1 (2026-09-30): created from file-tree.md v1.16, vision.md v0.19, tools/tabs.py and the owner inputs (D-033).
