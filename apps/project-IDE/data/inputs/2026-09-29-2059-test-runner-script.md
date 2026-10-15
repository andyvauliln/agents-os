# in-20260929-2059: Why no runner script for agent tests?
- At: 2026-09-29T20:59:45Z · Where: project chat · Source: chat · Ref: cmsg_01Sk8xdkWKCz34CUCfVMyQbxHr2UtBpKJaHbsxytu72vst
- Categories: tests-research, question
- Summary: The owner asked why there was no script that runs agent tests from their test config.

## Raw input
~~~text
why we not have script to run by config for testing agent?  agents/                         # [49.1] tests of the prompt + sub-agents (LLM behaviour)
│   │           │   │   ├── tests.config.json           # [49.1.1] every agent test: enabled, last_run, last_result, next_action
│   │           │   │   └── [test-id].test.md           # [49.1.2] scenario
~~~

## Answer (given in chat)
~~~text
There is one, but it's hidden: a single shared run-tests script covers both agent and script tests. It's linked into each level's scripts folder, not the tests folder. I've asked the [file tree explorer](#cmsg_01Sk8xdkWKCz34CUCfVMyQbxP1hyoB8xVJjehy8MzA6ckj) thread to add a run file inside tests/agents and tests/scripts at every level, and update the page.

~~The file tree explorer thread is waiting for your OK to read the Claude Code docs pages on scheduled jobs.~~ [Edit: approved, and the answer is now in [file tree explorer](#cmsg_01Sk8xdkWKCz34CUCfVMyQbxP1hyoB8xVJjehy8MzA6ckj).]
~~~

## Processed into
- file-tree.md v1.11 (runner links [10.8.1.3], [10.8.2.3], [19.12.1.3], [19.12.2.3], [21.12.1.3], [21.12.2.3], [49.1.3], [49.2.3]; [2.7.3], [2.11.7], [14.1])
