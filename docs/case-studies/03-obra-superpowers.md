# Harnedex No.003: Monkin — Fire Type 🔥
> **Archetype**: `obra/superpowers` | **Trait**: The Iron Law Crucible (Strict 4-step debugging)

The archetypal rigorous discipline harness that burns away symptom-patching and mandates root-cause investigation and reproducible test proofs before permitting code changes.

---

## 1. Overview & Design Philosophy

- **Repository** — [github.com/obra/superpowers](https://github.com/obra/superpowers)
- **Core Motto** — "No fixes without root-cause investigation first"
- **Design Philosophy** — A procedure-driven framework designed to prevent "guess-and-check thrashing" by strictly bounding the agent within phased execution protocols.

---

## 2. Architecture Breakdown

```text
superpowers/
├── skills/
│   ├── systematic-debugging/        # • 4-phase root-cause first debugging
│   │   ├── SKILL.md                 # • Core directive (The Iron Law)
│   │   └── references/              # • Contextual debugging playbooks
│   ├── test-driven-development/     # • Enforces Red-Green-Refactor TDD loop
│   ├── verification-before-completion/ # • Evidence-based verification before done
│   └── architecture-decision-records/ # • Structured ADR documentation skill
└── commands/                        # Slash command entry points
```

---

## 3. Key Innovative Mechanisms

### 1. The Iron Law of Debugging
- **Core Law** — **"NO fixes without root-cause investigation first."**
- **4-Phase Mandatory Procedure**:
  1. **Phase 1 (Investigation)** — Reproduce the bug, trace stack calls, write a failing automated test case.
  2. **Phase 2 (Hypothesis Testing)** — Alter only one variable at a time; reject unverified guesses.
  3. **Phase 3 (Minimal Fix)** — Forbid symptom patches (e.g. premature null guards); address root architectural faults.
  4. **Phase 4 (Regression Verification)** — Verify complete test suite pass and retain regression guards.

### 2. Blocking Symptom Patching
- Explicitly forbids the common AI failure mode of wrapping faulty code in ad-hoc defensive conditionals to silence errors, preventing long-term codebase rot.

---

## 4. Architectural Analysis

### Strengths (Takeaways)
- **Quality & Reliability** — Eradicates destructive guessing and unintended side-effects.
- **TDD Internalization** — Requires creating failing test reproductions before modifying source code.

### Trade-offs & Anti-patterns
- **Token Inefficiency in Static Context** — Storing extensive debugging manuals in always-on prompts wastes tokens; requires dynamic on-demand routing.

---

## 5. Recommended For

- Mission-critical backend, financial, and core infrastructure systems.
- Codebases requiring strict regression testing and zero-guesswork debugging.
