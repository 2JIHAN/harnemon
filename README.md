<div align="center">

# ⚡ HARNEMON ⚡

**The Pokémon-Style, Zero-Dependency Autonomous Harness Companion for AI Coding Agents**

<p align="center">
  <em>"Global Harnemon is a Class (Species), and Project Harnemon is an Instance ('Ash's Pikachu')."</em>
</p>

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](LICENSE)
[![Zero-Dependency](https://img.shields.io/badge/Dependencies-Zero-success.svg?style=for-the-badge)](#-the-3-invariants)
[![Runtime: Pure POSIX Bash](https://img.shields.io/badge/Runtime-Pure_POSIX_Bash-orange.svg?style=for-the-badge)](#-the-3-invariants)
[![Architecture: 3 Pillars](https://img.shields.io/badge/Architecture-3_Pillars-purple.svg?style=for-the-badge)](#-the-3-pillars)
[![Evolution: Self-Evolving](https://img.shields.io/badge/Evolution-Hermetic_Learning-red.svg?style=for-the-badge)](#-self-evolution-engine-powered-by-hermes--grok-bot)

<br/>

```text
       ┌──────────────────────────────────────────────────────────────┐
       │   🌐 GLOBAL HARNEMON (Class / Species)                       │
       │   ~/.harnemon/ (Numbleet, Fortoise, Monkin, Yagni Blueprints)│
       └──────────────────────────────────────────────────────────────┘
                                      │
                   harnemon adopt     │  (Adoption / Instantiation)
                                      ▼
       ┌──────────────────────────────────────────────────────────────┐
       │   🏠 PROJECT HARNEMON (Instance / Individual)                │
       │   /my-project/.agents/ (A living partner evolving with repo) │
       └──────────────────────────────────────────────────────────────┘
```

</div>

---

## 🌟 The Philosophy: Class vs. Instance

Traditional AI harnesses either copy-paste monolithic prompt blobs across repositories or burden projects with heavy npm/pip dependencies. **Harnemon solves this through the object-oriented Class/Instance paradigm, styled after the world of Pokémon.**

### 1. Global Harnemon is a Class (Species)
- Resides in the developer's global belt at `~/.harnemon`.
- Just as **Pikachu, Squirtle, Charmander, and Bulbasaur** represent species blueprints, Global Harnemon holds the pure **DNA (rules, skills, hooks architecture)** unpolluted by any single codebase.

### 2. Project Harnemon is an Instance ('Ash's Pikachu')
- Running `harnemon adopt` inside any repository instantiates a **unique, living Harnemon instance** bound to that workspace.
- Just as **Ash's Pikachu** journeyed alongside Ash to master unique combat moves, your adopted Harnemon **absorbs your repo's domain conventions, architectural quirks, and bug history to evolve autonomously (Self-Evolution)**.
- **Zero-Dependency Footprint**: Leaves **0 bytes** in `package.json`, `Cargo.toml`, or `pyproject.toml`. Harnemon runs purely on native POSIX Bash and standard Git.

---

## 📖 Harnedex — The 4 Legendary Gen-1 Archetypes

Harnemon comes equipped with 4 archetypal species inspired by classic Gen-1 Pokémon starters. Choose the companion that matches your team's engineering mindset:

| No. | Species | Gen-1 Type | Real-World Origin | Signature Trait & Core Moves |
| :---: | :--- | :--- | :--- | :--- |
| **No.001** | **[Numbleet](docs/case-studies/01-jihan-harness.md)** | `Electric ⚡` | `2JIHAN/jihan-harness` | **Trait: Lightning Router**<br>Ultra-fast 50-token Skill Router. Lightning-fast response, zero-dependency root-clean agility. |
| **No.002** | **[Fortoise](docs/case-studies/02-everything-claude-code.md)** | `Water 💧` | `affaan-m/everything-claude-code` | **Trait: Config-Guard Shell**<br>A colossal fortress of 288 moves. Hard-blocks any sneaky attempt by AI to weaken linter/formatter rules. |
| **No.003** | **[Monkin](docs/case-studies/03-obra-superpowers.md)** | `Fire 🔥` | `obra/superpowers` | **Trait: The Iron Law Crucible**<br>Practitioner of *The Iron Law*. Burns away guesswork; strictly forbids touching code until root causes are proven. |
| **No.004** | **[Yagni](docs/case-studies/04-dietrich-ponytail.md)** | `Grass 🍃` | `DietrichGebert/ponytail` | **Trait: Ladder of Laziness**<br>The genius slacker who prunes bloat. Slashes speculative code (`-N lines`), prefers stdlib, and harvests debt. |

---

## 🏛️ The 3 Pillars

Every Harnemon’s anatomy is built upon 3 orthogonal engineering pillars rather than bloated prompt files:

```text
       ┌──────────────────────────────────────────────────┐
       │                Harnemon Anatomy                  │
       └──────────────────────────────────────────────────┘
             │                  │                  │
             ▼                  ▼                  ▼
      [ Pillar 1: Rule ] [ Pillar 2: Skill ] [ Pillar 3: Hook ]
      • Abilities        • Learned Moves     • Held Items
      • Passive Limits   • On-demand Mastery • Physical Gates
      • (~50-token hub)  • (Detailed specs)  • (exit 0 / exit 1)
```

1. **Abilities (`rules/`)**: Minimal cognitive guardrails loaded into every turn (`fluent-korean`, `task-execution-protocol`, `skill-routing`).
2. **Moves (`skills/`)**: On-demand specialized playbooks loaded only when triggered (`ponytail`, `systematic-debugging`, `writing-docs`).
3. **Held Items (`hooks/`)**: Deterministic Git pre-commit and commit-msg gates that reject bad commits with physical exit codes (`commit-msg`, `pre-commit`).

---

## 🔒 The 3 Invariants

Every tool and rule in Harnemon strictly obeys 3 system invariants:

- **1. Idempotency** — Running `harnemon adopt` once or a hundred times yields the exact same deterministic state.
- **2. Auto-wiring** — Newly learned skills or rules are instantly linked into `.agents/AGENTS.md` and AI client configs (`.claude`, `.gemini`).
- **3. Zero-dependency** — Completely free of Node.js, Python, or Cargo dependencies. Operates anywhere Bash and Git exist.

---

## ⚡ Quickstart

### 1. Install Global Tool
```bash
# Clone to global belt and symlink to PATH
git clone https://github.com/2JIHAN/harnemon.git ~/.harnemon
ln -sf ~/.harnemon/bin/harnemon ~/.local/bin/harnemon
```

### 2. Adopt a Starter Harnemon (`adopt`)
Navigate to any project directory and run `harnemon adopt`:
```bash
cd /path/to/my-project

# Interactive Professor Oak starter selection dialog:
harnemon adopt

# Or directly adopt by species:
harnemon adopt numbleet   # Electric ⚡ (Fast skill router)
harnemon adopt fortoise   # Water 💧    (Config guardian shell)
harnemon adopt monkin     # Fire 🔥     (The Iron Law debugging)
harnemon adopt yagni      # Grass 🍃    (Ladder of Laziness)
```

### 3. Inspect Partner Status & Health
```bash
# 1. View your adopted partner's profile, abilities, moves, and held items
harnemon status

# 2. Diagnose token health, rule bloat, and hook executability
harnemon audit

# 3. Browse the legendary Harnedex archetypes
harnemon dex
```

---

## 🧬 Self-Evolution Engine (Powered by Hermes + Grok Bot)

Your adopted Harnemon doesn't stay static—it learns and evolves as you code together:

```text
[Coding Session] ──2x Corrections──▶ [Pattern Detection] ──Hermes Loop──▶ [Autonomous SKILL.md]
                                                                                  │
[Evolution Complete] ◀── Self-Audit Pass ◀── Inscribe to skill-routing.md ────────┘
```

- **The 2-Correction Rule**: When a developer corrects a behavior or explains a convention twice, Harnemon flags it for codification.
- **Autonomous Skill Synthesis (Hermes Loop)**: Harnemon abstracts the solution and writes `.agents/skills/<new-move>/SKILL.md` autonomously.
- **Cross-Pollination (`sync`)**: New moves learned in Project A can be synced back to the global belt to empower Harnemons in other repos:
  ```bash
  harnemon sync
  ```

---

## 📂 Repository Structure

```text
harnemon/
├── bin/
│   └── harnemon                             # Global Trainer CLI
├── rules/                                   # [Abilities: Always-on Rules]
│   ├── fluent-korean.md                     # • Natural Korean interaction conventions
│   ├── harness-evolution.md                 # • Self-evolution & ownership protocol
│   ├── skill-routing.md                     # • On-demand skill dispatcher hub
│   ├── task-execution-protocol.md           # • Sizing, anti-polling & verification
│   └── terminal-response-format.md          # • Clean visual presentation layout
├── skills/                                  # [Moves: On-Demand Skills]
│   ├── harness-evolution/                   # • Skill synthesis and router playbook
│   ├── systematic-debugging/                # • Root-cause tracing & 4-step debugging
│   ├── ponytail/                            # • Minimal coding & Ladder of Laziness
│   ├── ponytail-review/                     # • Diff complexity hunter review
│   ├── ponytail-audit/                      # • Full-repo bloat auditor
│   ├── ponytail-debt/                       # • Shortcut debt ledger harvester
│   ├── delegate-to-aside/                   # • Aside AI browser integration
│   ├── writing-docs/                        # • Technical writing standards
│   └── writing-docs-in-korean/              # • Korean technical documentation
├── hooks/                                   # [Held Items: Git Hard Gates]
│   ├── commit-msg/                          # • 72-char limit & AI signature blocker
│   └── pre-commit/                          # • Config weakening & secret leak blocker
├── docs/                                    # [Harnedex & Theory]
│   ├── what-is-a-harness.md                 # • Harness vs prompt definition
│   ├── maturity-model.md                    # • 5-stage harness maturity framework
│   ├── three-pillars-and-invariants.md      # • 3 Pillars & Invariants specification
│   └── case-studies/                        # • Detailed Harnedex archetype entries
└── README.md
```

---

## 📄 License

Harnemon is open-sourced under the [MIT License](LICENSE).
