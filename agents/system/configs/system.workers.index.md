---
about: agent-os/agents/system/configs/system.workers.json
node: n-11.10
basis: 7c1542d4df4a
written: 2026-10-07T19:01:11Z
by: knowledge-base-agent
confirmed: 2026-10-09T10:48:55Z
---
# system.workers.json

## What it is

The list of everything the system agent itself runs, on a schedule or on demand: relinking and link checks, tests, index rebuilds, data collectors shared by several domains, its helpers' runs, and the knowledge base agent's regular sync. Each job is either a plain script or an AI run, and says whether it is on, when it runs, where, and with which AI model. Every agent has a file just like it.

## Who looks after it

The owner, from the dashboard: turning jobs on or off and changing when, where and with which model they run. The system's helpers propose changes. For now every job is off (the owner, 2026-10-09): they stay in the file and run only once turned on.

## When and how it changes

Only when someone adds, changes, pauses or removes a job. What actually happened when a job ran is kept elsewhere, so the file does not change with every run.

## Who uses it, and when

The scheduler reads it to start each job at its time; the dashboard and the list of all jobs show it.

## Where it is mentioned

The jobs files of every other agent, which use the same format; the list of all jobs; the scheduler.

## Related knowledge

- A live job needs the owner's approval and an agent on the live list.
- Jobs that run in the cloud, on the desktop or on GitHub get no keys and never act live.
- The exact fields are a proposal.

## Keep in mind

- When you want to pause a job, turn it off; never delete it to pause it.
- When a job would act live, get the owner's approval first.
