---
title: Git and deployment
desc: Git and deployment troubleshooting covers conflicts, lost commits, production route errors, environment differences and failed CI builds.
---
## Git: frequent situations
| I want to | Command |
|---|---|
| Undo the last commit keeping changes | `git reset --soft HEAD~1` |
| Discard changes to a file | `git restore file` |
| Save half-done changes | `git stash -u` / `git stash pop` |
| Find which commit broke something | `git bisect start` |
| Recover something "lost" | `git reflog` |
| Remove an already pushed file from the repo without deleting it | `git rm --cached file` |

- **Secret pushed by mistake**: revoke it **first** (rotate the key); rewriting history is secondary.
- Do not use `push --force` on shared branches; `--force-with-lease` if unavoidable.
- Conflicts: read both sides, do not accept "all mine" without looking.

## Works locally, fails in production
1. **404 on routes**: an SPA without a fallback to `index.html`, or a folder ignored by `.gitignore` (a case pattern on Windows can hide folders).
2. **Relative paths vs base**: GitHub Pages serves under `/repo/`; configure the bundler `base`.
3. **Case**: Windows/macOS do not distinguish; Linux (CI, hosting) does. `Logo.png` ≠ `logo.png`.
4. **Environment variables** not defined on the host.
5. **Build in CI**: a different Node, `npm ci` with an outdated lock, warnings treated as errors.
6. **CDN cache**: purge, or change the filename (hash).

## Before pushing
```bash
git status && git diff --stat
npm run build && npm test
```
Commit messages with the *why*; small commits are easier to revert.

> [!NOTE] Generated files
> If the repo contains build output, decide whether it is versioned. If not, `.gitignore` it and let CI generate it.

=== esquema
# Git
- reset --soft HEAD~1 — undoes the commit and keeps changes.
- stash -u — saves half-done changes.
- reflog — recovers what seems "lost".
- Pushed secret — revoke it first.
# Production
- Case — Linux tells Logo.png from logo.png.
- Base path — GitHub Pages serves under /repo/.
- Variables — defined on the host, not only in the local .env.
=== test
? You pushed a key to git by mistake. What do you do first?
- Rewrite the history
* Revoke and rotate the key
- Delete the repo
! If it leaked, it is already public; cleaning history is secondary.
? It works on your Windows and an image gives 404 in production. Suspicion?
* A difference in upper/lower case in the filename
- Lack of RAM
- The dark theme
! Linux distinguishes case; Windows does not.
? How do you undo the last commit without losing the changes?
- git reset --hard HEAD~1
* git reset --soft HEAD~1
- git revert --hard
! --soft leaves the changes staged.
