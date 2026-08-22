# Kodo v0.10.6 — Public Truth Seal

## Current public claims

- Team: **NPLUS**
- Project: **Kodo**
- Core game logic: implemented
- UI: implemented
- Gas system: in development
- Current CV tooling: **YOLO via Ultralytics** and **OpenCV**
- YOLO is used for entity detection; wall detection has used YOLOv11.
- OpenCV is used for template matching, HSV masking and colour counting.
- CV outputs currently discussed by the implementation team include wall positions, player/ally/enemy positions, and readiness signals for super/gadget/hypercharge.
- Projectile tracking is reported by the CV implementer as extremely difficult from computer vision. The public page describes it as the current perception frontier rather than claiming complete projectile-state recovery.

## Public copy rule

The homepage leads with what Kodo builds, what currently works, and where it is going. Internal authority bookkeeping remains in repository documentation and release checks rather than being repeated in user-facing copy.

## Release method

This release applied three Workshop methods without writing any Kodo record back into Notion:

1. **Writing Inside the Research Loop** — attack the sentence and remove copy that weakens or overstates the project.
2. **Explanandum Lock Before Explanation** — explain the public system and observed implementation state; do not turn candidate architecture into fact.
3. **Preserve Historical Private Receipts; Audit Public Surfaces** — keep detailed history in the repo while auditing only the current public surface for release.
