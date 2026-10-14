---
about: agent-os/.secrets/test/
basis: fc2a99c201bc
written: 2026-09-30T20:11:26Z
by: knowledge-agent
confirmed: 2026-10-14T15:07:13Z
---
# test/

## Summary

The test side of the secrets store. It holds one file, `.env`, with all test keys; agents may read and update it because the keys are safe test credentials. Scripts load them through `load-secret`.
