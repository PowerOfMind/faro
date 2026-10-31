---
title: Risks of AI-generated code
desc: AI-generated code can hide security flaws. Review common risks involving secrets, access control and input validation before publishing.
---
Generated code **compiles and looks right**. That is exactly the risk: the AI optimises for it working in the happy-path example, not for resisting an attacker.

## Failures that repeat
| Failure | Example |
|---|---|
| Secrets in the client or the repo | An API key in browser JS, a committed `.env` |
| Validation only on the front end | The button is disabled, but the endpoint accepts anything |
| Missing authorisation (IDOR) | `GET /api/orders/123` returns another user's order |
| Open database | Firebase/Supabase rules in test mode, RLS disabled |
| Injection | Concatenated SQL, `innerHTML` with user text |
| Dubious dependencies | An invented or abandoned package |
| Error messages with internals | Stack traces shown to the user |
| No usage limit | An endpoint that calls the model with no rate limit: an infinite bill |

## Minimum review (15 minutes)
1. **Look for secrets**: `git grep -nEi "api[_-]?key|secret|token|password"` and check the history.
2. **For every endpoint**: who can call it? Does it check the resource is *theirs*? Does it validate the body?
3. **For every query**: is it parameterised?
4. **For every `innerHTML`/`dangerouslySetInnerHTML`/`unsafeHTML`**: where does the data come from?
5. **Database rules** in production, not in test mode.
6. `npm audit` and review the new dependencies.
7. **Test as an attacker**: open another session as another user and request the first user's resources.

> [!AI] Ask the AI, but do not treat it as the only barrier
> "Review this endpoint like a pentester: list possible unauthorised access." Useful as a second opinion. It does not replace real tests or a human review of auth and payments.

> [!SEC] Reference framework
> **OWASP Top 10** (web apps) and **OWASP Top 10 for LLMs** (if your app calls models) are the lists to walk through. Next: [secrets](@/seguridad/secretos), [auth and data](@/seguridad/auth-y-datos), [checklist](@/seguridad/checklist).

=== esquema
# Typical failures
- Secrets in the client — keys in browser JS or in git.
- Front-end-only validation — the endpoint accepts anything.
- IDOR — nobody checks the resource belongs to the user.
- Open database — RLS disabled or rules in test mode.
# Review
- Look for secrets — git grep and the history.
- Every endpoint — who can call it and on which resource.
- Test with two users — request the other one's resources.
=== test
? Why is "working" generated code dangerous?
* It optimises the happy path, not resisting an attacker
- It always has syntax errors
- It is slower
! Working does not mean secure.
? A button is disabled on the front end. Is that enough as access control?
- Yes
* No: the server must check on every request
- Only with HTTPS
! Anyone can call the endpoint directly.
? Which list do you walk through if your app calls models?
- OWASP Top 10 for LLMs
- ISO 9001
- Lighthouse
! Besides the web Top 10, it covers prompt injection and excessive consumption.
