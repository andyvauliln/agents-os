# in-20260929-1703: Every level has the same agent folder
- At: 2026-09-29T17:03:03Z · Where: project chat, reply thread under the file tree update · Source: chat · Ref: cmsg_01Sk8xdkWKCz34CUCfVMyQbxS6M2s9uuqt7NE592b6UhL2
- Categories: agents, structure
- Summary: The owner asked for three agent levels (system, domain, strategy) with an identical folder structure including CLAUDE.md, package.json, requirements.txt, init.sh and start.sh, with the system also reaching every agent's data.

## Raw input
~~~text
and for now each agents should have also this files ├── CLAUDE.md                           # [37] main agent prompt/instructions
│   │           ├── package.json                        # [38] JS deps + npm scripts
│   │           ├── requirements.txt                    # [39] Python deps
│   │           ├── init.sh                             # [40] one-time setup, creates the *.link symlinks
│   │           └── start.sh                            # [41] start one run / the scheduler. generally they should be indentical by files structure, it's just one that manage all domains and development system and another domain agents, responsable for domain and 3 type responsible for concreate strategy, system should have just all data from all agents in a related agent subfolder pls own docs or configs or etc
~~~

## Processed into
- D-022; vision.md v0.13; file-tree.md ([10], [19], [21], [23], [37]-[41]; standard folder in [2.7])
