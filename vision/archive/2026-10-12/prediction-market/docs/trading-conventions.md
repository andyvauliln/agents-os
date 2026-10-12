# Agent OS, prediction-market domain: Trading conventions (v0.1)

The trading layer of the system's conventions note: how strategy agents and their variants are named, what makes a new variant, the domain's `decision` scripts and where its shared ones sit, and the trading fields of an agent's config. Read it together with the system's `conventions.md`; a later trading domain copies it. Trading account ids (`acct-pm-test-1`, format open) are in trading-data-schemas.md and index/accounts.md [19.6.18.1]; who may approve an account is in trading-safety.md.

## Variant names
<!-- k: id=conv-variant-names applies=[23],[21],[2.18.1],[14.1] sources=D-032,in-20260930-1453-2,D-056 status=decided -->
General rule: see the system's `conventions.md` (Agent names).
- A trading variant's name always starts with its strategy, then its own name, then suffixes for its main platform/model and its mode (D-032).
- The strategy is readable from the name alone, and all variants of one strategy sort together.
- Example: `pm-strategy-1.momentum-v1.opus55-test` [23] is a variant of strategy 1 [21]. "momentum" is only a placeholder modification name.
- The mode suffix is part of the name because test and live agents are different agents (see the system's conventions.md, `conv-no-rename`).

### Variant name format
<!-- k: id=tr-conv-variant-name-format applies=[23],[14.1],[2.18.1] sources=D-032,D-056 status=proposed -->
General rule: see the system's `conventions.md` (Domain codes).
- `[strategy-id].[own-name]-v[N].[platform-model]-[test|live]`.
- Lowercase `a-z`, `0-9`, `-` and `.` only, at most 64 characters. Dots separate the strategy, the variant and the suffix parts.
- `[strategy-id]` is the strategy agent's ID without `-agent` and without its suffixes: strategy `pm-strategy-1-agent.opus55-test` gives `pm-strategy-1`. It must match the parent strategy.
- `[platform-model]` is a short code without dots, e.g. `opus55` (Opus 5.5), `composer25` (Composer 2.5). It must match the agent's route in [11.11]; `create-agent` [14.1] checks it.
- Example: `pm-strategy-1.momentum-v1.opus55-test`.

## Strategy agent IDs
<!-- k: id=conv-strategy-agent-ids applies=[21],[21.1.5],[2.18.1] sources=D-032,in-20260930-1453-2,D-056 status=decided -->
- A strategy agent's ID also carries the main platform/model it runs with and its mode (D-032). Example for [21]: `pm-strategy-1-agent.opus55-test`.
- Its variants' names start with its strategy part (`pm-strategy-1`), see `tr-conv-variant-name-format`.

### Strategy ID format and folder names
<!-- k: id=tr-conv-level-ids applies=[21],[23],[2.18.1] sources=D-012,D-032,D-056 status=proposed -->
General rule: see the system's `conventions.md` (Level agent IDs and folder names).
- Strategy agent ID format: `[domain]-[strategy]-agent.[platform-model]-[test|live]`.
- Strategy folders keep their structural names (`strategy-1-agent/`); the ID lives in the strategy's config and in the registry [2.18.1]. A trading variant's folder name is its ID.

## Variants and v[N]
<!-- k: id=tr-conv-clones applies=[23],[21],[21.1.1.1],[27.2],[27.4],[11.11] sources=D-012,D-032,D-056 status=proposed -->
General rule: see the system's `conventions.md` (Clones and versions).
- In this domain a new version of a trading agent is a new variant. A changed config, prompt or code makes a new variant and bumps `v[N]`. A different model changes the `[platform-model]` part.
- A trading agent's model is part of its name, so moving a variant to a new model means a new test variant, never an edit of the old one.
- A change to a job's logic (prompt, model, tools, inputs) in the workers file (e.g. [27.4]) makes a new variant.
- Variants are made by the strategy agent through its SI sub-agent [21.1.1.1] (D-032) or by the domain agent, always as test agents first.

## Decision scripts
<!-- k: id=tr-conv-script-kinds applies=[14.3],[33],[30],name:*.decision.*,[31] sources=D-007,in-20260929-1455,in-20260929-1545,D-056 status=decided -->
General rule: see the system's `conventions.md` (Script kinds and suffixes).
- The domain adds the script kind `decision` (buy, sell, risk checks): `[name].decision.[ext]`.
- Examples: `make-buy.decision.js` [33], `risk-check.decision.js` [14.3]; a worker of this domain: `get-polymarket-data.worker.py` [31].
- A link to a decision script keeps its kind: `risk-check.decision.link.js` [30.1] is still a decision script.

### The domain's shared decision scripts
<!-- k: id=tr-conv-shared-script-folders applies=[14.3],[19.3],[30.1] sources=D-007,D-056 status=proposed -->
General rule: see the system's `conventions.md` (Shared script folders).
- The domain's shared decision scripts sit in its `scripts/decisions/` [14.3] (moved from the system's `scripts/`, number kept): `*.decision.js|py` only, such as `risk-check.decision.js` and the buy and sell building blocks.
- A trading agent links the ones it needs, e.g. `risk-check.decision.link.js` [30.1] from `@domain/scripts/decisions/risk-check.decision.js`.

## Trading fields of an agent's config
<!-- k: id=tr-conv-agent-config-files applies=[27.2],[27.1],[19.2.4],[21.2] sources=D-006,D-014,D-029,D-031,in-20260930-0938,D-056 status=decided -->
General rule: see the system's `conventions.md` (Per-agent config files).
- A trading agent's `[name].config.json` [27.2] also holds its risk settings (`capital_and_risk`, which may only tighten the domain's caps) and its strategy parameters. Example name: `pm-strategy-1.momentum-v1.opus55-test.config.json`.
- The domain's own config is `prediction-market-agents.config.json` [19.2.4]: risk limits, trading accounts, venues, fees, market filters, default workers, the currency, the order stop switch and trade notifications (moved from [11.1], D-058). A trading agent reaches it through a file link `prediction-market-agents.config.link.json` [27.1].
- The strategy's files use its folder name today (`strategy-1-agent.workers.json`).
- Fields: trading-data-schemas.md.

## Open questions
<!-- k: id=tr-conv-open applies=[23],[21],[21.2.1],[21.2.3],[21.2],[2.18.1] sources=D-031,D-032,derived,D-056 status=open -->
- Does `v[N]` belong to the variant name or to the strategy (`strategy-1` to `strategy-1-v2`)? (D-032)
- Should the strategy folder carry the `.[platform-model]-[test|live]` suffixes too, or only its ID in config and the registry? Renaming the folder touches every [21.x] path. (D-032)
- A variant starts with `pm-strategy-1` while its strategy's ID is `pm-strategy-1-agent.opus55-test`. Is the prefix always the ID without `-agent` and its suffixes, as `tr-conv-variant-name-format` assumes?
- Do the strategy's own files take its ID (`pm-strategy-1-agent.opus55-test.workers.json`) or keep its folder name (`strategy-1-agent.workers.json` [21.2.1], [21.2.3])?
- The domain now has its own `[name].config.json` ([19.2.4], D-058). Does the strategy [21.2] get one too?

## Changelog
- v0.1 (2026-10-07): created from the trading parts of conventions.md v0.4 (D-056, D-058); the copy-trading code `ct` and its example left out (D-056).
