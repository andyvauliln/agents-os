# Questions: README.md

## Open questions for the owner

- **Which shared trading parts move up into `agents/trading/` once there are two trading domains?** The README describes the settings, decision scripts and notes as living in a domain; a move would change the layout and several parts.
- **Is `v[N]` part of the trading agent's name or of the strategy's?** It changes the names in "Names of strategies and trading agents" and every example path.
- **Do strategy folders carry the model and mode, or do folders take the shorter form `strategy-1/strategy-1.v1.Claude-Opus5.5/`?** Renaming touches every path under the prediction-market domain.
- **Is `apps/trading-ui/` still needed, or does the project IDE take its place?** The README lists it as the planned dashboard.
- **Where are positions kept, and where are market outcomes recorded?** The metrics part depends on both.
- **How do account entries map to key prefixes in the `.env` files?** The accounts part names the prefix rule but not the mapping.

## The owner's questions

### 2026-10-07: Did everything about trading move down?

> also did we remove all related to trading agent down to trading agents in our case i think to prediction market domain

Not yet at that moment; it was done the same day. Today the system level stays general, with nothing about money, markets or orders, and all trading knowledge sits in `agents/trading/prediction-market/docs/`. This changed later: trading became a folder of domains, `agents/trading/`, with its own docs, and the prediction-market domain sits inside it.
