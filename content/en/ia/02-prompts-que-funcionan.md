---
title: Prompts that work
desc: Prompts for coding work better with context, a clear goal and constraints. Use a practical template and examples to reduce back-and-forth.
---
## Template
```text
Context: Lit 3 + TypeScript, Vite, no framework.
Goal: an accessible <app-tabs> with keyboard support.
Constraints: no new dependencies; do not touch src/legacy/.
Output: only the diff of the files that change.
Check: how to verify it works (command or steps).
```

## What improves the result
- **Explicit versions** (`React 19`, `Angular 22`, `Node 22`).
- **A "done" criterion**: "`npm test` passes", "no console errors".
- **The full error**, not a paraphrase: message, stack and the line of code.
- **An input/output example** when the format matters.
- **Ask for alternatives with trade-offs** before implementing something big.
- **Narrow the scope**: "only this file".

## What makes it worse
- Asking several unrelated things in one message.
- Insisting after 2 failures without changing anything: change the context (see [breaking out of the loop](@/atascado/metodo)).
- Contradictory instructions ("keep it simple and cover every case").

> [!AI] Useful patterns
> - "Before writing code, tell me what questions you have."
> - "Explain why it fails with one hypothesis and how to test it."
> - "What assumptions did you make that I did not tell you?"
> - "Review your answer looking for APIs that might not exist in the stated version."

=== esquema
# Template
- Context — versions and stack (Lit 3, Node 22).
- Goal — one concrete thing.
- Constraints — what not to touch and what not to add.
- Check — how to know it works.
# Avoid
- Asking several things at once — it mixes the context.
- Insisting without changing anything — change the context after two failures.
- Contradictory instructions — "simple" and "covers everything".
=== test
? What improves a coding prompt the most?
* Stating versions and a "done" criterion
- Making it longer
- Writing it in capitals
! Versions and a success criterion prevent wrong APIs and half answers.
? After two failed attempts with the same error, what do you do?
- Repeat the same prompt
* Change the context: full error, minimal code and what you ruled out
- Ask the same thing more insistently
! Insisting adds noise; a new, better context gives a different answer.
? How do you give the AI the error?
* With the full message and stack and the line of code
- With your summary of what you think happens
- Just "it does not work"
! A paraphrase loses the details that reveal the cause.
