# Agent OS: Agents index (v0.2)

The registry of agent names [2.18.1] (D-012): one row for every agent the tree names, including example names and names that were replaced, so that no name is ever used twice. It is written by hand from file-tree.md v1.16 for now; later `create-agent` [14.1] keeps it, and it may be generated from a JSON registry (open, [2.18]). Name format: see conventions.md. Column meanings: see data-schemas.md, `schema-index-tables`. Sub-agents are not in this list: see subagents.md.

## Agents
<!-- k: id=idx-agents applies=[2.18.1],[10],[19],[21],[23],[27.2] sources=D-012,D-022,D-032,in-20260929-1607,in-20260930-1453-2,derived,D-056 status=proposed -->
Nothing is built yet, so no agent is active or has a created date. `status` says what each name is today: `planned` (a level agent the tree defines), `example` (a name used only in examples), `replaced` (a name dropped before anything was built; kept here so it is never reused). `type` is the agent config's `agent.type`: `system`, `domain`, or a type the agent's domain defines (the prediction-market domain defines `strategy` and `variant`; D-022). `route` is the model it would get from [11.11] (see models.md). Funding is not kept here: the prediction-market domain lists its trading accounts, funded or not, in its own `index/accounts.md` [19.6.18.1].

| name | type | domain | parent | route | mode | status | created | path |
|---|---|---|---|---|---|---|---|---|
| `sys-system-agent` | system | system | - | open: [11.11] has no `system` type | - | planned | - | `agents/system/` [10] |
| `pm-domain-agent` | domain | prediction-markets | - | `opus-5.5` (type `domain`) | - | planned | - | `agents/trading/prediction-market/` [19] |
| `pm-strategy-1-agent.opus55-test` | strategy | prediction-markets | - | `opus-5.5` by its name; [11.11] has no `strategy` type, so it needs a named route | test | planned | - | `agents/trading/prediction-market/strategy-1-agent/` [21] |
| `pm-strategy-1.momentum-v1.opus55-test` | variant | prediction-markets | none (`agent.parent: null`) | `opus-5.5` (type `main`; its `main-run` job also names `opus-5.5`) | test | example | - | `agents/trading/prediction-market/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/` [23] |
| `pm-strategy-1.momentum-v2.opus55-test` | variant | prediction-markets | `pm-strategy-1.momentum-v1.opus55-test` (the research example `r-0001` in [50] led to it) | `opus-5.5` by its name | test | example | - | not in the tree; would sit next to [23] |
| `pm-strategy-1.momentum-v2.sonnet55-test` | variant | prediction-markets | not stated | `sonnet-5.5` by its name | test | example | - | not in the tree; only in the explorer's `subagents.link/` example (tools/enrich.py) |
| `pm-momentum-v1-agent-opus55-test` | variant | prediction-markets | - | - | test | replaced | - | old name of [23]; replaced by D-032 |
| `pm-strategy-1-agent` | strategy | prediction-markets | - | - | - | replaced | - | old proposed ID of [21] ([2.7], level agent IDs); D-032 added `.opus55-test` |

- **Where the names come from:** `sys-system-agent` and `pm-domain-agent` are the proposed level agent IDs in [2.7]. `pm-strategy-1-agent.opus55-test` and the variant format `[strategy-id].[own-name]-v[N].[platform-model]-[test|live]` are the owner's (D-032; format proposed; now in the domain's `trading-conventions.md` [19.6.7]).
- **Folder name vs ID (D-032):** level folders keep their structural names (`system/`, `prediction-market-agents/`, `strategy-1-agent/`); the ID lives in the agent's config and in this list. A variant's folder name is its ID.
- **Domain:** the key used in the agent config (`prediction-markets`); the folder is `prediction-market-agents/`, and the domain's own settings are in [19.2.4].
- **Not named yet:** the agents of every later domain. Each domain's IDs start with its domain code ([2.7]).
- **Open (D-032):** does `v[N]` belong to the variant or to the strategy? Should the strategy folder carry the `.[platform-model]-[test|live]` suffixes too?
- **Open:** the domain's `trading-conventions.md` [19.6.7] says a variant's strategy part must match its strategy agent's ID, but the variant starts with `pm-strategy-1` while the strategy agent's ID is `pm-strategy-1-agent.opus55-test`. Which string is the `[strategy-id]`?

## Changelog
- v0.2 (2026-10-07): trading parts moved to the prediction-market domain's `index/accounts.md` (the `funded` column); the `strategy` column dropped, `parent` stays; the copy-trading row and notes removed (D-056, D-058).
- v0.1 (2026-09-30): created from file-tree.md v1.16, vision.md v0.19, tools/tabs.py and the owner inputs (D-033).
