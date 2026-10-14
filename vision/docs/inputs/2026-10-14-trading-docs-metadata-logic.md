# Input 2026-10-14: all trading information in the docs; the full metadata logic in ASD

- From: the owner, in the thread "Interactive file tree UI"
- Date: 2026-10-14

## Raw input
~~~text
for trading i think all current available information we need put in a docs, also i need detailed full explanation in asd style for the metadata logic, there should be all logic related to it in a new system add this to the top level docs
~~~

## Answer
~~~text
Done (D-067). Trading: all trading notes now sit in agents/trading/prediction-market/docs/ (the ten trading-*.md notes, doc-outlines.md, trading-vision-notes.md, common/, how-to/, index/accounts.md, and the two trading-parts files from the system README and rebuild prompt), each with its How it works and Details files; materialize.py treats that docs folder as stage one; the trading, system and project docs, CLAUDE.md and the file-index skill say so. Metadata: docs/metadata.md, the full metadata logic of the new system in ASD-STE100 (15 sections), linked from docs/README.md, README.asd.md, the rebuild prompt and CLAUDE.md's reading list. While checking it, found that found (scanned) items never showed their own How it works and Details on the page; enrich.py now reads them from the files next to the item.
~~~

## Processed into
- docs/metadata.md (new), docs/README.md, docs/README.asd.md, docs/rebuild-prompt.md, docs/vision.md
- agents/system/CLAUDE.md, agents/system/docs/README.md, README.asd.md
- agents/trading/docs/README.md, README.asd.md, rebuild-prompt.md, docs.index.md
- agents/trading/prediction-market/docs/ (the trading notes with metadata)
- vision/tools/materialize.py (stage_two), vision/tools/enrich.py (metadata of found items)
- skills file-index (both copies)
- apps/project-IDE/data/plans/2026-10-13-leave-vision-files.md
- decisions.md D-067
