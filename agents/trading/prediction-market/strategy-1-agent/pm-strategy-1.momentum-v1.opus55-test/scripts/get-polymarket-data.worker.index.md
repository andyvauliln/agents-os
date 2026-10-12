---
about: agent-os/agents/trading/prediction-market/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/scripts/get-polymarket-data.worker.py
node: n-31
basis: 4a7faccdc665
written: 2026-10-07T19:03:05Z
by: knowledge-base-agent
confirmed: 2026-10-07T19:07:29Z
---
# get-polymarket-data.worker.py

## Summary

The agent's own worker: a Python script that fetches Polymarket market details for this agent's markets. It runs as a job in the jobs file [27.4] and writes dated files plus a stable `latest.json` (`id`, `question`, `price_yes`, `volume_usd`) to `data/get-polymarket-data/` [35.2], logging to `logs/` [34]. Keys reach it only through `load-secret`. When a second agent of the domain needs it, it moves to the domain's shared `scripts/` (proposed; whether automatically is open).

## Keep in mind

- When you need a key here, declare its name in `secret_keys` and read it from the environment `load-secret` sets; never put a key in the code.
- When you write output, write the dated file first, then replace `latest.json` in one step (temp file, then rename), so readers never see half a file.
- When you find a second agent of this domain needs this data, move the worker to the domain's shared `scripts/` and link it; never copy it.
