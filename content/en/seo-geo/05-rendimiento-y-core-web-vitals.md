---
title: Performance and Core Web Vitals
desc: A practical guide to performance and core web vitals, common mistakes, decisions, and checks to help you solve problems with confidence.
---
## Metrics
LCP measures when the largest visible content paints; INP measures responsiveness across interactions; CLS measures unexpected layout shifts. Good thresholds are LCP ≤ 2.5 s, INP ≤ 200 ms and CLS ≤ 0.1, assessed at the 75th percentile by device.

## Images and fonts
Size images appropriately, reserve space with width and height and prioritize the main image when appropriate. Avoid lazy-loading the LCP resource. Reduce font variants and reserve space to limit shifts.

## JavaScript and measurement
Reduce main-thread work and split long tasks to improve responsiveness. Compare real field data (CrUX or your own measurements) with Lighthouse and DevTools diagnostics; INP requires real interactions, while Lighthouse uses TBT as a lab indicator.

## Quick decisions
| Question | Answer |
|---|---|
| What does LCP measure? | The largest visible content paint |
| What does INP measure? | Interaction responsiveness |
| What does CLS measure? | Unexpected layout shifts |

> [!AI] With AI
> Describe your version, environment, expected and actual results, and a minimal reproduction. Ask for a testable explanation and references to the official documentation.

Documentation: [official guide](https://web.dev/articles/vitals).

Related: [continue with a related guide](@/react/hooks-propios-y-rendimiento).

=== esquema
# Key ideas
- Metrics — LCP measures when the largest visible content paints; INP measures responsiveness across interactions; CLS measures unexpected layout shifts.
- Images and fonts — Size images appropriately, reserve space with width and height and prioritize the main image when appropriate.
- JavaScript and measurement — Reduce main-thread work and split long tasks to improve responsiveness.
=== test
? What does LCP measure?
* The largest visible content paint
- Interaction responsiveness
- Unexpected layout shifts
! The largest visible content paint.
? What does INP measure?
* Interaction responsiveness
- Unexpected layout shifts
- The 75th
! Interaction responsiveness.
? What does CLS measure?
* Unexpected layout shifts
- The 75th
- Lab diagnostics
! Unexpected layout shifts.
? Which percentile is used for thresholds?
* The 75th
- Lab diagnostics
- The largest visible content paint
! The 75th.
? What does Lighthouse provide?
* Lab diagnostics
- The largest visible content paint
- Interaction responsiveness
! Lab diagnostics.
