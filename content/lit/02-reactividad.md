---
title: Propiedades reactivas
desc: "@property, @state, cuándo se re-renderiza y la trampa de los class fields."
pkgs: lit
---
## Pública o interna
- `@property()` / `static properties`: API de entrada del componente.
- `@state()`: estado interno, sin atributo, privado.

Opciones de `@property`: `attribute` (nombre o `false`), `type`, `converter`, `reflect`, `hasChanged` (por defecto `!==`), `noAccessor`, `state`.

## Flujo
setter → `requestUpdate()` → compara con `hasChanged` → si cambió, **actualización asíncrona agrupada (microtask)** → `update()` → `render()`.

## Mutar no dispara render
Misma referencia, mismo valor, ningún render.
```ts
// mal: this.items.push(x)
this.items = [...this.items, x];          // preferido (inmutable)
// o, si mutas:
this.items.push(x); this.requestUpdate();
```

## La trampa de los class fields
Un campo de clase JS sombrea el accessor del prototipo y deja de ser reactivo.

| Entorno | Solución |
|---|---|
| TypeScript con decoradores experimentales | `"useDefineForClassFields": false` |
| Sin esa opción | `declare name: string;` |
| Decoradores estándar (TS 5.2+) | keyword `accessor` |

```ts
@property() accessor name = 'x';   // decoradores estándar
```

## Atributos
- Nombre por defecto = propiedad en minúsculas (`fooBar` → `foobar`).
- Booleanos: empiezan en `false` para poder ponerlos en el markup.
- `reflect: true` solo si lo necesitas en CSS (`:host([active])`). Nunca con objetos o arrays.
- Valores derivados: `willUpdate`, no un setter a mano.

> [!WARN] Síntoma clásico
> "Cambio el dato y la UI no se actualiza": casi siempre es mutación en sitio o un class field que sombrea el accessor.
