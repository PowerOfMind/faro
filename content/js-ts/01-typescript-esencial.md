---
title: TypeScript esencial
desc: Tipos que usarás cada día y los errores más comunes.
pkgs: typescript
---
## Lo básico
```ts
type User = { id: number; name: string; email?: string };      // opcional
interface Repo<T> { get(id: number): Promise<T>; }              // genérico
type Estado = 'idle' | 'loading' | 'error';                     // unión literal
const cfg = { mode: 'dark' } as const;                          // inmutable y literal
function esString(x: unknown): x is string { return typeof x === 'string'; }  // type guard
```

## `type` o `interface`
Para objetos da casi igual. `interface` se puede extender y fusionar; `type` sirve para uniones, tuplas y tipos calculados. Elige una y sé coherente.

## `unknown` mejor que `any`
`any` apaga el chequeo. `unknown` obliga a comprobar antes de usar. Datos externos (JSON, `fetch`) son `unknown`: **valídalos** con Zod/Valibot, porque los tipos no existen en ejecución.

## Uniones discriminadas
```ts
type Res = {ok: true; data: string} | {ok: false; error: Error};
function f(r: Res) { if (r.ok) r.data; else r.error; }   // TS estrecha el tipo
```

## Errores típicos
| Mensaje | Causa y arreglo |
|---|---|
| `Object is possibly 'undefined'` | Comprueba antes, `?.`, `??`; evita `!` salvo certeza |
| `Type 'X' is not assignable to 'Y'` | Revisa la forma; no lo silencies con `as any` |
| `Cannot find module` | `moduleResolution`, paths, o falta `@types/...` |
| `Property does not exist on type` | El tipo es demasiado ancho: estréchalo |
| Funciona en el editor, falla en build | Versiones distintas de TS; usa la del proyecto |

## `tsconfig` sensato
```json
{ "compilerOptions": { "strict": true, "target": "ES2022", "module": "ESNext",
  "moduleResolution": "Bundler", "noUncheckedIndexedAccess": true, "skipLibCheck": true } }
```

> [!NOTE] TypeScript 7
> La línea 7.x es el compilador reescrito en código nativo (mucho más rápido). Si migras, revisa las notas de la versión: algunas opciones antiguas de `tsconfig` se han retirado o cambiado. El lenguaje y los tipos de esta página no cambian.

> [!AI] Atajos peligrosos
> Ante un error de tipos, la IA a menudo añade `as any` o `// @ts-ignore`. Pídele que entienda el tipo real en vez de callarlo.

=== esquema
# Tipos
- unknown — obliga a comprobar; mejor que any.
- Unión discriminada — estrecha el tipo con una propiedad.
- as const — literales inmutables.
- satisfies — valida sin ensanchar.
# Datos externos
- JSON y fetch — son unknown; valida con Zod o Valibot.
- tsconfig — strict y noUncheckedIndexedAccess.
=== test
? ¿Por qué unknown antes que any?
* Obliga a comprobar el tipo antes de usarlo
- Es más rápido
- Desactiva el chequeo
! any apaga TypeScript; unknown lo mantiene.
? Los tipos de TypeScript, ¿existen en ejecución?
- Sí
* No: por eso los datos externos se validan
- Solo en producción
! Se borran al compilar.
? Error "possibly undefined". ¿Solución?
* Comprobar antes, ?. o ??
- Añadir as any
- Usar @ts-ignore
! Silenciarlo oculta un fallo real.
