# Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic

**Video URL:** https://youtu.be/TqC1qOfiVcQ?si=Fz9YUae0Ux7QirHZ  
**Channel:** AI Engineer  
**Speaker:** Thariq Shihipar, Developer Relations Lead at Anthropic

## Executive Summary

This 2-hour workshop provides a comprehensive deep-dive into the Claude Agent SDK, built on top of Claude Code. Thariq explains Anthropic's opinionated approach to agent building: using bash and code generation as the primary tools rather than creating hundreds of specialized tools. The workshop covers the agent loop pattern (gather context → take action → verify work), context engineering strategies, sub-agents for managing complexity, and practical prototyping with a Pokemon agent example. Key philosophy: agents should be simple but elegant, with the harness handling low-level complexity so developers can focus on domain-specific problems.

---

## Topics

### [Introduction & Workshop Agenda](https://www.youtube.com/watch?v=TqC1qOfiVcQ&t=0s)
- Workshop overview: Understanding the Claude Agent SDK and why Anthropic built it
- Focus on giving participants a unique perspective beyond standard documentation
- Emphasis on coding agents, not just chatbots

### [Evolution of AI Features: Single LLM → Workflows → Agents](https://www.youtube.com/watch?v=TqC1qOfiVcQ&t=120s)
- **Single LLM Call**: Simple prompt-response, like ChatGPT conversations
- **Workflows**: Chaining multiple LLM calls in a predetermined orchestration
- **Agents**: LLM decides dynamically what tools to use and in what order
- Key insight: Agents should be trusted to make decisions like human employees

### [Why Claude Agent SDK is Built on Claude Code](https://www.youtube.com/watch?v=TqC1qOfiVcQ&t=240s)
- Claude Code serves as the foundation and sandbox for experimentation
- Anthropic ships features fast (6-month journey from project to product)
- SDK extracts learnings from Claude Code into a reusable harness
- Philosophy: Let the agent do its best work without micromanagement

### [Anthropic's Opinionated Approach: "Bash is All You Need"](https://www.youtube.com/watch?v=TqC1qOfiVcQ&t=480s)
- Only 3 core tools needed: Read, Write, Execute (Bash)
- Bash provides thousands of tools with zero maintenance
- Code generation works for non-coding tasks (spreadsheets, data analysis)
- Models are trained on code, making them highly capable at code generation

### [Security: Swiss Cheese Defense Model](https://www.youtube.com/watch?v=TqC1qOfiVcQ&t=720s)
- Multiple overlapping security layers like holes in Swiss cheese
- No single security measure is perfect; layers provide protection
- Human-in-the-loop permission system for dangerous operations
- Container sandboxing and automatic permission denials

### [Bash Tool Power & Composability](https://www.youtube.com/watch?v=TqC1qOfiVcQ&t=900s)
- Example: Slack integration with 200+ API endpoints simplified to bash commands
- File system as memory: Agents can persist state across conversations
- Composability: grep + head + tail can accomplish complex searches
- Real-world example: Finding lines in code by combining bash primitives

### [Agent Loop Design: Gather → Act → Verify](https://www.youtube.com/watch?v=TqC1qOfiVcQ&t=1320s)
- **Gather Context**: Read files, search code, understand the problem
- **Take Action**: Write code, execute commands, make changes
- **Verify Work**: Run tests, check linters, validate outputs
- Loop continues until task is complete; avoid premature stopping

### [Tools vs Bash vs Code Generation](https://www.youtube.com/watch?v=TqC1qOfiVcQ&t=1500s)
- **Tools**: Best for structured data retrieval; 15-20 max recommended
- **Bash**: Best for composable operations; access to thousands of commands
- **Code Generation**: Best for complex algorithms and data processing
- Decision framework: Tools for retrieval, bash for operations, codegen for computation

### [Agentic Search & Progressive Context Disclosure](https://www.youtube.com/watch?v=TqC1qOfiVcQ&t=1620s)
- Traditional RAG (Retrieval Augmented Generation) is limited
- Agentic search: Model actively searches and refines queries
- Progressive disclosure: Start with summaries, drill down as needed
- File system structure can guide agent navigation

### [Skills: Teaching Agents Domain Knowledge](https://www.youtube.com/watch?v=TqC1qOfiVcQ&t=1860s)
- Skills are markdown files that teach agents specific capabilities
- Skills automatically loaded based on trigger conditions
- Example: Teaching git workflow or deployment processes
- Skills enable "good code" by preserving proven patterns

### [When to Use the Claude Agent SDK](https://www.youtube.com/watch?v=TqC1qOfiVcQ&t=2280s)
- Best for: Agentic workflows, code generation tasks, complex tool usage
- Not needed for: Simple chatbots, single-turn completions
- Trade-off: More power but requires understanding agent patterns
- Value proposition: Skip low-level engineering, focus on domain problems

### [Designing Agents Example: Spreadsheet Agent](https://www.youtube.com/watch?v=TqC1qOfiVcQ&t=3000s)
- Convert spreadsheets to SQLite for powerful querying
- Natural language → SQL query → Execute → Return results
- Verification: Check SQL before execution, validate outputs
- Reversibility: Maintain ability to undo operations

### [Sub-Agents for Context Management](https://www.youtube.com/watch?v=TqC1qOfiVcQ&t=3960s)
- Sub-agents preserve main agent's context window
- Main agent delegates read-heavy tasks to sub-agents
- Sub-agents return summaries, not raw data
- Parallel sub-agents for handling large datasets

### [State Management & Memory](https://www.youtube.com/watch?v=TqC1qOfiVcQ&t=4200s)
- File system as persistent memory across sessions
- JSON files for structured state (user preferences, progress)
- Compact/summarize context when approaching limits
- User preferences can be stored and recalled

### [Verification Strategies](https://www.youtube.com/watch?v=TqC1qOfiVcQ&t=4860s)
- Verification should happen everywhere, not just at the end
- Use hooks for deterministic verification
- Give feedback on errors; models respond well to error messages
- Rules and heuristics catch common mistakes

### [Live Demo: Pokemon Agent Prototyping](https://www.youtube.com/watch?v=TqC1qOfiVcQ&t=5160s)
- Building a Pokemon information agent using PokeAPI
- Generated TypeScript SDK from API documentation
- CLAUDE.md file as the agent's instruction set
- Code generation for complex queries across 200+ Pokemon

### [Tools-Based vs Code-Generation Agents](https://www.youtube.com/watch?v=TqC1qOfiVcQ&t=5460s)
- Comparison: Pre-defined tools vs dynamic code generation
- Tools version: Limited to defined functions
- Codegen version: Can write arbitrary scripts
- Trade-off: Control vs flexibility

### [Productionizing Agents with Sandboxes](https://www.youtube.com/watch?v=TqC1qOfiVcQ&t=5880s)
- Local apps may return for AI (Claude Code runs locally)
- Sandbox providers (Cloudflare) for hosted agents
- Dev server pattern: Live-refreshing UI in sandbox
- Sandbox per user for multi-tenant applications

### [Hooks for Deterministic Control](https://www.youtube.com/watch?v=TqC1qOfiVcQ&t=6420s)
- Hooks fire on events (before/after tool calls)
- Use cases: Validation, context injection, verification
- Example: Insert user changes after every tool call
- Deterministic guardrails within agentic flexibility

### [Handling Large Codebases](https://www.youtube.com/watch?v=TqC1qOfiVcQ&t=6660s)
- Semantic search has trade-offs (brittleness, indexing overhead)
- Grep is model-native; semantic search is bespoke
- Good CLAUDE.md files help navigate large repos
- Start in the right directory, use verification hooks

### [Monetization & Business Considerations](https://www.youtube.com/watch?v=TqC1qOfiVcQ&t=6720s)
- Agents are currently expensive; models still maturing
- Charge fewer people more money for hard problems
- Subscription vs usage-based pricing depends on use case
- Design monetization strategy upfront

---

## Key Takeaways

1. **Simple ≠ Easy**: Your agent code should be simple, but achieving that simplicity requires thoughtful design
2. **Bash is incredibly powerful**: Access thousands of Unix tools with zero maintenance overhead
3. **Code generation is universal**: Even non-coding tasks benefit from code generation approaches
4. **Context engineering is critical**: How you structure information determines agent success
5. **Verification everywhere**: Don't just verify at the end; build verification into every step
6. **Let agents be intelligent**: Trust them to make decisions rather than over-constraining
7. **File system as memory**: Use files for persistent state across conversations
8. **Sub-agents for scale**: Delegate read-heavy tasks to preserve main agent context
9. **Prototype in Claude Code**: Use Claude Code locally before productionizing with SDK
10. **Focus on domain problems**: The SDK handles infrastructure so you can solve real problems

---

## Resources

- **GitHub Repo**: thariq212 (speaker's personal GitHub)
- **Twitter**: @TRQ212
- **Documentation**: Claude Agent SDK docs on Anthropic website
- **Related Talk**: AI Engineer World's Fair presentation on Claude Code
