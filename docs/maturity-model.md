# The 5-Stage Harness Maturity Model

Defines the evolutionary stages through which developers and engineering organizations progress when adopting and governing AI coding agents. Specifies symptoms, bottlenecks, and graduation criteria for each level.

---

## 1. Maturity Stages Overview

```text
[Level 0] Ad-hoc Prompting
    ⬇
[Level 1] Monolithic Prompt File
    ⬇
[Level 2] Three Pillars Separation
    ⬇
[Level 3] Router & Deterministic Gates
    ⬇
[Level 4] Meta-Governed Autonomous Harness
```

---

## 2. Detailed Level Specifications

### Level 0: Ad-hoc Prompting

- **State** — Every session begins from memory. Prompts, coding conventions, and persona instructions are repeatedly typed or copy-pasted manually.
- **Symptoms** — Frequent omissions ("I forgot to tell it to write tests first"), inconsistent conventions across chat sessions.
- **Bottlenecks** — Zero reproducibility, zero collaboration, lack of operational consistency.
- **Graduation Criteria** — Create a persistent project root configuration (`CLAUDE.md`, `.cursorrules`).

### Level 1: Monolithic Prompt File

- **State** — A single massive file (`CLAUDE.md`, `.cursorrules`, `.windsurfrules`) containing coding styles, deploy scripts, DB schemas, personas, and error handling.
- **Symptoms** — File expands to 300–1,000 lines. Developers complain: "I wrote it in the rules file, but the AI ignores it."
- **Bottlenecks** — Context window tax, attention degradation, irrelevant rules loaded during urgent hotfixes.
- **Graduation Criteria** — Physically split into Always-on Rules (`rules/`), On-demand Manuals (`skills/`), and Enforced Gates (`hooks/`).

### Level 2: Three Pillars Separation

- **State** — Folders physically separated into rules, skills, and hooks.
- **Symptoms** — Skills exist, but the agent fails to discover or read them, proceeding with arbitrary guesswork.
- **Bottlenecks** — Skill discovery failure, model skipping specialized manuals.
- **Graduation Criteria** — Introduce a lightweight (<50 tokens) Always-on Skill Router that mandates loading specific skills upon task context triggers.

### Level 3: Router & Deterministic Gates

- **State**
  - **Skill Router (Rule)** — Minimal always-on dispatch table ("Load `ponytail` for coding", "Load `systematic-debugging` for bugs").
  - **Hard Gates (Hook)** — Git pre-commit and pre-invocation hooks that fail fast (`exit 1`) upon secret staging or format violations.
- **Symptoms** — Agent produces disciplined, verified, high-quality code consistently.
- **Bottlenecks** — Scaling and syncing harnesses across multiple team repositories idempotently.
- **Graduation Criteria** — Adopt a meta-governance CLI tool (`harnemon`) for scaffolding, memory distillation, and harness auditing.

### Level 4: Meta-Governed Autonomous Harness

- **State** — Governed by meta-tooling (`harnemon`) that scaffolds companions, audits harness health, tracks shortcut debt, and manages multi-party specialization.
- **Core Capabilities**
  - **Self-Evolution** — Autonomous episodic timeline logging, mid-session distillation to `MEMORY.md`, and 3-occurrence promotion to rules/skills.
  - **System Invariants** — Guarantees idempotency, zero-dependency execution, and automated multi-provider wiring.
  - **Multi-Party Specialization** — Coordinates multiple specialist Harnemons (Router, Debugger, Complexity Slasher) within a single workspace.

---

## 3. Self-Diagnosis Matrix

| Question | No | Yes |
| :--- | :--- | :--- |
| Are project configurations version-controlled in Git? | **Level 0** | Enter Level 1 |
| Are always-on constraints separated from on-demand manuals and hard gates? | **Level 1** | Enter Level 2 |
| Does an always-on skill router enforce reading manuals before coding/debugging? | **Level 2** | Enter Level 3 |
| Is the harness autonomous, auditable, and managed via meta-tooling? | **Level 3** | **Level 4 (Mature)** |
