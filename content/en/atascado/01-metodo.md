---
title: Breaking out of the AI loop
desc: What to do when you are three attempts in and the error is still the same.
---
The pattern: the AI proposes a fix, it fails, it proposes a similar one, it fails. **Every attempt adds noise to the context.** Stop.

## Method
1. **Reproduce small.** A minimal file that fails. If you cannot reproduce it, you do not understand it yet.
2. **Read the whole error**, bottom to top in the stack: the first line of *your* code is usually the cause.
3. **One hypothesis, one test.** Change one thing and observe. Do not apply three fixes at once.
4. **Measure, don't assume.** `console.log` the real value, `typeof`, the Network tab, the installed version (`npm ls package`).
5. **Search the exact message** in quotes in the project's issue tracker, not only in a search engine.
6. **Restart the conversation** with: all versions, minimal code, exact error and **what you already ruled out**.
7. **Change angle**: ask the AI to explain the concept, not to fix the bug.

## Where to look when the AI does not know
| Source | When |
|---|---|
| Official docs for **your version** | Always first |
| Repository issues (open and closed) | Bugs and regressions |
| Releases / CHANGELOG | "It used to work" |
| Repo discussions, official Discord | Odd cases |
| Stack Overflow | Classic errors; check the date and version |
| The library source | When the docs are silent |

## A question that gets an answer (human or AI)
```text
I want: <goal>
Environment: Node 22, Vite 7, Windows 11
Minimal code: <20 lines>
Expected: <...>  Got: <full error>
Already tried: <1>, <2>
```

> [!TIP] Bisect
> If "it used to work": `git bisect`, or go back to the last good commit and reapply the changes one by one.

=== esquema
# Method
- Reproduce small — a minimal file that fails.
- One hypothesis, one test — change one thing at a time.
- Measure — log the real value and the installed version.
# If it persists
- Search the exact message — in the project's issues.
- Restart the conversation — with versions, minimal code and what you ruled out.
- git bisect — if it used to work.
=== test
? What do you do before asking the AI for another fix?
- Ask for three fixes at once
* Reproduce the failure in a minimal example
- Switch framework
! If you cannot reproduce it small, you do not understand the problem yet.
? In a stack trace, which line usually shows the cause?
* The first line of your own code
- The last library line
- The very first line
! Library lines are usually a consequence of something you called.
? "It used to work": which tool helps?
- git blame over the whole repo
* git bisect
- npm audit
! Bisect finds the commit that broke it.
