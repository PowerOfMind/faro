---
title: Módulos y bundlers
desc: Guía práctica de módulos y bundlers, errores frecuentes, decisiones y comprobaciones para resolver problemas con criterio.
pkgs: vite, typescript
---
## ESM y CommonJS
ESM usa `import` y `export`; CommonJS usa `require` y `module.exports`. El entorno y la configuración determinan cómo se interpreta cada archivo. En HTML, un módulo nativo usa `<script type="module">`.

## Carga y Vite
`import('./modulo.js')` devuelve una promesa y permite cargar código bajo demanda. Vite sirve módulos durante desarrollo y genera una salida para producción; comprueba los scripts y configuración del proyecto.

## TypeScript
`moduleResolution` debe reflejar el ejecutor: `bundler` para un bundler compatible; `node16` o `nodenext` para los modos correspondientes de Node. Revisa también `module`, extensiones y el campo `type` del paquete.

## Decisiones rápidas
| Pregunta | Respuesta |
|---|---|
| ¿Qué sintaxis usa ESM? | import y export |
| ¿Qué devuelve import dinámico? | Una promesa |
| ¿Cómo se declara un módulo en HTML? | Con script type="module" |

> [!AI] Con IA
> Indica la versión, el entorno, el resultado esperado y real, y una reproducción mínima. Pide una explicación comprobable y referencias a la documentación oficial.

Documentación: [guía oficial](https://vite.dev/guide/).

Relacionado: [continúa con otra guía](@/js-ts/testing-con-vitest-y-playwright).

=== esquema
# Ideas clave
- ESM y CommonJS — ESM usa `import` y `export`; CommonJS usa `require` y `module.exports`.
- Carga y Vite — `import('./modulo.js')` devuelve una promesa y permite cargar código bajo demanda.
- TypeScript — `moduleResolution` debe reflejar el ejecutor: `bundler` para un bundler compatible; `node16` o `nodenext` para los modos correspondientes de Node.
=== test
? ¿Qué sintaxis usa ESM?
* import y export
- Una promesa
- Con script type="module"
! import y export.
? ¿Qué devuelve import dinámico?
* Una promesa
- Con script type="module"
- Desarrollo y empaquetado para producción
! Una promesa.
? ¿Cómo se declara un módulo en HTML?
* Con script type="module"
- Desarrollo y empaquetado para producción
- El entorno que resuelve módulos
! Con script type="module".
? ¿Para qué sirve Vite?
* Desarrollo y empaquetado para producción
- El entorno que resuelve módulos
- import y export
! Desarrollo y empaquetado para producción.
? ¿Qué debe reflejar moduleResolution?
* El entorno que resuelve módulos
- import y export
- Una promesa
! El entorno que resuelve módulos.

=== prueba

## Importación dinámica
```js
const source = 'export const message = "Hello from a module";';
const url = URL.createObjectURL(new Blob([source], {type: 'text/javascript'}));
try {
  const module = await import(url);
  console.log(module.message);
} finally {
  URL.revokeObjectURL(url);
}
```
Reto: cambia el mensaje exportado.

## Gestionar un error de importación
```js
try {
  await import('data:text/javascript,throw%20new%20Error(%22Module%20failed%22)');
} catch (error) {
  console.error('Could not load module:', error.message);
}
```
Reto: cambia el mensaje de error.
