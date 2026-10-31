---
title: Estilos, Shadow DOM y slots
desc: Estilos y slots en Lit para crear componentes personalizables, con Shadow DOM, variables CSS, partes exportadas y proyección de contenido.
pkgs: lit
---
## Estilos
```ts
static styles = css`
  :host { display: block; }
  :host([active]) { outline: 2px solid var(--accent, royalblue); }
  ::slotted(p) { margin: 0; }
`;
```
- Se evalúan **una vez por clase** y usan `adoptedStyleSheets`.
- Dentro de `css` solo van valores `css` o números. Strings con `unsafeCSS`.
- Herencia: `static styles = [Super.styles, css`...`]`.

## Theming desde fuera (de más a menos recomendable)
1. **Herencia CSS**: `color`, `font-*` y variables atraviesan el shadow.
2. **Custom properties** con fallback: `var(--mi-color, yellow)`.
3. **`::part()`**: marca `part="boton"` dentro y estila `mi-el::part(boton)` fuera.

## Slots
```html
<slot></slot>
<slot name="footer">Contenido por defecto</slot>
```
- El contenido dentro del `<slot>` es el *fallback*.
- Evento `slotchange`; `slot.assignedElements({flatten: true})`.
- `::slotted()` solo alcanza hijos directos.

## Acceder al DOM interno
`@query('#x')`, `@queryAll`, `@queryAsync`, `@queryAssignedElements`. Evita `document.querySelector`: no entra en el shadow.

## Sin Shadow DOM
```ts
createRenderRoot() { return this; }
```
Pierdes encapsulación de estilos y slots. Útil para integrar con CSS global (Tailwind).

> [!TIP] Foco en formularios
> `static shadowRootOptions = {...LitElement.shadowRootOptions, delegatesFocus: true}` hace que el foco del host pase al primer control interno.

> [!AI] Tailwind + Shadow DOM
> Los estilos globales no entran en el shadow. La IA suele olvidarlo: o usas light DOM o inyectas la hoja compilada en `static styles`.

=== esquema
# Ámbito
- static styles — se escribe con la etiqueta css; puede ser un array.
- Evaluación — ocurre una vez por clase, no por instancia.
- Herencia — se hace con un array que incluye los estilos de la superclase.
# Selectores
- :host — estila el elemento anfitrión; son estilos por defecto sobreescribibles.
- ::slotted() — alcanza solo hijos directos del slot, no descendientes.
- <style> en render — es por instancia y menos eficiente con expresiones.
# Theming
- Herencia CSS — cruza el shadow DOM: color, fuentes y custom properties.
- Custom properties — se leen con var(--nombre, valor por defecto).
- classMap y styleMap — aplican clases y estilos desde objetos.

=== test
? Crea estilos encapsulados usando el tagged template literal de Lit:
```js
import { LitElement, ___ } from 'lit';
class MiBoton extends LitElement {
  static styles = ___`:host { display: inline-block }`;
}
```
* css
- styles
- style
- html
! css crea un CSSResult que Lit optimiza compartiendo hojas de estilo Constructable Stylesheets entre instancias.

? Aplica estilos al propio elemento host cuando esté activo:
```js
static styles = css`
  ___([activo]) {
    border: 2px solid gold;
  }
`;
```
* :host
- host
- :self
- ::host
! :host([activo]) selecciona el elemento contenedor del Shadow DOM cuando posee el atributo activo.

? Aplica estilos a los elementos span proyectados a través del slot:
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
! ::slotted(selector) estiliza los hijos directos del light DOM proyectados en un <slot>.

? Expón el botón interno para que el CSS exterior pueda personalizarlo con ::part:
```js
render() {
  return html`<button ___="etiqueta">Pulsar</button>`;
}
```
* part
- slot
- exportparts
- name
! part="etiqueta" permite estilizar el elemento desde fuera con el selector mi-boton::part(etiqueta).

? Lee una custom property con valor de respaldo por defecto para theming:
```js
button {
  background: ___
}
```
* var(--boton-color, #6d4aff);
- env(--boton-color);
- $boton-color || #6d4aff;
- attr(boton-color);
! Las CSS Custom Properties con var(--nombre, fallback) cruzan la frontera del Shadow DOM permitiendo theming.

=== prueba

## Theming desde fuera: custom properties y ::part
La primera tarjeta usa los valores por defecto; las otras dos se tematizan con variables CSS. `::part(titulo)` estiliza una pieza interna.
```html
<style>
  .amarilla { --tarjeta-fondo: #fde68a; --tarjeta-texto: #422006 }
  .oscura   { --tarjeta-fondo: #1e293b; --tarjeta-texto: #e2e8f0 }
  tarjeta-tema::part(titulo) { text-transform: uppercase; letter-spacing: .08em }
</style>
<tarjeta-tema>Por defecto (fallback)</tarjeta-tema>
<tarjeta-tema class="amarilla">Con variables</tarjeta-tema>
<tarjeta-tema class="oscura">Otra variante</tarjeta-tema>
```
```js
import {LitElement, html, css} from 'lit';

class TarjetaTema extends LitElement {
  static styles = css`
    :host { display: block; margin: 8px 0; padding: 12px; border-radius: 12px;
            background: var(--tarjeta-fondo, var(--surface-2));
            color: var(--tarjeta-texto, var(--text)); }
    h4 { margin: 0 0 4px }`;
  render() { return html`<h4 part="titulo">Título (part)</h4><slot></slot>`; }
}
customElements.define('tarjeta-tema', TarjetaTema);
```
Reto: añade `--tarjeta-fondo: tomato` en una regla `tarjeta-tema { ... }` del HTML.
Clave: Se tematiza con herencia CSS, custom properties var(--x, fallback) y ::part(). Es la API de estilos pública del componente.

## :host, ::slotted, classMap y styleMap
`:host([destacado])` reacciona a un atributo reflejado; `::slotted(em)` solo alcanza hijos directos del slot (la negrita queda sin estilo).
```html
<mi-aviso>Texto con <em>énfasis proyectado</em> y <strong>negrita (no estilada)</strong></mi-aviso>
```
```js
import {LitElement, html, css} from 'lit';
import {classMap} from 'lit/directives/class-map.js';
import {styleMap} from 'lit/directives/style-map.js';

class MiAviso extends LitElement {
  static properties = { destacado: {type: Boolean, reflect: true}, tam: {type: Number} };
  static styles = css`
    :host { display: block; padding: 10px; border: 2px solid var(--line); border-radius: 10px }
    :host([destacado]) { border-color: var(--primary); background: var(--primary-soft) }
    ::slotted(em) { color: var(--bad) }
    .grande { font-weight: 800 }`;
  constructor() { super(); this.destacado = false; this.tam = 16; }

  render() {
    return html`
      <div class=${classMap({grande: this.destacado})} style=${styleMap({fontSize: this.tam + 'px'})}><slot></slot></div>
      <button @click=${() => (this.destacado = !this.destacado)}>destacado</button>
      <button @click=${() => (this.tam += 2)}>A+</button>`;
  }
}
customElements.define('mi-aviso', MiAviso);
```
Reto: cambia `::slotted(em)` por `::slotted(*)` y verás que ahora alcanza a todos los hijos directos, no a los anidados.
Clave: static styles se evalúa una vez por clase. :host estiliza el anfitrión; ::slotted solo hijos directos del slot.
