## 📝 Summary of Changes

<!-- Provide a brief explanation of what this PR does and why. -->

## 🔗 Related Issues

<!-- Fixes #123, Closes #456 -->

## 🏛️ 3-Invariants Checklist

- [ ] **Zero-Dependency**: No npm, pip, cargo or foreign packages added to core harness.
- [ ] **Idempotency**: Scripts can be run repeatedly without duplicating or corrupting state.
- [ ] **Auto-Wiring**: Rules and skills are properly linked into `.agents/AGENTS.md` and client configs.

## 🧪 Testing Performed

- [ ] Ran `bash -n bin/harnemon` (Syntax check passed)
- [ ] Ran `./bin/harnemon status` and `./bin/harnemon audit`
- [ ] Tested on target operating system (macOS / Linux)
