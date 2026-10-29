---
title: Estilos, Shadow DOM y slots
desc: Encapsulación, theming desde fuera con variables y ::part, y slots.
pkgs: lit
---
## Estilos
```ts
static styles = css`
  :host { display: block; }
  :host([active]) { outline: 2px solid var(--accent, royalblue); }
  ::slotted(p) { margin: 0; }
`;
```
- Se evalúan **una vez por clase** y usan `adoptedStyleSheets`.
- Dentro de `css` solo van valores `css` o números. Strings con `unsafeCSS`.
- Herencia: `static styles = [Super.styles, css`...`]`.

## Theming desde fuera (de más a menos recomendable)
1. **Herencia CSS**: `color`, `font-*` y variables atraviesan el shadow.
2. **Custom properties** con fallback: `var(--mi-color, yellow)`.
3. **`::part()`**: marca `part="boton"` dentro y estila `mi-el::part(boton)` fuera.

## Slots
```html
<slot></slot>
<slot name="footer">Contenido por defecto</slot>
```
- El contenido dentro del `<slot>` es el *fallback*.
- Evento `slotchange`; `slot.assignedElements({flatten: true})`.
- `::slotted()` solo alcanza hijos directos.

## Acceder al DOM interno
`@query('#x')`, `@queryAll`, `@queryAsync`, `@queryAssignedElements`. Evita `document.querySelector`: no entra en el shadow.

## Sin Shadow DOM
```ts
createRenderRoot() { return this; }
```
Pierdes encapsulación de estilos y slots. Útil para integrar con CSS global (Tailwind).

> [!TIP] Foco en formularios
> `static shadowRootOptions = {...LitElement.shadowRootOptions, delegatesFocus: true}` hace que el foco del host pase al primer control interno.

> [!AI] Tailwind + Shadow DOM
> Los estilos globales no entran en el shadow. La IA suele olvidarlo: o usas light DOM o inyectas la hoja compilada en `static styles`.
