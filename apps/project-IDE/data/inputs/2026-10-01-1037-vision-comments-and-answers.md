# in-20261001-1037: Comments on the vision and answers to its open questions
- At: 2026-10-01T10:37:47Z · Where: thread "Interactive file tree UI" · Source: chat · Ref: cmsg_01Sk8xdkWKCz34CUCfVMyQbxTWVpRpfxXGnimz1a5xaA8w
- Categories: vision, agents, process
- Summary: The owner commented on the people vision: end-of-run compression, run triggers (e.g. when research finishes) and a parallel-run limit set by a system helper; agreed that strategies can be code, AI or both, that each strategy has its own back-testing, that agents subscribe to each other's data (risk manager, news worker), and that a workers agent handles worker requests; deferred outside-text protection to live trading; answered most open questions (first strategy given by the owner, real money after good results, start scale, venues per strategy, reuse of Polymarket tools, own server, owner approves every new strategy configuration, SI and agents free, per-agent back-testing and memory, test/live for every action with testnets, blockchain-only actions for now, JSON CRUD scripts); asked for the pull, executor, ledger and digest ideas to be explained as problem and solution so they can decide.

## Raw input
~~~text
ITS mine comments and answers, update whatever you need update now, tell me what you update and we continue with points i not understand give me more information and we decide there. 

From Vision

**2. Giving each agent only what it needs.** When an agent is created, it is handed exactly the files its strategy uses, so it never wades through information that does not matter to it. On every run it reads everything that is new since its last run. all important information from last compressed or summarised and what is not need or not important cleaned for next run, 2)
**4. Running at the right moments.** Agents run on a regular interval, and also when an important file changes. In that case the current run is stopped and a new one starts with the fresh information. Unimportant changes simply wait for the next run. - if it some trigger happen, for example he start research for somthing and he need run when research finished get all run information he subscribed and including this research. 3 Add also that we probably should have max agent running limition base on server it's running, so shoulв be probably agent aslo that can check system and configure how many in parallel can be runed. 4)

## Ideas we are still weighing

135- **Agents pull their own information.** Instead of having files linked in, each agent would fetch what it needs and keep a bookmark of what it has already read. Workers would not need to know about agents, and replaying history for back-testing would be easy. For now files are linked; how an agent keeps track of what is new since its last run is still open.

I don’t really get it explain better and easer and how we get here some more context problem solution

136- **Agents decide, a separate part acts.** An agent's decision would become a clear order that passes risk checks written in code, then goes to one executor that can trade live, on paper or in a back-test. Test mode would become a simple setting.

I don’t really get it explain better and easer and how we get here some more context problem solution

137- **A ledger keeps the true positions.** One record would hold what every agent owns, and agents would only see a read-only copy.

I don’t really get it explain better and easer and how we get here some more context problem solution

138- **Not every strategy suits an AI loop.** Market making and arbitrage need fast, event-driven code, so strategies could be plain code, AI, or a mix. yes this correct

139- **Digest information once.** Shared summaries would be built once for everyone, each agent would filter them, and every run would end with a short memory note.

I don’t really get it explain better and easer and how we get here some more context problem solution

140- **AI back-tests can cheat.** A model may already know how past events turned out, so paper trading is the honest test for AI strategies. Every strategy can have they own way for backtasting 

141- **Outside text cannot be trusted.** News, videos and social posts can hide instructions aimed at AI, so hard risk limits would live in code, not in an agent's instructions. we think about this problem when we ll build live account we ll put some protection layers at this point.

142- **Agents that use other agents.** Some agents would take other agents' signals as input, to combine strategies or share out capital. yes agent to agent for example risk managment bot that got some news about that everytihng collapsing big war or something, so he ll need give information for all agent to sell everything what they have, of for example it ll be news domain agent or worker that handling twitter post on specific topic and another aggent can decide this information is usefull for mine strategy and subscribe on this data and when some news came he ll put information in a his data, and another agent when next time run or if it data that can interrupt his work

143- **Limits on new workers.** Before an agent gets a new worker, the system would check whether the information already exists, so hundreds of agents do not create duplicates. Yes if some agent need some worker he need ask worker agent who know how to create them and know what is exist what is not, or maybe just need extend already working and give information about data to the agent it needs that he can have access to it and know when and how to use it for it self

145## Open questions

**147- **Which strategies go first?** The first area is prediction markets on Polymarket and the next is copy trading, but the first two or three strategies are not chosen yet. We go like this, i give first one strategy from polymarket and we start the wheel and see how it works and self imrove, later continue with another after reaching a good flow**

**148- **When does real money start?** Whether to begin with paper trading only, and with what limits on capital. also real money goes after we make any good agent and strategy that shows some results**

149- **How big, and at what cost?** How many agents run at once, how often, and what AI budget that allows. Right now will be running system agent, domain agent, strategy agent and 2-3 configurations

150- **Which markets and accounts?** Which trading venues are available, given country rules, identity checks and API access. also later every strategy ll have it’s own so we decide when first strategy ll be in development

151- **What happens to the existing Polymarket tools?** The current suite covers liquidity provision, arbitrage across platforms, trading on outcomes that are already known but not yet settled, and copy trading. They could be reused as strategies, kept separate or replaced. yes some strategy workers and datas can be used in another agents strategies and etc

152- **Where does it run?** On the owner's computer, a rented server or the cloud, and which machine runs the scheduler. Now we ll use one of mine server, but we should be able easly run on another with more resourses

153- **What else needs the owner's approval?** Funding live accounts does; other actions, and the way the owner is notified, are open. for now if we create new configuration of strategy i want to see report about that approve and then this agent can start working

154- **How free is self-improvement?** What it may change without asking, and how success is measured: profit, win rate, biggest loss, or how well its odds match reality. how i said it can do whatever it needs, but for approve run some new strategy configuration i would approve it

155- **How free are agents to create workers and helpers?** And within what limits. free to do whatever they want for now

156- **How much history is kept** for back-testing and analysis. Every agent ll have own backstrategy if applicable for this agent, with own configurations and strategy how to test it for example i want this strategy have 1 month of testing on a old data but it should be appoached as a live data etc, every agent can take decision to compress or summarise information he need for next run, stay in the same session or create new, what he need every run what is not or decide for example in this case i want this information too and subscribe to additional avalable information or make additional research or create additional workder etc.

157- **How are live keys handled** once real-money trading begins. yes, but generally all actions like buy sell and etc should support at the begining and test and live mode, i guess for example for blockchain things sometimes for test we can use testnets and etc and on a live main networks. Generally for now we ll handle only blockchain trading with a support any kind of networkds apps there, from cetralased solution like exchanges another app we can just collect infomrations but not do for now any actions there,

also as we right now deal with files and lists we ll keep a json files, so i guess we ll need special scripts to deal with them like crud , filter operations that agent can
~~~

## Processed into
- D-035 (decisions.md): every answer and comment above.
- `.claude/docs/vision.md` rewritten: How it works steps 2, 4, 5, 6 (new: testing on the past), 7, 8 (new: agents listening to each other); What it is made of (workers helper, code/AI/mix strategies, JSON list scripts, the server); owner approves every new variation; Where we are now (Polymarket tools reused); What comes next (start scale, first strategy, venues per strategy, outside-text protection with live trading); principle "free to act inside those limits"; the four unclear ideas rewritten as problem, idea, what it would change; open questions cut to five.
- Agent rule "Problem first"; vision skill: ideas as problem, idea, change; system length 2,000 to 3,500 words.
- Notes `vision/docs/vision.md`: idea and question entries updated to the answers; new entries for run memory, run triggers, parallel limit, action scope and JSON scripts.
- Waiting for the owner: decide the four ideas (bookmark, executor, ledger, digest).
