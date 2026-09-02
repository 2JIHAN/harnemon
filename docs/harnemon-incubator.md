# Harnemon Incubator & Hatching System

Defines the incubation mechanics of starting from a **Blank Egg 🥚** with zero pre-packaged rules, absorbing developer conventions across pair-programming sessions, and graduating into a mature, custom Harnemon species.

---

## 🌟 Core Philosophy: From Blank Egg to Mature Species

```text
       ┌──────────────────────────────────────────────────────────────┐
       │   🥚 1. EGG (Incubation Stage)                               │
       │   `harnemon incubate` (Lightweight 30-token engine only)     │
       └──────────────────────────────────────────────────────────────┘
                                       │
                    2-Correction Loop  │  (Absorb feedback & conventions)
                                       ▼
       ┌──────────────────────────────────────────────────────────────┐
       │   🌱 2. INCUBATING (Growth & EXP Accumulation)                │
       │   Synthesizes Rule/Skill/Hook pillars, raising Readiness (%) │
       └──────────────────────────────────────────────────────────────┘
                                       │
                    harnemon hatch     │  (Name & graduate species)
                                       ▼
       ┌──────────────────────────────────────────────────────────────┐
       │   🐣 3. HATCHED SPECIES (Registration & Adoption)            │
       │   .harnemons/<species>/ ➔ Deployable across global Harnedex  │
       └──────────────────────────────────────────────────────────────┘
```

---

## 🏛️ 1. Internal Structure of an Egg

An Egg is a **zero-base template** containing only incubation kernels without pre-packaged conventions. Rules, language constraints, and workflows are promoted to `rules/` only after real-world developer feedback:

- **Incubation Kernel (`rules/incubation-kernel.md`)** — Real-time detection of user corrections and formatting preferences.
- **Self-Evolution Rule (`rules/harness-evolution.md`)** — Promotes repeated feedback to Rules, Skills, or Hooks.
- **Episodic Ledger (`memory/episodes/YYYY-MM-DD.md`)** — Append-only timeline of observations and conventions. Past entries are never modified.

---

## ⚡ 2. Operational Workflow

### Step 1: Incubate a Blank Egg
Spawn an egg in a new or existing repository:
```bash
harnemon incubate
```

### Step 2: Pair Program Naturally
Code and collaborate as usual. When giving feedback or setting project standards, record observations:
```bash
harnemon note "Run pnpm build before deploy to catch type errors"
harnemon note "Use native fetch instead of axios" --type convention
```
Entries are append-only. When the same feedback pattern repeats 2+ times, it graduates into the 3 pillars.

Hatch readiness is calculated from evidence and promotions (Episodes up to 40%, learned rules 40%, learned skills 20%). **Logging alone cannot hatch an egg without rule/skill graduation.**
```bash
harnemon status
```

### Step 3: Hatch into a New Species
Once readiness reaches 60%, assign a unique species name and element to officially hatch:
```bash
harnemon hatch "Supabird" --type "Database ⚡" --desc "Supabase RLS & Edge Function Master"
```
Hatching executes a **one-time distillation**: accumulated episodes are deduplicated into `memory/MEMORY.md` with source traceability tags (`<!-- id:m-0001 ... -->`). Raw episodes remain preserved as an audit trail. The temporary incubation kernel is removed and replaced with a mature Harnemon instance.

### Step 4: Memory Maintenance & Dreaming
Mature species maintain open episodic logs. Regular grooming is handled via resting:
```bash
harnemon rest
```
Identifies entries already promoted to rules, duplicate observations, or unreferenced claims. Run `harnemon rest --apply` to apply proposals; retired items are archived in `memory/retired.md`.

When referencing specific memories in work: `harnemon rest --cite m-0001`. Citation history serves as the primary metric for active memory relevance.

### Step 5: Global Harnedex Registration
Registering the hatched species to the global belt enables immediate adoption across any repository:
```bash
harnemon register
```
Adopt the newly registered species in other workspaces:
```bash
harnemon adopt supabird
```

---

## 🔒 3. Incubator Invariants

1. **Zero Prompt Bloat** — Always-on rules remain under 60 tokens during incubation to avoid degrading coding performance.
2. **Strict 3-Pillar Separation** — Learned knowledge strictly categorizes into Always-on Rules, On-demand Skills, or Deterministic Gates.
3. **Perpetual Idempotency** — `incubate`, `hatch`, and `register` operations execute idempotently via pure POSIX Bash.
