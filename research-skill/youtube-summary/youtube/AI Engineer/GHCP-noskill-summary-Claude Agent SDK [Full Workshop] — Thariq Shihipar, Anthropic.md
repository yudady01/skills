# Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic

## Video Information
- **Speaker**: Thariq Shihipar, Anthropic
- **Event**: AI Engineer Workshop
- **Duration**: ~1 hour 52 minutes
- **Twitter**: @TRQ212

## Summary

This workshop by Thariq Shihipar from Anthropic provides a comprehensive deep-dive into the Claude Agent SDK, covering agent design principles, the power of bash tools, skills, prototyping best practices, and productionization strategies. The talk emphasizes that building effective agents requires creative thinking about context engineering and verification rather than complex code.

## Key Concepts

### 1. Agent Design Philosophy
- **Simple but not easy**: Agent code should be simple and elegant, but requires thoughtful design
- **File system as context engineering**: Use the file system to store and manage context rather than keeping everything in memory
- **Progressive context disclosure**: Let agents discover information as needed rather than front-loading everything
- **Models are "grown, not designed"**: Understanding model capabilities requires experimentation and iteration

### 2. "Bash is All You Need"
Thariq's core thesis is that the bash tool is transformative for agents:

- **First programmatic tool calling**: Bash was essentially the first "code mode" - allowing agents to compose functionality dynamically
- **What makes Claude Code good**: Instead of having separate search, lint, and execute tools, Claude Code uses grep, package managers, and bash generically
- **Capabilities**:
  - Store tool call results to files
  - Dynamically generate and execute scripts
  - Compose functionality (tail, grep, etc.)
  - Use existing software (ffmpeg, LibreOffice)
  - Memory management through the file system

### 3. Agent Loop Structure
```
User Input → Gather Context → Take Action → Verify Work → Output
                ↑__________________________________|
```

- **Gather Context**: Use agentic search interfaces (SQL queries, grep, XML search, range strings like "B3:B5")
- **Take Action**: Execute operations using familiar interfaces the model knows well
- **Verify Work**: Preferably deterministic (null checks, linting, compile errors), can use sub-agents for complex verification

### 4. Sub-Agents
- **Purpose**: Manage context pollution and perform focused tasks
- **Use cases**: Search sub-agents, verification sub-agents, parallel processing
- **Key benefit**: Avoid context window pollution by having sub-agents return only final results
- **Claude Code excels**: Best experience for sub-agents with bash, handles race conditions and parallel execution well

### 5. Skills
- Collections of files that agents can `cd` into and read
- Good for **progressive context disclosure**
- Best for **repeatable instructions requiring expertise** (e.g., front-end design skill)
- Difference from Claude.md: Skills are loaded on-demand, Claude.md is always available
- **Plugin marketplace**: Available via `/plugins` in Claude Code

### 6. Hooks
- Fire as events during agent execution
- Use cases:
  - Deterministic verification (check spreadsheet state after each operation)
  - Insert live context changes (user modifications while agent is working)
  - Enforce rules (e.g., "don't write to a file you haven't read")

### 7. Security Best Practices
- **Network sandbox**: Critical for preventing data exfiltration
- **Container isolation**: Use sandbox providers (Cloudflare, Modal, E2B, Daytona)
- **Permission systems**: Deny-by-default for dangerous operations
- **Role-based access**: Create scoped API keys for agents
- **Guard rails**: Limit database write access, insert validation rules

## Prototyping Workflow

### Step 1: Start with Claude Code
```
1. Give Claude Code your APIs/libraries
2. Create a claude.md with context about your domain
3. Chat with it to test queries
4. Iterate on the prompt until it works well
```

### Step 2: Build the Agent File
- Agent file should be ~50 lines of mostly boilerplate
- The real work is in context engineering (file system, cloud.md, skills)
- Use the Agent SDK's primitives (bash tool, file system, sub-agents)

### Step 3: Productionize
**Option A: Local App**
- Ship as an installable app that runs locally
- Like Claude Code - works on user's computer

**Option B: Hosted Sandbox**
- Use sandbox providers (Cloudflare, Modal, E2B)
- Simple integration: `sandbox.start()` then `bun agent.ts`
- Can expose dev server for custom UI per user

## Design Patterns

### Agentic Search Interface Design
When building search capabilities, consider multiple approaches:
1. **SQL queries**: Translate data to SQL format (SQLite can query CSVs directly)
2. **XML search**: Structured query format (XLSX files are XML internally)
3. **Range strings**: Familiar spreadsheet format like "B3:B5"
4. **Grep/AWK**: For text-based data
5. **Add metadata**: Pre-process data with annotations for better search

### Context Management
- Clear context frequently rather than compacting
- State lives in files (git diff shows changes)
- Sub-agents prevent context pollution
- Don't need huge context windows - need good context management UX

### Verification Strategies
1. **Rule-based (preferred)**: Null checks, lint, compile, type checking
2. **Deterministic hooks**: Check state after each operation
3. **Sub-agent verification**: For complex or adversarial checking
4. **Checkpoint/rollback**: Enable time-travel for reversible state

## Practical Advice

### Tool vs Bash vs Codegen Decision
- **Use tools when**: Need strong guarantees, structured input/output, security constraints
- **Use bash/codegen when**: Dynamic queries, iterative refinement needed, model benefits from seeing errors and fixing them
- **General rule**: Give agents maximum access with guard rails, not minimum access

### State Reversibility
- **Good for agents**: Code (git), files (backups), structured data
- **Hard for agents**: Computer use, complex state machines, irreversible actions
- Consider: Can you implement checkpoints? Time-travel tools?

### Monetization
- Consider pricing upfront - hard to change later
- Options: Subscription, usage-based, or hybrid (rate limits + overage)
- Focus on problems people will pay for before optimizing costs

## Code Example: Pokemon Agent

Thariq demonstrated building a Pokemon agent:

**Components**:
1. TypeScript SDK generated from PokeAPI
2. Claude.md explaining the SDK modules and usage
3. Example scripts in `/examples` directory
4. Agent file (~50 lines) running queries

**Two approaches shown**:
1. **Tool-based**: Define specific tools (getPokemon, getMove, etc.) with the standard API
2. **Codegen-based**: Let agent write and execute scripts using the SDK

**Key insight**: The codegen approach was more flexible, handling complex queries like "find all Gen 2 water Pokemon" by writing scripts that iterate through data.

## Quotes

> "Bash is what makes Claude Code so good."

> "Simple is not the same as easy. Your agent should be simple, but simple requires elegant design."

> "We can write code 10 times faster now. We should throw out code 10 times faster as well."

> "Models are grown, not designed. We're understanding their capabilities."

> "If you're a startup, being able to rapidly iterate on agent capabilities is your largest advantage over competitors with 6-month incubation cycles."

## Resources
- **GitHub**: @thariq - Pokemon agent code available
- **Twitter**: @TRQ212
- **Claude Agent SDK docs**: Hooks, sub-agents, file system patterns
- **Sandbox providers**: Cloudflare Workers, Modal, E2B, Daytona

## Timestamps
- 00:00 - Introduction & Agent Design Principles
- 15:00 - Security & Sandboxing
- 15:30 - "Bash is All You Need" 
- 30:00 - Skills & Progressive Context Disclosure
- 50:00 - Designing Agents (Spreadsheet Example)
- 01:07:00 - Sub-agents & Context Management
- 01:23:00 - Prototyping with Claude Code
- 01:26:00 - Pokemon Agent Demo
- 01:40:00 - Agent SDK & Productionization
- 01:44:00 - Q&A
