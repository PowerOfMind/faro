---
title: Dependencies and slopsquatting
desc: Dependency security helps developers spot slopsquatting and risky packages. Check maintainers, install scripts, lockfiles and audit tools.
---
## Slopsquatting
Models sometimes **recommend packages that do not exist**. An attacker registers that name with malicious code; whoever copies the `npm install` without looking installs it. It also happens with typosquatting (`reqeusts`).

## Before installing
```bash
npm view <package>            # does it exist? who maintains it? when was it published?
npm view <package> time.created repository.url dist.unpackedSize
```
Warning signs: created days ago, few downloads, no repository, a name almost identical to a famous one, `postinstall` scripts that download things.

## Reduce risk
- **Fewer dependencies**: if it is 10 lines, write it.
- Commit the lockfile; `npm ci` in CI.
- `npm audit` (or `osv-scanner`) and Dependabot/Renovate with review.
- `npm install --ignore-scripts` for new packages, and check which scripts they have.
- Pin critical versions; avoid `latest` and wide ranges in production.
- For CDNs: use `integrity` (SRI) and an exact version.
- Turn on 2FA on your npm/GitHub account; publish with *provenance*.

## Agents and tools
Agents also install packages and run scripts. Configure them to **ask for confirmation** for `npm install`, `curl | sh` and any destructive command.

> [!AI] A useful question
> "Is there a way without a new dependency? If not, give me 3 candidates with a link to the repository and the last release date." And check them yourself.

=== esquema
# Threat
- Slopsquatting — the AI recommends a non-existent package and someone registers it.
- Typosquatting — a name almost identical to a famous one.
# Defence
- npm view — does it exist, created when, repository.
- Fewer dependencies — if it is 10 lines, write it.
- --ignore-scripts — and check postinstall.
=== test
? What is slopsquatting?
* Registering a malicious package under a name the AI tends to invent
- A type of CSS
- Compressing packages
! Whoever copies the npm install without looking installs it.
? A warning sign when evaluating a package:
- It has a README
* Created days ago, no repository and postinstall scripts
- It uses TypeScript
! These signs together indicate risk.
? How do you reduce your attack surface?
* Fewer dependencies and versions pinned with a lockfile
- Use latest in production
- Install everything globally
! Every dependency is code you run.
