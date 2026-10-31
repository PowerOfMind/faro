---
title: Building agents
desc: AI agents combine models and tools in a loop. Explore a TypeScript skeleton, practical limits and cases where a simpler solution fits.
pkgs: "@anthropic-ai/sdk", "@modelcontextprotocol/sdk"
---
## What it is
An agent is a **model in a loop with tools**: it decides, calls a tool, reads the result and decides again until it is done.

```text
goal → the model picks an action → tool (read, search, run) → result → done? → no: repeat
```

## Skeleton (TypeScript)
```ts
import Anthropic from '@anthropic-ai/sdk';
const client = new Anthropic();           // reads ANTHROPIC_API_KEY from the environment
const messages = [{role: 'user', content: 'Summarise the TODOs in src/'}];

for (let step = 0; step < 10; step++) {    // step cap
  const r = await client.messages.create({
    model: MODEL, max_tokens: 1024, tools, messages,
  });
  messages.push({role: 'assistant', content: r.content});
  if (r.stop_reason !== 'tool_use') break;
  const results = await runTools(r.content);   // your code, with validation
  messages.push({role: 'user', content: results});
}
```

## How not to lose control
- **A cap on steps and spend**, always.
- **Least privilege**: read-only tools by default; writes and network with confirmation.
- **Validate arguments** of every tool as if they came from a hostile user (they may come from an injection; see [prompt injection](@/seguridad/prompt-injection)).
- **Log** every call so you can reproduce failures.
- **Evaluate**: 10 real cases with the expected result, repeated after every change.

## When NOT to use an agent
If the steps are fixed, a script or a flow with a single model call is cheaper, faster and more predictable. Use an agent when the path depends on what it finds along the way.

> [!TIP] Subagents
> To research or read a lot, launch a subagent: it spends its own context and returns only the summary.

=== esquema
# Concept
- Agent — a model in a loop with tools.
- Loop — decide, use a tool, read the result, repeat.
# Control
- Step and spend cap — always.
- Least privilege — read-only tools by default.
- Validate arguments — as if they came from a hostile user.
- Evaluate — real cases repeated after every change.
=== test
? When should you NOT use an agent?
- When the path depends on what you find
* When the steps are fixed and known
- Never; it is always better
! A script or a single model call is cheaper and more predictable when the flow is fixed.
? What do you always limit in an agent?
* The number of steps and the spend
- Only the colour of the UI
- Nothing, so it is free
! A loop with no cap can spend without control.
? How do you treat the arguments the model passes to a tool?
- As trusted data
* As untrusted input that must be validated
- No need to look at them
! They may come from a prompt injection.
