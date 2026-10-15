# in-20260929-1455: First folder layout, agent types and workflow
- At: 2026-09-29T14:55:08Z · Where: project chat · Source: chat · Ref: cmsg_01Sk8xdkWKCz34CUCfVMyQbxH8bwvmiNMqshe7iCk9SRPc
- Categories: vision, structure, agents
- Summary: The owner gave the first folder layout (docs, agents with system and trading domains, apps, trading-ui), model and platform routing, agent types, triggers, test and live modes, JSON/MD data and the self-improvement workflow, and asked to update the vision and start a numbered file tree to review object by object.

## Raw input
~~~text
[README.md](http://readme.md/)

* docs // common docs about os and how it works (self support logic)
   * [vision.md](http://vision.md) (all mine inputs about system summaresed and structured, ll be context for another agent and knowing system better)
* agents
   * docs (self support logic)
      * now we need made on agentic system in a file tree view with a comments, on example of one agent, with full agents folder and file description and understanding what is it
      * common knowledge how agents works architecture, data, data flow etc
      * catalogs list of all agents, services, apps, and some base information about them
      * shared/common things how it works on this common level for all agents
   * system // everything that have every agent or most of the agent or belong the all system
      * configs(common and symlinks for every agent folder)
      * workers [scripts or agents that run scheduled and produce data] (common and symlinks for every agent folder)
      * subagents (common and symlinks for every agent folder)
      * scripts (common and symlinks for every agent folder)
      * logs (common and symlinks for every agent folder)
      * data (common and symlinks for every agent folder)
      * platforms and models [like claude code(default) fable Opus 5.5 with xhigh effort for all thingking planing inetelegant task and main agents, analysis improvments, sonet 5.5 medium for all not important tasks, cursor(supported for now model composer 2.5 for any task when we easy job or handle some data use it mostly for workers subagent that need make some things done light analysis, filtreation, etc also where we use a lot of tokens, but still not a intelegent job), openrouter (supported for now but not connected right now, some free models rotation on not imporatant things), codex(suported later), kimi 3 (supported later)]
         * here we need understand and configure all object that use ai and right route for them, like this agent X - do this things with this model or platform
   * trading-domains
      * prediction-market-agents
         * main-domain-agents
            * find, analyse, create, update, strategies and self improvment agents for them
            * resposible for all domain and that it make money eveything goes smooth
            * answer all question about the state of the system address mine comments
         * strategy-1-agent
            * pm-self-improvment-agent (long live with a memory agent, run ones in a time take last infromation from agent logs data ressearches and outside the world of mine left comments, run researches if need should be dynamic base on strategy but made with some of out templates how to build self improvment, he need make this strategy, be fast, cheap, efficient, simple, understandable, profitable, fix bugs, issues, test )
            * pm-[modifications-stretegy-1]-agent-[platform-model]-[test/live]
               * .claude
                  * skills
                  * agents
                  * …
               * config
                  * workers.config
                  * …
               * docs
               * scripts (for now just js/ts, python)
                  * [get-polymarket-data.worker.py/js](http://get-polymarket-data.worker.py/js)
                  * clean-data.system.js
                  * make-buy.decions.js
                  * …
               * logs
               * data
                  * worker-name/agent name
               * [CLAUDE.md](http://CLAUDE.md)
               * package.json
               * recirements.txt
               * [init.sh](http://init.sh)
               * [start.sh](http://start.sh)
      * copy-trading-agents
         * …
* apps (for the apps that we clone from github for our use or agent use)
   * some-github-repo
* trading-ui
   * nextjs api ui.
   * monitoring, analysis of all agents and system

Workflow
i or system by it self give some input for creating new agent, system should know how to create agent and integrate them in a system,
agent it’s harness/platform/model that represent main agent it runs one in a time get any information it needs for it self from workers or subagent to take a decision.
System should work like a wheel constantly self improving and analysing it self, i can just say create new agent base on this input and i just can see ui with a perfomance of agents, have ability to prove or not prove if i give account with a money, stope, delete, make comments ask question for this agent from ai, say what to do to be better etc, and i want see full view on agents all his components, logs, perfomance, what data he use what produce, all decisions he made, all improvments he had or what we change exactly in this agent to test it.
Self impovment logic should analyse this bot do if need additional research and make new configuration or whatever to test this new agent, new agent going on test. this logic also should get something from outside the system like related news, like new harness or new model came out system should update related logic and then run new agent for building new configuration for the agent in a testing them in a new configuration
types of agent,

* system support develompment, documentation, improvment, analyses, research …
* sub agents that take data from workers and preanalise it to main agents (worker+ai)
* main agent that run some strategy and take a descions (live/test mode)

for now let’s just use for data json and md files
agents should be run in interval of the time or if some of the files was update and it’s important and need cancel current run if it goes and start new with new information, some files could have not important information so system can wait next run
all services that do some action should have test mode and live mode and tooked from configurations. ...... it's mine some new thoghuts how it should works and some vision, update vision base on it.  for now goal make skeleton in a file tree views with explanation and detalisation of every file and folder, after you update vision, let's make another document file tree view and go one by one you ask me question about every object there and i ll give mine inputs and we udpate file tree view base on it
~~~

## Processed into
- D-001; D-005; vision.md v0.2 (§7-§14); overview.md v0.2; file-tree.md v0.1 (numbered skeleton, example agent [23])
