# in-20261007-0852: why the agents have no rebuild prompt
- At: 2026-10-07T08:52:10Z · Where: thread "Interactive file tree UI" · Source: chat · Ref: thread cmsg_01Sk8xdkWKCz34CUCfVMyQbxP1hyoB8xVJjehy8MzA6ckj, message cmsg_01Sk8xdkWKCz34CUCfVMyQbx4xHfzJTVJjPqkDBWzXpW8m
- Categories: docs-knowledge, question
- Summary: The owner asks why the domain, strategy and trading agents have no rebuild prompt in their docs.

## Raw input
~~~text
why agents didn't got a rebuild-prompt?
~~~

## Answer
~~~text
Because when we created the rebuild prompt, we proposed that lower levels get theirs only once their parts are designed in detail, so only the system had one. Your decision last night that every level has all three docs was still waiting in the plan, while the apps got theirs at once because you asked for them directly.

That's fixed now. Every domain, strategy and trading agent lists its own rebuild prompt, and the trading agent also gets its own vision, which was missing too. Each prompt builds only its own folder and lists its children's prompts in build order. None is written yet; they come with the docs at every level. The File Tree page shows them.
~~~

## Processed into
- D-053 changed (applies and Changed); file-tree v1.30 (new [19.6.4], [21.6.4], [46.3], [46.4]; [19], [19.6.x], [21.6.x], [46], [2.22]); rebuild-prompt-doc skill (every level has its own); README (domains, strategies, trading agents, docs at every level); rebuild prompt (tree, parts 3 to 5); sources notes; How it works of the new files, the three docs folders, the skill and the system's rebuild prompt; page v44 (data v38).
