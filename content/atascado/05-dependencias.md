---
title: Dependencias que no cuadran
desc: Dependencias incompatibles en proyectos JavaScript, con pasos para resolver errores ERESOLVE, versiones duplicadas y problemas de lockfile.
---
## ERESOLVE / peer dependency
`npm` dice que A necesita React 18 y tienes 19.
1. Lee **qué paquete** pide qué versión; ¿hay una versión nueva de ese paquete que lo soporte?
2. Actualiza ese paquete o espera su release; mira sus issues.
3. `--legacy-peer-deps` o `overrides` son parches: documenta por qué los pones.

```json
{ "overrides": { "paquete-viejo": { "react": "$react" } } }
```

## Dos copias del mismo paquete
Síntomas: `instanceof` falla, contexto de React vacío, **Lit "ya definido"** (`customElements.define` dos veces), hooks inválidos.
```bash
npm ls lit react            # busca "deduped" o varias versiones
npm dedupe
```
En monorepos, declara la librería como `peerDependency` en el paquete compartido.

## Lockfile
- Commitéalo (`package-lock.json`, `pnpm-lock.yaml`).
- En CI usa `npm ci`, que respeta el lock y falla si no cuadra.
- Borrar `node_modules` y lock "para arreglarlo" cambia versiones de todo: último recurso.

## ESM vs CommonJS
`require() of ES Module not supported` / `Cannot use import statement outside a module`:
- Pon `"type": "module"` en `package.json` o usa extensión `.mjs`.
- En TS, alinea `module` y `moduleResolution` (`NodeNext` o `Bundler`) con lo que ejecuta tu runtime.
- Los imports relativos en ESM nativo llevan extensión (`./util.js`).

## Antes de añadir una dependencia
`npm view <pkg>`: última publicación, mantenedores, tamaño. Si lo sugirió la IA, confirma que existe y es el paquete que crees (ver [slopsquatting](@/seguridad/dependencias)).

=== esquema
# Conflictos
- ERESOLVE — un paquete pide otra versión de un peer.
- Dos copias — instanceof falla o Lit define dos veces.
- overrides — parche documentado, no solución.
# Disciplina
- Lockfile commiteado — npm ci en CI.
- ESM vs CJS — type module o .mjs; extensión en imports relativos.
=== test
? ¿Qué hace npm ci en CI?
* Instala exactamente lo del lockfile y falla si no cuadra
- Actualiza todo a latest
- Borra node_modules sin instalar
! Da builds reproducibles.
? "Cannot use import statement outside a module". ¿Arreglo habitual?
- Cambiar de IDE
* "type": "module" o extensión .mjs
- Quitar el import
! Alinea el tipo de módulo con lo que ejecuta tu runtime.
? Borrar node_modules y el lockfile "para arreglarlo" es…
- La primera solución recomendada
* Último recurso: cambia versiones de todo
- Imprescindible cada semana
! Mejor entender qué paquete pide qué versión.
