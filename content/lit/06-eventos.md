---
title: Eventos
desc: Escuchar, despachar, bubbles/composed y retargeting.
pkgs: lit
---
## Escuchar
```ts
html`<button @click=${this._onClick}>OK</button>`
@eventOptions({passive: true}) _onScroll(e) {}
```
Listeners globales: añade en `connectedCallback`, quita en `disconnectedCallback`. Usa arrow functions como campos para conservar `this`.

## Despachar
```ts
this.dispatchEvent(new CustomEvent('item-selected', {
  detail: {id}, bubbles: true, composed: true,
}));
```
- `bubbles`: sube por el árbol.
- `composed`: cruza el límite del shadow DOM.
- Para que un ancestro lo escuche normalmente necesitas **ambos**.

## Retargeting
Desde fuera, `e.target` es el host. El origen real: `e.composedPath()[0]`.

## Buenas reglas
- **Props hacia abajo, eventos hacia arriba.**
- No despaches un evento porque el dueño cambió una propiedad (como `input.value = x` no dispara `change`). Sí cuando actúa el usuario o termina algo asíncrono.
- Si el evento describe estado renderizado: `await this.updateComplete` antes de despachar.
- Delegación: un listener en el ancestro leyendo `e.target`, solo para eventos que burbujean.

> [!WARN] "Mi evento no llega"
> El 90 % de las veces falta `composed: true`, o el listener se registró en otro nodo que el que emite.
