---
about: agent-os/.secrets/test/
node: n-47.1
basis: 522991459bf9
written: 2026-09-30T20:11:26Z
by: knowledge-agent
confirmed: 2026-10-07T14:22:08Z
---
# test/

## Summary

The test side of the secrets store. It holds one file, `.env`, with all test keys; agents may read and update it because the keys are safe test credentials. Scripts load them through `load-secret`.
