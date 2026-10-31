---
title: Events
desc: Lit events connect components to their surroundings. Learn to listen and dispatch, control bubbling across Shadow DOM and handle retargeting.
pkgs: lit
---
## Listen
```ts
html`<button @click=${this._onClick}>OK</button>`
@eventOptions({passive: true}) _onScroll(e) {}
```
Global listeners: add in `connectedCallback`, remove in `disconnectedCallback`. Use arrow functions as fields to keep `this`.

## Dispatch
```ts
this.dispatchEvent(new CustomEvent('item-selected', {
  detail: {id}, bubbles: true, composed: true,
}));
```
- `bubbles`: goes up the tree.
- `composed`: crosses the shadow DOM boundary.
- For an ancestor to hear it you normally need **both**.

## Retargeting
From outside, `e.target` is the host. The real origin: `e.composedPath()[0]`.

## Good rules
- **Props down, events up.**
- Do not dispatch an event because the owner changed a property (just as `input.value = x` does not fire `change`). Do it when the user acts or something async finishes.
- If the event describes rendered state: `await this.updateComplete` before dispatching.
- Delegation: one listener on the ancestor reading `e.target`, only for events that bubble.

> [!WARN] "My event does not arrive"
> 90 % of the time `composed: true` is missing, or the listener was registered on a different node than the emitter.

=== esquema
# Listen
- @event — registers a listener with this bound to the component.
- Global listeners — added in connectedCallback and removed in disconnectedCallback.
- Delegation — one listener on the ancestor, reading e.target.
# Dispatch
- detail — carries the event payload.
- bubbles — makes the event go up the tree.
- composed — makes the event cross the shadow DOM.
# Shadow DOM
- Retargeting — e.target is the host outside the shadow.
- composedPath() — the real origin of the event.
- <slot> — children; content inside is the fallback.
- @query — nodes of the renderRoot (and variants for slots).
=== test
? Make the event go up the tree and cross the shadow DOM up to the document:
```js
this.dispatchEvent(new CustomEvent('change', { detail: 1, ___ }));
```
* bubbles: true, composed: true
- bubbles: true
- composed: true
- cancelable: true
! You need both: bubbles to go up and composed to cross the shadow root boundary.
? Add a declarative click listener in the template:
```js
html`<button ___=${this._onClick}>Ok</button>`
```
* @click
- onclick
- .click
- ?click
! In Lit events are bound with @name; Lit adds them with the correct this.
? Create a named hole to project the avatar:
```js
<slot ___="avatar"></slot>
```
* name
- slot
- id
- part
! The name attribute of the <slot> is what matches the child's slot="avatar".
? Remove the global listener without leaks and call the parent:
```js
disconnectedCallback() {
  window.removeEventListener('resize', this._h);
  ___;
}
```
* super.disconnectedCallback()
- super.connectedCallback()
- this.remove()
- this.requestUpdate()
! You must always call super.disconnectedCallback() so you do not break Lit's lifecycle.
? Render in light DOM (no shadow root):
```js
createRenderRoot() {
  return ___;
}
```
* this
- this.shadowRoot
- document
- this.attachShadow({ mode: 'open' })
! Returning this renders inside the element itself: you lose slots and scoped styles.
=== prueba
## bubbles and composed, seen live
A button inside a shadow DOM dispatches an event. Tick/untick the boxes and press: who hears it? Also notice `target` (retargeting) versus the real origin.
```html
<label><input type="checkbox" id="bub" checked> bubbles</label>
<label><input type="checkbox" id="comp"> composed</label>
<div id="outer" style="padding:10px;border:2px dashed var(--line);margin-top:8px">
  <b>outer div (light DOM)</b><br>
  <emitter-el></emitter-el>
</div>
```
```js
import {LitElement, html} from 'lit';
const $ = (id) => document.getElementById(id);

class EmitterEl extends LitElement {
  render() { return html`<button @click=${this.emit}>Dispatch event from the inner button</button>`; }
  emit(e) {
    const ev = new CustomEvent('ping', {bubbles: $('bub').checked, composed: $('comp').checked});
    console.log('— dispatched: bubbles=' + ev.bubbles + ', composed=' + ev.composed);
    e.target.dispatchEvent(ev);              // dispatched from INSIDE the shadow DOM
  }
}
customElements.define('emitter-el', EmitterEl);

const who = (e) => `seen target = <${e.target.localName}>, real origin = <${e.composedPath()[0].localName}>`;
document.querySelector('emitter-el').addEventListener('ping', (e) => console.log('   host hears:', who(e)));
$('outer').addEventListener('ping', (e) => console.log('   outer div hears:', who(e)));
document.addEventListener('ping', (e) => console.log('   document hears:', who(e)));
```
Reto: try the four combinations: bubbles only → nobody outside hears it; composed only → only the host; both → it reaches document.
Clave: bubbles = goes up the tree; composed = crosses the shadow DOM. Outside, e.target is the host (retargeting); composedPath()[0] gives the origin.

## Slots: default, named, fallback and slotchange
Add and remove projected content and watch the fallback appear and `slotchange` fire.
```html
<my-panel id="p"><p>Panel body</p></my-panel>
<p><button id="ab">Add header</button> <button id="qu">Remove header</button> <button id="ac">Add paragraph</button></p>
```
```js
import {LitElement, html, css} from 'lit';

class MyPanel extends LitElement {
  static styles = css`.head { font-weight: 700; border-bottom: 1px solid var(--line); margin-bottom: 6px } i { color: var(--muted) }`;
  render() {
    return html`
      <div class="head"><slot name="header" @slotchange=${this.changed}><i>(default header: fallback content)</i></slot></div>
      <slot @slotchange=${this.changed}></slot>`;
  }
  changed(e) {
    const s = e.target;
    console.log(`slotchange on «${s.name || 'default'}» → ${s.assignedNodes({flatten: true}).length} assigned nodes`);
  }
}
customElements.define('my-panel', MyPanel);

const p = document.getElementById('p');
document.getElementById('ab').onclick = () => {
  if (p.querySelector('[slot=header]')) return;
  const s = document.createElement('span'); s.slot = 'header'; s.textContent = 'Projected header'; p.append(s);
};
document.getElementById('qu').onclick = () => p.querySelector('[slot=header]')?.remove();
document.getElementById('ac').onclick = () => { const x = document.createElement('p'); x.textContent = 'Another paragraph'; p.append(x); };
```
Reto: notice that projected children do NOT move into the shadow DOM: they are still `p.children` in the light DOM.
Clave: Content inside <slot> is the fallback; slotchange signals changes; @queryAssignedElements gets the assigned nodes.
