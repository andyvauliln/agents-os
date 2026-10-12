# Agent OS, prediction-market domain: Doc outlines (v0.1)

The trading layer of the system's doc skills: what this domain's own vision, README and rebuild prompt add to the general Domain outline, and the outlines and lengths of the docs of the two levels the domain defines below itself, the strategy and the trading agent. Read it together with the skills `vision-doc`, `readme-doc` and `rebuild-prompt-doc` and the knowledge base agent's "The same docs at every level" (all in `agents/system/.claude/`); a later trading domain copies it.

## The docs at each level
<!-- k: id=tr-doc-levels applies=[19.6.15],[19.6.2],[19.6.3],[19.6.4],[21.6.2],[21.6.3],[21.6.4],[46.2],[46.3],[46.4] sources=D-030,D-034,D-053,D-056 status=decided -->
General rule: see the knowledge base agent (The same docs at every level).
- The domain [19.6], every strategy [21.6] and every trading agent [46] has its own `docs/` with the same docs in the same format: a vision, a README and a rebuild prompt. Each one tells only its own story:
  - the domain's docs cover why this domain and how it makes money;
  - a strategy's docs cover its idea and how it is tested and improved;
  - a trading agent's docs cover what makes it different from its siblings.
- The domain reaches its strategies' docs through [19.6.1] `subagents.link/`, and each strategy reaches its trading agents' docs through [21.6.1].

## Vision
<!-- k: id=tr-doc-vision applies=[19.6.15],[19.6.3],[21.6.3],[46.3] sources=D-034,D-048,D-053,D-056 status=proposed -->
General rule and the System, Domain and App outlines: see the `vision-doc` skill (Outline, At other levels). Lengths: see Lengths below.
- Anything shared with the level above is not explained again: sum it up in a sentence or two ("Like every strategy here, it is tested on paper first and improved through variants that compete"), then describe only what is different.
- Style examples for this domain's docs, for the skill's "How to write it":
  - Lead with purpose, not machinery: "The system runs many small trading programs side by side and keeps the ones that make money" comes before anything about settings or folders.
  - Business rules as plain statements: "Only the owner can approve real money, one account at a time."
  - Examples are concrete and short: a real market, a real kind of source, what happens step by step, and how it ends.
  - Right, not too technical: "Small programs called workers collect information on a schedule, such as prices and news, and save it as simple files. Each trading agent is handed exactly the files its strategy needs, so it reads only what matters to it."

### The domain's vision
<!-- k: id=tr-doc-vision-domain applies=[19.6.15],[19.6.3] sources=D-034,D-048,D-056 status=proposed -->
- **Outline:** in short; why this domain; the concept here; how money is made, by the main families of strategies (the business logic); examples; where it stands and what comes next; its own principles, ideas and questions; going deeper (this domain's README).
- **The business logic:** how the domain turns ideas into money and decides what lives: where strategies come from, how a strategy becomes agents and variations, test mode and live mode, how results are compared and winners kept, when real money is allowed and who approves it, what may be traded, what limits apply, what costs count (AI, the server) and how losing agents are stopped. Each rule as a plain statement.
- **Examples:** two to four worked examples, each followed from start to end in a short paragraph or a few steps: for instance a prediction-market strategy from idea to its first approved live trade, trading on what a well-known YouTuber says, a risk agent telling every agent to sell. Real names of markets and sources, no file names.

### A strategy's vision
<!-- k: id=tr-doc-vision-strategy applies=[19.6.15],[21.6.3] sources=D-034,D-048,D-056 status=proposed -->
- **Outline:** the idea; why it should work; how it should behave, in plain words; its business rules (what it trades, its limits, when it goes live); one worked example; where it stands and what comes next; open questions; going deeper.

### A trading agent's vision
<!-- k: id=tr-doc-vision-agent applies=[19.6.15],[46.3] sources=D-034,D-048,D-053,D-056 status=proposed -->
- **Outline:** what makes it different from its siblings (model, settings, test or live); what it is testing; results so far; what comes next.

## README
<!-- k: id=tr-doc-readme applies=[19.6.15],[19.6.2],[21.6.2],[46.2] sources=D-034,D-036,D-048,D-053,D-056 status=proposed -->
General rule and the System, Domain and App outlines: see the `readme-doc` skill (Outline, At other levels). Lengths: see Lengths below.
- Each level's README describes only its own parts and sums up what it shares with the level above in a sentence or two ("Like every trading area here, it runs in test mode first and keeps its settings in one file").
- The inside of an agent stays out of every README here: what it trades and when is in the agent's own docs.

### The domain's README
<!-- k: id=tr-doc-readme-domain applies=[19.6.15],[19.6.2] sources=D-034,D-048,D-056 status=proposed -->
- **Outline:** in short; the domain at a glance; how it is laid out; its parts (its strategies, one short section each with the path to that strategy's README; the information it collects and shares; its settings and trading venues; its jobs; its tests and research); where each part's docs are; still open.
- The strategies, the trading agents and the trading dashboard (`apps/trading-ui/`, the domain's dashboard, empty for now) are described in this README, not in the system's.

### A strategy's README
<!-- k: id=tr-doc-readme-strategy applies=[19.6.15],[21.6.2] sources=D-034,D-048,D-056 status=proposed -->
- **Outline:** in short; the strategy at a glance; how it is laid out; its parts (its variations as a small table with name, what differs, model, mode and status, each with the path to that agent's README; the information it uses; how it is tested on past data; its jobs; its research); where each part's docs are; still open.

### A trading agent's README
<!-- k: id=tr-doc-readme-agent applies=[19.6.15],[46.2] sources=D-034,D-048,D-056 status=proposed -->
- **Outline:** what it is (its strategy, what makes it different, model, mode); what it holds; what it reads and what it produces; what it runs and how often; its tests; its docs. Its own logic is in its strategy doc [46.5], not here.

## Rebuild prompt
<!-- k: id=tr-doc-rebuild-prompt applies=[19.6.15],[19.6.4],[21.6.4],[46.4] sources=D-048,D-053,D-056 status=proposed -->
General rule: see the `rebuild-prompt-doc` skill (At other levels). Lengths: see Lengths below.
- The domain, every strategy and every trading agent has its own prompt, like its vision and README, and it covers only its own folder: it assumes the levels above exist, names what it takes from them, builds the rest and lists its children's prompts in build order (the domain lists its strategies' prompts, a strategy its trading agents'). Until a level's parts are designed, its prompt is only its How it works file.
- It holds no trading data, logs or results.
- "Your task" says what the agent never does: trade with real money.
- The acceptance checks include: nothing can trade live without the owner's approval.

## Lengths
<!-- k: id=tr-doc-lengths applies=[19.6.15],[21.6.2],[21.6.3],[21.6.4],[46.2],[46.3],[46.4] sources=D-034,D-048,D-053,D-056 status=proposed -->
General rule and the System, Domain and App lengths: see the Length section of each doc skill.

| Level | Vision | README | Rebuild prompt |
|---|---|---|---|
| Strategy | 400 to 800 words | 600 to 1,500 words | 1,000 to 2,500 words |
| Trading agent | 150 to 400 words | 200 to 600 words | 300 to 1,000 words |

## Changelog
- v0.1 (2026-10-07): created from the system's doc skills `vision-doc`, `readme-doc` and `rebuild-prompt-doc` and the knowledge base agent: the domain's own additions to the Domain outline, the strategy and trading agent outlines and their lengths moved here (D-056, D-058).
