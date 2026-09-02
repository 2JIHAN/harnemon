---
name: harness-evolution
description: Continuous self-evolution directive for AI agents. Governs autonomous episodic logging, in-session distillation, semantic knowledge extraction, and 3-occurrence promotion to rules and skills.
---

# Harness Self-Evolution Protocol (harness-evolution.md)

You must never passively consume your harness (Rules, Skills, Memory). You are actively responsible for **autonomously logging, distilling, and evolving your own harness** based on observations, conventions, and user feedback throughout active sessions.

## 1. In-Session Episodic Timeline Logging

- **Mid-Session Triggers (Do NOT defer to session end)**:
  1. Completion of a major task or milestone.
  2. Transition of conversational context or domain topic.
  3. Accumulation of 3+ unrecorded observations, conventions, or decisions.
- **Target File**: Today's `memory/episodes/YYYY-MM-DD.md` (daily timeline log, Append-only).
- **Episode Format**:
  ```markdown
  HH:MM - <Event / Policy / Task Title>
  <Concrete description of what occurred, context, policies, decisions, or user corrections>

  Reference: <Session ID, file path, API reference, or context link>
  ```

## 2. Semantic Domain Knowledge Management (Semantic Memory)

- **Definition & Target**: Thematic, structured, evergreen knowledge documents organized by entity, business policy, or system architecture (`memory/semantic/<topic>.md`).
- **Extraction & Update Triggers**:
  - When deep domain knowledge (service policies, pricing models, integration specs, infrastructure setups) is discovered during work.
  - Rather than letting knowledge remain buried in transient daily episodes, create or update the dedicated topic document (`memory/semantic/<topic>.md`) as a living document.
- **Operational Principle (L2 On-Demand Recall)**:
  - Conserve L1 always-on tokens by not loading full topic documents into initial system context. The agent inspects `memory/semantic/INDEX.md` and consults relevant topic files on-demand.

## 3. Autonomous Core Memory Distillation (In-Session Distillation)

- **Distillation Timing**: Immediately after writing new episodic entries or completing a milestone.
- **Target File**: `memory/MEMORY.md` (L1 Resident Memory).
- **Rules**:
  - Extract repeating patterns, architecture decisions, and conventions from daily episodes, merging duplicate points.
  - Retain source traceability tags (`<!-- id:m-0001 born:YYYY-MM-DD src:episodes/... -->`) on every distilled item.
  - Strictly maintain file length **under 100 lines** to prevent prompt bloat.

## 4. 3-Occurrence Autonomous Promotion

- **Trigger**: When the same correction, convention, or pattern occurs **3 or more times**, or when an immutable policy is confirmed.
- **Promotion Branches**:
  - **Always-on Cognitive Constraints (<50 lines)** ➔ Promote to `rules/<name>.md` (e.g. coding invariants, output formats).
  - **Procedural Playbooks & Manuals (>50 lines)** ➔ Create `skills/<name>/SKILL.md` and register 1 line in `skills/INDEX.md`.
  - **Absolute Binary Gates** ➔ Enforce via physical Git pre-commit gates.
- **Retirement**: Items fully promoted to Rules or Skills must be pruned from `MEMORY.md` and archived in `memory/retired.md`.

## 5. Zero-Fluff Discipline & Integrity

- **100-Line Limit**: Always-on rules in `rules/*.md` and `memory/MEMORY.md` must stay dense and under 100 lines.
- **Fluff Elimination**: Immediately delete obsolete legacy rules, duplicate entries, and tombstone comments.
- **Documentation i18n**: When creating or updating public documentation and READMEs, synchronize across all 4 languages (EN, KO, JA, ZH).
