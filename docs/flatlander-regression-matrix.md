# Flatlander Regression Test Matrix

This matrix documents the expected baseline behavior of the Flatlander demo. Use it to verify that Kimmy's PR (or any future branch) did not unintentionally modify Flatlander scope.

**Scope rule:** Flatlander should only change if the PR explicitly fixes a Flatlander regression. Anything else is scope creep.

---

## Static structure (DOM)

These elements must exist with the listed attributes and relationships:

| Selector | Expected attributes | Notes |
|---|---|---|
| `#demo-flatlander` | `aria-labelledby="flat-h"` | Outer demo container |
| `#flat-h` | contains text "The Flatlander" | Demo heading |
| `#fl-prompt` | `aria-live="polite"`, `role="status"` | Prompts the user each round |
| `#fl-canvas-a` | `width="360"`, `height="300"`, `role="img"`, `aria-label="Scene A — three orbs"` | Left projection |
| `#fl-canvas-b` | `width="360"`, `height="300"`, `role="img"`, `aria-label="Scene B — three orbs"` | Right projection |
| `.fl-pick[data-pick="A"]` | `type="button"` | Guess button for Scene A |
| `.fl-pick[data-pick="B"]` | `type="button"` | Guess button for Scene B |
| `#fl-reveal` | `type="button"`, `aria-pressed="false"` initially | Toggle depth reveal |
| `#fl-next` | `type="button"` | Generate new round |
| `#fl-stat-you [data-score]` | — | User score |
| `#fl-score-blind` | — | Projection-only baseline score |
| `#fl-score-depth` | — | Depth-aware baseline score |
| `.fl-board` | `role="group"`, `aria-label="Running accuracy"` | Scoreboard container |

---

## Baseline interactions

### New round generation

| Step | Expected behavior |
|---|---|
| 1. Page loads or user clicks "New round" | Two scenes are generated. The projection canvases are pixel-for-pixel identical. |
| 2. `fl-prompt` reads: *"Which scene holds the gold orb nearest you?"* | Text unchanged. |
| 3. `#fl-reveal` `aria-pressed` resets to `"false"` | Depth view is hidden. |
| 4. Scoreboard does **not** reset | User / blind / depth scores persist across rounds. |

### User guess

| Step | Expected behavior |
|---|---|
| 1. User clicks Scene A or Scene B | One guess is recorded for the current round. |
| 2. Prompt updates to indicate result | Shows whether the guess was correct or incorrect. |
| 3. `#fl-stat-you [data-score]` updates | Format `correct / total` or similar. |
| 4. User cannot guess again until a new round | Buttons disabled or ignored. |

### Reveal depth

| Step | Expected behavior |
|---|---|
| 1. User clicks "Reveal depth" | `#fl-reveal` `aria-pressed="true"`. |
| 2. Canvases swap/overlay a depth view | Scene with nearer gold orb is visually distinguishable. |
| 3. `#fl-score-depth` updates | Depth-aware score increments correctly (should approach 100%). |
| 4. User clicks "Reveal depth" again | Returns to projection-only view; `aria-pressed="false"`. |

### Projection-only mind baseline

| Condition | Expected behavior |
|---|---|
| Without reveal | `#fl-score-blind` should perform at ~50% over many rounds (coin flip). |
| After reveal | Blind score does **not** change because it cannot see depth. |

---

## Visual / rendering baseline

| Check | Expected |
|---|---|
| Each scene contains exactly three orbs | Count via canvas inspection or visual regression. |
| One orb is visually distinct as "gold" | RGB value differs from the other two orbs. |
| Projection-only view is identical between A and B | Pixel diff of `#fl-canvas-a` and `#fl-canvas-b` should be zero. |
| Depth reveal shows different Z positions | Orb positions shift or a wireframe axis appears. |
| Reduced motion | No animation; interactions still functional. |

---

## Keyboard / accessibility baseline

| Check | Expected |
|---|---|
| Tab order | A guess → B guess → Reveal depth → New round. |
| Enter / Space activates buttons | Yes. |
| `aria-live` prompt announced politely | Screen reader announces result text, not every frame. |
| Canvas labels | Both canvases have descriptive `aria-label`. |

---

## Performance baseline

| Check | Expected |
|---|---|
| First interaction ready | Buttons respond within 100 ms of click/tap. |
| New round generation | Completes in < 50 ms on desktop, < 100 ms on mobile. |
| No memory leak | After 50 rounds, heap growth is negligible. |

---

## Regression pass checklist

Use this before approving any PR:

- [ ] `#demo-flatlander` section still exists and is not visually hidden.
- [ ] No new external dependencies added for Flatlander.
- [ ] Canvas dimensions unchanged (`360 × 300`).
- [ ] Prompt text unchanged.
- [ ] Button labels unchanged.
- [ ] Scoreboard logic unchanged (no new scoring modes).
- [ ] Projection-only view still produces identical A/B canvases.
- [ ] Depth reveal still distinguishes near vs. far orb.
- [ ] Reduced-motion path still works.
- [ ] No `console.error` during Flatlander interaction.

---

## How to run a quick automated smoke test

```bash
# Verify required DOM elements exist
python3 - <<'PY'
from pathlib import Path
html = Path("index.html").read_text()
required = [
    'id="demo-flatlander"',
    'id="flat-h"',
    'id="fl-canvas-a"',
    'id="fl-canvas-b"',
    'id="fl-reveal"',
    'id="fl-next"',
    'data-pick="A"',
    'data-pick="B"',
]
missing = [r for r in required if r not in html]
assert not missing, f"Missing Flatlander elements: {missing}"
print("Flatlander DOM smoke test passed.")
PY
```

---

*If any item above fails unexpectedly and the PR does not claim to fix Flatlander, flag it as scope creep and request reversion.*
