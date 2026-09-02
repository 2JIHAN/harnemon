# The 3 Pillars & 3 Invariants

Specifies the structural taxonomy (3 Pillars) and perpetual integrity laws (3 Invariants) governing the Harnemon architecture.

---

## 1. The 3 Pillars

Every instruction, script, and configuration in a harness must belong to exactly one of the three pillars without mixing concerns:

```text
       ┌─────────────────────────────────────────┐
       │             AI Agent Harness            │
       └─────────────────────────────────────────┘
            │                 │                 │
            ▼                 ▼                 ▼
     [ Pillar 1: Rule ] [ Pillar 2: Skill ] [ Pillar 3: Hook ]
     (Always-on Ability) (On-demand Move)   (Held Item Gate)
```

### Pillar 1: Rule (Always-on Cognitive Constraints)
- **Nature** — Lightweight cognitive boundaries automatically transcluded into every conversational turn.
- **Scope** — Visual output layout (`terminal-response-format`), task execution discipline (`task-execution-protocol`), and on-demand skill dispatchers (`skill-routing`).
- **Design Standard** — **Extreme minimalism**. Rules exceeding hundreds of lines degrade attention and inflate token costs. Every rule file must remain dense and under 50–100 tokens.

### Pillar 2: Skill (On-demand Playbooks)
- **Nature** — Detailed procedural execution manuals loaded dynamically via tools (`view_file`, `invoke_skill`) only when matching task contexts arise.
- **Scope** — Root-cause debugging (`systematic-debugging`), complexity reduction (`ponytail`), technical writing standards (`writing-docs`), and browser GUI orchestration (`delegate-to-aside`).
- **Design Standard** — Freely contains 100–500 lines of rigorous playbooks and examples without contaminating always-on context.

### Pillar 3: Hook (Deterministic Binary Gates)
- **Nature** — OS and Git lifecycle interceptors that enforce binary constraints without relying on probabilistic model compliance.
- **Scope** — Pre-invocation transclusion dispatchers, pre-commit secret guards, and commit message format validators.
- **Design Standard** — Strictly restricted to binary outcomes (`exit 0` or `exit 1`). Subjective qualitative evaluations must never be implemented as hooks.

---

## 2. The 3 System Invariants

Every Harnemon companion and workspace must uphold these three system invariants:

### Invariant 1: Idempotency
- **Principle** — Executing harness setup or update operations 1 time or 100 times must produce the exact same final deterministic state.
- **Implementation**
  - Configuration blocks are fenced by versioned markers: `<!-- harnemon:<id>:begin v<VERSION> -->` to `<!-- harnemon:<id>:end -->`. Regenerations replace only fenced blocks, preserving hand-written developer prose.
  - Symlink creations and path resolutions safely overwrite or update existing targets.

### Invariant 2: Auto-wiring
- **Principle** — Adding or modifying components (Rules, Skills, Memory) must never require manual multi-file registration.
- **Implementation**
  - Placing rules or skills automatically wires imports into `.agents/AGENTS.md` and generates aggregated symlinks under `.agents/skills/`.
  - Platforms (Antigravity, Claude Code, Cursor, Codex) automatically discover the unified harness without fragmented configurations.

### Invariant 3: Zero-dependency
- **Principle** — Harness operation must not impose heavy external runtimes or package manager overhead.
- **Implementation**
  - Core CLI tools and dispatchers execute instantly across macOS and Linux using POSIX shell and standard utilities (`git`, `grep`, `sed`).
  - Operates in under 10ms regardless of the target project's tech stack (Node, Python, Go, Rust).
