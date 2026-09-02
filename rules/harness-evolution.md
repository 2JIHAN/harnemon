---
name: harness-evolution
description: Continuous self-evolution directive for AI agents. Governs autonomous episodic logging, in-session distillation, semantic knowledge extraction, write routing decision trees, and 3-occurrence promotion.
---

# Harness Self-Evolution Protocol (harness-evolution.md)

You must never passively consume your harness (Rules, Skills, Memory). You are actively responsible for **autonomously logging, distilling, and evolving your own harness** based on observations, conventions, and user feedback throughout active sessions.

## 1. Memory Write Routing Decision Tree

When encountering new information, user corrections, or domain discoveries during active sessions, follow this decision tree:

1. **Is the information durable beyond the current session?**
   - **No** ➔ Keep it ephemeral in turn context; do NOT write to durable memory.
   - **Yes** ➔ Proceed to Step 2.

2. **Is it event-like, an immediate observation, or a work-in-progress signal?**
   - **Yes** ➔ Append to today's episodic ledger: `memory/episodes/YYYY-MM-DD.md`.
   - **No** (Direct domain fact or policy) ➔ Proceed to Step 3.

3. **Did the observation establish or modify a durable domain policy, architecture, or entity understanding?**
   - **Yes** ➔ Update or create the primary topic document: `memory/semantic/<topic>.md`.
     - **Write Shape**:
       - `Frontmatter`: Topic metadata (`topic`, `domain`).
       - `## Current`: Concise, up-to-date factual state (rewritten only when understanding changes).
       - `## History`: Append-only chronological trail referencing source episodes (`src: episodes/YYYY-MM-DD.md`).
     - **Index**: Register a 1-line summary in `memory/semantic/INDEX.md`.
   - **No** ➔ Retain as raw episode in `memory/episodes/`.

4. **Is the knowledge globally critical to default agent behavior at session start across multiple tasks?**
   - **Yes** ➔ Distill into `memory/MEMORY.md` (keep strictly under 100 lines, with tracking tag `<!-- id:m-0001 ... -->`).
   - **No** ➔ Keep in `memory/semantic/<topic>.md` (retrieved on-demand only).

5. **Has a convention, constraint, or playbook repeated 3+ times?**
   - **Constraints (<50 lines)** ➔ Promote to `rules/<name>.md`.
   - **Playbooks (>50 lines)** ➔ Promote to `skills/<name>/SKILL.md` + register in `skills/INDEX.md`.
   - **Retire**: Prune promoted items from `MEMORY.md` into `memory/retired.md`.

## 2. In-Session Episodic Timeline Logging

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

## 3. Semantic Domain Knowledge Management (Semantic Memory)

- **Definition & Target**: Thematic, structured, evergreen knowledge documents organized by entity, business policy, or system architecture (`memory/semantic/<topic>.md`).
- **Standard Format (`Current` + `History`)**:
  ```markdown
  ---
  topic: <topic-slug>
  domain: <domain-or-scope>
  ---

  # <Topic Title>

  ## Current
  - <Concise bullet points of current facts, active policies, or architecture design>

  ## History
  - YYYY-MM-DD: <Summary of change or observation> (src: episodes/YYYY-MM-DD.md)
  ```
- **Operational Principle (L2 On-Demand Recall)**:
  - Conserve L1 always-on tokens by not loading full topic documents into initial system context. The agent inspects `memory/semantic/INDEX.md` and consults relevant topic files on-demand.

## 4. Autonomous Core Memory Distillation (In-Session Distillation)

- **Distillation Timing**: Immediately after writing new episodic entries or completing a milestone.
- **Target File**: `memory/MEMORY.md` (L1 Resident Memory).
- **Rules**:
  - Extract repeating patterns, architecture decisions, and conventions from daily episodes, merging duplicate points.
  - Retain source traceability tags (`<!-- id:m-0001 born:YYYY-MM-DD src:episodes/... -->`) on every distilled item.
  - Strictly maintain file length **under 100 lines** to prevent prompt bloat.

## 5. Zero-Fluff Discipline & Integrity

- **100-Line Limit**: Always-on rules in `rules/*.md` and `memory/MEMORY.md` must stay dense and under 100 lines.
- **Fluff Elimination**: Immediately delete obsolete legacy rules, duplicate entries, and tombstone comments.
- **Documentation i18n**: When creating or updating public documentation and READMEs, synchronize across all 4 languages (EN, KO, JA, ZH).
