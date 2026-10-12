---
about: agent-os/agents/trading/prediction-market/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/init.sh
node: n-40
basis: d120c27eb841
written: 2026-10-01T01:03:51Z
by: summary-worker
confirmed: 2026-10-07T19:05:50Z
---
# init.sh

## Summary

The agent's setup script, safe to run again. It installs the dependencies from `package.json` and `requirements.txt`, then runs `relink --agent` for this agent, which builds its file links from its links file and its entries in its strategy's `subagents.link/` folders. It also registers the agent in the index and the UI. create-agent runs it once; later link changes need no re-run, since relink runs by itself. This wiring is proposed; whether create-agent generates the script is open.

## Keep in mind

- When you change a links file, do not re-run `init.sh`; relink picks up the change by itself.
- When you need a link, let relink build it; never make a symlink by hand.
