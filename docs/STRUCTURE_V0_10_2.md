# Website Prototype 0.10.2 — System Narrative, Technical Diagram Grammar & Information Architecture Court

Status: **STRUCTURE LOCK / PAGE CODE UNCHANGED**

This document reorganizes the Kodo website around the new Algorithm Stack and Training Roadmap materials. It does **not** treat every label, number, named library, or blocker in those diagrams as already implemented or public-release truth.

## 1. Why the information architecture changes

The current page explains Kodo mainly as:

`Build → Learning → System`

The new materials expose a more specific system narrative:

`two observation sources → shared actor representation → memory → policy → action`

plus a training progression:

`human play logs → behaviour cloning → multi-agent self-play → real-device test`

This is more informative than a generic research-area taxonomy. The website should therefore present **one engineered system with several operating regimes**, not a collection of AI topics.

## 2. Proposed public narrative

### 00 — HERO / PROJECT THESIS

Keep:

> Building agents that learn to play.

Short supporting idea:

> Kodo builds the game environment, trains agents inside it, and keeps the policy interface consistent as observation moves from simulation to the device.

Do not put detailed algorithm names in the hero.

### 01 — SYSTEM PREMISE / ONE POLICY, TWO LOOPS

Purpose: explain the key architectural idea before showing implementation detail.

Public-level message:

- simulation and device execution are different observation sources;
- the actor-facing representation is intended to stay compatible;
- training can use information that deployment cannot;
- deployment must respect what the visual pipeline can actually observe.

Suggested compact diagram:

`SIM STATE ─┐`
`           ├→ OBSERVATION → ENCODER → MEMORY → POLICY → ACTION`
`DEVICE CV ─┘`

A separate training-only branch may feed the critic, but it must be visually marked `TRAINING ONLY`.

### 02 — STACK / ALGORITHM STACK

This replaces the current generic “project layers” list as the primary technical section.

Recommended visual grammar:

- **blue** = source / environment / device endpoint
- **green** = observation / representation / encoder / memory
- **violet** = policy / action
- **amber** = training-only path or optimisation loop
- **cyan** = deploy-only path
- **red** = blockers / invalid assumptions / throw-away work

These colors are semantic and local to technical diagrams. The rest of the site remains mostly monochrome.

The diagram should be built with HTML/CSS/SVG primitives, not embedded as a screenshot, so labels and status can evolve independently.

#### Proposed stack groups

1. **Source**
   - Kodo simulation
   - device screen / visual source

2. **Actor input**
   - observation vector or observation contract

3. **Representation**
   - encoder
   - memory

4. **Policy**
   - multi-agent policy layer

5. **Action**
   - game-control action contract

6. **Training-only branch**
   - privileged critic / optimiser / replay etc. only after current architecture is confirmed

Do not publish exact dimensions, head counts, action cardinalities, library names, or hyperparameters merely because they appear in a planning diagram. They require confirmation as current architecture.

### 03 — TWO EXECUTION REGIMES

Use a split composition rather than two unrelated feature cards.

#### SIMULATION

Show the controlled training loop:

`Kodo environment → actor observation → policy → action → environment`

Possible supporting facts already confirmed elsewhere:

- core game logic implemented;
- UI implemented;
- gas system under development.

#### DEVICE / VISUAL

Show the intended device path at a higher authority-safe level:

`screen → perception → actor observation → policy → device control`

Until explicitly confirmed, CV model family and device-control library names remain architecture candidates rather than locked public facts.

### 04 — PLAN / TRAINING ROADMAP

The second uploaded diagram should become a **roadmap section**, not a status claim.

Narrative:

`Human data → Imitation → Multi-agent learning → Device testing`

Recommended representation:

- horizontal ordered stages on desktop;
- vertical sequence on mobile;
- one red `GATE` block before training stages;
- optional loop arrows only when they communicate a real dependency.

Stage labels should carry status tags such as:

`PLANNED / UNDER REVIEW / BLOCKED / ACTIVE / COMPLETE`

rather than looking equally implemented.

### 05 — GATES / WHAT MUST BE TRUE FIRST

The “GATE” idea is strong enough to become a first-class website section.

Do not immediately expose G1–G7 verbatim as public blockers without confirmation. Instead build the component contract now:

- gate id;
- short title;
- status;
- why it matters;
- affected downstream stages;
- source / as-of date.

This can later show real blockers without turning the site into a progress-bar dashboard.

### 06 — EVIDENCE / EVALUATION CONTRACT

The small numerical panels in the roadmap diagram suggest a useful future section, but the website must distinguish:

- **design target**;
- **measured result**;
- **simulation estimate**;
- **evaluation requirement**.

No naked number should be published.

Each public metric should eventually include:

`value + unit + definition + evaluation population + build/checkpoint + date + uncertainty when relevant`

Examples from the planning material (aim budget, delay sensitivity, match-count requirement, gamma/lambda) should remain non-public candidate material until their interpretation and status are confirmed.

### 07 — REAL KODO MEDIA

Real environment screenshots/video should remain the strongest visual evidence.

Recommended placement:

- one large environment capture after the system premise;
- smaller captures attached to Stack / Roadmap stages only where they genuinely document the stage;
- no decorative screenshot gallery.

The existing `media-manifest.js` truth gate remains valid.

### 08 — FOOTER / NPLUS

Keep the team identity stable and avoid a public member roster for now.

## 3. Proposed navigation

Replace:

`Build / Learning / System`

with:

`Overview / Stack / Roadmap / Status`

or, if Status remains too sparse:

`Overview / Stack / Roadmap`

“Stack” and “Roadmap” now correspond to real explanatory objects, so they are stronger navigation labels than generic research categories.

## 4. Diagram grammar mutation

Previous design constitution: one accent color maximum.

### v0.10.2 mutation

Retain one dominant page accent, **but permit a bounded semantic palette inside system diagrams only**.

Rules:

1. color must encode role, not decoration;
2. the same role always receives the same color;
3. outside diagrams, return to the monochrome Field Signal system;
4. every colored route must remain understandable without color alone;
5. training-only and deploy-only paths must also differ by line style / labels;
6. red is reserved for blockers, invalid assumptions, or discarded work—not ordinary emphasis.

This preserves the visual discipline of the current site while allowing the system diagrams to carry more information density.

## 5. Claim-authority matrix for the new materials

| Material type | Website authority now | Rule |
|---|---|---|
| Kodo / NPLUS identity | LOCKED | render normally |
| game logic + UI implemented | CONFIRMED | render normally |
| gas system in development | CONFIRMED / temporal | include as-of context when useful |
| one-policy / two-observation-source idea | ARCHITECTURE DIRECTION | may explain as design intent; do not imply deployed equivalence |
| training roadmap ordering | ROADMAP | render as plan with stage states |
| named algorithms/libraries | CANDIDATE SPEC unless reconfirmed | do not promote to current stack automatically |
| exact vector sizes / heads / action dimensions | CANDIDATE SPEC | hold from public copy until confirmed |
| G1–G7 blocker list | PLANNING ARTIFACT | componentize first; publish only after status confirmation |
| numerical targets / budgets / match counts | EVIDENCE CANDIDATE | require definition/provenance before public metric |

## 6. Homepage composition after refactor

Recommended order:

1. Hero — project thesis
2. System premise — one policy, two observation sources
3. Real Kodo media slot
4. Stack — source → observation → encoder → memory → policy → action
5. Two regimes — simulation vs device
6. Roadmap — human data → imitation → self-play → device test
7. Gates / current status
8. Evidence / evaluation notes (only when admissible data exists)
9. NPLUS footer

The old “Research Fields” and generic Observatory sections should not survive as separate top-level concepts. Their useful components can be recombined into Stack, Regimes, and Evidence.

## 7. What not to do in v0.10.2

- Do not embed the two uploaded diagrams directly into the homepage as final UI.
- Do not copy their white-slide visual style wholesale.
- Do not claim PufferRL, PPO, MAPPO, YOLOv8, Transformer, LSTM, dimensions, hyperparameters, or blocker completion states as final unless re-confirmed.
- Do not turn every system node into a rounded card.
- Do not make the site a dense architecture diagram from the first viewport.
- Do not replace real environment media with diagram decoration.

## 8. Next implementation gate

Before changing the live page, obtain one lightweight architecture confirmation from the project lead:

- Which labels in the two diagrams are **current decisions**?
- Which are **under review / proposed**?
- Which blockers are **current** versus illustrative?
- Are exact dimensions/hyperparameters intended to be public?

After that confirmation, v0.10.3 can refactor the actual homepage without authority drift.
