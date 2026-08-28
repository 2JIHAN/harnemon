# Contributing to Harnemon ⚡

Thank you for your interest in contributing to **Harnemon**!

Harnemon is an open-source, zero-dependency autonomous harness companion ecosystem built for modern AI coding agents. We welcome contributions of all kinds: bug fixes, documentation improvements, new CLI features, and **new Harnemon Species submissions to the Harnedex**!

---

## 🏛️ The 3 Invariants (Non-Negotiable Rules)

Every contribution must strictly adhere to the 3 Invariants:

1. **Zero-Dependency Footprint**:
   - Harnemon CLI and hooks must run purely on standard POSIX Bash and Git.
   - Never add runtime dependencies (npm, pip, cargo, etc.) to the core harness.
2. **Idempotency**:
   - Running any installer or CLI command 1 time or 100 times must produce the exact same deterministic state.
3. **Auto-Wiring Integrity**:
   - New rules or skills must automatically connect into `.agents/AGENTS.md`, `.claude/`, and `.gemini/`.

---

## 🐾 How to Submit a New Harnemon Species (Harnedex Entry)

Have you trained or incubated an awesome custom Harnemon in your project? Share it with the community!

1. Breed or hatch your species:
   ```bash
   harnemon incubate
   # ...code and train...
   harnemon hatch "YourSpecies" --type "Rust 🦀" --desc "Description"
   ```
2. Place your species case study in `docs/case-studies/0N-species-name.md`.
3. Add a starter blueprint to `catalog/<species-name>/` or `skills/`.
4. Open a Pull Request using the **Species Submission** template!

---

## 🛠️ Local Development & Testing

1. Clone the repository:
   ```bash
   git clone https://github.com/2JIHAN/harnemon.git
   cd harnemon
   ```
2. Run the test suite:
   ```bash
   ./bin/harnemon audit .
   bash -n bin/harnemon
   ```

---

## 📬 Pull Request Workflow

1. Fork the repo and create a feature branch (`git checkout -b feat/my-awesome-feature`).
2. Write clean, self-documenting code.
3. Commit with semantic commit messages (`feat: ...`, `fix: ...`, `docs: ...`).
4. Submit your PR and ensure CI passes!
