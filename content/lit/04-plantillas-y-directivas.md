---
title: Plantillas y directivas
desc: Los 4 tipos de binding, listas, condicionales y las directivas que sí se usan.
pkgs: lit
---
## Regla de oro del binding
| Sintaxis | Qué hace |
|---|---|
| `attr=${x}` | atributo (string) |
| `?attr=${bool}` | añade o quita el atributo |
| `.prop=${obj}` | propiedad JS, sin serializar |
| `@evt=${fn}` | listener (`this` ya es el componente) |

```ts
html`<my-list .items=${this.items} ?disabled=${this.busy} @select=${this._onSelect}></my-list>`
```

- `nothing`: no renderiza o quita el atributo. `ifDefined(x)` = `x ?? nothing`.
- Condicionales: ternario, `&&` o `when(cond, () => a, () => b)`.
- No se puede enlazar el nombre de una etiqueta o atributo (usa `static-html` con `literal`), ni dentro de `<textarea>` (usa `.value`).

## Listas: map o repeat
```ts
html`<ul>${this.items.map(i => html`<li>${i.name}</li>`)}</ul>`
html`<ul>${repeat(this.items, i => i.id, i => html`<li>${i.name}</li>`)}</ul>`
```
`map` actualiza en sitio (más ligero). `repeat` con clave conserva la identidad del DOM al reordenar (inputs con foco, animaciones).

## Directivas útiles
| Necesidad | Directiva |
|---|---|
| Clases / estilos dinámicos | `classMap`, `styleMap` |
| Valor real del input | `live` |
| Recrear al cambiar una clave | `keyed` |
| Conservar DOM al alternar vistas | `cache` |
| Recalcular solo con dependencias | `guard` |
| Referencia a un elemento | `ref` |
| Promesas / streams | `until`, `asyncAppend` |

```ts
html`<input .value=${live(this.q)} @input=${e => this.q = e.target.value}>`
html`<div class=${classMap({active: this.on, big: this.size > 1})}></div>`
```

> [!SEC] XSS
> Lit escapa por defecto. `unsafeHTML` y `unsafeStatic` solo con contenido que controlas.
