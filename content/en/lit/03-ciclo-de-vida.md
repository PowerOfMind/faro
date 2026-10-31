---
title: Lifecycle
desc: Lit lifecycle callbacks determine when components render and update. Follow their order and learn where to put setup and derived values.
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
  this.startListeners();
}
```
* super.connectedCallback()
- super()
- this.connected()
- super.render()
! You must always call super.connectedCallback() so Lit creates the renderRoot and starts the update cycle.
? Cancel the update if the required identifier is missing:
```js
___(changes) {
  return Boolean(this.id);
}
```
* shouldUpdate
- willUpdate
- beforeUpdate
- canRender
! shouldUpdate(changes) controls whether the render continues; if it returns false, the cycle stops.
? Compute derived values just before render without causing an extra cycle:
```js
___(changes) {
  if (changes.has('price') || changes.has('vat')) {
    this.total = this.price * (1 + this.vat);
  }
}
```
* willUpdate
- updated
- firstUpdated
- render
! willUpdate(changes) runs before render(); modifying properties here schedules no second cycle.
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
updated(changes) {
  const previous = changes.___
  console.log(`From ${previous} to ${this.count}`);
}
```
* get('count')
- has('count')
- count
- old('count')
! changes is a Map where changes.get('prop') returns the value the property had before updating.
=== prueba
## The lifecycle, in the console
Press the component's button to change `n`, and remove / re-add the element in the DOM. Read the order of the logs.
```html
<div id="host"><my-cycle></my-cycle></div>
<p><button id="q">Remove from DOM</button> <button id="p">Put it back</button></p>
```
```js
import {LitElement, html} from 'lit';

class MyCycle extends LitElement {
  static properties = { n: {type: Number} };
  constructor() { super(); console.log('constructor'); this.n = 0; }
  connectedCallback() { super.connectedCallback(); console.log('connectedCallback'); }
  disconnectedCallback() { super.disconnectedCallback(); console.log('disconnectedCallback'); }
  shouldUpdate(c) { console.log('shouldUpdate  changed:', [...c.keys()].join(', ')); return true; }
  willUpdate()    { console.log('willUpdate'); }
  render()        { console.log('render  (n = ' + this.n + ')'); return html`<button @click=${() => this.n++}>n = ${this.n}</button>`; }
  firstUpdated()  { console.log('firstUpdated  (first time only)'); }
  updated(c)      { console.log('updated  changed:', [...c.keys()].join(', ')); }
}
customElements.define('my-cycle', MyCycle);

const el = document.querySelector('my-cycle');
document.getElementById('q').onclick = () => el.remove();
document.getElementById('p').onclick = () => document.getElementById('host').append(el);
```
Reto: return `false` in shouldUpdate when `this.n > 3` and notice there is no render or updated any more.
Clave: Order: constructor → connectedCallback → shouldUpdate → willUpdate → render → firstUpdated → updated.

## Derived values: willUpdate vs updated
`full` is computed in willUpdate: typing in each input produces a single updated. Watch the console.
```html
<my-name></my-name>
```
```js
import {LitElement, html} from 'lit';

class MyName extends LitElement {
  static properties = {
    first: {}, last: {},
    full: {state: true},
  };
  constructor() { super(); this.first = 'Ada'; this.last = 'Lovelace'; this.cycles = 0; }

  willUpdate(changes) {                       // deriving here does NOT cause another cycle
    if (changes.has('first') || changes.has('last')) {
      this.full = `${this.first} ${this.last}`;
    }
  }
  updated() { this.cycles++; console.log('updated #', this.cycles); }

  render() {
    return html`
      <input .value=${this.first} @input=${(e) => (this.first = e.target.value)}>
      <input .value=${this.last}  @input=${(e) => (this.last = e.target.value)}>
      <p>Full name: <b>${this.full}</b></p>`;
  }
}
customElements.define('my-name', MyName);
```
Reto: move the computation of `full` into `updated()` (with an `if` on `changes`): you will see two `updated` per keystroke, because changing a property there schedules another cycle.
Clave: Derived values in willUpdate (no extra cycle). Changing properties in updated schedules another cycle: guard it with changed.has().
