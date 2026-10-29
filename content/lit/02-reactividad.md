---
title: Propiedades reactivas
desc: "@property, @state, cuándo se re-renderiza y la trampa de los class fields."
pkgs: lit
---
## Pública o interna
- `@property()` / `static properties`: API de entrada del componente.
- `@state()`: estado interno, sin atributo, privado.

Opciones de `@property`: `attribute` (nombre o `false`), `type`, `converter`, `reflect`, `hasChanged` (por defecto `!==`), `noAccessor`, `state`.

## Flujo
setter → `requestUpdate()` → compara con `hasChanged` → si cambió, **actualización asíncrona agrupada (microtask)** → `update()` → `render()`.

## Mutar no dispara render
Misma referencia, mismo valor, ningún render.
```ts
// mal: this.items.push(x)
this.items = [...this.items, x];          // preferido (inmutable)
// o, si mutas:
this.items.push(x); this.requestUpdate();
```

## La trampa de los class fields
Un campo de clase JS sombrea el accessor del prototipo y deja de ser reactivo.

| Entorno | Solución |
|---|---|
| TypeScript con decoradores experimentales | `"useDefineForClassFields": false` |
| Sin esa opción | `declare name: string;` |
| Decoradores estándar (TS 5.2+) | keyword `accessor` |

```ts
@property() accessor name = 'x';   // decoradores estándar
```

## Atributos
- Nombre por defecto = propiedad en minúsculas (`fooBar` → `foobar`).
- Booleanos: empiezan en `false` para poder ponerlos en el markup.
- `reflect: true` solo si lo necesitas en CSS (`:host([active])`). Nunca con objetos o arrays.
- Valores derivados: `willUpdate`, no un setter a mano.

> [!WARN] Síntoma clásico
> "Cambio el dato y la UI no se actualiza": casi siempre es mutación en sitio o un class field que sombrea el accessor.

=== esquema
# Declaración
- @property — declara un dato de entrada visible desde fuera, como el nombre que se escribe en una etiqueta.
- @state — declara un dato interno, como si el menú está abierto; no crea un atributo HTML.
- static properties — equivale a los decoradores sin necesidad de compilador.
# Opciones
- attribute — fija el nombre del atributo o false para no tenerlo.
- type y converter — convierten traducen el texto del HTML a un valor JS, como "3" a 3.
- reflect — escribe copia la propiedad al atributo: actualiza la etiqueta de una caja al cambiar su contenido.
- hasChanged — decide si hay cambio; por defecto compara con !==.
# Actualización
- Setter — llama a requestUpdate().
- Cambios múltiples — dan un solo render por microtask.
- Mutar arrays — exige avisar con una lista nueva o requestUpdate(): cambiar una página del cuaderno sin cambiar el cuaderno no se detecta.
# Trampas
- Class fields — sombrean los accessors del prototipo y quitan reactividad.
- Booleanos — deben empezar en false para poder fijarlos desde el markup.
- Reflejar objetos — se evita solo tiene sentido con tipos simples.

=== test
? Declara _abierto como estado interno que provoca render pero NO crea atributo HTML:
```js
static properties = {
  _abierto: { ___: true }
};
```
* state
- internal
- private
- noAttribute
! state: true define una propiedad reactiva privada que no se sincroniza con ningún atributo HTML.

? Haz que al cambiar la propiedad en JS se actualice el atributo en el DOM (<mi-tag activo>):
```js
static properties = {
  activo: { type: Boolean, ___: true }
};
```
* reflect
- sync
- attribute
- mirror
! reflect: true escribe los cambios de la propiedad de vuelta en el atributo HTML.

? Indica que items es un Array complejo y no debe leerse de un atributo HTML:
```js
static properties = {
  items: { ___: false }
};
```
* attribute
- reflect
- type
- converter
! attribute: false desactiva la lectura desde atributos HTML, ideal para objetos y arrays complejos.

? Añade un elemento a la lista garantizando una nueva referencia para que Lit detecte el cambio:
```js
añadir(nuevo) {
  this.items = ___
}
```
* [...this.items, nuevo];
- this.items.push(nuevo);
- this.items.concat();
- Object.assign(this.items, nuevo);
! Lit usa comprobación !==. Mutar con .push() mantiene la misma referencia en memoria y no dispara el render.

? Configura un hasChanged personalizado que solo active render cuando el valor sea mayor que cero:
```js
static properties = {
  puntos: {
    type: Number,
    ___: (nuevo, viejo) => nuevo > 0 && nuevo !== viejo
  }
};
```
* hasChanged
- shouldChange
- isDifferent
- compare
! hasChanged define la función que determina si un cambio de valor debe desencadenar una actualización.

=== prueba

## Atributo ↔ propiedad, type y reflect
La propiedad `valor` es Number y se refleja (reflect) en el atributo. Compara qué pasa al cambiar la propiedad o el atributo.
```html
<mi-barra valor="30"></mi-barra>
<p><button id="a">propiedad: valor += 10</button> <button id="b">setAttribute('valor', 80)</button></p>
<pre id="h"></pre>
```
```js
import {LitElement, html, css} from 'lit';

class MiBarra extends LitElement {
  static properties = { valor: {type: Number, reflect: true} };
  static styles = css`
    .pista { background: var(--surface-2); border-radius: 8px; height: 18px; overflow: hidden }
    .relleno { background: var(--primary); height: 100%; transition: width .3s }`;
  render() {
    return html`<div class="pista"><div class="relleno" style="width:${this.valor}%"></div></div>
      <small>valor (propiedad): ${this.valor} · typeof ${typeof this.valor}</small>`;
  }
}
customElements.define('mi-barra', MiBarra);

const $ = (id) => document.getElementById(id);
const el = document.querySelector('mi-barra');
const ver = () => el.updateComplete.then(() => { $('h').textContent = el.outerHTML; });
$('a').onclick = () => { el.valor += 10; ver(); };
$('b').onclick = () => { el.setAttribute('valor', 80); ver(); };
ver();
```
Reto: quita `reflect: true` y comprueba que al cambiar la propiedad el atributo del HTML ya no se actualiza.
Clave: El atributo es string; `type: Number` lo convierte a propiedad. `reflect` copia propiedad → atributo (úsalo poco).

## Mutar un array no re-renderiza
Tres botones: mutar con push, crear una nueva referencia (la forma buena) y push + requestUpdate().
```html
<mi-lista></mi-lista>
```
```js
import {LitElement, html} from 'lit';

class MiLista extends LitElement {
  static properties = { items: {type: Array} };
  constructor() { super(); this.items = ['uno']; this.renders = 0; }

  render() {
    this.renders++;
    return html`
      <p>render nº ${this.renders} · ${this.items.length} elementos</p>
      <ul>${this.items.map((i) => html`<li>${i}</li>`)}</ul>
      <button @click=${this.mal}>push (mal)</button>
      <button @click=${this.bien}>nueva referencia (bien)</button>
      <button @click=${this.regular}>push + requestUpdate()</button>`;
  }
  mal()     { this.items.push('mal ' + this.items.length); console.log('push sin reasignar → no hay render'); }
  bien()    { this.items = [...this.items, 'bien ' + this.items.length]; }
  regular() { this.items.push('rU ' + this.items.length); this.requestUpdate(); }
}
customElements.define('mi-lista', MiLista);
```
Reto: pulsa «mal» tres veces: no pasa nada. Luego pulsa «bien»: aparecen todos de golpe (el render lee el array actual).
Clave: Lit compara por referencia (!==). Mutar no cambia la referencia: reasigna (inmutable) o llama a requestUpdate().
