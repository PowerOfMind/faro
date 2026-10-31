---
title: Injection and XSS
desc: Injection and XSS prevention helps developers secure SQL, HTML and system commands with parameterisation, sanitisation and headers.
---
## SQL
```ts
// bad
db.query(`SELECT * FROM users WHERE email = '${email}'`);
// good: parameterised
db.query('SELECT * FROM users WHERE email = $1', [email]);
```
ORMs parameterise, except in their "raw" functions. Review them.

## XSS
Inserting user text as HTML lets scripts run in other people's browsers.
- **By default** React, Angular, Vue and Lit escape what you interpolate.
- The danger is in: `innerHTML`, `dangerouslySetInnerHTML`, `v-html`, `[innerHTML]`, `unsafeHTML`, `href="javascript:..."`.
- If you need user HTML (editor, markdown), **sanitise** with DOMPurify and an allow-list of tags.
- Validate URLs: only `https:` and `mailto:`.

## System commands
Never concatenate user input into `exec`. Use `execFile` with an argument array and validate the values.

## Headers that matter
```text
Content-Security-Policy: default-src 'self'; script-src 'self'; object-src 'none'; base-uri 'none'
Strict-Transport-Security: max-age=31536000; includeSubDomains
X-Content-Type-Options: nosniff
Referrer-Policy: strict-origin-when-cross-origin
Permissions-Policy: camera=(), microphone=(), geolocation=()
```
Start the CSP in `Content-Security-Policy-Report-Only` mode, see what breaks and tighten it. Free checks: securityheaders.com and the DevTools security panel.

## File uploads
Validate the type by content (not just extension), limit the size, store outside the public root and serve with `Content-Disposition: attachment` if it is not an image.

## CSRF
Session cookies + requests that change data: use `SameSite=Lax` or `Strict` and a CSRF token if there are cross-site forms.

> [!AI] Review sentence
> "List every point where user data reaches SQL, HTML, a URL, a command or a file, and say how each one is sanitised."

=== esquema
# Injection
- Parameterised queries — never concatenate input into SQL.
- execFile with an array — never user input in exec.
# XSS
- Escaped by default — React, Angular, Vue and Lit escape what you interpolate.
- Danger zones — innerHTML, dangerouslySetInnerHTML, v-html, unsafeHTML.
- DOMPurify — if you need user HTML.
- CSP — start in Report-Only mode.
=== test
? How do you avoid SQL injection?
* Parameterised queries
- Stripping quotes by hand
- Using capitals
! The engine separates code from data.
? When is rendering user text dangerous?
- With normal interpolation
* When inserting it as unsanitised HTML
- With textContent
! innerHTML and equivalents run what they receive.
? What is a CSP for?
* It limits which scripts and resources the page can load
- It speeds up loading
- It encrypts cookies
! It reduces the damage if an XSS arrives.
