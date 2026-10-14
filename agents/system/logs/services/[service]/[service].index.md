---
about: agent-os/agents/system/logs/services/[service]/
node: n-15.2
basis: 35090fb4837a
written: 2026-10-07T19:01:11Z
by: knowledge-base-agent
---
# services/[service]/

## Summary

One log folder per acting service shared by several domains, named after it. Every action, test or live, is one JSONL line: when, the service, the mode, the agent, the account, the action and its result, `blocked_by_kill_switch` included. A domain's own acting services log in the domain, such as the prediction-market domain's order logs. The format is proposed.

## Keep in mind

- When you build an acting service, log every action here, test or live, blocked ones included.
