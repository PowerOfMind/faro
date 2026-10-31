---
title: Controllers, Context y Task
desc: Controllers, Context y Task en Lit para reutilizar lógica y compartir datos, con ejemplos de ciclo de vida y tareas asíncronas.
pkgs: lit, @lit/context, @lit/task
---
## Reactive Controllers
Objeto que se engancha al ciclo de vida del host.
```ts
class ClockController implements ReactiveController {
  value = new Date(); private t?: number;
  constructor(private host: ReactiveControllerHost) { host.addController(this); }
  hostConnected() { this.t = setInterval(() => { this.value = new Date(); this.host.requestUpdate(); }, 1000); }
  hostDisconnected() { clearInterval(this.t); }
}
// en el componente: private clock = new ClockController(this);
```
**Frente a mixins**: tiene estado propio, no toca el prototipo, puedes tener varios por host y no hay colisiones de nombres. Casos: observers, eventos externos, tareas async.

## Context (`@lit/context`)
```ts
export const userContext = createContext<User>('user');
// proveedor
@provide({context: userContext}) user = {...};
// consumidor
@consume({context: userContext, subscribe: true}) user!: User;
```
- Sin `subscribe: true` el consumidor recibe el valor **una sola vez**.
- Usa eventos DOM (`context-request`): interopera con otras librerías.
- Casos: usuario actual, idioma, servicios, tema.

## Task (`@lit/task`)
```ts
private _user = new Task(this, {
  task: async ([id], {signal}) => (await fetch(`/u/${id}`, {signal})).json(),
  args: () => [this.id] as const,
});
render() {
  return this._user.render({
    pending: () => html`Cargando…`,
    complete: u => html`${u.name}`,
    error: e => html`Error: ${e}`,
  });
}
```
Estados `INITIAL`, `PENDING`, `COMPLETE`, `ERROR`. Se reejecuta al cambiar `args`; la ejecución anterior recibe un `AbortSignal` (pásalo a `fetch`). `autoRun: false` + `run()` para modo manual.

=== esquema
# Qué es
- ReactiveController — es una interfaz con hooks opcionales del ciclo.
- addController — registra el controller en el host, que es LitElement o cualquier ReactiveControllerHost.
- requestUpdate — pide un render cuando cambia el estado del controller.
# Hooks
- hostConnected — monta Listeners, observers o timers.
- hostUpdate y hostUpdated — permiten leer el DOM antes y después de la actualización.
- hostDisconnected — limpia lo creado en hostConnected.
# Composición
- Mixins — añaden comportamiento en el prototipo y la cadena de herencia.
- Controllers — evitan colisiones de nombres y permiten varias instancias.
- Casos de uso — incluyen ResizeObserver, eventos externos y tareas asíncronas.
# Context
- createContext — define la clave que identifica los datos.
- @provide / @consume — conectan proveedor y consumidor; también ContextProvider y ContextConsumer.
- subscribe: true — da actualizaciones posteriores al consumidor.
- context-request — es el evento DOM del protocolo comunitario.
# Task
- Task — es un controller reactivo con task, args y autoRun.
- TaskStatus — tiene INITIAL, PENDING, COMPLETE y ERROR.
- task.render — recibe initial, pending, complete y error.
- AbortSignal — cancela la ejecución anterior si llega una más nueva.
# Cuándo
- Context — sirve para Usuario, locale, servicios y temas.
- Task — sirve para fetch con carga, éxito y error en el template.

=== test
? Registra el controller en el host:
```js
constructor(host) {
  (this.host = host).___(this);
}
```
* addController
- registerController
- attach
- use
! El host expone addController para engancharlo a su ciclo de vida.

? Limpia el listener cuando el host se desconecta:
```js
hostConnected() {
  window.addEventListener('mousemove', this._m);
}
___() {
  window.removeEventListener('mousemove', this._m);
}
```
* hostDisconnected
- hostRemoved
- disconnect
- hostDestroy
! hostDisconnected es el hook de limpieza del controller.

? Pide al host que se repinte con la nueva posición:
```js
this._m = (e) => {
  this.pos = { x: e.clientX, y: e.clientY };
  this.host.___();
};
```
* requestUpdate
- render
- update
- refresh
! El controller no renderiza: pide un update al host.

? Crea una clave de contexto:
```js
const ctx = ___('tema');
```
* createContext
- newContext
- context
- provide
! createContext crea la clave que comparten proveedor y consumidores.

? Consume el contexto y recibe cada cambio:
```js
@___({ context: ctx, subscribe: true })
tema;
```
* consume
- provide
- inject
- state
! consume con subscribe: true actualiza el valor cuando cambia.

? Provee el contexto sin decoradores:
```js
_p = new ___(this, { context: ctx, initialValue: 'claro' });
```
* ContextProvider
- ContextRoot
- ContextRequest
- Provider
! ContextProvider es la versión con controller del decorador @provide.

=== prueba

## Un ReactiveController: el reloj
El controller arranca el intervalo al conectarse y lo limpia al desconectarse. Quita y vuelve a poner el elemento y mira los logs.
```html
<div id="host"><mi-reloj></mi-reloj></div>
<p><button id="q">Quitar</button> <button id="p">Poner</button></p>
```
```js
import {LitElement, html} from 'lit';

class ClockController {
  constructor(host, intervalo = 1000) {
    this.host = host;
    this.intervalo = intervalo;
    this.value = new Date().toLocaleTimeString();
    host.addController(this);                    // se registra en el host
  }
  hostConnected() {
    console.log('hostConnected → arranca setInterval');
    this.timer = setInterval(() => {
      this.value = new Date().toLocaleTimeString();
      this.host.requestUpdate();                 // pide un render
    }, this.intervalo);
  }
  hostDisconnected() {
    console.log('hostDisconnected → clearInterval');
    clearInterval(this.timer);
  }
}

class MiReloj extends LitElement {
  clock = new ClockController(this, 1000);
  render() { return html`<p>Hora: <b>${this.clock.value}</b></p>`; }
}
customElements.define('mi-reloj', MiReloj);

const el = document.querySelector('mi-reloj');
document.getElementById('q').onclick = () => el.remove();
document.getElementById('p').onclick = () => document.getElementById('host').append(el);
```
Reto: añade un `hostUpdated() { console.log('hostUpdated'); }` al controller.
Clave: Controller = lógica reutilizable ligada al ciclo del host. Registro: host.addController(this); refresco: host.requestUpdate().

## Reutilizar un controller en varios componentes
El mismo ResizeController da el ancho a dos componentes distintos. Mueve el slider para redimensionar el segundo.
```html
<ancho-a></ancho-a>
<ancho-b style="width:60%"></ancho-b>
<input type="range" min="30" max="100" value="60" oninput="document.querySelector('ancho-b').style.width = this.value + '%'">
```
```js
import {LitElement, html, css} from 'lit';

class ResizeController {
  w = 0;
  constructor(host) { this.host = host; host.addController(this); }
  hostConnected() {
    this.obs = new ResizeObserver(([e]) => { this.w = Math.round(e.contentRect.width); this.host.requestUpdate(); });
    this.obs.observe(this.host);
  }
  hostDisconnected() { this.obs.disconnect(); }
}

const caja = css`:host { display: block; padding: 8px; margin: 6px 0; border: 1px dashed var(--primary); border-radius: 8px }`;

class AnchoA extends LitElement {
  static styles = caja;
  size = new ResizeController(this);
  render() { return html`A mide ${this.size.w}px`; }
}
class AnchoB extends LitElement {
  static styles = caja;
  size = new ResizeController(this);
  render() { return html`B mide <b>${this.size.w}px</b> (mismo controller, otra instancia)`; }
}
customElements.define('ancho-a', AnchoA);
customElements.define('ancho-b', AnchoB);
```
Reto: un mixin habría añadido métodos al prototipo; el controller no toca la clase y puedes tener varios por host.
Clave: Controller frente a mixin: identidad y estado propios, sin colisiones de nombres, varios por host y composable.

## Context: datos sin prop drilling
La raíz provee el tema; la capa intermedia no sabe nada de él; la hoja lo consume con `subscribe: true`.
```html
<app-raiz></app-raiz>
```
```js
import {LitElement, html} from 'lit';
import {createContext, ContextProvider, ContextConsumer} from '@lit/context';

const temaCtx = createContext('tema');

class AppRaiz extends LitElement {
  provider = new ContextProvider(this, {context: temaCtx, initialValue: 'claro'});
  render() {
    return html`
      <button @click=${() => this.provider.setValue(this.provider.value === 'claro' ? 'oscuro' : 'claro')}>
        Cambiar tema (en la raíz)
      </button>
      <capa-media></capa-media>`;
  }
}
class CapaMedia extends LitElement {
  render() {
    return html`<div style="padding:8px;border:1px dashed var(--line);margin-top:8px">
      Capa intermedia (no recibe ni pasa el tema por props)
      <div><boton-hoja></boton-hoja></div></div>`;
  }
}
class BotonHoja extends LitElement {
  consumer = new ContextConsumer(this, {context: temaCtx, subscribe: true});
  render() {
    const t = this.consumer.value;
    return html`<span style="display:inline-block;margin-top:6px;padding:6px 12px;border-radius:8px;
      background:${t === 'oscuro' ? '#111' : '#fde68a'};color:${t === 'oscuro' ? '#fff' : '#111'}">Soy la hoja → tema ${t}</span>`;
  }
}
customElements.define('app-raiz', AppRaiz);
customElements.define('capa-media', CapaMedia);
customElements.define('boton-hoja', BotonHoja);
```
Reto: quita `subscribe: true`: la hoja se queda con el valor inicial y no vuelve a actualizarse.
Clave: Context usa el evento DOM «context-request»: el consumidor lo lanza y un ancestro proveedor responde. Sirve para usuario, locale, servicios, temas.
