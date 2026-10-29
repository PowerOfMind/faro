---
title: Qué IA usar para cada cosa
desc: Claude, ChatGPT, Gemini, Copilot y buscadores con IA: para qué sirve cada uno.
---
No hay una IA "mejor". Hay tareas y herramientas. Prueba la misma pregunta en dos antes de fiarte de una.

| Necesitas | Empieza por | Por qué |
|---|---|---|
| Programar dentro de tu repo | Claude Code, Codex CLI, Cursor, Copilot | Leen y editan tus ficheros y ejecutan tests |
| Entender un error o diseñar una solución | Claude o ChatGPT (chat) | Razonan con el contexto que pegues |
| Información reciente (versiones, precios, noticias) | Buscador con IA (Perplexity, ChatGPT/Gemini con búsqueda) | Citan fuentes; el modelo "a secas" se queda en su fecha de corte |
| Documento enorme o muchos PDF | Modelos de contexto largo (Gemini, Claude) | Caben más páginas |
| Imágenes, vídeo, audio | Gemini, ChatGPT, herramientas especializadas | Son multimodales |
| Automatizar tareas repetidas | Agentes con herramientas (ver [agentes](@/ia/agentes)) | Encadenan pasos |

## Reglas que ahorran tiempo
- **Fecha de corte**: el modelo no sabe lo publicado después de su entrenamiento. Para librerías que cambian rápido, pega la doc o activa la búsqueda.
- **Un chat por tarea**: los chats largos degradan la calidad y gastan más tokens.
- **Modelo grande para decidir, pequeño para ejecutar**: diseño y depuración difícil con el más capaz; renombrados, formato y tareas mecánicas con el barato.
- **Datos sensibles**: no pegues claves, datos personales ni código bajo NDA en servicios cuya política de entrenamiento no conozcas.

> [!TIP] Prueba de humo
> Si la respuesta incluye una función, flag o paquete que no reconoces, búscalo en la doc oficial antes de seguir. Ver [verificar lo que dice la IA](@/ia/verificar).
