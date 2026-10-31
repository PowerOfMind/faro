---
title: Secrets and API keys
desc: API key security helps developers prevent leaks. Learn where secrets belong, how to restrict access and what to do after exposure.
---
## Rule
Everything that reaches the browser is public: JS, HTML, `VITE_*` / `NEXT_PUBLIC_*` variables, source maps. **A key in the client is a published key.**

## Where they go
| Type | Where |
|---|---|
| Server key (AI model, Stripe secret, DB) | Environment variables **on the server** or a secrets manager |
| "Public" key (Stripe publishable, Maps with a domain restriction) | Client, but **restricted** by domain/API |
| User token | `HttpOnly; Secure; SameSite` cookie rather than `localStorage` |

If the browser needs to use an AI model or a payment API, create **your own endpoint** that makes the call with the key, authenticates the user and limits usage.

## Avoid the accident
```bash
echo ".env*" >> .gitignore && echo "!.env.example" >> .gitignore
```
- A `pre-commit` hook with a scanner (gitleaks, trufflehog) blocks keys before the commit.
- Turn on the provider's secret scanning (GitHub secret scanning and push protection).
- Do not paste keys into the chat with the AI; use fake values.
- Agents: make them **unable to read** `.env` (the agent's permission rules).

## If it leaked
1. **Revoke and rotate** the key now. It is the only thing that matters in the first hour.
2. Check the provider's usage/billing for unusual activity.
3. Clean the history (`git filter-repo`) only afterwards, and assume it is still compromised.
4. Add spending limits and alerts.

> [!WARN] Bots
> Bots scan public repos and find keys within minutes. A repository that is "private for a while" is not safe.

=== esquema
# Rule
- Everything that reaches the browser is public — including VITE_* and NEXT_PUBLIC_*.
- Server key — on the server only.
# If it leaked
- Revoke and rotate — first, now.
- Check the provider's usage — unusual activity.
- Spending limits — and alerts.
=== test
? Your browser needs to call a paid AI model. How do you do it?
- Put the key in a VITE_ variable
* Create your own endpoint that uses the key, authenticates and limits usage
- Obfuscate it in the JS
! The key can only live on the server.
? You pushed a key to a public repo. What do you do first?
* Revoke it and create another
- Delete the commit
- Make the repo private
! Bots copy it within minutes; the history is secondary.
? What prevents the accident before the commit?
- A CSS linter
* A secret scanner (gitleaks) in pre-commit
- Restarting the machine
! It blocks keys before they leave your machine.
