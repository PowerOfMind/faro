---
title: Eventos
desc: Eventos en Lit para comunicar componentes, con ejemplos de escucha y despacho, propagación por Shadow DOM y limpieza de listeners.
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

=== esquema
# Escuchar
- @evento — registra un listener con this enlazado al componente.
- Listeners globales — se añaden en connectedCallback y se quitan en disconnectedCallback.
- Delegación — usa un listener en el ancestro y mirar e.target.
# Despachar
- detail — lleva la carga útil del evento.
- bubbles — hace que el evento suba por el árbol.
- composed — hace que el evento cruce el shadow DOM.
# Shadow DOM
- Retargeting — hace que e.target sea el host fuera del shadow.
- composedPath() — revela el origen real del evento.
- <slot> — proyecta Hijos; el contenido dentro es fallback.
- @query — da acceso a nodos del renderRoot (y variantes para slots).

=== test
? Haz que el evento suba por el árbol y cruce el shadow DOM hasta el documento:
```js
this.dispatchEvent(new CustomEvent('cambio', { detail: 1, ___ }));
```
* bubbles: true, composed: true
- bubbles: true
- composed: true
- cancelable: true
! Hacen falta las dos: bubbles para subir y composed para atravesar el límite del shadow root.

? Añade un listener declarativo de clic en la plantilla:
```js
html`<button ___=${this._onClick}>Ok</button>`
```
* @click
- onclick
- .click
- ?click
! En Lit los eventos se enlazan con @nombre; Lit los añade con el this correcto.

? Crea un hueco nombrado para proyectar el avatar:
```js
<slot ___="avatar"></slot>
```
* name
- slot
- id
- part
! El atributo name del <slot> es el que casa con slot="avatar" del hijo.

? Quita el listener global sin dejar fugas y llama al padre:
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
! Siempre hay que llamar a super.disconnectedCallback() para no romper el ciclo de vida de Lit.

? Renderiza en light DOM (sin shadow root):
```js
createRenderRoot() {
  return ___;
}
```
* this
- this.shadowRoot
- document
- this.attachShadow({ mode: 'open' })
! Devolver this renderiza dentro del propio elemento: pierdes slots y estilos con ámbito.

=== prueba

## bubbles y composed, visto en vivo
Un botón dentro de un shadow DOM despacha un evento. Marca/desmarca las casillas y pulsa: ¿quién lo oye? Fíjate también en `target` (retargeting) frente al origen real.
```html
<label><input type="checkbox" id="bub" checked> bubbles</label>
<label><input type="checkbox" id="comp"> composed</label>
<div id="externo" style="padding:10px;border:2px dashed var(--line);margin-top:8px">
  <b>div externo (light DOM)</b><br>
  <emisor-el></emisor-el>
</div>
```
```js
import {LitElement, html} from 'lit';
const $ = (id) => document.getElementById(id);

class EmisorEl extends LitElement {
  render() { return html`<button @click=${this.emitir}>Despachar evento desde el botón interno</button>`; }
  emitir(e) {
    const ev = new CustomEvent('ping', {bubbles: $('bub').checked, composed: $('comp').checked});
    console.log('— despachado: bubbles=' + ev.bubbles + ', composed=' + ev.composed);
    e.target.dispatchEvent(ev);              // se despacha desde DENTRO del shadow DOM
  }
}
customElements.define('emisor-el', EmisorEl);

const quien = (e) => `target visto = <${e.target.localName}>, origen real = <${e.composedPath()[0].localName}>`;
document.querySelector('emisor-el').addEventListener('ping', (e) => console.log('   host escucha:', quien(e)));
$('externo').addEventListener('ping', (e) => console.log('   div externo escucha:', quien(e)));
document.addEventListener('ping', (e) => console.log('   document escucha:', quien(e)));
```
Reto: prueba las cuatro combinaciones: solo bubbles → nadie fuera lo oye; solo composed → únicamente el host; ambas → llega hasta document.
Clave: bubbles = sube por el árbol; composed = cruza el shadow DOM. Fuera, e.target es el host (retargeting); composedPath()[0] da el origen.

## Slots: por defecto, con nombre, fallback y slotchange
Añade y quita contenido proyectado y mira cómo aparece el fallback y se dispara `slotchange`.
```html
<mi-panel id="p"><p>Cuerpo del panel</p></mi-panel>
<p><button id="ab">Añadir cabecera</button> <button id="qu">Quitar cabecera</button> <button id="ac">Añadir párrafo</button></p>
```
```js
import {LitElement, html, css} from 'lit';

class MiPanel extends LitElement {
  static styles = css`.cab { font-weight: 700; border-bottom: 1px solid var(--line); margin-bottom: 6px } i { color: var(--muted) }`;
  render() {
    return html`
      <div class="cab"><slot name="cabecera" @slotchange=${this.cambio}><i>(cabecera por defecto: contenido fallback)</i></slot></div>
      <slot @slotchange=${this.cambio}></slot>`;
  }
  cambio(e) {
    const s = e.target;
    console.log(`slotchange en «${s.name || 'por defecto'}» → ${s.assignedNodes({flatten: true}).length} nodos asignados`);
  }
}
customElements.define('mi-panel', MiPanel);

const p = document.getElementById('p');
document.getElementById('ab').onclick = () => {
  if (p.querySelector('[slot=cabecera]')) return;
  const s = document.createElement('span'); s.slot = 'cabecera'; s.textContent = 'Cabecera proyectada'; p.append(s);
};
document.getElementById('qu').onclick = () => p.querySelector('[slot=cabecera]')?.remove();
document.getElementById('ac').onclick = () => { const x = document.createElement('p'); x.textContent = 'Otro párrafo'; p.append(x); };
```
Reto: mira que los hijos proyectados NO se mueven al shadow DOM: sigue siendo `p.children` en el light DOM.
Clave: El contenido dentro de <slot> es fallback; slotchange avisa de cambios; @queryAssignedElements obtiene los nodos asignados.
