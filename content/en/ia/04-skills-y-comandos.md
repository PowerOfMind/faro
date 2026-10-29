---
title: Skills, commands and hooks
desc: Package the way you work so the agent repeats it the same way.
---
## Skill
A folder with a `SKILL.md`: instructions the agent loads **only when the task fits** (which is why they save context).
```text
.claude/skills/review-seo/
  SKILL.md        # name + description header, then the instructions
  template.md     # optional resources
```
```markdown
---
name: review-seo
description: Reviews a page's title, meta, headings and structured data. Use it when editing public HTML.
---
1. Check <title> (<60 characters) and meta description.
2. One <h1>. Images with alt.
3. Return a table: element · status · fix.
```
The **description** is what matters most: it decides when the skill activates. Write it as "what it does + when to use it".

## Other pieces
| Piece | Purpose | Where (Claude Code) |
|---|---|---|
| Project map | Fixed repo context | `CLAUDE.md` |
| Custom command | A `/my-command` shortcut with a prompt | `.claude/commands/` |
| Subagent | Specialist with its own context | `.claude/agents/*.md` |
| Hook | Code that **always** runs on an event (before/after a tool) | `settings.json` |
| MCP | Connect external tools and data | see [MCP](@/ia/mcp) |

> [!NOTE] Decision rule
> If you want something to happen **always**, it is a hook (the system runs it). If you want the model to **remember and apply it with judgement**, it is a skill or the map. An instruction in the chat does not persist.

## Good practice
- One skill, one task. If it does three things, they are three skills.
- Instructions as checkable steps; include an example of the output.
- No secrets in `SKILL.md`.
- Test it with 3 real requests and adjust the description until it activates on its own.

=== esquema
# Pieces
- Skill — a SKILL.md loaded only when the task fits.
- CLAUDE.md — fixed repository context.
- Subagent — a specialist with its own context.
- Hook — code that always runs on an event.
- MCP — connects external tools and data.
# Rules
- Something that must always happen — hook.
- Something the model should remember with judgement — skill or map.
- One skill, one task — if it does three things, they are three.
=== test
? What matters most in SKILL.md for it to activate?
- The folder name
* The description: what it does and when to use it
- The number of steps
! The model decides from the description when to load the skill.
? You want a formatter to run ALWAYS after editing. What do you use?
* A hook
- A skill
- A sentence in the chat
! Hooks are run by the system; an instruction in the chat does not persist.
? Why do skills save context?
- Because they are shorter
* Because they only load when the task needs them
- Because they clear the history
! The full instructions enter the context only when needed.
