# Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic

**Video URL:** https://youtu.be/TqC1qOfiVcQ

---

## Executive Summary

This 2-hour workshop by Thariq Shihipar from Anthropic provides a comprehensive deep-dive into the Claude Agent SDK, explaining why Anthropic built it on top of Claude Code and how to design effective agents. The workshop covers the "Anthropic way" of building agents using Unix primitives (bash and file system), the agent loop architecture (gather context → take action → verify work), and practical guidance on choosing between tools, bash, and code generation. Thariq emphasizes that agents should be "simple but not easy" — the codebase should be minimal but elegantly designed around what the model needs. The session includes a live coding demo building a Pokemon API agent, demonstrating how to prototype agents quickly using Claude Code before productionizing with the Agent SDK.

---

## Topics

### 1. Introduction & Workshop Overview
[00:00](https://www.youtube.com/watch?v=TqC1qOfiVcQ&t=0s)

- Workshop agenda: What is Claude Agent SDK, why use it, agent design, and live prototyping
- Interactive format with Q&A throughout
- Building agents is "an art or intuition" developed through practice

### 2. Evolution of AI Features: From Single LLM to Agents
[02:00](https://www.youtube.com/watch?v=TqC1qOfiVcQ&t=120s)

- Single LLM features → workflows → agents
- Claude Code as the canonical agent example
- Agents build their own context and decide their own trajectories autonomously
- We're at a "break point" where agent technology is ready for production use

### 3. Why Claude Agent SDK
[04:00](https://www.youtube.com/watch?v=TqC1qOfiVcQ&t=240s)

- Built on top of Claude Code due to internal learnings at Anthropic
- Components: models, tools, prompts, file system, skills, sub-agents, web search, compacting, hooks, memory
- Non-coding teams (finance, marketing, data science) started using Claude Code effectively
- SDK packages all these components together with best practices baked in

### 4. The Anthropic Way to Build Agents
[08:00](https://www.youtube.com/watch?v=TqC1qOfiVcQ&t=480s)

- Unix primitives (bash and file system) as core building blocks
- Agents build their own context
- Code generation for non-coding tasks (composing APIs, data analysis)
- Every agent runs in a container or locally with file system access
- Strong opinions: "Bash tool is the most powerful agent tool"

### 5. Security & Guardrails (Swiss Cheese Defense)
[13:00](https://www.youtube.com/watch?v=TqC1qOfiVcQ&t=780s)

- Multi-layered defense approach:
  - Model alignment layer
  - Harness layer (permissioning, prompting, bash parser)
  - Sandboxing layer (network, file system)
- "Lethal trifecta": execute code + change file system + exfiltrate data
- Sandbox providers: Cloudflare, Modal, E2B, Daytona

### 6. Bash Is All You Need
[15:32](https://www.youtube.com/watch?v=TqC1qOfiVcQ&t=932s)

- Bash as the "first code mode" / "first programmatic tool calling"
- Store tool results to files, generate scripts dynamically, compose functionality
- Use existing software (ffmpeg, LibreOffice) through bash
- Email agent example: Without bash = dump 100 emails into context; With bash = grep for prices, pipe results, store with line numbers, verify work

### 7. Workflows vs Agents
[20:36](https://www.youtube.com/watch?v=TqC1qOfiVcQ&t=1236s)

- Agents: natural language input, flexible action (like Claude Code)
- Workflows: defined inputs/outputs (like GitHub Actions)
- Both can be built with Agent SDK
- Structured outputs recently released for workflows
- Even "workflow-like" tasks benefit from agent capabilities (e.g., issue triaging needs to clone repos, spin up Docker)

### 8. The Agent Loop: Gather Context → Take Action → Verify
[22:00](https://www.youtube.com/watch?v=TqC1qOfiVcQ&t=1320s)

- **Gather context**: Finding relevant files/emails/data (often underthought)
- **Take action**: Using the right tools (code generation, bash are more flexible)
- **Verify work**: Critical for agent success; if you can verify, it's a great agent candidate
- Meta-learning: Read the transcripts over and over again to understand agent behavior

### 9. Tools vs Bash vs Code Generation
[25:00](https://www.youtube.com/watch?v=TqC1qOfiVcQ&t=1500s)

| Approach | Pros | Cons |
|----------|------|------|
| **Tools** | Structured, reliable, minimal errors | High context usage, not composable, no discoverability |
| **Bash** | Composable, static scripts, low context | Discovery latency, slightly lower call rates |
| **Code Generation** | Highly composable, dynamic scripts | Longest to execute, needs linting/compilation |

- Tools: atomic actions needing guarantees (write file, send email)
- Bash: composable actions (searching, linting, memory)
- Code Generation: highly dynamic logic, composing APIs, data analysis

### 10. Skills
[30:58](https://www.youtube.com/watch?v=TqC1qOfiVcQ&t=1858s)

- Skills = collections of files for progressive context disclosure
- Agent CDs into skill directory, reads instructions, writes scripts
- Example: DOCX skills, front-end design skill
- Skills vs CLAUDE.md: still evolving best practices
- Skills need bash tool and virtual file system (Agent SDK requirement)

### 11. When to Use the Agent SDK
[38:32](https://www.youtube.com/watch?v=TqC1qOfiVcQ&t=2312s)

- If building an agent, start with Agent SDK
- Bash + file system provides power and flexibility for any agent
- Trade-off with hosting complexity vs capabilities
- Analogy: Agent SDK is like React to jQuery — more boilerplate but more powerful

### 12. Designing Tools for Agents
[43:00](https://www.youtube.com/watch?v=TqC1qOfiVcQ&t=2580s)

- When to use tools vs bash vs codegen: no single best practice
- Database example: Give maximum access, add guardrails, provide feedback on errors
- Model learns from error feedback and adjusts behavior
- Custom bash scripts: add `-help` flags for progressive disclosure

### 13. Spreadsheet Agent Design Example
[50:44](https://www.youtube.com/watch?v=TqC1qOfiVcQ&t=3044s)

- Search strategies: CSV → grep → SQL (translate to familiar interface)
- Key insight: Convert data to interface model knows well (SQL)
- Pre-processing: add metadata, have agent annotate spreadsheet
- Action: Use existing tools (Google Sheets API, code generation for dynamic queries)
- Verification: Check outputs, lint generated code

### 14. Context Management
[01:15:39](https://www.youtube.com/watch?v=TqC1qOfiVcQ&t=4539s)

- Clear context frequently in Claude Code (state is in files, not conversation)
- For non-technical users: design UX around context (reset conversations, auto-compact)
- Store preferences/memory to file system
- Sub-agents preserve main agent's context window

### 15. Sub-Agents
[01:17:54](https://www.youtube.com/watch?v=TqC1qOfiVcQ&t=4674s)

- Sub-agents were made to protect main agent's context
- Can run multiple sub-agents in parallel (Agent SDK handles race conditions)
- Example: 3 sub-agents summarize 3 different sheets simultaneously
- Focus on domain problems, not systems engineering

### 16. Verification Strategies
[01:20:34](https://www.youtube.com/watch?v=TqC1qOfiVcQ&t=4834s)

- Two types: Deterministic rules vs sub-agent verification
- Deterministic: Fast, reliable (check file exists, character count, lint)
- Sub-agent: More flexible, higher cost (verify sense, appropriateness)
- Verify everywhere, not just at the end
- Give feedback on rule violations; model listens and adjusts

### 17. State Reversibility
[01:09:00](https://www.youtube.com/watch?v=TqC1qOfiVcQ&t=4140s)

- Code agents: more reversible (git revert, delete files)
- Computer use agents: less reversible (sent emails, deleted files)
- Reversibility determines how much autonomy to grant
- "Time travel" tools for agents (revert to previous state)

### 18. Prototyping with Claude Code
[01:23:26](https://www.youtube.com/watch?v=TqC1qOfiVcQ&t=5006s)

- Simple to get started: Claude Code + scripts + libraries + CLAUDE.md
- Build something that feels good with Claude Code first
- Get high conviction before productionizing
- Simple but not easy: minimal code, elegant design matching what model needs

### 19. Live Demo: Pokemon Agent
[01:26:00](https://www.youtube.com/watch?v=TqC1qOfiVcQ&t=5160s)

- PokeAPI as example of complex external API
- Two approaches shown:
  1. Traditional tools via Messages API (defined get_pokemon, get_species, etc.)
  2. Code generation via Claude Code (generates TypeScript SDK, writes scripts)
- Code generation approach: more flexible, handles more Pokemon, verifies via execution
- Used Bun for fast TypeScript prototyping (no compile step)

### 20. Productionizing Agents
[01:40:00](https://www.youtube.com/watch?v=TqC1qOfiVcQ&t=6000s)

- Agent SDK file can be ~50 lines
- File system = context engineering inputs
- Two deployment options:
  1. Local apps (might be making a comeback with AI)
  2. Hosted containers
- Process: Test with Claude Code → Write minimal Agent SDK file → Deploy

---

## Key Takeaways

1. **Bash is the most powerful agent tool** — it enables composability, dynamic script generation, and leveraging existing software

2. **Design agents around the model** — translate your domain into interfaces the model knows well (e.g., convert spreadsheets to SQL)

3. **Verification is critical** — if you can verify an agent's work (like code with linting), it's a great candidate for automation

4. **Progressive context disclosure** — don't load everything upfront; let the agent discover what it needs

5. **Read the transcripts** — the meta-learning for agent design is observing agent behavior and iterating

6. **Simple but not easy** — agent code should be minimal and elegant, not complex

7. **Sub-agents for context management** — spin off tasks to preserve main agent's context window

8. **Prototype with Claude Code first** — skip to domain-specific problems, get high conviction, then productionize
