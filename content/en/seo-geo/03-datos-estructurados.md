---
title: Structured data (schema.org)
desc: Structured data helps search engines interpret a page. Learn which schema.org types to use, how to add JSON-LD and validate the markup.
---
Structured data describes the page in a format machines read without interpreting the text. It is added as **JSON-LD** in the `<head>`.

## Most useful types
| Page | Type |
|---|---|
| Article / guide | `Article`, `TechArticle` |
| Breadcrumbs | `BreadcrumbList` |
| Questions and answers | `FAQPage` (FAQ rich results are very limited in Google, but it still adds structure) |
| Organisation / site | `Organization`, `WebSite` |
| Product | `Product` + `Offer` + `AggregateRating` |
| Recipe, event, video | `Recipe`, `Event`, `VideoObject` |

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "TechArticle",
  "headline": "Reactive properties in Lit 3",
  "inLanguage": "en",
  "dateModified": "2026-10-29",
  "author": {"@type": "Person", "name": "Your name"}
}
</script>
```

## Rules
- Mark up only what **is visible on the page**. Data the user cannot see can lead to a penalty.
- One source of truth: generate the JSON-LD from the same data as the page (as this site does).
- Validate with the **Rich Results Test** and the **Schema Markup Validator**.
- ISO 8601 dates; absolute URLs.

> [!AI] Careful
> The AI invents properties or ratings. Do not mark up ratings that do not exist: it is against the policies and risks a manual action.

=== esquema
# Basics
- JSON-LD — the recommended format, in the head.
- schema.org — the vocabulary of types.
# Types
- Article and TechArticle — guides and articles.
- BreadcrumbList — breadcrumbs.
- Organization and WebSite — the entity and the site.
- Product — with Offer and real ratings.
=== test
? What do you mark up with structured data?
* Only what is visible on the page
- Hidden data to rank better
- Invented ratings
! Marking up the invisible goes against the policies.
? How do you validate the markup?
- By eye
* Rich Results Test and Schema Markup Validator
- With a CSS linter
! They detect errors and invalid properties.
? What is the recommended format?
* JSON-LD
- Microdata only
- Old XML
! It is independent of the visible HTML.
