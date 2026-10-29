---
title: Tipos utilidad y genéricos
desc: Partial, Pick, Omit, Record, ReturnType, satisfies y friends.
pkgs: typescript
---
## Los de uso diario
| Utilidad | Resultado |
|---|---|
| `Partial<T>` | Todas las propiedades opcionales |
| `Required<T>` | Todas obligatorias |
| `Readonly<T>` | Solo lectura |
| `Pick<T, 'a' \| 'b'>` | Solo esas claves |
| `Omit<T, 'a'>` | Todas menos esas |
| `Record<K, V>` | Objeto con claves K y valores V |
| `ReturnType<typeof f>` | Tipo que devuelve `f` |
| `Parameters<typeof f>` | Tupla de parámetros |
| `Awaited<Promise<T>>` | `T` |
| `NonNullable<T>` | Sin `null` ni `undefined` |

```ts
type UpdateUser = Partial<Omit<User, 'id'>>;
const labels: Record<Estado, string> = { idle: 'Listo', loading: 'Cargando', error: 'Error' };
```

## Derivar tipos de valores
```ts
const ROLES = ['admin', 'user'] as const;
type Rol = typeof ROLES[number];            // 'admin' | 'user'
type Clave = keyof typeof cfg;
```

## `satisfies`
Valida contra un tipo **sin ensanchar** el literal:
```ts
const rutas = { home: '/', about: '/sobre' } satisfies Record<string, string>;
rutas.home;   // sigue siendo '/' , no string
```

## Genéricos con restricción
```ts
function pluck<T, K extends keyof T>(items: T[], key: K): T[K][] { return items.map(i => i[key]); }
```

## Condicionales y mapeados (cuando haga falta)
```ts
type Nullable<T> = { [K in keyof T]: T[K] | null };
type ElementOf<T> = T extends (infer U)[] ? U : never;
```
Si un tipo necesita cinco líneas de magia, probablemente conviene simplificar el diseño.

=== esquema
# Utilidades
- Partial y Required — propiedades opcionales u obligatorias.
- Pick y Omit — quedarse con o quitar claves.
- Record — objeto con claves K y valores V.
- ReturnType y Parameters — de una función.
- Awaited — el valor de una promesa.
# Derivar
- typeof ROLES[number] — unión desde un array as const.
- satisfies — comprueba sin ensanchar.
=== test
? ¿Qué hace Omit<User, 'id'>?
* Todas las propiedades menos id
- Solo id
- Hace id opcional
! Es el complemento de Pick.
? Sacar la unión de valores de un array as const:
- typeof ROLES
* typeof ROLES[number]
- keyof ROLES
! Indexar con number da el tipo de los elementos.
? ¿Qué aporta satisfies?
* Valida contra un tipo sin perder el literal
- Convierte a any
- Ejecuta código
! Mantiene tipos precisos.
