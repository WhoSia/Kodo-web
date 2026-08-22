# Website Prototype 0.10.4 — Audit

Status: **PASS — PUBLIC NARRATIVE CALIBRATED / INTERNAL AUTHORITY GATE RETAINED**

## Design court

- Hero keeps `Building agents that learn to play.`
- `Colt` is removed from hero metadata and reframed later as `FIRST TARGET / COLT`.
- Public copy no longer repeats audit-language such as `not locked`, `under review`, `withheld`, `public simplification`, `authority basis`, or `conceptual fallback`.
- The lower-page ambition section states direction rather than achieved capability: master the loop → widen the game → close the simulator/device gap.

## Technical narrative

Public sequence:

`Environment → shared actor loop → human play → imitation → multi-agent learning → device loop`

The homepage describes roles rather than publishing candidate library/model choices. Exact stack details remain governed by `ARCHITECTURE_AUTHORITY_V0_10_3.md` and `TECHNICAL_NARRATIVE_V0_10_4.md`.

## Real-media integration

- The hero remains the primary real-Kodo media landing zone.
- Current mode stays `conceptual` in `media-manifest.js`.
- Visible fallback language is reduced to `SYSTEM SCHEMATIC` and a neutral system-view caption.
- A later approved Kodo capture can replace the schematic without changing page composition.

## Release gate

`python tools/check_site.py` → `SITE_GATE=PASS`

Checks include:

- exact `Kodo` casing;
- no `PROJECT X`;
- no Colt in the hero;
- Colt ambition section present;
- Overview / Stack / Roadmap / Progress navigation;
- candidate algorithm/library/detail leakage blocked;
- defensive public-language gate;
- media manifest and slot present;
- `part-6.css` + `part-7.css` loaded;
- authority docs present;
- duplicate IDs absent.

## Runtime court

Chromium layout validation was run without generating screenshots.

- 1440 CSS px: no document horizontal overflow
- 820 CSS px: no document horizontal overflow
- 390 CSS px: no document horizontal overflow
- mobile menu: PASS
- `aria-expanded` state: PASS
- reduced-motion browser mode: PASS
- conceptual media fallback visible while real-media element remains hidden: PASS
- console errors: none

## Authority court

Public HTML still excludes candidate specifics such as PufferRL, MAPPO, YOLOv8, Transformer, LSTM, observation/critic dimensions, action cardinalities, and detailed blocker IDs. The more confident public rhetoric therefore does **not** constitute an authority upgrade of those implementation details.
