---
title: Testing with Vitest and Playwright
desc: A practical guide to testing with vitest and playwright, common mistakes, decisions, and checks to help you solve problems with confidence.
pkgs: vitest, @playwright/test, @testing-library/react
---
## Choosing tests
Test rules and edge cases with Vitest; use React Testing Library for observable component behavior and Playwright for complete browser journeys. Prioritize failures that affect users.

## Mocks
Mock external boundaries when needed, such as a request or clock, and reset mocks between tests. Do not mock the function whose logic you want to verify: that removes the signal from the test.

## Reliable E2E
Use role and name locators, isolated data and assertions that wait for the expected state. Avoid fixed delays and dependencies between tests. Inspect traces and failure causes before retrying or increasing timeouts.

## Quick decisions
| Question | Answer |
|---|---|
| What does an E2E test check? | A complete browser journey |
| What is appropriate to mock? | An external boundary when needed |
| Which locator reflects the accessible UI? | Role and name |

> [!AI] With AI
> Describe your version, environment, expected and actual results, and a minimal reproduction. Ask for a testable explanation and references to the official documentation.

Documentation: [official guide](https://playwright.dev/docs/best-practices).

Related: [continue with a related guide](@/js-ts/modulos-y-bundlers).

=== esquema
# Key ideas
- Choosing tests — Test rules and edge cases with Vitest; use React Testing Library for observable component behavior and Playwright for complete browser journeys.
- Mocks — Mock external boundaries when needed, such as a request or clock, and reset mocks between tests.
- Reliable E2E — Use role and name locators, isolated data and assertions that wait for the expected state.
=== test
? What does an E2E test check?
* A complete browser journey
- An external boundary when needed
- Role and name
! A complete browser journey.
? What is appropriate to mock?
* An external boundary when needed
- Role and name
- Isolated data
! An external boundary when needed.
? Which locator reflects the accessible UI?
* Role and name
- Isolated data
- Investigate its cause and traces
! Role and name.
? What reduces interference between tests?
* Isolated data
- Investigate its cause and traces
- A complete browser journey
! Isolated data.
? What should you do with a flaky failure?
* Investigate its cause and traces
- A complete browser journey
- An external boundary when needed
! Investigate its cause and traces.
