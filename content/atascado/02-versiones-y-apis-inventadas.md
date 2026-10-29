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

=== esquema
# Causas
- Mezcla de versiones — el modelo vio React Router v5 y v7 a la vez.
- Paradigma antiguo — NgModules, pages/, componentes de clase.
# Soluciones
- Decir versión y paradigma — "Next 15 App Router".
- .d.ts real — node_modules/<pkg>/dist/*.d.ts es la verdad.
- npm ls — qué versión está instalada de verdad.
=== test
? Una API "no hace nada" o "is not a function". ¿Primera sospecha?
* Código de otra versión de la librería
- Un fallo del navegador
- La memoria RAM
! Los modelos mezclan APIs de versiones distintas.
? ¿Cuál es la fuente de verdad de los tipos de tu versión?
- El primer resultado de un buscador
* El .d.ts dentro de node_modules
- Una respuesta de foro antigua
! Es exactamente el código instalado.
? ¿Qué haces ante un error de tipos que revela una API inexistente?
- as any para silenciarlo
* Entender el tipo real y corregir el uso
- Desactivar TypeScript
! Callarlo oculta el problema, no lo arregla.
