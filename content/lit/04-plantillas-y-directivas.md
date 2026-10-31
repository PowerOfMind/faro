---
title: Plantillas y directivas
desc: Plantillas y directivas de Lit para construir interfaces, con ejemplos de atributos, propiedades, eventos, condicionales y listas.
pkgs: lit
---
## Regla de oro del binding
| Sintaxis | Qué hace |
|---|---|
| `attr=${x}` | atributo (string) |
| `?attr=${bool}` | añade o quita el atributo |
| `.prop=${obj}` | propiedad JS, sin serializar |
| `@evt=${fn}` | listener (`this` ya es el componente) |

```ts
html`<my-list .items=${this.items} ?disabled=${this.busy} @select=${this._onSelect}></my-list>`
```

- `nothing`: no renderiza o quita el atributo. `ifDefined(x)` = `x ?? nothing`.
- Condicionales: ternario, `&&` o `when(cond, () => a, () => b)`.
- No se puede enlazar el nombre de una etiqueta o atributo (usa `static-html` con `literal`), ni dentro de `<textarea>` (usa `.value`).

## Listas: map o repeat
```ts
html`<ul>${this.items.map(i => html`<li>${i.name}</li>`)}</ul>`
html`<ul>${repeat(this.items, i => i.id, i => html`<li>${i.name}</li>`)}</ul>`
```
`map` actualiza en sitio (más ligero). `repeat` con clave conserva la identidad del DOM al reordenar (inputs con foco, animaciones).

## Directivas útiles
| Necesidad | Directiva |
|---|---|
| Clases / estilos dinámicos | `classMap`, `styleMap` |
| Valor real del input | `live` |
| Recrear al cambiar una clave | `keyed` |
| Conservar DOM al alternar vistas | `cache` |
| Recalcular solo con dependencias | `guard` |
| Referencia a un elemento | `ref` |
| Promesas / streams | `until`, `asyncAppend` |

```ts
html`<input .value=${live(this.q)} @input=${e => this.q = e.target.value}>`
html`<div class=${classMap({active: this.on, big: this.size > 1})}></div>`
```

> [!SEC] XSS
> Lit escapa por defecto. `unsafeHTML` y `unsafeStatic` solo con contenido que controlas.

=== esquema
# Bindings
- attr=${x} — pone texto en la etiqueta, como escribir el título en una pegatina.
- ?attr=${x} — añade o quita una opción sí/no, como marcar o desmarcar una casilla.
- .prop=${x} — asigna el valor JS original, como entregar una lista entera en vez de copiarla en una nota.
- @evento=${fn} — registra una acción para cuando ocurra algo, como un timbre que suena al pulsarlo.
# Hijos
- Primitivos — se muestran como Texto; null, undefined y '' no renderizan nada.
- TemplateResult — se anidan con plantillas dentro de plantillas.
- Arrays e iterables — se renderizan elemento a elemento, en orden.
# Centinelas y límites
- nothing — elimina el contenido o el atributo completo.
- static-html — permite expresiones en nombres de etiqueta con literal.
- Dentro de textarea — se usa .value en vez de una expresión hija.
# Estilo
- classMap — aplica clases según un objeto clase→booleano.
- styleMap — aplica propiedades de estilo inline desde un objeto.
# Listas y condicionales
- when — elige entre dos plantillas según un booleano.
- map — recorre un iterable sin diff; más pequeña y rápida.
- repeat — mantiene la identidad del DOM mediante una función de clave.
# Cambios
- cache — conserva el DOM de plantillas inactivas para alternar rápido.
- keyed — recrea el DOM cuando cambia su clave.
- guard — evita Re-evaluar si no cambian sus dependencias.
- live — compara con el valor real del DOM, no el último de Lit.

=== test
? Enlaza el valor del input como propiedad de JavaScript en lugar de como atributo HTML:
```js
html`<input type="text" ___=${this.texto}>`;
```
* .value
- value
- ?value
- @value
! El prefijo . indica un binding a propiedad del objeto DOM (.value=${this.texto}).

? Añade o elimina el atributo booleano disabled según el estado:
```js
html`<button ___=${this.cargando}>Enviar</button>`;
```
* ?disabled
- .disabled
- disabled
- @disabled
! El prefijo ? añade el atributo si es truthy y lo elimina por completo si es falsy.

? Registra un escuchador de eventos nativo con la sintaxis de lit-html:
```js
html`<button ___=${this._onClick}>Guardar</button>`;
```
* @click
- onclick
- .click
- ?click
! El prefijo @ registra un listener nativo con addEventListener manteniendo el contexto this.

? Renderiza la lista reordenando el DOM por clave:
```js
${___(this.items, (i) => i.id, (i) => html`<li>${i.n}</li>`)}
```
* repeat
- map
- when
- join
! repeat recibe la clave y mueve nodos del DOM en vez de recrearlos.

? Evita que Lit pise lo que el usuario escribe en el input:
```js
html`<input .value=${___(this.texto)}>`
```
* live
- cache
- keyed
- guard
! live compara con el valor real del DOM y no con el último valor que renderizó Lit.

? Pon el atributo solo si hay valor:
```js
html`<a href=${___(this.url)}>Ir</a>`
```
* ifDefined
- live
- ref
- guard
! ifDefined quita el atributo cuando el valor es undefined.

=== prueba

## Los cuatro bindings: atributo, ?booleano, .propiedad, @evento
Uno de cada, más un hijo que recibe un array con `.items` (sin serializar a string).
```html
<demo-bindings></demo-bindings>
```
```js
import {LitElement, html, css} from 'lit';

class ListaHija extends LitElement {
  static properties = { items: {type: Array} };
  render() { return html`<p>La hija recibió un array con <code>.items</code>: ${this.items.join(', ')}</p>`; }
}
customElements.define('lista-hija', ListaHija);

class DemoBindings extends LitElement {
  static properties = { nombre: {}, activo: {type: Boolean} };
  static styles = css`.on { color: var(--ok); font-weight: 700 } .off { color: var(--muted) }`;
  constructor() { super(); this.nombre = 'mundo'; this.activo = false; this.colores = ['rojo', 'verde', 'azul']; }

  render() {
    return html`
      <p>Atributo (string): <span class=${this.activo ? 'on' : 'off'} title="Hola ${this.nombre}">hola ${this.nombre}</span></p>
      <p>Booleano <code>?</code>: <button ?disabled=${!this.activo}>solo si activo</button></p>
      <p>Propiedad <code>.</code>: <input .value=${this.nombre} @input=${(e) => (this.nombre = e.target.value)}></p>
      <p>Evento <code>@</code>: <button @click=${() => (this.activo = !this.activo)}>activo = ${String(this.activo)}</button></p>
      <lista-hija .items=${this.colores}></lista-hija>`;
  }
}
customElements.define('demo-bindings', DemoBindings);
```
Reto: cambia `.items=${this.colores}` por `items=${this.colores}` (sin punto): el array llega como el string «rojo,verde,azul».
Clave: attr = string · ?attr = booleano · .prop = valor JS · @evt = listener (this ya está enlazado al componente).

## Condicionales, listas y `nothing`
Ternario con plantillas anidadas, `.map()` y `nothing` para quitar un atributo por completo.
```html
<demo-cond></demo-cond>
```
```js
import {LitElement, html, nothing} from 'lit';

class DemoCond extends LitElement {
  static properties = { logueado: {type: Boolean}, items: {type: Array}, ayuda: {} };
  constructor() { super(); this.logueado = false; this.items = ['a', 'b', 'c']; this.ayuda = ''; }

  render() {
    return html`
      ${this.logueado ? html`<p>Bienvenido 👋</p>` : html`<p>Inicia sesión</p>`}
      <button @click=${() => (this.logueado = !this.logueado)}>alternar sesión</button>

      <ul>${this.items.map((x, i) => html`<li>${i}: ${x}</li>`)}</ul>
      <button @click=${() => (this.items = [...this.items, String.fromCharCode(97 + this.items.length)])}>añadir</button>

      <p><input placeholder="texto de aria-label" @input=${(e) => (this.ayuda = e.target.value)}>
         <button aria-label=${this.ayuda || nothing}>botón</button></p>
      <p>aria-label en el DOM: <code>${this.ayuda ? this.ayuda : '(ninguno: nothing quitó el atributo)'}</code></p>`;
  }
}
customElements.define('demo-cond', DemoCond);
```
Reto: cambia `this.ayuda || nothing` por `this.ayuda`: con texto vacío el atributo existe pero vacío; con `nothing` desaparece.
Clave: `nothing` no renderiza nada o elimina el atributo entero; null/undefined/'' en un hijo tampoco pintan nada.

## map vs repeat: la identidad del DOM
Escribe algo distinto en cada input y pulsa «Invertir». Con `map` el texto se queda en su posición (el DOM se reutiliza en el sitio); con `repeat` y clave el input viaja con su elemento.
```html
<demo-lista></demo-lista>
```
```js
import {LitElement, html} from 'lit';
import {repeat} from 'lit/directives/repeat.js';

class DemoLista extends LitElement {
  static properties = { items: {type: Array}, modo: {} };
  constructor() { super(); this.items = ['A', 'B', 'C']; this.modo = 'map'; }

  render() {
    const fila = (x) => html`<li>${x}: <input placeholder="escribe aquí"></li>`;
    return html`
      <p>Modo:
        <select .value=${this.modo} @change=${(e) => (this.modo = e.target.value)}>
          <option>map</option><option>repeat</option>
        </select>
        <button @click=${() => (this.items = [...this.items].reverse())}>Invertir lista</button></p>
      <ul>${this.modo === 'map' ? this.items.map(fila) : repeat(this.items, (x) => x, fila)}</ul>`;
  }
}
customElements.define('demo-lista', DemoLista);
```
Reto: prueba con `map`: tras invertir, el texto que escribiste en «A» queda en la fila de arriba, que ahora es «C».
Clave: map = rápido, sin diff ni movimiento. repeat con clave = mantiene y mueve el DOM (foco, inputs, animaciones) al reordenar.
