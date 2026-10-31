---
title: Ahorrar tokens y contexto
desc: Tokens y contexto en agentes de código, con hábitos para reducir costes sin perder calidad y ejemplos de mapas de proyecto e instrucciones.
---
Los tokens se gastan en lo que **lee** el modelo (contexto) más que en lo que escribe. Cada mensaje reenvía el historial.

## Hábitos con más efecto
1. **Limpia el contexto entre tareas** (`/clear` en Claude Code). No arrastres una tarea terminada.
2. **Un mapa del proyecto** (`CLAUDE.md` o `AGENTS.md`): dónde está cada cosa, comandos, trampas. Evita que el agente explore a ciegas.
3. **Marca lo generado** como "no leer": builds, `dist/`, lockfiles, JSON enormes. Una línea en el mapa ahorra miles de tokens.
4. **Pide trozos, no ficheros**: "lee solo `foo()` y su llamador".
5. **Modelo adecuado**: el más capaz para diseñar, uno ligero para tareas mecánicas.
6. **Salida corta**: "devuelve solo el diff", "responde en 5 líneas".
7. **Delega lecturas largas** a un subagente: trabaja en su propio contexto y devuelve un resumen.
8. **Caché de prompt**: mantener estable el principio del prompt (instrucciones, mapa) abarata las repeticiones; no cambies el inicio sin necesidad.

## Qué poner en el mapa del proyecto
```markdown
# Proyecto X
## Dónde se edita cada cosa
- UI: src/components/ (Lit). Estilos globales: src/theme.css
## Generado (no editar ni leer)
- dist/, public/search.json
## Comandos
- Build: npm run build · Tests: npm test
## Trampas
- El service worker cachea: desregístralo al probar cambios.
```

> [!TIP] Medir
> Mira el uso de contexto del agente de vez en cuando. Si una tarea supera el 50 % del contexto, resume y empieza de nuevo con ese resumen.

=== esquema
# Qué gasta
- Contexto leído — cada mensaje reenvía el historial.
- Salida larga — pide diff, no ficheros.
# Qué ahorra
- /clear entre tareas — no arrastres una tarea terminada.
- Mapa del proyecto — CLAUDE.md con dónde está cada cosa.
- Marcar lo generado — dist/, lockfiles y JSON enormes fuera de lectura.
- Subagentes — leen mucho en su contexto y devuelven un resumen.
=== test
? ¿Dónde se van la mayoría de los tokens?
* En lo que el modelo lee (contexto)
- En las tildes
- Solo en lo que escribe
! Cada mensaje reenvía el historial, así que el contexto pesa más que la salida.
? ¿Para qué sirve un CLAUDE.md?
- Para guardar contraseñas
* Para darle al agente un mapa fijo: dónde editar, comandos y trampas
- Para borrar el historial
! Evita que explore a ciegas en cada sesión.
? ¿Qué haces al terminar una tarea y empezar otra distinta?
* Limpiar el contexto (/clear)
- Seguir en el mismo chat
- Pegar más ficheros
! Arrastrar la tarea anterior gasta tokens y distrae al modelo.
