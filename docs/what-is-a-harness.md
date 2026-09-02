# What is an AI Harness?

Defines the conceptual foundation of an **AI Harness**, its fundamental distinction from raw prompts, and the engineering imperatives that necessitate harness architecture.

---

## 1. Conceptual Definition of a Harness

- **Definition** — An **external engineering control layer** that governs AI coding assistants, ensuring deterministic adherence to project rules, specialized tools, and verification protocols while preventing hallucinations and arbitrary code drift.
- **Etymology** — Originates from the equine harness that channels a wild horse's strength under a driver's control, or the safety harness that secures a climber.
- **Core Role** — Rather than attempting to retrain or fine-tune the LLM brain itself, a harness places **Always-on Rules**, **On-demand Skills**, and **Deterministic Hooks** at the input/output boundaries of the model to strictly bound its operational envelope.

---

## 2. Comparison: Prompt vs. Agent vs. Harness

| Dimension | **Prompt** | **Agent** | **Harness** |
| :--- | :--- | :--- | :--- |
| **Nature** | Ephemeral natural language instruction | Autonomous reasoning and execution loop | External system specification governing the agent |
| **Analogy** | Spoken order given to a driver | The driver operating the vehicle (LLM) | Guardrails, traffic signals, seatbelts, and speed governors |
| **Persistence** | Evaporates when the turn completes | Persists across conversational session | Bound to Git lifecycle and repository lifespan |
| **Enforceability** | 0% (Model can ignore instructions) | Partial (Depends on internal reasoning) | **100% (Physical binary gates, e.g. Pre-commit/Pre-invocation hooks)** |
| **Failure Mode** | Instruction forgetfulness, formatting drift | Infinite retry loops, destructive edits | Bloat if Single Responsibility Principle is violated |

---

## 3. Why Raw Prompt Engineering Inevitably Fails

Stuffing hundreds of lines of instructions into a monolithic system prompt (`CLAUDE.md`, `.cursorrules`) breaks down as codebases scale due to four engineering bottlenecks:

- **Attention Degradation (The Haystack Problem)** — Even with massive context windows, complex rules placed in monolithic prompts are progressively forgotten due to non-uniform attention distribution.
- **The Context Tax (Token Bloat)** — Injecting 10,000 tokens of static rules into every trivial turn ("Explain this function") causes explosive API costs and sluggish latency.
- **Absence of Hard Gates** — Asking an LLM politely ("Keep commits under 72 characters", "Never weaken linter configs") fails 1–5% of the time due to probabilistic token generation.
- **Rule Collisions & Conflicting Directives** — As uncurated instructions accumulate, contradictory rules paralyze model decision-making.

---

## 4. The 3 Essential Pillars of a Modern Harness

Production-grade harnesses discard monolithic prompts in favor of three physically separated pillars:

1. **Rule (Always-on Ability)** — Minimal cognitive constraints injected into every turn (<100 tokens).
2. **Skill (On-demand Move)** — Deep, multi-step execution playbooks loaded dynamically only when matching task contexts occur.
3. **Hook (Held Item Gate)** — Physical OS/Git gates that intercept execution and fail fast (`exit 1`) upon invariant violations.
