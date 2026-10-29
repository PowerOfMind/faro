---
title: SSR, testing and framework integration
desc: Testing Lit, server rendering, using it in React and migrating from Lit 1/2.
pkgs: lit, "@lit/react", "@lit-labs/ssr", "@web/test-runner"
---
## Testing
In a real browser: Web Test Runner (+ `@open-wc/testing`, `fixture`) or Playwright. Always `await el.updateComplete` before assertions.
```ts
const el = await fixture<MyEl>(html`<my-el name="Ana"></my-el>`);
expect(el.shadowRoot!.textContent).to.contain('Ana');
```

## SSR (`@lit-labs/ssr`, experimental)
It generates HTML with **Declarative Shadow DOM** and hydrates on the client (`@lit-labs/ssr-client`). Only `willUpdate` and `render` run. Integrations: Eleventy, Astro, Next (pages), Nuxt.

## In React
```tsx
import {createComponent} from '@lit/react';
export const MyEl = createComponent({tagName: 'my-el', elementClass: MyElement, react: React, events: {onSelect: 'item-selected'}});
```
React 19 already passes properties and events to custom elements; in React < 19 everything arrived as string attributes, which is why the wrapper exists.

## In Angular
Add `CUSTOM_ELEMENTS_SCHEMA` and bind properties with `[prop]` and events with `(event)`.

## Other
- **Localisation**: `@lit/localize`.
- **Publishing**: ES modules; `lit` as a dependency, not bundled inside.
- `lit-analyzer` / IDE plugin detects template errors.

## Lit 1/2 → 3
- `lit-element` + `lit-html` → a single `lit` package. `UpdatingElement` → `ReactiveElement`.
- Decorators in `lit/decorators.js`; Lit 3 supports the standard ones (`accessor`).
- Lit 3: ES2021, no IE11. Libraries can declare `"^2.7.0 || ^3.0.0"`.

=== esquema
# Testing
- Environment — must be a browser, without simulating the DOM.
- Tools — Web Test Runner and WebdriverIO.
- updateComplete — wait for the render to finish before asserting.
# SSR
- @lit-labs/ssr — renders components to HTML in Node.
- Declarative Shadow DOM — describes the shadow root inside the HTML.
- Hydration — reactivates the components on the client.
# React
- createComponent — creates a React wrapper for a Lit element.
- events — maps custom events to props.
- useController — turns a controller into a hook.
# Lit 3 changes
- Compatibility — drops IE11 and deprecated Lit 2.x APIs.
- UpdatingElement — replaced by ReactiveElement.
- Decorators — imported from lit/decorators.js.
# Standard decorators
- accessor — the keyword added to decorated fields.
- TypeScript — needs version 5.2 or higher.
- Interoperability — lets you mix Lit 2.x and 3.0.
# Interview
- Choosing Lit — justified by standards, size and interoperability.
- Cons — a smaller ecosystem than React and experimental SSR.
- Your example — should include decision, trade-off and result.
=== test
? Mount the component in a test (open-wc):
```js
const el = await ___(html`<mi-boton></mi-boton>`);
```
* fixture
- render
- mount
- create
! fixture renders the template in the browser and waits for the first update.
? Wait for the component to finish updating:
```js
el.shadowRoot.querySelector('button').click();
await el.___;
expect(el.shadowRoot.textContent).to.equal('1');
```
* updateComplete
- ready
- renderComplete
- whenDefined
! updateComplete is the promise that resolves when the update finishes.
? Use the web component inside React:
```js
const MiBoton = ___({ react: React, tagName: 'mi-boton', elementClass: MiBotonEl });
```
* createComponent
- wrap
- createElement
- defineComponent
! createComponent, from @lit/react, generates the React wrapper.
? Import the Lit 3 base:
```js
import { LitElement, html } from '___';
```
* lit
- lit-element
- lit-html
- @lit/core
! In Lit 2 and 3 everything is imported from the lit package.
? Declare a reactive property with standard decorators:
```js
@property({ type: Number })
___ count = 0;
```
* accessor
- static
- let
- reactive
! Standard decorators need the accessor word on the field.
? Declare internal state with the decorator:
```js
@___() accessor _abierto = false;
```
* state
- internal
- observe
- private
! @state marks private reactive state, with no attribute.
=== prueba
## The interview exercise: a complete component
It brings together the important things: a reactive property with reflect, a derived value in willUpdate, a named slot with fallback, a composed event, a custom property and :host. Try to write it from memory.
Reto: delete the code in the editor and rewrite it from memory; run it and compare.
Clave: If you explain it while you write it (reactivity, lifecycle, shadow DOM, events), you cover 80 % of the interview.
