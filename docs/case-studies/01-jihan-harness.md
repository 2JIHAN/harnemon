# Harnedex No.001: Nimbleet — Electric Type ⚡
> **Archetype**: `2JIHAN/jihan-harnesslake` | **Trait**: Lightning Router (50-token ultralight speedster)

The archetypal lean 3-pillar harness implementing the 50-token skill dispatcher pattern and zero-dependency root-clean integrity.

---

## 1. Overview & Design Philosophy

- **Repository** — [github.com/2JIHAN/jihan-harnesslake](https://github.com/2JIHAN/jihan-harnesslake)
- **Core Motto** — "Zero-Fluff High-Density Practical Harness"
- **Design Philosophy** — Rather than bundling hundreds of speculative functions, it curates only essential rules, playbooks, and memory scaffolding into a 3-pillar structure, sustaining blazing execution speed and near-zero prompt overhead.

---

## 2. Architecture Breakdown

```text
jihan-harnesslake/
├── rules/                           # [Pillar 1] Always-on cognitive constraints (<100 tokens)
│   ├── fluent-korean.md             # • High-clarity Korean prose directives
│   ├── skill-routing.md             # • 50-token task-context skill dispatch table
│   ├── task-execution-protocol.md   # • No-polling & zero-blind verification protocol
│   └── terminal-response-format.md  # • Visual layout and Markdown output rules
├── skills/                          # [Pillar 2] On-demand playbooks
│   ├── systematic-debugging/        # • Root-cause first debugging methodology
│   ├── ponytail/                    # • Ladder of Laziness & minimal coding
│   ├── ponytail-review/             # • Diff complexity hunter
│   ├── ponytail-audit/              # • Whole-repo over-engineering audit
│   ├── ponytail-debt/               # • Shortcut debt ledger harvester
│   ├── delegate-to-aside/           # • Real-time browser GUI automation
│   ├── writing-docs/                # • English technical documentation standard
│   └── writing-docs-in-korean/      # • Korean technical documentation standard
├── memory/                          # [Pillar 3] 3-Layer Autonomous Memory
│   ├── episodes/                    # • Append-only daily timeline logs
│   ├── MEMORY.md                    # • Distilled L1 decisions & active conventions
│   └── semantic/                    # • Evergreen domain & architecture catalog
└── install.sh                       # Idempotent auto-wiring master setup
```

---

## 3. Key Innovative Mechanisms

### 1. The 50-Token Skill Dispatcher Pattern
- **The Problem** — Placing heavy procedural guides in always-on rules wastes tokens. Storing them only in unindexed skill folders causes the AI to overlook them and guess arbitrarily.
- **The Solution** — `rules/skill-routing.md` loads a 50-token contextual traffic signal into every turn:
  - On Coding / Refactoring ➔ Mandates loading `ponytail`
  - On Bugs / Test Failures ➔ Mandates loading `systematic-debugging`
  - On Documentation ➔ Mandates loading `writing-docs`
  - On Complexity Review ➔ Mandates loading `ponytail-review`
- **Result** — Minimizes baseline token consumption while ensuring 100% compliance when specialized execution is required.

### 2. Zero-Dependency Clean Root Wiring
- Operates entirely via POSIX Bash and Python transclusion without external package dependencies.
- Isolates configurations within `.agents/` and transparently bridges `.claude/` and `.gemini/` via recursive `@` transclusion.

---

## 4. Architectural Takeaways

- **Extreme Token Efficiency** — Keeps always-on rules compact, preventing model attention degradation across long multi-hour sessions.
- **Universal Compatibility** — Operates consistently across Antigravity, Claude Code, Cursor, and Codex CLI environments.

---

## 5. Recommended For

- Solo developers, startups, and agile teams demanding ultra-fast turn speed.
- Teams prioritizing minimal prompt token costs and zero-bloat repository hygiene.
