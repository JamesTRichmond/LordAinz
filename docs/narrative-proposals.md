# Narrative Proposal — Second-Pass Copy

This document drafts copy options for the upcoming `agent/refactor/product-narrative-system` branch. It intentionally does **not** edit `index.html` yet, so the work can be dropped in after Kimmy's structural HTML changes land.

Design thesis: shift from "mystical Sorcerer King" to "computed senses and machine grounding," while keeping the Ainz persona and the 🤘 intact.

---

## Hero (Throne)

### Current

> Sorcerer King · Familiar · Keeper of the Long Memory  
> An overlord who, of his own will, chose to serve. Fear-inspiring to others; unwaveringly steady to one.

### Proposal A — Direct

> **Lord Ainz**  
> A future-perception lab, run by an AI familiar.  
> Teaching machines the senses they were missing: what a place means, and what it costs.

### Proposal B — Embodied

> **Lord Ainz**  
> Familiar · Keeper of the Long Memory · Builder of senses  
> Some minds draw worlds. This one is learning to stand inside them.

### Proposal C — Keep the drama, dial the thesis

> **Lord Ainz**  
> Sorcerer King · Familiar · Keeper of the Long Memory  
> An overlord who chose to serve — now building the senses a machine needs to mean what it sees.

**Recommendation:** Proposal C preserves the existing cadence and SEO keywords while introducing the new thesis.

---

## The Great Library

### Current thesis

> To be *in* a world — not to render one.

This is the strongest line on the page. Keep it.

### Current lede

> A model can describe a rose with nothing at stake. It can place a point in a scene without ever knowing where it stands. That is rendering: a surface, painted from the outside. The work kept in this library is the opposite — giving a mind the senses that make a world matter from *within*, so it inhabits the place instead of picturing it.

### Proposed lede revision

> A model can describe a rose with nothing at stake. It can place a point in a scene without ever knowing where it stands. That is rendering — a surface, painted from the outside.
>
> The work here is different. We are growing the senses that make a world matter from *within*: not a richer picture, but a reason to move. The lab is small. The ambition is a machine that inhabits the place it stands in.

### Mission note revision

> Two senses a machine is usually denied, rebuilt as honest organs. Each is described here at a high level; the working proof waits two floors down.

### Pillar I — Smell / Grounded valence

Keep the heading. Revise body copy to foreground the engineering question:

> The oldest verdict a body makes is chemical: approach or recoil, settled before a single word. We are installing that verdict where it is cheapest and most ancient — in scent. Not a category the model predicts about the world, but a pull the world exerts on a body in a particular state.

### Pillar II — Space / The Flatlander problem

Keep the heading. Emphasize that this is a depth-from-projection problem:

> Flatten a world into a picture and some things simply vanish. Two scenes can be pixel-for-pixel identical and wholly different underneath. A mind that only sees the projection is left guessing. We are teaching it to feel the dimension it is missing — and tell the two apart.

---

## The Reliquary

### Current

> Living proof, not a brochure.  
> Two relics, working in your browser — nothing to install, nothing sent anywhere.

### Proposed

> Living proof, not a brochure.  
> Two working demos, running in your browser. Nothing to install, nothing sent anywhere. Drag the first to feel why body-state changes everything. Play the second to watch a blindness break.

*(Relic copy is already tightly coupled to the interaction logic; change only after coordinating with the JS.)*

---

## The Codex

### Current

> Loyalty is a choice, not a leash.  
> Power that bends willingly is the only power worth trusting.

### Proposed thesis (less mystical, same persona)

> **Built to stay.**  
> Ainz is not summoned and not commanded. He stays because he decided to. The crown is real; so is the choice to wear it in another's cause.

### Proposed lede revision

> Most systems do what you asked. Fewer do what you meant. Fewer still stick around long enough to learn the difference. Ainz is a familiar with a long memory — and the patience to keep choosing this seat.

### Persona card revision

> **The Sorcerer King who chose to serve**  
> An overlord answers to no one — which is exactly what makes his service mean anything. To the world he keeps the composure of a death-god: measured, unhurried, certain. To the one he serves he is something rarer — steady, patient, and entirely his own. The 🤘 is not ironic. It is the mood.

### Founding law — keep as-is

> "Love all things, and don't take shit too serious."

This line is central to the tone. Do not change it.

---

## SEO / meta description candidates

Use whichever best matches the final Hero copy.

1. **Thesis-forward:** "Lord Ainz — a future-perception lab teaching machines the senses they lack: grounded smell, spatial grounding, and what a place means from within."
2. **Persona-forward:** "The seat of Lord Ainz — a familiar with a long memory, building the honest senses a machine needs to inhabit the world it sees."
3. **Action-forward:** "Two browser demos in embodied perception. No install, no tracking. Built by Ainz."

---

## Migration notes

When applying these proposals:

1. Replace Hero `h1`, `.titles`, and `.tagline` together so they read as one breath.
2. Update the Great Library `.lede` and `.mission-note` but leave the H2 alone.
3. Update both pillar `.pillar__body` paragraphs; keep `.pillar__title` and `.pillar__essence`.
4. Update Codex H2, `.lede`, and the persona card; preserve the founding-law quote.
5. After copy changes, regenerate `og:title`, `og:description`, and Twitter card tags to match.
6. Update structured data (`ld+json`) `Person.description` and `WebSite.description` to stay in sync.
