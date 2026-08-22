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

## Design release v0.11.3

This release removes the public GitHub CTA, moves the Kodo crest into the top navigation, replaces the large Hero logo with a square system-field visual, strengthens dark-mode card outlines, constrains the Roadmap width, and shifts the System section toward an open schematic.

See [`docs/AESTHETIC_COURT_V0_11_3.md`](docs/AESTHETIC_COURT_V0_11_3.md).
