# Agent OS, prediction-market domain: Create a strategy or a variant (v0.1)

The trading layer of the system's `how-to/create-agent.md`: the extra steps for a strategy agent (like [21]) or a trading variant (like [23]). The most common case is a new variant of a strategy, and that is usually made by the strategy's self-improvement (SI) sub-agent (D-032). Naming rules: `trading-conventions.md`. Read it together with `how-to/create-agent.md`; a later trading domain copies it.

## Steps
<!-- k: id=tr-howto-create-agent-steps applies=[19.6.17.1],[14.1],[21],[23],[21.1.1.1],[27.2],[19.2.4],[46.5],[19.6.18.1],[21.13],[21.5] sources=D-012,D-022,D-024,D-025,D-029,D-030,D-031,D-032,in-20260929-1455,in-20260930-1453-2,D-056 status=proposed -->
General rule: see `how-to/create-agent.md` (Steps). Each item below adds to the general step with the same number.

- **Step 1, the input.** For a new variant of a strategy, the usual creator is that strategy's SI sub-agent, e.g. `pm-strategy-1-self-improvement-agent` [21.1.1.1], working for the strategy agent [21] (D-032).
- **Step 2, the level and the parent.** A strategy goes under its domain, like [21] under [19]. A variant goes under its strategy, like [23] under [21].
- **Step 3, the name.** A variant name always starts with its strategy's ID: `[strategy-id].[own-name]-v[N].[platform-model]-[test|live]`, e.g. `pm-strategy-1.momentum-v2.opus55-test` (owner rule; exact format proposed; D-032). A strategy agent's ID carries its main model and its mode, e.g. `pm-strategy-1-agent.opus55-test`, while its folder keeps the name `strategy-1-agent/`.
- **Step 5, its own config** (like [27.2]) also holds `agent.strategy`, `capital_and_risk` (only tighter than the domain config's `risk` [19.2.4]) and the `strategy` parameters. A variant sets `parent` to the agent it was cloned from.
- **Step 8, its docs** also include `strategy.md` (like [46.5]).
- **Step 9, its route:** the platform and model in the name must match the route.
- **Step 12, the registry:** a new agent is not funded. Funding is kept per trading account, in the domain's `index/accounts.md` [19.6.18.1], not in the registry.
- **Step 14, for a variant made by the SI loop:** open a research item in the strategy's `research/` [21.13] (see record-research.md), list the new variant in its `related.variants`, and add the variant to the cross-variant history in the strategy's `data/` [21.5]. After the test period the strategy compares it with the other variants and folds the change back or retires it (see `common/strategy-si-templates.md`).

## Checks
<!-- k: id=tr-howto-create-agent-checks applies=[19.6.17.1],[2.18.1],[11.11],[21.2.2.1],[21.3.1.1],[21.4.1.1],[21.5.1.1],[21.6.1.1],[21.12.3.1],[21.13.3.1] sources=D-012,D-025,D-029,D-030,D-031,D-032,D-056 status=proposed -->
- A variant's name starts with its parent strategy's ID, and its `[platform-model]` part matches its route in [11.11].
- A variant has an entry in each of its strategy's `subagents.link/` folders: [21.2.2.1], [21.3.1.1], [21.4.1.1], [21.5.1.1], [21.6.1.1], [21.12.3.1], [21.13.3.1].
- For a variant: the research item and the strategy's cross-variant history name it.

## Changelog
- v0.1 (2026-10-07): created from the trading parts of the system's `how-to/create-agent.md` v0.1 (D-056, D-058).
