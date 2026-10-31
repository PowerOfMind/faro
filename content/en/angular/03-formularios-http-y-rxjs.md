---
title: Angular: forms, HTTP and RxJS
desc: A practical guide to angular: forms, http and rxjs, common mistakes, decisions, and checks to help you solve problems with confidence.
pkgs: @angular/core, @angular/forms, @angular/common, rxjs
---
## Reactive forms
`FormControl` represents a field and `FormGroup` groups controls. Import `ReactiveFormsModule`, apply validators and show errors after the field is touched or submitted. Do not rely only on client validation.

## HTTP
Configure `provideHttpClient()` and use `HttpClient` from a service. Its methods return observables: each subscription to an HTTP request can initiate another request. Handle errors and loading states.

## RxJS and templates
`map` transforms emissions, `switchMap` switches to the latest observable and `catchError` handles failures. The `async` pipe subscribes and unsubscribes when the view is destroyed; avoid manual subscriptions without cleanup.

## Quick decisions
| Question | Answer |
|---|---|
| What does FormControl represent? | A field |
| How do you configure HttpClient? | With provideHttpClient |
| What can two HTTP subscriptions cause? | Two requests |

> [!AI] With AI
> Describe your version, environment, expected and actual results, and a minimal reproduction. Ask for a testable explanation and references to the official documentation.

Documentation: [official guide](https://angular.dev/guide/forms/reactive-forms).

Related: [continue with a related guide](@/angular/signals-y-control-flow).

=== esquema
# Key ideas
- Reactive forms — `FormControl` represents a field and `FormGroup` groups controls.
- HTTP — Configure `provideHttpClient()` and use `HttpClient` from a service.
- RxJS and templates — `map` transforms emissions, `switchMap` switches to the latest observable and `catchError` handles failures.
=== test
? What does FormControl represent?
* A field
- With provideHttpClient
- Two requests
! A field.
? How do you configure HttpClient?
* With provideHttpClient
- Two requests
- Switches to the latest observable
! With provideHttpClient.
? What can two HTTP subscriptions cause?
* Two requests
- Switches to the latest observable
- The pipe when the view is destroyed
! Two requests.
? What does switchMap do?
* Switches to the latest observable
- The pipe when the view is destroyed
- A field
! Switches to the latest observable.
? Who cleans up an async subscription?
* The pipe when the view is destroyed
- A field
- With provideHttpClient
! The pipe when the view is destroyed.
