---
about: agent-os/agents/trading/prediction-market/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/docs/
node: n-46
basis: 26c3d2c962f3
written: 2026-10-07T19:03:05Z
by: knowledge-base-agent
---
# docs/

## Summary

The agent's own docs folder, a real folder like its configs, scripts, logs and data. Its own Markdown docs say what it is (`README.md`), its strategy in plain words, exactly what differs from its parent and what is being tested (`changes.md`), its notable decisions and the owner's comments and answers (`notes.md`). Like every level it also has a vision and a rebuild prompt, not written yet, following the outlines in the domain's `doc-outlines.md`. Read-only file links [46.1] bring in the rules and architecture notes for every agent (`safety.link.md`, `agent-architecture.link.md`) and for every trading agent (`trading-safety.link.md`, `trading-agent-architecture.link.md`). create-agent scaffolds it; the agent, its strategy's SI sub-agent and the domain agent keep it current. The formats are proposed; whether the agent may edit its own docs is open.

## Keep in mind

- When you need another shared doc, add it to your links file and let relink build the link; never copy the doc in.
- When you record what changed in this variant, use `changes.md` here; the cross-variant history belongs in the strategy's `data/`.
