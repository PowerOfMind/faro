---
title: Web Components and what Lit adds
desc: The 4 browser standards and the thin layer Lit puts on top.
pkgs: lit
---
## The 4 standards
- **Custom Elements**: `customElements.define('my-tag', Class)`. The name **must contain a hyphen**.
- **Shadow DOM**: encapsulated DOM and CSS.
- **`<template>` and `<slot>`**: inert templates and content projection.
- **ES Modules**: how they are distributed.

Native callbacks: `constructor`, `connectedCallback`, `disconnectedCallback`, `attributeChangedCallback` (only for `observedAttributes`), `adoptedCallback`.

> [!NOTE] Attribute vs property
> An attribute is always a string and lives in the HTML. A property is JS and can be any type. Lit keeps both in sync.

## What Lit is
A ~5 KB (min+gzip) library from Google. `lit` brings everything; `lit-html` is the template engine; `LitElement` is the base class (it extends `ReactiveElement`).

- **No virtual DOM**: it parses the template once and on each render only updates the `${}` holes.
- Components are **native**: they work in React, Angular, Vue or with no framework.
- No build required; decorators are optional.

## Minimal component
```ts
import {LitElement, html, css} from 'lit';
import {customElement, property} from 'lit/decorators.js';

@customElement('simple-greeting')
export class SimpleGreeting extends LitElement {
  static styles = css`p { color: blue; }`;
  @property() name = 'Somebody';
  render() { return html`<p>Hello, ${this.name}!</p>`; }
}
```

Without decorators (plain JS):
```js
class SimpleGreeting extends LitElement {
  static properties = { name: {} };
  constructor() { super(); this.name = 'Somebody'; }
  render() { return html`<p>Hello, ${this.name}!</p>`; }
}
customElements.define('simple-greeting', SimpleGreeting);
```

## Versus React
React calls the component again and compares a VDOM. Lit touches only the bindings. A Lit element exposes the standard DOM API (properties, attributes, events), which is why it fits anywhere.

> [!AI] Where the AI tends to fail
> It mixes Lit 1/2 syntax (`lit-element`, `UpdatingElement`) with Lit 3, or generates React-style event names (`onClick`) on a Lit element. Always ask for "Lit 3, `lit` package".

=== esquema
# Standards
- Custom Elements — registered with customElements.define('my-tag', Class). The name must contain a hyphen.
- Shadow DOM — gives DOM and style encapsulation.
- Template and slot — inert templates, and projecting children into holes with <slot>.
# Native lifecycle
- constructor — called when the element is created or upgraded.
- connectedCallback / disconnectedCallback — called when it enters and leaves the DOM.
- attributeChangedCallback — reacts to changes in observedAttributes.
- adoptedCallback — called when the element moves to another document.
# Attributes and properties
- Attribute — always a string; it lives in the HTML.
- Property — a JS value of any type.
- Upgrade — happens when the element definition arrives after it is already in the DOM.
# Pieces
- lit — the package that bundles everything.
- lit-html — the template engine with html``.
- LitElement — the base class for Lit components with reactivity and templates.
# Why Lit
- Native components — they work in any framework or none.
- Design systems — benefit from a component written once that serves several stacks.
=== test
? Complete the native call to register the element with a valid name:
```js
customElements.define('___', MiEtiqueta);
```
* mi-etiqueta
- mietiqueta
- MiEtiqueta
- mi_etiqueta
! Custom element names must contain a hyphen so they never collide with native tags.
? Declare the static getter to observe changes in the 'texto' attribute:
```js
class MiEtiqueta extends HTMLElement {
  static get ___() { return ['texto']; }
}
```
* observedAttributes
- watchedAttributes
- attributes
- observed
! observedAttributes is the only static list the browser consults to fire attributeChangedCallback.
? Attach the Shadow DOM so it is reachable at this.shadowRoot:
```js
constructor() {
  super();
  this.attachShadow({ mode: '___' });
}
```
* open
- closed
- true
- isolated
! mode: 'open' lets outside JavaScript read and manipulate element.shadowRoot.
? Extend Lit's base class to create a component with Shadow DOM:
```js
class MiSaludo extends ___ {
  render() { return html`<p>Hola</p>`; }
}
```
* LitElement
- HTMLElement
- ReactiveElement
- Component
! LitElement combines ReactiveElement and lit-html, giving reactivity and efficient rendering.
? Declare the reactive property in standard JavaScript without decorators:
```js
class MiSaludo extends LitElement {
  static ___ = {
    nombre: { type: String }
  };
}
```
* properties
- props
- state
- observedAttributes
! In standard JavaScript without decorators, reactive properties are declared in the static properties field.
? Produce the TemplateResult in render with Lit's tagged template:
```js
render() {
  return ___`<p>Hola, <b>${this.nombre}</b></p>`;
}
```
* html
- css
- template
- vdom
! html marks a Lit template; its dynamic holes are explained in the templates topic.
=== prueba
## A native custom element (without Lit)
Notice the order of the logs: the element was already in the HTML and gets "upgraded" when the class is registered.
Reto: remove `static observedAttributes` and check that attributeChangedCallback is no longer called.
Clave: The name has a hyphen; attributeChangedCallback only fires for observedAttributes; an element already present is upgraded when it is registered.
## Shadow DOM and slots: encapsulation
Global CSS paints the outside paragraph red; the one inside the shadow DOM is not affected.
Reto: delete the span with slot="titulo" from the HTML and watch the fallback content "Sin título" appear.
Clave: Shadow DOM encapsulates DOM and styles; <slot>s project the children without moving them.
## Your first Lit component
Reactive property + template + event. No build: standard JavaScript.
Reto: add `?disabled=${this.cuenta >= 5}` to the button to block it at 5.
Clave: Change a reactive property → Lit schedules an async render → only the affected ${} hole is updated.
