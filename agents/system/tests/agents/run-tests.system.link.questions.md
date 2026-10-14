# Questions: run-tests.system.link.js

## Open questions for the owner

None open.

## The owner's questions

### 2026-09-29: Why is there no script that runs the agent tests from a config?

> why we not have script to run by config for testing agent?

There is one shared run-tests script for the agent tests and the code tests. Each tests folder links it as `run-tests.system.link.js`, next to its `tests.config.json`.

The script runs the tests of that folder. It writes the results into the list and into the logs of the level.

The script is planned and is empty now. There is no test yet.

Docs improved: agents/system/tests/agents/run-tests.system.link.index.md.
