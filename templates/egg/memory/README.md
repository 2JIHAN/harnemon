# Memory

A Harnemon remembers in two layers, whether it is still an egg or already hatched.

## episodes/

`episodes/YYYY-MM-DD.md` holds what actually happened, one line per observation:

```
- [correction] 2026-08-28T08:12:03Z :: Always run pnpm build before deploying
```

Written by `harnemon note "<text>" [--type correction|convention|decision]`.

**Append only.** Past entries are never rewritten. This log is the evidence a
hatch is judged on, and the record every later distillation is checked against.
A hatched species keeps writing to it: the ledger is how a mature partner stays
accountable to what it was actually taught.

## MEMORY.md

Distilled from the episodes above, written at hatch or on the first
`harnemon rest` of a mature partner. Each entry keeps a pointer back to the
episode it came from, so a claim can always be traced to the moment it was
learned. Tended afterwards by `harnemon rest`.
