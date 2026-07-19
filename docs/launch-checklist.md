# Launch QA Checklist — LordAi.nz

Use this checklist before calling the site "released." Each section is designed to be run in isolation, so QA can be split across devices or team members without losing context.

## How to use this list

- Check off only what you have personally verified.
- Attach screenshots or notes for any item that fails or feels off.
- If an item is blocked by DNS, Pages build, or asset caching, mark it **blocked** and note the dependency.

---

## 1. Baseline environment

- [ ] Site loaded from canonical URL: `https://lordai.nz/`
- [ ] HTTPS enforced and `http://lordai.nz/` redirects to HTTPS
- [ ] No console errors on first load (DevTools → Console)
- [ ] No console errors after interacting with both demos
- [ ] Favicon renders in browser tab
- [ ] Manifest loads and returns valid JSON (`/site.webmanifest`)
- [ ] Robots.txt and sitemap.xml load without 404
- [ ] Canonical URL in `<head>` matches final production domain

---

## 2. Desktop viewport (≥ 1280 px, Chromium / Safari / Firefox)

### Layout

- [ ] Hero fills viewport without horizontal scroll
- [ ] Nav stays fixed at top; brand + links do not wrap
- [ ] Skip-link is visible on first Tab and jumps to `#library`
- [ ] Great Library pillars sit side-by-side with readable gutters
- [ ] Reliquary demo stages are centered and controls stay inside viewport
- [ ] Footer sits at bottom after all content

### Typography

- [ ] Cormorant Garamond loaded for headings (serif fallback acceptable)
- [ ] Inter loaded for body copy (sans-serif fallback acceptable)
- [ ] No `font-display` swap flash that breaks layout
- [ ] `h1` line does not wrap awkwardly at 1280 px
- [ ] Gold text remains legible against animated hero background

### Hero / Throne

- [ ] Canvas ambient animates smoothly at 60 fps
- [ ] Scroll cue is visible and pulses
- [ ] "See it work" and "The work" buttons are clickable

### Demos

- [ ] Valence Flip: slider moves smoothly; live gauge updates in real time
- [ ] Valence Flip: state-blind gauge stays frozen
- [ ] Valence Flip: caption text updates correctly at extremes
- [ ] Flatlander: Scene A and Scene B both render matching projections
- [ ] Flatlander: buttons A / B are clickable
- [ ] Flatlander: "Reveal depth" toggles the wireframe depth view
- [ ] Flatlander: "New round" generates a new pair of scenes
- [ ] Flatlander: running score updates after each guess or reveal

---

## 3. Narrow mobile viewport (≤ 390 px, iOS Safari + Android Chrome)

- [ ] No horizontal scroll on any section
- [ ] Nav collapses gracefully or wraps without overlap
- [ ] Hero text remains readable; `h1` does not overflow
- [ ] Great Library pillars stack vertically
- [ ] Demo canvases scale to fit screen width
- [ ] Valence Flip slider has a touch-friendly hit area
- [ ] Flatlander buttons are large enough to tap reliably
- [ ] Footer text wraps cleanly and stays centered

---

## 4. Reduced motion (`prefers-reduced-motion: reduce`)

- [ ] Hero canvas animation is paused or replaced with static gradient
- [ ] Scroll cue pulse is disabled
- [ ] Valence Flip gauge updates without animated transitions
- [ ] Flatlander "Reveal depth" works instantly without motion blur
- [ ] No vestibular triggers anywhere on the page

---

## 5. Social preview (cards)

- [ ] Facebook Sharing Debugger returns `200` with correct title / description / image
- [ ] Twitter Card Validator shows `summary_large_image` with `og.png`
- [ ] LinkedIn Post Inspector fetches metadata correctly
- [ ] Slack / Discord unfurl shows title, description, and thumbnail
- [ ] `og:image` URL is absolute and returns a 1200 × 630 PNG
- [ ] `og:image:alt` is descriptive and accurate

---

## 6. Accessibility

- [ ] Lighthouse Accessibility score ≥ 95
- [ ] All images / canvases have descriptive `aria-label` or `alt` text
- [ ] Focus order follows visual order
- [ ] Color contrast for body text meets WCAG AA (4.5:1)
- [ ] Gold accent text on dark backgrounds meets WCAG AA for large text (3:1)
- [ ] `aria-live` regions update politely without announcing every frame

---

## 7. SEO / metadata

- [ ] `<title>` and `<meta name="description">` match final narrative thesis
- [ ] Open Graph tags match the desired card copy
- [ ] Twitter card tags present and consistent with Open Graph
- [ ] Structured data (`ld+json`) validates in Google's Rich Results Test
- [ ] Canonical tag points to `https://lordai.nz/`

---

## 8. Demo-specific edge cases

### Valence Flip

- [ ] Slider at minimum shows revulsion / "bad-for-me"
- [ ] Slider at maximum shows craving / "good-for-me"
- [ ] Midpoint copy is ambiguous as intended
- [ ] Caption resets if the slider is released mid-drag

### The Flatlander

- [ ] Projections can be identical by design
- [ ] Correct answer is not guessable from the image alone
- [ ] Reveal depth clearly distinguishes near vs. far orb
- [ ] Score resets to `0 / 0` after a new round only when expected
- [ ] Keyboard-only users can operate all controls

---

## 9. Final release checks

- [ ] `https://www.lordai.nz/` redirects or resolves as intended
- [ ] `dig +short lordai.nz A` returns four GitHub Pages IPs
- [ ] `curl -I https://lordai.nz/og.png` returns `200`
- [ ] Custom domain in GitHub Pages shows **Verified**
- [ ] **Enforce HTTPS** is enabled in Pages settings
- [ ] CHANGELOG.md updated with release date
- [ ] This checklist is archived under `docs/launch-checklist-completed-YYYY-MM-DD.md`

---

*End state: every box is checked, or every unchecked box has a blocker ticket.*
