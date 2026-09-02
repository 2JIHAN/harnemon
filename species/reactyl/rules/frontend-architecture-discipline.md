---
name: frontend-architecture-discipline
description: Always-on frontend feature constraints. Enforces feature-sliced structure, unidirectional imports, server/client boundary discipline, status-union async state, and role-first integration tests.
---

# Frontend Architecture Discipline (frontend-architecture-discipline.md)

Binding constraints for every component, hook, route and frontend test you write.

## 1. Feature-Sliced Structure

- **Features own their code** — Every unit of functionality lives under `src/features/<feature>/` with only the subfolders it actually needs (`api`, `components`, `hooks`, `stores`, `types`, `utils`). Do not create empty scaffolding folders.
- **Unidirectional imports** — Flow is `shared → features → app`. A feature never imports from another feature; shared code never imports from a feature. Cross-feature needs are lifted into `shared` or composed at the app layer.
- **No `containers/` split** — Never emit `XContainer` / `XView` pairs. Extract stateful and data-fetching logic into a `useX` hook the component calls directly.

## 2. Server and Client Boundary

- **Push `'use client'` to the leaves** — Mark the smallest interactive component. Never place the directive on a layout or page, which drags its entire import graph into the browser bundle.
- **Every `'use server'` export is a public unauthenticated endpoint** — Inside each server function, in this order: parse and validate every argument with a schema (`safeParse`), then authenticate, then authorize the specific resource, and only then touch data. Never trust an argument because the only caller is your own form.
- **Segments are explicit** — A folder becomes a public URL only when it contains `page.tsx` or `route.ts`. Colocate components, hooks, queries and tests inside the segment; use route groups to organize without affecting the URL.
- **Read the version-matched docs** — Before writing framework-specific code, consult the docs bundled in the installed package rather than recalling API shapes from memory.

## 3. State

- **Server state and client state are different things** — Data owned by the server lives in a query cache with a stable key factory. Never mirror fetched data into `useState` and never hand-synchronize the two.
- **Status unions, never loading booleans** — Model async state as one string union (`'idle' | 'pending' | 'resolved' | 'rejected'`), never as two or more independent boolean flags that can contradict each other.
- **One global store, sliced** — Keep a single global store split into slice creators. Update only through the setter API; never mutate store state directly.
- **Derive, do not duplicate** — Compute values from existing state during render. A piece of state that can be derived is a bug waiting to desynchronize.

## 4. Forms and Validation

- **One schema, both sides** — Define the validation schema once and use it for client-side form validation and for server-side argument parsing. A client-only check is a convenience, never a guarantee.
- **Accessible by construction** — Every input has a programmatically associated label, and every error message is linked to its field and announced.

## 5. Testing

- **Mostly integration** — Default every new test to the integration layer: render the real component tree with real children, real router and real store, mocking only the network boundary.
- **Query priority is fixed** — Select elements in this order, stopping at the first that works: `getByRole` (with the `name` option), `getByLabelText`, `getByPlaceholderText`, `getByText`, `getByDisplayValue`. Reach for a test id only when no accessible query can express the intent.
- **Assert only observable behavior** — Rendered text, roles, accessible names, visible state, and the callbacks a parent receives. Never assert on internal component state, instance methods, or implementation-only props.
- **Real user events** — Open every interaction test with `const user = userEvent.setup()` before `render()`, and `await` every `user.*` call. Use low-level event firing only for events a real user cannot produce.
- **Unhandled requests fail loudly** — Configure the network mock with `onUnhandledRequest: 'error'` so a request without a handler fails the test instead of escaping to the real network.
- **No arbitrary waits** — Wait on a condition or a web-first assertion. A fixed sleep in a test is a defect, not a stabilization.

## 6. Performance

- **Measure before optimizing** — Do not add memoization, code splitting or virtualization without a profile or a bundle report showing the cost.
- **Budget the bundle** — Every route has a size budget. A change that exceeds it is either justified in the same change or reverted.
