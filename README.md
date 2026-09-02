<div align="center">

# ⚡ HARNEMON ⚡

**The Pokémon-Style, Zero-Dependency Autonomous Harness Companion for AI Coding Agents**

<p align="center">
  <em>"Global Harnemon is a Class (Species), and Project Harnemon is an Instance ('Ash's Pikachu')."</em>
</p>

<p align="center">
  <a href="README.md"><b>English</b></a> •
  <a href="README.ko.md"><b>한국어</b></a> •
  <a href="README.ja.md"><b>日本語</b></a> •
  <a href="README.zh-CN.md"><b>简体中文</b></a>
</p>

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](LICENSE)
[![Zero-Dependency](https://img.shields.io/badge/Dependencies-Zero-success.svg?style=for-the-badge)](#-the-3-invariants)
[![Runtime: Pure POSIX Bash](https://img.shields.io/badge/Runtime-Pure_POSIX_Bash-orange.svg?style=for-the-badge)](#-the-3-invariants)
[![Architecture: 3 Pillars](https://img.shields.io/badge/Architecture-3_Pillars-purple.svg?style=for-the-badge)](#-the-3-pillars)
[![Evolution: Self-Evolving](https://img.shields.io/badge/Evolution-Hermetic_Learning-red.svg?style=for-the-badge)](#-self-evolution--incubating-engine)

<br/>

```text
       ┌──────────────────────────────────────────────────────────────┐
       │   🌐 GLOBAL HARNEMON (Class / Species)                       │
       │   ~/.harnemon/ (Nimbleet, Fortoise, Monkin, Yagni Blueprints)│
       └──────────────────────────────────────────────────────────────┘
                    │                                 ▲
     harnemon adopt │                                 │ harnemon register
                    ▼                                 │
       ┌──────────────────────────────────────────────────────────────┐
       │   🏠 PROJECT HARNEMON (Instance / Individual)                │
       │   /my-project/.harnemons/ (An adopted or hatched partner)   │
       └──────────────────────────────────────────────────────────────┘
```

</div>

---

## 🌟 The Philosophy: Class vs. Instance & Incubator

Traditional AI harnesses either copy-paste monolithic prompt blobs across repositories or burden projects with heavy npm/pip dependencies. **Harnemon solves this through the object-oriented Class/Instance paradigm, styled after the world of Pokémon.**

### 1. Global Harnemon is a Class (Species)
- Resides in the developer's global belt at `~/.harnemon`.
- Just as **Pikachu, Squirtle, Charmander, and Bulbasaur** represent species blueprints, Global Harnemon holds the pure **DNA (rules, skills, hooks architecture)** unpolluted by any single codebase.

### 2. Project Harnemon is an Instance ('Ash's Pikachu')
- Running `harnemon adopt` inside any repository instantiates a **unique, living Harnemon instance** bound to that workspace.
- Just as **Ash's Pikachu** journeyed alongside Ash to master unique combat moves, your adopted Harnemon **absorbs your repo's domain conventions, architectural quirks, and bug history to evolve autonomously (Self-Evolution)**.
- **Zero-Dependency Footprint**: Leaves **0 bytes** in `package.json`, `Cargo.toml`, or `pyproject.toml`. Harnemon runs purely on native POSIX Bash and standard Git.

### 3. The Harnemon Incubator (Blank Egg 🥚)
- Don't want pre-packaged rules? Run `harnemon incubate` to start with a **completely blank Egg**.
- As you code and provide feedback (The 2-Correction Rule), the Egg automatically synthesizes 3-Pillar rules/skills and accumulates EXP.
- When mature, run `harnemon hatch <name>` to birth your own custom species, and `harnemon register` to save it to your global Harnedex!

---

## 📖 Harnedex — The 4 Legendary Gen-1 Archetypes

Harnemon comes equipped with 4 archetypal species inspired by classic Gen-1 Pokémon starters:

| No. | Species | Gen-1 Type | Real-World Origin | Signature Trait & Core Moves |
| :---: | :--- | :--- | :--- | :--- |
| **No.000** | **[Harnemon Egg](docs/harnemon-incubator.md)** | `Incubating 🌱` | `Harnemon Incubator` | **Trait: Blank Canvas**<br>0-rule starter. Absorbs developer habits and 2-correction feedback to hatch a custom species. |
| **No.001** | **[Nimbleet](docs/case-studies/01-jihan-harness.md)** | `Electric ⚡` | `2JIHAN/jihan-harness` | **Trait: Lightning Router**<br>Ultra-fast 50-token Skill Router. Lightning-fast response, zero-dependency root-clean agility. |
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

### 1. Install Global Tool & Awaken Global Awareness
```bash
# Clone to global belt and run one-time global setup
git clone https://github.com/2JIHAN/harnemon.git ~/.harnemon
~/.harnemon/bin/harnemon setup
```
> `harnemon setup` automatically symlinks the CLI to your PATH and registers Global Harnemon Awareness in `~/.agents/AGENTS.md` and `~/.claude/CLAUDE.md` so AI agents in all workspaces recognize Harnemon.

### 2. Adopt a Starter or Incubate a Blank Egg
Navigate to any project directory:
```bash
cd /path/to/my-project

# Option A: Start from a Blank Egg (Incubation mode — evolves through coding):
harnemon incubate

# Option B: Interactive starter selection dialog:
harnemon adopt

# Option C: Directly adopt by species:
harnemon adopt nimbleet   # Electric ⚡ (Fast skill router)
harnemon adopt fortoise   # Water 💧    (Config guardian shell)
harnemon adopt monkin     # Fire 🔥     (The Iron Law debugging)
harnemon adopt yagni      # Grass 🍃    (Ladder of Laziness)
```

### 3. Hatch & Register Your Custom Species
Once your incubated egg matures through feedback loops:
```bash
# Hatch into a named custom species:
harnemon hatch "Supabird" --type "Database ⚡" --desc "Supabase RLS & Edge Function Master"

# Register to global Harnedex so all your projects can adopt it:
harnemon register
```

### 4. Build a Multi-Harnemon Party (`adopt` / `party` / `switch`)
Assemble a team of up to 6 specialized Harnemons in a single project with simple `adopt` commands:
```bash
# Adopt specialist partners into your party anytime:
harnemon adopt monkin      # Adopt Monkin 🔥 for strict debugging
harnemon adopt yagni       # Adopt Yagni 🍃 for code-pruning

# View your party lineup:
harnemon party

# Switch the Active Lead partner dynamically:
harnemon switch nimbleet   # Active turns now handled by Nimbleet ⚡
```bash
# Recruit specialist partners into your party:
harnemon recruit monkin    # Recruit Monkin 🔥 for strict debugging
harnemon recruit yagni     # Recruit Yagni 🍃 for code-pruning

# View your party lineup:
harnemon party

# Switch the Active Lead partner dynamically:
harnemon switch monkin     # Active turns now handled by Monkin 🔥
```

### 5. Inspect Partner Status & Health
```bash
# 1. View your adopted partner profile or egg incubation progress
harnemon status

# 2. Diagnose token health, rule bloat, and hook executability
harnemon audit

# 3. Browse the legendary Harnedex archetypes & custom species
harnemon dex
```

---

## 🧬 Self-Evolution & Incubating Engine

Your adopted Harnemon doesn't stay static—it learns and evolves as you code together:

```text
[Coding Session] ──2x Corrections──▶ [Pattern Detection] ──Hermes Loop──▶ [Autonomous SKILL.md]
                                                                                  │
[Evolution Complete] ◀── Self-Audit Pass ◀── Inscribe to skill-routing.md ────────┘
```

- **The 2-Correction Rule**: When a developer corrects a behavior or explains a convention twice, Harnemon flags it for codification.
- **Autonomous Skill Synthesis (Hermes Loop)**: Harnemon abstracts the solution and writes `skills/<new-move>/SKILL.md` autonomously.
- **Cross-Pollination (`sync`)**: New moves learned in Project A can be synced back to the global belt to empower Harnemons in other repos:
  ```bash
  harnemon sync
  ```

---

## 📂 Repository Structure

```text
harnemon/
├── bin/
│   └── harnemon                             # ⚡ Global Trainer CLI (v0.9.0)
├── species/                                 # 🧬 [Mature Gen-1 Species Blueprints]
│   ├── nimbleet/                            # • No.001: Lightning Router (⚡)
│   ├── fortoise/                            # • No.002: Config-Guard Fortress (💧)
│   ├── monkin/                              # • No.003: The Iron Law Crucible (🔥)
│   └── yagni/                               # • No.004: Ladder of Laziness Pruner (🍃)
├── catalog/                                 # 🌐 Community & Hatched Custom Species
├── docs/                                    # 📚 Architecture Theory & Harnedex
├── .github/                                 # 🚀 Open-source Governance & CI Workflows
└── README.md (EN / KO / JA / ZH)            # 🌐 4-Language Synchronized Docs
```

---

## 👥 Contributors

Thanks goes to these wonderful people for contributing to Harnemon:

<a href="https://github.com/2JIHAN/harnemon/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=2JIHAN/harnemon" alt="Harnemon Contributors" />
</a>

Contributions of all kinds (bug fixes, new Harnemon species, documentation) are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) to get started.

---

## 📄 License

Harnemon is open-sourced under the [MIT License](LICENSE).
