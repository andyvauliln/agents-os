---
about: agent-os/agents/trading/prediction-market/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/start.sh
node: n-41
basis: 455015bb168f
written: 2026-10-01T01:03:51Z
by: summary-worker
confirmed: 2026-10-07T19:05:50Z
---
# start.sh

## Summary

Starts the agent for one run. The scheduler calls it for the main-run job in the workers file, every 15 minutes in the example, and the owner can also run it by hand. Through `run-agent` it merges the config, writes `logs/effective-config.json` and starts Claude Code headless in the agent's own folder, with its own `.claude/` and links. Unlike the system's `start.sh`, it does not start the scheduler. How it ties in is proposed.
