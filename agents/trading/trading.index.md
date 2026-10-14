---
about: agent-os/agents/trading/
basis: b6acccba8273
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T15:07:13Z
---
# trading/

## What it is

The folder of trading domains. Trading is the first kind of work the Agent OS does, and everything about it lives below this folder, so the system level stays general. Today it holds `docs/` (trading's vision, README, README twin and rebuild prompt), `researches/` with the research studies, and the prediction-market domain `prediction-market/`, which waits for stage two. The copy-trading domain comes later, as a copy of the prediction-market domain. It is not an agent: it has no prompt, config, scripts or jobs of its own.

## Who looks after it

It is written by the owner and knowledge-base-agent.

## When and how it changes

It changes when a trading domain or a study is added, moved or removed, or trading's own docs change.

## Who uses it, and when

It is read by the owner, knowledge-base-agent and project-ide-agent.

## Where it is mentioned

It is described in `agents/trading/docs/README.md`, `agents/trading/docs/vision.md`, `agents/trading/docs/rebuild-prompt.md`, `agents/system/docs/README.md`, `docs/file-tree.md` and its folder's How it works file `agents/agents.index.md`.

## Related knowledge

The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `agents/system/CLAUDE.md` (section "Where the project is now: stage one"), `agents/system/docs/README.md` (section "Domains") and `docs/metadata.md`.

## Keep in mind

- When you add a trading domain, create it with `create-agent` as a copy of the prediction-market domain; never copy a folder by hand.
- When something about money, accounts, markets or orders is written, keep it inside `trading/`; nothing about trading goes above it.
- When this folder changes, check its docs and the system's README and rebuild prompt.
