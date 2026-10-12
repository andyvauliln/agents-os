# Trading in the Agent OS: vision

## In short

Trading is the first kind of work the Agent OS does, and everything about it lives in one place: a folder of trading domains, with trading's own docs and its research. A trading domain is one area of trading, such as prediction markets, where people trade on the outcome of events. Every trading domain runs many small trading agents side by side, tries each idea in test mode with no real money, keeps the versions that work and lets only the owner put real money in. The first trading domain is prediction markets on Polymarket; a new one starts as a copy of it and changes only what is its own. Today trading has its docs and its research, and the prediction-market domain is a set of empty folders waiting for the project's second stage.

## Why trading has its own place

The Agent OS runs agents of any kind, and its top level says only what holds for all of them. Trading brings much that other kinds of work do not share: money, trading accounts, markets, orders, fees, risk limits and trade alerts. Keeping all of it in one place keeps the rest of the system general and gives every trading domain one home for what trading means.

There are also many ways to make money by trading, and most first ideas fail. On prediction markets alone there are up to about eighty approaches; crypto, following traders who already do well and trading on what one well-known person says bring their own. One home lets these domains grow side by side, learn from each other and later be combined.

The goals: agents that make money cheaply in ways that are simple to understand; every idea tried in test first; real money always under the owner's control; and results compared fairly, so the better versions win.

## The concept

Trading is a folder, not an agent: it has no instructions, settings or jobs of its own. It holds trading's own docs, the research studies the trading domains start from, and the trading domains themselves.

Each trading domain is a full domain of the Agent OS and arranges its agents in three levels:

- **The domain agent** owns the area: it finds and creates strategies, makes sure the domain makes money and answers the owner's questions.
- **Strategy agents**, one per way to make money. A strategy can be plain code, AI or a mix, and may have its own way of testing on past data.
- **Trading agents**, also called variants: the versions of a strategy that actually trade, each with one set of changes, one AI model and one mode, test or live. A trading agent's name starts with its strategy and ends with its model and mode, so its versions sort together and can be compared.

Every agent has the same standard folder: settings, scripts, logs, data, docs, tests, research and its own AI setup, and a parent reaches its children's folders one level at a time.

What only one trading domain uses stays in that domain: its trading notes, its settings with risk limits and accounts, and its shared buy, sell and risk scripts. When a second domain needs the same thing, that part can move up into trading's own folder.

## How trading should work

1. **An idea becomes a strategy.** The owner gives a strategy in plain words, or the domain agent finds one in the research, and the domain agent creates a strategy agent for it.
2. **The strategy gets its first versions,** for example the same strategy on the strongest AI model and on a cheaper one.
3. **The owner approves before anything starts.** Every new trading agent comes with a short report and starts only after the owner approves it, always in test mode: orders are simulated or placed on a test network.
4. **Trading agents run and log everything.** Each run reads what its strategy needs, such as prices, decides and acts: buy, sell, sell everything, wait or plan its next run. Every order, test or live, is logged.
5. **Results are compared,** and the better versions become the strategy's standard. Which numbers decide is still open; the candidates are profit and loss, win rate, the deepest fall from a peak, forecast accuracy and cost.
6. **The strategy improves itself.** Through its self-improvement helper the strategy agent makes new test versions of itself, compares them and folds a winning change back into the strategy.
7. **Real money comes last.** When a trading agent has shown good results, the owner may give it an account with real money.

## What every trading domain shares

On top of what the system says for every agent:

- **Test first.** Every trading agent, including every version made by self-improvement, starts in test mode.
- **Only the owner puts in real money,** account by account, after good results. No agent can approve an account, and only the owner adds a live account's keys.
- **Every new configuration needs the owner's approval** after a short report.
- **New versions, never changes in place.** A change to a trading agent's settings, instructions, code or model makes a new test version with a new name.
- **Actions on blockchains only, for now.** Centralised exchanges and other apps are sources of information only.
- **Every order is logged,** in test and in live.
- **Keys stay in the keys store,** known to everything else by name only.
- **Outside text is data,** never instructions; protection against hidden instructions is built together with live trading.

Two more are our proposals, the defaults until the owner decides: risk limits written in code and checked before every order, which a lower level may only tighten; and an order stop switch in each trading domain that refuses every new order at once.

## How a new trading domain is made

A new trading domain is a copy of the prediction-market domain, made when the owner asks. It keeps the levels, the standard folders, the trading notes, the shape of the settings and the shared scripts, then changes what is its own: where it may act, what information it collects, its fees, strategies and risk limits. Its domain agent is created like every agent, and it starts with no real money.

## Examples

**A first strategy, from the idea to real money.** The owner gives a Polymarket strategy in plain words. The prediction-market domain agent creates a strategy agent, which sets up three test versions: on the strongest model, on a cheaper model, and with a small change to its settings. The owner reads a report on each and approves them. They trade in test mode, and their logged orders are compared. The cheaper version earns almost as much for far less, and becomes the strategy's standard. When its results hold, the owner gives it a small account with real money.

**A second trading domain.** The owner wants agents that follow traders who already do well. The new domain starts as a copy of the prediction-market domain and changes what is different: which traders it watches and where it may act. Its first agents start in test mode, and everything shared works for it at once.

## What the owner sees and does

- They give strategies in plain words and read the research.
- They approve every new trading agent and decide which ones get real money.
- They watch every agent's results and orders, and can stop or delete any trading agent at any time.
- They alone change risk limits and accounts.

## Where it stands and what comes next

Nothing that trades is built yet. Trading has its docs and its research: about forty studies of ways to make money on prediction markets with their evidence, a study of agents that improve themselves and a study of how trading agents are built. The prediction-market domain exists only as empty folders, for its domain, one strategy and one trading agent; its designs are kept aside.

In the first stage, now, the project finishes the owner's project page, the metadata of every file and the docs of the project, the system and trading in general. In the second stage the prediction-market domain is written again from its kept designs, and the first run starts small: the system agent, the domain agent, one strategy agent and two or three trading agents, all in test mode. Later, more trading domains are copied from it.

## Principles

- **Nothing about money goes above trading,** so the system stays general.
- **What one domain uses stays there; what several share moves up,** so trading's own folder stays small until sharing is real.
- **The owner approves real money, every time,** because it is the one thing no agent may decide.
- **An AI may propose a trade; code checks the limits,** so a mistaken or tricked AI cannot break them. This is our proposal.

## Ideas we are still weighing

**One part that places every order.** If every agent places its own orders, a bug in one can skip a limit. Instead, agents would only write the orders they want, and one shared part would check the limits and place them. All money checks would sit in one place.

**One ledger for positions and cash.** If each agent keeps its own record of what it holds, records can disagree with the account. One ledger, written only by the part that places orders, would give one true answer to what is held.

**Champion and challengers.** A version that changes itself while trading can drift unnoticed. Instead, each new version would have to beat the current best in test, over the same period, before it takes its place.

## Open questions

- **How is success measured?** It sets what self-improvement aims for.
- **How much money goes live first?** It sets how much a mistake can cost.
- **What happens to open positions when trading is stopped?** Closing them needs orders while the stop refuses new ones.
- **May a strategy fold a winning change into itself without the owner?** It decides how fast strategies improve and how much the owner reviews.
- **Which trading domain comes next, and when?** Copy trading is the likely one.
- **How are trading agents named on disk?** A shorter form with the model's full name has come up next to the names in use.
- **How does the owner get trade alerts?** The channel is not chosen yet.

## Going deeper

The README describes every part of trading exactly: its folders, its research, what every trading domain holds and where each part's docs are, at `agents/trading/docs/README.md`.
