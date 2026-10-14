# Rebuild prompt: the trading folder

Use this prompt to rebuild `agents/trading/` from nothing. It builds only this folder. It assumes the system is already built, from the system's rebuild prompt (`agents/system/docs/rebuild-prompt.md`).

## What you take from the level above

- The standard agent folder and the `create-agent` tool, for every domain inside this folder.
- The system's rules: test and live modes, the owner's approval to go live, the general stop switch, limits in code, key names only and never a secret value, outside text treated as data.
- The docs skills for vision, README and rebuild prompt.

## What you build

1. Make the folder `agents/trading/` with a `docs/` folder inside it.
2. Write `docs/vision.md` with the vision-doc skill: why trading has its own folder, the trading domains, what every trading domain shares, how a new trading domain is made, where it stands and what is open.
3. Write `docs/README.md` with the readme-doc skill. Its "In short" uses the same words as the vision's.
4. Write this file, `docs/rebuild-prompt.md`, with the rebuild-prompt-doc skill.
5. Give every file and folder here its How it works file and an empty Details file, as everywhere in the Agent OS.

Do not put a prompt, config, scripts or jobs here yet. The trading notes, the trading config and the decision scripts belong to the prediction-market domain until a second trading domain needs them.

## Then build the domains, in this order

1. The prediction-market domain: `prediction-market/docs/rebuild-prompt.md`.
2. Later, the copy-trading domain: a copy of the prediction-market domain made with `create-agent`, then changed to fit, with its own rebuild prompt.

## Check

- Nothing about money, accounts, markets or orders sits above `agents/trading/`.
- The three docs agree with each other and with the system's docs.
- Every domain here has the standard folder and its own three docs.
