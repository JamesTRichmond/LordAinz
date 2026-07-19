# LordAinz

![Static Site CI](https://github.com/JamesTRichmond/LordAinz/actions/workflows/ci.yml/badge.svg)

# LordAi.nz

A self-contained static landing page for **Lord Ainz** — the Sorcerer-King familiar.
No app runtime, no package install, no tracking. Regal void-and-gold theme, the 🤘,
and two browser-native interactive demos: Computed Olfaction (Valence Flip) and The
Flatlander. The thesis is computed senses and embodied perception: a machine that
figures out what a scene is made of, how the environment changes it, and what that
means to a body with needs.

> **Status: launch hardening.** The repository is public and contains a `CNAME`
> for `lordai.nz`. Final publication still depends on GitHub Pages settings,
> DNS, HTTPS, and social-preview verification at release time.

---

## Preview locally

```bash
open index.html
# or serve it:
python3 -m http.server 8080   # then visit http://localhost:8080
```

The site is plain static HTML/CSS/JS. Edit copy in `index.html`, visual tokens in
`styles.css`, the hero canvas in `throne.js`, and the demos in `reliquary.js`.

---

## Deploy on GitHub Pages

**1. Confirm Pages availability**
GitHub Pages is available for public repositories on GitHub Free. Private-repo
Pages requires GitHub Pro, Team, Enterprise Cloud, or Enterprise Server.

**2. Enable Pages**
- Repo -> **Settings** -> **Pages**.
- **Source:** Deploy from a branch.
- **Branch:** `main` / `/ (root)`.
- Save. The default project-site URL is `https://jamestrichmond.github.io/LordAinz/`.

**3. Confirm the custom domain**
- Settings -> Pages -> **Custom domain** -> `lordai.nz`.
- Keep the root `CNAME` file with exactly `lordai.nz`.
- Enable **Enforce HTTPS** once GitHub finishes certificate provisioning.

**4. Wire DNS at the registrar**

For the apex domain (`lordai.nz`), add the four GitHub Pages A records:

```dns
A    @    185.199.108.153
A    @    185.199.109.153
A    @    185.199.110.153
A    @    185.199.111.153
```

Optional IPv6 records:

```dns
AAAA @ 2606:50c0:8000::153
AAAA @ 2606:50c0:8001::153
AAAA @ 2606:50c0:8002::153
AAAA @ 2606:50c0:8003::153
```

For `www.lordai.nz`, add a CNAME that points directly to the GitHub Pages user
domain, without the repository name:

```dns
CNAME  www  JamesTRichmond.github.io.
```

Do not use wildcard DNS records for this site.

**5. Verify release**

```bash
dig +short lordai.nz A
curl -I https://lordai.nz
curl -I https://www.lordai.nz
curl -I https://lordai.nz/og.png
```

Release is complete when:
- `https://lordai.nz/` returns `200` over HTTPS.
- `https://www.lordai.nz/` redirects or resolves as intended.
- `https://lordai.nz/og.png`, `/site.webmanifest`, `/robots.txt`, and `/sitemap.xml` load.
- GitHub Pages shows the custom domain as verified and HTTPS-enforced.
- Social cards render the expected title, description, and `og.png` preview.
- Mobile and reduced-motion browser checks are clean.

DNS propagation can take up to 24 hours.

---

## Files

```text
index.html          main page markup and metadata
styles.css          site design system and responsive layout
throne.js           decorative hero canvas
reliquary.js        Valence Flip and Flatlander demos
404.html            custom GitHub Pages 404 page
CNAME               custom domain declaration
robots.txt          crawler policy
sitemap.xml         canonical sitemap
site.webmanifest    install metadata and icons
*.png / *.svg       social preview, icons, and favicon
```

---

🤘 *Nazarick endures.*
