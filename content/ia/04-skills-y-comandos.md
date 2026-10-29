---
title: Skills, comandos y hooks
desc: Empaquetar tu forma de trabajar para que el agente la repita igual.
---
## Skill
Carpeta con un `SKILL.md`: instrucciones que el agente carga **solo cuando la tarea encaja** (por eso ahorran contexto).
```text
.claude/skills/revisar-seo/
  SKILL.md        # cabecera name + description, luego las instrucciones
  plantilla.md    # recursos opcionales
```
```markdown
---
name: revisar-seo
description: Revisa title, meta, headings y datos estructurados de una página. Úsala al editar HTML público.
---
1. Comprueba <title> (<60 caracteres) y meta description.
2. Un solo <h1>. Imágenes con alt.
3. Devuelve una tabla: elemento · estado · arreglo.
```
La **descripción** es lo más importante: decide cuándo se activa. Escríbela como "qué hace + cuándo usarla".

## Otras piezas
| Pieza | Para qué | Dónde (Claude Code) |
|---|---|---|
| Mapa del proyecto | Contexto fijo del repo | `CLAUDE.md` |
| Comando propio | Atajo `/mi-comando` con un prompt | `.claude/commands/` |
| Subagente | Especialista con su propio contexto | `.claude/agents/*.md` |
| Hook | Código que **siempre** se ejecuta ante un evento (antes/después de una herramienta) | `settings.json` |
| MCP | Conectar herramientas y datos externos | ver [MCP](@/ia/mcp) |

> [!NOTE] Regla de decisión
> Si quieres que algo ocurra **siempre**, es un hook (lo ejecuta el sistema). Si quieres que el modelo lo **recuerde y aplique con criterio**, es una skill o el mapa. Una instrucción en el chat no persiste.

## Buenas prácticas
- Una skill, una tarea. Si hace tres cosas, son tres skills.
- Instrucciones en pasos comprobables; incluye un ejemplo de salida.
- No metas secretos en el `SKILL.md`.
- Pruébala con 3 peticiones reales y ajusta la descripción hasta que se active sola.
