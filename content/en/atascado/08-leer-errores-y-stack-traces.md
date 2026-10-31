---
title: Reading errors and stack traces
desc: A practical guide to reading errors and stack traces, common mistakes, decisions, and checks to help you solve problems with confidence.
---
## Read the message
Start with the exact type and message; identify the relevant file and line in your code. The first stack frame is not always the root cause: follow calls and chained causes to the origin.

## Isolate and reproduce
Record steps, expected and actual results, versions and environment. Reduce the example while preserving the failure; compare with the last working state and change one hypothesis at a time.

## Ask for useful help
Give the AI the complete message, stack, minimal example and what you tried, without secrets or personal data. Ask for a testable hypothesis, a way to disprove it and the relevant official source.

## Quick decisions
| Question | Answer |
|---|---|
| Where do you start? | With the exact type and message |
| What does a minimal reproduction contain? | Only what is needed to preserve the failure |
| What should you compare? | The last working state |

> [!AI] With AI
> Describe your version, environment, expected and actual results, and a minimal reproduction. Ask for a testable explanation and references to the official documentation.

Documentation: [official guide](https://react.dev/learn/react-developer-tools).

Related: [continue with a related guide](@/js-ts/testing-con-vitest-y-playwright).

=== esquema
# Key ideas
- Read the message — Start with the exact type and message; identify the relevant file and line in your code.
- Isolate and reproduce — Record steps, expected and actual results, versions and environment.
- Ask for useful help — Give the AI the complete message, stack, minimal example and what you tried, without secrets or personal data.
=== test
? Where do you start?
* With the exact type and message
- Only what is needed to preserve the failure
- The last working state
! With the exact type and message.
? What does a minimal reproduction contain?
* Only what is needed to preserve the failure
- The last working state
- One at a time
! Only what is needed to preserve the failure.
? What should you compare?
* The last working state
- One at a time
- Secrets and personal data
! The last working state.
? How should you test hypotheses?
* One at a time
- Secrets and personal data
- With the exact type and message
! One at a time.
? What should you remove before sharing logs?
* Secrets and personal data
- With the exact type and message
- Only what is needed to preserve the failure
! Secrets and personal data.

=== prueba

## Read an error
```js
function parseCount(value) {
  const count = Number(value);
  if (!Number.isFinite(count)) throw new Error('Invalid count');
  return count;
}
try {
  console.log(parseCount('many'));
} catch (error) {
  console.error(error.name, error.message, error.stack);
}
```
Reto: change the input and compare the result.

## Preserve the cause
```js
try {
  try {
    throw new Error('Connection failed');
  } catch (error) {
    throw new Error('Could not load data', {cause: error});
  }
} catch (error) {
  console.error(error.message, error.cause.message);
}
```
Reto: inspect the cause as well as the message.
