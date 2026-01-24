# Summary: Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic

**Video URL:** https://youtu.be/TqC1qOfiVcQ?si=Fz9YUae0Ux7QirHZ

---

## Overview

In this 2-hour workshop, Thariq Shihipar from Anthropic provides a comprehensive introduction to the Claude Agent SDK, covering agent design principles, implementation strategies, and live coding demonstrations. The session emphasizes practical approaches to building agents using code generation and file system-based context management.

---

## Key Topics

### [00:00 - 15:00] Introduction and Agent Evolution

**[00:23](https://youtu.be/TqC1qOfiVcQ?si=Fz9YUae0Ux7QirHZ&t=23s)** - Workshop begins with agenda overview

**[02:15](https://youtu.be/TqC1qOfiVcQ?si=Fz9YUae0Ux7QirHZ&t=135s)** - Evolution of AI features:
- **Single LLM features**: Simple categorization tasks
- **Workflows**: Structured tasks like email labeling, RAG-based code completion
- **Agents**: Autonomous systems that build their own context and decide trajectories (Claude Code as the canonical example)

**[03:50](https://youtu.be/TqC1qOfiVcQ?si=Fz9YUae0Ux7QirHZ&t=230s)** - Claude Code: The first true agent working for 10-30+ minutes autonomously

**[04:15](https://youtu.be/TqC1qOfiVcQ?si=Fz9YUae0Ux7QirHZ&t=255s)** - Why the Claude Agent SDK was built:
- Anthropic kept rebuilding the same components
- Core components: Models, Tools, Prompts, File System, and the Agent Loop

**[12:43](https://youtu.be/TqC1qOfiVcQ?si=Fz9YUae0Ux7QirHZ&t=763s)** - Security: "Swiss cheese defense"
- Model layer: Alignment and reward hacking prevention
- Harness layer: Bash parser, permissions, and prompting
- Sandboxing: Network and file system operations restricted

### [15:00 - 35:00] Agent Design Principles

**[17:00](https://youtu.be/TqC1qOfiVcQ?si=Fz9YUae0Ux7QirHZ&t=1020s)** - Agent loop components:
1. **Gathering context** - How agents discover information
2. **Taking action** - How agents make changes
3. **Verifying work** - How agents check their results

**[19:30](https://youtu.be/TqC1qOfiVcQ?si=Fz9YUae0Ux7QirHZ&t=1170s)** - Philosophy: "Prefer code generation over custom tools"
- Code generation for non-coding tasks (composing APIs, fetching weather, etc.)
- Agents can write scripts to solve problems dynamically

**[29:45](https://youtu.be/TqC1qOfiVcQ?si=Fz9YUae0Ux7QirHZ&t=1785s)** - Context management best practice:
- Offload tool results to file system
- Return file paths instead of large outputs
- Prevents context explosion

**[31:00](https://youtu.be/TqC1qOfiVcQ?si=Fz9YUae0Ux7QirHZ&t=1860s)** - Skills explained:
- Progressive context disclosure
- Collections of files agents can read on-demand
- Example: DOCX skills, front-end design skill
- Allows expertise to be loaded when needed

**[32:55](https://youtu.be/TqC1qOfiVcQ?si=Fz9YUae0Ux7QirHZ&t=1975s)** - Skills vs CLAUDE.md:
- Both are new concepts (Skills released 2 weeks ago)
- Skills are for repeatable instructions requiring expertise
- Best practices still evolving

### [35:00 - 60:00] Context Engineering and Spreadsheet Example

**[40:00](https://youtu.be/TqC1qOfiVcQ?si=Fz9YUae0Ux7QirHZ&t=2400s)** - Context engineering is the key challenge
- Gathering context is extremely creative
- Multiple iteration approaches needed

**[59:00](https://youtu.be/TqC1qOfiVcQ?si=Fz9YUae0Ux7QirHZ&t=3540s)** - Spreadsheet agent design approaches:
- **Spreadsheet syntax**: Use B3:B5 range notation (familiar to agents)
- **SQL queries**: Agents know SQL well
- **XML queries**: XLSX files are XML under the hood
- Try multiple approaches to see what the agent prefers

**[01:00:44](https://youtu.be/TqC1qOfiVcQ?si=Fz9YUae0Ux7QirHZ&t=3644s)** - "Gathering context is really really creative"
- If you've only tried one iteration, it's probably not enough
- Make problems as "in-distribution" as possible for the model

### [01:02:00 - 01:26:00] Verification and Action Patterns

**[01:03:10](https://youtu.be/TqC1qOfiVcQ?si=Fz9YUae0Ux7QirHZ&t=3790s)** - Verification strategies:
- Check for null pointers
- Similar APIs for gathering context and taking action
- Consistency between read and write operations

**[01:25:39](https://youtu.be/TqC1qOfiVcQ?si=Fz9YUae0Ux7QirHZ&t=5139s)** - Agent design philosophy:
- "Simple but simple is not easy"
- Code should not be huge or extremely complex, but elegant
- Make it what the model wants
- Example: Turn spreadsheets into SQL queries

### [01:26:00 - 01:50:00] Live Coding: Pokemon Agent

**[01:26:02](https://youtu.be/TqC1qOfiVcQ?si=Fz9YUae0Ux7QirHZ&t=5162s)** - Pokemon agent demonstration begins
- Goal: Build agent to chat about Pokemon and create competitive teams
- Uses PokeAPI (complex API with thousands of Pokemon)

**[01:27:20](https://youtu.be/TqC1qOfiVcQ?si=Fz9YUae0Ux7QirHZ&t=5240s)** - Implementation approach:
- Generated TypeScript SDK from PokeAPI documentation
- Created CLAUDE.md with instructions
- Agent writes scripts in examples directory and executes them

**[01:29:00](https://youtu.be/TqC1qOfiVcQ?si=Fz9YUae0Ux7QirHZ&t=5340s)** - Generated TypeScript interface:
- Pokemon API with methods: getByName, listPokemon, getAllPokemon, getSpecies, getAbilities
- All generated from a simple prompt

**[01:30:00](https://youtu.be/TqC1qOfiVcQ?si=Fz9YUae0Ux7QirHZ&t=5400s)** - Two approaches shown:
1. **Code generation approach**: Agent generates and executes TypeScript scripts
2. **Tool-based approach**: Using messages completion API with explicit tools

### [01:50:00 - 01:52:00] Q&A and Closing

**[01:50:36](https://youtu.be/TqC1qOfiVcQ?si=Fz9YUae0Ux7QirHZ&t=6636s)** - Large codebase question:
- For 50M+ line codebases, grep tool limitations
- Use good CLAUDE.md files
- Start in correct directory
- Add verification steps, hooks, and links
- Anthropic dogfoods Claude Code (no custom semantic search)

**[01:51:00](https://youtu.be/TqC1qOfiVcQ?si=Fz9YUae0Ux7QirHZ&t=6660s)** - Future of agent tooling:
- "Generally, yes" - things will evolve rapidly
- Semantic search has trade-offs (more brittle, requires indexing)
- Model trained on grep, not custom semantic search

**[01:52:06](https://youtu.be/TqC1qOfiVcQ?si=Fz9YUae0Ux7QirHZ&t=6726s)** - Workshop concludes

---

## Key Takeaways

1. **Prefer Code Generation**: Agents work best when generating and executing code rather than using many custom tools
2. **File System for Context**: Use the file system to manage context and prevent context window explosion
3. **Progressive Disclosure**: Skills enable loading expertise on-demand through the file system
4. **Iterate on Context Gathering**: Context engineering is highly creative - try multiple approaches
5. **Make it In-Distribution**: Frame problems using patterns the model already knows (SQL, spreadsheet notation, XML)
6. **Swiss Cheese Security**: Layer defenses at model, harness, and sandboxing levels
7. **Simple but Elegant**: Agent code should be elegant rather than complex
8. **Verification Matters**: Build in ways for agents to check their own work

---

## Resources Mentioned

- Claude Agent SDK (built on Claude Code)
- PokeAPI - Example of complex API for demonstration
- Anthropic's reward hacking paper
- GitHub repository with workshop code (personal GitHub of presenter)

---

## Practical Applications

- GitHub automations (issue triaging)
- Slack automations
- API composition and integration
- Spreadsheet manipulation
- Complex research tasks requiring multiple tool calls
- Building domain-specific agents with Skills
