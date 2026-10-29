---
title: Technical SEO on one page
desc: The minimum that decides whether you get indexed and how you are displayed.
---
## Essentials
| Element | Rule |
|---|---|
| `<title>` | Unique per page, ~50-60 characters, keyword first |
| `meta description` | ~140-160 characters, written to win the click |
| `<h1>` | One, describes the page |
| `<html lang>` | The right language (`en`) |
| `canonical` | The preferred URL; avoids duplicates from parameters |
| Images | Descriptive `alt`, `width`/`height`, modern format (WebP/AVIF) |
| URLs | Short, readable, stable; 301-redirect if they change |
| Internal links | Descriptive text, not "click here" |

```html
<title>Lit 3 guide: reactive properties</title>
<meta name="description" content="How @property and @state work in Lit 3, when it re-renders and the class fields trap.">
<link rel="canonical" href="https://example.com/lit/reactivity">
<meta property="og:title" content="..."><meta property="og:image" content="https://example.com/og.png">
```

## Crawling and indexing
- `robots.txt` says what to crawl; it does **not** stop a URL from appearing. To avoid indexing use `<meta name="robots" content="noindex">`.
- `sitemap.xml` with canonical URLs, referenced in `robots.txt` and submitted in Search Console.
- A real 404 returns status 404 (not 200 with "not found").
- Use **Google Search Console**: coverage, performance, URL inspection (shows the rendered HTML Google sees).

## Performance (Core Web Vitals)
| Metric | Target | Lever |
|---|---|---|
| LCP | < 2.5 s | Optimised main image, `fetchpriority="high"`, less blocking JS |
| INP | < 200 ms | Less main-thread JS, split long tasks |
| CLS | < 0.1 | Reserve space for images, ads and fonts |

Measure with PageSpeed Insights (field data) and Lighthouse (lab).

> [!AI] AI and SEO
> It tends to generate pages with a repeated `<title>`, several `h1`s or content only in JS. Check "View source" (not the inspector) to know what a crawler without JS sees.

=== esquema
# Essentials
- title — unique, ~50-60 characters.
- meta description — ~140-160, written for the click.
- h1 — one per page.
- canonical — the preferred URL.
# Crawling
- robots.txt — crawling, not indexing; to avoid indexing use noindex.
- sitemap.xml — canonical URLs.
- Core Web Vitals — LCP, INP and CLS.
=== test
? Does robots.txt stop a URL from appearing in search engines?
- Yes, always
* No: to avoid indexing you use noindex
- Only on mobile
! robots.txt controls crawling, not indexing.
? LCP target:
* Under 2.5 s
- Under 10 s
- Does not matter
! It is the loading metric for the main content.
? What does "View source" show that the inspector does not?
* The HTML a crawler receives without running JS
- The compiled CSS
- The cookies
! It shows what exists before JavaScript runs.
