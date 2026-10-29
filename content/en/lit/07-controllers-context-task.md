---
title: Controllers, Context and Task
desc: Reusing logic, avoiding prop drilling and handling async with states.
pkgs: lit, @lit/context, @lit/task
---
## Reactive Controllers
An object that hooks into the host's lifecycle.
```ts
class ClockController implements ReactiveController {
  value = new Date(); private t?: number;
  constructor(private host: ReactiveControllerHost) { host.addController(this); }
  hostConnected() { this.t = setInterval(() => { this.value = new Date(); this.host.requestUpdate(); }, 1000); }
  hostDisconnected() { clearInterval(this.t); }
}
// in the component: private clock = new ClockController(this);
```
**Versus mixins**: it has its own state, does not touch the prototype, you can have several per host and there are no name collisions. Cases: observers, external events, async tasks.

## Context (`@lit/context`)
```ts
export const userContext = createContext<User>('user');
// provider
@provide({context: userContext}) user = {...};
// consumer
@consume({context: userContext, subscribe: true}) user!: User;
```
- Without `subscribe: true` the consumer receives the value **only once**.
- It uses DOM events (`context-request`): it interoperates with other libraries.
- Cases: current user, language, services, theme.

## Task (`@lit/task`)
```ts
private _user = new Task(this, {
  task: async ([id], {signal}) => (await fetch(`/u/${id}`, {signal})).json(),
  args: () => [this.id] as const,
});
render() {
  return this._user.render({
    pending: () => html`Loading…`,
    complete: u => html`${u.name}`,
    error: e => html`Error: ${e}`,
  });
}
```
States `INITIAL`, `PENDING`, `COMPLETE`, `ERROR`. It reruns when `args` change; the previous run receives an `AbortSignal` (pass it to `fetch`). `autoRun: false` + `run()` for manual mode.

=== esquema
# What it is
- ReactiveController — an interface with optional lifecycle hooks.
- addController — registers the controller on the host, which is a LitElement or any ReactiveControllerHost.
- requestUpdate — asks for a render when the controller state changes.
# Hooks
- hostConnected — listeners, observers or timers.
- hostUpdate and hostUpdated — read the DOM before and after the update.
- hostDisconnected — clean up what was created in hostConnected.
# Composition
- Mixins — behaviour on the prototype and the inheritance chain.
- Controllers — no name collisions and allow several instances.
- Use cases — ResizeObserver, external events and async tasks.
# Context
- createContext — the key that identifies the data.
- @provide / @consume — provider and consumer; also ContextProvider and ContextConsumer.
- subscribe: true — later updates reach the consumer.
- context-request — the DOM event of the community protocol.
# Task
- Task — a reactive controller with task, args and autoRun.
- TaskStatus — INITIAL, PENDING, COMPLETE and ERROR.
- task.render — initial, pending, complete and error.
- AbortSignal — aborts the previous run if a newer one arrives.
# When
- Context — user, locale, services and themes.
- Task — a fetch with loading, success and error in the template.
=== test
? Register the controller on the host:
```js
constructor(host) {
  (this.host = host).___(this);
}
```
* addController
- registerController
- attach
- use
! The host exposes addController to hook it into its lifecycle.
? Clean up the listener when the host disconnects:
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
! hostDisconnected is the controller's cleanup hook.
? Ask the host to repaint with the new position:
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
! The controller does not render: it asks the host for an update.
? Create a context key:
```js
const ctx = ___('tema');
```
* createContext
- newContext
- context
- provide
! createContext creates the key shared by provider and consumers.
? Consume the context and receive every change:
```js
@___({ context: ctx, subscribe: true })
tema;
```
* consume
- provide
- inject
- state
! consume with subscribe: true updates the value when it changes.
? Provide the context without decorators:
```js
_p = new ___(this, { context: ctx, initialValue: 'claro' });
```
* ContextProvider
- ContextRoot
- ContextRequest
- Provider
! ContextProvider is the controller version of the @provide decorator.
=== prueba
## A ReactiveController: the clock
The controller starts the interval when connected and clears it when disconnected. Remove and re-add the element and watch the logs.
Reto: add a `hostUpdated() { console.log('hostUpdated'); }` to the controller.
Clave: Controller = reusable logic tied to the host's lifecycle. Registration: host.addController(this); refresh: host.requestUpdate().
## Reusing a controller in several components
The same ResizeController gives the width to two different components. Move the slider to resize the second one.
Reto: a mixin would have added methods to the prototype; the controller does not touch the class and you can have several per host.
Clave: Controller versus mixin: own identity and state, no name collisions, several per host and composable.
## Context: data without prop drilling
The root provides the theme; the middle layer knows nothing about it; the leaf consumes it with `subscribe: true`.
Reto: remove `subscribe: true`: the leaf keeps the initial value and never updates again.
Clave: Context uses the DOM event "context-request": the consumer fires it and an ancestor provider answers. Good for user, locale, services, themes.
