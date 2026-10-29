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

=== esquema
# Callbacks de elemento
- constructor — pide la primera actualización y fija valores por defecto; prepara la mochila antes de salir.
- connectedCallback — crea el renderRoot y arranca el primer update; aquí van listeners externos.
- disconnectedCallback — limpia listeners y timers; el update se pausa hasta reconectar.
# Ciclo de actualización
- shouldUpdate — decide si hace falta actualizar la pantalla, como comprobar si cambió algo antes de imprimir una hoja.
- willUpdate — calcula valores derivados antes de renderizar, como sumar el subtotal antes de mostrar la factura.
- update y render — producen el DOM: update refleja atributos y llama a render.
- firstUpdated y updated — corren después del DOM; firstUpdated solo una vez.
# Cuidados
- Cambiar props en updated — programa otro ciclo: usa changed.has para evitar bucles.
- Cambiar props en willUpdate — no programa otro ciclo, por eso es ideal para derivados.
- updateComplete — permite esperar al render antes de leer el DOM o disparar eventos.

=== test
? Inicializa el ciclo de vida de Lit al conectar el elemento al DOM:
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
! Siempre se debe llamar a super.connectedCallback() para que Lit cree el renderRoot e inicie el ciclo de actualización.

? Cancela la actualización si falta el identificador requerido:
```js
___(cambios) {
  return Boolean(this.id);
}
```
* shouldUpdate
- willUpdate
- beforeUpdate
- canRender
! shouldUpdate(cambios) controla si continúa el render; si devuelve false, el ciclo se detiene.

? Calcula valores derivados justo antes del render sin provocar un ciclo adicional:
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
! willUpdate(cambios) se ejecuta antes de render(); modificar propiedades aquí no programa un segundo ciclo.

? Accede al DOM creado inmediatamente tras la primera renderización:
```js
___() {
  this.renderRoot.querySelector('input').focus();
}
```
* firstUpdated
- connectedCallback
- updated
- renderComplete
! firstUpdated() se ejecuta una única vez después de que el elemento ha renderizado su DOM por primera vez.

? Consulta el valor previo que tenía la propiedad antes de la actualización actual:
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
! cambios es un Map donde cambios.get('prop') devuelve el valor que tenía la propiedad antes de actualizarse.

=== prueba

## El ciclo de vida, en la consola
Pulsa el botón del componente para cambiar `n`, y quita / vuelve a poner el elemento en el DOM. Lee el orden de los logs.
```html
<div id="host"><mi-ciclo></mi-ciclo></div>
<p><button id="q">Quitar del DOM</button> <button id="p">Volver a poner</button></p>
```
```js
import {LitElement, html} from 'lit';

class MiCiclo extends LitElement {
  static properties = { n: {type: Number} };
  constructor() { super(); console.log('constructor'); this.n = 0; }
  connectedCallback() { super.connectedCallback(); console.log('connectedCallback'); }
  disconnectedCallback() { super.disconnectedCallback(); console.log('disconnectedCallback'); }
  shouldUpdate(c) { console.log('shouldUpdate  cambió:', [...c.keys()].join(', ')); return true; }
  willUpdate()    { console.log('willUpdate'); }
  render()        { console.log('render  (n = ' + this.n + ')'); return html`<button @click=${() => this.n++}>n = ${this.n}</button>`; }
  firstUpdated()  { console.log('firstUpdated  (solo la primera vez)'); }
  updated(c)      { console.log('updated  cambió:', [...c.keys()].join(', ')); }
}
customElements.define('mi-ciclo', MiCiclo);

const el = document.querySelector('mi-ciclo');
document.getElementById('q').onclick = () => el.remove();
document.getElementById('p').onclick = () => document.getElementById('host').append(el);
```
Reto: devuelve `false` en shouldUpdate cuando `this.n > 3` y observa que ya no hay render ni updated.
Clave: Orden: constructor → connectedCallback → shouldUpdate → willUpdate → render → firstUpdated → updated.

## Valores derivados: willUpdate vs updated
`completo` se calcula en willUpdate: escribir en cada input produce un solo updated. Mira la consola.
```html
<mi-nombre></mi-nombre>
```
```js
import {LitElement, html} from 'lit';

class MiNombre extends LitElement {
  static properties = {
    nombre: {}, apellido: {},
    completo: {state: true},
  };
  constructor() { super(); this.nombre = 'Ada'; this.apellido = 'Lovelace'; this.ciclos = 0; }

  willUpdate(cambios) {                       // derivar aquí NO provoca otro ciclo
    if (cambios.has('nombre') || cambios.has('apellido')) {
      this.completo = `${this.nombre} ${this.apellido}`;
    }
  }
  updated() { this.ciclos++; console.log('updated nº', this.ciclos); }

  render() {
    return html`
      <input .value=${this.nombre}   @input=${(e) => (this.nombre = e.target.value)}>
      <input .value=${this.apellido} @input=${(e) => (this.apellido = e.target.value)}>
      <p>Nombre completo: <b>${this.completo}</b></p>`;
  }
}
customElements.define('mi-nombre', MiNombre);
```
Reto: mueve el cálculo de `completo` a `updated()` (con `if` sobre `cambios`): verás dos `updated` por tecla, porque cambiar una propiedad ahí programa otro ciclo.
Clave: Derivados en willUpdate (sin ciclo extra). Cambiar propiedades en updated programa otro ciclo: protégelo con changed.has().
