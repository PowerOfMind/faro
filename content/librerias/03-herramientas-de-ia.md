---
title: SDKs y herramientas para apps con IA
desc: Librerías para llamar a modelos, hacer streaming, RAG y evaluar.
pkgs: "@anthropic-ai/sdk", openai, ai, "@modelcontextprotocol/sdk", langchain
---
| Necesidad | Opción |
|---|---|
| Llamar a un modelo | SDK oficial del proveedor (`@anthropic-ai/sdk`, `openai`, `@google/genai`) |
| Capa común entre proveedores, streaming y UI de chat | **Vercel AI SDK** (`ai`) |
| Agentes con herramientas | SDK de agentes del proveedor, o tu bucle propio (ver [Crear agentes](@/ia/agentes)) |
| Conectar herramientas externas | **MCP** (`@modelcontextprotocol/sdk`) |
| Salida estructurada (JSON validado) | Esquema Zod + modo estructurado/tool use del proveedor |
| Embeddings + búsqueda semántica | Postgres + **pgvector**, o Qdrant/Pinecone |
| Orquestación compleja | LangGraph; evalúa si un bucle simple basta |
| Evaluar calidad | Conjunto propio de casos + Promptfoo / Braintrust |
| Observabilidad de llamadas | Langfuse, Helicone, LangSmith |
| Ejecutar modelos en local | Ollama, LM Studio, llama.cpp |

## Buenas prácticas en producción
- **Nunca llames al modelo desde el navegador con tu clave**; pasa por tu servidor (ver [Secretos](@/seguridad/secretos)).
- **Streaming** para respuestas largas (percepción de velocidad).
- **Reintentos con backoff** ante 429/5xx; **timeouts**; **tope de tokens**.
- **Caché de prompts** y de respuestas repetidas para ahorrar coste.
- **Registra** entrada, salida, latencia y coste (cuidando datos personales).
- Fija el **modelo por versión** y repite tus evaluaciones al cambiarlo: el comportamiento varía.
- RAG: troceado razonable, metadatos, y mostrar **fuentes** al usuario.

> [!WARN] Precios y modelos cambian
> No copies cifras de coste de un artículo antiguo. Consulta la página de precios del proveedor el día que decidas.
