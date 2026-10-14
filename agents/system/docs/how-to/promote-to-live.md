# Agent OS: Promote to live (v0.2)

How a test agent goes live. Only the owner approves it, in the UI (vision §12). Live is a later phase: live keys come later (D-027). The safety rules are in safety.md; the test criteria are in metrics.md [2.16]. A domain may add its own steps: for example, the prediction-market domain's `how-to/go-live-with-money.md` adds a funded account, risk caps and its promotion thresholds.

## Steps
<!-- k: id=howto-promote-to-live-steps applies=[2.11.4],[2.16],[11.1],[47.2.1],[47.3],[49.1.1],[49.2.1],[27.2],[27.4],[2.18.1],[15.2] sources=D-012,D-023,D-025,D-027,D-029,in-20260929-1455,D-056 status=proposed -->
1. **Check the criteria:** every enabled test passing, including the `before_promote` ones: `node scripts/run-tests.system.link.js --schedule before_promote` (D-025), plus any criteria the agent's domain sets (metrics.md [2.16]).
2. **Propose it.** The agent's parent or an SI sub-agent proposes the promotion; the owner gets a `promotion_proposed` notification ([11.1] `notifications`).
3. **Owner approval in the UI.** Nothing else can approve going live.
4. **Live keys.** If the agent needs keys, the owner puts their live values in [47.2.1] `.secrets/live/.env` with the same key names as in test (see add-account-or-secret.md).
5. **Create the live agent.** Names never change, so going live creates a new agent with the same name ending in `-live` and `parent` set to the test agent (see create-agent.md). The test agent keeps running or is retired.
6. **Switch its mode.** The live agent's config (like [27.2]) says `mode: live`, the agent is added to [11.1] `modes.live_allowlist`, and its jobs get `mode: live` in its workers file (like [27.4]). Live jobs run `local` only; cloud, desktop and GitHub jobs are always test.
7. **Monitor.** Live actions are logged in [15.2] `logs/services/[service]/`; the UI shows the agent. The general stop switch in [11.1] `modes` stops every outside action at once.
8. **Update the registry** [2.18.1]: a row for the live agent and the test agent's new status.

## Checks
<!-- k: id=howto-promote-to-live-checks applies=[2.11.4],[11.1],[47.2.1],[2.18.1],[27.2] sources=D-012,D-023,D-027,D-056 status=proposed -->
- The live agent has its own new name ending in `-live` and its `parent` is the test agent; the test agent is unchanged.
- The agent is in `live_allowlist`.
- `load-secret` hands live keys (`AGENT_OS_ENV=live`) only to this agent's approved runs and refuses every other agent.
- No live value appears in any config, doc, log, prompt or link, and every level's `settings.json` still denies `.secrets/live/**`.
- The stop switch is off.

## Changelog
- v0.2 (2026-10-07): trading parts moved to the prediction-market domain's `how-to/go-live-with-money.md`; `TRADING_OS_ENV` is now `AGENT_OS_ENV` (D-056, D-058).
- v0.1 (2026-09-30): created from file-tree.md v1.15, vision.md v0.19 and the owner inputs (D-033).
