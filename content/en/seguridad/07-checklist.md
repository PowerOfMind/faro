---
title: Checklist before publishing
desc: 20 security, privacy and quality checks for an app built with AI.
---
## Secrets and configuration
1. No key in the client or in the git history.
2. `.env` ignored; `.env.example` without values.
3. Spending limits and alerts at the AI and cloud providers.
4. Debug mode off; generic errors for the user.

## Access and data
5. Every endpoint checks the session **and** ownership of the resource.
6. Database rules (RLS/Firestore/Storage) enabled and tested with two users.
7. Inputs validated on the server with a schema (Zod, Valibot...).
8. Parameterised queries.
9. Rate limiting on login, sign-up, recovery and endpoints that cost money.
10. Payment webhooks with the signature verified.

## Browser
11. HTTPS and HSTS.
12. CSP, `nosniff`, `Referrer-Policy`.
13. `HttpOnly; Secure; SameSite` cookies.
14. No `innerHTML` with unsanitised data.

## Dependencies
15. `npm audit` with no critical issues; lockfile committed.
16. Every new dependency checked (it exists, is maintained, is not suspicious).

## Legal and privacy
17. Legal notice, privacy policy and cookies where applicable (GDPR in the EU).
18. Consent before non-essential cookies.
19. Backups and a way to delete a user's data.

## Quality
20. Test on mobile, with keyboard and a basic screen reader; Lighthouse with no serious errors.

> [!TIP] Automate what you can
> Gitleaks in pre-commit, Dependabot, `npm audit` in CI, and a pre-launch audit agent to walk this list against the real code.

=== esquema
# Before publishing
- Secrets — no key in the client or in the history.
- Access — session and resource ownership on every endpoint.
- Data — RLS/rules enabled and tested with two users.
- Limits — rate limiting and a spending cap.
- Browser — HTTPS, HSTS, CSP, secure cookies.
- Legal — privacy and cookies where applicable.
=== test
? Before publishing, how do you test access control?
* With two users trying to access each other's resources
- With a single admin user
- By glancing at the code
! It is the most direct way to detect IDOR.
? What do you put on payments and endpoints that cost money?
- Nothing
* Rate limiting and spending limits
- More animations
! It prevents abuse and unexpected bills.
? What do you automate in CI?
* npm audit and a secret scanner
- The design
- The legal texts
! They catch recurring failures without manual effort.
