---
about: agent-os/agents/trading/prediction-market/docs/trading-conventions.md
node: n-19.6.7
basis: 24a5bc45c73b
written: 2026-10-07T18:56:50Z
by: knowledge-base-agent
---
# trading-conventions.md

## Summary

The trading layer of the system's `conventions.md`: how strategy agents and variants are named (a variant starts with its strategy, as in `pm-strategy-1.momentum-v1.opus55-test`), what makes a new variant and bumps `v[N]`, the `decision` script kind this domain adds and its shared decision scripts in `scripts/decisions/`, and the trading fields of an agent's config. The exact formats are proposed, and several naming questions are still open.

## Keep in mind

- When you name a variant, start with its strategy's ID and end with its platform/model and mode; never rename or reuse a name.
- When you change a config, prompt, code or model, make a new variant with a new `v[N]` or model part, never an edit of the old one.
