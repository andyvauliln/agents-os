# Plan: trading as a folder of domains, and the top docs

Status: done · Request: in-20261009-0940 · Updated: 2026-10-09

## The request

You asked to put the prediction-market domain into one folder, `trading/prediction-market`, with `trading/copytrading` as a later one; to give `trading/docs` its first three docs; to leave the prediction-market and copy-trading docs alone for now; and to write the system's three docs too, "and that is it for now".

## The change

1. `agents/trading/` [56] is new. For now it holds only `docs/` [56.1] with `vision.md`, `README.md` and `rebuild-prompt.md`, and its domains. No agent, settings or scripts of its own yet.
2. The prediction-market domain moves to `agents/trading/prediction-market/` and keeps its number [19] and everything inside it, including its file names. Every path that names it changes; relative links from it to the system get one more `../`.
3. Copy trading stays out of the tree; trading's docs name it as the next domain.
4. The system's README and rebuild prompt are rewritten in general terms, like its vision; trading's three docs say what all trading domains share and where it lives today (in the prediction-market domain).

## Steps

1. Save your message, this plan, decision D-059.
2. Tree, notes, tools, mirror tree: the new folder and the move. Check: parse and the map report no problem; every link resolves.
3. Trading's three docs.
4. The system's README and rebuild prompt.
5. How it works for the changed items; rebuild, check and publish the page; push to GitHub.

## Log

- 2026-10-09 09:45: plan written; building.
- 2026-10-09: all steps done: trading folder, trading's three docs, system README and rebuild prompt in general terms (removed trading text archived in archive/2026-10-09/), How it works 404/404 fresh, page v48.
