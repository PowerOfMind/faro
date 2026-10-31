---
title: Verify what the AI tells you
desc: AI answer verification helps developers catch invented APIs, packages and commands using documentation, version checks and small tests.
---
## What gets invented most
| What | How you notice |
|---|---|
| Functions or parameters that don't exist | "is not a function", an option silently ignored |
| An API from another version | Works in the example, fails in your project |
| Non-existent packages | `npm install` fails... or installs a **malicious** one with that name |
| CLI flags | `unknown option` |
| Exact-looking facts | Versions, dates, limits, prices |

## A 60-second check
1. **Search the symbol in the official docs** for the version you use.
2. `npm view <package> version time.modified` (does it exist? is it maintained?).
3. **Run it**: a minimal test beats rereading the code.
4. Ask the AI: "In which version was this added and where is it documented?" If it hesitates, distrust it.
5. Open the changelog if the API changed recently.

## If you are not convinced
- Paste the **real documentation** into the chat and ask it to stick to it.
- Ask it to quote the doc passage it relies on.
- Switch model or use web search.

> [!WARN] Confidence
> A confident, fluent answer is not a correct answer. Tone does not measure reliability.

=== esquema
# Invented
- APIs and parameters — functions that do not exist.
- Versions — an API from another version of the library.
- Packages — non-existent (or malicious) names.
# Check
- Official docs — search the symbol in your version.
- npm view — does it exist and is it maintained?
- Run it — a minimal test beats rereading.
=== test
? A confident, fluent answer: is it reliable because of that?
- Yes, the tone shows it
* No: tone does not measure correctness
- Only if it is long
! Models sound sure even when they invent.
? What is the fastest check for an unknown function?
* Search it in the docs for your version
- Ask the same model again
- Copy it and hope
! The official docs for your version are the source of truth.
? Before installing a package the AI suggested...
- Install it and see if it fails
* Check with npm view that it exists, who maintains it and when it was published
- Trust the name
! It may not exist, or be a malicious package using that name.
