---
title: CSS that does not obey
desc: z-index, horizontal scroll, mobile 100vh, overflowing flex, Safari.
---
## z-index does not work
An ancestor with `position`+`z-index`, `transform`, `opacity<1`, `filter` or `isolation` creates a **stacking context**. A child never escapes it. Fix by raising the ancestor, or moving the element out (modals: `<dialog>` + `showModal()` or a portal).

## Unexpected horizontal scroll
1. Inspect: `document.querySelectorAll('*').forEach(e => e.scrollWidth > innerWidth && console.log(e))`.
2. Causes: `100vw` (includes the scrollbar), images without `max-width:100%`, wide `pre` or tables, negative margins.
3. Do not hide it with `overflow-x:hidden` on `body` without finding the source.

## Overflowing flex/grid
Flex children have `min-width:auto`: long text or a `pre` pushes. Fix: `min-width:0` on the child and `overflow:auto`. In grid: `minmax(0,1fr)` instead of `1fr`.

## 100vh on mobile
The browser bar breaks it. Use `100dvh` (or `svh`/`lvh` as appropriate).

## Positions and heights
- `position:sticky` does not stick if an ancestor has `overflow` other than `visible`.
- `height:100%` requires the parent to have a defined height.
- `margin` collapses between siblings and parent-child; use `gap` in flex/grid.

## Mobile and touch
- Touch targets of at least **44×44 px**.
- `font-size` < 16px on an `input` makes iOS zoom on focus.
- `:hover` does not exist on touch: do not hide features behind it.

## Dark mode
Define colours as variables (`--bg`, `--text`), swap the set under `prefers-color-scheme: dark` and allow forcing with an attribute. Check contrast in both (WCAG AA: 4.5:1).

> [!AI] When asking an AI for CSS
> Give it the real HTML and the parent container; without them it invents structure. Ask for the cause, not just an `!important`.

=== esquema
# Layers and overflow
- Stacking context — position+z-index, transform, opacity<1.
- 100vw — includes the scrollbar and overflows.
- min-width:0 — for flex children with long text or pre.
# Mobile
- 100dvh — instead of 100vh.
- 44×44 px — minimum touch target.
- font-size 16px — avoids iOS zoom on inputs.
=== test
? A huge z-index does not put your modal in front. Why?
* An ancestor creates another stacking context
- The browser ignores z-index
- !important is missing
! The child cannot leave its ancestor's context.
? A flex child with long text pushes the width. Fix?
- width:100vw
* min-width:0 and suitable overflow
- display:block on the body
! Flex children have min-width:auto by default.
? Which unit do you use for full-screen height on mobile?
- 100vh
* 100dvh
- 100%
! dvh adjusts to the browser bar.
