# Harnedex No.001: Nimbleet — Electric Type ⚡
> **Archetype**: `2JIHAN/jihan-harnesslake` | **Trait**: Lightning Router (50-token ultralight speedster)

The archetypal lean 3-pillar harness implementing the 50-token skill dispatcher pattern and zero-dependency root-clean integrity.

---

## 1. Overview & Design Philosophy

- **Repository** — [github.com/2JIHAN/jihan-harnesslake](https://github.com/2JIHAN/jihan-harnesslake)
- **Core Motto** — "Zero-Fluff High-Density Practical Harness"
- **Design Philosophy** — Rather than bundling hundreds of speculative functions, it curates only essential rules, playbooks, and physical gates into a 3-pillar structure, sustaining blazing execution speed and near-zero prompt overhead.

---

## 2. Architecture Breakdown

```text
jihan-harnesslake/
├── rules/                           # [Pillar 1] Always-on cognitive constraints (<100 lines each)
│   ├── fluent-korean.md             # • High-clarity Korean prose directives
│   ├── task-execution-protocol.md   # • No-polling & zero-blind verification protocol
│   └── terminal-response-format.md  # • Visual layout and Markdown output rules
├── skills/                          # [Pillar 2] On-demand playbooks
│   ├── INDEX.md                     # • The always-on catalog: trigger and location per skill
│   ├── ponytail/                    # • Ladder of Laziness & minimal coding
│   ├── ponytail-review/             # • Diff complexity hunter
│   ├── ponytail-audit/              # • Whole-repo over-engineering audit
│   ├── ponytail-debt/               # • Shortcut debt ledger harvester
│   ├── systematic-debugging/        # • Root-cause first debugging methodology
│   ├── grill-me/                    # • Planning interview entry point (stateless)
│   ├── grill-with-docs/             # • Planning interview that writes CONTEXT.md and ADRs
│   ├── grilling/                    # • The interview engine: design tree asked in rounds
│   ├── domain-modeling/             # • Glossary and ADR discipline
│   ├── delegate-to-aside/           # • Real-time browser GUI automation
│   ├── graph-artifact-builder/      # • Standalone HTML node-edge graph artifacts
│   └── writing-docs-in-korean/      # • Korean technical documentation standard
├── hooks/                           # [Pillar 3] Deterministic physical gates (0 tokens)
│   ├── commit-msg/                  # • Conventional Commits, 72-char cap, AI signature block
│   ├── pre-commit/                  # • Linter-config weakening and secret staging block
│   └── install.sh                   # • Hook-only installer
├── docs/                            # Architecture specification (3 pillars, 3 invariants)
└── install.sh                       # Idempotent auto-wiring master setup
```

---

## 3. Key Innovative Mechanisms

### 1. The 50-Token Skill Dispatcher Pattern
- **The Problem** — Placing heavy procedural guides in always-on rules wastes tokens. Storing them only in unindexed skill folders causes the AI to overlook them and guess arbitrarily.
- **The Solution** — `skills/INDEX.md` loads a contextual traffic signal into every turn, one row per skill, and marks the rows that must be loaded before the first file is touched:
  - On Coding / Refactoring ➔ Mandates loading `ponytail`
  - On Bugs / Test Failures ➔ Mandates loading `systematic-debugging`
  - On Korean Documentation ➔ Mandates loading `writing-docs-in-korean`
  - On Complexity Review ➔ Points at `ponytail-review`
- **Why the catalog lives in `skills/`, not `rules/`** — The routing table changes every time the skill set changes. Kept as a rule, one addition means editing two pillars, and any drift between them points the model at a skill that no longer exists. Housed inside the skill bundle, the index moves with the skills it indexes.
- **Result** — Minimizes baseline token consumption while ensuring 100% compliance when specialized execution is required.

### 2. Zero-Dependency Clean Root Wiring
- Installs and wires with POSIX Bash alone, and the gates run on Bash and Node. Nothing is fetched or built, so there is no lockfile and no package to go stale.
- Isolates configurations within `.agents/` and transparently bridges `.claude/` and `.gemini/` via recursive `@` transclusion.
- `install.sh` is idempotent: rerunning it never duplicates a transclusion line and never overwrites a hand-edited `AGENTS.md`.

### 3. Physical Gates Below the Model
- The third pillar consumes zero context because it never enters one. `commit-msg` rejects non-Conventional summaries, summaries past 72 characters, and every AI signature trailer, so the repository history reads as human-authored regardless of who typed it.
- `pre-commit` blocks two failure modes the model is prone to: weakening `eslint`/`prettier`/`biome`/`ruff` configuration to make a check pass, and staging `.env`, `*.pem`, or `*.key`.

---

## 4. Architectural Takeaways

- **Extreme Token Efficiency** — Keeps always-on rules compact, preventing model attention degradation across long multi-hour sessions.
- **Universal Compatibility** — Operates consistently across Antigravity, Claude Code, Cursor, and Codex CLI environments.
- **Enforcement Laddering** — Each constraint sits at the weakest layer that can still hold it: prose in rules, procedure in skills, and anything countable in a hook that exits non-zero.

---

## 5. Recommended For

- Solo developers, startups, and agile teams demanding ultra-fast turn speed.
- Teams prioritizing minimal prompt token costs and zero-bloat repository hygiene.
