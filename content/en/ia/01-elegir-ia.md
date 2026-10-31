---
title: Which AI to use for what
desc: AI tools serve different tasks. Compare coding agents, chat assistants and AI search, and learn when to check sources or protect data.
---
There is no "best" AI. There are tasks and tools. Try the same question in two of them before trusting one.

| You need | Start with | Why |
|---|---|---|
| Coding inside your repo | Claude Code, Codex CLI, Cursor, Copilot | They read and edit your files and run tests |
| Understand an error or design a solution | Claude or ChatGPT (chat) | They reason over the context you paste |
| Recent information (versions, prices, news) | AI search (Perplexity, ChatGPT/Gemini with search) | They cite sources; a bare model stops at its cutoff date |
| A huge document or many PDFs | Long-context models (Gemini, Claude) | More pages fit |
| Images, video, audio | Gemini, ChatGPT, specialised tools | They are multimodal |
| Automating repetitive tasks | Agents with tools (see [agents](@/ia/agentes)) | They chain steps |

## Rules that save time
- **Cutoff date**: the model does not know what was published after its training. For fast-moving libraries, paste the docs or turn on search.
- **One chat per task**: long chats degrade quality and burn more tokens.
- **Big model to decide, small model to execute**: design and hard debugging with the most capable one; renames, formatting and mechanical work with the cheap one.
- **Sensitive data**: do not paste keys, personal data or NDA code into services whose training policy you do not know.

> [!TIP] Smoke test
> If the answer includes a function, flag or package you do not recognise, look it up in the official docs before continuing. See [verify what the AI says](@/ia/verificar).

=== esquema
# Choose a tool
- Code in your repo — an agent that reads and edits files (Claude Code, Codex, Cursor, Copilot).
- Error or design — a chat with reasoning and the context pasted in.
- Recent data — AI search that cites sources.
# Rules
- Cutoff date — the model does not know what came after its training.
- One chat per task — long chats degrade and cost more.
- Sensitive data — never keys or personal data in services you do not know.
=== test
? What do you use to ask about the latest version of a library?
- The bare model, which surely knows
* AI search or the official documentation
- A long chat you already started
! The model stops at its cutoff date; for recent data you must search or paste the docs.
? Why is one chat per task a good idea?
* Long chats degrade quality and burn more tokens
- Because the model forgets the language
- Because each chat is free
! Every message resends the history: less useless context, better answers, lower cost.
? What should you NOT paste into an AI service you do not know?
- A fragment of public code
* API keys and personal data
- A generic error message
! Keys and personal data should not leave your environment.
