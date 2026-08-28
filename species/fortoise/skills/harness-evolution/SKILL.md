---
name: harness-evolution
description: Comprehensive playbook for AI agents to inspect, refactor, prune, and evolve their own harness (Rules, Skills, Hooks). Use when auditing or improving project harnesses.
---

# Harness Evolution Playbook (SKILL.md)

This playbook guides an AI agent when auditing, refactoring, expanding, or pruning its own harness structure.

## When to Use

- User says "하네스 점검해봐", "하네스 개선해줘", "audit our harness", or invokes `/mhm-evolve`
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

## 2. Refactoring a Bloated Rule (Skill Router Decomposition)

When a rule file in `rules/` exceeds 100 lines:
1. Extract the detailed examples, edge cases, and procedural steps into `skills/<topic>/SKILL.md`.
2. Reduce the rule file to a 3-5 line traffic cop pointing to the skill:
   ```markdown
   ## Trigger Condition
   - **Mandatory Skill**: `.agents/skills/<topic>/SKILL.md`
   - **When**: <Condition>
   - **Directives**: <1-2 bullet points of core non-negotiables>
   ```
3. Verify with `mhm audit` that the rule is now < 50 lines.

---

## 3. The Pattern Promotion Workflow

When the user gives the same architectural guidance or correction twice:
1. **Identify the Scope**: Is this repo-specific or team-wide?
2. **Draft the Minimal Diff**:
   - Prefer modifying an existing skill/rule before creating a new file.
   - Use the shortest working phrasing (Ponytail principle).
3. **Confirm with User**:
   - Present the exact location and 1-line summary of what will be added.
   - Request approval before writing.
4. **Deploy, Index & Wire**:
   - Write `skills/<name>/SKILL.md` (with complete YAML frontmatter).
   - Append 1 line to `skills/INDEX.md` catalog (name, trigger, description) to eliminate dark skills.
   - Ensure auto-wiring in `AGENTS.md` and `CLAUDE.md` remains intact.

---

## 4. Harness Audit Checklist

Before declaring a harness evolution complete, verify:
- [ ] No rule in `rules/` exceeds 100 lines.
- [ ] Every skill in `skills/` has valid YAML frontmatter (`name`, `description`).
- [ ] Every hook in `hooks/` is executable (`chmod +x`) and exits 0 for benign cases.
- [ ] The 3 Invariants hold:
  - **Idempotent**: running `install.sh` twice produces zero diff.
  - **Auto-wired**: new rules are referenced in `.agents/AGENTS.md`.
  - **Zero-dependency**: no unneeded npm/pip packages required for hook execution.
