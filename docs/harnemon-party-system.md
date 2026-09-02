# Harnemon Multi-Party System

Defines the multi-Harnemon architecture that enables assembling a **team of up to 6 specialized Harnemons in a single workspace**, dynamically switching the active lead partner or delegating sub-tasks to specialist party members.

---

## 🌟 Core Concept: Multi-Party Division of Labor

```text
       ┌──────────────────────────────────────────────────────────────┐
       │   🐾 PROJECT HARNEMON PARTY (.harnemons/)                    │
       │   ├── ⚡ Nimbleet  (Active Lead: 50-token ultralight router)  │
       │   ├── 🔥 Monkin    (Specialist: The Iron Law root-cause TDD) │
       │   ├── 🍃 Yagni     (Specialist: Complexity slasher -N lines) │
       │   └── 💧 Fortoise  (Specialist: Configuration & lint guard)  │
       └──────────────────────────────────────────────────────────────┘
```

- **Active Lead** — Leads general turn interactions and coding tasks, signing turns with its unique signature (`-Harnemon {Name} {Emoji}-`).
- **Party Members** — Specialized teammates activated on-demand during dedicated phases (debugging, refactoring, security audits) via `switch` or subagent delegation.

---

## 🛠️ Party Management CLI Commands

### 1. Adopt & Recruit Party Members (`adopt`)
Adopting a first partner or recruiting additional specialists is handled via the unified **`harnemon adopt`** command:
```bash
# Adopt initial partner (automatically set as Active Lead):
harnemon adopt nimbleet

# Recruit additional specialist Harnemons into the existing party:
harnemon adopt monkin     # Monkin 🔥 (Debugging & root-cause discipline)
harnemon adopt yagni      # Yagni 🍃 (Complexity reduction & dead code pruning)
```

### 2. Inspect Party Roster (`party`)
View all recruited Harnemons and check the currently active lead:
```bash
harnemon party
```

### 3. Switch Active Lead (`switch`)
Instantly switch the active lead to tailor turn signatures and primary focus to the task at hand:
```bash
# Switch to Monkin for intensive debugging sessions:
harnemon switch monkin
# ➔ Subsequent turns signed with: -Harnemon Monkin 🔥-

# Switch to Yagni for major refactoring & pruning:
harnemon switch yagni
# ➔ Subsequent turns signed with: -Harnemon Yagni 🍃-
```

### 4. Dismiss Party Member (`dismiss`)
Remove a specialist who is no longer needed from the workspace party:
```bash
harnemon dismiss fortoise
```

---

## 🔒 Party System Invariants

1. **Physical Isolation** — Each Harnemon maintains its independent 3 pillars (Rules, Skills, Memory) under `.harnemons/<species>/`.
2. **Aggregated Skills Exposure** — All active party members have their individual skills linked into `.agents/skills/`, exposing the entire party's skillset to the IDE native registry simultaneously.
3. **Zero-Dependency Switching** — Party assembly, recruitment, and switching operate in <10ms via pure POSIX Bash.
