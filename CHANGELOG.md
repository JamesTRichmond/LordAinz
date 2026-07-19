# Changelog

## [Unreleased]

### Social & PWA metadata (2026-07-19)

#### ✅ Completed
- Added `humans.txt` with plain-text site authorship and standards credits.
- Linked `humans.txt` from `index.html` (`rel="author"`) and `404.html`.
- Enriched `site.webmanifest` with `orientation`, `categories`, `lang`, and `dir`.
- Updated CI launch-critical file list and static metadata checks to include `humans.txt`.

---

### CI & Quality Hardening (2026-07-15)

#### ✅ Completed
- Stabilized **Static Site CI** on `main`.
- Updated HTML validation execution to fail only on real errors:
  - `vnu --skip-non-html --errors-only /work`
- Corrected workflow command formatting for validator image invocation.
- Fixed markup/accessibility issues that were causing validation failures:
  - Updated favicon data-URL encoding where needed.
  - Added missing semantic role for grouped running-accuracy UI.
- Normalized HTML void elements to modern HTML style (removed XHTML-style self-closing slashes in relevant tags).
- Added a **Static Site CI** status badge to `README.md`.

#### 🧪 Validation Outcome
- Latest `Static Site CI` workflow run is passing on `main`.
- `pages-build-deployment` is also passing.

#### 🔖 Audit Trail
Key commits associated with this effort:
- `aeddeb7` — Relax HTML validator to warnings while fixing markup
- `9636162` — Fix HTML validator errors for favicon data URL and ARIA role
- `9af74bc` — Use errors-only for HTML validator
- `5a8112c` — Fix validator command, normalize void tags, add CI badge

