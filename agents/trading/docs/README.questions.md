# Questions: README.md

## Open questions for the owner

- **Which shared trading parts move up into `agents/trading/` once there are two trading domains?** The README describes the settings, decision scripts and notes as living in a domain; a move would change the layout and several parts.
- **Is `v[N]` part of the trading agent's name or of the strategy's?** It changes the names in "Names of strategies and trading agents" and every example path.
- **Do strategy folders carry the model and mode, or do folders take the shorter form `strategy-1/strategy-1.v1.Claude-Opus5.5/`?** Renaming touches every path under the prediction-market domain.
- **Is `apps/trading-ui/` still needed, or does the project IDE take its place?** The README lists it as the planned dashboard.
- **Where are positions kept, and where are market outcomes recorded?** The metrics part depends on both.
- **How do account entries map to key prefixes in the `.env` files?** The accounts part names the prefix rule but not the mapping.

## The owner's questions

None recorded yet.
