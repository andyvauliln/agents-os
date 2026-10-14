# Questions: run-tests.system.link.js

## Open questions for the owner

None open.

## The owner's questions

### 2026-09-29: Why is there no script that runs agent tests from their config?

> why we not have script to run by config for testing agent?

There is one shared run-tests script for both agent tests and code tests. Each tests folder links it as `run-tests.system.link.js`, next to its `tests.config.json`; it runs that folder's tests and writes the results back into the list and into the level's logs. It is planned and still empty, and no test is written yet.
