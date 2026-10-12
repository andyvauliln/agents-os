---
about: agent-os/agents/system/docs/common/self-improvement-templates.md
node: n-2.17.4
basis: 52db3ccbc6f6
written: 2026-10-07T19:01:11Z
by: knowledge-base-agent
---
# self-improvement-templates.md

## Summary

The templates every self-improvement helper is built from. It sets what each one does (take in logs, data, research, news and owner comments, and improve what it owns through new test agents), a base helper file, and what the system's and a domain's helper own, read and write. A domain adds templates for the levels it defines, as the prediction-market domain does for its strategies. Most of it is proposed.

## Keep in mind

- When a self-improvement helper changes anything, it makes a new test agent; it never edits a running agent, touches live agents or loosens a limit.
- When a self-improvement helper writes memory, it keeps lessons and research ids only, never the research itself.
