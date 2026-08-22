# Kodo-web

Official website for **Kodo**, an **NPLUS** project building a controllable Brawl Stars environment and training agents inside it.

## Current state

- Core game logic: implemented
- UI: implemented
- Gas system: in development
- CV tooling: YOLO via Ultralytics + OpenCV
- Entity detection: YOLO
- Wall detection: YOLOv11 has been used
- OpenCV utilities: template matching, HSV masking, colour counting
- Perception targets: walls, players/allies/enemies, and ability-readiness signals
- Projectile tracking: current visual-perception frontier

## Live site

- https://kodoresearch.org

## Run locally

```bash
python -m http.server 4173
```

Then open `http://localhost:4173`.

## Add real Kodo media

1. Put approved media in `assets/`.
2. Update `media-manifest.js` and switch the slot from `conceptual` to `real`.
3. Add a useful alt description and caption.

See [`docs/MEDIA_INTAKE.md`](docs/MEDIA_INTAKE.md).

## Release v0.10.6

This release integrates the Kodo/NPLUS visual identity, compresses public copy, adds current perception tooling, and keeps detailed authority history behind the public surface.

See [`docs/PUBLIC_TRUTH_V0_10_6.md`](docs/PUBLIC_TRUTH_V0_10_6.md).
