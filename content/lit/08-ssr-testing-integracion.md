---
title: SSR, testing e integración con frameworks
desc: Probar Lit, renderizar en servidor, usarlo en React y migrar de Lit 1/2.
pkgs: lit, "@lit/react", "@lit-labs/ssr", "@web/test-runner"
---
## Testing
En navegador real: Web Test Runner (+ `@open-wc/testing`, `fixture`) o Playwright. Siempre `await el.updateComplete` antes de las aserciones.
```ts
const el = await fixture<MyEl>(html`<my-el name="Ana"></my-el>`);
expect(el.shadowRoot!.textContent).to.contain('Ana');
```

## SSR (`@lit-labs/ssr`, experimental)
Genera HTML con **Declarative Shadow DOM** y se hidrata en cliente (`@lit-labs/ssr-client`). Solo corren `willUpdate` y `render`. Integraciones: Eleventy, Astro, Next (pages), Nuxt.

## En React
```tsx
import {createComponent} from '@lit/react';
export const MyEl = createComponent({tagName: 'my-el', elementClass: MyElement, react: React, events: {onSelect: 'item-selected'}});
```
React 19 ya pasa propiedades y eventos a custom elements; en React < 19 todo llegaba como atributo string, por eso existe el wrapper.

## En Angular
Añade `CUSTOM_ELEMENTS_SCHEMA` y enlaza propiedades con `[prop]` y eventos con `(evento)`.

## Otros
- **Localización**: `@lit/localize`.
- **Publicar**: ES modules; `lit` como dependencia, no empaquetado dentro.
- `lit-analyzer` / plugin de IDE detecta errores de plantilla.

## Lit 1/2 → 3
- `lit-element` + `lit-html` → paquete único `lit`. `UpdatingElement` → `ReactiveElement`.
- Decoradores en `lit/decorators.js`; Lit 3 admite los estándar (`accessor`).
- Lit 3: ES2021, sin IE11. Libs pueden declarar `"^2.7.0 || ^3.0.0"`.

=== esquema
# Testing
- Entorno — debe ser un navegador, sin simular el DOM.
- Herramientas — son web Test Runner y WebdriverIO.
- updateComplete — espera A que termine el render antes de comprobar.
# SSR
- @lit-labs/ssr — renderiza componentes a HTML en Node.
- Declarative Shadow DOM — describe el shadow root dentro del HTML.
- Hidratación — reactiva los componentes en el cliente.
# React
- createComponent — crea un wrapper React de un elemento Lit.
- events — mapea eventos personalizados a props.
- useController — convierte un controller en un hook.
# Cambios de Lit 3
- Compatibilidad — descarta IE11 y APIs deprecadas de Lit 2.x.
- UpdatingElement — se sustituye por ReactiveElement.
- Decoradores — se importan de lit/decorators.js.
# Decoradores estándar
- accessor — es la palabra clave que se añade a campos decorados.
- TypeScript — necesita la versión 5.2 o superior.
- Interoperabilidad — permite mezclar Lit 2.x y 3.0.
# Entrevista
- Elegir Lit — se justifica con Estándares, tamaño e interoperabilidad.
- Contras — son ecosistema menor que React y SSR experimental.
- Tu ejemplo — debe incluir Decisión, trade-off y resultado.

=== test
? Monta el componente en un test (open-wc):
```js
const el = await ___(html`<mi-boton></mi-boton>`);
```
* fixture
- render
- mount
- create
! fixture renderiza la plantilla en el navegador y espera al primer update.

? Espera a que el componente termine de actualizarse:
```js
el.shadowRoot.querySelector('button').click();
await el.___;
expect(el.shadowRoot.textContent).to.equal('1');
```
* updateComplete
- ready
- renderComplete
- whenDefined
! updateComplete es la promesa que se resuelve al terminar el update.

? Usa el web component dentro de React:
```js
const MiBoton = ___({ react: React, tagName: 'mi-boton', elementClass: MiBotonEl });
```
* createComponent
- wrap
- createElement
- defineComponent
! createComponent, de @lit/react, genera el wrapper de React.

? Importa la base de Lit 3:
```js
import { LitElement, html } from '___';
```
* lit
- lit-element
- lit-html
- @lit/core
! En Lit 2 y 3 todo se importa desde el paquete lit.

? Declara una propiedad reactiva con decoradores estándar:
```js
@property({ type: Number })
___ count = 0;
```
* accessor
- static
- let
- reactive
! Los decoradores estándar necesitan la palabra accessor en el campo.

? Declara el estado interno con el decorador:
```js
@___() accessor _abierto = false;
```
* state
- internal
- observe
- private
! @state marca estado privado y reactivo, sin atributo.

=== prueba

## El ejercicio de entrevista: componente completo
Reúne lo importante: propiedad reactiva con reflect, derivado en willUpdate, slot con nombre y fallback, evento composed, custom property y :host. Intenta escribirlo de memoria.
```html
<style>contador-tarjeta { --contador-borde: var(--primary) }</style>
<contador-tarjeta max="3"><span slot="titulo">Mi contador</span></contador-tarjeta>
```
```js
import {LitElement, html, css} from 'lit';

class ContadorTarjeta extends LitElement {
  static properties = {
    cuenta: {type: Number, reflect: true},
    max: {type: Number},
    mensaje: {state: true},
  };
  static styles = css`
    :host { display: block; padding: 12px; border: 2px solid var(--contador-borde, var(--line)); border-radius: 12px }
    ::slotted([slot=titulo]) { font-weight: 800 }
    button { padding: 6px 14px }`;

  constructor() { super(); this.cuenta = 0; this.max = 5; this.mensaje = ''; }

  willUpdate(cambios) {                                   // derivados aquí
    if (cambios.has('cuenta') || cambios.has('max')) {
      this.mensaje = this.cuenta >= this.max ? '¡Máximo!' : `Faltan ${this.max - this.cuenta}`;
    }
  }
  updated(cambios) {                                      // efecto tras renderizar
    if (cambios.has('cuenta') && cambios.get('cuenta') !== undefined) {
      this.dispatchEvent(new CustomEvent('cuenta-cambiada', {detail: {cuenta: this.cuenta}, bubbles: true, composed: true}));
    }
  }
  render() {
    return html`
      <slot name="titulo">Contador</slot>
      <p>${this.cuenta} — ${this.mensaje}</p>
      <button ?disabled=${this.cuenta >= this.max} @click=${() => this.cuenta++}>+1</button>`;
  }
}
customElements.define('contador-tarjeta', ContadorTarjeta);

document.addEventListener('cuenta-cambiada', (e) => console.log('evento recibido: cuenta =', e.detail.cuenta));
```
Reto: borra el código del editor y reescríbelo de memoria; ejecuta y compara.
Clave: Si lo explicas mientras lo escribes (reactividad, ciclo, shadow DOM, eventos), cubres el 80 % de la entrevista.
