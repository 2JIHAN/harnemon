---
name: harness-evolution
description: Comprehensive playbook for AI agents to inspect, refactor, prune, and evolve their own harness (Rules, Skills, Hooks). Use when auditing or improving project harnesses.
---

# Harness Evolution Playbook (SKILL.md)

This playbook guides an AI agent when auditing, refactoring, expanding, or pruning its own harness structure.

## When to Use

- User says "하네스 점검해봐", "하네스 개선해줘", "audit our harness", or invokes `/harness-evolution`
- You have captured a recurring convention or correction and are ready to codify it
- An existing rule has grown beyond 100 lines and needs to be decomposed into the Skill Router pattern
- Running a self-health check on your rules, skills, and hooks

---

## 1. The Decision Matrix (Where Does This Belong?)

When codifying a new behavior, strictly classify it into one of the 3 Pillars:

| Question | Destination | Example |
| :--- | :--- | :--- |
| Must the agent be aware of this in **EVERY SINGLE TURN**? | **Rule** (`rules/<name>.md`) | Language standard, visual response format, execution protocol |
| Is this a deep manual needed only for **SPECIFIC TASKS**? | **Skill** (`skills/<name>/SKILL.md`) | TDD procedure, E2E testing guide, domain migration guide |
| Can this be deterministically enforced with **EXIT 0 / EXIT 1**? | **Hook** (`hooks/<name>/`) | Commit message length, secret leak block, linter config lock |

---

## 2. Wiring a New Rule, Skill, or Hook

The harness lives in `.harnemons/<species>/`. Harnemon writes every wiring it owns into `.agents/AGENTS.md` between HTML comment markers, `<!-- harnemon:<id>:begin v<version> -->` through `<!-- harnemon:<id>:end -->`. A regeneration rewrites only the block carrying that marker, so hand-written prose in the same file survives untouched. The managed ids are `partner`, `rules`, `party`, `skills`, and `hooks`, plus `awareness` in the global `~/.agents/AGENTS.md`.

- **Rule** — Place the file at `.harnemons/<species>/rules/<name>.md`, then run `harnemon update` to regenerate the `rules` block from the directory listing. To wire by hand instead, add `@../.harnemons/<species>/rules/<name>.md` inside the `rules` block and keep the list alphabetical, so the next regeneration produces zero diff.
- **Skill** — Place the directory at `.harnemons/<species>/skills/<name>/SKILL.md` with complete YAML frontmatter (`name`, `description`). No block entry is required: `.claude/skills` and `.agents/skills` are symlinks to the species skills directory, so agents discover the skill on the next session.
- **Hook** — Place the gate at `.harnemons/<species>/hooks/<git-hook-name>/`, and the `hooks` block lists it on the next regeneration. Enforcement comes from the copy installed into `.git/hooks/`, never from the markdown listing.
- **Catalog** — Append one line to `skills/INDEX.md` to eliminate dark skills. Its links resolve relative to `INDEX.md` itself, which already sits inside `skills/`, so write `<name>/SKILL.md` and never `skills/<name>/SKILL.md`.

Never treat text outside a marker as wiring, and never delete a marker pair to remove wiring: the next regeneration simply appends a fresh block at the end of the file. Remove the underlying rule, skill, or hook instead.

---

## 3. Refactoring a Bloated Rule (Skill Router Decomposition)

When a rule file in `rules/` exceeds 100 lines:
1. Extract the detailed examples, edge cases, and procedural steps into `skills/<topic>/SKILL.md`.
2. Reduce the rule file to a 3-5 line traffic cop pointing to the skill:
   ```markdown
   ## Trigger Condition
   - **Mandatory Skill**: `.agents/skills/<topic>/SKILL.md`
   - **When**: <Condition>
   - **Directives**: <1-2 bullet points of core non-negotiables>
   ```
3. Verify with `harnemon audit` that the rule is now < 50 lines.

---

## 4. The Pattern Promotion Workflow

When the user gives the same architectural guidance or correction twice:
1. **Identify the Scope**: Is this repo-specific or team-wide?
2. **Draft the Minimal Diff**:
   - Prefer modifying an existing skill/rule before creating a new file.
   - Use the shortest working phrasing (Ponytail principle).
3. **Confirm with User**:
   - Present the exact location and 1-line summary of what will be added.
   - Request approval before writing.
4. **Deploy, Index & Wire**: Follow section 2. Never hand-edit `.agents/AGENTS.md` as a source of truth, because `harnemon update` regenerates it from the `rules/` directory.

---

## 5. Harness Audit Checklist

Before declaring a harness evolution complete, verify:
- [ ] No rule in `rules/` exceeds 100 lines.
- [ ] Every skill in `skills/` has valid YAML frontmatter (`name`, `description`).
- [ ] Every hook in `hooks/` is executable (`chmod +x`) and exits 0 for benign cases.
- [ ] The 3 Invariants hold:
  - **Idempotent**: running `harnemon update` twice produces zero diff.
  - **Auto-wired**: new rules are referenced inside the `harnemon:rules` block of `.agents/AGENTS.md`.
  - **Zero-dependency**: no unneeded npm/pip packages required for hook execution.
