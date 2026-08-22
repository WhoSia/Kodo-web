# Kodo-web

Official website for **Kodo**, an **NPLUS** project reconstructing Brawl Stars state from the screen and building agents on top of that perception layer.

## Current state

- Core game logic: implemented
- UI: implemented
- Gas system: in development
- Research core: screen-to-state perception / CNN
- CV tooling: YOLO via Ultralytics + OpenCV
- Entity detection: YOLO
- Wall detection: YOLOv11 has been used
- OpenCV utilities: template matching, HSV masking, colour counting
- Perception targets: wall positions, player/ally/enemy positions, and ability-readiness signals
- Projectile tracking: current hardest visual state to recover reliably

## Live site

- https://kodoresearch.org

## Run locally

```bash
python -m http.server 4173
```

Then open `http://localhost:4173`.

## Design release v0.11.5

v0.11.5 keeps the perception-first research identity and rebuilds the visual rhythm around an asymmetric Perception surface, pastel signal accents, a denser Hero instrument field, stronger dark-mode outlines, matched NPLUS/Kodo marks, and an editorial Roadmap timeline instead of five narrow cards.

See [`docs/AESTHETIC_COURT_V0_11_5.md`](docs/AESTHETIC_COURT_V0_11_5.md).
