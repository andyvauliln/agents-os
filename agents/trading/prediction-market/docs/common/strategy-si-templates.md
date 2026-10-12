# Agent OS, prediction-market domain: Strategy SI templates (v0.1)

The trading layer of the system's `common/self-improvement-templates.md`: the trading words of the base template, the domain template [19.1.1.2] in trading terms, and the strategy template [21.1.1.1] with the variant loop the owner asked for in D-032. Promotion and comparison rules are in `trading-metrics.md` [19.6.11]. Read it together with `common/self-improvement-templates.md`; a later trading domain copies it.

## Base template for the trading levels
<!-- k: id=tr-common-si-base-template applies=[19.6.16.3],name:*self-improvement-agent.md,[19.1.12],[21.1.12] sources=D-018,D-024,D-025,D-029,D-056 status=proposed -->
General rule: see `common/self-improvement-templates.md` (Base template).

The SI sub-agents of this domain and of its strategies start from the base template, with these trading lines in place of the general ones:
- `description`: "...; proposes or creates new test variants; adds tests."
- Goal: "fast, cheap, efficient, simple, understandable, profitable."
- Step 4: "If a change is worth trying, make it a new TEST variant with create-agent, add tests for what changed, and link the variant in the item's `related`."
- Never: "touch live agents, raise risk caps, read .secrets/live/, or delete another agent's files."

## Domain level
<!-- k: id=tr-common-si-domain applies=[19.6.16.3],[19.1.1.2],[19.13],[19.1.12],[19.2.1] sources=D-018,D-022,D-024,D-056 status=proposed -->
- **Owns:** the domain's set of strategies.
- **Reads:** every strategy and its variants through the domain's `subagents.link/` folders ([19.4.1], [19.5.1], [19.6.1]), domain-wide data, owner comments.
- **Writes:** comparisons of strategies and variants across the domain, proposals for new strategies or variants, domain-wide issues; research in [19.13].
- **Memory:** [19.1.12] `pm-self-improvement-agent/MEMORY.md`. **Job:** a nightly `subagent` job in [19.2.1].

## Strategy level
<!-- k: id=common-si-strategy applies=[19.6.16.3],[21.1.1.1],[21],[21.13],[21.5],[21.1.12],[21.2.1] sources=D-018,D-022,D-025,D-032,D-056 status=proposed -->
- **Owns:** one strategy and all its variants [23].
- **Reads:** its variants' logs, data, docs and tests through the strategy's `subagents.link/` folders ([21.4.1], [21.5.1], [21.6.1], [21.12.3]); past research in [21.13] and in the variants' `research/`; news; owner comments.
- **Writes:** new test variants (via create-agent), research in [21.13], tests in [21.12] and, when it creates a variant, that variant's first `tests/` (through create-agent; the child links stay read-only), the cross-variant history `changes.md` in [21.5].
- **Memory:** [21.1.12] `pm-strategy-1-self-improvement-agent/MEMORY.md`. **Job:** the strategy's nightly SI `subagent` job in [21.2.1].

### The variant loop
<!-- k: id=common-si-variant-loop applies=[19.6.16.3],[21],[21.1.1.1],[23] sources=D-032,in-20260930-1453-2,D-056 status=decided -->
The strategy agent improves itself through its SI sub-agent (D-032): it creates modifications of itself as new test variants, tests how they work, analyses them against each other, and when a modification wins, updates itself. Every variant's name starts with the strategy's ID, e.g. `pm-strategy-1.momentum-v1.opus55-test` under `pm-strategy-1-agent.opus55-test`.

### Loop steps
<!-- k: id=common-si-loop-steps applies=[19.6.16.3],[21],[21.1.1.1],[23],[21.6],[21.2],[21.1.5],[21.5],[21.13],[46.2],[19.6.11] sources=D-025,D-032,D-056 status=proposed -->
1. **Propose a modification.** From logs, data, research, news or an owner comment; open a research item in [21.13] with the question and the method.
2. **Create the variant.** Run create-agent with the changed config, prompt, code or model: a new test variant under the strategy, named `[strategy-id].[own-name]-v[N].[platform-model]-test`, with `parent` set and its `docs/changes.md` saying exactly what differs (how-to/create-strategy-or-variant.md).
3. **Test.** Add or update tests for what changed; the variant runs in test mode on its schedule for the test period.
4. **Compare.** Against its parent and the other variants, on the same period and capital, with the metrics in `trading-metrics.md` [19.6.11]; write the result into the research item and the cross-variant history [21.5].
5. **Fold back or retire.** If it wins, update the strategy itself: its definition in `docs/` [21.6], its config in [21.2] and its prompt [21.1.5], and record the change. If it loses, stop it and record why (how-to/stop-trading-agent.md). Going live is a separate owner decision (how-to/go-live-with-money.md).
6. **Close the item** with `results_summary`, `decisions` and `related` (variants, changes, tests), and save a pointer in memory.

## Open questions
<!-- k: id=common-si-open applies=[19.6.16.3],[21.1.1.1],[23],[27.3],[21] sources=derived,D-056 status=open -->
- May an SI sub-agent retire variants, or only create them ([21.1.1.1])?
- What may SI change without owner approval, and which metrics decide success (PnL, win rate, drawdown, calibration)?
- Does `v[N]` belong to the variant or to the strategy (`strategy-1` to `strategy-1-v2`) ([23])?
- Is a link change a new variant, or may small additions happen in place ([27.3])?
- Where does the strategy definition live: a skill in [21.1.2] or `docs/` [21.6] (proposed)?

## Changelog
- v0.1 (2026-10-07): created from the trading parts of the system's `common/self-improvement-templates.md` v0.1 (D-056, D-058): `common-si-strategy`, `common-si-variant-loop`, `common-si-loop-steps` and `common-si-open` moved here; trading lines of the base and domain templates as `tr-` sections.
