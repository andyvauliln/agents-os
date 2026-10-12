---
about: agent-os/agents/trading/prediction-market/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/
node: n-23
basis: ac62fd3659de
written: 2026-10-07T19:03:05Z
by: knowledge-base-agent
confirmed: 2026-10-09T09:57:03Z
---
# pm-strategy-1.momentum-v1.opus55-test/

## Summary

The example trading agent: one variant of strategy 1, on Opus 5.5 through Claude Code in test mode, deciding one run at a time. Its name, `pm-strategy-1.momentum-v1.opus55-test`, is its permanent ID: strategy, own name and version, model, mode (proposed). It has the standard folder, without `subagents.link/`: a variant has no children.

Its main run starts every 15 minutes through `start.sh`. Each run works here with its own `.claude/` and links (proposed): it reads what is new, decides, trades only through its decision script, logs the run and leaves a note for the next. Next to the system's config and notes it links its domain's config, risk check, prices and trading notes.

The strategy's SI sub-agent prepares variants like this, starts each once the owner approves its report, compares them and folds a winner back. Going live makes a new `-live` agent, with the owner's approval. Open: whose `v[N]` it is, and whether the SI sub-agent may retire variants itself.

- `.claude/` [24]: prompt, settings, sub-agents
- `configs/` [27], `scripts/` [30]: settings, links and code
- `logs/` [34], `data/` [35]: what it writes and reads
- `docs/` [46], `tests/` [49], `research/` [50]
- `init.sh` [40], `start.sh` [41]: setup and one run

## Keep in mind

- When you change its config, prompt, code or model, create a new test variant with a new name; never edit a running agent in place.
- When you want it live, create a new `-live` agent after the owner approves; never rename this one.
- When you trade, use only the decision scripts, which read the mode and the risk limits.
