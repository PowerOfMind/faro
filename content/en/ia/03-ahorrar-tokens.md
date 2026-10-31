---
title: Saving tokens and context
desc: AI token usage can grow with every message. Save context and money using project maps, focused reads, model choice and prompt caching.
---
Tokens are spent on what the model **reads** (context) more than on what it writes. Every message resends the history.

## Habits with the most effect
1. **Clear the context between tasks** (`/clear` in Claude Code). Do not drag a finished task along.
2. **A project map** (`CLAUDE.md` or `AGENTS.md`): where everything is, commands, traps. It stops the agent exploring blindly.
3. **Mark generated files** as "do not read": builds, `dist/`, lockfiles, huge JSON. One line in the map saves thousands of tokens.
4. **Ask for pieces, not files**: "read only `foo()` and its caller".
5. **Right model**: the most capable for design, a lighter one for mechanical tasks.
6. **Short output**: "return only the diff", "answer in 5 lines".
7. **Delegate long reads** to a subagent: it works in its own context and returns a summary.
8. **Prompt caching**: keeping the start of the prompt (instructions, map) stable makes repeats cheaper; do not change the beginning without a reason.

## What to put in the project map
```markdown
# Project X
## Where each thing is edited
- UI: src/components/ (Lit). Global styles: src/theme.css
## Generated (do not edit or read)
- dist/, public/search.json
## Commands
- Build: npm run build · Tests: npm test
## Traps
- The service worker caches: unregister it when testing changes.
```

> [!TIP] Measure
> Check the agent's context usage from time to time. If a task passes 50 % of the context, summarise and start again with that summary.

=== esquema
# What costs
- Context read — every message resends the history.
- Long output — ask for a diff, not whole files.
# What saves
- /clear between tasks — do not drag a finished task along.
- Project map — CLAUDE.md with where everything is.
- Mark generated files — dist/, lockfiles and huge JSON off-limits.
- Subagents — read a lot in their own context and return a summary.
=== test
? Where do most tokens go?
* On what the model reads (context)
- On accents
- Only on what it writes
! Every message resends the history, so context weighs more than output.
? What is a CLAUDE.md for?
- Storing passwords
* Giving the agent a fixed map: where to edit, commands and traps
- Clearing the history
! It stops the agent exploring blindly in every session.
? What do you do when you finish a task and start a different one?
* Clear the context (/clear)
- Stay in the same chat
- Paste more files
! Dragging the previous task along wastes tokens and distracts the model.
