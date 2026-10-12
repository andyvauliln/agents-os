# Trading

## In short

Trading is the first kind of work the Agent OS does. All of it lives in one folder, `agents/trading/`, which holds the trading domains side by side: today the prediction-market domain, and next a copy-trading domain. Every trading domain runs many small trading agents at the same time, tries each idea in test mode first, keeps what makes money and lets the owner approve anything that touches real money. A new trading domain starts as a copy of the prediction-market domain and then changes only what is its own.

## Trading at a glance

- **What it is:** a folder of trading domains, not an agent of its own. It has no prompt, config or jobs of its own yet.
- **What it shares:** the trading rules every trading domain follows (test first, limits only get tighter, new versions instead of changes in place, every order logged). They are written in the vision next to this file.
- **What it does not hold yet:** the trading notes, the trading config and the decision scripts. They stay in the prediction-market domain until a second domain needs them.

## Layout

```
agents/trading/
├── docs/                 trading's own docs
│   ├── README.md         this file
│   ├── vision.md         why trading, what every trading domain shares
│   └── rebuild-prompt.md how to rebuild this folder
└── prediction-market/    the first trading domain
```

`copytrading/` will sit next to `prediction-market/` when it is added.

## Its domains

- **Prediction market** (`prediction-market/`): trades on Polymarket first, with strategy agents and below them their trading agents. It holds the trading notes, the domain config with risk limits, accounts, venues and the order stop switch, and the shared buy, sell and risk-check scripts. Its README: `prediction-market/docs/README.md`.
- **Copy trading** (`copytrading/`): next, not in the tree yet. It will be a copy of the prediction-market domain.

## Info, settings, jobs, tests and research

None at this level yet. Each domain keeps its own in its standard folder.

## Where the docs are

- This folder: `docs/vision.md`, `docs/README.md`, `docs/rebuild-prompt.md`.
- The level above, the system: `agents/system/docs/`.
- Each domain: its own `docs/`.

## Still open

- What the copy-trading domain trades on.
- Which parts move up here once there are two trading domains.
