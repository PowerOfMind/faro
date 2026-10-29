---
title: Reactive properties
desc: "@property, @state, when it re-renders and the class fields trap."
pkgs: lit
---
## Public or internal
- `@property()` / `static properties`: the component's input API.
- `@state()`: internal state, no attribute, private.

`@property` options: `attribute` (name or `false`), `type`, `converter`, `reflect`, `hasChanged` (default `!==`), `noAccessor`, `state`.

## Flow
setter → `requestUpdate()` → compare with `hasChanged` → if changed, **batched async update (microtask)** → `update()` → `render()`.

## Mutating does not trigger a render
Same reference, same value, no render.
```ts
// bad: this.items.push(x)
this.items = [...this.items, x];          // preferred (immutable)
// or, if you mutate:
this.items.push(x); this.requestUpdate();
```

## The class fields trap
A JS class field shadows the prototype accessor and stops being reactive.

| Environment | Fix |
|---|---|
| TypeScript with experimental decorators | `"useDefineForClassFields": false` |
| Without that option | `declare name: string;` |
| Standard decorators (TS 5.2+) | the `accessor` keyword |

```ts
@property() accessor name = 'x';   // standard decorators
```

## Attributes
- Default name = the property in lowercase (`fooBar` → `foobar`).
- Booleans: start at `false` so they can be set in markup.
- `reflect: true` only if you need it in CSS (`:host([active])`). Never with objects or arrays.
- Derived values: `willUpdate`, not a hand-written setter.

> [!WARN] Classic symptom
> "I change the data and the UI does not update": almost always in-place mutation or a class field shadowing the accessor.

=== esquema
# Declaration
- @property — declares an input visible from outside, like the name typed into a tag.
- @state — declares internal data, like whether a menu is open; it creates no HTML attribute.
- static properties — the equivalent of decorators without a compiler.
# Options
- attribute — sets the attribute name, or false for none.
- type and converter — convert the HTML text into a JS value, like "3" to 3.
- reflect — copies the property back to the attribute.
- hasChanged — decides whether there is a change; by default compares with !==.
# Updating
- Setter — calls requestUpdate().
- Multiple changes — give a single render per microtask.
- Mutating arrays — needs a new list or requestUpdate(): changing a page of the notebook without changing the notebook is not detected.
# Traps
- Class fields — shadow prototype accessors and remove reactivity.
- Booleans — must start at false so they can be set from markup.
- Reflecting objects — avoid it; it only makes sense with simple types.
=== test
? Declare _open as internal state that triggers render but creates NO HTML attribute:
```js
static properties = {
  _open: { ___: true }
};
```
* state
- internal
- private
- noAttribute
! state: true defines a private reactive property that syncs with no HTML attribute.
? Make the attribute in the DOM update when the property changes in JS (<my-tag active>):
```js
static properties = {
  active: { type: Boolean, ___: true }
};
```
* reflect
- sync
- attribute
- mirror
! reflect: true writes property changes back to the HTML attribute.
? Say that items is a complex Array and must not be read from an HTML attribute:
```js
static properties = {
  items: { ___: false }
};
```
* attribute
- reflect
- type
- converter
! attribute: false turns off reading from HTML attributes, ideal for objects and complex arrays.
? Add an element to the list guaranteeing a new reference so Lit detects the change:
```js
add(next) {
  this.items = ___
}
```
* [...this.items, next];
- this.items.push(next);
- this.items.concat();
- Object.assign(this.items, next);
! Lit uses a !== check. Mutating with .push() keeps the same memory reference and does not trigger the render.
? Configure a custom hasChanged that only triggers a render when the value is greater than zero:
```js
static properties = {
  points: {
    type: Number,
    ___: (next, prev) => next > 0 && next !== prev
  }
};
```
* hasChanged
- shouldChange
- isDifferent
- compare
! hasChanged defines the function that decides whether a value change should trigger an update.
=== prueba
## Attribute ↔ property, type and reflect
The `value` property is a Number and is reflected to the attribute. Compare what happens when you change the property or the attribute.
```html
<my-bar value="30"></my-bar>
<p><button id="a">property: value += 10</button> <button id="b">setAttribute('value', 80)</button></p>
<pre id="h"></pre>
```
```js
import {LitElement, html, css} from 'lit';

class MyBar extends LitElement {
  static properties = { value: {type: Number, reflect: true} };
  static styles = css`
    .track { background: var(--surface-2); border-radius: 8px; height: 18px; overflow: hidden }
    .fill { background: var(--primary); height: 100%; transition: width .3s }`;
  render() {
    return html`<div class="track"><div class="fill" style="width:${this.value}%"></div></div>
      <small>value (property): ${this.value} · typeof ${typeof this.value}</small>`;
  }
}
customElements.define('my-bar', MyBar);

const $ = (id) => document.getElementById(id);
const el = document.querySelector('my-bar');
const show = () => el.updateComplete.then(() => { $('h').textContent = el.outerHTML; });
$('a').onclick = () => { el.value += 10; show(); };
$('b').onclick = () => { el.setAttribute('value', 80); show(); };
show();
```
Reto: remove `reflect: true` and check that changing the property no longer updates the HTML attribute.
Clave: The attribute is a string; `type: Number` converts it to a property. `reflect` copies property → attribute (use it sparingly).

## Mutating an array does not re-render
Three buttons: mutate with push, create a new reference (the right way) and push + requestUpdate().
```html
<my-list></my-list>
```
```js
import {LitElement, html} from 'lit';

class MyList extends LitElement {
  static properties = { items: {type: Array} };
  constructor() { super(); this.items = ['one']; this.renders = 0; }

  render() {
    this.renders++;
    return html`
      <p>render #${this.renders} · ${this.items.length} items</p>
      <ul>${this.items.map((i) => html`<li>${i}</li>`)}</ul>
      <button @click=${this.bad}>push (bad)</button>
      <button @click=${this.good}>new reference (good)</button>
      <button @click=${this.okay}>push + requestUpdate()</button>`;
  }
  bad()  { this.items.push('bad ' + this.items.length); console.log('push without reassigning → no render'); }
  good() { this.items = [...this.items, 'good ' + this.items.length]; }
  okay() { this.items.push('rU ' + this.items.length); this.requestUpdate(); }
}
customElements.define('my-list', MyList);
```
Reto: press "push (bad)" three times: nothing happens. Then press "new reference (good)": they all appear at once (the render reads the current array).
Clave: Lit compares by reference (!==). Mutating does not change the reference: reassign (immutable) or call requestUpdate().
