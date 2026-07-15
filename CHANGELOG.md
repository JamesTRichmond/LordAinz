# Changelog

## [Unreleased]

### CI: JS Syntax Check (2026-07-15)

#### ✅ Completed
- Added **JS syntax validation** step to `Static Site CI` workflow.
  - Runs `node --check` on `throne.js` and `reliquary.js` after HTML validation.
  - Catches parse errors and reserved-word violations before deployment.

### Docs: README refresh (2026-07-15)

#### ✅ Completed
- Updated `README.md` to reflect current project state:
  - Status: **LIVE** at [lordai.nz](https://lordai.nz) (was "STAGED, NOT DEPLOYED").
  - Corrected CSS variables reference — properties live in `styles.css`, not inline.
  - Expanded the Files section to document every file in the repo.
  - Removed now-obsolete deploy/DNS setup instructions.

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

