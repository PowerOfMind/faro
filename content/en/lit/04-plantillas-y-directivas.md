---
title: Templates and directives
desc: Lit templates bind attributes, properties and events to data. Explore conditionals, list identity and directives for common UI patterns.
pkgs: lit
---
## The golden rule of binding
| Syntax | What it does |
|---|---|
| `attr=${x}` | attribute (string) |
| `?attr=${bool}` | adds or removes the attribute |
| `.prop=${obj}` | JS property, not serialised |
| `@evt=${fn}` | listener (`this` is already the component) |

```ts
html`<my-list .items=${this.items} ?disabled=${this.busy} @select=${this._onSelect}></my-list>`
```

- `nothing`: renders nothing or removes the attribute. `ifDefined(x)` = `x ?? nothing`.
- Conditionals: ternary, `&&` or `when(cond, () => a, () => b)`.
- You cannot bind a tag or attribute name (use `static-html` with `literal`), nor inside `<textarea>` (use `.value`).

## Lists: map or repeat
```ts
html`<ul>${this.items.map(i => html`<li>${i.name}</li>`)}</ul>`
html`<ul>${repeat(this.items, i => i.id, i => html`<li>${i.name}</li>`)}</ul>`
```
`map` updates in place (lighter). `repeat` with a key keeps DOM identity when reordering (focused inputs, animations).

## Useful directives
| Need | Directive |
|---|---|
| Dynamic classes / styles | `classMap`, `styleMap` |
| The real input value | `live` |
| Recreate when a key changes | `keyed` |
| Keep the DOM when toggling views | `cache` |
| Recompute only with dependencies | `guard` |
| A reference to an element | `ref` |
| Promises / streams | `until`, `asyncAppend` |

```ts
html`<input .value=${live(this.q)} @input=${e => this.q = e.target.value}>`
html`<div class=${classMap({active: this.on, big: this.size > 1})}></div>`
```

> [!SEC] XSS
> Lit escapes by default. `unsafeHTML` and `unsafeStatic` only with content you control.

=== esquema
# Bindings
- attr=${x} — puts text in the tag, like writing the title on a sticker.
- ?attr=${x} — adds or removes a yes/no option, like ticking or unticking a box.
- .prop=${x} — assigns the original JS value, like handing over a whole list instead of copying it into a note.
- @event=${fn} — registers an action for when something happens, like a bell that rings when pressed.
# Children
- Primitives — shown as text; null, undefined and '' render nothing.
- TemplateResult — nested with templates inside templates.
- Arrays and iterables — rendered element by element, in order.
# Sentinels and limits
- nothing — removes the content or the whole attribute.
- static-html — allows expressions in tag names with literal.
- Inside textarea — use .value instead of a child expression.
# Style
- classMap — applies classes from a class→boolean object.
- styleMap — applies inline style properties from an object.
# Lists and conditionals
- when — chooses between two templates from a boolean.
- map — walks an iterable without diffing; smaller and faster.
- repeat — keeps DOM identity through a key function.
# Changes
- cache — keeps the DOM of inactive templates to toggle fast.
- keyed — recreates the DOM when its key changes.
- guard — avoids re-evaluating if its dependencies do not change.
- live — compares with the real DOM value, not Lit's last one.
=== test
? Bind the input value as a JavaScript property rather than as an HTML attribute:
```js
html`<input type="text" ___=${this.text}>`;
```
* .value
- value
- ?value
- @value
! The . prefix indicates a binding to a DOM object property (.value=${this.text}).
? Add or remove the boolean attribute disabled depending on state:
```js
html`<button ___=${this.loading}>Send</button>`;
```
* ?disabled
- .disabled
- disabled
- @disabled
! The ? prefix adds the attribute if truthy and removes it entirely if falsy.
? Register a native event listener with lit-html syntax:
```js
html`<button ___=${this._onClick}>Save</button>`;
```
* @click
- onclick
- .click
- ?click
! The @ prefix registers a native listener with addEventListener keeping the this context.
? Render the list reordering the DOM by key:
```js
${___(this.items, (i) => i.id, (i) => html`<li>${i.n}</li>`)}
```
* repeat
- map
- when
- join
! repeat receives the key and moves DOM nodes instead of recreating them.
? Stop Lit from overwriting what the user types in the input:
```js
html`<input .value=${___(this.text)}>`
```
* live
- cache
- keyed
- guard
! live compares with the real DOM value, not the last value Lit rendered.
? Set the attribute only if there is a value:
```js
html`<a href=${___(this.url)}>Go</a>`
```
* ifDefined
- live
- ref
- guard
! ifDefined removes the attribute when the value is undefined.
=== prueba
## The four bindings: attribute, ?boolean, .property, @event
One of each, plus a child that receives an array with `.items` (not serialised to a string).
```html
<demo-bindings></demo-bindings>
```
```js
import {LitElement, html, css} from 'lit';

class ChildList extends LitElement {
  static properties = { items: {type: Array} };
  render() { return html`<p>The child received an array with <code>.items</code>: ${this.items.join(', ')}</p>`; }
}
customElements.define('child-list', ChildList);

class DemoBindings extends LitElement {
  static properties = { name: {}, active: {type: Boolean} };
  static styles = css`.on { color: var(--ok); font-weight: 700 } .off { color: var(--muted) }`;
  constructor() { super(); this.name = 'world'; this.active = false; this.colors = ['red', 'green', 'blue']; }

  render() {
    return html`
      <p>Attribute (string): <span class=${this.active ? 'on' : 'off'} title="Hello ${this.name}">hello ${this.name}</span></p>
      <p>Boolean <code>?</code>: <button ?disabled=${!this.active}>only if active</button></p>
      <p>Property <code>.</code>: <input .value=${this.name} @input=${(e) => (this.name = e.target.value)}></p>
      <p>Event <code>@</code>: <button @click=${() => (this.active = !this.active)}>active = ${String(this.active)}</button></p>
      <child-list .items=${this.colors}></child-list>`;
  }
}
customElements.define('demo-bindings', DemoBindings);
```
Reto: change `.items=${this.colors}` to `items=${this.colors}` (no dot): the array arrives as the string "red,green,blue".
Clave: attr = string · ?attr = boolean · .prop = JS value · @evt = listener (this is already bound to the component).

## Conditionals, lists and `nothing`
A ternary with nested templates, `.map()` and `nothing` to remove an attribute entirely.
```html
<demo-cond></demo-cond>
```
```js
import {LitElement, html, nothing} from 'lit';

class DemoCond extends LitElement {
  static properties = { loggedIn: {type: Boolean}, items: {type: Array}, help: {} };
  constructor() { super(); this.loggedIn = false; this.items = ['a', 'b', 'c']; this.help = ''; }

  render() {
    return html`
      ${this.loggedIn ? html`<p>Welcome 👋</p>` : html`<p>Please sign in</p>`}
      <button @click=${() => (this.loggedIn = !this.loggedIn)}>toggle session</button>

      <ul>${this.items.map((x, i) => html`<li>${i}: ${x}</li>`)}</ul>
      <button @click=${() => (this.items = [...this.items, String.fromCharCode(97 + this.items.length)])}>add</button>

      <p><input placeholder="aria-label text" @input=${(e) => (this.help = e.target.value)}>
         <button aria-label=${this.help || nothing}>button</button></p>
      <p>aria-label in the DOM: <code>${this.help ? this.help : '(none: nothing removed the attribute)'}</code></p>`;
  }
}
customElements.define('demo-cond', DemoCond);
```
Reto: change `this.help || nothing` to `this.help`: with empty text the attribute exists but empty; with `nothing` it disappears.
Clave: `nothing` renders nothing or removes the whole attribute; null/undefined/'' in a child do not paint anything either.

## map vs repeat: DOM identity
Type something different in each input and press "Reverse". With `map` the text stays in its position (the DOM is reused in place); with `repeat` and a key the input travels with its element.
```html
<demo-list></demo-list>
```
```js
import {LitElement, html} from 'lit';
import {repeat} from 'lit/directives/repeat.js';

class DemoList extends LitElement {
  static properties = { items: {type: Array}, mode: {} };
  constructor() { super(); this.items = ['A', 'B', 'C']; this.mode = 'map'; }

  render() {
    const row = (x) => html`<li>${x}: <input placeholder="type here"></li>`;
    return html`
      <p>Mode:
        <select .value=${this.mode} @change=${(e) => (this.mode = e.target.value)}>
          <option>map</option><option>repeat</option>
        </select>
        <button @click=${() => (this.items = [...this.items].reverse())}>Reverse list</button></p>
      <ul>${this.mode === 'map' ? this.items.map(row) : repeat(this.items, (x) => x, row)}</ul>`;
  }
}
customElements.define('demo-list', DemoList);
```
Reto: try `map`: after reversing, the text you typed in "A" stays in the top row, which is now "C".
Clave: map = fast, no diff or movement. repeat with a key = keeps and moves the DOM (focus, inputs, animations) when reordering.
