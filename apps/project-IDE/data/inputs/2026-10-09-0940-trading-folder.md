# in-20261009-0940: The owner makes trading a folder: agents/trading/prediction-market, later trading/copytrading
- At: 2026-10-09T09:40:23Z · Where: thread "Interactive file tree UI" · Source: chat · Ref: thread cmsg_01Sk8xdkWKCz34CUCfVMyQbxP1hyoB8xVJjehy8MzA6ckj, message cmsg_01Sk8xdkWKCz34CUCfVMyQbx4U8EmoHPCTY2p6Gn3Wc6oS
- Categories: structure, naming, docs-knowledge
- Summary: The owner makes trading a folder: agents/trading/prediction-market, later trading/copytrading; trading/docs gets its first three docs (vision, README, rebuild prompt); the prediction-market and copytrading docs are not touched now; the system also gets its three docs, and that is all for now.
- Same request as the owner's message of 2026-10-07 19:43 (message cmsg_01Sk8xdkWKCz34CUCfVMyQbxKanYQpQaagRC71F9CDQaC9), which was interrupted before it was saved; its text, word for word: "let's consider prediction market is a trading domain we can just add it to one folder trading/prediction-market, next one for trading could be trading/copytrading  and let's put in a  trading docs first 3 documents that relates to trading, prediction-market and copytrading we right now not need to touch, so yes make for system agent also 3 files and that is it for now"

## Raw input
~~~text
let's consider prediction market is a trading domain we can just add it to one folder trading/prediction-market, next one for trading could be trading/copytrading and let's put in a trading/docs first 3 documents that relates to trading, prediction-market and copytrading we right now not need to touch, so yes make for system agent also 3 files and that is it for now
~~~

## Answer
~~~text
Done. `agents/trading/` now holds the prediction-market domain and its own docs folder with a vision, a README and a rebuild prompt; copy trading will sit next to it later. The system's README and rebuild prompt are rewritten in general terms (its vision was already). The prediction-market docs were not touched; the trading text removed from the system docs is kept in archive/2026-10-09/ for that domain's docs later. File Tree page v48.
~~~

## Processed into
- D-059; file-tree.md v1.33 ([56], [56.1], [56.1.1]-[56.1.3], [19], [4]); docs/trading/{vision,README,rebuild-prompt}.md; .claude/docs/README.md and rebuild-prompt.md; architecture.md, glossary.md, conventions.md paths; plan 2026-10-09-0940-trading-folder; changelog 2026-10-09; page v48
