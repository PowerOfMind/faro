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

=== esquema
# Elegir herramienta
- Código en tu repo — agente que lee y edita ficheros (Claude Code, Codex, Cursor, Copilot).
- Error o diseño — chat con razonamiento y el contexto pegado.
- Datos recientes — buscador con IA que cita fuentes.
# Reglas
- Fecha de corte — el modelo no sabe lo posterior a su entrenamiento.
- Un chat por tarea — los chats largos degradan y cuestan más.
- Datos sensibles — nunca claves ni datos personales en servicios que no conoces.
=== test
? ¿Qué usas para preguntar por la última versión de una librería?
- El modelo sin búsqueda, que seguro lo sabe
* Un buscador con IA o la documentación oficial
- Un chat largo ya empezado
! El modelo se queda en su fecha de corte; para datos recientes hay que buscar o pegar la doc.
? ¿Por qué conviene un chat por tarea?
* Los chats largos degradan la calidad y gastan más tokens
- Porque el modelo olvida el idioma
- Porque cada chat es gratis
! Cada mensaje reenvía el historial: menos contexto inútil, mejores respuestas y menos coste.
? ¿Qué NO deberías pegar en un servicio de IA que no conoces?
- Un fragmento de código público
* Claves de API y datos personales
- Un mensaje de error genérico
! Las claves y los datos personales no deben salir de tu entorno.
