---
about: agent-os/agents/trading/prediction-market/data/markets-catalog/
node: n-19.5.2
basis: 2fe6b7e375c9
written: 2026-10-05T13:25:49Z
by: knowledge-base-agent
confirmed: 2026-10-07T18:57:42Z
---
# markets-catalog/

## Summary

The output folder of the domain's `markets-catalog` worker: `latest.json` plus dated history, the catalogue of markets the domain trades. It is domain data, so it lives in the domain's own `data/`; the strategy and its variants read it only through file links (`@domain`).

## Keep in mind

- When a strategy or variant needs the catalogue, link `latest.json` through its links file; never copy it or write here.
