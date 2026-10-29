---
title: Ahorrar tokens y contexto
desc: Cómo gastar menos sin perder calidad al trabajar con agentes de código.
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
