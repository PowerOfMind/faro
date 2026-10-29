---
title: Lifecycle
desc: The exact order of the callbacks and what to put in each.
pkgs: lit
---
## First render, in order
1. `constructor()`: default values.
2. `connectedCallback()`: creates the shadow root and starts the update. External listeners (`window`).
3. `shouldUpdate(changed)`: if it returns `false`, the rest is skipped.
4. `willUpdate(changed)`: **derived values**. Changing props here does not cause another cycle.
5. `update(changed)`: reflects attributes and calls `render()`.
6. `render()`: returns the template. It must be pure.
7. `firstUpdated(changed)`: **only once** (focus, measure the DOM).
8. `updated(changed)`: after every render.
9. `updateComplete` (Promise) resolves.

```ts
willUpdate(changed: PropertyValues) {
  if (changed.has('items')) this.total = this.items.reduce((s, i) => s + i.price, 0);
}
updated(changed: PropertyValues) {
  if (changed.has('open') && this.open) this.shadowRoot!.querySelector('input')?.focus();
}
```

## Rules
- Changing a prop in `updated()` schedules another cycle: guard it with `changed.has(...)` or you get an infinite loop.
- `changedProperties` is a `Map` with the **previous value**; the current one is read with `this.prop`.
- Always call `super.connectedCallback()` / `super.disconnectedCallback()`.
- Clean up timers and global listeners in `disconnectedCallback()`. Template listeners do not need it.
- `await this.updateComplete` before reading the DOM in tests, or before dispatching an event that describes rendered state.
- `hasUpdated` indicates the first render has happened.

> [!NOTE] SSR
> On the server only `willUpdate` and `render` run. `firstUpdated`, `updated` and `update` do not.

=== esquema
# Element callbacks
- constructor — requests the first update and sets defaults; packing the bag before leaving.
- connectedCallback — creates the renderRoot and starts the first update; external listeners go here.
- disconnectedCallback — cleans up listeners and timers; the update pauses until reconnect.
# Update cycle
- shouldUpdate — decides whether the screen needs updating, like checking something changed before printing a sheet.
- willUpdate — computes derived values before rendering, like adding up the subtotal before showing the invoice.
- update and render — produce the DOM: update reflects attributes and calls render.
- firstUpdated and updated — run after the DOM; firstUpdated only once.
# Care
- Changing props in updated — schedules another cycle: use changed.has to avoid loops.
- Changing props in willUpdate — schedules no other cycle, which is why it is ideal for derived values.
- updateComplete — lets you wait for the render before reading the DOM or dispatching events.
=== test
? Start Lit's lifecycle when the element connects to the DOM:
```js
connectedCallback() {
  ___;
  this.iniciarListeners();
}
```
* super.connectedCallback()
- super()
- this.connected()
- super.render()
! You must always call super.connectedCallback() so Lit creates the renderRoot and starts the update cycle.
? Cancel the update if the required identifier is missing:
```js
___(cambios) {
  return Boolean(this.id);
}
```
* shouldUpdate
- willUpdate
- beforeUpdate
- canRender
! shouldUpdate(cambios) controls whether the render continues; if it returns false, the cycle stops.
? Compute derived values just before render without causing an extra cycle:
```js
___(cambios) {
  if (cambios.has('precio') || cambios.has('iva')) {
    this.total = this.precio * (1 + this.iva);
  }
}
```
* willUpdate
- updated
- firstUpdated
- render
! willUpdate(cambios) runs before render(); modifying properties here schedules no second cycle.
? Access the created DOM right after the first render:
```js
___() {
  this.renderRoot.querySelector('input').focus();
}
```
* firstUpdated
- connectedCallback
- updated
- renderComplete
! firstUpdated() runs only once, after the element has rendered its DOM for the first time.
? Look up the value the property had before the current update:
```js
updated(cambios) {
  const anterior = cambios.___
  console.log(`De ${anterior} a ${this.cuenta}`);
}
```
* get('cuenta')
- has('cuenta')
- cuenta
- old('cuenta')
! cambios is a Map where cambios.get('prop') returns the value the property had before updating.
=== prueba
## The lifecycle, in the console
Press the component's button to change `n`, and remove / re-add the element in the DOM. Read the order of the logs.
Reto: return `false` in shouldUpdate when `this.n > 3` and notice there is no render or updated any more.
Clave: Order: constructor → connectedCallback → shouldUpdate → willUpdate → render → firstUpdated → updated.
## Derived values: willUpdate vs updated
`completo` is computed in willUpdate: typing in each input produces a single updated. Watch the console.
Reto: move the computation of `completo` into `updated()` (with an `if` on `cambios`): you will see two `updated` per keystroke, because changing a property there schedules another cycle.
Clave: Derived values in willUpdate (no extra cycle). Changing properties in updated schedules another cycle: guard it with changed.has().
