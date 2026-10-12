---
about: agent-os/agents/system/docs/index/models.md
node: n-2.18.6
basis: b9ab293511a1
written: 2026-10-01T00:58:42Z
by: summary-worker
confirmed: 2026-10-07T19:02:04Z
---
# models.md

## Summary

A readable view of the routing in `models.config.json`: every platform and model with its status, default effort and use, and who routes to it (type defaults, named routes, jobs, agents whose name carries the model). Claude Code with Opus 5.5 is the default; Sonnet 5.5 and Cursor's Composer 2.5 are supported, OpenRouter is not connected yet, and Codex and Kimi come later. Open: type names, default effort and the sub-agent default differ between the config and the File Tree page.

## Keep in mind

- When you change a route or a model's status, change `models.config.json`; this file only mirrors it.
