# Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic

**Video URL:** https://youtu.be/TqC1qOfiVcQ

---

## Executive Summary

Thariq Shihipar from Anthropic presents a comprehensive workshop on the Claude Agent SDK, explaining the evolution from single LLM features to workflows and now fully autonomous agents. The SDK is built on top of Claude Code and packages battle-tested components including tools, prompts, file systems, bash capabilities, and best practices learned from production deployments. The workshop emphasizes the "Anthropic way" of building agents using Unix primitives (bash and file system), code generation for non-coding tasks, and container-based architecture. Thariq demonstrates live prototyping of a Pokemon team-building agent to showcase practical agent development, debugging strategies, and the power of letting agents build their own context through scripting rather than relying solely on custom tools.

---

## Topics and Key Points

### [Introduction and Workshop Agenda](https://www.youtube.com/watch?v=TqC1qOfiVcQ&t=23s)
*Starting at 00:23*

- Workshop overview covering: what the Claude Agent SDK is, why use it, agent design principles, and live coding demonstrations
- Interactive format with collaborative questions throughout
- Focus on practical, non-canned demonstrations showing real agent development process

**Key Points:**
- Two-hour collaborative workshop format
- Emphasis on practical prototyping and thinking through problems live
- Building agent loops is described as "an art or intuition"

---

### [Evolution of AI Features: From Single LLM to Agents](https://www.youtube.com/watch?v=TqC1qOfiVcQ&t=132s)
*Starting at 02:12*

- **Single LLM features**: Simple categorization and single-turn responses (GPT-3 era)
- **Workflows**: Multi-step processes like email labeling, RAG-based code indexing, and structured code generation
- **Agents**: Autonomous systems that build their own context, decide trajectories, and work independently for extended periods (10-30+ minutes)

**Key Points:**
- Claude Code represents the first true agent - first time AI worked autonomously for extended periods
- Agents don't have restricted actions; they take a wide variety of actions based on text interaction
- Current era is the "break point" where building functional agents becomes practical

---

### [What is the Claude Agent SDK?](https://www.youtube.com/watch?v=TqC1qOfiVcQ&t=241s)
*Starting at 04:01*

Built on top of Claude Code, the SDK solves the problem of repeatedly rebuilding the same components at Anthropic.

**Core Components:**
- **Models**: Foundation LLMs
- **Tools**: Custom tools, file system interactions, bash capabilities
- **Agent loop**: Execution framework
- **Prompts**: Core agent prompts and system instructions
- **File system**: Context engineering through files and scripts
- **Skills**: Recently rolled out capability system
- **Advanced features**: Sub-agents, web search, compacting, hooks, memory

**Key Insight:**
- Context is not just prompts - it's also the tools, files, and scripts available to the agent
- All these components are packaged together for immediate use

---

### [Who's Building with the SDK](https://www.youtube.com/watch?v=TqC1qOfiVcQ&t=382s)
*Starting at 06:22*

**Popular Use Cases:**
- Software agents: reliability, security, bug triaging and finding
- Site and dashboard builders (extremely popular)
- Office agents: document processing, automation
- Legal, finance, and healthcare applications

**Why it Works:**
- People were already using Claude Code for non-coding tasks
- Finance, data science, marketing teams all found it useful
- Anthropic kept coming back to the same architecture for non-coding agents

---

### [The Anthropic Way of Building Agents](https://www.youtube.com/watch?v=TqC1qOfiVcQ&t=508s)
*Starting at 08:28*

**Core Opinions:**
1. **Unix primitives** (bash and file system) are fundamental
2. **Bash tool is the most powerful agent tool**
3. **Agents build their own context** - don't over-constrain
4. **Code generation for non-coding tasks** - use scripting to compose APIs, fetch data, analyze information
5. **Every agent has a container or is hosted locally** - needs file system and bash access

**Rationale:**
- Strong opinions based on scale and production learnings from Claude Code
- Best practices baked in (tool use errors, compacting, etc.)
- Discoveries at scale that individual developers would struggle to find

---

### [Code Generation for Non-Coding Tasks](https://www.youtube.com/watch?v=TqC1qOfiVcQ&t=625s)
*Starting at 10:25*

**Example: Weather and Wardrobe Recommendation**
- Agent writes script to fetch weather API
- Dynamically gets location from IP address
- Calls sub-agent for recommendations
- Potentially integrates with wardrobe API

**High-Level Approach:**
- Think of it as "composing APIs"
- Writing reusable scripts for repeated tasks
- Letting agents create their own tools through code

---

### [Workflows vs Agents](https://www.youtube.com/watch?v=TqC1qOfiVcQ&t=707s)
*Starting at 11:47*

**When to Use Workflows:**
- Deterministic, repetitive business processes
- Same steps every time
- Predictable input/output

**When to Use Agents:**
- Need flexibility and autonomy
- Variable problem-solving required
- Building context dynamically

**Key Point:**
- Can use Cloud Agent SDK for both workflows and agents
- Start with agent, identify patterns, then lock down as workflow if needed

---

### [Prototyping Strategy: Use Claude Code First](https://www.youtube.com/watch?v=TqC1qOfiVcQ&t=829s)
*Starting at 13:49*

**Recommended Development Process:**
1. Use Claude Code to prototype your agent
2. Test with real data and scenarios
3. Once working, extract the key components
4. Document in Claude.md for production agent
5. Create helper scripts from prototyping session
6. Write agent.ts to orchestrate

**Benefits:**
- Claude Code is itself built on the Agent SDK
- Fast iteration without writing boilerplate
- Discover what context and tools are actually needed
- Natural way to find the right agent architecture

---

### [Live Demo: Pokemon Team Building Agent (Part 1)](https://www.youtube.com/watch?v=TqC1qOfiVcQ&t=1080s)
*Starting at 18:00*

**Project Setup:**
- Using Smogon competitive Pokemon data (50MB+ text files)
- Goal: Build agent to recommend team compositions
- Starting point: Large text file with Pokemon stats and strategies
- Approach: Let agent explore and figure out structure

**Initial Challenges:**
- Raw text data needs parsing
- Agent must discover data structure
- Finding relevant Pokemon for team building
- Balancing multiple Pokemon stats and types

---

### [Agent Development Process and Debugging](https://www.youtube.com/watch?v=TqC1qOfiVcQ&t=1680s)
*Starting at 28:00*

**Debugging Strategies:**
- Review tool calls and outputs
- Check what files agent created
- Examine scripts the agent wrote
- Iterate on Claude.md instructions when agent goes off track

**Common Patterns:**
- Agents naturally create helper scripts
- They build context through exploration
- Sometimes need guidance to use correct APIs
- Hooks can enforce certain behaviors (e.g., "always write a script")

---

### [Live Demo: Pokemon Agent (Part 2)](https://www.youtube.com/watch?v=TqC1qOfiVcQ&t=3147s)
*Starting at 52:27*

**Agent's Approach:**
- Searched for Venusaur and related Pokemon
- Found teammates and counters automatically
- Analyzed relationships between Pokemon
- Generated scripts to process and recommend teams

**Key Observations:**
- Agent built its own indexing through search
- Created analysis tools on the fly
- Discovered team synergies from text data
- Showed value of letting agents build context vs. pre-processing everything

---

### [Hooks for Deterministic Verification](https://www.youtube.com/watch?v=TqC1qOfiVcQ&t=6420s)
*Starting at 01:47:00*

**What are Hooks:**
- Events fired during agent execution
- Register callbacks in Agent SDK
- Enable deterministic verification and context insertion

**Use Cases:**
- Verify spreadsheet after each operation
- Insert live user changes into agent context
- Enforce "must read before write" rules
- Check that agent used required scripts
- Provide feedback when agent skips steps

**Example:**
- If agent returns response without writing script, hook provides feedback: "Please make sure you write a script"
- Similar to Claude Code's built-in rules

---

### [Container and Sandbox Architecture](https://www.youtube.com/watch?v=TqC1qOfiVcQ&t=6060s)
*Starting at 01:41:00*

**Deployment Patterns:**
- Each agent runs in its own container or locally
- Services like Cloudflare, E2B, Modal make deployment simple
- Example: `sandbox.start()` then `bun agent.ts`

**Advanced Pattern for Custom UIs:**
- Run dev server in sandbox (e.g., Bun or Node)
- Expose port from container
- Agent edits code that live-refreshes
- User interacts with dynamically generated website
- Powers many site builders like Lovable

**Benefits:**
- Per-user sandboxes enable customization
- Agent can adapt UI in real-time
- Isolated execution environment

---

### [Large Codebase Strategies](https://www.youtube.com/watch?v=TqC1qOfiVcQ&t=6274s)
*Starting at 01:50:34*

**Question:** How to handle 50M+ line codebases where grep doesn't scale?

**Recommendations:**
- **Trade-offs of semantic search**: More brittle, requires indexing, model not specifically trained for it
- **What works well**: Good Claude.md files, start in right directory, verification hooks
- **Anthropic's approach**: Dogfood Claude Code - no custom semantic search
- Focus on good context engineering rather than complex tooling

**Key Point:**
- Grep is trained into the model's behavior
- Custom semantic search may not work as well as expected
- Better to use native tools and good prompting

---

### [Monetization and Cost Considerations](https://www.youtube.com/watch?v=TqC1qOfiVcQ&t=6319s)
*Starting at 01:45:19*

**Current State:**
- Agents are relatively expensive right now
- Models are just becoming capable enough for agentic behavior
- Focus on most intelligent models rather than cheapest

**Pricing Strategies:**
- **Subscription with rate limits**: Works for high-usage products like Claude Code
- **Usage-based pricing**: Better for occasional-use agents
- **Hybrid approach**: Base subscription + usage overages

**Key Advice:**
- Solve problems people want to pay for first
- Find hard use cases worth higher prices
- Better to charge fewer people more for real value
- Design monetization upfront - hard to walk back promises

---

### [Q&A Highlights](https://www.youtube.com/watch?v=TqC1qOfiVcQ&t=6520s)
*Starting at 01:48:40*

**On Transferring Working Prototypes:**
- Use Claude.md to document approach
- Save helper scripts from prototyping
- Create agent.ts for production orchestration
- Don't rewrite everything - extract what works

**On Agents "Lying" About Using Scripts:**
- Agent SDK retries twice by default
- Use hooks to enforce script usage
- Add deterministic checks for required steps
- Sometimes need coercion through better prompts

**On Semantic Search:**
- Will likely be obsolete soon (general AI advancement pattern)
- Current trade-off: brittleness vs. simple grep/tools
- Model trained on grep, not on semantic search results

---

## Additional Resources

**Speaker:** Thariq Shihipar ([@TRQ212 on Twitter](https://twitter.com/TRQ212))
- Tweets frequently about Agent SDK
- Code examples will be shared on GitHub
- Active in the community

**Key Takeaways:**
1. Start prototyping with Claude Code before writing SDK code
2. Embrace Unix primitives (bash + file system) as core tools
3. Let agents build their own context through scripting
4. Use hooks for deterministic verification
5. Think about monetization and use cases upfront
6. Container/sandbox per user enables powerful customization
7. Code generation works for non-coding tasks through API composition

