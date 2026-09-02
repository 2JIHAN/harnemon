# Harnedex No.002: Fortoise — Water Type 💧
> **Archetype**: `affaan-m/everything-claude-code` | **Trait**: Config-Guard Shell (288-move fortress)

The archetypal fortress harness housing over 280 skills and defensive lifecycle hooks to strictly guard linter and formatter configurations.

---

## 1. Overview & Design Philosophy

- **Repository** — [github.com/affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code)
- **Core Motto** — "The Agentic OS & Performance Optimization System"
- **Design Philosophy** — A monolithic powerhouse packaging 280+ skills, 70 subagents, and 90 slash commands to transform the coding assistant into a full-spectrum engineering system.

---

## 2. Architecture Breakdown

```text
everything-claude-code/
├── agents/                          # 70+ role-specific subagent prompts (architect, reviewer, etc.)
├── commands/                        # 96+ user entry point slash commands (/tdd, /plan, /e2e, etc.)
├── skills/                          # 288+ comprehensive on-demand domain playbooks
├── rules/                           # Modular rules across 25 language/framework stacks
├── hooks/
│   └── hooks.json                   # Interception map for PreToolUse, PostToolUse, Stop
├── scripts/hooks/                   # Node.js runtime hook implementations
│   ├── config-protection.js         # • Blocks weakening of linter/formatter configs
│   ├── stop-format-typecheck.js     # • Batched formatting & tsc at Stop event
│   └── check-console-log.js         # • Residual debug logging warning
└── scaffolds/                       # Multi-agent setups (.claude, .cursor, .codex)
```

---

## 3. Key Innovative Mechanisms

### 1. Runtime Lifecycle Hooks
- Intercepts tool calls immediately prior to execution (`PreToolUse`) and upon model turn completion (`Stop`).
- **`config-protection`** — Cancels tool execution (`exit 2`) if the agent attempts to modify `.eslintrc`, `.prettierrc`, or `biome.json` to bypass linting errors.
- **Batched Formatting & Typechecking** — Executes formatting (Biome/Prettier) and `tsc --noEmit` only once during the `Stop` event on touched files, avoiding per-file turn latency.

### 2. Modular Language Stack Isolation
- Separates rules by stack (`rules/typescript/`, `rules/python/`, `rules/golang/`) to dynamically mount only relevant language constraints.

---

## 4. Architectural Analysis

### Strengths (Takeaways)
- **Configuration Defense** — Eliminates agent corner-cutting (disabling linters) via system-level physical blocking.
- **Batched Execution Optimization** — Defers expensive formatting and typechecking to turn boundaries.
- **Security Baseline** — Comprehensive protections against prompt injection, zero-width unicode exploits, and secret leakage.

### Trade-offs & Anti-patterns
- **Extreme Bloat** — 288 skills and massive package dependencies make whole-repo comprehension difficult.
- **Heavy Node.js Dependency** — Running runtime hooks via Node.js introduces environment fragility.
- **Setup Complexity** — Fragmented manual installation steps violate zero-dependency idempotency.

---

## 5. Recommended For

- Large enterprise teams requiring fine-grained lifecycle audits.
- Complex multi-language codebases deeply coupled with the Claude Code ecosystem.
