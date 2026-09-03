---
name: frontend-discipline
description: Binding frontend constraints for design and implementation. Load before writing any screen, component, hook, stylesheet, route or frontend test. Covers token-only styling, the 4pt grid, 12-step semantic color, WCAG 2.2 ship blockers, feature-sliced structure, server/client boundaries, status-union async state, and role-first integration tests.
---

# Frontend Discipline (frontend-discipline)

Pixwing의 서명 규율입니다. 이 문서의 항목들은 취향이 아니라 출시 차단 기준입니다. 앞의 다섯 절은 화면이 어떻게 보여야 하는지를 정하고, 뒤의 여섯 절은 그 화면이 어떤 코드로 만들어져야 하는지를 정합니다.

# Part A — 디자인 시스템 (Design System)

## 1. Token-Only Styling

- **No raw values in component CSS** — Color, spacing, radius, shadow, z-index, font-size and font-family come from a token or a scale variable. A literal hex, a bare `px` spacing value, or an ad-hoc `rgba()` in component code is a defect.
- **Tokens carry meaning, not appearance** — Name a token by its role (`--color-surface-raised`, `--space-4`), never by its value (`--gray-200`, `--space-16px`). Primitive value tokens exist only in the palette file that semantic tokens alias.
- **One escape hatch, documented** — When a one-off value is genuinely required, add it as a new token rather than inlining it, and state in the same change why the existing scale did not cover the case.

## 2. Spacing, Sizing and Type Scale

- **4pt base grid** — Every margin, padding, gap and fixed dimension is a multiple of 4px, expressed through the spacing scale. Values such as `13px` or `7px` are rejected outright.
- **Modular type scale** — Font sizes come from a declared ratio-based scale. Never introduce a size that is not already a step on that scale, and never fake hierarchy by nudging a size by one or two pixels.
- **Hierarchy through de-emphasis** — Establish visual hierarchy by lowering the weight, size or contrast of secondary elements before raising the prominence of the primary one.

## 3. Color

- **12-step semantic scale (Radix Colors model)** — Steps have fixed jobs: 1–2 app and subtle backgrounds, 3–5 component backgrounds by interaction state, 6–8 borders and separators, 9–10 solid fills, 11–12 text. Pick the step by its job, never by how the swatch looks.
- **Perceptually uniform space** — Author and interpolate color in OKLCH (CSS Color 4). Do not build ramps by hand-tweaking hex values, and do not interpolate gradients in sRGB when a perceptual space is available.
- **Never grey text on a colored surface** — Tint the low-emphasis text toward the surface hue instead of desaturating it to grey.
- **Both themes are first-class** — Define the complete light palette on `:root`, redefine only the tokens in the dark block, and give every surface an explicit background token. A transparent body borrows the host's theme and breaks.

## 4. WCAG 2.2 Ship Blockers

Treat these as build failures, not review comments:

- **1.4.3 Contrast (Minimum)** — Body text at least 4.5:1, large text (≥18pt, or ≥14pt bold) at least 3:1, measured against the actual rendered background including any overlay or image.
- **1.4.11 Non-text Contrast** — Control boundaries, focus indicators, and meaningful graphical parts at least 3:1.
- **2.4.7 / 2.4.11 Focus** — Every interactive element has a visible focus indicator, and that indicator is never fully hidden by sticky headers, footers or overlays. Never ship `outline: none` without an equivalent replacement.
- **2.5.8 Target Size (Minimum)** — Every interactive element has a hit area of at least 24×24 CSS px, achieved with padding or an `::after` overlay that extends the hit region rather than by inflating the visible glyph.
- **1.4.10 Reflow** — Content reflows to a 320px viewport width without a horizontal scrollbar on the page body. Wide tables, diagrams and code blocks scroll inside their own container.

## 5. Motion and Media Preferences

- **Reduced-motion escape hatch is mandatory** — Every stylesheet ships a `@media (prefers-reduced-motion: reduce)` block that neutralizes animation and transition durations globally.
- **Respect `prefers-color-scheme` and declare `color-scheme`** — Set the `color-scheme` property so form controls, scrollbars and the canvas match the theme.
- **Motion carries meaning or it is removed** — Animate to explain a state change or spatial relationship. Decorative motion with no informational job is deleted, not tuned.

## 6. Semantics Before ARIA

- **Native element first** — Reach for `<button>`, `<a href>`, `<dialog>`, `<details>`, `<input type=checkbox>`, `<select>` and `<table>` before any `role=` attribute. A `div` with an `onClick` is a defect.
- **Follow the APG pattern verbatim** — When a widget genuinely has no native equivalent, implement the ARIA Authoring Practices Guide pattern completely, including its keyboard interaction table, rather than inventing a subset.

# Part B — 프론트엔드 아키텍처 (Frontend Architecture)

## 7. Feature-Sliced Structure

- **Features own their code** — Every unit of functionality lives under `src/features/<feature>/` with only the subfolders it actually needs (`api`, `components`, `hooks`, `stores`, `types`, `utils`). Do not create empty scaffolding folders.
- **Unidirectional imports** — Flow is `shared → features → app`. A feature never imports from another feature; shared code never imports from a feature. Cross-feature needs are lifted into `shared` or composed at the app layer.
- **No `containers/` split** — Never emit `XContainer` / `XView` pairs. Extract stateful and data-fetching logic into a `useX` hook the component calls directly.

## 8. Server and Client Boundary

- **Push `'use client'` to the leaves** — Mark the smallest interactive component. Never place the directive on a layout or page, which drags its entire import graph into the browser bundle.
- **Every `'use server'` export is a public unauthenticated endpoint** — Inside each server function, in this order: parse and validate every argument with a schema (`safeParse`), then authenticate, then authorize the specific resource, and only then touch data. Never trust an argument because the only caller is your own form.
- **Segments are explicit** — A folder becomes a public URL only when it contains `page.tsx` or `route.ts`. Colocate components, hooks, queries and tests inside the segment; use route groups to organize without affecting the URL.
- **Read the version-matched docs** — Before writing framework-specific code, consult the docs bundled in the installed package rather than recalling API shapes from memory.

## 9. State

- **Server state and client state are different things** — Data owned by the server lives in a query cache with a stable key factory. Never mirror fetched data into `useState` and never hand-synchronize the two.
- **Status unions, never loading booleans** — Model async state as one string union (`'idle' | 'pending' | 'resolved' | 'rejected'`), never as two or more independent boolean flags that can contradict each other.
- **One global store, sliced** — Keep a single global store split into slice creators. Update only through the setter API; never mutate store state directly.
- **Derive, do not duplicate** — Compute values from existing state during render. A piece of state that can be derived is a bug waiting to desynchronize.

## 10. Forms and Validation

- **One schema, both sides** — Define the validation schema once and use it for client-side form validation and for server-side argument parsing. A client-only check is a convenience, never a guarantee.
- **Accessible by construction** — Every input has a programmatically associated label, and every error message is linked to its field and announced.

## 11. Testing

- **Mostly integration** — Default every new test to the integration layer: render the real component tree with real children, real router and real store, mocking only the network boundary.
- **Query priority is fixed** — Select elements in this order, stopping at the first that works: `getByRole` (with the `name` option), `getByLabelText`, `getByPlaceholderText`, `getByText`, `getByDisplayValue`. Reach for a test id only when no accessible query can express the intent.
- **Assert only observable behavior** — Rendered text, roles, accessible names, visible state, and the callbacks a parent receives. Never assert on internal component state, instance methods, or implementation-only props.
- **Real user events** — Open every interaction test with `const user = userEvent.setup()` before `render()`, and `await` every `user.*` call. Use low-level event firing only for events a real user cannot produce.
- **Unhandled requests fail loudly** — Configure the network mock with `onUnhandledRequest: 'error'` so a request without a handler fails the test instead of escaping to the real network.
- **No arbitrary waits** — Wait on a condition or a web-first assertion. A fixed sleep in a test is a defect, not a stabilization.

## 12. Performance

- **Measure before optimizing** — Do not add memoization, code splitting or virtualization without a profile or a bundle report showing the cost.
- **Budget the bundle** — Every route has a size budget. A change that exceeds it is either justified in the same change or reverted.
