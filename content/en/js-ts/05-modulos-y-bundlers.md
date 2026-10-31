---
title: Modules and bundlers
desc: A practical guide to modules and bundlers, common mistakes, decisions, and checks to help you solve problems with confidence.
pkgs: vite, typescript
---
## ESM and CommonJS
ESM uses `import` and `export`; CommonJS uses `require` and `module.exports`. The runtime and configuration determine how each file is interpreted. In HTML, a native module uses `<script type="module">`.

## Loading and Vite
`import('./module.js')` returns a promise and supports on-demand loading. Vite serves modules during development and produces a production build; check the project's scripts and configuration.

## TypeScript
`moduleResolution` should match the runtime: `bundler` for a compatible bundler; `node16` or `nodenext` for the corresponding Node modes. Also check `module`, file extensions and the package `type` field.

## Quick decisions
| Question | Answer |
|---|---|
| Which syntax does ESM use? | import and export |
| What does dynamic import return? | A promise |
| How is an HTML module declared? | With script type="module" |

> [!AI] With AI
> Describe your version, environment, expected and actual results, and a minimal reproduction. Ask for a testable explanation and references to the official documentation.

Documentation: [official guide](https://vite.dev/guide/).

Related: [continue with a related guide](@/js-ts/testing-con-vitest-y-playwright).

=== esquema
# Key ideas
- ESM and CommonJS — ESM uses `import` and `export`; CommonJS uses `require` and `module.exports`.
- Loading and Vite — `import('./module.js')` returns a promise and supports on-demand loading.
- TypeScript — `moduleResolution` should match the runtime: `bundler` for a compatible bundler; `node16` or `nodenext` for the corresponding Node modes.
=== test
? Which syntax does ESM use?
* import and export
- A promise
- With script type="module"
! import and export.
? What does dynamic import return?
* A promise
- With script type="module"
- Development and production bundling
! A promise.
? How is an HTML module declared?
* With script type="module"
- Development and production bundling
- The environment resolving modules
! With script type="module".
? What is Vite used for?
* Development and production bundling
- The environment resolving modules
- import and export
! Development and production bundling.
? What should moduleResolution reflect?
* The environment resolving modules
- import and export
- A promise
! The environment resolving modules.

=== prueba

## Dynamic import
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
Reto: change the exported message.

## Handle an import error
```js
try {
  await import('data:text/javascript,throw%20new%20Error(%22Module%20failed%22)');
} catch (error) {
  console.error('Could not load module:', error.message);
}
```
Reto: change the error message.
