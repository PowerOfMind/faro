---
title: Angular: signals and control flow
desc: A practical guide to angular: signals and control flow, common mistakes, decisions, and checks to help you solve problems with confidence.
pkgs: @angular/core
---
## Signals
`signal` holds a value read by calling it: `count()`. Update it with `set` or `update`; `computed` derives a value and tracks dependencies. Avoid mutating objects in place, which may not notify consumers.

## Effect
`effect` runs logic when signals it reads change; use it to synchronize with external systems, not to copy derived state. It is normally created in an injection context such as a component constructor.

## Templates and standalone
`@if` renders conditions; `@for (item of items; track item.id)` identifies rows with a stable key and supports `@empty`. A standalone component imports its template dependencies directly.

## Quick decisions
| Question | Answer |
|---|---|
| How do you read a signal? | Call it as a function |
| How do you derive a value? | With computed |
| What is effect for? | Synchronizing with external systems |

> [!AI] With AI
> Describe your version, environment, expected and actual results, and a minimal reproduction. Ask for a testable explanation and references to the official documentation.

Documentation: [official guide](https://angular.dev/guide/signals).

Related: [continue with a related guide](@/angular/formularios-http-y-rxjs).

=== esquema
# Key ideas
- Signals — `signal` holds a value read by calling it: `count()`.
- Effect — `effect` runs logic when signals it reads change; use it to synchronize with external systems, not to copy derived state.
- Templates and standalone — `@if` renders conditions; `@for (item of items; track item.id)` identifies rows with a stable key and supports `@empty`.
=== test
? How do you read a signal?
* Call it as a function
- With computed
- Synchronizing with external systems
! Call it as a function.
? How do you derive a value?
* With computed
- Synchronizing with external systems
- track with a stable key
! With computed.
? What is effect for?
* Synchronizing with external systems
- track with a stable key
- In its imports
! Synchronizing with external systems.
? What identifies rows in @for?
* track with a stable key
- In its imports
- Call it as a function
! track with a stable key.
? Where does a standalone component import dependencies?
* In its imports
- Call it as a function
- With computed
! In its imports.
