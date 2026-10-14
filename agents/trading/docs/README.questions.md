# Questions: README.md

## Open questions for the owner

- **Which shared trading parts move up into `agents/trading/` when there are two trading domains?** The README puts the settings, the decision scripts and the notes in a domain. A move changes the layout and many parts.
- **Is `v[N]` part of the name of the trading agent, or of the strategy?** The answer changes the names in "Names of strategies and trading agents". It also changes each example path.
- **Do the strategy folders show the model and the mode?** The alternative is the shorter form `strategy-1/strategy-1.v1.Claude-Opus5.5/`. A new name changes each path in the prediction-market domain.
- **Do we still need `apps/trading-ui/`, or does the project IDE replace it?** The README shows it as the planned dashboard.
- **Where do we keep the positions, and where do we record the market results?** The metrics part needs both.
- **How do the account entries relate to the key prefixes in the `.env` files?** The accounts part gives the prefix rule. It does not give this relation.

## The owner's questions

### 2026-10-07: Did all the trading parts move down?

> also did we remove all related to trading agent down to trading agents in our case i think to prediction market domain

Not at that time. The agent did it on the same day.

Today the system level stays general. It has nothing about money, markets or orders. All trading knowledge is in `agents/trading/prediction-market/docs/`.

This changed later: trading became a folder of domains, `agents/trading/`, with its own docs. The prediction-market domain is in that folder.

Docs improved: agents/trading/docs/README.md, agents/trading/docs/README.asd.md, agents/trading/docs/README.index.md, agents/trading/docs/vision.index.md.
