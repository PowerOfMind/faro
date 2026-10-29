---
title: Styles, Shadow DOM and slots
desc: Encapsulation, theming from outside with variables and ::part, and slots.
pkgs: lit
---
## Styles
```ts
static styles = css`
  :host { display: block; }
  :host([active]) { outline: 2px solid var(--accent, royalblue); }
  ::slotted(p) { margin: 0; }
`;
```
- Evaluated **once per class** and use `adoptedStyleSheets`.
- Inside `css` only `css` values or numbers go. Strings with `unsafeCSS`.
- Inheritance: `static styles = [Super.styles, css`...`]`.

## Theming from outside (most to least recommended)
1. **CSS inheritance**: `color`, `font-*` and variables cross the shadow.
2. **Custom properties** with a fallback: `var(--my-color, yellow)`.
3. **`::part()`**: mark `part="button"` inside and style `my-el::part(button)` outside.

## Slots
```html
<slot></slot>
<slot name="footer">Default content</slot>
```
- Content inside the `<slot>` is the *fallback*.
- `slotchange` event; `slot.assignedElements({flatten: true})`.
- `::slotted()` only reaches direct children.

## Reaching the internal DOM
`@query('#x')`, `@queryAll`, `@queryAsync`, `@queryAssignedElements`. Avoid `document.querySelector`: it does not enter the shadow.

## Without Shadow DOM
```ts
createRenderRoot() { return this; }
```
You lose style and slot encapsulation. Useful to integrate with global CSS (Tailwind).

> [!TIP] Focus in forms
> `static shadowRootOptions = {...LitElement.shadowRootOptions, delegatesFocus: true}` makes the host's focus go to the first internal control.

> [!AI] Tailwind + Shadow DOM
> Global styles do not enter the shadow. The AI often forgets it: either use light DOM or inject the compiled sheet into `static styles`.

=== esquema
# Scope
- static styles — the css tag; it can be an array.
- Evaluation — once per class, not per instance.
- Inheritance — an array that includes the superclass styles.
# Selectors
- :host — the host element; default styles that can be overridden.
- ::slotted() — only direct children of the slot, not descendants.
- <style> in render — per instance and less efficient with expressions.
# Theming
- CSS inheritance — crosses the shadow DOM: colour, fonts and custom properties.
- Custom properties — var(--name, default value).
- classMap and styleMap — classes and styles from objects.
=== test
? Create encapsulated styles using Lit's tagged template literal:
```js
import { LitElement, ___ } from 'lit';
class MyButton extends LitElement {
  static styles = ___`:host { display: inline-block }`;
}
```
* css
- styles
- style
- html
! css creates a CSSResult that Lit optimises by sharing constructable stylesheets between instances.
? Style the host element itself when it is active:
```js
static styles = css`
  ___([active]) {
    border: 2px solid gold;
  }
`;
```
* :host
- host
- :self
- ::host
! :host([active]) selects the container element of the Shadow DOM when it has the active attribute.
? Style the span elements projected through the slot:
```js
static styles = css`
  ___(span) {
    font-weight: 700;
  }
`;
```
* ::slotted
- :slotted
- ::slot
- :slot
! ::slotted(selector) styles the light DOM direct children projected into a <slot>.
? Expose the internal button so outside CSS can customise it with ::part:
```js
render() {
  return html`<button ___="label">Press</button>`;
}
```
* part
- slot
- exportparts
- name
! part="label" lets you style the element from outside with the selector my-button::part(label).
? Read a custom property with a default fallback value for theming:
```js
button {
  background: ___
}
```
* var(--button-color, #6d4aff);
- env(--button-color);
- $button-color || #6d4aff;
- attr(button-color);
! CSS custom properties with var(--name, fallback) cross the Shadow DOM boundary, enabling theming.
=== prueba
## Theming from outside: custom properties and ::part
The first card uses the default values; the other two are themed with CSS variables. `::part(title)` styles an internal piece.
```html
<style>
  .yellow { --card-bg: #fde68a; --card-text: #422006 }
  .dark   { --card-bg: #1e293b; --card-text: #e2e8f0 }
  theme-card::part(title) { text-transform: uppercase; letter-spacing: .08em }
</style>
<theme-card>Default (fallback)</theme-card>
<theme-card class="yellow">With variables</theme-card>
<theme-card class="dark">Another variant</theme-card>
```
```js
import {LitElement, html, css} from 'lit';

class ThemeCard extends LitElement {
  static styles = css`
    :host { display: block; margin: 8px 0; padding: 12px; border-radius: 12px;
            background: var(--card-bg, var(--surface-2));
            color: var(--card-text, var(--text)); }
    h4 { margin: 0 0 4px }`;
  render() { return html`<h4 part="title">Title (part)</h4><slot></slot>`; }
}
customElements.define('theme-card', ThemeCard);
```
Reto: add `--card-bg: tomato` in a `theme-card { ... }` rule in the HTML.
Clave: You theme with CSS inheritance, custom properties var(--x, fallback) and ::part(). It is the component's public style API.

## :host, ::slotted, classMap and styleMap
`:host([highlighted])` reacts to a reflected attribute; `::slotted(em)` only reaches direct children of the slot (the bold stays unstyled).
```html
<my-notice>Text with <em>projected emphasis</em> and <strong>bold (not styled)</strong></my-notice>
```
```js
import {LitElement, html, css} from 'lit';
import {classMap} from 'lit/directives/class-map.js';
import {styleMap} from 'lit/directives/style-map.js';

class MyNotice extends LitElement {
  static properties = { highlighted: {type: Boolean, reflect: true}, size: {type: Number} };
  static styles = css`
    :host { display: block; padding: 10px; border: 2px solid var(--line); border-radius: 10px }
    :host([highlighted]) { border-color: var(--primary); background: var(--primary-soft) }
    ::slotted(em) { color: var(--bad) }
    .big { font-weight: 800 }`;
  constructor() { super(); this.highlighted = false; this.size = 16; }

  render() {
    return html`
      <div class=${classMap({big: this.highlighted})} style=${styleMap({fontSize: this.size + 'px'})}><slot></slot></div>
      <button @click=${() => (this.highlighted = !this.highlighted)}>highlighted</button>
      <button @click=${() => (this.size += 2)}>A+</button>`;
  }
}
customElements.define('my-notice', MyNotice);
```
Reto: change `::slotted(em)` to `::slotted(*)` and you will see it now reaches all direct children, not nested ones.
Clave: static styles is evaluated once per class. :host styles the host; ::slotted only the slot's direct children.
