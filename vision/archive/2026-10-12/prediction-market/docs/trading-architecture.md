# Agent OS, prediction-market domain: Trading architecture (v0.1)

The trading layer of the system's architecture: this domain's folder, its strategy and trading-agent levels, strategy agents and their variants with the strategy loop, the trading items of the owner's first agent-folder list, the domain's config and dashboard, and how the domain's levels run. Read it together with the system's `architecture.md`; a later trading domain copies it. Numbers [n] are the objects in file-tree.md.

## The domain's folder
<!-- k: id=tr-arch-domains applies=[19],[21],[23] sources=D-013,D-015,in-20260929-1616,D-056 status=decided -->
General rule: see the system's `architecture.md` (Domains under agents/).
- This domain's folder [19] is its domain agent's folder. Its strategies are sub-folders of it, and each strategy's variants are sub-folders of the strategy.
- A later trading domain copies this shape from this domain when needed (D-056).

## Agent levels
<!-- k: id=tr-arch-levels applies=[19],[21],[23] sources=D-018,D-022,D-026,D-030,in-20260929-1703,D-056 status=decided -->
Below its domain agent, this domain defines two levels, both with the standard folder (D-022). The domain agent [19.1.5] finds, creates and updates strategies and keeps the domain making money; its children are the strategies.

| Level | Folder | Prompt | Responsible for | Children |
|---|---|---|---|---|
| Strategy | e.g. `strategy-1-agent/` [21] | [21.1.5] strategy manager | one concrete strategy: its definition, its variants and its self-improvement loop | trading variants |
| Trading variant | e.g. [23] | [24.5] trading agent | trading: one platform/model, one mode, one run at a time | none |

- Strategy agents have IDs in config and the index (e.g. `pm-strategy-1-agent.opus55-test`) while their folders keep structural names (D-032). Format: `trading-conventions.md` `conv-strategy-agent-ids`.
- The system reaches a trading variant in three steps, one `subagents.link/` at a time: domain, strategy, variant.

### Strategy agents and variants
<!-- k: id=arch-strategy-variants applies=[21],[23],[21.1.1.1],[21.5],[21.13] sources=D-022,D-032,in-20260930-1453-2,D-056 status=decided -->
- A strategy agent [21] holds one strategy: its definition (in `docs/` [21.6], proposed), its own config and prompt, and all its variants as sub-folders.
- A variant (modification) [23] is the strategy with one set of changes, on one platform/model, in one mode. Its name starts with the strategy's ID, so all variants of one strategy sort together (D-032; format: `trading-conventions.md` `conv-variant-names`).
- **The strategy loop (D-032):** the strategy agent, through its SI sub-agent [21.1.1.1], creates modifications of itself as new test variants, runs them, analyses them against each other (cross-variant history in [21.5], research in [21.13]), and folds a winning change back into the strategy's definition, config and prompt. Whether the SI sub-agent may retire losing variants itself is open (`trading-roadmap.md` `road-q-si-retire`).
- Loop steps: `common/strategy-si-templates.md` `common-si-variant-loop`; the flow: `trading-flows.md` `flow-si-strategy-loop`; how variants are compared: `trading-metrics.md` `metric-champion`.

## The owner's first agent-folder list: trading items
<!-- k: id=tr-arch-owner-list applies=[23],[19.2.4],[19.6.18.1],[21.1.1.1] sources=in-20260929-1452,derived,D-056 status=proposed -->
The trading items of the owner's first list (the vision notes `tr-vis-block-agent-folder` in `trading-vision-notes.md`; the rest of the list: the system's `architecture.md`): self-improvement strategy → the strategy's SI sub-agent [21.1.1.1]; trading accounts → the domain config [19.2.4] `accounts`, listed in `index/accounts.md`. No home yet: the current portfolio and analytics.

## The domain's config
<!-- k: id=tr-arch-configs applies=[19.2.4] sources=D-006,D-011,D-014,D-029,D-031,in-20260929-1537,D-056 status=decided -->
- `prediction-market-agents.config.json` [19.2.4] is the domain's own config. It holds what the system config held for trading: risk limits, trading accounts, venues, fees, market filters, default workers, the currency, the order stop switch and trade notifications (proposed default, D-058).
- A trading agent reads it through a file link, as it reads the system's shared configs. How the risk and account rules merge: `trading-safety.md`.

## The domain's dashboard
<!-- k: id=tr-arch-apps-ui applies=[45] sources=in-20260929-1455,in-20260929-1545,D-056 status=decided -->
- `apps/trading-ui/` [45] is this domain's dashboard. It stays in `apps/` where the owner put it (proposed default, D-058). It is empty for now; it may never be needed if the project IDE does the job (owner, 2026-10-06).
- The plan: a Next.js API and UI for monitoring and analysing every agent and the system, and for the owner's actions (the system's vision notes `vis-ui`). It reaches every level's files from the system down through `subagents.link/`. Whether it reads the files directly or through an API layer is open (`trading-roadmap.md` `road-q-ui-access`).

## How the domain's levels run
<!-- k: id=tr-arch-runs-per-level applies=[21],[23] sources=D-021,D-029,D-030,D-056 status=proposed -->
- Each strategy session runs at its strategy folder, and each trading variant in its own folder, started by `run-agent` [14.1].
- Example jobs: the strategy session daily, a variant's main run every 15m.

## Changelog
- v0.1 (2026-10-07): created from the trading parts of the system's `architecture.md` v0.1 (D-056, D-058); `arch-strategy-variants` moved here whole.
