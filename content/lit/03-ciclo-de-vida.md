---
title: Ciclo de vida
desc: Orden exacto de los callbacks y qué poner en cada uno.
pkgs: lit
---
## Primer render, en orden
1. `constructor()`: valores por defecto.
2. `connectedCallback()`: crea el shadow root y arranca la actualización. Listeners externos (`window`).
3. `shouldUpdate(changed)`: si devuelve `false`, se salta lo demás.
4. `willUpdate(changed)`: **valores derivados**. Cambiar props aquí no provoca otro ciclo.
5. `update(changed)`: refleja atributos y llama a `render()`.
6. `render()`: devuelve la plantilla. Debe ser pura.
7. `firstUpdated(changed)`: **una sola vez** (foco, medir DOM).
8. `updated(changed)`: tras cada render.
9. `updateComplete` (Promise) se resuelve.

```ts
willUpdate(changed: PropertyValues) {
  if (changed.has('items')) this.total = this.items.reduce((s, i) => s + i.price, 0);
}
updated(changed: PropertyValues) {
  if (changed.has('open') && this.open) this.shadowRoot!.querySelector('input')?.focus();
}
```

## Reglas
- Cambiar una prop en `updated()` programa otro ciclo: protégelo con `changed.has(...)` o tendrás un bucle infinito.
- `changedProperties` es un `Map` con el **valor anterior**; el actual se lee con `this.prop`.
- Llama siempre a `super.connectedCallback()` / `super.disconnectedCallback()`.
- Limpia timers y listeners globales en `disconnectedCallback()`. Los del template no hace falta.
- `await this.updateComplete` antes de leer el DOM en tests o antes de despachar un evento que describe estado renderizado.
- `hasUpdated` indica que ya hubo primer render.

> [!NOTE] SSR
> En el servidor solo corren `willUpdate` y `render`. `firstUpdated`, `updated` y `update` no.
