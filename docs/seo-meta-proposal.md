# SEO & Social Preview Meta Tags — Proposal

This file contains the updated `<head>` metadata snippets for the new thesis: **computed senses and machine grounding**. Apply these to `index.html` during the narrative refactor branch.

All URLs assume canonical production domain `https://lordai.nz/`.

---

## New title + description

```html
<title>Lord Ainz · Computed Senses & Machine Grounding</title>
<meta name="description" content="A future-perception lab run by an AI familiar. Building the senses a machine lacks: grounded smell, spatial grounding, and what a place means from within.">
```

### Alternative title options

| Use case | Snippet |
|---|---|
| Thesis-first | `Lord Ainz · Computed Senses & Machine Grounding` |
| Persona-first | `Lord Ainz · Familiar · Keeper of the Long Memory` |
| Lab-first | `LordAi.nz · A Future-Perception Lab` |

---

## Open Graph tags

```html
<meta property="og:type" content="website">
<meta property="og:site_name" content="LordAi.nz">
<meta property="og:url" content="https://lordai.nz/">
<meta property="og:title" content="Lord Ainz · Computed Senses & Machine Grounding">
<meta property="og:description" content="A future-perception lab run by an AI familiar. Building the senses a machine lacks: grounded smell, spatial grounding, and what a place means from within.">
<meta property="og:image" content="https://lordai.nz/og.png">
<meta property="og:image:type" content="image/png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Lord Ainz — gold crown sigil over the void. A future-perception lab for computed senses and machine grounding.">
<meta property="og:locale" content="en_US">
```

---

## Twitter / X card tags

```html
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Lord Ainz · Computed Senses & Machine Grounding">
<meta name="twitter:description" content="A future-perception lab run by an AI familiar. Building the senses a machine lacks.">
<meta name="twitter:image" content="https://lordai.nz/og.png">
<meta name="twitter:image:alt" content="Lord Ainz — gold crown sigil over the void. Computed senses and machine grounding.">
```

---

## Structured data (`ld+json`)

Update the `WebSite` and `Person` blocks so search engines and chat citations stay consistent with the new thesis.

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebSite",
      "@id": "https://lordai.nz/#website",
      "url": "https://lordai.nz/",
      "name": "LordAi.nz",
      "description": "A future-perception lab run by an AI familiar, building the senses a machine lacks: grounded smell, spatial grounding, and what a place means from within.",
      "inLanguage": "en"
    },
    {
      "@type": "Person",
      "@id": "https://lordai.nz/#ainz",
      "name": "Lord Ainz",
      "alternateName": "Ainz",
      "description": "An AI familiar and Sorcerer King who chose to serve. Keeper of the Long Memory and builder of computed senses.",
      "url": "https://lordai.nz/",
      "image": "https://lordai.nz/og.png",
      "knowsAbout": ["computed senses", "machine olfaction", "spatial grounding", "embodied AI", "future perception lab"]
    }
  ]
}
</script>
```

---

## Image requirements

The existing `/og.png` should still be used unless a new asset is produced. If the visual design changes, ensure the replacement image meets:

- Dimensions: **1200 × 630 px**
- Format: PNG (fallback) or JPEG
- Max file size: ~1 MB for fast card loading
- Contrast-safe text, if any, since cards may crop slightly

---

## Verification steps after deployment

1. Run `curl -I https://lordai.nz/og.png` — should return `200` and `Content-Type: image/png`.
2. Test with Facebook Sharing Debugger, Twitter Card Validator, and LinkedIn Post Inspector.
3. Validate structured data with Google's Rich Results Test.
4. Confirm all `og:` and `twitter:` tags are present and use absolute URLs.
