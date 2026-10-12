# Agent OS, prediction-market domain: Stop a trading agent (v0.1)

The trading layer of the system's `how-to/stop-or-delete-agent.md`: what stopping a trading agent adds, which is closing its positions and unfunding its account, and how a variant retired by the strategy loop is recorded. Read it together with `how-to/stop-or-delete-agent.md`; a later trading domain copies it.

## Steps
<!-- k: id=tr-howto-stop-or-delete-agent-steps applies=[19.6.17.4],[19.2.4],[19.6.18.1],[21.13],[21.5],[21.1.1.1] sources=D-012,D-029,D-030,D-031,in-20260929-1455,D-056 status=proposed -->
General rule: see `how-to/stop-or-delete-agent.md` (Steps). Each item below adds to the general steps.

- **Close positions (live only),** at the general step 2. Close or flatten open positions, and the owner sets its account in the domain config [19.2.4] `accounts` back to unfunded.
- **For a variant retired by the SI loop,** record why in the strategy's research item [21.13] and its cross-variant history [21.5]. Whether the SI sub-agent may retire variants on its own is still open ([21.1.1.1]).

## Checks
<!-- k: id=tr-howto-stop-or-delete-agent-checks applies=[19.6.17.4],[19.2.4] sources=D-012,D-030,D-031,D-056 status=proposed -->
- A live trading agent has no open positions.

## Changelog
- v0.1 (2026-10-07): created from the trading parts of the system's `how-to/stop-or-delete-agent.md` v0.1 (D-056, D-058).
