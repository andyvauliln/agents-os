---
about: agent-os/agents/trading/prediction-market/strategy-1-agent/docs/rebuild-prompt.md
node: n-21.6.4
basis: 3baaf921295d
written: 2026-10-07T19:03:05Z
by: knowledge-base-agent
---
# rebuild-prompt.md

## Summary

The strategy's own rebuild prompt: the instructions an AI follows to rebuild the strategy's folder exactly, assuming the system and its domain exist. It names what it takes from them, gives its own settings, prompt, helpers, data and docs with exact names, lists its trading agents' prompts in build order, and ends with checks, including that nothing trades live without the owner's approval. It is written last, with the rebuild prompt skill and the domain's `doc-outlines.md`; nothing is written yet.

## Keep in mind

- When you change the strategy's design, update this prompt after its vision and README, then check the domain's rebuild prompt.
