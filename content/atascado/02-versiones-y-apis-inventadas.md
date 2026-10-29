---
title: APIs obsoletas o inventadas
desc: El fallo número uno del código generado y cómo detectarlo.
---
## Por qué pasa
El modelo aprende de código de **muchas versiones a la vez**. Mezcla `react-router` v5 con v7, Next `pages/` con `app/`, Angular con NgModules con standalone, Tailwind 3 con 4, Lit 2 con 3.

## Síntomas
- `X is not a function` / `Module not found` / `has no exported member`.
- Un parámetro que "no hace nada".
- Ejemplos que usan `lit-element`, `componentWillMount`, `getServerSideProps` en un proyecto que no lo soporta.

## Qué hacer
1. Dile la versión **y** el paradigma: "Next 15 App Router", "Angular standalone con signals".
2. Pega el fragmento de doc o el `.d.ts` real: `node_modules/<pkg>/dist/*.d.ts` es la verdad de tu versión.
3. `npm ls <pkg>` para ver qué versión está realmente instalada (puede haber dos).
4. Lee la guía de migración de la última versión mayor.
5. En TypeScript, el error de tipos suele delatar la API inexistente: no lo silencies con `any`.

```bash
npm ls react lit            # versiones reales
npm view react versions --json | tail -5
npm view lit dist-tags
```

> [!AI] Pedir a la IA que se corrija
> "Comprueba cada import y cada método de tu respuesta contra la versión X. Marca los que no estés seguro que existan."

> [!TIP] Fija el contexto
> Pon las versiones clave en el mapa del proyecto (`CLAUDE.md`) para que cada sesión las tenga.
