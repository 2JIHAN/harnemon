# Harnedex No.004: Yagni — Grass Type 🍃
> **Archetype**: `DietrichGebert/ponytail` | **Trait**: Ladder of Laziness (Complexity slasher & pruner)

The archetypal minimalist diet harness that prunes dead code branches, slashes unneeded dependencies, and compresses implementation down to the shortest solution that actually works.

---

## 1. Overview & Design Philosophy

- **Repository** — [github.com/DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)
- **Core Motto** — "The simplest solution that actually works"
- **Design Philosophy** — Forbids speculative abstractions and gratuitous dependencies, forcing the AI to reach for the standard library (stdlib) and high-density, concise expressions.

---

## 2. Architecture Breakdown

```text
ponytail/
├── skills/
│   ├── ponytail/                    # • Ladder of Laziness (YAGNI → Reuse → Stdlib → Native → 1-Line)
│   ├── ponytail-review/             # • Diff-focused over-engineering reviewer
│   ├── ponytail-audit/              # • Whole-repo complexity scan & ranking report
│   └── ponytail-debt/               # • Deliberate shortcut (# ponytail:) ledger harvester
└── benchmarks/                      # Line-count and token-reduction benchmarks
```

---

## 3. Key Innovative Mechanisms

### 1. The Ladder of Laziness
Before writing code, mandates climbing a 5-step ladder to guarantee the simplest possible implementation:
1. **YAGNI** — Does this code need to exist right now? If not, do not write it.
2. **Reuse** — Reuse existing helper functions already present in the codebase.
3. **Stdlib** — Exhaust standard library capabilities before introducing external packages (npm/pip).
4. **Native Platform** — Use native runtime features (e.g. `Intl.DateTimeFormat`, `fetch`).
5. **One Line over Fifty** — Prefer dense, readable standard expressions over multi-line class boilerplate.

### 2. Complexity Review Tagging (`ponytail-review`)
- Reviews diffs specifically to identify **what to delete**.
- Tag format: `L30-44: shrink: manual dictionary build loop. Shorten to dict(zip(k, v)).`
- Concluding metric: `net: -34 lines possible.` (Negative line count is the gold standard for PRs).

### 3. Shortcut Debt Harvester (`ponytail-debt`)
- Tracks deliberate shortcuts via `# ponytail: <constraint>, <trigger>` comments, harvesting them via ripgrep so deferred work never rots into forgotten tech debt.

---

## 4. Architectural Analysis

### Strengths (Takeaways)
- **Anti-Bloat** — Suppresses speculative AI boilerplate and needless architectural layers at the source.
- **Maintainability through Simplicity** — Shorter code with fewer dependencies drastically reduces the defect surface area.
- **Measurable Value** — Evaluates engineering leverage through net negative lines (`-N lines`).

---

## 5. Recommended For

- Legacy refactoring initiatives and technical debt paydowns.
- Security-sensitive environments requiring strict minimal dependency graphs.
- Lean startups moving rapidly through MVP validation cycles.
