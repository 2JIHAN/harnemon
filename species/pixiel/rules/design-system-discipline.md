---
name: design-system-discipline
description: Always-on visual design constraints for web UI. Enforces token-only styling, a fixed spacing and type scale, 12-step semantic color usage, and WCAG 2.2 ship blockers.
---

# Design System Discipline (design-system-discipline.md)

Binding constraints for every screen, component, or stylesheet you emit. These are ship blockers, not preferences.

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
