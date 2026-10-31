---
title: SDKs and tools for AI apps
desc: AI app tools support model calls, streaming, retrieval and evaluation. Compare SDKs and libraries with practical production guidance.
pkgs: "@anthropic-ai/sdk", openai, ai, "@modelcontextprotocol/sdk", langchain
---
| Need | Option |
|---|---|
| Call a model | The provider's official SDK (`@anthropic-ai/sdk`, `openai`, `@google/genai`) |
| A common layer across providers, streaming and chat UI | **Vercel AI SDK** (`ai`) |
| Agents with tools | The provider's agent SDK, or your own loop (see [Building agents](@/ia/agentes)) |
| Connect external tools | **MCP** (`@modelcontextprotocol/sdk`) |
| Structured output (validated JSON) | Zod schema + the provider's structured/tool-use mode |
| Embeddings + semantic search | Postgres + **pgvector**, or Qdrant/Pinecone |
| Complex orchestration | LangGraph; check whether a simple loop is enough |
| Evaluate quality | Your own set of cases + Promptfoo / Braintrust |
| Call observability | Langfuse, Helicone, LangSmith |
| Run models locally | Ollama, LM Studio, llama.cpp |

## Good practice in production
- **Never call the model from the browser with your key**; go through your server (see [Secrets](@/seguridad/secretos)).
- **Streaming** for long answers (perceived speed).
- **Retries with backoff** on 429/5xx; **timeouts**; **token cap**.
- **Prompt caching** and caching of repeated answers to save cost.
- **Log** input, output, latency and cost (taking care with personal data).
- Pin the **model by version** and repeat your evaluations when you change it: behaviour varies.
- RAG: reasonable chunking, metadata, and show **sources** to the user.

> [!WARN] Prices and models change
> Do not copy cost figures from an old article. Check the provider's pricing page the day you decide.

=== esquema
# Pieces
- Provider SDK — call the model.
- Vercel AI SDK — streaming and a common layer.
- MCP — connect external tools.
- pgvector — embeddings and semantic search.
# Production
- Intermediate server — never the key in the browser.
- Retries with backoff — on 429 and 5xx.
- Evaluate — your cases when you change model.
=== test
? Where do you call the model from with your key?
* From your server
- From the browser
- From a public file
! The key must not reach the client.
? A 429 response from the provider. What do you do?
* Retry with backoff
- Retry without pause
- Ignore it
! Backoff avoids saturating and respects the limits.
? You change model. What do you do?
* Repeat your evaluations
- Nothing
- Raise max_tokens
! Behaviour changes between models.
