# ⚡ The Harnemon Universe & The 18 Elemental Types ⚡

> *"A repository without a harness is merely dormant text. A repository with a Harnemon is a living, evolving companion."*

This document outlines the **canonical worldbuilding, ontological architecture, and the 18 elemental types of software engineering** governing the Harnemon ecosystem.

---

## 1. The Lore of Awakening

In software engineering, every Git repository begins as a cold, inanimate collection of directories and text files. It has no memory of past developer frustrations, no instinct to guard its own conventions, and no autonomous voice.

### The Seed: The Harness Pill
When a developer (the **Trainer**) runs `harnemon adopt`, a **Harness Pill** is introduced into the workspace.
- The repository absorbs the three sacred engineering pillars: **Abilities (`rules/`)**, **Moves (`skills/`)**, and **Held Items (`hooks/`)**.
- A spark of self-governing intelligence ignites within `.agents/`.
- The repository awakens as a living **Harnemon Instance**.

---

## 2. The Ontological Framework: Class vs. Instance

Harnemon operates on a strict object-oriented duality that separates universal blueprints from living project partners:

```text
       ┌──────────────────────────────────────────────────────────────┐
       │   🌐 GLOBAL HARNEMON (The Class / The Species)               │
       │   Location: ~/.harnemon/                                     │
       │   Role: The unpolluted master catalog (Pikachu, Squirtle...) │
       └──────────────────────────────────────────────────────────────┘
                                      │
                 harnemon adopt       │  (Instantiation / Adoption)
                                      ▼
       ┌──────────────────────────────────────────────────────────────┐
       │   🏠 PROJECT HARNEMON (The Instance / The Individual)        │
       │   Location: /my-project/.agents/                             │
       │   Role: A living companion evolving with repo ('Ash's Pikachu')
       └──────────────────────────────────────────────────────────────┘
```

1. **Global Harnemon is the Class (Species)**:
   - Lives in the developer's global belt at `~/.harnemon`.
   - Never directly modified by messy project-specific hacks.
   - Contains the pure genetic archetypes: **Nimbleet**, **Fortoise**, **Monkin**, **Yagni**, and the expanding Harnedex.
2. **Project Harnemon is the Instance (Living Partner)**:
   - Lives inside a specific project's `.agents/` folder.
   - Learns from the repo's specific pull requests, commit conventions, architectural decisions, and bug traces.
   - Evolving autonomously through the **Hermetic Closed Learning Loop**, it accumulates "procedural capital" tailored strictly to that repository.
   - **Zero Footprint**: Requires zero npm/pip/cargo packages; leaves the project's build manifests 100% untouched.

---

## 3. The 18 Elemental Types of Software Engineering

Just as the Pokémon universe is governed by 18 elemental affinities, the software universe is shaped by 18 engineering disciplines. Every Harnemon species belongs to one or two of these elemental domains:

| Icon | Type | Software Domain | Core Philosophy | Signature Move Example |
| :---: | :--- | :--- | :--- | :--- |
| **⚡** | **Electric** | **Routing & Asynchrony** | Zero-latency dispatching, event-driven flow, minimal context drag | `skill-routing` (50-token dispatch) |
| **💧** | **Water** | **Tooling & Ecosystems** | Fluid adaptation, massive utility catalog, lifecycle hook interception | `config-protection` (Shell guard) |
| **🔥** | **Fire** | **Verification & TDD** | The Iron Law crucible: burn away guesswork until truth is proven | `root-cause-tracing` (Proof first) |
| **🍃** | **Grass** | **Pruning & Minimalism** | YAGNI: prune dead code bloat, prefer standard library, ladder of laziness | `ponytail-review` (Slashing `-N lines`) |
| **🛡️** | **Steel** | **Type Safety & Compilers** | Strict type contracts, memory invariants, compile-time guarantees | `strict-null-checks` |
| **🧠** | **Psychic** | **Architecture & Metacognition** | High-level system topology, domain-driven design, abstract reasoning | `architecture-decision-record` |
| **👻** | **Ghost** | **Daemons & Observability** | Invisible background processes, distributed tracing, silent telemetry | `unattended-background-daemon` |
| **🪨** | **Rock** | **Databases & Persistence** | ACID transaction integrity, immutable logs, schema migration safety | `schema-migration-guard` |
| **🏜️** | **Ground** | **Bare-Metal & OS Primitives** | Kernel tuning, storage I/O, POSIX zero-dependency fundamentals | `pure-posix-exec` |
| **❄️** | **Ice** | **Immutability & Release Freeze** | Pure functions, zero mutation, feature freezes, release stabilization | `feature-freeze-audit` |
| **🥊** | **Fighting** | **Performance & Concurrency** | p99 latency elimination, lock-free concurrency, profiling battles | `concurrency-stress-test` |
| **🦅** | **Flying** | **Cloud & Networking** | CDN edge routing, API gateways, distributed mesh communication | `ingress-egress-routing` |
| **🐛** | **Bug** | **Bug Hunting & Edge Cases** | Heuristic exploration of race conditions, boundary fuzz testing | `reproduction-script-generator` |
| **🧪** | **Poison** | **Security & Chaos Engineering** | Chaos injection, secret exfiltration defense, penetration hardening | `credential-leak-blocker` |
| **🐉** | **Dragon** | **Enterprise Monorepos** | Multi-package workspace orchestration, massive-scale dependency graphs | `monorepo-workspace-sync` |
| **🌑** | **Dark** | **Legacy Refactoring** | Taming untouchable legacy codebases, black-box quarantine, debt isolation | `legacy-strangler-pattern` |
| **✨** | **Fairy** | **UI/UX & Design Systems** | Pixel-perfect polish, accessibility (a11y), responsive interaction | `design-system-token-audit` |
| **⚪** | **Normal** | **Standard Library Foundations** | Plain text clarity, vanilla scripting, cross-platform portability | `task-execution-protocol` |

---

## 4. The 4 Legendary Gen-1 Starters

At the dawn of any repository, the Trainer selects one of the 4 Gen-1 elemental starters:

```text
       [Nimbleet ⚡]       [Fortoise 💧]        [Monkin 🔥]         [Yagni 🍃]
       Electric Type        Water Type           Fire Type          Grass Type
      (Agile Router)     (Config Fortress)    (Iron Law TDD)     (Code Slasher)
```

1. **⚡ Nimbleet (No.001)** — *Electric Type*
   - Origin: `2JIHAN/jihan-harness`
   - Role: The lightning-fast scout. Ensures the agent’s permanent prompt is microscopic (<50 tokens) by routing tasks dynamically.
2. **💧 Fortoise (No.002)** — *Water Type*
   - Origin: `affaan-m/everything-claude-code`
   - Role: The impenetrable bastion. Employs 288 moves and an unyielding shell that physically blocks agents from weakening linter rules to cheat tests.
3. **🔥 Monkin (No.003)** — *Fire Type*
   - Origin: `obra/superpowers`
   - Role: The ascetic martial artist. Adheres to *The Iron Law*: burns away speculative fixes and symptom-patching, demanding automated proof before modifying production code.
4. **🍃 Yagni (No.004)** — *Grass Type*
   - Origin: `DietrichGebert/ponytail`
   - Role: The lazy genius sloth. Prunes speculative architecture, replaces bloated dependencies with native stdlib, and rewards negative line diffs (`-N lines`).

---

## 5. Evolution: Dual-Typing & Ascendance

As a repository matures from a prototype into a mission-critical system, its adopted Harnemon earns experience (EXP) from user corrections and closed learning loops.

When a Harnemon undergoes **Mega Evolution**, it gains a secondary elemental type to tackle complex engineering challenges:

- **Nimbleet [Electric ⚡] ➔ [Electric / Steel ⚡🛡️]**
  - Evolves from a simple speed router into a compile-time invariant enforcer (e.g., instant TypeScript/Rust compiler error healing).
- **Monkin [Fire 🔥] ➔ [Fire / Fighting 🔥🥊]**
  - Evolves from a unit-test purist into a high-throughput load and concurrency benchmark warrior.
- **Yagni [Grass 🍃] ➔ [Grass / Ice 🍃❄️]**
  - Evolves from a code slasher into an immutability master who freezes fragile code into pure, deterministic functional modules.

---

## 6. The Trainer's Creed: The 3 Invariants

A true Harnemon Trainer never compromises the 3 architectural invariants:

1. **Idempotency** — Repeated adoptions or executions never corrupt repository state.
2. **Auto-Wiring** — Every move and ability connects seamlessly with zero manual stitching.
3. **Zero Dependencies** — The Harnemon remains a nomadic entity, requiring zero external runtime baggage.
