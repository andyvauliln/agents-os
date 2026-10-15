# in-20260930-1045: One content-folder template with subagents.link/
- At: 2026-09-30T10:45:57Z · Where: thread: Interactive file tree UI · Source: chat · Ref: cmsg_01Sk8xdkWKCz34CUCfVMyQbxXGCuFLc1qeYHMdr5VRq7nb
- Categories: links, structure
- Summary: The owner asked for one template at every level: each content folder (docs, research, tests, scripts, configs, data, logs) holds the level's own files plus subagents.link/[child]/ for each child agent, and no .claude folders are linked for now.

## Raw input
~~~text
look we need this kind of structure for all domain layers so system should have on example of docs so own docs folder inside own docs and [docs]/subagents.link/[domain_name](here related docs)   and it should be same template for another folders like research, tests, scripts, configs, data, logs. domain agent should have same [docs]/[ /subagents.link/[agent_name](here related docs). strategy layer same. and for now let's not symlink claude related folders in system and domain, strategy ...,  so update all file tree base on it and make related changes in a docs or whatever it needs right now
~~~

## Processed into
- D-030; vision.md v0.18; file-tree.md v1.14 ([2.7.4], [2.20], [11.2], [14.4], [15.5], [16.4], [10.8.3], [10.9.3], [19.x] and [21.x] subagents.link/; [10.1.3], [10.1.4], [21.1.3], [21.1.4] retired; [11.12] merged into [11.2]); feature-map.md v1.10
