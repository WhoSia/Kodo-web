# Website Prototype 0.11.6 — Perception-to-Field Narrative Release

Status: `PUBLIC-COPY + COMPOSITION UPDATE / SOURCE-GROUNDED / LIVE-DEPLOYMENT-UNVERIFIED`

## Authority boundary
- Kodo is an NPLUS website/product surface. The official site should not borrow results of unrelated developers as implemented Kodo achievements.
- AngelFire [PYLA], 2026-08-22: describes YOLO through Ultralytics (v8 entities, v11 walls) and OpenCV template matching/HSV/color-counting as *their* working CV implementation; ability readiness, wall and player positions reported as candidate recoverable signals. Projectile detection is difficult and HP was not implemented in that account. These statements do not establish the Kodo repo's CV model versions.
- Sean, 2026-08-24: Kodo aims at self-play training, a service for high-level players, and eventual real-world deployment. These are project intentions, not shipped service features.
- AngelFire, 2026-10-08–09: a separate experimental offline-game reverse-engineering/Rust/Python bridge/PPO pipeline was described; simulation lacked real-world frame and input latency, and later simulated lag was being explored. Do not promote this experiment to a verified Kodo implementation.
- 2026-09-09–2026-10-06: project activity was delayed and then resumed; no new benchmark metrics were supplied.

## Actual release changes
1. Retains existing 0.11.5 split hero, branding, dual themes, asymmetric Perception cards and five-stage editorial timeline.
2. Tightens public copy toward perception, state recovery, self-play and the simulation-to-device gap.
3. Adds a deliberately compact editorial section: **FIELD CONDITIONS / NEXT CHALLENGE** with **MECHANICS / TIMING / TRANSFER**.
4. Uses future-oriented research verbs for unimplemented field transfer; publishes no invented FPS, precision/recall, win rate or response-time numbers.
5. Loads `styles/part-14.css` with narrow-screen reflow; no new images or fonts.

## Verification
GitHub source-level gate: PASS — `real-world` section present, stylesheet imported, mobile breakpoints present, existing 5 roadmap stages preserved, brand assets kept, public model-version ambiguity avoided.
Runtime visual browser gate: NOT RUN in this release.
Live Cloudflare production SHA/DNS gate: NOT VERIFIED by GitHub source inspection.

## Next
Await directly verified project screenshots, model evaluation and end-to-end latency measurements before making claims about achieved live-agent performance. The earlier Research OS long-form Kodo-web genealogy remains DEFERRED pending an actual conversation-archive Markdown file.
