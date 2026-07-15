# LordAinz

![Static Site CI](https://github.com/JamesTRichmond/LordAinz/actions/workflows/ci.yml/badge.svg)

# LordAi.nz

A slick, self-contained static site for **Lord Ainz** — the Sorcerer-King
familiar. No build step, no dependencies, no tracking. Regal void-and-gold theme,
the 🤘, two interactive in-browser demos (Valence Flip + The Flatlander).
Sibling research repos (Petrichor, Nobody) are staged but private.

> **Status: LIVE** at [lordai.nz](https://lordai.nz). The repo is public and
> GitHub Pages serves it directly from `main` at the custom domain.

---

## Preview locally

```bash
open index.html          # macOS — opens in default browser
# or serve it:
python3 -m http.server 8080   # then visit http://localhost:8080
```

Edit copy/colors in `styles.css` — CSS custom properties live in `:root` at the
top (`--gold-500`, `--void-800`, `--blood-500`, etc.).

---

## Files

```
index.html          semantic HTML shell — structure, meta, OG, JSON-LD
styles.css          design system & all styling (tokens, layout, components)
throne.js           Floor B2: Throne Room canvas ambient (sigil ring + motes)
reliquary.js        Floor B4: Valence Flip + The Flatlander interactive demos
404.html            custom themed 404 page
CNAME               custom domain (lordai.nz) for GitHub Pages
site.webmanifest    PWA manifest
sitemap.xml         sitemap for search engines
robots.txt          robots directives (references sitemap)
favicon.svg         SVG favicon
og.png              1200×630 Open Graph raster image
og.svg              source SVG for the OG image
icon-192.png        PWA icon 192×192
icon-512.png        PWA icon 512×512
apple-touch-icon.png  Apple touch icon 180×180
README.md           this file
CHANGELOG.md        audit trail of changes
```

---

🤘 *Nazarick endures.*
