# Trading in the Agent OS: vision

## In short

Trading is the first kind of work the Agent OS does. All of it lives in one folder, `agents/trading/`, which holds the trading domains side by side: today the prediction-market domain, and next a copy-trading domain. Every trading domain runs many small trading agents at the same time, tries each idea in test mode first, keeps what makes money and lets the owner approve anything that touches real money. A new trading domain starts as a copy of the prediction-market domain and then changes only what is its own.

## Why trading has its own folder

The Agent OS runs agents of any kind, and the system level says only what holds for all of them. Trading brings a lot that the other kinds do not share: money, accounts, markets, orders, fees, risk limits and trade alerts. Keeping all of that below one folder keeps the system general, and it gives every trading domain one obvious place to look for what trading means.

There are many ways to make money by trading. On prediction markets alone, where people trade on the outcome of events such as elections or sports, there are up to about eighty approaches, and most first ideas do not work. Other markets, and other ways of trading such as following traders who already do well, bring their own approaches. One folder for all of them lets these domains grow next to each other, learn from each other and later be combined.

## The concept

`agents/trading/` is a folder of trading domains. Each domain inside it is a full domain of the Agent OS, with its own domain agent and the standard agent folder, and it arranges its agents in the levels its work needs.

- **The prediction-market domain** (`agents/trading/prediction-market/`) is the first. It trades on Polymarket first. Below its domain agent sit its strategy agents, each owning one way to make money, and below each strategy its trading agents, the versions of that strategy that actually trade.
- **The copy-trading domain** (`agents/trading/copytrading/`) comes next. It will follow traders who already do well. It is not in the tree yet and nothing is decided about it beyond its place.
- **Trading's own docs** (`agents/trading/docs/`) are this vision, a README and a rebuild prompt. They say what every trading domain shares and how a new one is made.

For now the trading folder holds nothing else. The trading notes, the trading config and the shared buy, sell and risk-check scripts stay inside the prediction-market domain, because it is the only domain that uses them. When a second trading domain needs the same thing, the shared part can move up into `agents/trading/`.

## What every trading domain shares

These hold for any trading domain, on top of what the system says for every agent:

- **Test first.** A trading agent runs in test mode, with no real money, until it has shown it works. Only the owner approves an account with real money.
- **Limits only get tighter.** A domain's risk limits, its accounts and its order stop switch live in its config. A lower level may only make a limit tighter, never looser, and changing the limits or the accounts needs the owner's approval.
- **New versions, never changes in place.** Changing a trading agent's settings, prompt, code or AI model makes a new test version with a new name. A running version is not changed.
- **Names say what an agent is.** A trading agent's name starts with its strategy and ends with its AI model and its mode, so agents that differ only by model run side by side and can be compared.
- **Every order is logged.** Orders go to the domain's order logs, and the owner gets the trade alerts the domain's config asks for.
- **Actions on blockchains only, for now.** Orders are placed on blockchain venues. Centralised exchanges are used only as sources of information.

## How a new trading domain is made

A new trading domain is a copy of the prediction-market domain. The copy keeps the standard folder, the trading notes, the config shape and the decision scripts, and then changes what is its own: its venues, its fees and market filters, its strategies and its risk limits. Its domain agent is created like every agent, never by copying a folder by hand, and it starts with no money until the owner approves.

## Examples

- A strategy in the prediction-market domain watches the price of a market on Polymarket every five minutes. Its trading agents are versions of that strategy with different settings or AI models. They all run in test mode, and the one that does best becomes the standard.
- Later, the copy-trading domain picks traders who have done well and follows their trades in test mode. If the results hold, the owner may approve a small account with real money.

## Where it stands

Nothing is built yet; this is the plan. The trading folder exists in the plan with its three docs. The prediction-market domain has its own notes, config and scripts in the plan. The copy-trading domain is only named.

## Principles

- Trading is one kind of work in a general system, so nothing about money goes above `agents/trading/`.
- What only one trading domain uses stays in that domain; what two or more share moves up into `agents/trading/`.
- The owner approves real money, every time.

## Open questions

- What the copy-trading domain trades on, and which traders it follows.
- Which parts move up into `agents/trading/` once there are two trading domains.
- What the order stop switch does with positions that are already open.
- How success is measured in numbers for a trading domain.

## Going deeper

- The system's vision: `agents/system/docs/vision.md`.
- The prediction-market domain and its trading notes: `agents/trading/prediction-market/docs/`.
- This folder's README and rebuild prompt, next to this file.
